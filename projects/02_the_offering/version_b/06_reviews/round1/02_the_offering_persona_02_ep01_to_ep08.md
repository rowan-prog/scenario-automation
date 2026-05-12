# AIGC Production Director 검토 보고서 — THE OFFERING (Version B) EP01-EP08

## 검토 요약
LOCKED OUT 4-블록 표준 ([Visual]/[Camera]/[DIALOGUE]/[FX]) 모두 충족. EP 본문 한국어 0건 확인. 헤더 메타·footer 미작성 — 영어 일원화 룰 준수. AIGC 실사 세로 9:16 정합 — 클로즈업·MACRO·TIGHT 비율 충분. 회차 평균 4-5 씬, 페이월 EP8만 5 씬 = 청사진 룰 정합.

## 발견된 문제

### 🔴 즉시 수정 필요
없음.

### 🟡 약점 (수정 권장)

**1. EP04 → EP05 손목 화염 자국 연속성 누락**
- 위치: EP05 / S#1 / [Visual]
- 원문 FIND: `Her inner wrist glows faintly gold against the dark.`
- 문제: EP04 / S#4에서 `Vael's thumb wiping a streak of ash across her inner wrist` + `the flame surfacing... his fingertip tracing the mark beneath her skin... a new faint scorched-line — burned ash, not skin — sits over the mark.` — 즉 EP4에서 손목 자국 위에 화염 자국이 추가된 상태. EP5 S#1에서는 이 추가 자국 묘사가 사라짐 (gold만 묘사). AIGC 생성 시 연속성 깨질 가능성.
- 수정 방향: EP05 / S#1 [Visual] 손목 묘사를 `Her inner wrist glows faintly gold against the dark, the thin scorched-line from yesterday's flame still tracing the mark beneath her skin.` 정도로 보강.

**2. EP02 의상 reveal 묘사 — 비주얼 락 등재 항목과의 정합**
- 위치: EP02 / S#3 / [Visual]
- 원문 FIND: `Isolde walks the long corridor toward the great hall in **the new gown — black silk over the floor, silver-and-pearl embroidery along the bodice and sleeves, oblique neckline baring the line of her collarbone, the porcelain inside of her wrists visible, dark-brown hair brushed long and loose down her back.**`
- 문제: 비주얼 락 v5 Look 2 (Vael's Choice) 명세 = "검은 비단 베이스 + 흰·실버 자수·진주 디테일·은빛 사슬". 본문 묘사에서 "은빛 사슬" 누락. AIGC 생성 시 어셋 핵심 디테일 한 가지 누락 → 락과 본문 미일치.
- 수정 방향: 묘사 끝에 `with a thin silver chain detail at the waist` 추가.

### 🟢 선택적 개선

**1. EP01 / S#1 베일 어셋 직접 묘사**
- 위치: EP01 / S#1 / [Visual]
- 원문 FIND: `VAEL DRAKONIS (mid-30s, broad-shouldered, lustrous black hair tied back, grey eyes, sharp jaw — Dragon Lord)`
- 검토: 첫 등장에 어셋 기본 묘사 정확. 다만 비주얼 락 v2의 "흑갈색 머리" 명세 — 본문은 "lustrous black hair". 미세 톤 차이로 락 영문 일관 정정 권장 (lustrous black ↔ dark — 어셋 일관용).

## 의심 지점 사전 스캔
1. EP01-EP08 본문 한국어 검출 → 처리: 검토했으나 유지 (Grep 검증 시 0건 — 아래 영어 일원화 검증 명령 결과).
2. 헤더 메타·footer 잔존 → 처리: 검토했으나 유지 (모든 EP가 첫 헤더 + S#1 ~ Hard Cut 본문만 충족).
3. EP04 / S#4 손목 화염 자국 연속성 → 처리: 🟡 (위 1번).
4. EP02 / S#3 의상 reveal 락 정합 → 처리: 🟡 (위 2번).
5. EP01 / S#1 베일 어셋 머리 색 명세 → 처리: 🟢 (위 1번).
6. EP08 / S#5 — 12 guards buckle / court goes to knees — 군중 인원 AIGC 처리 가능성 → 처리: 검토했으나 유지 (LOCKED OUT 류 군중 처리 정합. WIDE shot으로 분리, 각 KNEE 비트는 CLOSE로 분할되어 있어 생성 가능).

## 검토했으나 유지
1. EP08 / S#1 — 의심: 12 dragon silhouettes on ridge — AIGC 풀샷 의존 위험. 검증 결과: WIDE + SLOW PUSH IN으로만 처리 (EP 전체 1 비트), 부분 비늘·날개 그림자 위주의 청사진 룰 12-7 정합.
2. EP07 / S#3 — 의심: 와이드 윈도우 너머 ridge의 세 wing-shadow를 단일 씬 안에 → 처리: WIDE / SLOW PUSH IN / CUT / CUT / CUT 분리 = AIGC 가능. 풀샷 의존도 낮음.
3. EP03 / S#3 — 의심: 한 씬에 6-비트 응축 — AIGC 생성 시 단일 씬 안 컷 분리 작동 가능성. 검증 결과: 11 cam shots로 분리 (TRACKING / CLOSE / MEDIUM / MACRO 분기), 단일 컷 안 비트 누적 X — 컷별 1 비트로 작동.

## 잘 작동하는 부분
- EP01-EP08 전체 — 한국어 0건 / 메타·footer 0건. 영어 일원화 룰 준수.
- 4-블록 ([Visual]/[Camera]/[DIALOGUE]/[FX]) 모든 씬에 누락 0.
- EP08 / S#5 — `EXTREME WIDE — the ridge above the castle, twelve dragon outlines roaring at once → REVERSE EXTREME WIDE — the outer courtyard, the wall of sound hitting` — 페이월 spectacle의 컷 분리 작동.

## 검토 총평 (Verdict)

- **Verdict 4단계:** 패치 필수 (🟡 2건 — 자동 trigger 06 영역 정합 위반)
- **LOCK / PATCH THEN LOCK / HOLD:** PATCH THEN LOCK
- 다음 단계: EP5 손목 자국 묘사 보강 + EP2 silver chain detail 추가 후 LOCK.
