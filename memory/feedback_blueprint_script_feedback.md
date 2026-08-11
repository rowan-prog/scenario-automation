---
name: 청사진 ↔ 스크립트 환류 원칙
description: scenario-automation에서 집필된 스크립트가 청사진보다 더 강한 요소를 발견하면 청사진에 부분 환류. 모든 작품·트랙 적용
type: feedback
originSessionId: 764e3acd-d10a-4307-82be-cb216d64afc2
---
scenario-automation에서 청사진은 최상위 기준이나, **실제 집필된 스크립트가 더 좋은 요소(더 강한 비트·더 선명한 캐논·더 구체적인 비주얼·더 적절한 룩 변형·더 강한 cadence)를 발견한 경우, 그 요소를 청사진에 부분 업데이트**한다.

**Why:** 사용자가 2026-05-08에 명시. 청사진이 완벽할 수 없고, 집필 과정에서 더 나은 디테일이 자연스럽게 발견됨. 이 발견을 청사진에 환류하지 않으면 후속 화 집필이 청사진의 약한 부분을 그대로 답습. 이 원칙은 본 프로젝트만이 아니라 모든 작품·모든 트랙(메인·각색·외부 대본)에 동일 적용.

**How to apply:**
1. phase_4 집필 중 청사진보다 더 나은 요소 발견 시 — 청사진(`04_blueprint_full.md`)의 해당 항목 직접 편집.
2. 환류 대상: 캐릭터 캐논 보강 / 비주얼 락 디테일 / 룩 변형 / 관계 변화 지점 / 권능 단계 표현 / 정보 설계 미세 조정.
3. 환류 금지: Hard Lock 영역 (작품 정체성·핵심 결제 트리거·페이월 구조·트랙 분류). 변경 시 사용자 승인 필요.
4. 청사진 말미 "환류 로그"에 한 줄 기록 (예: `2026-05-08 EP18 — KORINNE 추가, 황금 winged sandals를 권능 도구로 등재`).
5. 이미 phase_3·phase_4 prompt + CLAUDE + PORTING § K에 등재됨 — 메모리 저장은 백업 + 단순 환기.

## 2026-05-16 보강 — Baseline 적용 디벨롭 시 환류 강제 (사용자 명시)

> **"새로 세운 기준, 진짜 매출이 잘 나오는 대본을 집필하기 위한 기준에 맞춰 디벨롭한 대본이, 청사진과 상이한 경우, 청사진의 디벨롭이 필요하다."**

### 새 룰
- 매출 baseline 8개 (`feedback_paid_vertical_viewer_psychology.md` 외 7) 적용해 무료회차·유료회차 디벨롭 시
- 디벨롭 결과가 청사진과 상이하면 **청사진 부분 디벨롭 필수**
- 특히 50화 작품 = 무료 완성 후 유료 진행 전 **청사진 정합 보장**

### 적용 흐름
```
청사진 (옛) → baseline 적용 EP 집필 → 청사진 ↔ EP 정합 검증 → 상이 부분 청사진 부분 업데이트 → 환류 로그 → 유료 진행
```

### 환류 대상 (baseline 적용 시 확장)
- 6 conversion 매핑 (`feedback_paid_vertical_6_conversion_patterns.md`)
- 메인·보조 결제 엔진 (`feedback_v3_17_payment_engines.md`)
- 50화 7 룰 정합 (`feedback_50_episode_serial_engines.md`)
- 시청자 심리 톤 (`feedback_paid_vertical_viewer_psychology.md`)
- A/B 엔진 분리 (`feedback_female_buy_engine_relational.md`)
- 캐릭터 성격·상황 매력 (3축)

### Hard Lock vs Soft Lock 재확인

청사진 Hard Lock (사용자 승인 필요):
- 작품 정체성
- 핵심 결제 트리거
- 페이월 구조
- 트랙 분류

청사진 Soft Lock (자율 환류):
- 화별 비트 디테일
- 캐릭터 voice·습관·매력 디테일
- 비주얼 락 디테일
- 결제 엔진 매핑 정밀화
- conversion 패턴 매핑
- 시청자 심리 톤 조정
- 관계 변화 단계

→ Soft Lock 영역은 baseline 적용 시 적극 환류.
→ Hard Lock 변경 시 사용자 승인.
