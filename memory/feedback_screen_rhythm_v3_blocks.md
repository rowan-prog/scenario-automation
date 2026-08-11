---
name: screen-rhythm-v3-blocks
description: "EP 양식 v3 — 영상 리듬 5블록 신설 (MONTAGE·VO·FLASHBACK·INSERT/CUTAWAY·INTERCUT). 옛 v2 (장면 5블록만) = 화면 선형화 근본 원인. 매 EP 영상 리듬 1개+ 강제·후반부 반복 위험 EP = 2개+. 2026-05-19 V16 통합 피드백."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2d65e927-1cd5-4df0-bd23-1493c3adfb18
---

> **근본 진단:** 옛 EP 양식 v2 [VISUAL/ACTION]/[KEY CAMERA]/[DIALOGUE]/[GRAPHIC/UI]/[END HOOK] = 한 씬 단위·한 공간·한 시간 작성 강제 → 시간순 진행·정면 대화 반복·VO/플래시백/몽타주 차단 = 화면 선형화. OFFERING V14·V15·V16 모든 정정 = 본문 단위 미세 patch·영상 언어 부재 = 같은 함정.

## 룰

**EP 양식 v3 = 장면 5블록 + 영상 리듬 5블록 = 10 블록.** 매 EP 영상 리듬 1개+ 필수·후반부 반복 위험 EP = 2개+.

## 영상 리듬 5 블록

### 1. [MONTAGE]
- **기능:** 시간 압축·여러 짧은 컷·반복 비트를 한 화면 흐름에 담음
- **양식:** 1 비트당 1줄·5-15 비트
- **사용 위치:** 후반부 임신 build·문 잠금 반복·산후 회복 등 시간/반복 표현
- **예시:**
```
[MONTAGE]
Vael locks the same door at dawn.
Belly grows under silk.
Kiran reports from the same threshold.
Ridge eyes open then close.
Candle burns to a stub.
Bedsheets fresh, then crumpled, then fresh.
Vael's hand on her belly more careful each night.
Isolde turns his hand to a different spot.
Mark close-up — fading, darkening, fading again.
Vael's eyes awake at dawn.
```

### 2. [VO]
- **기능:** 감정·시간 압축·외부 관찰자 객관화
- **양식:** 화자 명시 `(V.O.)` · 1-2문장 이하 · 설명·문학체 금지
- **사용 위치:** 임신 중 감정·산후 회복·외부 시점 압축·love confession 직전
- **예시 (좋음):**
```
[VO]
ISOLDE (V.O.): The keep did not get smaller. He made the world stop at the door.
```
- **예시 (나쁨·회피):**
```
ISOLDE (V.O.): In the prison of his love, I learned the shape of my own desire...
```

### 3. [FLASHBACK]
- **기능:** 1-2초 insert·감각 회수·과거 비트 재호명
- **양식:** 시간·위치 명시·대사 재생 금지 또는 한 단어만·길지 않게
- **사용 위치:** 작품 전체 2-3회 (특정 비트 회수 시점만)
- **예시:**
```
[FLASHBACK]
EP01 — Isolde's chained wrist on the cart floor. Iron biting skin. 1 second.
```
또는:
```
[FLASHBACK]
EP05 — Her hand turning inside his. Her fingers closing on his thumb. 2 seconds.
```

### 4. [INSERT/CUTAWAY]
- **기능:** Object·Body·Detail close-up
- **양식:** 단일 이미지 1초·정보 또는 상징
- **사용 위치:** 시그니처 소품 회수·body 부분·환경 detail
- **예시:**
```
[INSERT]
Iron link in the cradle corner — melted, forged into the wood. EP01 chain visible at the join.
```
또는:
```
[CUTAWAY]
Wet pebble on the bench. First daughter's small handprint on the stone.
```

### 5. [INTERCUT]
- **기능:** 두 공간 동시 진행·cross-cut 표기·긴장·재점화 cadence
- **양식:** "공간 A: ... / 공간 B: ..." 또는 "INTERCUT — A / B"
- **사용 위치:** 외부 위협 + 내부 사적 공간 동시 진행
- **예시:**
```
[INTERCUT]
Corridor: Kiran's four men at the chamber door. Hands on hilts.
Chamber: Vael's hand on her belly. Slow circle. Her breath even.
```

## 적용 가이드

### EP당 영상 리듬 블록 권장 분포

| EP 범위 | 권장 블록 |
|---|---|
| EP01-05 (hook·시작) | INSERT/CUTAWAY 1-2개 (chain·pendant 시그니처 도입) |
| EP06-15 (관계 build) | VO 1개 (Isolde 감정 압축) + INSERT 1개 |
| EP16-25 (mate seat·임신 감지) | INTERCUT 1개 (외부 적·내부 사적) + INSERT 1개 |
| EP26-35 (임신 build·반복 위험) | MONTAGE 1개 + VO 1개 |
| EP36-40 (출산 전후) | MONTAGE 1개 (산 전 압축) + VO 1개 + FLASHBACK 1개 (EP01·EP05 회수) |
| EP41-50 (HEA build·둘째) | MONTAGE 1개 (recovery) + FLASHBACK 1개 (love confession 직전) + INSERT 1개 (cradle iron·wet pebble) |

### 영상 리듬 블록 = "장면 블록과 별도 섹션"

EP 본문 구조 예시:
```
# EP30

## S#1 — Chamber. Night.
[VISUAL/ACTION] ...
[KEY CAMERA] ...
[DIALOGUE] ...
[GRAPHIC/UI] ...
[END HOOK] ...

## S#2 — Pregnancy montage covering 3 weeks
[MONTAGE]
- Vael locks the door at dawn.
- Belly grows under silk.
- ... (8-12 비트)

## S#3 — Chamber. Late Night.
[VO]
ISOLDE (V.O.): ...
[VISUAL/ACTION] ...
[DIALOGUE] ...
[END HOOK] ...
```

## 자가 검수

1. **이 EP에 영상 리듬 블록 ≥1개 있는가?** (없으면 작업 중단·추가)
2. **장면 5블록만 반복이면 = 화면 선형화. 다른 5블록 1개+ 강제 삽입.**
3. **후반부 (반복 위험·EP30+) = 영상 리듬 ≥2개 강제.**

→ 1개라도 NO = 본문 재작성 권장.

## 옛 시스템 룰과 정합

- `feedback_episode_format_v2.md` (옛 5블록 baseline) → v3 보강·5블록 → 10블록.
- `config/hard_rules.md` 1번 룰 정정 (v3 양식 명시).
- `prompts/phase_4_episode_writing.md` raw script 룰과 함께 새 baseline.

## 절대 한 줄

> **장면 5블록 + 영상 리듬 5블록 = v3. 매 EP 영상 리듬 1개+. 후반부 2개+.**

관련: [[no-theater-tone]] / [[dark-romance-relationship-centered-v2-3]] / [[female-gaze-camera-polish]] / [[master-platform-safe-dual-version]]
