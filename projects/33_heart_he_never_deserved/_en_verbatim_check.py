# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
raw = open('reference/He_Broke_the_Heart_That_Saved_Him_EP01-EP52_English_Production_Script.md', encoding='utf-8').read()
norm = lambda s: re.sub(r'\s+', ' ', s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
rawn = norm(raw)
t = open('33_heart_he_never_deserved_paid_11-50_v1.md', encoding='utf-8').read()
cur=None; bad=0; tot=0
for l in t.split('\n'):
    m = re.fullmatch(r'(\d+)화', l.strip())
    if m: cur=m.group(1)
    for q in re.findall(r'— "(.+?)"\s*$', l):
        tot+=1
        frags = [norm(f) for f in q.split(' / ')]
        miss = [f for f in frags if f and f not in rawn]
        if miss:
            bad+=1; print(f'{cur}화 [{l[:6]}] MISSING: {miss}')
print(f'quotes {tot} · with missing fragments {bad}')
