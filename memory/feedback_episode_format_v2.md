---
name: ep-v2-visual-action-key-camera-dialogue-graphic-ui-end-hook-2026-05-15
description: 새 EP 표준 양식. FX/AUDIO 블록 제거 (사운드는 VISUAL/ACTION 통합). KEY CAMERA는 스토리·상업 엔진 중요 컷만. 미세 디테일 X — 연출/제작팀 영역.
update_2026-05-17:
  - "각 블록에 내용 없을 시 'None.' 또는 'None except above.' 표시 허용 (양식 위반 X)"
  - "5 블록 순서 (VISUAL/ACTION → KEY CAMERA → DIALOGUE → GRAPHIC/UI → END HOOK) 유지·내용 없는 블록도 표시"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 462b4a02-4290-4164-a105-ac1f2ff0ecca
---

# EP 양식 v2 (2026-05-15 사용자 표준)

## 핵심 (사용자 명시)

> **양식은 아래로 고정.**
> **비주얼/액션 지문 = 고강도가 아님. 연출가 및 제작팀이 참고할 뿐임. 미세 디테일 X — 핵심만.**
> **카메라 지문도 다 쓸 필요 없다. 스토리상·상업 엔진상 중요한 컷만.**
> **FX/AUDIO도 집필 영역이 아니다. 스토리상 중요한 소리는 [VISUAL / ACTION]에 통합.**
> **대사를 맛깔나게 + 씬·상황 구성이 중요.**

이전 4 블록 ([Visual] [Camera] [DIALOGUE] [FX])은 **폐기.**

## 새 양식 (5 블록 — 일부 선택)

```
EP[N] — [TITLE]

S#[번호] — [LOCATION / SUB-LOCATION / TIME or CONTINUOUS]

[VISUAL / ACTION]
(상황·동작·블로킹·시각 정보 통합 단락. 스토리상 중요한 소리도 여기.)

[KEY CAMERA]
(스토리·상업 엔진 중요한 컷만 — 보통 2-5 cuts. 선택.)
SHOT TYPE: 무엇이 잡히는가 한 줄.

[DIALOGUE]
CHARACTER: line (3-10 단어 이하)
CHARACTER: line

[GRAPHIC / UI]    ← 필요한 씬만
[END HOOK]        ← 회차 마지막 씬만
```

## 블록별 룰

### [VISUAL / ACTION] — 필수 (모든 씬)
- 상황·동작·블로킹·시각 정보·스토리상 중요한 사운드 비트 통합
- 미세 디테일·연출 세부 X (제작팀 영역)
- 핵심만 명료하게
- 어셋 식별 (의상 첫 등장·변경·재착용) 포함 — `feedback_visual_lock_system.md` 참조

### [KEY CAMERA] — 선택 (스토리·상업 엔진 중요 컷만)
- 모든 컷 명시 X (연출가 재량)
- 스토리상 또는 상업 엔진상 (섹슈얼 인서트·감정 클로즈업·페이월 컷·광고 컷) 중요한 컷만
- 미명시 = 연출 재량
- 명시할 때만 그 컷 의도 전달

### [DIALOGUE] — 필수 (대사 씬)
- 캐릭터별 말투·맛 살리기 — 살아있는 대사
- 라인 3-10 단어 이하 우선
- 캐릭터 voice 일관성

### [GRAPHIC / UI] — 선택
- UI 알림·문서·뉴스 헤드라인·warrant·증서·시스템 표시
- 화면 그래픽 노출 시만

### [END HOOK] — 회차 마지막 씬 (마지막 회차 제외)
- 다음 회차로 끄는 한 줄
- 마지막 회차 = 자연 엔딩 (Hard Cut X)

## 제거된 블록

### [FX] / [AUDIO] — 별도 블록 X
- 사운드·음악은 연출/제작팀 영역
- 스토리상 중요한 소리 (문 닫히는 소리·발자국·전화 벨 — 사건 비트가 되는 소리) = [VISUAL / ACTION]에 통합

### 모든 카메라 컷 나열 X
- [Camera] 4-7 shots → 폐기
- [KEY CAMERA]에 중요 컷만

## 사용자 표준 예시

```
S#4 — PUBLIC RELAY / NO FORGIVENESS

[VISUAL / ACTION]
The dock hears the recording. Low-rank workers stare at Drake. Sienna lowers her blade as the old order plays. Jax drops old porter tags at Drake's feet.

Public relay fragments stutter across the board: a sealed door closing, porter tags left behind, Drake's badge before the crack. The images are short and physical, more accusation than memory.

Drake denies the record. Jax refuses the denial. Victor reframes the problem: not whether the proof is real, but whether Jax is allowed to keep producing proof.

[KEY CAMERA]
CLOSE: Drake's face draining as the recording plays.
PUBLIC RELAY CUTS: Sealed door, abandoned tags, uncracked Drake badge.
INSERT: Porter tags hitting the floor.
CLOSE: Victor cutting the relay.

[DIALOGUE]
DRAKE: That's edited.
JAX: They don't get edited back to life.
VICTOR: Then we remove the source.

[GRAPHIC / UI]
Kross Warrant: JAX MERCER.

[END HOOK]
The black warrant activates with Jax's name on it.
```

## Hard Cut (중간 EP 마지막) vs 자연 엔딩 (마지막 EP)

| EP | EP 마지막 |
|---|---|
| 중간 EP (1, 2, ..., 49) | `Hard Cut` 마커 강제 (또는 [END HOOK] 한 줄) |
| 시리즈 종결 EP (마지막 회차) | `Hard Cut` 금지 — Pull back / Tilt up / Held final image + `Fade Out.` / `End.` / 마커 없음 |

## 핵심 원칙

- **대사 맛깔나게 + 씬 구성·상황 구성이 핵심.**
- [KEY CAMERA]·[GRAPHIC/UI]·[END HOOK]은 그 씬에 필요할 때만.
- 카메라·FX 디테일에 매달리지 말 것 — 연출/제작팀 일.
- 씬 자체 비트·인물 관계·주도권 갱신·사건 흐름이 명확하면 [VISUAL / ACTION] + [DIALOGUE] 둘만으로도 회차 작동.

## 통합 검증 룰 갱신 (필수)

기존 `feedback_final_consolidation_three_files.md`의 검증 항목:
- ❌ 옛: "Visual = scene count / Camera·DIALOGUE·FX = scene count + end image"
- ✅ 새: "[VISUAL / ACTION] = scene count / [DIALOGUE] = 대사 씬 / [KEY CAMERA]·[GRAPHIC/UI]·[END HOOK] = 선택 (사용 시만 카운트)"

## 적용 시점

- **즉시 (2026-05-15부터):** phase_4·protocol_premium_pilot·phase_a_2 모든 신규 EP
- **기존 EP들:** 그대로 유지 (소급 적용 X). 단, 사용자 명시 시 일괄 변환 가능
- **검토 페르소나:** 02·06이 양식 정합 자동 검증

## How to apply

- phase_4 진입 시 본 양식 자동 적용
- 매 씬 [VISUAL / ACTION] + [DIALOGUE] = default
- [KEY CAMERA]·[GRAPHIC/UI]·[END HOOK]은 필요 씬에만
- [FX] 블록 작성 금지

## 핵심 한 줄

> **대본은 사건·동작·대사. 카메라·FX 디테일은 연출/제작팀에 맡긴다.**
