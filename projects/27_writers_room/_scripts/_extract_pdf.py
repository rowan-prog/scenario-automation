# -*- coding: utf-8 -*-
"""PDF -> txt 추출 + 무결성 계측 (writers room 인입용).
파일명이 NFD(자소분리)인 경우가 있어 glob + 정규화 매칭으로 찾는다.
"""
import os, re, glob, unicodedata
import fitz

DL = r"C:\Users\Rowan\Downloads"
WANT = [
    ("가면 뒤 괴물 대공님의 저주", "A_kimbohyung_masked_duke"),
    ("밤마다 나를 탐하는 노예 남편", "B_joeunbyul_slave_husband"),
    ("울프스 메이트", "C_parkjuhee_wolfs_mate"),
]
OUT = r"C:\Users\Rowan\scenario-automation\projects\27_writers_room\01_source"
os.makedirs(OUT, exist_ok=True)

files = glob.glob(os.path.join(DL, "*.pdf"))
norm = {unicodedata.normalize("NFC", os.path.basename(p)): p for p in files}

for key, slug in WANT:
    hit = [p for n, p in norm.items() if key in n]
    if not hit:
        print(f"!! NOT FOUND: {key}")
        continue
    path = hit[0]
    doc = fitz.open(path)
    pages, chars, imgs = [], 0, 0
    for i, page in enumerate(doc):
        t = page.get_text("text")
        chars += len(t.strip())
        imgs += len(page.get_images(full=True))
        pages.append(f"\n<<<PAGE {i+1}>>>\n{t}")
    body = unicodedata.normalize("NFC", "".join(pages))
    with open(os.path.join(OUT, slug + ".txt"), "w", encoding="utf-8") as f:
        f.write(body)
    ko = len(re.findall(r"[가-힣]", body))
    ep = len(re.findall(r"\d{1,3}\s*화", body))
    print(f"{slug}: pages={doc.page_count} chars={chars} korean={ko} images={imgs} ep_marks={ep}")
    doc.close()
