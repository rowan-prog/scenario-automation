---
name: 북미 paid vertical / AIGC 판단 기준 — 한국식 기본값 X
description: 한국어 = 협업 언어. 작품 판단 기준 X. 전 단계(아이디어/청사진/피칭덱/스크립트/검토/최종고) = 북미 paid vertical / AIGC 타깃 기준. 한국식 가족·체면·위계·리듬·감정·제도 기본값 절대 X. 영어 대사 = 처음부터 영어.
type: feedback
originSessionId: 84137f65-ae18-4af2-b7fd-da37ae3ce880
---
한국어는 협업·문서 언어일 뿐이며 **작품 판단 기준이 아니다**. 아이디어 → 청사진 → 피칭덱 → 스크립트 → 검토 → 최종고 **전 과정이 북미 paid vertical / AIGC 타깃 기준**.

**Why:** 2026-05-12 사용자 명시. AI가 한국어로 대화한다는 이유로 한국식 정서·관계·제도·말맛이 기본값으로 들어가면 작품이 북미 타깃과 어긋남. 수위 한정 룰(`feedback_north_american_explicit_standard.md`)을 넘어 **전 영역**으로 확대.

**기본값 금지 (모든 단계 / 모든 작품):**

| 영역 | 한국식 (X) | 북미 paid vertical (O) |
|---|---|---|
| **가족 정서** | 효·부모 우선·가족 갈등·체면 보호 | 개인 우선·로맨틱 관계 우선·가족은 적·동맹·도전 대상 |
| **체면 / 위계** | 호칭·격식·존댓말 함의·상사 절대 | 평등주의·이름 호칭·직접 도전·능력 중심 |
| **회사/사회 위계** | 연차·접대·조직 충성 | corporate ladder·open challenge·CEO 대결·prenup·NDA |
| **대사 리듬** | 짧은 호명·여운·은유·의문어미 | 직접·구체·짧고 강력·소유 발화 |
| **감정 표현** | 절제·간접·"눈빛으로"·여운 | 직접 발화·신체 행동·소리 ("Kiss me"·"You're mine"·"I want you") |
| **제도 감각** | 한국 결혼·재산·신분·법 | prenup·divorce·dating·gun·NDA·crown·title·blood right |

**원작이 한·중·일권일 때:**
- **사건 뼈대만** 가져옴
- **욕망·공간·직업·관계·제도·말맛 = 북미 시청자가 즉시 읽게 번역**
- 예시:
  - 한국 재벌 → American family empire / Wall Street dynasty
  - 한국 회사 위계 → corporate ladder + open boardroom challenge
  - 한국식 결혼 부담 → prenup·family approval·society reveal
  - 한국 사극 → medieval fantasy / Renaissance court
  - 한국 학원물 → American prep school / Ivy League

**영어 대사 룰 (필수):**
- "한국어로 생각한 뒤 번역" 절대 X
- **북미 배우·성우가 처음부터 말하는 문장**처럼 판단
- 번역체 대사 예시 (모두 X):
  - "당신을 사랑합니다" 식 정중 톤 X → "I love you. Have always."
  - "그녀는 나의 것이다" 직역 X → "She's mine."
  - "왜 저를 제물처럼 대하지 않으세요?" 정중 의문 X → "Why don't you treat me like one?" / "Then stop pretending I'm not."
- 북미 검증 톤 = ReelShort·NetShort·DreameShort 대사 직접·짧음·소유·도전

**모든 단계 적용:**
- **아이디어:** 글로벌 IP + 검증 트로프 + 북미 직장·연애·결혼·가족 구조 베이스
- **청사진:** 캐릭터·관계·세계 룰 = 북미 시청자가 즉시 읽을 수 있게
- **피칭덱:** 한국식 분석어 X (`feedback_banned_expressions.md`)
- **스크립트:** 영어 대사 = 처음부터 영어. 한국어 메모 → 영어 변환 X
- **검토:** 시청자 페르소나 09(여성)·08(남성) = 북미 시청자 시각. 한국 시청자 평가 X
- **최종고:** 영어 대사 자연성 검수 — "한국어 번역체" 자동 🟡 trigger

**시청자 페르소나 자동 🟡 trigger 추가:**
- 한국 가족 정서 (효·부모 우선 갈등) 감지
- 한국식 위계·체면 모티프 감지
- 간접 감정 표현 ("시선만으로"·"공기가 무거워진다" 류)
- 번역체 영어 대사 (북미 배우가 절대 말하지 않을 톤)

**관련 메모리:**
- `feedback_north_american_explicit_standard.md` (수위 한정)
- `feedback_paid_vertical_visual_principles.md`
- `feedback_banned_expressions.md`
- `feedback_target_alignment_all_steps.md`
- `feedback_aigc_explicit_action_over_subtle.md`
