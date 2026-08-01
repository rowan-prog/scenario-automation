# -*- coding: utf-8 -*-
import os as _os; _os.chdir(r'C:\Users\Rowan\scenario-automation\projects\16_moses')
"""각색 가이드 v12가 원작에 대해 주장하는 사실을 원작 파일에 대조."""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

B = r"C:\Users\Rowan\scenario-automation\projects\16_moses" + "\\"
O = {}
for ln in open(B + '03_작업파일/_orig_paras.txt', encoding='utf-8'):
    if '\t' not in ln:
        continue
    n, t = ln.rstrip('\n').split('\t', 1)
    O[int(n)] = t
TXT = '\n'.join(O.values())

# 회차 경계
EPS = {}
for n, t in O.items():
    m = re.match(r'^제(\d+)화$', t.strip())
    if m:
        EPS[int(m.group(1))] = n
order = sorted(EPS.items())


def ep_text(e):
    st = EPS.get(e)
    if st is None:
        return ''
    nxt = min([v for k, v in order if v > st], default=max(O) + 1)
    return '\n'.join(O[i] for i in range(st, nxt) if i in O)


ok = bad = 0


def chk(claim, cond, evidence=''):
    global ok, bad
    if cond:
        ok += 1
        print(f'[O] {claim}' + (f'  ← {evidence}' if evidence else ''))
    else:
        bad += 1
        print(f'[X] {claim}' + (f'  ← {evidence}' if evidence else ''))


print('=== 가이드가 원작에 대해 주장하는 것 ===')
chk('원작 = 48화', max(EPS) == 48, f'파일 내 최대 = 제{max(EPS)}화')
chk('원작 32화에 화자명 "레도" 오타 존재', '레도:' in ep_text(32),
    [l[:40] for l in ep_text(32).split('\n') if l.startswith('레도')][:1])
e37 = ep_text(37)
allmix = sum(1 for t in O.values() if re.match(r'^[가-힣0-9]+\s*:', t) and '△' in t)
chk('원작에 지문-대사 혼입 없음', allmix == 0, f'{allmix}건')
chk('원작 37화 피시아/파시아 혼용', ('피시아' in e37 and '파시아' in e37),
    f'피시아 {e37.count("피시아")} · 파시아 {e37.count("파시아")}')

print()
print('=== 조연 원작 이름 ===')
for nm in ['피시아', '파시아', '노리라', '제시타']:
    chk(f'원작에 "{nm}" 존재', nm in TXT, f'{TXT.count(nm)}회')

print()
print('=== G30 원작 요소 처리표 — 원작에 실재하는가 ===')
for nm in ['월계관', '월계수', '태양의 석판', '올리브', '에게해', '심연',
           '황금 마차', '흑마', '수호대', '아레오파고스', '델포이', '델리아']:
    chk(f'"{nm}"', nm in TXT, f'{TXT.count(nm)}회')
chk('아폴론의 황금빛 피', '황금빛 피' in TXT, f'{TXT.count("황금빛 피")}회')
chk('황금 검 펜던트 = 원작 명칭', '황금 검 펜던트' in TXT, f'{TXT.count("황금 검 펜던트")}회')
chk('화관 의식 = 원작', '화관' in TXT, f'{TXT.count("화관")}회')

print()
print('=== 신계 씬 화수 (11·13·17·19·38·47·48) ===')
for e in [11, 13, 17, 19, 38, 47, 48]:
    t = ep_text(e)
    chk(f'원작 {e}화에 신계/올림포스 씬', ('올림포스' in t or '레토' in t), '')

print()
print('=== 인물 관계 ===')
chk('도리에우스 = 레오니다스의 형', '레오니다스의 형' in TXT or '형님' in TXT,
    f'"형님" {TXT.count("형님")}회')
chk('레토 = 아폴론의 어머니', ('어머니' in TXT and '레토' in TXT), '')
chk('원작에 "백성" 0건 (우리 발명)', '백성' not in TXT, f'{TXT.count("백성")}회')
chk('원작에 "벽화" 0건 (작가 발명)', '벽화' not in TXT, f'{TXT.count("벽화")}회')
chk('원작 5화에 바다 가르기 없음 (우리 발명)', '바다' not in ep_text(5), '')

print()
print(f'통과 {ok} / 불일치 {bad}')
