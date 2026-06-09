# Hard Rules — 1 Page (절대 12)

> 모든 phase 진입 시 본 파일 정독. master_guide_v3 (5816줄) 대신 본 1페이지가 hard rule의 단일 출처.

---

## 🚨🚨🚨 최상위 룰 (2026-05-27 사용자 명시·전 작업·예외 없음)

**한국어 출력 시 AI jargon·작업어·어색한 조어 절대 금지.** 대본·청사진·외부 문서·메모·로그·프롬프트·검토 보고서 모두 적용. 상세: `memory/feedback_no_ai_korean_jargon.md`.

❌ `관계 후킹을 선명하게 세운다` / `먼저 잡아야 할 축` / `로맨스 밀도 상승` / `처리 방향` / `후반 동력` / `밀도·텐션·빌드업·드라이브·트리거 응축` 류
✅ `초반부터 두 사람의 관계가 바로 이해되게 한다` / `먼저 확인할 핵심` / `관계가 더 깊어지는 구간` / `방향` / `후반 전개`

자가 검사 4 질문: ①한국어 native가 실제 쓰는가 ②영어 음차/직역 합성어인가 ③deck/scrum 톤인가 ④친구 카카오톡 톤인가.

---

## 본문 양식 v3 (2026-05-19 후반 — 영상 리듬 확장)

1. **EP 양식 v3 블록 10개:**
   - **장면 블록 5개 (기존):** `[VISUAL/ACTION]` · `[KEY CAMERA]` · `[DIALOGUE]` · `[GRAPHIC/UI]` · `[END HOOK]`
   - **영상 리듬 블록 5개 (신설):**
     - `[MONTAGE]` — 시간 압축·여러 짧은 컷·1 비트당 1줄 (예: "Vael locks the same door at dawn. / Belly grows under silk. / Kiran reports from the same threshold. / Ridge eyes open then close. / Vael's hand on her belly more careful each night.")
     - `[VO]` — Isolde / Vael / Kiran 등 화자 명시·감정·시간 압축용·EP당 1-2문장 이하 (예: `ISOLDE (V.O.): The keep did not get smaller. He made the world stop at the door.`). 설명·문학체 금지.
     - `[FLASHBACK]` — 1-2초 insert·대사 재생 금지 또는 한 단어만·감각 회수용 (예: `EP01 chain on her wrist — 1 second cut.`)
     - `[INSERT/CUTAWAY]` — Object·Body·Detail close-up·1초 (예: `Wet pebble on bench. / Mireille pendant catching firelight. / Iron link in cradle corner.`)
     - `[INTERCUT]` — 두 공간 동시 진행·cross-cut 표기 (예: `INTERCUT — corridor: Kiran's men at the door. Chamber: Vael's hand on her belly.`)

2. **50화·총 70-80k chars default (MEMORY 0-2 절대 룰) + Hard Cut = EP수-1.** 마지막 EP = 자연 엔딩 (`Fade Out.` / `End.` / 없음). mid-EP `Hard Cut` 마지막 EP에 두면 즉시 fail.
3. **9:16 default.** 16:9는 명시적 사유 필요.
4. **EP body Korean character 0건.** `\p{IsHangulSyllables}` 매칭 = 즉시 fail.

## 화면 리듬 (가장 비싼 룰·반드시 준수)

5. **EP당 영상 리듬 블록 ≥1개 필수.** `[VISUAL/ACTION]` 정면 대화만 = 화면 선형화. 매 EP MONTAGE / VO / FLASHBACK / INSERT / INTERCUT 중 1개+ 삽입. 후반부 (반복 위험) EP = 2개+.
6. **부위 순회형 tracking 금지 (Female gaze 룰).** "thigh → ribs → throat → collarbone" 순회 = male gaze. 대신 Vael 통제 상실·forearm weight·Isolde agency·breath·firelight·sheet·hand·choice 우선. 부위 자체 줄임 X / **시선 우선화.** 상세: `feedback_female_gaze_camera_polish.md`.
7. **Master + Platform-safe 이원화.** 초고수위 씬 = master version (`07_final/[작품]_FINAL_v{N}.md`) 보존·platform-safe = 별도 파일 (`07_final/[작품]_FINAL_v{N}_platform_safe.md`) 카메라·문장 우회 본문. 상세: `feedback_master_platform_safe_dual_version.md`.
8. **Spoken English 원어민 polish.** 5단어 default·자연 spoken English 우선. 5단어 이하 강제 = "원시인 영어"·"코미디" 위험 (`If she cost me you.` 류 문법 오류·`Her no holds. Her names cost hands.` 류 부자연 압축). 자연 spoken 위해 5-10 단어 허용·핵심 결정 발화만 1-3 단어.

8-1. **🆕🎙️ AI 더빙+AI 영상 = 톤-독립 단일 의미 대사 (2026-06-08 사용자 명시·히트작 10개 실증).** 산출물은 AI 영상 + **AI 더빙(TTS)** 둘 다로 제작 → 두 제약 동시 적용: ①**대사는 flat하게 읽어도 한 가지 의미로 수렴.** 반어·sarcasm·이중의미·의미심장·애매처럼 *톤이 의미를 결정*하는 대사 금지 — AI 더빙이 못 살림. 의미는 *단어+행동*이 운반. cue(괄호 톤 지문)는 *이미 단일 의미인 문장* 위 안전망일 뿐·톤 의존 문장을 구제하려 cue를 붙이지 마라(문장을 먼저 고친다). **짧음과 무관**(긴 직설 OK·짧은 암시 실패). ②서브텍스트는 톤이 아니라 4 해소법으로 외화: 짧은 cue / 다음 대사 평문 재진술 / V.O.가 직접 말함 / 이미 보여준 행동이 고정. ③**미세 표정연기 의존 지문 제한** — "묘한/복잡한/의미심장한 표정"·unreadable에 핵심 의미 X·무성 facial insert + V.O.로 외화·특정 샷(ECU·crash zoom)으로 귀결. 상세: `memory/feedback_ai_dub_tone_independent_dialogue.md` (= `compound-tone-parentheticals`의 상위 층).

## 집필 컨텍스트

9. **매 phase_4 진입 시 매칭 히트작 raw 대본 3-5 EP + 이전 EP 3개 raw 정독.** 옛 "첫 1-2 씬만 Read" 룰 = 폐기. 메타 baseline = 매 phase 진입 시 always-load 3개만 (MEMORY.md). 나머지 = 호출 트리거. **검증 보고서·테이블·자가 검수 풀이 = 본문 외 작성 금지.**

## 작품·폴더·파일

10. **작품 폴더 prefix 명명** (`projects/02_the_offering/02_the_offering_04_blueprint.md`). 폐기 = `_X_NN_slug` (자동 차단). **최종고 1종 + V 번호 명명** (`07_final/[작품]_FINAL_v{N}.md`). 옛 정본 = `07_final/_archive_versions/`.

## 검토 / 환류

11. **검토 채택 필터 — 순서 고정 (2026-06-05·운용 룰 §1):** **필터 0 (최우선) = 엔진/쾌감 선판정** — 이 지적을 반영하면 장르 쾌감 엔진·막장 톤이 죽는가? 죽으면 정합성 지적이라도 그대로 채택 X (쾌감 보존 방식 = 한 줄/한 행동으로만 수정). cadence류 지적은 **시그니처/의도된 빌런 연기(diegetic) 예외를 메인(쇼러너)이 최종 판정** 후 채택. → 필터 1 (채택) = 공간/시간/소품/인과/정합성/언어 일원화 위반·**부위 순회 tracking·시선 위반·영상 리듬 블록 부재·🆕 시적/대구/운율/낭송형 cadence·🆕 1-3 단어 단독 턴 3턴 이상 연속·🆕 같은 화제 4 턴 이상 짧은 핑퐁·🆕 정전 쓰레기 형태 (`One X. One Y. My Z. Now I N. The A was not B. ...`)·🆕 동일 prop 3+ 장면 반복·🆕 prop-anchored reveal trigger** 추가. 필터 2 (거부) = 작품 핵심 쾌감 약화·캐릭터 매력 약화·Soft Lock 강제 표준화.
12. **청사진 ↔ 본문 환류.** 본문이 더 강하면 청사진 부분 업데이트 (Hard Lock = 사용자 승인). 환류 시 청사진 말미 1줄 로그.

---

## 자료 출처 (필요 시만 정독)

| 자료 | 위치 | 진입 시점 |
|---|---|---|
| Conversion Runway 7 단계 | `prompts/phase_4_episode_writing.md` | phase_4 진입 |
| 영상 리듬 baseline | `memory/feedback_screen_rhythm_v3_blocks.md` | 집필 진입 |
| Female gaze baseline | `memory/feedback_female_gaze_camera_polish.md` | 다크 로맨스 집필 진입 |
| Master + platform-safe | `memory/feedback_master_platform_safe_dual_version.md` | 초고수위 작품 |
| Spoken English | `memory/feedback_spoken_english_native_polish.md` | 영어 대본 집필 |
| 페르소나 | `config/personas/` | LOCK 전 3-4인 패널만 (전면 9인 검토 폐기·token-diet) |
| 검수 agent 운용 룰 | `config/agent_operating_rules.md` | 검수·LOCK 진입 시 |
| 최종고 검수 흐름 (10+3패스·모드 선택·쇼러너 merge) | `config/final_review_flow.md` | 최종고·새 정본·외부 대본 검수 진입 시 |
| Engine brief 템플릿 | `config/engine_brief_template.md` | phase_3 완료·phase_4 진입 게이트 |
| Production handoff 템플릿 | `config/production_handoff_template.md` | LOCK 후 docs 환류 시 |
| 마케팅 셀링포인트 템플릿 | `config/mkt_selling_points_template.md` | LOCK 후 환류 다음 — 작품 마무리 산출물 |
| 평가위원 7인 | `config/evaluators.md` | 피칭 시점만 |
| 타깃 자료 | `config/target_research/[성별]_target_research.md` | phase_0-5 진입 |
| 히트작 분석 | `config/vertical_drama_hit_scripts_analysis/` | 청사진·집필 진입 |
| 히트작 raw 대본 | `config/vertical_drama_hit_scripts/` | 집필 시 (룰 #9) |
| Reference INDEX | `config/reference_scripts/INDEX.md` | phase_3/4 진입 |

---

## 자동 차단 (실행 X)

- 폐기 프로젝트 (`_X_*`) 호출 → 폐기 알림 + 작업 거부
- 본문 한국어 → 즉시 정정
- 영상 리듬 블록 0개 EP → 작업 중단·MONTAGE/VO/FLASHBACK/INSERT 1개+ 추가
- 부위 순회 tracking (thigh → ribs → throat 순서 묘사) → 시선 우선화 정정
- 검증 보고서·테이블·자가 검수 풀이 = 작성 거부
- **🚨 Vertical 자체 룰 — 행정/법/정치/외교 절대 금지** (성별·신분·장르 무관). charter·treasury·hearing·decree·외교 협상·exile (formal)·policy·writes letter·brand mark·council vote·sentence 등. 어떤 캐릭터도 (왕·여왕·주인공·악역) 행정 행위 X. Vertical ≠ HBO 변호사 드라마. 사용자 명시 지시 없으면 *즉시 personal violence + visceral claim 비트로 reframe*. 상세: `memory/feedback_vertical_no_admin_power.md`.
- **🆕🚨 시적·대구·운율·낭송형·티키타카 stage 톤 cadence 자동 차단** (2026-05-27 사용자 명시):
  - Tri-colon anaphora (`A. B. C.` 동일 cadence 3 fragment) EP당 2건 이상 → 즉시 정정
  - Mirror echo (`X. / Y. / X. / Y.` 핑퐁) 2쌍 이상 → 즉시 정정
  - Parallel structure (`The X was Y. The X will be Z.`) → 즉시 정정
  - 정전 쓰레기 형태 (`One X. One Y. My Z. Now I N. The A was not B. The C will not be D.`) 1건 → 즉시 폐기
  - 1-3 단어 단독 턴 3턴 이상 연속 → 묶기 (인간 호흡 한 turn)
  - 같은 화제 4 턴 이상 짧은 핑퐁 (기능 턴 제외) → 묶기
  - 상세: `memory/feedback_no_theater_tone.md`
- **🆕🚨 소품 의존 plot 전개 자동 차단** (2026-05-27 사용자 명시):
  - 동일 prop 3+ 장면 등장 = 🟡 (재설계 검토)
  - Reveal trigger = prop matching (jaw·pin·mark·ring) = 🔴 (캐릭터 dialogue·VO로 교체)
  - Motif·상징 욕심으로 박은 prop 반복 등장 → 즉시 삭제
  - 상세: `memory/feedback_vertical_protagonist_voice_ownership.md` 룰 5
- **🆕🚨🎙️ 톤 의존 대사·미세 표정 의존 지문 자동 차단** (2026-06-08 사용자 명시·AI 더빙+AI 영상):
  - 의미가 *톤*에서만 나오는 대사(반어·이중의미·의미심장·애매) → 톤-독립 단일 의미로 재집필 (또는 진의를 V.O./다음 대사/행동으로 외화)
  - "묘한 표정/복잡한 얼굴/의미심장한 미소/unreadable"에 *핵심 의미*가 걸린 지문 → 무성 insert + V.O.로 외화·특정 샷으로 귀결
  - cue로 톤 의존 문장을 구제하려는 패턴 → 문장 자체를 먼저 단일 의미로 수술
  - 상세: `memory/feedback_ai_dub_tone_independent_dialogue.md`
- **🆕🚨 구체·시각·천박·원형 단어 → 추상·범주·'점잖은' 단어 교체 자동 차단** (2026-06-08·"개처럼"→"부하처럼" 개악):
  - '관객이 더 공감/이해할 것'이라는 명분의 추상화 = 직관 파괴. 구체 원형어는 한 의미로 수렴, 추상 범주어는 발산(사람마다 관념 다름)+장르 전하 0
  - 비유 vehicle을 tenor 범주에 literal 매핑('사람 얘기니 사람 단어') = 낙차=엔진 거세 → 금지
  - AI의 '직관/쉽다' 자가 판정 불신 — 진짜 직관 = 하나의 gut-image가 빨리·똑같이 박히는가
  - 상세: `memory/feedback_easy_dopamine_over_logic.md`

---

## 한 줄

> **장면 5블록 + 영상 리듬 5블록 = v3. 매 EP 영상 리듬 1개+. Female gaze 시선 우선. Master + platform-safe 이원화. Spoken English 자연 5-10단어.**
