# Continuity & Logic Auditor 검토 보고서 — THE OFFERING (Version B) EP01-EP08

## 검토 요약
공간 동선·시간 줄·소품 위치 일관. EP1 vs EP8 페이월 분리 깨끗. 다만 EP3에서 자객 배후(KING ALDRIC)가 청사진의 EP3 닫히는 정보 명세를 위반하여 직접 발화로 노출 — 정보 설계 ripple 영향 (EP4-8의 정보 비대칭 약화). 자동 패치 필수 trigger.

## 발견된 문제

### 🔴 즉시 수정 필요
없음 (정합성 단일 결함 — 🟡로 분류, 다만 자동 trigger).

### 🟡 약점 (수정 권장)

**1. EP03 자객 배후 정보 누설 — 청사진 12-6 정보 설계 위반**
- 위치: EP03 / S#1 / [DIALOGUE] + EP03 / S#2 / [DIALOGUE]
- 원문 FIND:
  - S#1 `ASSASSIN (low, almost whisper): Aldric still keeps his promises.`
  - S#2 `VAEL (to the body, low, final): Aldric sent you.`
- 문제: 청사진 12-6 정보 설계 — `❌ 알드릭 왕의 음모 본격` 무료 구간 닫힘. EP3 화별 락 표 — `닫히는 정보: 자객 배후`. 즉 자객의 배후 = 알드릭 왕임은 무료 구간 EP3에서 직접 노출 X. 본문은 자객 + 베일 양쪽 발화로 두 번 명시. 페이월 직전 (EP4+)의 "왕국이 누구인가" 텐션 약화 → 페이월 결제 동력 ripple 손실. EP4의 베일이 인간 왕국 거부 비트 + EP8 알드릭 명시 비트의 응축력 분산.
- 수정 방향:
  - S#1 ASSASSIN 라인 → `"They never let the kingdom forget its promises."` (배후 익명 유지)
  - S#2 VAEL 라인 → `"The kingdom keeps its promises."` (알드릭 단어 제거 / "왕국" 추상 유지)

**2. EP04 → EP05 손목 화염 자국 연속성 누락**
- 위치: EP05 / S#1 / [Visual]
- 원문 FIND: `Her inner wrist glows faintly gold against the dark.`
- 문제: EP04 / S#4에서 추가된 "burned ash, not skin — sits over the mark" 자국이 EP5 시작 시 묘사 누락. EP6+ 어디서도 회수되지 않음 → 시각 표지의 단명 (자국 추가는 누적이지 일회성 X). 비주얼 락 v5 sensual 표지 영구화 룰 위반.
- 수정 방향: EP05 / S#1 [Visual] 마지막에 `the thin scorched-line from the council chamber still traces the mark beneath her skin` 추가. EP6 자발 옆자리 [Visual]에도 한 줄 더 — `the scorched-line over her wrist mark visible now alongside the gold`.

### 🟢 선택적 개선

**1. EP01 / S#2 — 엄밀 시간 연속성 표기**
- 위치: EP01 / S#2 슬러그라인
- 원문 FIND: `S#2 — BLACK CASTLE / OUTER GATES / CONTINUOUS`
- 검토: S#1의 시점이 "VAEL'S HIGH CHAMBER / DUSK", S#2는 "OUTER GATES / CONTINUOUS" — 베일이 그녀의 도착을 보고 명령을 내린 시점과 그녀의 도착이 연속이라는 신호. 동일 dusk 시각으로 정합 — 통과. 다만 두 위치가 다르므로 `CONTINUOUS`보다 `MOMENTS LATER`나 `SAME DUSK`가 정확. AIGC 컨텍스트에서는 통상 통용되나 후속 라운드에서 미세 정정 권장.

## 의심 지점 사전 스캔
1. EP01 / S#3 — 의심: 룬 + 시그닛 동시 깜빡임 비트가 청사진 락 — 작성됐는가 → 처리: 검토했으나 유지 (S#3 [Visual] + [Camera] + [FX] 모두 명시 — 청사진 락 100% 정합).
2. EP03 / S#1, S#2 자객 배후 발화 → 처리: 🟡 (위 1번).
3. EP04 / S#4 손목 화염 자국 연속성 → 처리: 🟡 (위 2번).
4. EP07 / S#3 드래곤 무리 첫 그림자 — EP1-6의 이전 무리 흔적과 충돌 X → 처리: 검토했으나 유지 (EP1·EP4·EP5의 "distant wing-beat" 단수 표지 + EP7의 ridge 위 12 silhouettes로 확장 정합).
5. EP06 / S#4 두 번째 herald 등장 — EP4 first delegation과 위치·소속 분리 정합 → 처리: 검토했으나 유지 (EP4 = "smaller human-kingdom delegation" 일반 사절단 / EP6-7-8 = 왕의 사절단 + 더 큰 깃발 + seal-bearer = 분리 명확).
6. EP08 / S#5 — twelve guards buckle: 청사진 페이월 트리거 명세 12명과 정합 → 처리: 검토했으나 유지 (`twelve full-armor ESCORT GUARDS` S#1에 설정, S#5 `twelve guards buckling, knees to cobblestone in unison` 일치).

## 검토했으나 유지
1. EP03 / S#2 — 의심: 자객의 검이 부러지는 물리 — 베일의 비늘 손은 어떻게 검을 부러뜨릴 수 있는가. 검증 결과: 청사진 12-7 비주얼 캐논 + 12-3 베일 캐논 = 손등 검은 비늘이 분노·소유·보호 시 강해짐. 검과 비늘의 물리 비대칭 = Dragon Lord 정체성. 청사진 락 정합.
2. EP07 / S#4 — 의심: 하나의 회의실 안에서 베일의 손이 동시에 무릎 위 Isolde + 화염 + 시간 인지 — 동선 과부하. 검증 결과: [Camera] 분리 7 shots 분기. 좌우 양손 + 시점 분리. AIGC 가능.
3. EP08 / S#5 — 의심: dragon roar로 신부 선언이 끊겼는데 베일은 mouth still a breath from her — 입은 안 떨어진다 → 그런데 신부 선언은 끊김. 정합: 비늘 손 신호로 끊김 / 입은 거리 유지. 신부 선언의 마지막 단어가 안 나옴이지 입이 떨어지는 게 아님. 청사진 정합.

## 잘 작동하는 부분
- EP01-EP08 — 시간 줄 일관 (EP1 dusk → EP2 night → EP3 night → EP4 day → EP5 night → EP6 day → EP7 day → EP8 dusk).
- EP01 / S#3 룬 + 시그닛 동시 깜빡임 — 회수 보장 단서로 작동 (Hidden Identity Reveal Arc 5 대비).
- 인간 왕국 사절단 vs 왕의 사절단 분리 명확 (EP4 vs EP8).
- EP08 / S#5 — 청사진 페이월 트리거 6 비트 (깃발 태움 + 허리 끌어올림 + 머리채 + 잇자국 자리 + 끊긴 선언 + 12 무릎 + 자발 마킹) 모두 본문 명시.

## 검토 총평 (Verdict)

- **Verdict 4단계:** 패치 필수 (🟡 2건 — 자동 trigger 03 정합 위반)
- **LOCK / PATCH THEN LOCK / HOLD:** PATCH THEN LOCK
- 다음 단계: EP3 자객 배후 발화 익명화 + EP5·EP6 손목 화염 자국 시각 표지 연속화 후 LOCK.
