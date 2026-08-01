# -*- coding: utf-8 -*-
import os as _os; _os.chdir(r'C:\Users\Rowan\scenario-automation\projects\16_moses')
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from docx import Document
d = Document(r"C:\Users\Rowan\scenario-automation\projects\16_moses\내 남편은 거지 모세_1-21화 수정 지시서_v3.docx")
tot = 0
for t in d.tables:
    hdr = [c.text for c in t.rows[0].cells]
    if hdr[:1] == ['단락'] or (len(hdr) == 3 and hdr[1] in ('지금', '찾을 말')):
        n = len(t.rows) - 1
        tot += n
        print(f'  {hdr} → {n}')
print('교체 지시 행 합계:', tot)
