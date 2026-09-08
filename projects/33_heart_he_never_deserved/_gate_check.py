# -*- coding: utf-8 -*-
"""유료 11~50화 트리트먼트 기계 게이트. 사용: python _gate_check.py <file>"""
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = sys.argv[1]
t = open(p, encoding='utf-8').read()
lines = t.split('\n')
fails = []

# 1) 화 헤더 = 정확히 'N화' 한 줄, 11~50 순서대로 40개
hdr = [(i, l) for i, l in enumerate(lines) if re.fullmatch(r'\s*\d+화\s*', l)]
nums = [int(re.match(r'\s*(\d+)', l).group(1)) for _, l in hdr]
if nums != list(range(11, 51)):
    fails.append(f'화 헤더 {len(nums)}개 / 기대 40 (11~50): {nums[:5]}...{nums[-5:]}')
# 부제 의심: 'N화' 뒤에 다른 글자가 붙은 줄
sub = [l for l in lines if re.match(r'\s*\d+화\s*\S', l)]
if sub: fails.append(f'회차 부제 의심 {len(sub)}: {sub[:3]}')

# 2) 각 화 블록에 핵심 대사 1줄 + 클리프행어 1줄
blocks = {}
for k, (i, l) in enumerate(hdr):
    j = hdr[k+1][0] if k+1 < len(hdr) else len(lines)
    blocks[nums[k]] = lines[i+1:j]
for n, b in blocks.items():
    kd = [x for x in b if x.startswith('핵심 대사:')]
    cl = [x for x in b if x.startswith('클리프행어:')]
    if len(kd) != 1: fails.append(f'{n}화 핵심 대사 줄 {len(kd)}개')
    if len(cl) != 1: fails.append(f'{n}화 클리프행어 줄 {len(cl)}개')
    story = [x for x in b if x.strip() and not x.startswith(('핵심 대사:', '클리프행어:'))]
    sents = sum(len([s for s in re.split(r'(?<=[.다!?」])\s+', x) if s.strip()]) for x in story)
    if sents < 2 or sents > 8: fails.append(f'{n}화 스토리 문장 수 {sents}')

# 3) 금지어
bad = {
 '페이월': r'페이월|paywall',
 '시간부사': r'며칠 뒤|며칠 후|같은 주|주말에|얼마 뒤|얼마 후|그 사이|몇 주 뒤|몇 달 뒤|한 달 뒤|이튿날|다음 날|다음날',
 'SF잔재': r'홀로그램|드론|사이버|크레딧|클라우드 시티|스캐너|로봇|포드\b|접근키|칩\b|마그레브|우주|정거장|방사능|하이퍼|데이터 키|스카이넷|Skynet',
 '원작인명': r'미아|밴스|레오|스텔라|줄리[언안]|데커드|스털링|Mia\b|Vance|Leo\b|Stella|Julian',
 '작업어': r'엔진|비트|훅|락인|구조적|오해 해소|정보 비대칭|클리프(?!행어)|서사|플롯|캐릭터',
 '은유동사': r'삼킨다|삼키|무너져 내리|찢어지|파고든다|스며|휘감|집어삼|사무친|번진다|번져',
 '카메라': r'카메라|클로즈업|컷\b|앵글|프레임',
}
for name, pat in bad.items():
    hits = [(i+1, l.strip()[:70]) for i, l in enumerate(lines) if re.search(pat, l)]
    if hits: fails.append(f'{name} {len(hits)}건: ' + ' | '.join(f'L{i} {s}' for i, s in hits[:6]))

# 4) 3년 뒤 = 38화에만 1회
yr = [(n, x) for n, b in blocks.items() for x in b if '3년 뒤' in x or '삼 년 뒤' in x]
if not (len(yr) == 1 and yr[0][0] == 38): fails.append(f'"3년 뒤" 위치/횟수: {[(n, x[:30]) for n, x in yr]}')

print(f'화 수: {len(nums)} · 총 {len(t)}자')
for n in sorted(blocks):
    b = blocks[n]; story = ''.join(x for x in b if x.strip() and not x.startswith(('핵심 대사:', '클리프행어:')))
    q = story.count('「')
    print(f'{n}화 {len(story)}자 「」{q}')
print('FAIL' if fails else 'PASS')
for f in fails: print(' -', f)
