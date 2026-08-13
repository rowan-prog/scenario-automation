# -*- coding: utf-8 -*-
"""추출본 정리(zero-width 제거) + 기계 계측."""
import os, re, unicodedata, glob

SRC = r"C:\Users\Rowan\scenario-automation\projects\27_writers_room\01_source"

def clean(t):
    t = t.replace("\u200b", "").replace("\ufeff", "").replace("\xa0", " ")
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{4,}", "\n\n\n", t)
    return t

for p in sorted(glob.glob(os.path.join(SRC, "*.txt"))):
    with open(p, encoding="utf-8") as f:
        t = clean(f.read())
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)
    eps = sorted({int(m) for m in re.findall(r"(?m)^\s*(\d{1,3})\s*화\s*$", t)})
    scenes = len(re.findall(r"(?m)^\s*S\s*#", t))
    lines = t.count("\n")
    print(f"{os.path.basename(p)}: chars={len(t)} lines={lines} scenes={scenes} "
          f"eps={len(eps)} range={eps[:1]}~{eps[-1:]} missing={[i for i in range(1,(eps[-1] if eps else 0)+1) if i not in eps][:12]}")
