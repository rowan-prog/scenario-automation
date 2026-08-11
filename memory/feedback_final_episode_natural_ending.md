---
name: hard-cut
description: 작품의 마지막 회차(시리즈 종결 EP)는 Hard Cut 금지. 자연스러운 fade·여운·시청자 만족감 충족. 중간 EP의 Hard Cut과 구분.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 868e03f4-e9d0-41c4-ac4d-5b5b74c6d554
---

작품의 **마지막 회차(시리즈 종결 EP, 예: EP50)**는 `Hard Cut` 마커 사용 금지. 자연스러운 여운으로 마무리.

**Why:** 사용자 명시 (2026-05-13) — "마지막화는 Hard Cut일 필요 없음. 자연스럽게 여운을 남기며, 시청자 만족감을 충족시키는 엔딩." 중간 EP의 Hard Cut은 다음 화 결제 동기·궁금증 유발 목적이지만, 마지막 화는 회수·정산·여운이 핵심.

**How to apply:**

## 1. 적용 범위

- **마지막 회차 = 시리즈 종결 EP** (보통 EP50, 또는 작품별 총 화수의 마지막)
- 시즌제 작품의 경우 시즌 마지막 EP도 동일 (작품 전체 종결과 시즌 종결 구분 가능)
- **무료/유료 경계 EP는 해당 X** (예: EP8은 페이월 — Hard Cut 정상 필수)
- **Heavy Gate EP는 해당 X** (단순 블록 heavy 트리거)

## 2. 마지막 회차 엔딩 룰

### 금지
- `Hard Cut` 마커 (대문자·소문자 무관)
- `Hard Cut.` (period 포함)
- 갑작스러운 BLACK
- 다음 EP 회수 fuse (이미 모든 약속 회수된 상태)

### 권장
- **자연스러운 카메라 마무리** — wide-out·pull back·slow zoom out·tilt up to sky/stars·dolly back
- **여운 비트** — final image held 길게·캐릭터 응시·환경 디테일·소리만 남는 정적
- **사운드 모티프 회수** — 시리즈 첫 EP에서 등장한 사운드 모티프 다시 (수미상관)
- **End** 또는 **Fade Out** 또는 그냥 **마커 없이** 마지막 [FX] 블록으로 마무리
- 자막 형식: `END.` / `FIN.` / 또는 표기 없이 — 작품 톤에 맞게

### 엔딩 비트 체크리스트

마지막 회차 마지막 씬은 다음 충족:

| 항목 | 기준 |
|---|---|
| **회수 완결성** | 무료 페이월 + 유료 페이월 + 마지막 paywall 약속 모두 회수 |
| **캐릭터 아크 완결** | 주인공·메인 mate·핵심 supporting 캐릭터 모두 종결 위치 |
| **여운 시각** | 마지막 컷이 안정·만족감·미래 암시 (혼란·미해결 X) |
| **상승 곡선** | EP1 시작 위치보다 정서적·서사적 위치가 명확히 상승 |
| **수미상관 가능** | EP1의 모티프(첫 라인·첫 시각·첫 사운드) 재현 또는 변주 |

## 3. 시스템 영향

### Hard Cut count 검증 수정

**기존:** `Hard Cut count = EP count`
**갱신:** `Hard Cut count = EP count - 1` (마지막 EP 제외)

또는 더 정확히:
- `Hard Cut count (non-final EPs)` = EP count - 1
- `Hard Cut count (final EP)` = 0

### 4 블록 룰 유지

마지막 회차 마지막 씬도 4 블록 (Visual / Camera / DIALOGUE / FX) 강제. 단 [Camera]에 `Hard Cut` 마커 자리에 `Fade Out.` / `Hold and Fade.` / 또는 BLACK held로 종결.

### 통합 FINAL.md 검증

`07_final/FINAL.md` 검증 시:
- Hard Cut count = 전체 EP 수 - 1 (마지막 EP 제외)
- 마지막 EP는 자연스러운 종결 확인

## 4. 예시 패턴

### 패턴 A — Pull back to wide (가장 일반)

```
[Camera]
... (씬 마지막 컷) → SLOW PULL BACK: characters on bed/throne/landscape → WIDE: full setting with characters small → TILT UP: sky / stars / dragon shadow → HOLD WIDE → FADE

[FX]
... sustained final hum, distant character motif, paired bond hum, slow fade to silence

Fade Out.
```

### 패턴 B — Final image held

```
[Camera]
... → ECU: final image (character expression / hand / mark / artifact) → HOLD → SLOW FADE

[FX]
... sustained note, character breath, environmental texture, slow fade

End.
```

### 패턴 C — Sound-led ending

```
[Camera]
... → BLACK (gentle)

[FX]
character motif (slow, sustained), environmental sound (lingering — 5+ seconds), final breath / line echo, silence held

(no marker — or simply "FIN.")
```

## 5. 적용 의무

- 작품 마지막 EP 집필 시 자동 적용 — Hard Cut 자동 제외
- phase_4 (집필) 가이드에 명시
- phase_7 (4-Gate) 검증 시 마지막 EP Hard Cut 발견 = 🔴 (즉시 수정)
- `07_final/FINAL.md` 통합 검증 시 마지막 EP Hard Cut 발견 = 🔴

## 6. 기존 작품 회고 적용

작품 완결 시점에 마지막 EP 검토:
- Hard Cut 마커 있으면 → 자연스러운 fade로 재작성
- [Camera] 마지막 블록 → pull back / tilt up / hold + fade
- [FX] 마지막 블록 → sustained motif + slow fade
- 마커 자리 → `Fade Out.` 또는 `End.` 또는 마커 없이 빈 줄

## 7. 관련 룰

- 3종 최종고 통합·검증: `feedback_final_consolidation_three_files.md`
- 4 블록 강제: phase_4 / production_guide
- 시나리오 영어 일원화: `feedback_script_english_only.md`

## 핵심 한 줄 결론

> **마지막 EP = Hard Cut 금지 + 자연스러운 여운 + 시청자 만족감 충족 엔딩. 모든 프로젝트 예외 X.**
