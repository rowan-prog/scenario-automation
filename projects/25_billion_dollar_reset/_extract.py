# -*- coding: utf-8 -*-
"""docx 완전 추출 (raw XML) — 표/텍스트박스 포함, mc:Fallback 중복 제거.
[[docx-conversion-drops-table-textbox-text]] 대응."""
import zipfile, sys, io
from lxml import etree

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
}
W = NS['w']
MC = NS['mc']

src = sys.argv[1]
out = sys.argv[2]

z = zipfile.ZipFile(src)
xml = z.read('word/document.xml')
root = etree.fromstring(xml)

def para_text(p):
    parts = []
    for node in p.iter():
        tag = etree.QName(node).localname if isinstance(node.tag, str) else ''
        ns = etree.QName(node).namespace if isinstance(node.tag, str) else ''
        if ns != W:
            continue
        if tag == 't':
            parts.append(node.text or '')
        elif tag == 'tab':
            parts.append('\t')
        elif tag == 'br':
            parts.append('\n')
        elif tag == 'cr':
            parts.append('\n')
    return ''.join(parts)

def in_fallback(el):
    a = el.getparent()
    while a is not None:
        if isinstance(a.tag, str) and etree.QName(a).namespace == MC and etree.QName(a).localname == 'Fallback':
            return True
        a = a.getparent()
    return False

lines = []
seen_ids = set()
for p in root.iter('{%s}p' % W):
    if in_fallback(p):
        continue
    lines.append(para_text(p))

with io.open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('paragraphs:', len(lines))
print('chars:', sum(len(l) for l in lines))
