# -*- coding: utf-8 -*-
# phase_p 기계 게이트 — 16_moses
import re, sys

P0 = r"C:\Users\Rowan\scenario-automation\projects\16_moses\16_moses_p0_source.md"
SPEC = r"C:\Users\Rowan\scenario-automation\projects\16_moses\16_moses_p1_proposal_spec.txt"

p0 = open(P0, encoding='utf-8').read()
spec = open(SPEC, encoding='utf-8').read()
fails = []

# 게이트1: 원안 무료회차 본문 verbatim 전수 대조 (아사르→모세 치환 후 문장 단위)
wonan = p0.split('## 원안 (verbatim)', 1)[1]
src_block = wonan.split('무료회차 줄거리', 1)[1]
# 사용자 확정 치환 정본: 아사르→모세 · 황태자비→왕비 · 황태자/왕세자→파라오
src_block = src_block.replace('아사르', '모세').replace('황태자비', '왕비').replace('황태자', '파라오').replace('실라', '델릴라')
# EP 헤더 제거하고 문장·행 단위 비교
lines = [ln.strip() for ln in src_block.split('\n') if ln.strip() and not re.match(r'^EP\d', ln.strip())]
missing = [ln for ln in lines if ln not in spec]
if missing:
    fails.append(f"게이트1 원안 verbatim 누락 {len(missing)}행: " + " / ".join(m[:40] for m in missing[:5]))

# 원안 로그라인 3행 대조 (왕세자→황태자 1어절 승인 변경 반영)
log_block = wonan.split('로그라인', 1)[1].split('무료회차 줄거리')[0]
log_lines = [ln.strip().replace('왕세자', '파라오') for ln in log_block.split('\n') if ln.strip()]
log_missing = [ln for ln in log_lines if ln not in spec]
if log_missing:
    fails.append(f"게이트1b 로그라인 누락 {len(log_missing)}행: " + " / ".join(m[:40] for m in log_missing))

# 게이트3: 클리프 개수 = 무료 화수 5 · 요약형 마커 0
n_cliff = spec.count('클리프행어 — ')
if n_cliff != 5:
    fails.append(f"게이트3 클리프 개수 {n_cliff} != 5")
treat = spec.split('#SECTION 초반 회차 트리트먼트', 1)[1].split('#SECTION 제작 적절성')[0]
for marker in ['이 시작된다', '것일까', '수 있을까', '일까?']:
    if marker in treat:
        fails.append(f"게이트3b 요약형 마커 발견: {marker}")

# 게이트5: 구버전 인명·HTML 이스케이프 잔재
for bad in ['아사르', '실라', '황태자', '왕세자', '이집트', '가칭', '&lt;', '&gt;', '&amp;', '아이린', '에리스', '아폴론']:
    # 아폴론/아이린/에리스 = 원작 인명 — 레퍼런스 타이틀(영문) 외 본문 등장 금지
    hits = spec.count(bad)
    if bad == '아폴론':
        continue  # 영문 타이틀만 사용 확인: 한글 '아폴론' 자체가 spec에 없어야 함
    if hits:
        fails.append(f"게이트5 잔재 '{bad}' {hits}건")
if '아폴론' in spec:
    fails.append(f"게이트5 잔재 '아폴론' {spec.count('아폴론')}건 (원작 인명 한글 표기)")

# 게이트6: 일정/회차/타깃 = 원안·확정 값
for req in ['총 48화 / 무료회차: 1~5화', 'AI실사', '미정(TBD)', 'Rowan', '팀 리드 확인 A', '발화 언어: EN', 'I Chose a Slave, But He Parts the Sea', '내 남편은 거지 모세', '람세스', '라반', '델릴라 (Delilah)']:
    if req not in spec:
        fails.append(f"게이트6 필드 누락: {req}")

# 게이트4(변형): 중국어 생략 확인 — 中文 흔적 0
if re.search(r'[\u4e00-\u9fff]', spec.replace('東風', '')):  # 원안의 東風(한자 병기)만 허용
    fails.append("게이트4 중국어(한자) 잔재 발견 (원안 東風 제외)")

print("FAIL:\n" + "\n".join(fails) if fails else "ALL GATES PASS")
print(f"[집계] 클리프 {n_cliff}개 · 원안 대조 {len(lines)}행 전수 · 로그라인 {len(log_lines)}행")
