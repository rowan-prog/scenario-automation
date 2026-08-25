# -*- coding: utf-8 -*-
"""최종 대본 docx -> txt. 변경이력 수락(w:ins 채택 / w:del 제거) + 표 + 텍스트박스 포함.
사용: python _extract_final.py <src.docx> <out.txt>
"""
import sys, io, zipfile, re
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def q(t): return '{%s}%s' % (W, t)

src, out = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)
names = [n for n in z.namelist()]
xml = z.read('word/document.xml')
root = etree.fromstring(xml)

# 통계
n_ins = len(root.findall('.//' + q('ins')))
n_del = len(root.findall('.//' + q('del')))
n_cmt = 1 if 'word/comments.xml' in names else 0

def para_text(p):
    """문단 텍스트: w:del 하위 텍스트 제외, w:ins 포함, 텍스트박스는 별도 수집"""
    parts = []
    for node in p.iter():
        tag = node.tag
        if tag == q('t'):
            # 조상에 w:del 있으면 스킵
            anc = node.getparent()
            skip = False
            while anc is not None and anc is not p:
                if anc.tag == q('del'):
                    skip = True
                    break
                if anc.tag == q('txbxContent'):
                    skip = True
                    break
                anc = anc.getparent()
            if not skip:
                parts.append(node.text or '')
        elif tag == q('tab'):
            parts.append('\t')
        elif tag == q('br'):
            parts.append('\n')
    return ''.join(parts)

def txbx_texts(el):
    res = []
    for tb in el.findall('.//' + q('txbxContent')):
        for tp in tb.findall('.//' + q('p')):
            t = ''.join(n.text or '' for n in tp.findall('.//' + q('t')))
            if t.strip():
                res.append('[TXBX] ' + t)
    return res

lines = []
tbl_count = 0
txbx_count = 0
body = root.find(q('body'))

def walk_block(el, depth=0):
    global tbl_count, txbx_count
    for child in el:
        if child.tag == q('p'):
            t = para_text(child)
            lines.append(t)
            for x in txbx_texts(child):
                lines.append(x); txbx_count += 1
        elif child.tag == q('tbl'):
            tbl_count += 1
            for tr in child.findall(q('tr')):
                cells = []
                for tc in tr.findall(q('tc')):
                    ct = []
                    for cp in tc.findall(q('p')):
                        pt = para_text(cp)
                        if pt.strip():
                            ct.append(pt.strip())
                        for x in txbx_texts(cp):
                            ct.append(x); txbx_count += 1
                    cells.append(' / '.join(ct))
                row = ' | '.join(cells)
                if row.strip(' |'):
                    lines.append('[TBL] ' + row)
        elif child.tag == q('sdt'):
            c = child.find(q('sdtContent'))
            if c is not None:
                walk_block(c, depth+1)

walk_block(body)

text = '\n'.join(lines)
open(out, 'w', encoding='utf-8').write(text)
print(f'lines={len(lines)} tables={tbl_count} txbx={txbx_count} chars={len(text)} w:ins={n_ins} w:del={n_del} comments.xml={n_cmt}')
# 화 헤더 카운트
eps = re.findall(r'^\s*(\d+)\s*화', text, re.M)
print('ep-header-hits=', len(eps))
