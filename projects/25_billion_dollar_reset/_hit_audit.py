# -*- coding: utf-8 -*-
"""내가 25번에 쓴 잣대를 검증 히트작에 그대로 적용해본다."""
import re, io, os, collections

BASE = r'C:\Users\Rowan\scenario-automation\config\vertical_drama_hit_scripts'
FILES = [
    '(완)역대본_신의한방_01-46화.md',
    '회사도_남편도_다_내_것_01-76화.md',
    '나의_토깽이_아가씨_01-65화.md',
    '(완)역대본_거지남편아폴론_01-48화.docx',   # skip docx
    '완_나야말로이학교의퀸카_01-85화.md',
    '(완) 역대본_신부탈출기_01-90화.md',
    '지독한_사랑_01-80화.md',
    'False Weakling, True Power.역대본.md',
]

ep_re = re.compile(r'^##\s*(\d+)\s*화')
sc_re = re.compile(r'^###\s*#?\s*(\d+)')

def audit(path):
    raw = io.open(path, encoding='utf-8', errors='ignore').read()
    lines = raw.split('\n')
    eps, cur = [], None
    for ln in lines:
        s = ln.strip()
        m = ep_re.match(s)
        if m:
            cur = {'n': int(m.group(1)), 'lines': [], 'scenes': 0}
            eps.append(cur); continue
        if cur is None: continue
        if sc_re.match(s): cur['scenes'] += 1
        if s: cur['lines'].append(s)
    if not eps: return None
    chars = [sum(len(x) for x in e['lines']) for e in eps]
    scn = [e['scenes'] for e in eps]
    n = len(eps)
    first10 = sum(chars[:10]) / 10
    last10 = sum(chars[-10:]) / 10
    one_scene = sum(1 for s in scn if s <= 1)
    return dict(n=n, chars=chars, scn=scn, avg=sum(chars)//n,
                mn=min(chars), mx=max(chars), first10=int(first10),
                last10=int(last10), ratio=round(last10/first10, 2),
                one_scene=one_scene, tiny=sum(1 for c in chars if c < 900))

print(f"{'작품':<34}{'화':>4}{'평균자':>7}{'최소':>6}{'최대':>7}{'앞10평균':>8}{'뒤10평균':>8}{'뒤/앞':>7}{'씬1개화':>8}{'900자미만':>9}")
for f in FILES:
    p = os.path.join(BASE, f)
    if not os.path.exists(p) or f.endswith('.docx'):
        continue
    r = audit(p)
    if not r:
        print(f'{f[:32]:<34}  (회차 파싱 실패)')
        continue
    print(f"{f[:32]:<34}{r['n']:>4}{r['avg']:>7}{r['mn']:>6}{r['mx']:>7}{r['first10']:>8}{r['last10']:>8}{r['ratio']:>7}{r['one_scene']:>8}{r['tiny']:>9}")

# 25번 자신
print()
L = io.open(r'C:\Users\Rowan\scenario-automation\projects\25_billion_dollar_reset\25_billion_dollar_reset_source_CN.md', encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(L) if re.match(r'^第.+集\s*$', l.strip())] + [len(L)]
ch = []
sc = []
for k in range(len(idx)-1):
    seg = [x.strip() for x in L[idx[k]:idx[k+1]] if x.strip()]
    ch.append(sum(len(x) for x in seg))
    sc.append(sum(1 for x in seg if re.match(r'^\d+-\d+\s', x)))
n = len(ch)
f10 = sum(ch[:10])//10; l10 = sum(ch[-10:])//10
print(f"{'>>> 25_billion_dollar_reset':<34}{n:>4}{sum(ch)//n:>7}{min(ch):>6}{max(ch):>7}{f10:>8}{l10:>8}{round(l10/f10,2):>7}{sum(1 for s in sc if s<=1):>8}{sum(1 for c in ch if c<900):>9}")
print('\n※ 중국어는 1자 정보량이 한글보다 커서 자수 절대값은 비교 불가 — 비교 대상은 "뒤/앞 비율"·"씬1개화"·"편차"뿐.')
