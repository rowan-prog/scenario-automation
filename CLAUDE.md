# 시나리오 자동화

AIGC 숏폼 vertical drama 시나리오 제작. 최종 산출 = `projects/[작품]/07_final/[작품]_FINAL_v{N}.md`.

> **대본 문서 = 제1부(기획·개요) + 제2부(정식 회차 대본) 2부 구성 — 각색·신규 공통 필수** (2026-07-02). 상세 = `config/10_writing_standard.md` §B-0.

---

## 핵심 문서 3개 (2026-06-10 일원화 — 사용 시점별)

| 시점 | 문서 |
|---|---|
| 모든 작업의 근본 원리 (작품 진입 시 1회) | **`config/00_vertical_dna.md`** — 8 매체 조건·모든 룰의 모체 |
| 집필·재집필·가필 | **`config/10_writing_standard.md`** — 진입 게이트·△ 양식·연속극 구조·대사·State Ledger·모욕 표준 |
| 검수·LOCK | **`config/20_review_standard.md`** — 2모드·Track A/B·토큰 회계(tier-weighted belt·직교 sweep·병렬 fan-out)·입력 무결성 게이트·쇼러너 merge·§4-1 수술 파이프라인 |
| **외부 작가 대본 검수·코멘트** | **`config/30_writer_feedback_standard.md`** (2026-07-25 제정) — 사용자 코멘트 실물 3종 + AI 헛다리 대조로 도출한 4대 관점·형식 법칙·헛다리 필터·프로세스. 작가 회수본 올 때마다 §4 사례 환류 |

구 문서(hard_rules·final_review_flow·agent_operating_rules·lock_pipeline_standard·phase_4 prompt) = 위 3개로 통합·스텁만 잔존 (`config/_archive_2026-06-10/` 원문 보존). master_guide_v3(5816줄) = 집필 컨텍스트 진입 금지.

## 보조 자료 (필요 시점만)

| 필요 | 위치 |
|---|---|
| 작품 진행 메타 (이력 단일 진실) | `projects/[작품]/[작품]_00_meta.md` |
| 검증 히트작 raw | `config/vertical_drama_hit_scripts/` (집필 진입 시 매칭 3-5 EP 강제 정독) |
| 히트작 분석 / 페르소나 / 평가위원 | `config/vertical_drama_hit_scripts_analysis/` · `config/personas/`(검토 시) · `config/evaluators.md`(피칭 시) |
| 타깃 자료 | `config/target_research/` |
| 템플릿 | `config/engine_brief_template.md` · `mkt_selling_points_template.md`(온디맨드) · `meta_template.md` (visual_lock·production_handoff = 2026-07-13 폐지 — 애셋 단일 진실 = 본문 △ + Ledger ④) |
| Reference / 피칭 데이터 | `config/reference_scripts/INDEX.md` · `config/pitch_references/MASTER_DATASET.md` |
| 검수·집필지원·수술·발상 agent 14종 정의 | `~/.claude/agents/` (전원 frontmatter `model:` 핀 = opus 이하 — 운용 룰 = `config/20_review_standard.md` §7 3-tier 모델맵·직교 sweep·집필지원 W1-W3 = `10_writing_standard.md` §A-1. 수술 3종 = `script-surgeon`·`consistency-sweeper`·`copy-candidate-generator` · **발상 = `idea-diverger`**(2026-07-30 신설 · opus+effort:low = 저사고 발산 전용 · 입력은 적게·금기 2~3개만·출력 15~20줄 무근거 + 무리수 쿼터 · 선별/검증은 메인)) |
| 기계 도구 | `tools/build_treatment_doc.py`(회차 트리트먼트 docx — 무료=spec 인용/유료=`_paid_run_*.txt`) · `tools/voice_lint.py` · `tools/continuity_lint.py` · `tools/format_pass_verify.py` · `tools/pacing_lint.py`(공간 경제·절단 구조 6검사) · `tools/register_census.py`(인물별 레지스터/코치봇 — 둘 다 2026-07-10 신설) · `tools/esl_hardwords.py`(대사 어휘 Zipf 직관 스캔 — 2026-07-15 신설·localization 워크스페이스 포팅) |
| **라이터스룸 강의록 (집필·각색·검수 진입 정독)** | `config/vertical_drama_hit_scripts_analysis/craft_lecture_liv_writersroom2.md` — 2026-07-10 사용자: "vertical drama의 정수" (예문 verbatim 보존·요약 대체 불가) |
| 장르·작품 특수 메모리 | `memory/` (MEMORY.md 인덱스·호출 트리거 기반) |

---

## 워크플로우

```
phase_0 (아이디어) → phase_1 (러프 청사진) → phase_2 (피칭) → 피칭 결과
  → phase_3 (완성 청사진 + engine brief) → phase_4 (집필 = 10_writing_standard)
  → phase_5/6 (검토·패치 = 20_review_standard 경량) → phase_7 (LOCK = 20_review_standard 풀)

부가 트랙: phase_a (각색) / phase_b (외부 대본) / phase_c (외부 피드백) / phase_p (플랫폼 기획안 — 러프→정식 제출본)
```

### 작업 라우팅 (2026-07-06 — 세션 모델 무관·이 표대로 실행)

| 들어온 일 | 절차 (문서·§) | 실무 배치 |
|---|---|---|
| 아이디어→러프 청사진 (phase 0-1) | `00_vertical_dna.md` 정독 → 청사진 → meta 생성 | 메인 설계 + W1·W2 = sonnet |
| 피칭 (phase 2) | `config/evaluators.md` §17 + `pitch_references/MASTER_DATASET.md` (가상투표 = 명시 요청 시만) | evaluator-panel = opus → 판정 메인 |
| 완성 청사진·engine brief (phase 3) | 템플릿 (`config/engine_brief_template.md` — §5 가드레일 블록 포함) | 메인 지시서 → 초안 = opus |
| 집필 (phase 4) | `10_writing_standard.md` §A 진입게이트 → §A-1 지시서 → §B~F | 프로스 = opus agent(논문병 가드레일) → 채택 판정 메인 |
| **각색 (phase_a)** | **`prompts/phase_a_1`(청사진·4모드·치환표) → `prompts/phase_a_2`(집필 델타) + `10_writing_standard.md` §A-2 배치 기계 게이트**(치환 잔재 grep·골격 드리프트 — 2026-07-13) | 프로스 = opus agent · 잔재/골격 대조 = consistency-sweeper(sonnet) |
| 배치 점검 (phase 5/6) | `20_review_standard.md` §1 경량 + §8 평시 haiku 3종 상설 | haiku 3종 + 한 줄 수술 메인 |
| LOCK (phase 7) | `20_review_standard.md` §1 풀 belt(병렬 fan-out) → §2 Track B → §4 머지 → §5 **LOCK 후보 → 사용자 콜드리드 도장 → LOCK 확정** (핸드오프·비주얼락 환류 = 폐지·마감은 meta 갱신뿐) | belt = §7 모델맵 |
| **LOCK 후 피드백·수술** | **`20_review_standard.md` §4-1 수술 파이프라인** (판정→계획서→v분기→기계/프로스→머지 체크리스트→게이트→마감) | 기계 = 메인 직접 · 프로스 = script-surgeon(opus) · 정합 대조 = consistency-sweeper(sonnet) |
| 외부 대본/피드백 (phase b/c) | **입력 무결성 census 먼저(`20_review` §1 — 변환 결손 대조)** → external-intake 막장-필터 → §4 머지 | external-intake = opus |
| **작가 집필 대본 코멘트** (검수 후 작가 반환) | `config/30_writer_feedback_standard.md` — 3패스(콜드리드→장르·구조→라인)·코멘트 = 사용자 관점·형식 법칙·AI 헛다리 필터. 캐논 = 해당 작품 트리트먼트+내용요건 | 콜드리드 지점 신고 = funnel-cold-reader(sonnet) / 코멘트 작성·선별 = 메인 직접 |
| **플랫폼 기획안 (phase_p)** | `prompts/phase_p_platform_proposal.md` — **진입 게이트(hit_dna #9 + craftcard §5 공간 경제 정독 · 2026-07-30)** → **0단계 설계 확정 문답(fan-out 전 · 컨테이너 지도 포함)** → 대원칙 9종(원안=정본 verbatim·로그라인 5요소·갈등축 발명 금지·§C-4-2/§C-2-2 게이트·룰 정합·dramatic irony·내용요건=놓치기 쉬운 것만·사람 말 문체·**컨테이너 구조=방 순회 금지**) → 기계 게이트 7종(⑦=`pacing_lint.py --treatment` 컨테이너 계측) → 빌더 `tools/build_vigloo_proposal.py` (2026-07-16 제정 · 실증 = My Million-Dollar Reset·While My Wife's Away) | 0단계 문답 = 메인↔사용자 / **안목(로그라인·내용요건) = fable 1기 고정** / **머지 후 문체 콜드리드 = opus 별도 인스턴스 (2026-07-30 사용자 룰 — fable에서 하향)** / 훅·아크 = opus / 트리트먼트 = sonnet(보강 0 기본값) / 시놉·캐릭터 = sonnet / 메타 = haiku → 머지·게이트·docx = 메인. **Fable = 안목 유닛만 — 벌크 프로즈 배정 금지 (2026-07-22 2차 정밀화·근거 = 절차문 분업 §)** |
| 한국어 정본 검토 | 메모리 [[external-korean-script-review-belt]] (한국어 벤치마크 필수·voice_lint 무효→grep 대체) | opus + sonnet belt |
| 산출 라운드 (타이틀·광고카피·셀링포인트) | 후보 = 다시각 독립 N기 병렬 → 메인 선별(§4-1 머지 체크리스트 준용) → 사용자 확정 | 생성 = copy-candidate-generator(opus) / 추출 = mkt-selling-point-extractor(sonnet) |
| **발상이 막힐 때 (창의력 요구 지점)** (2026-07-30 신설) | 기획 장치·의식·설정 대안 / 클리프행어·비트·펀치라인 대안 / 한 공간 컨테이너 안 자극 비트 채우기 / 피드백 시 "더 나은 대안". **입력 = 과제 한 줄 + 요약 5줄 이내 + 절대금기 2~3개** (맥락을 많이 주면 기존 텍스트로 수렴해 발산이 죽는다) → 출력 = 무근거 15~20줄 → **선별·정합 검증·엔진 가드레일 = 메인, 확정 = 사용자.** 다시각 = 프레이밍 달리해 N기 병렬 | idea-diverger(opus·effort low) |
| 구조·룰·워크플로우 개정 | **유일한 Fable 투입처** — 개정 후 이 표 + 해당 § 즉시 갱신. **실무 세션(opus/sonnet)이 구조 결함을 발견하면 직접 개정하지 말고 발견 보고까지만 — 개정은 사용자가 Fable로 전환 후** (2026-07-10 실증: sonnet 구조 개정이 진단 절반 누락 + 오진 메모리 기록) | Fable 1회성 |

## 작품 파일 명명 규칙 (필수)

`projects/[NN]_[slug]/[NN]_[slug]_[단계번호]_[단계명].md` — 폴더 prefix 동일·하위 폴더(`05_episodes/`·`06_reviews/`·`07_final/`)도 prefix 적용·폐기 폴더 = `_X_NN_slug`(자동 차단).

---

## 현재 작품 (2026-06-10)

| 폴더 | 작품 | 현재 상태 |
|---|---|---|
| `_X_01_titan_born` · `_X_02_the_offering` · `_X_04_heiress_clause` · `_X_08_reborn_at_ten` · `_X_09_scarred_bride` | (폐기 5종) | 🚫 작업 금지 — `_X_09_scarred_bride`는 2026-07-10 `09_ashen_bride`(동일 컨셉 후속안)와 번호 충돌 발견돼 리네임(내용 무손실·git 이력 보존). 이력은 각 meta 파일 |
| `03_most_wanted_ship` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | phase_2 완료 |
| `09_ashen_bride` | THE BEAST KING'S WOUNDED BRIDE / 야수왕의 상처입은 신부 | phase_2 (피칭덱) — 미녀와야수 역전 고수위 몬스터 로맨스·정서 레퍼런스 Broken Vows |
| `10_buried_heir` | (가제) 임신한 애첩과 내가 묻어버린 신혈 계승자 | **LOCK 2026-07-06 — 정본 = `07_final/10_buried_heir_FINAL_v2.md` (한국어 54화·무료 1~10·2부 구성).** v1 LOCK → 콜드리드 수술 v2(제우스 카드 47화 봉인·28화 타르타로스 선언 제거·23화 과적 삭제·오리온 카피 교체·45화 환상 리컷·제1부 훅 31건 정합) → fresh-eyes 감사에서 시간축 역회귀 1건 잡아 복원 → LOCK. 中 이혼복수극 원작 구조 보존 + 올림푸스 신화 각색. 잔여 = 타이틀 확정(후보 = `10_buried_heir_04b_title_candidates.md`)·영어 번역(사용자). 이력 = `10_buried_heir_00_meta.md`. 핵심 메모리 = [[vertical-regret-man]] [[panic-begging-form-not-content]] |
| `06_she_stole_my_face` | SHE STOLE MY FACE | **정본 = `07_final/06_she_stole_my_face_FINAL_v70.md` (48화).** v63 LOCK 이후 사용자 cold-read 라운드(v64~v70): ①초반 가속 — EP1-3→2화 + 계단 EP3+EP4 병합 → **50→48화**(무료런 8→7·Noah 구원/희망 EP7·PAYWALL@EP8) ②대사 census de-rhythm(소유/나열 tic ~19→북엔드2+클라이맥스1) ③모녀=한 몸 공범(아일린 함께 침몰) ④goad 중복 해소(아파트=사회적 말살) ⑤노아 de-parrot(확신=행동) ⑥청중 스케일 표준화 ⑦프레임-탈피 소수정(on repeat→live·EP45 범죄자 선퇴장 등). 타임라인=이른 오후 클리닉→저녁 크래시→밤. 게이트: 한국어0·48화·HardCut47·END HOOK47·PAYWALL@EP8·END1. 상세 이력 = `06_she_stole_my_face_00_meta.md`. **버전 룰: 메이저 = v{N+1} 복사 후 수정.** **2026-07-10 사후분석(수정 안 함 — 인사이트만 흡수, Fable 재감사로 완성):** "TV드라마 같다" 판정의 3중 원인 실측 — ①행사 순회 구조(EP13~40 단발 행사 공간 순회·EP29-41 13화 연속 리셋 오프닝) ②net-zero 라운드(빌드업병 — 제거해도 뒤가 안 무너지는 찌르기 라운드 반복) ③쿨슬롭 레지스터(Lena 170라인 감탄 0·Noah 코치봇 cool톤 72%·빌런 Mara만 클린 = AI가 주인공/조력자를 망치는 편향). 8회 LOCK 사이클이 셋 다 놓침 → `pacing_lint.py`+`register_census.py` 기계 게이트 + §C-2-1·C-4-0·D-5-0 신설로 재발 방지. 핵심 메모리 = [[occasion-hopping-space-economy]] [[vertical-rhythmic-list-fuel-only-in-scarcity]] [[english-vertical-hit-dialogue-tone]] [[protagonist-not-villain-voice]] [[vertical-revenge-impostor-believed-engine]] [[vertical-regret-man]] |

| `11_the_outcast` | THE OUTCAST (CN 원어·남성향 사이다 파워판타지·NA 영어 타깃) | **검토 재교정 v2 (2026-07-08).** 리뷰 = `06_reviews/11_the_outcast_review_v2.md`. **v1의 EP34 결번·EP21~28 공란·EP37 대사공란 = 전부 철회 — `source_CN.md` python-docx 변환 손실(표/텍스트박스 대사 누락)이었고 원본 docx엔 50화 다 있음. source_CN.md = docx 완전추출본으로 교체 완료.** 실제 상태 = 50화 완결·엔진 A급. 잔여 = 하드오류 아님·전부 정리/보강급: 이중리빌 강도조정·EP42~43 최종처치 온스크린 컷·표기정리(EP37 씬넘버·EP7 헤더/오타·경기장명 드리프트)·정합소소(발렌상처·황제인지·알바도르동선·매수증인·达里安선고)·NA관리(테사·목걸이 레퍼런스·维莱拉/莱拉 이름충돌). 순서 = 소정리→영어 각색→라인검수→LOCK. 이력 = `11_the_outcast_00_meta.md`. 핵심 = [[na-target-intensity-calibration]] [[male-target-commercial-kwaegam-northstar]] [[no-hero-defeat-in-saida-power-fantasy]] [[docx-conversion-drops-table-textbox-text]] |
| `12_hired_to_ruin_me` | I Married the Woman Hired to Ruin Me / 날 파멸시키라고 고용된 여자와 결혼했다 | **🚨 대사 전면 재작성 라운드 (2026-07-15).** 사용자 콜드리드 판정 = 전 대사 코퍼스 레지스터 불합격(완곡·암시·재치 대구·압축 은유·큐의존 — "개구리다"·첫 대사부터) → **EP1~13 LOCK 해제.** 정본 = `07_final/12_hired_to_ruin_me_FINAL_v2.md` (50화·v1/v2 보존·KR 참고본 = `_v2_KR.md`). 부가A 각색(원작 = The CEO's Tempting Secretary → GL 치환·감시카메라 이중생활 엔진 보존). 이 판정에서 §D-2-1 직설 레지스터 표준·esl_hardwords.py·tts-literal-ear 심문5 신설([[dialogue-direct-register-wit-ration]] — 사고 경로: 유창해서 검수 통과 + 스타일 오분류 되돌림 + 무드 라벨 기각). **재작성 원칙 = 전개/비트/지문 불변·대사만 직설 재작성(§D-2-1)·수위는 올라가면 올라갔지 순화 금지.** EP1~3 적용본 = `07_final/12_hired_to_ruin_me_FINAL_v3.md`(교체 16+정합 6·게이트 통과·v2 보존) — **사용자 콜드리드 도장 대기** → 도장 후 EP4~50 fan-out → KR 동기화. 이력 = `12_hired_to_ruin_me_00_meta.md`. 핵심 = [[dialogue-direct-register-wit-ration]] [[english-vertical-hit-dialogue-tone]] [[protagonist-not-villain-voice]] |

| `13_janitor_billionaire` | Divorcing the Janitor, Begging the Billionaire / 청소부와 이혼하고, 억만장자에게 빌다 | **무료런 심화 v2 2026-07-15.** 정본 = `07_final/13_janitor_billionaire_FINAL_v2.md` (16화·무료1-8 심화+유료9-16 무변경)·무료회차 한국어본 = `_FINAL_v2_KR_freerun.md`(EP1-8만). v1 LOCK(2026-07-14) 보존. **"디벨롭=사건 추가"로 오독→사용자 교정: 레퍼런스(외부 50화본) 텍스처 이식=AI 조립병(사건·공간·용어 과적)·반면교사. 방향=8화 척추 불변·강도만 심화**(굴욕/수위/예열/훅/네이티브 대사·de-repetition·de-exposition·de-rhythm, 사건0·공간0). 부가A 각색(원작 = 외부 러프 영어 대본 `DON'T PISS OFF YOUR SUGAR MOMMY'S HUSBAND` = 135씬 1국 압축 완결본). 남성향 30-50 리벤지/히든아이덴티티/재벌·A급 AI실사. 3대 재발명: 헬스장→오피스빌딩 야간청소부(카트 미는 억만장자 훅)·맞는노인 로라친부→키어런 시아버지(빌런 로라 집중)·별개 후계자 리빌→키어런 자신=베일 홀딩스 회장(자기가 내친 청소부에게 무릎꿇는 아이러니). 집필 = opus 프로스 agent 2배치·검토 = 기계4종+haiku/sonnet 3종(수정 7건 전부 △/오류정정·대사 재작성0). **사용자 각색 원칙 = 원작 대사 verbatim 최대 계승·억지변경 금지·불가피할 때만 기능보존·추가 대사도 캐릭터 원작톤 준수.** 이력 = `13_janitor_billionaire_00_meta.md`. 핵심 = [[no-hero-defeat-in-saida-power-fantasy]] [[hero-dialogue-hardboiled-not-edgelord]] [[male-target-commercial-kwaegam-northstar]] [[adaptation-copy-source-dialogue-verbatim]] |

| `14_my_daughters_husband` | My Daughter's Husband / 딸의 남자 | **phase_p 제출본 v2 (2026-07-29)** — **여성향** 금단(장모×사위)·초고수위·50화·무료 8·발화 EN·오리지널·中文 생략. 폴더 리네임(`14_while_my_wifes_away`→현재·git mv). 인물 = 빅토리아 애쉬포드 43·이든 머서 30·슬론 머서 25·폴라 노왁 58. **슬론 = 의붓딸**(빅토리아가 33에 20살 연상과 재혼·당시 슬론 15·십 년 동거·1년 전 사별 — 친딸 배신 거부감 제거 + 배덕 유지·남성향 18은 친장모 유지). **시점·VO = 빅토리아 단독**(엔진 = 욕망의 증명·참으려다 무너짐). 산출 = 기획안 `Vigloo AI Drama Proposal_MY DAUGHTER'S HUSBAND.docx`(spec = `_p1_proposal_spec_v2_A_victoria.txt`) + **트리트먼트 `딸의 남자_회차 트리트먼트_1-50화.docx`**(무료 상세/유료 2~3문장). 캐논·내부규칙 = `_p0_source.md`·이력 = meta. 공통 문법 = 공간 불변·한 씬이 여러 화 시퀀스·시간 넘기기 금지·추리 금지·심리 전량 VO(레퍼런스 `Road of Lust.역대본.md`). **2026-07-30 컨테이너 재설계 — 유료 42화 = 컨테이너 4(각 한 공간·한 시간대·9~10화) + 브리지 3. 미수를 방마다 하나씩 배치 = 금지(메모리 [[occasion-hopping-space-economy]] 컨테이너 법칙).** 잔여 = 사용자 검토·TBD |

| `18_while_my_wifes_away` | While My Wife's Away / 아내가 없는 사이 | **phase_p 제출본 v1 (2026-07-29)** — **남성향 쿠거**(장모×사위)·초고수위·50화·무료 8·발화 EN·오리지널. **14와 소재만 공유하는 별개 작품**(사용자: "장모와 사위라는 소재로 여성향, 남성향을 한 거") — 인물·타이틀 전부 신규: 콜 베넷 27 / 다이앤 케슬러 46 / 에이바 베넷 28 / 로사 델가도 58. **시점·VO = 콜 단독·과거 회상형.** 엔진 = 장모의 잡아뗄 수 있는 은근한 어프로치 → 못 참고 달려듦 → "이러면 안 돼. 넌 내 딸 남편이야"(손은 안 치움) → 아침 "없던 일이야" → 그날 밤 열린 문. **야동 금지 규격 = 관계로 점프·전희 요약·생략 전부 금기**(파는 건 도달이 아니라 도달하기까지). 다이앤 속마음 폐쇄·콜 계산남 금지. 산출 = 기획안 + **트리트먼트 `아내가 없는 사이_회차 트리트먼트_1-50화.docx`**. **2026-07-30 컨테이너 재설계 — 공간 총량 4곳(주방/계단·장모침실/딸부부침실/이층복도)·유료 = 컨테이너 4 + 브리지 3·1화 현재시제 공간 7→2로 압축.** 이력 = `18_while_my_wifes_away_00_meta.md`. 잔여 = 사용자 검토·TBD |

| `15_reign_predators_office` | 군림: 포식자의 오피스 / REIGN: THE PREDATOR'S OFFICE | **phase_p 제출본 v2 (2026-07-28)** — 남성향 오피스 신분역전·섹슈얼·KR 발화·KR 20-40 남성·총 50화 내외(TBD)·무료 8·오리지널·中文 생략·레퍼런스 SarosTV <신생>. 제출본 = `Vigloo AI Drama Proposal_REIGN - THE PREDATOR'S OFFICE.docx` (2026-07-28 개정 템플릿 규격 — 원본 셀 직접 채움·spec = `_p1_proposal_spec_v2.txt`)·원안 정본 = `_p0_source.md`·이력 = `15_reign_predators_office_00_meta.md`. 엔진 = 무요구 군림(여자들이 스스로 바침)·무료 8화 = 세아 단일 축·3히로인 캐논(세아 33 조련축 / 채은 26 이중성·공범 진화 / 윤서희 39 배덕축 = 최도혁 아내)·채은/최도혁/서희 = 유료 카드·자극 2층위(노골+은근) 장면어 운반·회차 부제 금지. 잔여 = 사용자 검토·채은 동기/결말 캐논 확인·TBD(총 회차·일정·제작비)·EN 타이틀 표기 확정 |

| `16_moses` | 내 남편은 거지 모세 / I Chose a Slave, But He Parts the Sea | **작가 집필 1~21화 2차 회수본 검수 완료 (2026-08-03).** 여성향 회귀 리벤지 판타지·50화·무료 1~7·각색 원작 《Swapped to a Beggar But He is Apollo》(48화·플롯 구조 그대로 = 사용자 확정). **작가에게 나가는 것 3종 = `내 남편은 거지 모세_각색 가이드_v18.docx` · `_회차 트리트먼트_1-50화_v7.docx` · `_1-21화_검수코멘트_v11.docx`**(코멘트 27개 = 오류 레벨만·사용자 지시로 부담 관리). 진단 = 작가는 **코멘트 단 자리만 고치고 가이드 표는 전수 미적용**(연꽃 52→1 vs 사제 17→15) → 앞으로 앵커 필수. 기획안 = `Vigloo AI Drama Proposal_I Chose a Slave, But He Parts the Sea.docx`(05_구버전) · 원안 = `_p0_source.md` · 이력 = `16_moses_00_meta.md` · 폴더 지도 = `README.md`. ⚠️ 회수본 docx는 변경 이력 수락 후 읽을 것([[docx-conversion-drops-table-textbox-text]] 2차 실증). 잔여 = 사용자 확인 후 작가 발송 · 22화 이후 발주 시점 미정 |

| `17_son_of_the_lamp` | 《거지 알라딘과 요술램프》 Beggar Aladdin and the Almighty Lamp | **phase_p 제출본 v2 = v5 스파인 (2026-07-25)** — 히든 아이덴티티 메인·미국/글로벌 EN 발화·50화·무료 7·KR 전용. 스파인 = 《Bukan Pengawal Biasa》(최강자 위장 경호·보호 로맨스) + 《False Weakling, True Power》(손가락 마법·오인 쾌감) — 잠입 미션 축 제거(사용자). 코어 = 진의 왕 알라딘이 평범한 삶 찾아 공주의 하인으로 → 매회 '실수' 위장 몰래 구하기(물주전자 문법) → 공주의 정체 추적 = 로맨스. 램프 = 왕권·정령 봉인 신물(비비기 = 소환·닦는 척 = 부리는 중)·지니 카딤 = 귀환 압박→중매 변심 축·디즈니 제로. 제출본 = `Vigloo AI Drama Proposal_Beggar Aladdin and the Almighty Lamp.docx`·스펙 = `_p1_proposal_spec.txt`·캐논 = `_p0_source.md` §0·이력 = meta. 게이트 통과(킬러 대사 11종·中文 0·구버전 축 잔재 0). 잔여 = 사용자 검토·TBD(담당자·제작비·납품·릴리즈·샘플) |

| `_X_19_archmage_executed` | (폐기) MY KILLER CALLS ME SON | 🚫 **2026-07-31 사용자 전량 폐기** — 러프 v1~v9까지 9회 재작업 후 "구조가 쾌감을 못 일으키는 구조" 판정. 폐기 사유 누적(반복 금지): 짐꾼·잡역·빗자루 밑바닥 = 고구마 / 그를 조사하는 눈이 화면 채우면 미스터리 질감 / 1화 프롤로그 몽타주·상대가 세계(제도·균열) = 숏폼 아님 / 서류(각서·도면·조서·서명) = 소송극 / 8화 내내 공간·날짜·대립 상대가 매 화 바뀌면 돌아오는 핵심 쾌감이 없음 / 사용자 크래프트 감각을 공간 기능 원장·클리프 형태표로 법칙화 = 개소리. 기각 외부안 = 아르덴 모방 학파·사막 아티팩트 배후 미스터리·정체 윙크 대사. 이력 = `_X_19_archmage_executed/` |

| `20_three_queens` | THE HIDDEN ARCHMAGE'S THREE QUEENS / 숨겨진 대마법사와 세 여왕 | **phase_p 제출본 v1 (2026-07-30)** — 남성향 Hidden Identity + 배신자 정산 + 하렘·중세 판타지·글로벌 EN 발화·TBD(제안 50화 내외·무료 1~8)·오리지널·中文 생략. **모드 = 원안 골격 유지 + 원작 Stardust 《The Billionaire Swordsmith Fiance Returns》(55화·보유본=한국어 로컬라이징판) 살 이식**(사용자 판정 — 원형 충돌 기각). 캐스팅 = 에이든/비비안/루카스/드레이븐 + 세 여왕 **이벨린(제국 여제·검신) · 엘레나(엘프 여왕) · 프레이야(드래곤 퀸)** — 원안 '상단주'는 권력 종류가 돈이라 급이 안 서서 교체, 셋 다 초월 규격(벤다/존재로 굴복시킨다/시간으로 이긴다). **결말 = 하렘 해피엔딩(승자 1인 수렴 폐기·사용자)** — 3년 전 은인 반전은 승자 결정이 아니라 아내의 마지막 거짓말 파괴용. 3화 불륜 = 작품 최고 수위(사용자 지시·원작 실물 전량 이식). 공간 총량 4곳(즉위식장→대연회장→본탑→정문 광장). 제출본 = `Vigloo AI Drama Proposal_THE HIDDEN ARCHMAGE'S THREE QUEENS.docx` · spec = `_p1_proposal_spec.txt` · 캐논 = `_p0_source.md` · 러프+살 이식 맵 = `_p0_rough.md` · 이력 = `20_three_queens_00_meta.md`. 기계 게이트 7종 전량 통과(킬러 대사 24종 누락 0·클리프 8·컨테이너 PASS). 잔여 = 사용자 검토·TBD(회차·제작비·일정) |

| `21_black_hong_gildong` | 《흑길동》 / BLACK GILDONG | **러프 기획안 v10 (2026-08-03 · 트리트먼트 구조 재설계)** — **🚨 v9 트리트먼트 = 사건 8개·8일·화당 공간 3곳 = 일일극 골격이라 전면 재배열(§C-6 3질문 실측: 화 경계 7개 중 6개가 직전 훅을 안 이어받음).** v10 = **무료 8화 = 사건 1개(「첫 사냥이 자기 집으로 돌아오는 하루 반」) + 컨테이너 3개** — 관아 첫밤(1~3) / 홍판서 댁 그 낮(4~6) / 홍판서 댁 그 밤(7~8). 매 화 오프닝 = 끊긴 그 자리 그 순간·경과 서술 0. **50화 사건 지도 = 5개**(무료 1 + 아버지의 밤 9~20 + 대낮 관아 21~32 + 대전과 명부 33~44 + 삼백 년 45~50) · 공간 4곳이 각각 12~18화를 먹고 재방문이 회수. 근거 = 메모리 [[hit-script-event-count-measured]] 히트작 실측(50화물 = 사건 2~5개). **페이월 교체: 대전 "잘 왔다, 홍판서의 아들" → 유료 이월. 8화 = 자기 집 털고 돌아서니 아버지가 마당에 서 있고 "…네 어미가 종이다"(낮에 얼자에게 한 말을 밤에 두목에게 = 알아봤다) → 눈이 붉어지고 열아홉 해 만에 처음 아들 얼굴에 초점이 맞는다 "어디 보자, 내 아들."** "고개 들어라"도 유료 이월(무료 3화에 축소판 = 갓 씌워 내보내기·포졸 갓 벗기기). 채령 첫 조우 = 8화(은수저 자루를 값으로 안겨줌). 이하 v9 계승 — 한국 남성향 20-40·**히든 아이덴티티 메인 + 권선징악 + 액션 활극 + 코미디**·KR 발화·50화 내외·무료 8(제안)·홍길동전 각색·AI 실사. **🚨 시장 = KR 타깃으로 만들어서 글로벌에 판다 (2026-08-03 사용자 2회 교정). 순서를 뒤집지 말 것 — 글로벌에 맞춰 깎는 게 아니다.** 집필·연출·수위·말맛 = 100% KR 기준("외국 사람이 알아들을까"로 대사 한 줄도 안 바꾼다 — 깎으면 KR에서 먼저 죽고 팔 물건이 없어진다) · 판매 = 본편 무손질 + 자막만. 킹덤·기생충·오징어게임·파묘 전부 이 순서였다. KR 근거 = 홍길동 전 국민 인지·얼자/호부호형 설명 0·밈 출처를 타깃이 이미 앎·사극체↔쌍욕 낙차. **글로벌이 유난히 쉬운 이유(노려서 고른 게 아니라 결과적으로 겹침) = 심장의 관용구 둘이 영어권에 그대로 있다 — ① 은수저 = born with a silver spoon(특권층으로 태어난 그 은수저를 얼자가 녹여 총알로 쏨) ② 고혈을 빤다 = bloodsucker.** + 마른것이 갓 앞에 고개 숙임 = 자막조차 불요 · 마늘/은/햇빛 = 서양 룰 그대로 · 홍길동 = 조선의 로빈 후드 · 얼자 = Bastard Son · 갓 = 킹덤이 만든 글로벌 아이콘. **§10-2 표 = 판매·로컬라이징용, 집필 시 펴놓지 말 것.** **레퍼런스 지도 = §11** — 직접(홍길동전·킹덤·블레이드·시너스 2025) / 톤(**전우치**=톤의 정답·조선명탐정·장고) / 구조(귀멸의 칼날·각시탈·링컨뱀파이어헌터) / **반면교사 = 〈조선구마사〉 2회 폐지 = 실존 왕·실존 역사 건드려서 죽음 → 우리 안전장치 = 실존 인물/사건 0·가상 고을·가상 임금·연대 미표기(원전 홍길동전부터 허구)**. 대표 말맛 = **격식이 벗겨지는 3단계**(평소 "네 이놈, 어느 안전이라고" → 은수저 보면 "자, 잠깐. 그거 어디서 났어" → 죽기 직전 "씨발 잠깐만 내 말 좀—" → 재) · 역으로 **길동만 끝까지 격식**(종이 양반보다 예법 발라서 대비가 개그). **출처 = 인터넷 밈 〈흑길동〉(2019~·블레이드 리터칭) — 밈의 알맹이 = "탐관오리가 백성의 고혈을 빤다"는 관용구가 비유가 아니라 사실.** 톤 = 전원 진지·아무도 안 웃음(웃음 대상 = 관용구의 문자화). 세계 규칙 7 = 벼슬아치가 진짜로 빤다 / **한 번에 다 빨면 죽으니 조금씩 여러 번 → 말라붙어 일어난 게 '마른것'(좀비)** / **마른것은 갓 쓴 자를 못 문다**(죽어서도 예법 — 그래서 관아가 백성 통제용으로 마당에 푼다) / 은 = 양반집 수저·제기에만 있음 / 반가 밥상에 마늘 없음(백김치만) / 조정 = 야간 조회 관례 / 길동 = 반쪽이라 대낮에도 다니고 그를 문 것은 입이 탄다(**본인은 마늘 덕인 줄 안다 = 정보 비대칭 전부**). 핵심 쾌감 = **낮에 이마 땅에 대고 절한 상대의 목을 그날 밤에 벤다**(형태 고정·상대만 교체: 사또→형→포도대장→아버지→좌의정→임금). 최대 사이다 = 7화 갓 벗어 던지고 **"고개 들어라"** → 마른것 수십이 일제히 고개 듦. 히로인 = **윤채령 18**(좌의정 딸·형의 정혼자·유일한 인간 = 그것들은 서로 못 빨아 사람 신부가 필요 → 시집이 아니라 혼례상에 오르는 것·낮엔 길동을 부리고 밤엔 흑길동에게 "나를 납치해 주십시오") + 서브 **월향 23**(관기·목에 흉터 여럿·정체를 아는 유일한 사람·1화 첫 컷). 무기 사다리 = 은수저 자루→녹인 총알→은기고 통째→제기 녹인 은도→관고 은괴. 공간 4곳(홍판서 댁·관아·아지트·대전). 페이월 = 대낮인데 대전 창문 전부 닫힘 + "잘 왔다, 홍판서의 아들" + 대신들 눈 전부 붉음. **취급 규칙 = 멸시는 신분 용어로만·피부색 작중 언급 0·피부를 위장 장치로 쓰면 v1 폐기 사유(blackface 거울상) 재발·완력 중심 brute 몰이 금지.** 산출 = `_p0_rough.md`(v9) + `_p2_character_design.md`(캐릭터 디자인·키 비주얼 4종·이미지 프롬프트). 잔여 = 사용자 채택 판정 → phase_p · 기존작 대조(2022 웹툰 《은탄》·2025 AI 뮤비 《미스터홍》) |
| `22_the_crown_is_mine` | 《왕관은 내 것이다》 / THE CROWN IS MINE | **러프 기획안 v4 (2026-07-31)** — 글로벌 여성향·복수/권선징악 메인·**중세 판타지**·EN 발화·50화 내외·무료 8(제안). **원안 엔진 = `C:\Users\Rowan\Downloads\Bankrupt My Cheating Husband.역대본.md`**(내 남편의 여자가 내 것에서 나를 쫓아낸다 / 내 돈으로 산 목걸이를 그 여자가 걸고 있다 / 준 걸 회수해 알거지로) **× 용 여주·중세 왕국으로 세계 치환**(사용자: 시대·세계 바꿔도 됨). 세계 규칙 1 = 용의 보물은 주인을 안다, 부르면 돌아온다 → "파산시킨다"가 문자 그대로 실행. **핵심 쾌감 = 손을 들면 그녀 것이 돌아온다 · 형태 동일 · 규모만 확대**(목걸이→반지들→금실→쇠사슬→성문 금박→왕관). 무료 8화 = 통행세 못 내는 여자가 왕비 목의 심장석을 불러들임→도둑으로 끌려감→남편이 알아보고 "미친 여자다, 지하에 처넣어라"→창살 사이로 왕의 반지 회수→화형대 쇠사슬이 녹아 발밑으로→연회장 반지·금실 이탈→이졸데 맨목→성문 금박이 강처럼 흐르고 왕관이 떠올라 "이것부터 내 거였어". 이하 폐기 — — **소재 = 딸의 심장이 딸을 죽인 아이 가슴에서 뛴다.** 세계 규칙 2 = ①심장은 기억을 가져간다(카일리가 밤마다 린다의 마지막 밤을 린다 눈으로 다시 삶·깨면 잊고 몸만 기억 — 잠긴 문·계단·엄마 목소리) ②그 심장이 멈추면 린다가 두 번 죽는다(죽일 수 없어서 살려두고 부순다 = 50화 엔진). 무료 8화 = 폰 엎어놓음→추락+카일리 발작→같은 밤 같은 병원·못 알아봄(손등 붉은 점)→뇌사·이식 서명 **후에** 폰 켬(부재중 47통)→회복실 유리 너머 딸의 심장→장례식장에서 카일리가 "엄마, 살려줘"→몸만 기억하는 증상→"이제 네가 내 딸이야" + 가슴에 손. **v2 폐기 사유 = 원안 타이밍만 재배치·소재 0 (사용자: 창의성·독특한 소재감·세계관 없음).** 이하 — — 글로벌 여성향·**복수/권선징악 메인** + 모성 후회·EN 발화·50화 내외·무료 8(제안). **원안 = `C:\Users\Rowan\Downloads\Mom, Save Me.역대본.md`(49화) 골격 계승·무료런만 재배치.** 핵심 쾌감 = **엄마가 딸에게 안 해준 것을 딸을 죽인 아이에게 해준다**(전부 함정 — "왜 카일리처럼 못 하니"가 뒤집힘). 정보 비대칭 = 1화부터 시청자만 양쪽(잠긴 방의 딸 / 폰 엎어놓는 엄마). **원안 대비 재배치: 추락 9화→3화·사망 20화 장례→6화 사망·8화 복수 착수**(무료런 전부 피해자 서사면 결제 안 걸림). 4대 비트 = 병원 복도에서 딸 못 알아봄(손등 붉은 점) / 부재중 47통 전부 자기 번호 + "엄마, 살려줘" 음성 / 장례식장에서 카일리 손 잡고 "이제 네가 내 딸이야" / 문상객의 "저런 나약한 딸을". **v1 KNEEL FOR HER 폐기.** 산출 = `22_i_didnt_answer_p0_rough.md`. 잔여 = 사용자 채택 판정 → phase_p |

| `23_i_wear_what_i_kill` | 《내가 죽인 것을 입는다》 / I WEAR WHAT I KILL | **러프 기획안 v1 (2026-08-03)** — 남성향 20-40·**초고대 토템 판타지 + 신분역전 복수 + 액션 + 섹슈얼(초고수위)**·오리지널·50화 내외·무료 8(제안)·AIGC 실사 9:16. 시장 미확정(글로벌 EN 기본값 / KR 전환 가능). 소재 = 사용자 제시(다람쥐 부족 캐릭터 시트 이미지) = **토테미즘 문자화** — 우가우가 선사시대·거죽옷·괴물/공룡 허용·현실 정합 불요. **세계 규칙 = 네가 쓴 가죽이 네 힘이다 / 남의 짐승 쓰면 살이 썩는다 / 다람쥐 가죽엔 아무것도 안 나온다 / 빈 가죽은 아무거나 담는다(주인공만 예외 — 1화 첫 컷 시청자 선공개·부족들은 끝까지 모름 = dramatic irony) / 가죽이 오면 짐승도 온다(섹슈얼 명분 내장).** 핵심 쾌감 = **낮에 나를 밟은 놈의 가죽이 그날 밤 내 어깨에 걸린다** — 형태 고정·상대만 교체·실루엣이 매회 부풀어 강함을 설명 안 해도 보임(늑대→곰→검치호→매머드→하늘). 인물 = 카르그(주) / 바르가(곰 부족장) / 치키(다람쥐 부족장·딸랑이·유일 웃음담당, 주인공은 끝까지 안 웃음) / 모르(무녀). **히로인 3 = 네이라(배신녀·곰 무릎으로 걸어감·무료런 내내 그를 못 알아봄) / 루아(토끼 부족·완전 공략→몸도 마음도 복종→제 부족 굴길을 팔아먹음 = 7화 잠입 수단) / 사르카(검치호 여전사·유료).** ⚠️ **관계 축 금지 — 하렘물 아님**(축은 "죽여서 입는다" 하나·여자는 사다리 한 칸의 결과물). 수위 = 초고수위/고수위·밀도 절제(무료런 1회 = 5화). 공간 4곳(대집회 골짜기·사냥터·다람쥐 야영지·곰 야영지). 무료 마지막 8화 끝 = 곰 가죽 착용·곰 부족 전원 무릎·네이라 이마 → 해를 가리는 날개 + 그 등에 탄 사람. 산출 = `23_i_wear_what_i_kill_p0_rough.md`. 잔여 = 사용자 채택 판정 → phase_p · 미확정(시장·회차·유료 사다리·"가죽의 대가" 채택 여부) |

새 작품 번호 = **24**.

> **현재본 단일 진실:** `07_final/[작품]_FINAL_v{최신N}.md`. 메타·CLAUDE.md 모순 시 → 파일 시스템 우선·메타 즉시 갱신. CLAUDE.md 작품 행 = 현재 상태 + 포인터만(이력 누적 금지).

> **메모리 위치:** workspace 안에 `memory/` 폴더 없음. 실제 = `C:/Users/Rowan/.claude/projects/C--Users-Rowan-scenario-automation/memory/`.

---

## 룰

1. **묻지 말고 자율 진행.** 비가역(캐논 변경·작품 이름 변경·대량 삭제·Hard Lock 변경)만 사전 확인.
2. **검증 보고서·테이블·자가 검수 풀이 = 본문 외 작성 금지.** 메타 분량 = 본문 톤 침투의 근본 원인. 보고 = 경로 + 한 줄.
3. **집필 컨텍스트 = raw drama prose 우선.** 집필 진입 시 매칭 히트작 3-5 EP + 직전 배치 raw 정독 강제.
4. **EP 본문 = 영어 100% (한국어 0건).**
5. **한국어 출력 시 AI jargon·작업어·어색한 조어 절대 금지** (전 작업 — 대본·메모·로그·대화). 친구 카카오톡 톤 우선.
6. **사용자 질문 시 PushNotification** (200자 이내·결정/입력값/블로커).

## 모델·세션

**파이프라인 = 세션 모델 무관 자급 (2026-07-06 사용자 재정의): opus/sonnet/haiku만으로 완결 — Fable 상시 불요, 구조·룰·워크플로우 개정 때만 1회성 투입.** 메인 = 쇼러너(모델 무관): 오케스트레이션·역할/모델 분배·최종 판정 — 판정 = `config/20_review_standard.md` §4 머지 기준 + §4-1 수술 파이프라인 체크리스트(감 금지·절차 집행·체크리스트 밖 사유 = 문서 개정 안건). 프로스 실무 = 메인 직접 수행 금지(생산자/판정자 분리 — 메인이 opus여도 별도 opus agent에 지시서 위임·논문병 가드레일 의무). 실무 분담(§7 3-tier — 업무 성격이 티어를 정한다): **단독 정밀 발견/하드블록·집필/수술 = opus** / 반복 수렴·중난도 추출·정합 대조 = **sonnet** / 기계+naive-proxy(뇌오프·flat-TTS·무맥락 이미지생성기 — *덜 이해해야 정확*) = **haiku**. Agent 호출 시 `model` 명시. 생성기 프록시(`aigc-draw-auditor`·`tts-literal-ear`) 상설. 세션 시작 시 모델 확인 — Fable인데 구조·룰 개정 작업이 아니면 "opus로 충분"을 사용자에게 고지. **단, 세션 모델이 Fable이면 (사용자가 이미 비용을 선택한 것) subagent 배분에 fable 티어를 포함해 메인이 자율 배분** — 단독 정밀 발견·최상급 프로스 집필/수술 = fable 승격 후보, 나머지는 §7 티어맵 유지, agent frontmatter 핀은 호출 `model:`로 override (2026-07-22). 본문 영어·대화 한국어.
