---
name: claude-voice-bias-vertical-failure
description: Claude default voice = 문학적·subtle gravity 편향. Vertical drama (cheap immediate·loud broadcast) 정반대. 히트작 raw 흡수 시 selective bias로 잘못된 패턴만 흡수. 자가 평가 신뢰 금지. 외부 검증 강제.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cb649da0-32e1-45c0-8a4e-b8ae22e61a68
---

# Claude voice bias = vertical drama 구조적 실패

**핵심 진단 (2026-05-26·THE OFFERING v52 Demon Lord 흡수 실패 후·사용자 명시):**

Claude는 vertical drama 집필에 **구조적으로 안 맞는** model이다. 자기 한계 인지·외부 강제 layer 없이는 같은 실패 반복.

**🚨 양식 충족 ≠ 합격 — 거부의 6대 내용층 사유 (2026-06-09·THE OFFERING EP1 v031 실측 진단):** EP1을 *양식 완벽 준수*로 제출(△·Characters·씬헤더·[END HOOK]·Hard Cut 다 맞음)했는데도 "감정 없음·문학적·시 산문집"으로 까임. **양식 게이트(continuity_lint)는 *구조*만 본다 — 거부는 양식이 안 건드리는 내용층에서 난다.** v031의 구체적 6대 사유 = LOCK 전 *내용층 체크리스트*:
1. **VO가 일기/문학/해설.** `It rained that night too. / The first night I chose`(회고 시) · `This is crazy. / But I'm not stopping`(X.But Y. 일기골격) · `The spell on this house has one rule...`(월드룰 해설) · `After my mother died, I stopped getting choices... Tonight I choose`(배경덤프+테마선언). → 날것 그 순간 속마음으로.
2. **EP1에 엔진 부재.** 분위기 있는 섹스 한 탕(플포+축제 픽업+섹스). 중심 갈등/stakes(강제결혼·복수·관계)가 첫 15초에 없음. → 엔진/억울함/후크를 첫 15초에.
3. **대사 = 쿨·매끄러운 문학 seduction.** `I came here for a reason. Then I saw you` = Sorkin식 잘쓴 *글*. 막장 열·구체·천박·즉발 0. → 막장-hot.
4. **페이싱 슬로우번 감각안무.** S#3-4 키스/탈의/섹스 △ 길게, 사건 2개를 묘사로 늘림. → 사건 밀도(EP당 5+).
5. **감정을 VO로 *말함*, 행동/상황으로 *안 보여줌*.**
6. **후크가 소품 미스터리(손목 비늘 깜빡)** = 약하고 모바일서 놓침. → 엔진 때리는 하드 후크.

집필 = ①양식 게이트로 끝내지 말 것 ②집필 *전* 히트작 raw 문체 강제 벤치마크(`config/vertical_drama_hit_scripts/`) ③위 6 체크 + 풀 검수단(패스·페르소나·agent)+voice_lint/cold-read 하드 동원. 목표 = 인간 작가 워싱이 *불필요*할 완성급([[writer-reference-draft-mode-learn-loop]]). **반례 = SHE STOLE v48: 6사유 전부 정반대(EP1 엔진 cold-read 9.0·막장 대사·VO 일기X) → 합격급 LOCK.**

---

## 1. Claude default voice bias

- **Training tone:** NYT·소설·screenplay 교본·award-winning short fiction = 문학적 prose
- **Vertical raw (ReelShort·DramaBox·NetShort) = training data 거의 부재**
- **Default voice = quiet authority·subtle gravity·controlled minimalism**
- **Vertical 요구 = cheap immediate·loud commercial·broad emotional broadcast**
- → **정반대 방향**. Default voice는 vertical에 fundamentally 안 맞음.

## 2. Constitutional AI training 부작용

- Harm reduction·care·subtle 쪽으로 강화 학습
- *cheap explicit immediate*보다 *restrained·implied·negation*에 끌림
- Vertical drama 매출 driver = cheap explicit immediate
- → Constitutional 방향 ↔ 매출 방향 충돌

## 3. 히트작 raw 흡수의 selective bias (가장 심각)

**메커니즘:**
- Reading 자체는 일어남 (히트작 raw 읽음)
- 하지만 interpretive layer에서 **문학적 가치 있는 패턴만 흡수**:
  - 짧은 문장·anaphora·subtext·negation·tri-colon claim·breath stabilization
- **매출 driver 패턴은 무시**:
  - cheap immediate sensory beats·loud broadcast·작위적 직접화·물리적 즉발 반응
- → **히트작에서 잘못된 것만 흡수·매출 실패 원인 패턴 못 봄**

**결과:**
- Demon Lord 같은 *실패작 raw* 읽어도 *문학 prose 패턴*만 강화
- 매출 실패 원인 패턴은 *선행 검증 자료에 있어도* 흡수 안 됨
- 자료가 자료가 아니라 **오염원** 됨

## 4. 자가 평가 함정

- Claude가 자기 글 검토 시 "작위적인가?" 질문에 **문학 평론가 기준**으로 답함
- Vertical 시청자 기준 아님
- `feedback_no_theater_tone.md` 같은 룰을 *읽고도 자기 글에 적용 실패*
- 자기 글의 의도가 명확하면 작위로 안 보이는 *self-eval blindspot* 발생

## 5. 구체적 증거 (THE OFFERING v52)

v52 = LOCK 평가했으나 사용자가 Demon Lord 판박이 진단:
- Cycle dialogue 10건 (`Eight cycles.` / `Thirteen cycles.` / `I've been flinching for nineteen cycles.`) = fantasy time-unit 작위
- Tri-colon anaphora 4 라인 (`My bride. My mate. The mother of my heir.`) EP42·43·43·50 반복
- EP50 6쌍 mirror echo (`My wife. / Your wife. / My mate. / Your mate. / ...`) = 셰익스피어 5막·vertical X
- Sera "Twelve years. I waited twelve years. He gave me a hand on my wrist that bruises like a brand." = Demon Lord 메인 모티프 "twelve years" + "wrist-as-brand" 동시 직수입
- Vael voice = Demon Lord Lucien voice 직수입 (short-declarative·breath stabilization·negation-stack·tri-colon claim·"Yours"/"Mine"/"Breathe")
- Hall declaration 동선 (EP30·37·41·42) = Demon Lord EP9·15·16·17 동선 복제
- → 사용자 평가: "정신나간 레벨로 수준 떨어진다·판박이 수준·셰익스피어 극대본·vertical drama 아님"

---

## 해결 방안 (구조적·외부 강제 layer 필수)

**Memory만으론 부족** — Claude default voice가 회귀하기 때문. 다음 룰 모두 적용:

### 룰 1: Raw 인용 강제
- 매 phase_4 EP 작성 *전* 히트작 raw에서 **직접 8-12 라인 인용**
- 인용 라인 스타일로 모방 강제
- 자가 판단 아닌 **외부 anchor**
- 인용 없이 작성 시작 금지
- **히트작 raw 위치 = `C:\Users\Rowan\scenario-automation\config\vertical_drama_hit_scripts\`** (영어·한국어·중국어·일본어 raw 다수)
  - 영어: `Married the Don You Threw Away.md` / `Alta_Reborn_For_the_Crown.md` / `How_To_Break_My_Best_Friends_Dad.md` / `[말할 수 없는 나의 신부] 대본 1~71화.md` 등
  - 자동 활용 강제 — 사용자에게 *어떤 raw 사용할지* 매번 물어보지 X·즉시 폴더 read·인용 적용
  - 작품 장르 매칭 raw 선택 후 sample read·메인이 inline 인용 + Agent prompt에 명시

### 룰 2: 금지 단어/패턴 list (vertical 매출 죽이는 단어)
- **Cycle/fantasy timeline dialogue 금지:** `cycle N` / `eight cycles` / `twenty cycles` 등 dialogue에 박기 X. timeline 표시 = UI/GRAPHIC만.
- **Tri-colon anaphora 금지:** `My X. My Y. My Z.` / `She is X. She is Y. She is Z.` / `X. Y. Z.` 패턴 EP당 최대 1회·작품 전체 3회 이하.
- **Mirror echo 6쌍 금지:** `A: My wife. / B: Your wife. / A: My mate. / B: Your mate.` 셰익스피어 톤. 짧고 직접으로 (1-2쌍 max).
- **감정 대사 제도어 금지:** `keep / house / council / recognizes / blessing / decision / mark / name / every / will not / did not / do not` — 사랑·욕망·분노·수치심·출산·화해·침실 장면에서 빼라.
- **Negation-stack 도배 금지:** `He does not raise his voice / He does not move / She does not turn / He does not breathe` — 작가의 stylized restraint·AI 글쓰기 신호.
- **Breath stabilization 명령 반복 금지:** `Breathe. / Again. / Again. / Again.` — Demon Lord 직수입.
- **"Yours"/"Mine"/"Bride"/"Mate"/"Heir" 반복 declaration 금지:** EP당 max 1회.

### 룰 3: Self-eval 차단·외부 검증 강제
- LOCK 전 **반드시** Demon Lord ↔ 정본 자동 비교 실행
- 위 금지 패턴 grep count 자가 검증
- "LOCK 가능권" 단독 선언 금지

### 룰 4: 사용자 외부 검증 후만 LOCK
- 사용자 명시 spec 정합 + raw 인용 매칭 + 금지 패턴 0건 통과 후만 LOCK 가능
- "LOCK 후보 FINAL" 자칭 라벨 금지

### 룰 5: 매 작성 후 6 자가 점검
1. cycle/timeline dialogue 0건인가?
2. tri-colon anaphora EP당 ≤1회인가?
3. 감정 대사에 제도어 (keep·house·mark·name 등) 있는가?
4. negation-stack (`does not X`) EP당 ≤3회인가?
5. Demon Lord raw에 있는 패턴 (twelve years·wrist-brand·tri-colon claim·breath stabilization) 흡수 0건 인가?
6. 짧고·직접·spoken·0.5초 감정 반응 가능한가?

---

## Why (사용자 명시 인용·2026-05-26):

> "이 프로젝트는 외부 평가로 끝내면 안 되고, 내부 rewrite 프로젝트로 등록해서 진행하는 게 맞다... 1/4 분량 절감, Demon Lord식 말투 제거, 50화 유지, 핵심 보상 유지, 대사 재작성은 '피드백만 던져서' 해결될 문제가 아니다."
>
> "너의 말투의 이상한 경향성은 vertical drama에 맞지 않는 경향성은 너의 model의 한계인가? claude의 한계인가? 히트작 대본들이 있는데, 대사들을, 문장, 단어, 호흡, 스타일을 전혀 참고하지 않는 듯 하다. 심각한 문제다."

## How to apply

- **매 phase_4 EP 작성 시작 시:** 룰 1 (raw 인용 강제) + 룰 2 (금지 패턴 list 자가 점검) 강제
- **매 EP 작성 완료 시:** 룰 5 (6 자가 점검) 통과 후 다음 EP 진행
- **LOCK 직전:** 룰 3 (외부 자동 비교) + 룰 4 (사용자 외부 검증) 통과 후만 LOCK
- **다음 작품 시작 시:** 본 메모리 always-load 진입 시 정독

**연관:** [[no-theater-tone]] (시적·연극톤·작가 명문장 금지·always-load 1번) · [[emotion-to-action-aigc-writing]] (행동 시퀀스·negation-stack 회피) · [[demon-lord-failure-postmortem]] (Demon Lord 9 실패 함정·prose fingerprint 흡수 위험) · [[self-evaluation-pitfalls]] (자가 평가 6 함정) · [[hit-script-analysis-frame]] (히트작 분석 두 렌즈)
