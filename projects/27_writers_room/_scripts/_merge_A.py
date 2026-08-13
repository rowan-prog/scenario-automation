# -*- coding: utf-8 -*-
"""A 전사 조각 6개 병합 + 무결성 계측(페이지 연속성·화 번호 결번)."""
import os, re, unicodedata

SRC = r"C:\Users\Rowan\scenario-automation\projects\27_writers_room\01_source\A_chunks"
DST = r"C:\Users\Rowan\scenario-automation\projects\27_writers_room\01_source\A_kimbohyung_masked_duke.txt"

parts = []
for i in range(1, 7):
    p = os.path.join(SRC, f"A_part{i}.txt")
    with open(p, encoding="utf-8") as f:
        parts.append(f.read().strip("\n"))

body = unicodedata.normalize("NFC", "\n\n".join(parts))
body = body.replace("\u200b", "").replace("\xa0", " ")
with open(DST, "w", encoding="utf-8") as f:
    f.write(body + "\n")

pages = [int(m) for m in re.findall(r"<<<PAGE (\d+)>>>", body)]
missing_pg = [i for i in range(1, 109) if i not in pages]
dup_pg = sorted({p for p in pages if pages.count(p) > 1})
eps = sorted({int(m) for m in re.findall(r"(?m)^\s*[<\[]?\s*(\d{1,3})\s*화\s*[>\]]?\s*$", body)})
missing_ep = [i for i in range(1, (eps[-1] if eps else 0) + 1) if i not in eps]
scenes = len(re.findall(r"(?m)^\s*S\s*#", body))
unread = body.count("[판독불가]")

print(f"chars={len(body)}")
print(f"pages={len(pages)}/108 missing={missing_pg} dup={dup_pg}")
print(f"eps={len(eps)} range={eps[:1]}~{eps[-1:]} missing_ep={missing_ep}")
print(f"scenes={scenes} 판독불가={unread}")
print("->", DST)
