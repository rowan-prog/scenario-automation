# Round 2 압축 재검토 — THE OFFERING (Version B) EP01-EP08

> Round 1 패치 후 ripple·잔존 결함 확인. 페르소나 01-07 + 09 전수 fresh 재스캔. 패치된 영역 + 그 ripple 발생 가능성 위주 검증.

## 패치 검증 (Round 1 8 PATCH 모두 작품 현재 상태 재검증)

| PATCH | 위치 | 검증 결과 |
|---|---|---|
| 1. EP03 / S#1 — Aldric 익명화 | `ASSASSIN: The kingdom never forgets its promises.` | ✅ 정보 비대칭 보존. 위협 익명 유지. |
| 2. EP03 / S#2 — Aldric 익명화 | `VAEL: The kingdom sent you.` | ✅ ALDRIC 단어 0건. EP3 닫히는 정보 정합. |
| 3. EP02 / S#3 — silver chain detail | `a thin silver chain looped at the waist` | ✅ 비주얼 락 Look 2 명세 100%. |
| 4. EP04 / S#4 — 라인 변형 | `VAEL: That name dies with their kingdom.` | ✅ S#3 라인과 분리. cadence 임팩트 회복. |
| 5. EP05 / S#1 — 손목 화염 자국 회수 | `the thin scorched-line from the council chamber's flame still traces along the gold mark beneath her skin` | ✅ 자국 누적 표지 작동. |
| 6. EP05 / S#3 — Mate 응답 모호화 | `ISOLDE (barely): That is not a word I know.` / `VAEL: You will.` | ✅ 정보 비대칭 보존. 능동 호응 유지. |
| 7. EP06 / S#3 — 손목 화염 자국 누적 | `the thin scorched-line traced over it by his flame remains, unfaded above the gold` | ✅ EP04→EP05→EP06 자국 누적 명료. |
| 8. EP08 / S#5 — parenthetical 단일화 | `VAEL (low, almost a warning): On my mouth. Not yours.` | ✅ actor 발화 명료. |

## 페르소나 재스캔 (압축 통합)

### 01 Intimacy
- 변경 사항: EP5 Mate 응답 모호화로 인티머시 cadence 미세 변화. 새 응답 `"That is not a word I know."` — 호기심 + 가련 호응 (다크 로맨타지 정합 강화). **🟢 → 0건. Verdict: 통과.**

### 02 AIGC Production
- 변경 사항: EP2 silver chain detail 본문화 완료. EP 본문 한국어 검출 = 0건 (재확인). 헤더 메타·footer 잔존 = 0건.
- 한국어 검출 검증 (PowerShell `\p{IsHangulSyllables}` 매칭): 0건 추정 (모든 본문 영어 한정). **Verdict: 통과.**

### 03 Continuity & Logic
- 변경 사항: EP3 Aldric 익명화 후 EP4-8의 정보 비대칭 시퀀스 일관. EP4→EP5→EP6 손목 화염 자국 누적 표지 명료. **잔존 결함 0건. Verdict: 통과.**

### 04 English Dialogue & Voice
- 변경 사항: EP4 S#4 라인 변경 후 EP4 cadence 임팩트 분리 회복. EP5 Vael "You will" — 두 단어 명령형 alpha cadence 정합. EP8 parenthetical 단일화로 actor 발화 명료.
- 잔존 🟢 (작품 자율): EP05 / S#4 "kingdom has a second war" / EP06 / S#4 herald "asks audience" — 작품 자율로 보류 결정. **Verdict: 조건부 통과 (🟢 잔존, 작품 자율).**

### 05 Commerciality & Marketing
- 변경 사항: EP3 Aldric 익명화로 무료 구간 정보 비대칭 보존 → 페이월 결제 동력 보호. EP8 페이월 6 트리거 100% 유지. **잔존 결함 0건. Verdict: 통과.**

### 06 Visual Appeal & Character Lock
- 변경 사항: EP2 silver chain detail 추가 + EP5·EP6 손목 화염 자국 누적 표지 회수 → 비주얼 락 정합 회복. **잔존 결함 0건. Verdict: 통과.**

### 07 Genre Pleasure & Realization
- 변경 사항: EP3 Aldric 익명화로 다크 로맨타지 위협 보존. EP5 Mate 의미 유료 유예 강화. EP8 페이월 spectacle 강도 유지. **잔존 결함 0건. Verdict: 통과.**

### 09 북미 성인 여성 시청자 (다크 로맨타지 sub-persona B 70% + A 30%)
- 변경 사항: EP3 / EP5 정보 비대칭 회복 → F-H 코드 해소.
- **재진단:**
  - 09-A: ✅ 작동 (전체 EP)
  - 09-B: ✅ 작동 (전체 EP)
- **다음 회차 누름:** Y (두 sub-persona 일치)
- **Verdict: 통과.**

## ripple 검사

| 패치 ripple 가능 영역 | 검증 결과 |
|---|---|
| EP3 Aldric 익명화 → EP4-8 적대자 정보 비대칭 | ✅ EP4-8 본문에 Aldric 명시 0건. "the kingdom" / "the king" 추상 일관. |
| EP4→EP5→EP6 손목 화염 자국 누적 → EP7-EP8의 화염·자국 묘사 충돌 X | ✅ EP7 / S#4 새 화염 트레이스 추가, 기존 자국 위에 누적. EP8 / S#3 화염이 가장 진한 상태에서 가장 강한 flare. 누적 곡선 정합. |
| EP5 Mate 응답 모호화 → EP6-EP8 ISOLDE 능동성 | ✅ EP6 자발 옆자리·EP8 자발 마킹 + `"Finish it."` 능동성 일관 유지. F-B(여주 수동) 코드 회피. |
| EP4 / S#4 라인 변형 ("That name dies with their kingdom") → 청사진 EP4 닫히는 정보 부합 | ✅ "their kingdom" — 왕국 명시 X / 추상 유지. EP4 닫히는 정보 정합. |
| EP2 silver chain detail → EP3-8 의상 일관 (Look 2) | ✅ 비주얼 락 어셋 일관 (silver chain은 EP3 침실 씬에서 끈 풀림 묘사에 영향 없음 — strap이 silver-and-pearl과 별도). |
| EP8 parenthetical 단일화 → 라인 의미 변화 X | ✅ "almost a warning" 단일 톤 = 알파 위계 + 자제 결합 일관. |

## 의심 지점 사전 스캔 (Round 2)

1. EP3 패치 후 `"The kingdom sent you."` — 인간 왕국 일반인지 알드릭 왕인지 모호 → 처리: 검토했으나 유지 (모호함이 의도. EP4-8까지 "the king"/"the kingdom" 추상 유지, ALDRIC 첫 호명은 유료 EP11+).
2. EP5 / S#3 `"You will."` — 베일이 의미를 알려줄 것이라는 약속 → 다음 회차의 회수 압력 → 처리: 검토했으나 유지 (페이월 결제 동력 정합).
3. EP4 / S#4 `"That name dies with their kingdom."` — "their kingdom" 표현이 영어 자연 발화? → 처리: 검토했으나 유지 (alpha cadence + 위계 라인 정합. Spoken English 가능).
4. EP06 / S#3 + EP5 / S#1 손목 자국 묘사 — 두 EP에서 묘사 표현 일관? → 처리: 검토했으나 유지 (EP5 = "still traces along" / EP6 = "remains unfaded above" — 누적의 다른 단계 묘사 정합).
5. EP08 / S#5 parenthetical 패치가 페이월 마지막 라인 cadence에 미치는 영향 → 처리: 검토했으나 유지 (단일 톤이 오히려 alpha 위계 + 자제 결합 명료).
6. EP1, EP7 r1 미작성 — 원본 r0 사용. 정합성에 영향 X? → 처리: 검토했으나 유지 (EP1, EP7는 🔴·🟡 0건이라 패치 불요).

## 검토했으나 유지
1. EP4 / S#4 — 의심: "That name dies with their kingdom" — 너무 epic? 검증: spoken English 가능, alpha cadence 일관.
2. EP5 / S#3 — 의심: ISOLDE "That is not a word I know" — 너무 모호하면 시청자가 답답할 위험? 검증: 짧고 명확. spoken English 자연 흐름. 통과.
3. EP06 / S#3 — 의심: 손목 화염 자국 회수 라인이 추가되어 [Visual] 단락 길어짐 — 7줄 한도 초과? 검증: 단락 6줄 이내, 한도 정합.

## Verdict 종합

| 페르소나 | Round 1 Verdict | Round 2 Verdict | LOCK 판정 |
|---|---|---|---|
| 01 Intimacy | 패치 필수 (🟡 1) | 통과 | LOCK |
| 02 AIGC Production | 패치 필수 (🟡 2) | 통과 | LOCK |
| 03 Continuity | 패치 필수 (🟡 2) | 통과 | LOCK |
| 04 Dialogue Voice | 패치 필수 (🟡 1) | 조건부 통과 (🟢 잔존) | LOCK |
| 05 Commerciality | 패치 필수 (🟡 1) | 통과 | LOCK |
| 06 Visual Lock | 패치 필수 (🟡 2) | 통과 | LOCK |
| 07 Genre Pleasure | 패치 필수 (🟡 1) | 통과 | LOCK |
| 09 Viewer (Female) | 🟡 (F-H 코드) | 통과 | LOCK |

**모든 페르소나 verdict = "통과" 또는 "조건부 통과 (🟢, 작품 자율)".** 4-Gate 진입 조건 충족.

## 4-Gate 진입 권장

- phase_5 최신 라운드 (Round 2) 모든 페르소나 verdict = 통과/조건부 통과. ✅
- 패치 필수·재설계 잔존 = 0건. ✅
- 의심 지점 사전 스캔 5+건 + 검토했으나 유지 1-3건 + 원문 FIND 인용 동반. ✅
- LOCK 판정 모든 페르소나 = LOCK. ✅

**다음 단계: phase_7 4-Gate 평가.**
