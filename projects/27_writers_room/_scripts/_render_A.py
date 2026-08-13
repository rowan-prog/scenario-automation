# -*- coding: utf-8 -*-
import fitz, glob, os, unicodedata, sys

DL = r"C:\Users\Rowan\Downloads"
p = [f for f in glob.glob(os.path.join(DL, "*.pdf"))
     if "가면 뒤" in unicodedata.normalize("NFC", os.path.basename(f))][0]
d = fitz.open(p)
out = r"C:\Users\Rowan\AppData\Local\Temp\claude\C--Users-Rowan\43b5484b-d24c-4dee-a100-52835ac10b77\scratchpad"
os.makedirs(out, exist_ok=True)
dpi = int(sys.argv[1]) if len(sys.argv) > 1 else 110
pages = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [1, 2]
for n in pages:
    pg = d[n - 1]
    pg.get_pixmap(dpi=dpi).save(os.path.join(out, f"A_p{n}.png"))
    print(n, pg.rect, len(pg.get_images(full=True)))
