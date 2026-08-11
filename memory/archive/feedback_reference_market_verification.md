---
name: reference-2026-05-16
description: "Reference 등재 전 매출 데이터 검증 필수. Demon Lord's Marked Bride 매출 부진 사례. 매출 약한 작품 = 구조·분량·톤 모델 사용 X. 인사이트는 추출 가능."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 462b4a02-4290-4164-a105-ac1f2ff0ecca
---

# Reference 작품 매출 검증 룰

## 핵심 (사용자 명시 2026-05-16)

> **"Demon Lord's Marked Bride는 북미 포함 전 권역, 아시아 등까지 다 성과가 상당히 안 좋은 편."**

기존 시스템 핵심 reference였던 Demon Lord = 매출 부진 작품. **분량 모델·구조 모델로 사용 부적합.**

## 1. Reference 등재 룰 (필수)

### 등재 전 검증 필수
- **매출 데이터 (조회수·랭킹·결제 전환) 확인.**
- 글로벌 paid vertical 시장에서 검증되었는가?
- 무료→유료 전환율 데이터 있는가?
- ReelShort·DramaBox·NetShort·Flickreels 등 공식 신호 있는가?

### 매출 약한 작품 처리
- 구조·분량 모델 사용 X
- 인사이트 추출 (왜 약한가) 가능
- "이렇게 하면 안 된다" 사례 reference

## 2. Demon Lord's Marked Bride 사례

### 기존 시스템 등재
- `feedback_episode_split_and_runtime.md` 권장 모델 (75분·50화·EP당 1.5분)
- `config/reference_scripts/INDEX.md` 등재 (작품 메타 매칭용)
- protocol_premium_pilot 의상 묘사 절제 모델
- phase_4 분량 레퍼런스

### 사용자 명시 (2026-05-16)
> **북미·아시아·전 권역 매출 부진.**

### 함의
- **분량 모델 폐기:** 75분 / EP당 1.5분이 "잘 팔리는 분량" 아님. 다크 로맨타지 매출 미달 한 원인 가능.
- **구조 모델 폐기:** Demon Lord 비트 응축·간결한 톤이 "매출 최적"이라고 가정 X.
- **다크 로맨타지 무료 분량 권장 상향:** 2.5-3분/EP × 8 = 20-24분 (이전 16-20분에서).

## 3. 매출 부진 원인 추정 (다중 가설 — 절대 X)

> ⚠️ **사용자 명시 (2026-05-16):** "demon lord 실패에 대해 나의 진단이 절대적으로 정확하지 않을 수도 있고, 이유가 그것만은 아닐 것이다."

Demon Lord 부진 가능 원인 (외부 매출 데이터 미검증 — 다중 가설):

### 사용자 가설
1. **여주 과도 능동성** — niche "강하고 당차고 주도적 여성" 톤
2. **남주 매력 부족** — 압도적 매력 5 조건 미달 가능

### 시스템 추정 (다중 AI 평가·외부 인사이트 결합)
3. 분량 자체는 OK (사용자 명시) — 단 비트 응축·깊이 부족 가능
4. 손목마크/룬/trace 과의존 (싸 보임 — `feedback_paid_vertical_intuitive_money_triggers.md`)
5. "절제" 표현·의식적 cadence (상징·의식문 과의존)
6. 공개 무대 단계 상승 부재 (mutual claim ladder 약함)

### 외부 요인 (외부 데이터 직접 분석 필요)
7. 소재·트로프 niche (데몬·brand 글로벌 메이저 X 가능)
8. AIGC 퀄리티·캐릭터 디자인·비주얼 약함
9. 플랫폼 마케팅·광고 소재력·CPM·CTR 약함
10. 출시 타이밍·경쟁작
11. 번역체·번역 톤 (영어 자연스러움)
12. 무료→유료 전환 설계 (페이월 약함)

→ **외부 매출 데이터·플랫폼 신호 직접 분석 권장.** 본 추정은 가설 풀 / 절대 X.

## 4. 시스템 reference 정정

### 폐기 처리
- `feedback_episode_split_and_runtime.md` Demon Lord 권장 모델 표시 폐기
- 매출 부진 reference로 라벨

### 추후 등재 권장
- **매출 검증된 paid vertical** 작품 reference 등재
  - ReelShort 상위 (조회수 50M+)
  - DramaBox 상위
  - NetShort AIGC 상위
  - 히트작 라이브러리 (`config/hit_library/`)에서 검증된 작품
- 작품명 + 매출 데이터 + 분량 + 구조 + 매핑 키워드 명시

## 5. 향후 외부 자료 처리

### 외부 reference·평가·자료 수신 시
- **매출 검증 우선** — 매출 약한 작품 분석은 인사이트 추출만, 모델 사용 X.
- **외부 AI 평가도 동일** — 외부 AI가 "이 작품이 좋다"라고 해도 매출 검증 후 적용.

### 시스템 내 등재 시
- 작품 매출 데이터 + 추정 약점 + 인사이트 명시
- "모델로 사용 가능 / 인사이트 추출만 / 회피 사례" 라벨

## 6. 옛 reference 메모리·자료 영향

### 영향 받는 위치 (정합 갱신 필요)
- `feedback_episode_split_and_runtime.md` (분량 모델) — 본 메모리에서 갱신 완료
- `config/reference_scripts/INDEX.md` — Demon Lord 라벨 갱신 권장
- `protocol_premium_pilot_lite.md` (의상 묘사 절제 모델 — Demon Lord 인용 시 정정)
- `phase_4_episode_writing.md` (분량 레퍼런스 — Demon Lord 인용 시 정정)

## 7. OFFERING G 디벨롭 영향

### 분량 권고 갱신
- OFFERING FINAL_FREE_v2 = 약 17.9분 (EP당 ~2.2분)
- 새 권장 = 다크 로맨타지 무료 2.5-3분/EP × 8 = 20-24분
- **분량 보강 여지 있음** — EP별 +30-50초 깊이 확대 가능

### 디벨롭 권고 (`feedback_paid_vertical_intuitive_money_triggers.md` G 디벨롭 11에 추가)
- 손목마크 50% 절삭 + 직관 신체 장치 대체
- B 스케일·D mutual claim ladder·E self-unfastened band·C 왕국 음모 채굴
- **+ 무료 분량 EP별 +30-50초 확대 (다크 로맨타지 깊이 확보)**

## How to apply

- **모든 신규 작품 reference 등재 전:** 매출 검증 + 본 메모리 룰 적용
- **외부 자료 수신 시 (phase_c_external_feedback_intake.md):** 매출 검증 + 인사이트 분리
- **분량·구조 모델 결정 시:** 매출 검증된 reference만 모델 사용
- **`config/hit_library/vertical_hit_library_2026-05-15.xlsx`** 우선 검토 (288작·76 후보·81 tropes — 매출 신호 있는 작품)

## 핵심 한 줄

> **Reference 등재 전 매출 검증 필수. 매출 약한 작품 = 모델 사용 X / 인사이트 추출만. Demon Lord 권장 모델 폐기.**
