# 메모리 인덱스 v4 (2026-06-10 — 문서 일원화 개편)

> **v4 원칙: 룰 본문은 workspace에 산다. 메모리는 인덱스 + 작품/장르 특수 + 작업 방식 피드백만.**
> 보편 집필·검수 룰은 전부 workspace 3문서로 이관됨(사용자 지시 — 모델 무관 수행 가능해야):
> **`config/00_vertical_dna.md`(근본 원리) · `config/10_writing_standard.md`(집필) · `config/20_review_standard.md`(검수·LOCK)**
> 아래 개별 메모리 파일은 보존(학습 배경·상세 예문) — workspace 문서와 모순 시 workspace 우선.
> 백업: `MEMORY_2026-06-10_pre_v4_backup.md`(v3 원문·룰 요약 전문 포함).

---

## 🥇 매 작업 진입 시 (always)

1. **workspace 3문서** 중 해당 시점 문서 정독 (위). 이게 구 "always-load 메모리 17종"을 대체한다.
2. [no-ai-korean-jargon](feedback_no_ai_korean_jargon.md) — 한국어 출력 시 AI jargon·작업어 금지·카톡 톤 (CLAUDE.md 룰 5).
3. [token-diet-70-percent](feedback_token_diet_70_percent.md) — agent 최소·1 pass+수술·보고는 경로+한 줄. LOCK 토큰 회계 = `20_review_standard.md` §1.
3-1a. [fable-structure-only-pipeline-self-sufficient](feedback_fable_structure_only.md) — **파이프라인 = opus/sonnet/haiku 자급·Fable = 구조 개정 1회성·판정 = 체크리스트**(`20_review_standard.md` §4-1 수술 파이프라인). 감-판정 = 구조 미완성 신호 → 즉시 명문화. **단 세션 모델이 Fable이면 subagent 배분에 fable 티어 포함해 자율 배분**(2026-07-22 사용자) — 실증 판례: phase_p = fable 불요 확정·트리트먼트 sonnet 하향·티어 올릴 돈으로 0단계 선행 문답을 산다(같은 날).
3-1. [agent-orchestration-tier-map](feedback_agent_orchestration_tier_map.md) — **에이전트 티어 배치**: 업무성격→모델(발견=opus·수렴/추출=sonnet·기계+naive-proxy=haiku·집필/수술=메인). naive-proxy(뇌오프시청자·flat-TTS·무맥락 이미지생성기)는 작은 모델이 더 정확. 신규 haiku 2종(aigc-draw-auditor·tts-literal-ear)·직교 병렬 sweep·다시각=독립N×다른프레이밍·집필지원 W1-W3. 본문 = `20_review_standard.md` §7 + `10_writing_standard.md` §A-1.
3-2. [occasion-hopping-space-economy](feedback_occasion_hopping_space_economy.md) — 🆕(2026-07-10) **v70 "TV드라마" 판정의 3중 근본 원인**: ①행사 순회(단발 공간·리셋 오프닝 스트릭) ②net-zero 라운드(빌드업병 — 라운드 제거 테스트) ③쿨슬롭 레지스터(주인공 170라인 감탄 0·조력자 코치봇 — **빌런은 잘 쓰고 주인공/조력자를 망치는 게 AI 편향**). 기계 게이트 = `pacing_lint.py`+`register_census.py` 상설. 본문 = `10_writing` §C-2-1·C-4-0·D-5-0. ⚠️ "구조만 문제, 대사는 괜찮다"는 1차 오진 — 재발 금지. **+2026-07-30 컨테이너 법칙(①의 양성 처방): 한 컨테이너 = 한 공간 + 한 시간대 9~10화·점프는 브리지에서만·미수를 방마다 하나씩 = 금지·강도는 공간 아닌 근접자/옷/자세/소리로.**
3-1b-0. [price-defines-the-spec](feedback_price_defines_the_spec.md) — 🆕(2026-08-26 사용자) **가격이 규격을 정한다.** 우리 분당 단가가 영상 시장 최고가 → '고급감·완성도·품위'를 경쟁 축으로 잡으면 **자동 패배**(영화·OTT는 1/10 값에 100배). 이기는 축 = 그들이 배우·브랜드·심의 때문에 **구조적으로 못 파는 것** = 원초·금기·천박·윤리 이탈의 극단. 판정 = *"넷플릭스에 있어도 안 이상하다" = 결함 / "거긴 이런 걸 못 판다" = 정상.* ⚠️ 싸구려 허가 아님(틀린 건 여전히 결함) · 밀도는 오히려 더 높아야. 착지 = `00_vertical_dna` **조건 0 + S0-4(원초 욕망 9종)·S0-5(컨텍스트 제로 컷)·S0-6(후킹/락인/결제 세 관문)** · `20_review` **ⓞ 숏폼 6문** · `10_writing` §D-2-1 ⑦ 되감기 0. **락인이 제일 자주 빠진다 — 훅은 컷이고 락인은 1화 엔딩 계약서(뭘 줄지 확정) + 2~3화 첫 이행이다.**
3-1b. [paid-vertical-structure-first](feedback_paid_vertical_structure_first.md) — 🆕(2026-08-20 사용자) **판정 순서 = 엔진 → 구조 → 서사 → 라인.** "핵심은 장르/트롭이 아니라 구조다, 그 다음 서사다 · paid vertical drama 다운 구조가 존재해야 한다" + "기획안이 숏폼이 아니라 무료형 콘텐츠·장편 영화 같다(전개 속도·인과관계·감정선 / 트리트먼트·캐릭터 설정·기승전결)". 본문 = `00_vertical_dna.md` **구조 7항 + 붕괴 3축** · 게이트 = phase_p 대원칙 10·phase_1 §G·**`20_review` §1③ 기획 문서 모드(신설)**·`pacing_lint --shortform`. §C-1 사건 수 숫자도 실측으로 정정(무료 8화 = 사건 1개). 예외 = 장르 캐논 지연(후회남·정보 자본)은 결함 아님.
3-1c. [episode-opening-gate](feedback_episode_opening_gate.md) — 🆕(2026-08-23 사용자 IG 실측) **무료런 각 화의 첫 △ = 앞 화가 끊긴 그 동작의 다음 프레임.** 무인/주인공부재·기상리셋·사후정적으로 여는 화는 그 작품 안에서 상위 3위에 든 적 0/2작품(TITAN EP1 全景=4.1만 꼴찌 · LWM EP4 INSERT 외경=10.1만 최저). **무료런만 하드 적용·1화는 예외 없음·전체 FLAG 비율은 품질 지표 아님**(히트작이 우리보다 높다). 기계 = `tools/opening_lint.py`. §B '무성 워밍업 2컷+ 실패'는 실측 미지지 = 정밀화 안건. **+2026-08-25 같은 리포트 §7 뒤늦게 등재 — 컷이 팔리는 3요건 = 대립 구도가 첫 프레임에 보인다 / 갈등이 말·행동으로 밖에 나와 있다 / 다음이 확 궁금해지는 지점에서 끊긴다.** 대립은 필요조건이지 충분조건 아님(동작이 한 컷에 완결돼야 터진다) · 섹슈얼 고수위는 경쟁 아니라 겹칠 때 최상급이나 **대립 없는 벗기는 컷 단독 = 최저 성과** · 풍경·신체 클로즈업 오프닝 금지. 본문 = `00_vertical_dna` S0-3 · `20_review` §1③ · `40_selling_point` §3-4.
3-2c. [rough-proposal-is-a-pitch-doc](feedback_rough_proposal_is_a_pitch_doc.md) — 🆕(2026-08-04) **러프 기획안 = 피칭 문서.** 두 실패: ①내부 규격(컨테이너 표·"못 나가는 이유"·"비가역 산출")을 본문에 쓰면 설계도 = 룰2 위반·`_X_19` 폐기 사유 재발 ②지문체 평서문 = 읽는 재미 0(짧게 끊고 강한 동사·웃긴 지점은 문장 끝 · **단 어거지 비유·멋 부린 동사 금지**). 필수 5종 = 장르 이름표 한 줄 · 톤 레퍼런스 한 문장 합성 · 톤 선언 맨 앞 · 셀링포인트 5개 · 스캔 표+장면 이중. 외부 AI안 대조로 확정하되 **B급 라벨·회차 두 공간 걸침·굴욕 자리 이동·요약형 훅·1화 여성 누락은 기각.** 교훈 = 외부안이 나아 보이는 이유가 문장력이 아니라 **배치**일 때가 있다.
3-2f. [rebut-from-our-own-text-first](feedback_rebut_from_our_own_text_first.md) — 🆕(2026-08-25) **외부 지적에 수정안을 만들기 전에 "우리 대본이 실제로 깨졌는가"를 우리 원문으로 먼저 검증한다.** 28번 감독 피드백에서 수정 후보 8건을 냈다가 사용자 검증으로 전부 철회 — 근거는 전부 우리 대본에 이미 있었다(EP5 VO가 "안 들린다"가 아니라 "**잘** 들리지 않아"였던 것 등). 판정 질문은 "감독 말이 맞나"가 아니라 **"우리 두 곳이 서로를 부정하는가"** 하나. **원작 대조는 반박 재료지 수정 근거가 아니다.** 수정안은 기존 대사를 죽이지 않는지 역검증. **채택 목록을 내가 확정해 내밀지 말 것 — 내 판정은 사용자의 재료다.**
3-2d. [audit-must-pass-hit-scripts-first](feedback_audit_must_pass_hit_scripts_first.md) — 🆕(2026-08-07) **검수 잣대를 히트작에 먼저 대본다.** 실측: 내가 "분량 붕괴"로 깐 25번(뒤/앞 0.53·씬1개화 46%)이 신의한방(0.49·78%)·회사도(0.43)·퀸카(씬1개화 86%)보다 **균질**했다 → 판정 무효. 화 엔딩 "해소 직후 절단"도 히트작 표준(리액션 프리즈) — 유효 축은 "프리즈 직전 대사가 판돈을 올리는가"뿐. 지적 4분류 = **A 캐논 대조·B 장르 엔진/타깃 = 낸다 / C 화면에 뜬 숫자 = 조건부 / D 나노 정합·형식 = 버린다**(히트작 전량 불합격). 외부 AI 헛다리를 거르던 그 세션에서 나도 같은 걸 40개 냈다. 스크립트 = `projects/25_billion_dollar_reset/_hit_audit.py`.
3-2e. [cliff-types-are-mostly-not-danger](feedback_cliff_types_are_mostly_not_danger.md) — 🆕(2026-08-12) **히트작 50화 클리프 전수 분류: 물리 위기는 6개뿐.** 최다 = 관계 한 칸(13) · **빌런이 연락처를 넘기다 한 이름에서 멈추고 웃는다(10)** · 정서 잔상(9). 매 화 위기를 짜내면 사건을 발명하게 되고 그게 공간 순회로 간다. 같은 대본 **대사 비중 77%**(지문 30% 넘으면 프로즈가 대사 자리를 먹는 중 · 액션 화만 예외). 카드 = `craftcard_mafia_uncle.md`.
3-2b. [hit-script-event-count-measured](feedback_hit_script_event_count_measured.md) — 🆕(2026-08-03) **히트작 raw 실측: 50화물 = 사건 2~5개 · 한 사건이 12~41화**(신의한방 콜로세움 41화 연속·False Weakling 4개·가면 무투대회 12화+주루의 밤 17화). 무료 8화 = 사건 **1개**가 정상. 사용자 기준 "5~10개, 10개도 많다"보다 히트작이 더 적다. **세는 법 = 공간이 아니라 인과** — 컨테이너 3개여도 인과가 안 끊기면 사건 1개. ⚠️ **`10_writing` §C-1의 "아크 10~14개·각 3~6화"가 실측과 3~4배 충돌 = 구조 개정 안건**(§C-3·hit_dna #9는 이미 12~41화를 인정 — §C-1 숫자만 구버전 잔존). 러프 기획안 단계엔 컨테이너 게이트가 없다는 것도 같이 발견.
3-2a-1. [no-abstract-evasive-writing](feedback_no_abstract_evasive_writing.md) — 🆕(2026-07-24 사용자 상시 지시) **모든 집필(대사+지문+트리트먼트+기획 프로즈) = 추상어·회피어·검열문으로 핵심 회피 금지.** 판정: 누가-무엇을-하는지가 구체 명사·동사로 박혀 있는가. 절제(캐논)≠검열 — "어디서 멎는지"를 구체로. 본문 = `10_writing` §D-2-1 ⑧(2026-08-26 ⑦ 되감기 0 신설로 ⑥→⑧ 재번호).
3-2a. [dialogue-direct-register-wit-ration](feedback_dialogue_direct_register_wit_ration.md) — 🆕(2026-07-15) **대사 기본값 = 직설 평문(행위를 그 이름으로: kissing/sex/cheating/money) — 완곡·부위 우회·암시·재치 대구·압축 은유·큐의존 = 스타일 아니라 하드 결함.** 12_hired 전 코퍼스 실증("개구리다"). 유창해서 검수 통과 = 함정("유창한가" 말고 "직설인가"를 물어라). 위트 = EP당 1 배급제. 본문 = `10_writing` §D-2-1 + `20_review` §2B·§4. 기계 = esl_hardwords.py + tts-literal-ear 심문5. ⚠️ 자작 대사에 각색 보수주의("대사 불가침") 적용 금지·무드 라벨("알파 레지스터")로 기계 FLAG 기각 금지.
3-3. **라이터스룸 강의록 (2026-07-10 사용자: "vertical drama의 정수·꼭꼭 삼켜라")** — `config/vertical_drama_hit_scripts_analysis/craft_lecture_liv_writersroom2.md` (workspace 내·예문 verbatim). 클리프행어 5패턴(제3자 등장 절단)·훅은 웹툰보다 소소해도 됨·마지막 비트 진입·비후킹 필연 급행·3줄컷·주인공 전회차 등장·각색 중티 2분법(문화 마커 치환 > 개연성). 집필·각색·검수 진입 정독 의무(10_writing §A 3-1).
4. 진행 중 작품 엔진 메모리 — SHE STOLE: [vertical-revenge-impostor-believed-engine](feedback_vertical_revenge_impostor_believed_engine.md) (도둑이 끝까지 진짜로 믿겨야·악역 천박/뻔뻔/멍청·중간 보상=장면 단위). + [face-theft-evidence-diet](feedback_face_theft_evidence_diet.md) — 증거 多≠정교·관객 퀴즈화 결함·왕 증거 3개·여주 주체성 강박 버리기(남주=단두대/여주=칼날)·속은남자 후회 스택. + [human-first-action-not-explanation](feedback_human_first_action_not_explanation.md) — 논리구멍=대사로 막지 말고 인간 1차 행동→다음 문제 자연발생, 안 되면 장면 잘라냄. **사용자가 붙여주는 피드백 ≠ 승인**(엔진충돌이면 기각·[[external-ai-evaluation-individual-validity]]). + [vertical-repetition-emotional-not-procedural](feedback_vertical_repetition_emotional_not_procedural.md) — **히트작은 반복한다·단 관객이 *맞는* 반복(감정/강탈/굴욕/지위전)이지 *외우는* 반복(돈흐름·누가들음·clip·post·기자·서명절차)이 아니다.** 중반 피로=반복 多가 아니라 대상이 감정→절차로 샌 것. 돈은 감정 먹잇감 OK·증명 절차 X.

---

## 🥈 장르·단계 트리거 (해당 진입 시만 — 파일명 + 훅 한 줄)

### 집필 보편 (10_writing_standard에 통합됨 — 상세 예문 필요 시만 원본)
- [translation-proof-no-cinema](feedback_translation_proof_no_cinema_2026_06_10.md) — 직역 자막에도 꽂히는 대사·카드/부제/무드 콜드오픈/영화병 비트 금지·성인 수위·감정 3축(워크스페이스 §B·§D-6-1·§F 통합).
- [easy-dopamine-over-logic](feedback_easy_dopamine_over_logic.md) — 쉽다>정교·천박>세련·구체 원형어>추상.
- [no-theater-tone](feedback_no_theater_tone.md) — 7차원 금지·비선형 연출 필수 (상세 예문).
- [vertical-dialogue-forward-show-limited](feedback_vertical_dialogue_forward_show_limited.md) — show-don't-tell은 vertical에 한정적·대사-forward·콜드씬 직관.
- [ai-dub-tone-independent-dialogue](feedback_ai_dub_tone_independent_dialogue.md) — 톤-독립 단일 의미 (히트작 10개 실증 상세).
- [english-vertical-hit-dialogue-tone](feedback_english_vertical_hit_dialogue_tone.md) — 북미 영어 히트작 대사 톤(사용자 필사 실증)·감정=라벨 아닌 form(파편·반복·신난 가십·구체 잔인함)·우리 영어 대본 평탄함 교정 기준.
- [protagonist-not-villain-voice](feedback_protagonist_not_villain_voice.md) — 주인공 대사 악녀톤 금지·착하고 순진하되 강단·부 자랑은 조연 입으로·주인공은 사랑/감정을 보여줌.
- [vertical-name-card-format](feedback_vertical_name_card_format.md) — 첫 등장 네임카드 = 풀네임+짧은 직함 1-2단어·서술형 역할/잉여정보 금지(`Jeremy Whitmore / Bears Captain`).
- [aigc-prompt-script-writing](feedback_aigc_prompt_script_writing.md) — △ 양식 상세·일기 검출 골격.
- [claude-voice-bias-vertical-failure](feedback_claude_voice_bias_vertical_failure.md) — 자가 평가 불신·외부 강제 layer.
- [real-human-speech-01s-test](feedback_real_human_speech_01s_test.md) — 0.1초 테스트 자동 폐기 7종 예문.
- [panic-begging-form-not-content](feedback_panic_begging_form_not_content.md) — 감정 폭발 대사 = 형식(속도·반복·파편·중첩)이 감정·설명조/아련 어미(~잖아…) 금지·느낌표 테스트·붕괴 끝만 무음. 본문 = 10_writing §D-1-1.
- [compound-tone-parentheticals](feedback_compound_tone_parentheticals.md) — 톤 지문 4축 상세.
- [tense-variation-required](feedback_tense_variation_required.md) — 13 시제 카테고리.
- [vertical-structure-hit-script-lesson](feedback_vertical_structure_hit_script_lesson.md) — 셰익스피어화 7대 차이.
- [humiliation-violence-standard](feedback_humiliation_violence_standard.md) — 모욕 비트 4+·폭행 성별 룰.
- [vertical-regret-man](feedback_vertical_regret_man.md) — 후회남 트로프: 무시·모욕·계륵 취급→마지막 후회. 속음은 진짜·"알면서 외면"=문학 레지스터 금지·후회는 너무 늦게·여주는 냉대.
- [ep1-full-deck-engine-demo](feedback_ep1_full_deck_engine_demo.md) — EP1 = 패 선포+엔진 실연(암시 0점). 남성향 = 절정 프롤로그→박탈→숫자 카운트다운 퀘스트·로어 대신 룰. 다크로맨스 = 여주 송곳니는 행동. (OFFERING 3버전·中 TITAN BORN 실증)
- [vertical-no-admin-power](feedback_vertical_no_admin_power.md) — 행정/법/정치 금지 어휘 12 패턴.
- [vertical-no-metaphor-dodging](feedback_vertical_no_metaphor_dodging.md) — 은유가 사건 본체 대체 금지·판정 3질문.
- [t4-sex-scene-standard](feedback_t4_sex_scene_standard.md) — sex scene 물리·카메라 표준.
- [male-conquest-female-psyche-dual-subject](feedback_male_conquest_female_psyche_dual_subject.md) — 🆕(2026-07-22) 고수위 금기물 이원 주체: 정복(행동·시각 후킹) = 남주 / 심리(배덕 내면) = 여주. 여주 유혹자/썅년 프레임 금지·3층 심리("어쩔 수 없는 척"→"안 되는데 사위인데" 동시 발화→쾌락·스릴 향유)·남주 내면 독백 금지. (14 While My Wife's Away 실증)
- [emotion-to-action-aigc-writing](feedback_emotion_to_action_aigc_writing.md) — "That breaks him" 금지·행동 sequence.
- [flashback-source-ep-tag](feedback_flashback_source_ep_tag.md) — 플래시백 출처 태그 3 format.
- [setup-before-payoff-5ep-minimum](feedback_setup_before_payoff_5ep_minimum.md) — setup은 payoff 5화+ 전.
- [paywall-declaration-timing](feedback_paywall_declaration_timing.md) — 보상 declaration = EP9 첫 씬.
- [iloveyou-budget-3-max](feedback_iloveyou_budget_3_max.md) — "I love you" 3페어 max.
- [pregnancy-engine-birth-late](feedback_pregnancy_engine_birth_late.md) — 출산 EP48-49 default.
- [final-episode-natural-ending](feedback_final_episode_natural_ending.md) — 마지막 화 Hard Cut 금지.
- [screen-rhythm-v3-blocks](feedback_screen_rhythm_v3_blocks.md) — 구 블록 양식(레거시 작품용).
- [female-gaze-camera-polish](feedback_female_gaze_camera_polish.md) — 부위 순회 금지·시선 우선.
- [spoken-english-native-polish](feedback_spoken_english_native_polish.md) — 원어민 polish 상세.
- [master-platform-safe-dual-version](feedback_master_platform_safe_dual_version.md) — 초고수위 이원화.
- [vertical-protagonist-voice-ownership](feedback_vertical_protagonist_voice_ownership.md) — 주인공이 말로 장면 소유·소품 의존 금지.
- [props-minimization](feedback_props_minimization.md) · [character-name-diversity](feedback_character_name_diversity.md) · [episode-scene-count](feedback_episode_scene_count.md)
- [per-episode-runtime-gate](feedback_per_episode_runtime_gate.md) — **LOCK 게이트 추가: 각 화 ≥1분**(플랫폼 스펙). 추정식 cuts*3.24+대사words*0.54·짧은 화는 응징/회수 dessert로 확장(패딩 X)·split 직후 재검.

### 매출·시장 baseline (집필·청사진 진입 시)
- [paid-vertical-master](feedback_paid_vertical_master.md) — 매출 baseline 총론.
- [demon-lord-failure-postmortem](feedback_demon_lord_failure_postmortem.md) — 9 실패 함정 + 광고 컷 reference.
- [na-vertical-ad-creative-principles](feedback_na_vertical_ad_creative_principles.md) — 광고 2축 분리·15룰·대시보드 환류 7항. 광고 감사 = 집필과 분리(`NA광고감사` 트리거). **⚠️ 자기 장르(북미 여성향 톡식로맨스) 안에서만 권위.**
- [ad-hook-novelty-over-proven-trope](feedback_ad_hook_novelty_over_proven_trope.md) — 주장된 시장 성과(히트 여부·사용자 주장 포함)를 검증 가능한 종이/블라인드 증거 위에 두지 말 것. "BUSSY·DRAGON·TITAN 검증 히트" 전제로 판정 뒤집었으나 후에 미검증("개구라")로 밝혀짐. 권위 주장에 결론 뒤집기 금지·증거 신뢰 = 블라인드 콜드리드 > 종이 사실 > 프레임워크 > 주장.
- [blockbuster-structural-insights](feedback_blockbuster_structural_insights.md) — EP1 비트 밀도·페이월 3중.
- [hit-library-v2](feedback_hit_library_v2_2026_05_19.md) · [hit-script-analysis-frame](feedback_hit_script_analysis_frame.md) — 분석 두 렌즈 병행.
- [conversion-runway-writing](feedback_conversion_runway_writing.md) · [unified-writing-flow](feedback_unified_writing_flow.md) — 7단계·무료/유료 분리 폐기.

### 다크 로맨스·romantasy 진입 시
- [dark-romance-relationship-centered-v2-3](feedback_dark_romance_relationship_centered_v2_3.md) — 관계 70/30·진위 5질문.
- [mythology-as-borrowed-flavor](feedback_mythology_as_borrowed_flavor.md) — 신화=소재 차용·지명도/정합성 비핵심·유명1-2+마이너 섞기·'급 떨어지는' 라벨(발키리 등) 금지.
- [monster-romance-not-dark-romance](feedback_monster_romance_not_dark_romance.md) — 야수=안전지대·학대=빌런 몫이면 hurt/comfort 몬스터 로맨스지 다크 아님. 다크=커플 사랑이 가학적. '다크' 오라벨 금지.
- [monster-romance-double-information-asymmetry](feedback_monster_romance_double_information_asymmetry.md) — 비대칭 두 겹=마찰 2배(여주 "이용한다 믿음/빠짐"+남주 "다 안다/다 내줌"). 외부 THE OFFERING(Dragon Lord) 실증·09_ashen_bride 적용 후보.
- [dark-romance-high-explicit-4-prescriptions](feedback_dark_romance_high_explicit_4_prescriptions.md) · [dark-romance-v2-5-v13-lessons](feedback_dark_romance_v2_5_v13_lessons.md) · [dangerous-sweet-cage-insights](feedback_dangerous_sweet_cage_insights.md) · [dark-romantasy-paid-vertical-v3-diagnosis](feedback_dark_romantasy_paid_vertical_v3_diagnosis.md)

### VFX 남성향 진입 시
- [vfx-male-power-fantasy-engine](feedback_vfx_male_power_fantasy_engine.md) — combat-read 데코보코·char count 금지.
- [male-ntr-line-betrayal-fuel](feedback_male_ntr_line_betrayal_fuel.md) — 배신=분노 엔진/NTR 화면화=이탈 폭탄·4선·복귀 절대 금지.

### 피칭 (phase_2)
- `config/pitch_references/MASTER_DATASET.md` (단일 진실) · `config/evaluators.md` §17 (가상투표 v2)
- [pitch-master](feedback_pitch_master.md) · [pitch-pass-fail-inference](feedback_pitch_pass_fail_inference.md) · [committee-b-persuasion](feedback_committee_b_persuasion.md) · [pitch-treatment-density](feedback_pitch_treatment_density.md)
- [pitch-skip-virtual-vote](feedback_pitch_skip_virtual_vote.md) — 가상투표·페르소나 자동검수 X·사용자 직접 읽음 (명시 요청 시만).

### 검토·LOCK (20_review_standard에 통합됨 — 배경 원본)
- [pov-speaker-utterance-not-error](feedback_pov_speaker_utterance_not_error.md) — **화자 POV 우선:** 인물 발화가 객관 사실과 달라도 오신/거짓/허세면 오류 아님. 3자 전지 시점 오류판정 금지(dramatic irony·빌런·허세 붕괴). 진짜 오류=지식선후·물리·연속성·타임라인 등 화자 의도 무관 기계적 모순만. 본문 = `20_review_standard.md` §2E.
- [lock-fix-volume-writing-diagnostic](feedback_lock_fix_volume_writing_diagnostic.md) — LOCK 수정량 = 집필 품질 메트릭 (v49 학습).
- [lock-class-sweep-not-oneoff](feedback_lock_class_sweep_not_oneoff.md) — 같은 류 오류 반복 발견 = 패치가 시간표 선명화→숨은 모순 노출·초반 패스 좁음. 해법=LOCK 직전 *클래스 grep 전수*(로지스틱스: 소지품/정보경로/위치 · 표현: 문학지문/관용구/`the [형용사] face` 물건라벨 변형). 한 줄 교체·절차 보강 X.
- [lock-exhaustive-line-audit](feedback_lock_exhaustive_line_audit.md) — per-line 전수 방법.
- [voice-lint-gate-pass](feedback_voice_lint_gate_pass.md) · [agent-roster-orchestration](feedback_agent_roster_orchestration.md) · [fresh-eyes-full-inspection](feedback_fresh_eyes_full_inspection.md) · [self-evaluation-pitfalls](feedback_self_evaluation_pitfalls.md) · [persona-system-v2](feedback_persona_system_v2_2026_05_19.md) · [revision-meta-principles](feedback_revision_meta_principles.md) · [pre-final-writing-principles](feedback_pre_final_writing_principles.md)

---

## 🥉 작업 방식 (필요 시)

- [kr-native-then-sell-global](feedback_kr_native_then_sell_global.md) — 🆕(2026-08-03) **만들 때는 100% 로컬 기준, 팔 때는 자막만 붙여 확장.** 타깃을 좁힌 것 ≠ 시장을 좁히는 것. 기획안에서 글로벌 논거를 빼면 시장 규모를 스스로 깎는 것이고, 반대로 글로벌 어필한다고 집필 기준을 흔들면 로컬에서 먼저 죽어 팔 물건이 없어진다. 글로벌 논거 = 판매용 섹션으로 분리 + "집필 시 펴놓지 말 것" 명시. 판정 = 로컬 껍데기 안에 보편 감정이 있는가. (흑길동 2회 교정)
- [no-appearance-rating-in-proposal](feedback_no_appearance_rating_in_proposal.md) — 🆕(2026-08-01) 기획안에서 빼는 건 **생김새 스펙**(얼굴상·슬렌더/풍만·머리 길이·미인 판정)뿐. 옷·태도·굴욕 비트는 살린다(빼면 손해). 스펙만 도려내고 대체 문장 발명 금지. 캐논 p0_source 비주얼 지시는 유지.
- [rechecked-episodes-are-new-manuscript](feedback_rechecked_episodes_are_new_manuscript.md) — 🆕(2026-08-11) **회수본은 기검수 회차도 처음 보는 원고로 다시 읽는다.** 미반영 목록으로 축약 금지(사용자 교정). 직전 판본 diff를 떠서 *바뀐 자리*를 따로 볼 것 — 신규 오류는 거의 거기서 난다(16_moses 실증: 맞던 의식 문구가 개악·새 위반 컷 신설·전제 붕괴 구멍 2라운드 미검출).
- [selling-point-sheet-format-is-the-spec](feedback_selling_point_sheet_format_is_the_spec.md) — 🆕(2026-08-19 · **2026-08-25 기준 파일 교체**) **CD1 셀링포인트 = 팀 공용 xlsx 템플릿 서식이 규격.** 🚨 기준 = `C:\Users\Rowan\Downloads\[EN_AI] Selling Point_Template.xlsx`(Template + 작품 10탭) · 뼈대 = `Template` 탭 / 내용 모범 = `One Night with the Dragon Lord` 탭 · **스토리텔링은 `AI 신규 생성 페이크`에만**(20~30초 안에 압축 완결 · 컷별 스토리텔링 · VO로 연결 · 맛깔 대사 · 대본에 없어도 됨) / **기존 장면 활용 MKT = 축별 컷 묶음, 스토리텔링 아님** · G열 = 16.5 원본 유지(45.5 금지) · D1 = 작성 상태. 본문 = `config/40_selling_point_standard.md` · 빌더/검증 = `tools/build_cd1_sheet.py`·`cd1_validate.py`. 내 지난 산출물 2개가 **MKT Idea(실제 장면 묶음) 섹션을 통째로 누락** + 밴드 글꼴 15→10 · 빈 EP 행 잔존 · 예시문 서식 잔존. 손으로 만들지 말 것.
- [writer-comment-standard](feedback_writer_comment_standard.md) — 🆕(2026-07-25) **외부 작가 대본 코멘트 = `config/30_writer_feedback_standard.md` 정독 후.** 4대 렌즈(시청자>장르>캐릭터 매력>제작)·대사 = 교체 실물·수위는 항상 더 세게·AI 헛다리 필터(나노 연속성·미스터리 훈수·수위 자제·로직 프레임 = 금지). 작가 회수본 = §4 환류.
- [pushback-user-contradiction](feedback_pushback_user_contradiction.md) — **사용자 지시 무조건 수용 금지.** 확정 엔진·앞선 지시·원작·증거와 충돌하면 반박 지점 짚고(내 해석+확인) 집행. 사용자 실언·모순이 본문에 박히는 것 방지(실증: "여주 안 당함"→"안 꺾임" 정정). 단 진성 충돌만·트집 X.

- [writer-reference-draft-mode-learn-loop](feedback_writer_reference_draft_mode_learn_loop.md) — 산출물 = 인간 작가 참고초안 모드여도 내 형식/rigor 불변·작가 회수본 평가→학습 듀티.
- [transplant-intensity-not-actions](feedback_transplant_intensity_not_actions.md) — 🆕(2026-08-12) **세계 치환 모드에서 "원작만큼 세게" ≠ "원작이 한 짓 그대로".** 강도·기능·비트 자리는 원작 이상, 행위는 새 세계 것으로 재발명. 26번에서 2회 반복 실수(v3 치환 → v8 원상복귀) — **강도 보정 라운드가 곧 행위 복사 라운드가 되는 게 함정.** 원작 재독 시 행위 말고 **기능만 적어서** 대조표를 짜라. 각색 모드(verbatim 계승)와 정반대 룰이니 진입 시 모드부터 못박을 것. 치환하면 원작보다 나아진다(26번 = 개별 고문 나열 → 앞 화 상처가 다음 화 흉기가 되는 한 사슬).
- [adaptation-conservative-no-forced-rewrites](feedback_adaptation_conservative_no_forced_rewrites.md) — **각색 검토·수정 = 대사 억지 변경 금지·최대한 그대로/최소 변형·기능보존 리라이트는 정말 불가피할 때만.** 다른 장르/트롭/구조(히트작 포함) 기준 금지(다른 작품化 경계). source(원작)≠adaptation(우리 작성) — 자기 창작물 자기 기준 채점 순환논리 금지·약한 대사를 번역 clean-up으로 가리지 마라. 추가 대사도 캐릭터별 확립 톤 준수. 지문(△) 보완은 적극 OK(창작금지=새 스토리 발명 금지지 지문 보완 금지 아님). (12 EP1-13 LOCK 실증)
- [version-anchor-commit](feedback_version_anchor_commit.md) — 메이저 변경 전 새 v{N} 분기.
- [bulk-script-verify-strict](feedback_bulk_script_verify_strict.md) — 일괄 변환 후 깨진 패턴 grep 의무.
- [docx-conversion-drops-table-textbox-text](feedback_docx_conversion_drops_table_textbox_text.md) — python-docx paragraphs-only는 표/텍스트박스 대사 누락 → 유령 결번·공란 오진. 결손 지적은 원본 docx raw XML(document.xml 전 w:p)로 대조 후 보고.
- [speaker-tag-roster-mismatch](feedback_speaker_tag_roster_mismatch.md) — 병렬 배치 집필 시 화자 태그가 로스터의 *다른* 인물명으로 오기되면 전 기계 게이트 통과(register_census min-lines 스킵·char-complete 로스터 실존·voice 대상외). LOCK/참고본 전 화자태그 vs Characters 교차검증 · 번역 패스 = fresh-eyes QA층. (12 EP20 Delphine→NORA 오기 실증)
- [external-korean-script-review-belt](feedback_external_korean_script_review_belt.md) — 외부 한국어 대본 검토 = 목적별 모델 분배 belt(fresh-eyes opus·cold-read 3 sonnet·단순귀 sonnet·히트작 DNA 앵커 opus+보조 sonnet·병합 나) + 한국어 로맨스 히트작 3-4편 벤치마크 필수·단일패스 금지. voice_lint/한국어0 게이트 = 한국어엔 무효(오탐)→grep 대체.
- [script-file-zero-meta](feedback_script_file_zero_meta.md) — 대본 파일 = 타이틀+본문만.
- **[path-discipline](feedback_path_discipline.md) — 🚨 사용자에게 경로 말할 땐 언제나 절대경로. 모든 작업 공통·반복 지적 (2026-08-07 재확인).**
- [no-ask-autonomous](feedback_no_ask_autonomous.md) · [meta-trust-and-verify](feedback_meta_trust_and_verify.md) · [script-english-only](feedback_script_english_only.md) · [question-alarm](feedback_question_alarm.md) · [web-research-policy](feedback_web_research_policy.md) · [external-ai-input-handling](feedback_external_ai_input_handling.md) · [external-ai-evaluation-individual-validity](feedback_external_ai_evaluation_individual_validity.md)

## 작품 특수

- [project-dist-package](project_dist_package.md) — 🆕(2026-08-05) 사내 배포 패키지 = `tools/build_dist.py` · 문서 원본 `tools/dist_docs/` · 히트작 포함 확정 · 포팅 시 터진 인코딩 함정 2종.
- [project-locked-out-interactive-game](project_locked_out_interactive_game.md) — 🆕(2026-08-05) LOCKED OUT 인터랙티브 게임 — 작업 폴더 = Codex workspace(`...\Codex\scenario-automation-codex\projects\_reference\07_locked_out\`). 설계안 v017(결정34+서비스·엔딩 체계)·조감도 v020·Apps Script 세계수 에디터가 최신, START_HERE/매니페스트는 스테일.
- [project-she-stole-my-face-status](project_she_stole_my_face_status.md) — 정본 = CLAUDE.md 행 + meta 파일 우선.
- OFFERING 4종 (폐기 작품·참조만): [high-explicit-direction](project_offering_high_explicit_direction.md) · [isolde-charter](project_offering_isolde_character_charter.md) · [vael-charter](project_offering_vael_character_charter.md) · [v34-writing-charter](project_offering_v34_writing_charter.md)
- [project-overview](project_overview.md)

**archive:** `memory/archive/` · 그 외 73+ 파일 = 필요 시 폴더 검색.

---

## 자가 검수 (매 phase 진입 시)

1. 해당 시점 workspace 문서(00/10/20) 정독했는가?
2. 작품 엔진 메모리 + 장르 트리거 정독했는가?
3. 매칭 히트작 raw 3-5 EP + 직전 배치 raw 정독했는가? (집필 시)
4. State Ledger 준비/갱신했는가? (집필 시)

→ 하나라도 NO = 작업 중단·먼저 정독.
- [내 프로즈 디폴트 = 추상·완곡 세탁](my-prose-defaults-abstract-euphemistic.md) — 기획안·집필대본·각색대본 전부: 관념어·욕망 세탁·정의 프레임·개념 라벨·MC체 = 병 7종; 감정은 문장 자체가 실어야, 레지스터 모델 = 사용자 문장.
