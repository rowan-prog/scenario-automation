---
name: 피칭덱 위원 검증 detail 룰 (필수, 2026-05-10 갱신)
description: 위원 4/7 동의 통과 detail rule — 3초 직관성 / 거절 트리거 / 1차 오해 시뮬레이션 / 제목 형식 자유(명사형·분사형·문장형 모두 OK / 50 words 이하 / 부제 의무 X) / 거절 어휘
type: feedback
originSessionId: 77cee1d3-84b4-42dc-9c9b-fd5828dbb2e2
---
# 규칙

피칭덱 위원 통과 약화의 **3대 원인** + 대응:

## 원인 1 — 피칭 검증 방식 오류 (가장 큰 원인)

**문제:** 지금 자기 검증은 **작품을 충분히 읽고 판단**하는 쪽으로 흐름. 실제 위원은 제목·로그라인·paywall 한 줄만 보고 **1차 오해**한다.

**대응 — 1차 오해 시뮬레이션 강제:**
- 자기 검증 시 **제목 + 로그라인 + paywall 한 줄만**으로 위원 7인의 **첫 인상을 시뮬레이션**한다.
- "이 정보로만 보면 이 위원은 '○○물 또 하나'로 오독할 수 있다"를 항목별로 적시.
- 그 1차 오해를 차단하는 표현이 제목·로그라인·paywall에 들어있는지 점검.

예시:
- "Every Monday, Manhattan Dies" — 1차 오해 위험: "괴물 루프물 또 하나". 차단 표현 필요.
- "TITAN BORN" — 1차 오해 위험: "Titan submarine? Marvel Titan?" Greek mythology 즉시 식별 표현 필요.

## 원인 2 — 거절 트리거 부족 (위원 정보량 ≠ 위원 거절 패턴)

**문제:** 위원이 뭘 좋아하는지(`config/evaluators.md` 7인 프로필)만 있고, **무엇을 보면 거절하는지** 없음.

**거절 트리거 — 위원별 즉각 거절 패턴:**
- **A 위원 (Vertical Drama Veteran):** "복잡하다 / 설명 의존" 신호 — Cast 5+ / 세계관 용어 다수 / 한 줄 hook이 두 줄 이상.
- **B 위원 (Female Viewer Diagnostic):** "감정선 약함 / 관계가 늦다" — 무료 8화 안에 friction이나 betrayal 비트 부재 / 여주 능동 비트 부재.
- **C 위원 (AIGC Production Director):** "AIGC로 굳이?" 또는 "AIGC가 못 만들 영역" — 대규모 군중 / 격투 / face consistency 부담.
- **D 위원 (Commerciality Lead):** "안 팔린다 / 광고 컷 부재" — 단일 take paywall 부재 / 광고 컷 후보 1초 추출 어려움.
- **E 위원 (Genre Pleasure Auditor):** "장르 약속 깨짐" — 재결합·redemption·sympathy 등 장르 안전 락 위반 시사.
- **F 위원 (Continuity Logic Auditor):** "정합성 약함" — 세계관 link 다수 / reveal timing 불명료.
- **G 위원 (Visual Lock Auditor):** "Look 진화 부재" — 캐릭터 5단계 Look 진화 명시 없음.

**거절 트리거 점검 강제:** 자기 검증 시 위원 7인의 거절 트리거 각각 점검. 한 트리거라도 활성화되면 그 위원은 거절.

## 원인 3 — 타이틀 게이트 부재

**문제:** 북미 paid vertical 기준 제목 검증 룰 부재.

**타이틀 원칙 (필수):**

**핵심 — 통 타이틀 개념:**
- **3초 직관성 우선, 형식 자유.** 명사형·분사형·문장형 중 특정 형식 강제 X.
- "She Stole My Face" / "Every Monday, Manhattan Dies"처럼 **문장형도 갈등·장르 즉시 읽히면 강한 제목**.
- 통 타이틀 = 메인 + 부제 모두 포함 (콜론 뒤 포함). **부제 개념 없음 — 모두 통 타이틀**.
- 통 타이틀 **공백 포함 50 words 이하**.
- **부제 의무 X.** 메인 타이틀로 갈등·장르·필수 후킹 다 잡히면 부제 없음.
- 부제는 메인 타이틀에 빠진 **필수 후킹 소재 보강용**으로만 사용 (예: LOCKED OUT: I Rule the World With My AI Girls).
- 부제는 **로그라인 X. 후킹 소재 강화용**.

**상세 룰:** `config/reference_scripts/title_patterns.md` 참조 (시장 7대 패턴 + 시장 예시 200+ + 짓는 프로세스 5단계 + 거절 어휘 + 검증 체크리스트).

**7대 패턴 요약:**
1. 명사구 단독 (3-7 단어): "The Crown" / "Cleopatra"
2. 소유격·관계형 (가장 흔함): "My Cheating Husband" / "The Demon Lord's Marked Bride"
3. 명령형·직접 발화: "Marry my husband please!" / "Bite me, Stepbrother"
4. 상황·이벤트형: "The Day I Sold Myself" / "Married To A Stranger"
5. 콜론형 (메인 + 후킹 hook, 로그라인 X): "LOCKED OUT: I Rule the World With My AI Girls"
6. 분사구문·동명사 단독: "Reborn to Marry the Mafia Don"
7. 호명·역할형 (The X): "The Bride with a Secret Past"

**거절 패턴 (절대 금지):**
- ❌ 시간 mirror 로그라인 부제: "They did X. I did Y." 형식
- ❌ 콜론 뒤 스토리 풀이
- ❌ niche 어휘: SIGIL · GLYPH · RUNE · ARCANE · 코드네임
- ❌ 추상어: RECKONING · ASCENSION · TRANSCENDENCE
- ❌ 본문용 설정어: Route Nine · reset ownership · command node

**짓는 프로세스 (5단계 — title_patterns.md 참조):**
1. 후킹 소재 추출 (3-5개)
2. 형식 결정 (7대 패턴 중)
3. 단어 수 검증 (50 이하)
4. 거절 어휘·로그라인 패턴 검사
5. 1차 오해 시뮬레이션

**일률 회피:**
- 작품마다 형식 자유 — 5 작품 모두 같은 콜론형 X / 5 작품 모두 같은 부제 형식 X
- 작품 정체성에 맞는 패턴 선택

**타깃별 시장 차이 (필수):**
- **여성향 vertical drama**: 시장 예시 (My Cheating Husband / The Demon Lord's Marked Bride / Reborn to Marry the Mafia Don 류) 적용
- **남성향 애니메이션 (Solo Leveling·LOCKED OUT·BITE ME 류)**: vertical drama 시장 예시 문법과 다를 수 있음. 남성향 후킹 키워드(각성·정복·지배·1인칭 선언형 "I AM X"·폐기·먼치킨) 우선
- 남성향은 "I AM X" / "I RULE X" 1인칭 정복 선언 강함 (BITE ME: I AM ZOMBIE LORD / LOCKED OUT: I Rule the World With My AI Girls)
- **타깃 확인 → 시장 차이 적용**. 남성향 작품에 vertical drama 여성향 패턴 강제 X.

**"그래서 뭐?" 게이트 (필수):**
- 통 타이틀 본 위원이 "그래서 뭐 어쩌라고?" 반응할 위험 검증
- 갈등·관계·정복 즉시 명료해야 — 단순 명사구로 그치면 위험
- 예: "The God My Family Sealed" (단순) → "그래서 뭐?" / "The God My Family Sealed Wants Me Back" (갈등 명료) → 통과

**기존 작품·reference 작품 어휘 충돌 검사 (필수):**
- 새 작품 제목·핵심 발화 작성 시 **`config/reference_scripts/INDEX.md`의 등재 reference 작품들** + **현재 진행 중인 모든 `projects/` 작품들**의 제목·핵심 어휘와 충돌 검사.
- 충돌 어휘 (예: LOCKED OUT 제목 → "Locked Me In/Out" 어구 echo) 발견 시 회피.
- 메인 hook·페이월 발화는 다른 작품과 직접 echo 회피.

## 통합 게이트 — Title / Logline / Paywall 3초 게이트 (필수)

피칭덱 작성 후 다음 5개 항목 모두 통과해야 위원 통과 안전:

- [ ] **제목만 보고 장르와 갈등이 보이는가?** (3초 안)
- [ ] **로그라인 없이 제목만 봐도 타깃이 짐작되는가?** (북미 vertical paid mobile)
- [ ] **paywall 질문이 EP8 전에 명확한가?** (무료 구간 안에 결제 동력)
- [ ] **위원이 대충 읽어도 오독할 위험이 없는가?** (1차 오해 시뮬레이션 통과)
- [ ] **제목이 북미 paid mobile audience 기준으로 쉽고 강한가?** (어려운 어휘·희귀어·설정어 0)

## 거절 어휘 (제목·로그라인·한 줄 훅 사용 금지)

- **Niche 장르 전문어:** SIGIL · GLYPH · RUNE · ARCANE · LOCKED OUT
- **외국어/지역 전문어:** PENTELIC MARBLE / SIGMA-INSTALLATION / 코드네임
- **추상어:** RECKONING · ASCENSION · TRANSCENDENCE (구체 미감 X)
- **본문용 설정어:** Route Nine · reset ownership · command node 같은 본문 어휘 (제목으로는 모호)

**대체 일반 영어:**
- SIGIL → SEAL / KEY / LOCK
- ARCANE → HIDDEN / SECRET / OLD
- ASCENSION → RISE
- RECKONING → THE DAY / THE BILL

## Why
2026-05-08 외부 평가 — 5 작품 피칭덱 분석 후 발견:
- 1차 오해 시뮬레이션 부재가 가장 큰 원인 (위원이 작품을 읽지 않고 판단하는 현실 미반영)
- 위원 거절 트리거 부재 (위원 정보량과 별개)
- 타이틀 게이트 부재 (북미 paid vertical 기준)

사용자 예시 ("She Stole My Face" / "Every Monday, Manhattan Dies") — 문장형이지만 3초 직관성 강함. 형식 자체보다 직관성이 우선.

## How to apply
- phase_2 작성 시 5개 게이트 통과 점검
- 1차 오해 시뮬레이션 수행 후 차단 표현 명시
- 위원 거절 트리거 점검
- 거절 어휘 발견 시 일반 영어로 변환
- 제목 형식은 자유 — 3초 직관성이 우선
