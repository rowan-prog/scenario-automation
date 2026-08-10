# -*- coding: utf-8 -*-
import re, io, collections

p = '25_billion_dollar_reset_source_CN.md'
raw = io.open(p, encoding='utf-8').read()
lines = raw.split('\n')

# 1) 일괄치환 사고 (os -> VO / OS) 검출
bad = re.findall(r'\b[A-Za-z]*(?:VO|OS)[A-Za-z]+\b|\b[A-Za-z]+(?:VO|OS)\b', raw)
badf = [w for w in bad if w not in ('VO', 'OS')]
print('=== 영문 단어 내부 VO/OS 오염 ===')
for w, c in collections.Counter(badf).most_common(30):
    print(f'  {c:>3}  {w}')

# 2) 화별 영어 대사 / 중국어 대사 비율
ep_re = re.compile(r'^第(.+)集\s*$')
dlg_re = re.compile(r'^([A-Za-z一-鿿][^：:△\n]{0,24})[：:](.+)$')
cur = None
rows = []
for ln in lines:
    s = ln.strip()
    if ep_re.match(s):
        cur = {'en': 0, 'cn': 0}
        rows.append(cur)
        continue
    if cur is None or s.startswith('△') or s.startswith('（') or s.startswith('('):
        continue
    m = dlg_re.match(s)
    if not m or m.group(1).strip() in ('人物',):
        continue
    body = m.group(2)
    han = len(re.findall(r'[一-鿿]', body))
    lat = len(re.findall(r'[A-Za-z]', body))
    if lat > han * 2:
        cur['en'] += 1
    else:
        cur['cn'] += 1
print('\n=== 화별 대사 언어 (EN / CN) ===')
for i, r in enumerate(rows, 1):
    print(f'EP{i:<3} EN={r["en"]:<3} CN={r["cn"]:<3}', end='   ')
    if i % 4 == 0:
        print()
print()
print('총 EN 대사:', sum(r['en'] for r in rows), '/ 총 CN 대사:', sum(r['cn'] for r in rows))
first_cn_only = next((i for i, r in enumerate(rows, 1) if r['en'] == 0 and r['cn'] > 0), None)
print('EN 대사 0인 첫 화:', first_cn_only)

# 3) Attempt / PROGRESS 카운터 전수
print('\n=== Attempt / 次 카운터 ===')
for i, ln in enumerate(lines, 1):
    if re.search(r'Attempt|Ready：|第\s*\d+\s*次|\d+\s*次(失败|失敗)|\d+ (times|failures)|PROGRESS|Reset\]', ln):
        print(f'{i:>5}: {ln.strip()[:110]}')
