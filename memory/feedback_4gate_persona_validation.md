---
name: 4-Gate ↔ 페르소나 검증 흐름 — 4-Gate 자체 수정 X / production_guide·쾌감 > 4-Gate
description: phase_7 4-Gate 발견은 항상 대응 페르소나 검증 거쳐야 수정 가능. 4-Gate 자체 수정 권한 0. production_guide·작품 쾌감·캐릭터 매력이 4-Gate 24 체크리스트보다 상위.
type: feedback
originSessionId: 84137f65-ae18-4af2-b7fd-da37ae3ce880
---
phase_7 4-Gate (Structure / Narrative / Script / Production)는 **별개 수정자가 아니다**. 4-Gate에서 미통과 항목 발견 시 **항상 대응 페르소나의 타당성 검증을 거쳐야 수정 가능**.

**Why:** 2026-05-12 사용자 명시 — "4-Gate가 페르소나와 다른 기준으로 검토하면 중복 + 페르소나 벗어난 검토 우려. 4-Gate에서 수정해버리면 페르소나 판단과 많이 틀릴 수 있다. 4-Gate도, 기본적으로 프로덕션 가이드, 절대 원칙을 해칠 수 없다. 작품의 쾌감을 해칠 순 없다." 페르소나의 정밀한 분야별 시각이 4-Gate의 형식적 24 체크리스트에 의해 무력화되면 작품 쾌감·캐릭터 매력 약화 위험.

**How to apply:**

## 우선순위 (최상위)

> **production_guide · 작품 쾌감 · 캐릭터 매력 > 4-Gate 24 체크리스트**

페르소나 = 이 우선순위의 수호자. 4-Gate 자체 수정 권한 0.

## Gate ↔ 페르소나 매핑

| Gate | 주 페르소나 | 보조 |
|---|---|---|
| **Structure** (페이월·보상 단계·정보 설계·결제 동력) | 05 Commerciality · 07 Genre Pleasure | 03 Continuity (정보 설계) |
| **Narrative** (캐논·세계 규칙·관계·정보 흐름) | 03 Continuity · 06 Visual Lock | 07 Genre Pleasure (캐릭터 매력) |
| **Script** (대사·영어·캐릭터 보이스) | 04 Dialogue · 01 Intimacy (sensual 대사) | 07 Genre Pleasure (장르 톤) |
| **Production** (AIGC 제작·비주얼 락·자국 누적·언어 일원화) | 02 AIGC Production · 06 Visual Lock · 01 Intimacy (sensual 자국) | 자동 검출 룰 |

시청자 페르소나 (08·09)는 Gate 직접 매핑 X. 모든 Gate에 영향 (이탈 코드).

## 4-Gate 미통과 발견 시 흐름

```
[4-Gate 자체 평가 — 24 항목]
        ↓
[미통과 발견]
        ↓
[Gate ↔ 페르소나 매핑 호출]
        ↓
[페르소나 Fresh 타당성 검증]
   "이 4-Gate 발견이 진짜 결함인가, 아니면
    작품 쾌감·production_guide 원칙을 침해하는 4-Gate의 오판단인가?"
        ↓
   ┌────────────┬──────────────┬─────────────┐
[동의 (타당)]  [거부]          [충돌]
   ↓              ↓                    ↓
phase_6 패치  4-Gate 발견          사용자 결정
+ phase_5     reject + 통과         (PushNotification)
재검토         (사유 + 원문 인용)
+ phase_7
재진행
```

## 페르소나 거부 가능 사유 (예시)

| 사유 | 거부 페르소나 |
|---|---|
| "이 수정은 페이월 응축을 약화시킨다" | 05 · 07 |
| "이 수정은 다크 로맨타지 거리 차단을 해친다" | 07 · 09 |
| "이 수정은 캐릭터 매력을 죽인다 (안전·밋밋)" | 07 |
| "이 수정은 production_guide Section X 위반" | 해당 페르소나 |
| "이 수정은 sensual 강도를 약화시킨다 (북미 기준 미달)" | 01 · 07 |
| "이 4-Gate 항목은 Soft Lock 영역 — 작품 자율" | 전 페르소나 |

## 예외 (페르소나 검증 없이 즉시 처리 가능)

1. **자동 검출 룰 (Production Gate 한정):**
   - 한국어 검출 (`\p{IsHangulSyllables}` / `[ㄱ-ㆎ]`)
   - 헤더 메타 (`**Function:**`, `**Information:**`, `**Cut:**` 등) 잔존
   - Footer (`**Episode Update:**`, `**Series Update:**`) 잔존
   - 헤더 양식 위반 (`# [작품] — EP[NN]: [TITLE]` 외)
   - EP 누락·중복
   - 블록 카운트 불일치
   - separator 일관성 위반
   → 룰 기반 검증·판단 영역 X·즉시 수정.

2. **Soft Lock 영역 (production_guide Section 0-3):**
   - 톤·인티머시 강도·캐릭터 매력 강약·대사 방식·카메라 직접성 등 작품 자율 영역
   → 페르소나 호출 없이 즉시 reject (Soft Lock 분류).

## 라운드 한계

- phase_6 패치 → phase_5 재검토 → phase_7 재진행 = 1 라운드 카운트
- 라운드 5회 도달 시 사용자 판단 요청 (Soft Lock 분류 또는 작업 보류)

## 보고서 표기 (필수)

4-Gate 보고서에 다음 명시:
- **페르소나 검증 호출 내역:** Gate별 어느 페르소나 호출했는지
- **페르소나 판정:** 동의 / 거부 / 충돌
- **거부 시:** 거부 사유 + 페르소나 원문 인용 + reject 처리 명시
- **동의 시:** phase_6 패치 권장 사항
- **충돌 시:** 충돌 페르소나·각 사유·사용자 결정 대기 표시

## 관련 메모리

- `feedback_review_master.md` (검토·라운드 마스터 통합 — Verdict 4단계·공격성 7원칙·라운드 독립)
- `feedback_genre_reward_modes.md` (보상 단계 매트릭스 — 페르소나가 페이월 약화 판정 근거)
- `feedback_paywall_force_protection.md` (페이월 결제유도력 보호 절대)
- `feedback_north_american_explicit_standard.md` / `feedback_north_american_judgment_baseline.md` (북미 수위·판단 기준)
- `feedback_dark_romantasy_engine.md` (작품별 장르 매트릭스 — 거리 차단 약화 판정 근거)
