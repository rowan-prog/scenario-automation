---
name: 2026-05-15
description: "비주얼 락 = AIGC 어셋 생성 고정용. 첫 의상·바뀐 의상 첫 등장·재착용 시 [VISUAL/ACTION]에 어셋 식별 가능한 묘사 필수. 직전과 동일 의상 = 묘사 X."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 462b4a02-4290-4164-a105-ac1f2ff0ecca
---

# 비주얼 락 시스템

## 핵심 룰 (2026-05-15 사용자 명시 — 본질 정정)

> **비주얼 락 = AIGC 어셋 생성 고정용 DB.**
> **대본 [VISUAL / ACTION]은 어떤 어셋을 호출하는지 식별 가능해야 한다.**
> **첫 의상 / 바뀐 의상 첫 등장 / 재착용 시 = 묘사 필수.**
> **직전과 동일 의상 = 묘사 X (같은 어셋).**

이전 룰("[Visual]에 룩 디테일 X (대부분)" — 2026-05-12)은 **폐기.** 어셋 식별이 안 되면 사람이 일일이 추출해야 해서 훨씬 까다로워진다. 자동화 효율을 위해 대본에 어셋 식별자가 들어가야 한다.

## Why

사용자 명시 (2026-05-15):
> "비주얼 락을 거는 이유는, 이를 바탕으로 어셋을 생성하기 위함이다. 대본에 포함된 것만 있으면, 사람이 다 추출해서 정돈해야한다. 훨씬 까다롭다. 따라서, 첫 의상, 바뀐 의상 첫 등장일 땐 의상 묘사가 있어야하나, 같은 의상일 땐 할 필요 없다. 그러나 이전에 묘사 됐어도, 또 입는 경우(혹시라도) 있다면 그때도 어떤 의상 입었는지 묘사되어야한다."

## 의상 묘사 룰 (필수)

| 상황 | [VISUAL / ACTION] 묘사 | 비주얼 락 등재 |
|---|---|---|
| **첫 등장 (첫 의상)** | 필수 — 색·소재·실루엣·핵심 디테일 | O |
| **바뀐 의상 첫 등장** | 필수 — 새 어셋 정의 | O (변형 락 추가) |
| **직전 씬과 동일 의상 (연속 회차·동일 시간대)** | X — 같은 어셋 호출 | — |
| **이전에 묘사된 의상 재착용** | 필수 — 어떤 어셋인지 식별 (짧은 식별자) | — (이미 등재됨) |
| **사건 기능 있는 변화** (각성 표지·전투 흔적·신분 변경) | 필수 — 변화 디테일 | O (변형 락 추가) |
| **사건 기능 없는 부분 변화** (먼지·일상 피로) | X | — |

### 재착용 시 — 짧은 식별자

이미 비주얼 락에 등재되고 대본에서 이미 묘사한 의상을 다시 입을 때는 풀 묘사 X. **어떤 어셋인지 식별만.**

**좋은 재착용 명시:**
- `LIVIA back in the white silk robe.`
- `KAEL in his bronze chestplate again, the chain marks visible.`
- `Sienna in her warrior leathers from EP3.`

**나쁜 재착용 명시 (풀 묘사 반복):**
- `LIVIA in a white silk robe, silver pendant at her throat, dark hair loose past her shoulders.` (EP1에서 이미 묘사 → 반복 X)

## [VISUAL / ACTION] 통합 원칙

새 양식(2026-05-15)에서는 [Visual]·[Camera]·[FX]·[Action]이 [VISUAL / ACTION] + [KEY CAMERA] + [DIALOGUE] + [GRAPHIC / UI] + [END HOOK]로 재편. 의상 묘사는 [VISUAL / ACTION] 안에서 자연스럽게.

### 통합 묘사 예시 (첫 등장 + 사건)

```
[VISUAL / ACTION]
LIVIA enters the temple gate in a white silk robe, a silver pendant at her throat, her dark hair loose past her shoulders. She kneels before the dragon's altar. The pendant catches the torchlight.
```

### 통합 묘사 예시 (변경 + 사건 기능)

```
[VISUAL / ACTION]
LIVIA steps into the throne room. The silver pendant is gone — a black iron collar marks her throat, the dragon's seal. Her hands are bound at the wrist. ADRIAN watches from the dais.
```

### 통합 묘사 예시 (재착용 — 짧은 식별자)

```
[VISUAL / ACTION]
LIVIA back in the white silk robe. She places the letter on the altar. The robe sleeves brush the stone.
```

## 비주얼 락 파일 위치·양식

### 파일
- `projects/[작품명]/[작품명]_04_visual_lock.md` (청사진 부속)
- 단일 파일, 모든 캐릭터 포함

### 캐릭터 디테일 수준

| 카테고리 | 비주얼 락 등재 | 첫 등장 [VISUAL/ACTION] 묘사 |
|---|---|---|
| **주연급** (주인공·메인 히로인·남주·핵심 적대자) | 디테일 (9 섹션 모두 + 변형 락 2-4단계) | 디테일 통합 묘사 |
| **메인 빌런급** | 디테일 (위협 표지·정체성 마크) | 디테일 통합 묘사 |
| **조연급 (락 등재)** | 러프 (인상·체형·핵심 의상 1-2 요소) | 중간 — 인상·체형·핵심 의상 |
| **비락 보조·엑스트라** | X | 짧고 명료 — 1줄·5-10 단어 |
| **일회성 괴물·동물** | X | 짧고 명료 — 종·크기·색·핵심 특징 1-2개 |

### 짧은 묘사 예시 (비락)

**인물:**
- `A gaunt courier in muddy boots, hood pulled low.`
- `A bald guard in palace livery.`
- `A thin maid with a chipped tray.`

**괴물·동물:**
- `A black-furred wolf, one ear notched.`
- `A grey warhorse with iron-shod hooves.`
- `Three crows circling overhead.`

## 환류 사이클 (필수)

### A. 스크립트 → 비주얼 락
- 집필 중 새 어셋 식별 (예: "검은 비단 드레스" 신규 의상) → visual_lock 즉시 변형 락에 등재
- 새 캐릭터·괴물·동물 재등장 가능성 발견 → visual_lock 러프 등재

### B. 비주얼 락 → 스크립트
- 비주얼 락 수정 시 영향 EP 본문 갱신
- 어셋 변경 (예: 색 변경) → 등장 EP 모두 점검

### 환류 로그
- visual_lock 끝에 "환류 로그" 섹션 한 줄 기록

## 검토 단계 정합 검사 (phase_5)

### 검토 영역
- **의상·동작·사건 정합 검사** — 어셋 호출 정합성
- 예: visual_lock 변형 락 EP15부터 명시인데 EP10에서 변형 룩 등장 = 🔴
- 예: visual_lock에 등재된 검 명시인데 EP5에서 활 사용 = 🟡

### 페르소나 책임
- **02 AIGC Production Director** — 어셋 정합·룩 변형 1차 검토
- **06 Visual Appeal Character Lock Auditor** — 어셋 식별 누락·과잉 묘사 검토
- 다른 페르소나도 위반 발견 시 보고

### 자동 trigger
- 첫 등장 묘사 누락 = 자동 🟡
- 동일 의상 반복 풀 묘사 (재착용 식별자 수준 초과) = 자동 🟡
- 변형 락 미등재 새 의상 = 자동 🔴

## 단계별 적용

| 단계 | 비주얼 락 작업 |
|---|---|
| phase_3 (완성 청사진) | `04_visual_lock.md` 생성 (주연 디테일 + 조연 러프) |
| phase_4 (스크립트 집필) | visual_lock 정독 + [VISUAL/ACTION] 어셋 식별 + 새 어셋 환류 |
| phase_5 (검토) | 02·06 페르소나 어셋 정합 검사 |
| phase_6 (패치) | 비주얼 락 수정 시 영향 EP 환류 |
| phase_7 (최종고) | 4-Gate Production = 어셋 정합 자동 fail trigger |

## 사건 기능 있는 변화 (추가 묘사 + 변형 락 등재)

| 변화 | 기재 사유 |
|---|---|
| 권능·각성 표지 (눈 색·문양 발광·갑주 발현) | 각성 사건 = 정보 갱신 |
| 상해·전투 흔적 (찢긴 옷·이마 피·손목 자국) | 갈등 결과 = 상태 갱신 |
| 신분·정체 변경 룩 (왕좌 등극·갑주 첫 착용·가면 벗음) | 정체 reveal = 정보 갱신 |
| 공개 마킹·소유 표지 (목·손목 자국·반지·문장) | 관계 갱신 |
| 타락·변질·죽음 표지 (창백함·핏기·검은 정맥) | 상태 갱신 |
| 의상 단계 진화 (얌전 → 과감 → 권력자) | 캐릭터 톤 변화 = 사건 |
| 무기·소품 획득·상실 | 사건·주도권 갱신 |

### 사건 기능 없음 = 묘사 X
- 일상 옷 갈아입기 (날짜·상황 변경 — 같은 톤·계열 의상이면 락 변형도 X)
- 사소한 액세서리 추가·제거 (정체성 X)
- 먼지·일상 피로 (사건 결과 아니면)

## How to apply

- phase_4 (집필) 시 매 씬 진입에 자문: 이 인물이 어떤 어셋(=의상)인가? 직전 씬과 동일한가?
  - 동일 → 묘사 X
  - 첫 등장 / 변경 / 재착용 → 어셋 식별 가능하게 묘사
- 새 어셋 발견 시 visual_lock 즉시 환류
- phase_5 검토 시 02·06이 자동 trigger 적용

## 핵심 한 줄

> **대본은 어떤 어셋을 호출할지 식별 가능해야 한다. 첫 등장·변경·재착용 = 묘사. 직전과 동일 = 묘사 X.**
