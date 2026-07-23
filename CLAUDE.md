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
| 검수·집필지원·수술 agent 13종 정의 | `~/.claude/agents/` (전원 frontmatter `model:` 핀 = opus 이하 — 운용 룰 = `config/20_review_standard.md` §7 3-tier 모델맵·직교 sweep·집필지원 W1-W3 = `10_writing_standard.md` §A-1. 수술 3종 = `script-surgeon`·`consistency-sweeper`·`copy-candidate-generator`) |
| 기계 도구 | `tools/voice_lint.py` · `tools/continuity_lint.py` · `tools/format_pass_verify.py` · `tools/pacing_lint.py`(공간 경제·절단 구조 6검사) · `tools/register_census.py`(인물별 레지스터/코치봇 — 둘 다 2026-07-10 신설) · `tools/esl_hardwords.py`(대사 어휘 Zipf 직관 스캔 — 2026-07-15 신설·localization 워크스페이스 포팅) |
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
| **플랫폼 기획안 (phase_p)** | `prompts/phase_p_platform_proposal.md` — **0단계 설계 확정 문답(fan-out 전)** → 대원칙 8종(원안=정본 verbatim·로그라인 5요소·갈등축 발명 금지·§C-4-2/§C-2-2 게이트·룰 정합·dramatic irony·내용요건=놓치기 쉬운 것만·사람 말 문체) → 기계 게이트 6종 → 빌더 `tools/build_vigloo_proposal.py` (2026-07-16 제정 · 실증 = My Million-Dollar Reset·While My Wife's Away) | 0단계 문답 = 메인↔사용자 / **안목(로그라인·내용요건 + 머지 후 문체 콜드리드) = fable 1기 고정** / 훅·아크 = opus / 트리트먼트 = sonnet(보강 0 기본값) / 시놉·캐릭터 = sonnet / 메타 = haiku → 머지·게이트·docx = 메인. **Fable = 안목 유닛만 — 벌크 프로즈 배정 금지 (2026-07-22 2차 정밀화·근거 = 절차문 분업 §)** |
| 한국어 정본 검토 | 메모리 [[external-korean-script-review-belt]] (한국어 벤치마크 필수·voice_lint 무효→grep 대체) | opus + sonnet belt |
| 산출 라운드 (타이틀·광고카피·셀링포인트) | 후보 = 다시각 독립 N기 병렬 → 메인 선별(§4-1 머지 체크리스트 준용) → 사용자 확정 | 생성 = copy-candidate-generator(opus) / 추출 = mkt-selling-point-extractor(sonnet) |
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

| `14_while_my_wifes_away` | While My Wife's Away | **phase_p 제출본 v1 (2026-07-22)** — 남성향 금기(장모×사위) 최고수위·50화·무료 8·오리지널. 제출본 = `Vigloo AI Drama Proposal_WHILE MY WIFE'S AWAY.docx`·원안 정본 = `_p0_source.md`·이력 = `14_while_my_wifes_away_00_meta.md`. 주체 설계 = 정복 이든/심리 빅토리아([[male-conquest-female-psyche-dual-subject]]). 잔여 = 사용자 검토·TBD 필드(레퍼런스·일정·샘플 범위) 확정 |

| `15_reign_predators_office` | 군림: 포식자의 오피스 / REIGN: THE PREDATOR'S OFFICE | **phase_p 제출본 v1 (2026-07-22)** — 남성향 오피스 신분역전·섹슈얼·KR 발화·KR 20-40 남성·총 50화 내외(TBD)·무료 8·오리지널·中文 생략·레퍼런스 SarosTV <신생>. 제출본 = `Vigloo AI Drama Proposal_REIGN - THE PREDATOR'S OFFICE.docx`·원안 정본 = `_p0_source.md`·이력 = `15_reign_predators_office_00_meta.md`. 엔진 = 무요구 군림(여자들이 스스로 바침)·무료 8화 = 세아 단일 축·채은/최도혁 = 유료 카드. 잔여 = 사용자 검토·TBD 필드(총 회차·일정·제작비)·EN 타이틀 표기 확정 |

새 작품 번호 = **16**.

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
