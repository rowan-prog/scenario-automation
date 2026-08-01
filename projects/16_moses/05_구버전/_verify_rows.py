# -*- coding: utf-8 -*-
import os as _os; _os.chdir(r'C:\Users\Rowan\scenario-automation\projects\16_moses')
"""수정 지시서 각 행의 [단락 번호] ↔ [지금 원문]이 실제 초고와 일치하는지 전수 검증."""
import io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from docx import Document

BASE = r"C:\Users\Rowan\scenario-automation\projects\16_moses" + "\\"
draft = {}
for ln in open(BASE + '03_작업파일/_draft_paras.txt', encoding='utf-8'):
    if '\t' not in ln:
        continue
    n, t = ln.rstrip('\n').split('\t', 1)
    draft[int(n)] = t


def norm(s):
    return re.sub(r'[\s△…·\.\,!\?\'"\-—/()]+', '', s)


d = Document(BASE + '내 남편은 거지 모세_1-21화 수정 지시서_v3.docx')
bad, ok, skip = [], 0, 0
for t in d.tables:
    hdr = [c.text for c in t.rows[0].cells]
    if hdr[:1] != ['단락']:
        continue
    for r in t.rows[1:]:
        num_c, old_c = r.cells[0].text.strip(), r.cells[1].text.strip()
        if old_c in ('—', '') or '삽입' in num_c or '~' in num_c or '삭제' in old_c:
            skip += 1
            continue
        m = re.match(r'^(\d+)', num_c)
        if not m:
            skip += 1
            continue
        n = int(m.group(1))
        probe = norm(old_c.split('(')[0])[:22]
        if not probe:
            skip += 1
            continue
        if n in draft and probe in norm(draft[n]):
            ok += 1
            continue
        # 근처에서 찾아보기
        found = None
        for off in range(-6, 7):
            k = n + off
            if k in draft and probe in norm(draft[k]):
                found = k
                break
        bad.append((n, found, old_c[:70]))

print(f'검증 OK {ok} / 불일치 {len(bad)} / 대상외 {skip}')
print('-' * 70)
for n, found, txt in bad:
    tag = f'→ 실제 {found}' if found else '→ 초고에서 못 찾음'
    print(f'  {n} {tag}   {txt}')
