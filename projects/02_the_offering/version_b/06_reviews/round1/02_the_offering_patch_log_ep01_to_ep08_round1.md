# 패치 로그 — THE OFFERING (Version B) EP01-EP08 Round1

## 반영한 검토 항목

| 페르소나 | 등급 | 위치 | 처리 |
|---|---|---|---|
| 03 / 05 / 07 / 09 (중복 독립 확인) | 🟡 | EP03 / S#1, S#2 / [DIALOGUE] | 수정 (ALDRIC 익명화) |
| 02 / 03 / 06 (중복 독립 확인) | 🟡 | EP05 / S#1 / [Visual] | 수정 (손목 화염 자국 회수) |
| 03 / 06 | 🟡 | EP06 / S#3 / [Visual] | 수정 (손목 화염 자국 회수) |
| 02 / 06 | 🟡 | EP02 / S#3 / [Visual] | 수정 (silver chain detail 추가) |
| 04 | 🟡 | EP04 / S#4 / [DIALOGUE] | 수정 (라인 중복 변형) |
| 01 / 09 | 🟡 | EP05 / S#3 / [DIALOGUE] | 수정 (ISOLDE Mate 응답 모호화) |
| 01 | 🟢 | EP03 / S#4 / [DIALOGUE] | 보류 (작품 자율) |
| 02 | 🟢 | EP01 / S#1 / [Visual] | 보류 (작품 자율 — 비주얼 락은 lustrous black로 정합 가능 톤) |
| 04 | 🟢 | EP05 / S#4 / [DIALOGUE] | 보류 (작품 자율) |
| 04 | 🟢 | EP08 / S#5 / [DIALOGUE] | 수정 (parenthetical 단일화) |
| 06 | 🟢 | EP02 / S#3 / [Visual] | 보류 (헤어 어셋 lustrous 일관 — Look 2 reveal 묘사에 추가 필요성 낮음) |
| 07 | 🟢 | EP06 / S#4 / [DIALOGUE] | 보류 (작품 자율) |

## 패치 내역

### PATCH 1 — EP03 / S#1 / [DIALOGUE]

- **문제:** 자객 발화에서 ALDRIC 직접 노출 → 무료 구간 정보 비대칭 약화 (페르소나 03·05·07·09 동시 확인)
- **원인 판정:** 정보 설계
- **FIND:**
  ```
  ASSASSIN (low, almost whisper): Aldric still keeps his promises.
  ```
- **REPLACE:**
  ```
  ASSASSIN (low, almost whisper): The kingdom never forgets its promises.
  ```
- **이유:** ALDRIC 단어 제거 → "the kingdom" 추상 후퇴. 위협 누구인지의 텐션 유료로 유예.

### PATCH 2 — EP03 / S#2 / [DIALOGUE]

- **문제:** 베일 발화에서 ALDRIC 직접 노출
- **원인 판정:** 정보 설계
- **FIND:**
  ```
  VAEL (to the body, low, final): Aldric sent you.
  ```
- **REPLACE:**
  ```
  VAEL (to the body, low, final): The kingdom sent you.
  ```
- **이유:** PATCH 1과 동일 — ALDRIC 명시는 유료 EP11+로 유예.

### PATCH 3 — EP02 / S#3 / [Visual]

- **문제:** Look 2 reveal 묘사에서 비주얼 락 명세 디테일 "은빛 사슬" 누락 (페르소나 02·06)
- **원인 판정:** 정합성 (비주얼 락 vs 본문)
- **FIND:**
  ```
  Isolde walks the long corridor toward the great hall in **the new gown — black silk over the floor, silver-and-pearl embroidery along the bodice and sleeves, oblique neckline baring the line of her collarbone, the porcelain inside of her wrists visible, dark-brown hair brushed long and loose down her back.**
  ```
- **REPLACE:**
  ```
  Isolde walks the long corridor toward the great hall in **the new gown — black silk over the floor, silver-and-pearl embroidery along the bodice and sleeves, a thin silver chain looped at the waist, oblique neckline baring the line of her collarbone, the porcelain inside of her wrists visible, dark-brown hair brushed long and loose down her back.**
  ```
- **이유:** 비주얼 락 Look 2 명세 100% 정합.

### PATCH 4 — EP04 / S#4 / [DIALOGUE]

- **문제:** S#3 끝 베일 라인과 S#4 끝 베일 라인이 동일 ("They will not call you that name again.") → cadence 임팩트 분산 (페르소나 04)
- **원인 판정:** 대사
- **FIND:**
  ```
  VAEL: They will not call you that name again.
  ISOLDE: And what will you call me.
  VAEL: Not yet.
  ```
- **REPLACE:**
  ```
  VAEL: That name dies with their kingdom.
  ISOLDE: And what will you call me.
  VAEL: Not yet.
  ```
- **이유:** S#3은 외부 발화 (사절단 향) / S#4는 내부 발화 (이솔데 향) — cadence 분리. 의미는 동일하나 발화 대상 분리.

### PATCH 5 — EP05 / S#1 / [Visual]

- **문제:** EP04에서 추가된 손목 화염 자국 (scorched-line)이 EP05 시작 시 묘사 누락 (페르소나 02·03·06)
- **원인 판정:** 정합성 (시각 표지 누적)
- **FIND:**
  ```
  Isolde stands at the obsidian balustrade, fingertips on the cold stone, her dark-brown hair loose. The black silk gown still has the high cut hiding the bite-mark on her collarbone. Her inner wrist glows faintly gold against the dark.
  ```
- **REPLACE:**
  ```
  Isolde stands at the obsidian balustrade, fingertips on the cold stone, her dark-brown hair loose. The black silk gown still has the high cut hiding the bite-mark on her collarbone. Her inner wrist glows faintly gold against the dark — the thin scorched-line from the council chamber's flame still traces along the gold mark beneath her skin.
  ```
- **이유:** 비주얼 락 v5 sensual 표지 누적 룰 정합. AIGC 어셋 자국 일관.

### PATCH 6 — EP05 / S#3 / [DIALOGUE]

- **문제:** ISOLDE의 Mate 단어 응답이 인간 측이 Mate 개념을 이미 안다고 명시 → 정보 비대칭 약화 (페르소나 01·09)
- **원인 판정:** 정보 설계
- **FIND:**
  ```
  VAEL: Mate.
  ISOLDE (barely): That is not a thing your kind says to mine.
  VAEL: My kind does not say it twice.
  ```
- **REPLACE:**
  ```
  VAEL: Mate.
  ISOLDE (barely): That is not a word I know.
  VAEL: You will.
  ```
- **이유:** ISOLDE가 단어를 받되 의미는 모름 유지. 베일의 응답 "You will" → 유료 의미 노출 약속. 정보 비대칭 보존.

### PATCH 7 — EP06 / S#3 / [Visual]

- **문제:** EP04 손목 화염 자국 회수 — EP05 패치만으로는 누적 회수 부족 (페르소나 03·06)
- **원인 판정:** 정합성 (시각 표지 누적)
- **FIND:**
  ```
  He raises it slowly into the wall-torch light — palm-down, then turns it palm-up. The pale gold mark on her inner wrist is steady now — no flicker, no fade.
  ```
- **REPLACE:**
  ```
  He raises it slowly into the wall-torch light — palm-down, then turns it palm-up. The pale gold mark on her inner wrist is steady now — no flicker, no fade — and the thin scorched-line traced over it by his flame remains, unfaded above the gold.
  ```
- **이유:** EP04 화염 자국이 EP06 공개 손 키스 씬에서도 명시되어 누적 표지 일관.

### PATCH 8 — EP08 / S#5 / [DIALOGUE]

- **문제:** parenthetical 두 톤 동시 지시 (almost a smile, almost a warning) → actor 모호 (페르소나 04)
- **원인 판정:** 대사
- **FIND:**
  ```
  VAEL (low, almost a smile, almost a warning): On my mouth. Not yours.
  ```
- **REPLACE:**
  ```
  VAEL (low, almost a warning): On my mouth. Not yours.
  ```
- **이유:** 단일 톤 — alpha 위계 라인의 임팩트 살림. 미세 smile 디테일은 actor 자율.

## 보류 항목

- **🟢 EP03 / S#4 베일 "Because I haven't yet decided what you are to me"** — 작품 자율 영역. 알파 자제 + 거리 회복 motivation 작동, 변경 시 의미 손실.
- **🟢 EP01 / S#1 베일 머리 색 명세 (lustrous black vs 흑갈색)** — lustrous black ↔ dark brown-black 톤 차이 정합 가능. 비주얼 락에서 흑갈색은 dark brown to black 톤을 모두 포함하는 우산 — 본문 lustrous black는 그 안. 위반 X.
- **🟢 EP05 / S#4 "kingdom has a second war"** — 작품 자율. 베일 cadence가 약간 문어체로 가는 것 자체가 다크 로맨타지의 Dragon Lord 톤 정합.
- **🟢 EP02 / S#3 헤어 lustrous 표지** — Look 2 reveal 의상 중심 묘사로 충분. 어셋 일관은 EP1 첫 등장에서 lustrous 명시 → 후속 회차 일관 가능.
- **🟢 EP06 / S#4 herald "asks audience"** — 작품 자율 (적대자 강경 vs 외교적 발화는 작품 톤 자율 영역).

## 새 문제 발생 가능성

- **EP3 ALDRIC 익명화 후 EP11+ ALDRIC 명시 비트의 강도 점검 필요** — 청사진 12-6에서 ALDRIC 명시는 EP35 본격이지만 유료 초반 EP11+에서 첫 호명 가능. ripple — 청사진 환류 권장.
- **EP5 / EP6 손목 화염 자국 회수 후 EP7 회의실 씬에 동일 자국 명시 누락 확인 필요** — EP7 / S#4의 화염이 다시 그 자국 위로 흐름. 새 자국과 기존 자국이 겹쳐 누적 명료한지 EP7 [Visual] 재확인 권장 (현재는 새 화염 추가 묘사로 자연 누적 — 별도 패치 불요).
- **EP5 / S#3 Mate 응답 모호화 후 시청자가 ISOLDE가 비전 모르는 상태로 비치는 위험** — 다만 능동성은 EP6 자발 옆자리 + EP8 자발 마킹으로 회수 → F-B(여주 수동) 코드 회피 정합.
