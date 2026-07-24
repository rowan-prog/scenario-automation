# -*- coding: utf-8 -*-
# phase_p 기계 게이트 — 16_moses
# 2026-07-24 개정: 게이트1 = 행 단위 → 문장 단위 (사용자 재지시 — 원작 클리프 구조 복원으로
#   원안 문장이 회차 간 이동함. 문장 자체는 verbatim 보존 검사 유지).
#   + 별도 작가용 트리트먼트 문서(16_moses_p1_treatment_full.md) 잔재·형식 게이트 추가.
import re, sys, os

BASE = r"C:\Users\Rowan\scenario-automation\projects\16_moses"
P0 = BASE + r"\16_moses_p0_source.md"
SPEC = BASE + r"\16_moses_p1_proposal_spec.txt"
TREAT = BASE + r"\16_moses_p1_treatment_full.md"

p0 = open(P0, encoding='utf-8').read()
spec = open(SPEC, encoding='utf-8').read()
treat_doc = open(TREAT, encoding='utf-8').read() if os.path.exists(TREAT) else ""
fails = []


def sentences(text):
    # 문장 단위 분리: 종결부호(다. 요. ! ? …) + 닫는 따옴표 뒤에서 절단
    parts = re.split(r'(?<=[.!?…])(?=\s|$)|(?<=[.!?…]")(?=\s|$)', text)
    return [s.strip().strip('"').strip() for s in parts if s and len(s.strip()) >= 6]


# 게이트1: 원안 무료회차 본문 = 문장 단위 verbatim 전수 (치환 인명 반영·회차 간 이동 허용)
wonan = p0.split('## 원안 (verbatim)', 1)[1]
src_block = wonan.split('무료회차 줄거리', 1)[1]
src_block = src_block.replace('아사르', '모세').replace('황태자비', '왕비').replace('황태자', '파라오').replace('실라', '델릴라')
src_lines = [ln.strip() for ln in src_block.split('\n') if ln.strip() and not re.match(r'^EP\d', ln.strip())]
sents = []
for ln in src_lines:
    sents.extend(sentences(ln))
targets = [spec] + ([treat_doc] if treat_doc else [])
missing = [s for s in sents if not any(s in t for t in targets)]
if missing:
    fails.append(f"게이트1 원안 문장 누락 {len(missing)}건: " + " / ".join(m[:40] for m in missing[:6]))

# 게이트1b: 원안 로그라인 3행 대조 (왕세자→파라오 1어절 승인 변경 반영)
log_block = wonan.split('로그라인', 1)[1].split('무료회차 줄거리')[0]
log_lines = [ln.strip().replace('왕세자', '파라오') for ln in log_block.split('\n') if ln.strip()]
log_missing = [ln for ln in log_lines if ln not in spec]
if log_missing:
    fails.append(f"게이트1b 로그라인 누락 {len(log_missing)}행: " + " / ".join(m[:40] for m in log_missing))

# 게이트3: 기획안 클리프 마커 = 무료 화수 5 · 요약형 마커 0
n_cliff = spec.count('클리프행어 — ')
if n_cliff != 5:
    fails.append(f"게이트3 기획안 클리프 개수 {n_cliff} != 5")
treat_sec = spec.split('#SECTION 초반 회차 트리트먼트', 1)[1].split('#SECTION 제작 적절성')[0]
for scope_name, scope in [('기획안 트리트먼트', treat_sec), ('작가용 문서', treat_doc)]:
    for marker in ['이 시작된다', '것일까', '수 있을까', '일까?']:
        if marker in scope:
            fails.append(f"게이트3b 요약형 마커 발견({scope_name}): {marker}")

# 게이트3c: 작가용 트리트먼트 문서 — 1~50화 전수 + 무료 클리프 마커 7
# (2026-07-24 무료 구간 5→7화 분할 = 작가용 문서만 적용·기획안은 원안 5화 유지 = 사용자 지시)
if treat_doc:
    ep_nums = re.findall(r'^(\d+)화\s*[—-]', treat_doc, re.M)
    got = sorted(set(int(n) for n in ep_nums))
    want = list(range(1, 51))
    if got != want:
        miss = [n for n in want if n not in got]
        fails.append(f"게이트3c 작가용 문서 회차 결번/이상: 누락 {miss[:10]} (총 {len(got)}화 검출)")
    n_cliff_t = treat_doc.count('클리프행어 — ')
    if n_cliff_t != 7:
        fails.append(f"게이트3c 작가용 문서 클리프 마커 {n_cliff_t} != 7 (무료 7화 전용)")
    # 무료 5화 원본 클리프 5종 보존 검사 (분할해도 절단점 자체는 불변)
    for keep in ['스스로 지옥의 불길 속으로 걸어 들어갔을 뿐이야',
                 '흙투성이인 그와 다말의 눈이 얽힌다',
                 '내가 이 남자를 선택했으니까',
                 '당신의 신부가 되어 기다리고 있을게요',
                 '약속대로, 나의 신부를 맞이하러 왔다']:
        if f'클리프행어 — ' not in treat_doc or keep not in treat_doc.split('## 유료 회차')[0]:
            fails.append(f"게이트3d 원본 클리프 소실: {keep[:24]}")

# 게이트5: 구버전·원작 인명, 금지어, HTML 이스케이프 잔재 (기획안 + 작가용 문서)
BAD = ['아사르', '실라', '황태자', '왕세자', '이집트', '가칭', '&lt;', '&gt;', '&amp;',
       '아이린', '에리스', '아폴론', '레오니다스', '데메트리오스', '리키아', '에도루스', '레토', '델포이', '올림푸스']
for scope_name, scope in [('기획안', spec), ('작가용 문서', treat_doc)]:
    if not scope:
        continue
    for bad in BAD:
        hits = scope.count(bad)
        if bad == '아폴론':
            continue
        if hits:
            fails.append(f"게이트5 잔재({scope_name}) '{bad}' {hits}건")
    if '아폴론' in scope:
        fails.append(f"게이트5 잔재({scope_name}) '아폴론' {scope.count('아폴론')}건 (원작 인명 한글 표기 금지 — 영문 타이틀만 허용)")

# 게이트6: 일정/회차/타깃 = 원안·확정 값
for req in ['총 48화 / 무료회차: 1~5화', 'AI실사', '미정(TBD)', 'Rowan', '팀 리드 확인 A', '발화 언어: EN',
            'I Chose a Slave, But He Parts the Sea', '내 남편은 거지 모세', '람세스', '라반', '델릴라 (Delilah)']:
    if req not in spec:
        fails.append(f"게이트6 필드 누락: {req}")

# 게이트4(변형): 중국어 생략 확인 — 한자 잔재 0 (원안의 東風 병기만 허용)
for scope_name, scope in [('기획안', spec), ('작가용 문서', treat_doc)]:
    if scope and re.search(r'[\u4e00-\u9fff]', scope.replace('東風', '')):
        fails.append(f"게이트4 한자 잔재 발견({scope_name}) (東風 제외)")

print("FAIL:\n" + "\n".join(fails) if fails else "ALL GATES PASS")
print(f"[집계] 기획안 클리프 {n_cliff}개 · 원안 문장 {len(sents)}건 전수 · 로그라인 {len(log_lines)}행"
      + (f" · 작가용 문서 {len(set(re.findall(chr(94)+r'(\d+)화', treat_doc, re.M)))}화" if treat_doc else " · 작가용 문서 없음"))
