# English Dialogue & Voice Auditor 검토 보고서 — THE OFFERING (Version B) EP01-EP08

## 검토 요약
북미 실사형 spoken English 기준 — 자연 발화 가능 라인 위주. 짧고 단언적 alpha cadence 일관 (Vael) / 단정·자기 보존 cadence (Isolde). 번역체 0건 / honorific 0건 / 일본어 dub style 0건. 평균 라인 3-10 단어 이내 충실. 다만 베일의 두 라인이 짙은 문어체로 cadence 정정 권장.

## 발견된 문제

### 🔴 즉시 수정 필요
없음.

### 🟡 약점 (수정 권장)

**1. EP04 / S#4 베일 마지막 라인 — 문어체 cadence**
- 위치: EP04 / S#4 / [DIALOGUE]
- 원문 FIND: `VAEL: They will not call you that name again.`
- 문제: 라인 자체는 EP4 화별 락의 cut line으로 청사진 명시 — 유지가 맞다. 다만 EP04 / S#3 끝에 이미 동일 라인이 나옴 (`They will not call you that name again.`). EP04 안에 같은 라인이 두 번 — cadence 누적 X / 임팩트 분산. S#3는 sentry / S#4는 ISOLDE 향발화여야.
- 수정 방향: EP04 / S#4 VAEL 라인을 다른 발화로 — 청사진 사이드 락 `"Not yet."` 활용 또는 `"That name dies with the kingdom."` 등 cadence 변형.

### 🟢 선택적 개선

**1. EP05 / S#4 "kingdom has a second war"**
- 위치: EP05 / S#4 / [DIALOGUE]
- 원문 FIND: `VAEL: Because once it is yours, the kingdom has a second war.`
- 검토: 자연 발화 가능. 다만 "second war" 표현이 약간 문어체 — 베일의 통상 cadence보다 길다. `"Because once it is yours, the kingdom comes for both of us."` 가 더 spoken. 작품 자율.

**2. EP08 / S#5 베일 마지막 라인**
- 위치: EP08 / S#5 / [DIALOGUE]
- 원문 FIND: `VAEL (low, almost a smile, almost a warning): On my mouth. Not yours.`
- 검토: 라인 자체 강함. 다만 (almost a smile, almost a warning) — 두 톤 동시 지시는 actor에게 모호. 하나로 통일 권장: `(low, almost a warning)` 또는 `(low, the start of a smile)` 중 택1.

## 의심 지점 사전 스캔
1. EP01-EP08 honorific (`-san`, `-sama`, `-sensei` 등) 잔존 → 처리: 검토했으나 유지 (Grep 검증 0건).
2. EP01-EP08 일본 dub style 양식화 선언형 → 처리: 검토했으나 유지 (해당 카테고리 = 여성향 다크 로맨타지, 양식화 적용 X — 본문 자연 spoken English 일관).
3. EP04 / S#3 + S#4 동일 라인 반복 → 처리: 🟡 (위 1번).
4. EP05 "kingdom has a second war" → 처리: 🟢 (위 1번).
5. EP07 / S#2 `VAEL (still to Isolde, not the herald): Are you cold.` — 알파 위계의 도발적 무시 cadence → 처리: 검토했으나 유지 (북미 spoken + 위계 시그널 + 알파 자제 동시 — 완벽 cadence).
6. EP08 / S#3 `VAEL: They burn before her now.` — 셋 단어 문장 — 라인 짧음의 임팩트 → 처리: 검토했으나 유지 (paid vertical 셋-단어 cut line 표준 cadence).

## 검토했으나 유지
1. EP02 / S#5 `ISOLDE: For tonight.` / `VAEL: For longer.` — 의심: 두 음절 응답이 cadence 충분한가. 검증 결과: paid vertical 짧은 임팩트 라인의 표준 — Demon Lord's Marked Bride / Wolfless Carpenter 검증 cadence와 정합.
2. EP01 / S#5 `ISOLDE (barely above a breath): What do you see.` — 의심: 너무 시적인 cadence. 검증 결과: spoken English 자연 흐름 — actor가 작은 호흡으로 발화 가능. 통과.
3. EP06 / S#3 `ISOLDE (to the hall, even): The mark holds.` — 의심: 자기 발화 + 공개 — F-F 코드(정치적 올바름 자기 발화) 위험. 검증 결과: 베일의 발화에 대한 호응으로만 작동 (`VAEL: Then say it where they can hear.`) — 자기 선언 X / 베일이 명령한 발화 = 능동 호응 정합. F-F 회피.

## 잘 작동하는 부분
- EP01 / S#4 `VAEL: Don't lower your eyes.` — 알파 짧은 명령형, 3 단어, 강한 cadence.
- EP07 / S#4 `VAEL: To kneel before her — or to lose his banner before her.` — paid vertical 위계 라인의 표준 cadence (or 분기 + 위계 + spectacle 예고).
- EP08 / S#5 `ISOLDE: Finish it.` — 두 단어, 능동 여주 cadence, F-K(여주 강함 약화) 회피.
- Vael의 cadence 일관 — 짧은 명령형 + 자제 표지 ("Not yet.") + 위계 라인 / Isolde cadence 일관 — 단정 + 자기 보존 + 호응 + 능동.

## 검토 총평 (Verdict)

- **Verdict 4단계:** 패치 필수 (🟡 1건)
- **LOCK / PATCH THEN LOCK / HOLD:** PATCH THEN LOCK
- 다음 단계: EP4 / S#4 중복 라인 변형 후 LOCK.
