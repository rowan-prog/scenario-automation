---
name: 검토 강도 시스템 — Verdict 4단계 + 자동 Trigger + 엄격 default
description: 페르소나 검토(phase_5) verdict 4단계 / 자동 패치 필수 trigger / 🔴+🟡 모두 필수 수정 / 🟢 페르소나별 가변 / 엄격 default. 무결 통과 의심 시 재검토
type: feedback
originSessionId: 764e3acd-d10a-4307-82be-cb216d64afc2
---
scenario-automation 검토 사이클(phase_5)의 강도·verdict·자동 trigger 시스템.

**Verdict 4단계 (각 페르소나 산출):**
- 통과 (결함 0건)
- 조건부 통과 (🟢만 발견)
- 패치 필수 (🔴 또는 🟡 발견)
- 재설계 (Hard Lock 다수 위반)

**자동 패치 필수 trigger (Soft Lock 회피 불가):**
- 03 Continuity 논리 오류 → 🟡
- 05 Commerciality Paywall/Payoff 약함 → 🟡
- 07 Genre Pleasure 장르 쾌감 약화 → 🟡
- 08/09 Viewer 이탈 코드 감지 → 🟡

**등급별 처리:**
- 🔴 + 🟡 = 필수 수정 (변경 — 기존 🟡는 "권장")
- 🟢 = 페르소나별 가변:
  - 03/05/07/08/09 → 수정 권장
  - 01/04 → 작품 자율 (Soft Lock — 강도·말맛)
  - 02 → 제작 결정
  - 06 → 참고 (룩 변형 락 위반 시는 🔴/🟡 자동)

**검토 강도 default = 엄격.** 사용자 명시 안 하면 자동 적용. 페르소나당 평균 1-3 🟡 발견 목표. 0 🟡 → 검토 약함 의심 → 재검토.

**4-Gate 진입 조건:** 모든 페르소나 verdict ≥ "조건부 통과". "패치 필수" 잔존 시 4-Gate 불가.

**말맛 보존 원칙:** 오류는 사이즈 무관 수정. 단 캐릭터 voice·cadence 최대 보존. 안전·밋밋 수정 누적 금지.

**"전체 순차" 검토 시 필수:** 01-07 + 작품 타깃 정렬 시청자 1개.

**Why:** 사용자가 2026-05-08 명시 — 두 작품(TITAN BORN·THE OFFERING) Round 1 무결 통과(🟡 0건)가 비현실적이라고 지적. AI 검토가 작품을 방어하는 자세에 빠져 결함 hunting 안 함. 페르소나 시스템 자체는 합리지만 적용이 느슨했음. 새 시스템으로 0 🟡 무결을 의심 신호로 처리.

**How to apply:**
1. phase_5 호출 시 default 강도 = 엄격. 페르소나당 결함 적극 hunting.
2. 자동 trigger 페르소나(03/05/07/08/09)는 Soft Lock 분류 불가. 핵심 영역 결함 잡으면 즉시 🟡.
3. 🟡 등급은 모두 패치 (말맛 손상 위험 영역만 신중).
4. 🟢는 페르소나 매트릭스 따라 가변.
5. 4-Gate 진입 전 모든 페르소나 verdict 점검.
6. phase_5·phase_6·phase_7·CLAUDE·PORTING § N에 등재됨 — 메모리는 백업.
