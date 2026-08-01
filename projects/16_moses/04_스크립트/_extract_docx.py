# -*- coding: utf-8 -*-
import os as _os; _os.chdir(r'C:\Users\Rowan\scenario-automation\projects\16_moses')
# docx -> md 추출: 본문 순서 보존, 표/텍스트박스 포함 (docx-conversion-drops-table-textbox-text 대응)
import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def para_text_with_txbx(p):
    # 일반 run 텍스트 + 문단 내 텍스트박스(w:txbxContent) 텍스트
    parts = [p.text]
    for txbx in p._element.findall('.//w:txbxContent', NS):
        for tp in txbx.findall('.//w:p', NS):
            t = ''.join(n.text or '' for n in tp.findall('.//w:t', NS))
            if t.strip():
                parts.append('[TXBX] ' + t)
    return '\n'.join(x for x in parts if x.strip()) if any(x.strip() for x in parts) else ''

def iter_block_items(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag.endswith('}p'):
            yield Paragraph(child, doc)
        elif child.tag.endswith('}tbl'):
            yield Table(child, doc)

src, out = sys.argv[1], sys.argv[2]
doc = Document(src)
lines = []
tbl_count = 0
txbx_count = 0
for block in iter_block_items(doc):
    if isinstance(block, Paragraph):
        t = para_text_with_txbx(block)
        if '[TXBX]' in t:
            txbx_count += t.count('[TXBX]')
        lines.append(t)
    else:
        tbl_count += 1
        for row in block.rows:
            cells = []
            for c in row.cells:
                ct = '\n'.join(p.text for p in c.paragraphs if p.text.strip())
                cells.append(ct)
            row_txt = ' | '.join(cells).strip()
            if row_txt.strip(' |'):
                lines.append('[TBL] ' + row_txt)

text = '\n'.join(lines)
with open(out, 'w', encoding='utf-8') as f:
    f.write(text)
print(f'paragraph-lines={len(lines)} tables={tbl_count} txbx-hits={txbx_count} chars={len(text)}')
