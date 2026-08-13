# -*- coding: utf-8 -*-
"""스캔본 A(가면 뒤 괴물 대공님의 저주) 108p 전량 PNG 렌더 — 비전 전사용."""
import fitz, glob, os, unicodedata

DL = r"C:\Users\Rowan\Downloads"
p = [f for f in glob.glob(os.path.join(DL, "*.pdf"))
     if "가면 뒤" in unicodedata.normalize("NFC", os.path.basename(f))][0]
out = r"C:\Users\Rowan\scenario-automation\projects\27_writers_room\01_source\A_pages"
os.makedirs(out, exist_ok=True)

d = fitz.open(p)
for i, pg in enumerate(d):
    dst = os.path.join(out, f"A_p{i+1:03d}.png")
    pg.get_pixmap(dpi=120).save(dst)
print("rendered", d.page_count, "->", out)
