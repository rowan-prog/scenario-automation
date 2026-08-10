# -*- coding: utf-8 -*-
import re, io, sys, collections

p = '25_billion_dollar_reset_source_CN.md'
lines = io.open(p, encoding='utf-8').read().split('\n')

ep_re = re.compile(r'^第(.+)集\s*$')
scene_re = re.compile(r'^\s*(\d+)-(\d+)\s*(.*)$')
# 대사 라인: "이름：..." 또는 "이름（...）：..."
dlg_re = re.compile(r'^([A-Za-z一-鿿][^：:△\n]{0,24})[：:](.*)$')

eps = []
cur = None
for i, ln in enumerate(lines):
    m = ep_re.match(ln.strip())
    if m:
        cur = {'label': ln.strip(), 'start': i+1, 'lines': [], 'scenes': [], 'dlg': [], 'sd': 0}
        eps.append(cur)
        continue
    if cur is None:
        continue
    cur['lines'].append(ln)
    s = scene_re.match(ln.strip())
    if s and not ln.strip().startswith('△'):
        cur['scenes'].append(ln.strip())
    if ln.strip().startswith('△'):
        cur['sd'] += 1
    d = dlg_re.match(ln.strip())
    if d and not ln.strip().startswith('△') and not ln.strip().startswith('（') and not s:
        name = d.group(1).strip()
        if name not in ('人物',) and len(name) <= 24:
            cur['dlg'].append((name, d.group(2).strip()))

print(f"{'EP':<6}{'lines':>6}{'scenes':>7}{'△':>5}{'dlg':>5}{'chars':>7}  speakers")
tot = collections.Counter()
for k, e in enumerate(eps, 1):
    ch = sum(len(x) for x in e['lines'])
    sp = collections.Counter(n for n, _ in e['dlg'])
    for n, c in sp.items():
        tot[n] += c
    top = ' '.join(f'{n}:{c}' for n, c in sp.most_common(6))
    print(f"{k:<6}{len(e['lines']):>6}{len(e['scenes']):>7}{e['sd']:>5}{len(e['dlg']):>5}{ch:>7}  {top}")

print('\n=== 전체 화자 ===')
for n, c in tot.most_common(40):
    print(f'{c:>5}  {n}')
