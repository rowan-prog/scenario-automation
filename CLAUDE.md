# 시나리오 자동화

AIGC 숏폼 vertical drama 시나리오 제작. 최종 산출 = `projects/[작품]/07_final/[작품]_FINAL_v{N}.md`.

---

## 어디서 무엇 찾는지 (이 파일은 인덱스만)

| 필요 | 위치 |
|---|---|
| Hard rule 12개 | `config/hard_rules.md` (1페이지·매 phase 진입 시 정독) |
| Phase별 prompt | `prompts/phase_*.md` (단계 진입 시) |
| 작품 진행 메타 | `projects/[작품]/[작품]_00_meta.md` |
| 검증 히트작 raw 대본 | `config/vertical_drama_hit_scripts/` (집필 시 매칭 작품 3-5 EP raw 강제 정독) |
| 히트작 분석 | `config/vertical_drama_hit_scripts_analysis/` |
| 페르소나 | `config/personas/` (검토 시점만) |
| 평가위원 | `config/evaluators.md` (피칭 시점만) |
| 타깃 자료 | `config/target_research/[성별]_target_research.md` |
| 비주얼 락 템플릿 | `config/visual_lock_template.md` |
| Reference 인덱스 | `config/reference_scripts/INDEX.md` |
| 시스템 baseline 메모리 | `memory/` (always-load 3개만·MEMORY.md 참조) |
| 상태·정합성 도구 | `prompts/status.md` · `prompts/audit.md` |

> **master_guide_v3.md (5816줄) = 시스템 백과·집필 컨텍스트 진입 금지.** Hard rule 12개는 `config/hard_rules.md`에 추출됨.

---

## 워크플로우

```
phase_0 (아이디어) → phase_1 (러프 청사진) → phase_2 (피칭) → 피칭 결과
  → phase_3 (완성 청사진 + visual lock) → phase_4 (Conversion Runway 집필)
  → phase_5 (페르소나 검토) → phase_6 (패치) → phase_7 (최종고)

부가 트랙: phase_a (각색) / phase_b (외부 대본) / phase_c (외부 피드백)
```

---

## 작품 파일 명명 규칙 (필수)

`projects/[NN]_[slug]/[NN]_[slug]_[단계번호]_[단계명].md`
- 폴더 prefix = 폴더명 동일
- 하위 폴더 (`05_episodes/`·`06_reviews/`·`07_final/`) 안 파일도 prefix 적용
- 폐기 폴더 = `_X_NN_slug` prefix (자동 차단)

---

## 현재 작품 (2026-05-21)

| 폴더 | 작품 | 현재본 (정본) | 단계 |
|---|---|---|---|
| `01_titan_born` | TITAN BORN | (07_final 확인 필요) | 완결 ✅ |
| `02_the_offering` | THE OFFERING: Claimed by the Dragon Lord | **🎬 `07_final/02_the_offering_FINAL_v68_dialogue_surgery.md`** (대사·VO surgery 적용) | **v68 dialogue surgery (2026-05-27·외부 2인 리뷰 반영)** — v65→v66→v67→v68. 5217 lines (v67 5232 → -15). **3 카테고리 처치:** ①법정 심문형 (`Say it/Tell them` 강요 자백) 제거 — EP08·09·14·25·30·32·37·41·42·43 / ②스카카토 핑퐁 (꽁트풍 단답 교환) 깸 — EP01·09·10·13·15·**18 (deathbed 최우선)**·23·28·46 / ③시적/연극적 VO 트림 — EP01·02·04·05·10·12·28. **핵심 paywall payoff 유지·롤프닝:** EP21 Sabine 처형 tri-colon 제거 + "My mother's blood is on your hands. So is mine." / EP46 reveal "I missed a stranger / let me feel insane" → "I was sick over a stranger and the stranger was you. While I thought I was losing my mind." / EP50 "Vael, break both hands." 펀치 유지. **논리 fix:** EP24 "No one had to" (이전 draft 잔재) 정리. **Verification:** Korean 0·EP 50/50·Hard Cut 50/50·sex scene 7건 보존·"Say it/that" 잔여 2 (왕명·통치 voice·OK). v65 매출 1위급 baseline 위에 외부 리뷰 2인 (대사·VO 전수검사) 반영. |
| `03_most_wanted_ship` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | (07_final 확인 필요) | phase_2 완료 |
| `_X_04_heiress_clause` | I AM THE HEIR | — | 폐기 |
| `06_she_stole_my_face` | SHE STOLE MY FACE | **🎬 `07_final/06_she_stole_my_face_FINAL_v38.md`** (v38.1 · 2026-06-01 · vertical 재분절 + 상업 cadence 보정·게이트 통과·docs 재동기화 폐기) | v30(외부 81점 진단·"버릴 게 아니라 90점 가능 소재가 81점 구조로 늘어짐")에서 **장르 엔진 재설계**. **엔진:** EP48까지 세상은 Mara를 Lena로 믿음·진실은 Lena+Noah만 앎·Lena는 증명 X 당함(꺾이지 않고 주체적·머리 쓰고 빌드업)·억울함 축적 → EP48-49 폭발. **악역=뻔뻔/저지능/천박(체스 X)·세상이 가짜 편이라 이김.** 5블록+피날레: B1(09-16 거짓말쟁이 낙인·자기 얼굴이 역증거) B2(17-24 엄마 도둑맞기) B3(25-32 가짜 신부+몸) B4(33-40 Mara 실제 결혼=최저점·EP37 truth-delay#2 계단 자해+카메라 사각 논리) B5(41-48 결혼식 전쟁·Mara 난입) EP49-50(폭발=Mara 자멸 X·Noah가 결핍 정확히 찔러 터뜨림+이름·남자·엄마 회수, 구원 X). truth-delay 2회(EP13·37). **제거:** admin/board/legal·prop-as-key(진실은 캐릭터 자멸로)·정확한 수치·영국식. **유지:** 의상/룩 비주얼 디테일·T2 4건(EP15·23·38·45). Verify: 50EP·HC49·한국어0·~93.8k(분량 70-80k 압축 잔여). 메모리 신규: [[vertical-revenge-impostor-believed-engine]](엔진+악역룰+소품룰+수치/NA룰+Lena주체성룰). 이전: v30 thriller→emotion reset(폐기). **v32 (2026-05-29·외부 종합 피드백):** v31 구조 위에 대사·VO만 수술(구조 재작성 X). ①토막 나열 제거(`My face. My home.`→한 문장) ②은유 제거(`wear like a costume`·`worn my life like a coat`) ③번역투→북미 실제 구어(`She married my life`→`She married Ethan in my name`) ④EP48 `She doesn't need X` 3연 펀치(연극톤) 제거 ⑤T2 반복 지문 분리(EP38·45) ⑥EP49 폭로=감정 먼저+압축 ⑦EP50 Hector 문 열어줌(`Welcome home, Ms. Sterling`)=사회적 회복 물리적으로. 신규 도구 `tools/voice_lint.py`(문학톤 기계 탐지·LLM 0). Verify: ANAPHORA 14→7(잔여=Mara TV연기 등 정상)·METAPHOR 18→1(literal)·한국어0·HC49·50EP·~93.8k. **v33 (2026-05-29·외부 line-level 리스트 전수·무료부 포함 ~50 라인):** ①숫자 흐림(40분·16분·2cm·200명·half a second→soon·not long·under her ear·ballroom full) ②번역투 직역 제거(`She married my life`→`married Ethan in my name`·`wears my name to sleep`→`sleeps in my bed and answers to my name`) ③빌런 더 천박(Eileen `Take her name. Take the house. Take the man.`·Victoria `had plastic surgery...sniffing around`·Mara `I have your face. They eat it up.`) ④후크 8개 직관화(`A WHOLE WORLD CALLS ME CRAZY`→`THEY ALL CALL ME CRAZY. NOAH DOESN'T.`) ⑤Noah 무뚝뚝(EP47 `Let them talk. I know who I'm marrying.`) ⑥EP48 cool-quip 제거(`You aren't invited. Get out.`) ⑦EP49 폭로 압축+`plastic surgery scar` 명시. Verify: 91.8k(-2k)·한국어0·HC49·50EP·ANAPHORA 잔여 7=전부 정상(무료부 blunt·빌런 sanctioned 명령조·Mara TV연기·패닉). **v34 (2026-05-29·외부 90.5점 검토·production-lock 직전):** 🚨핵심=**EP06 Mrs. Halloran "Lena 알아봄"→"거의 알아볼 뻔하다 더 잔인하게 부정"**(`Don't use her voice`·`I knew Lena. You're not her. Get help.`)로 반전 → "Lena+Noah만 안다" 엔진 락 복구(불합격 사유 해소). + 3인칭 자기지칭 오류(EP37 `Lena grew up`→`I grew up`·EP03 Mara가 진짜 Lena를 "Mara"로) / 논리구멍(EP26 `you gave all this up`→`I'm in here living your life`·EP30 Lena 함정 알고 내림→"심은 기자 확인하려다 더 빨리 잡힘") / 빌런 천박(EP17·21·28) / 작전 한 줄 보강(EP07·08 `Get the scar`) / EP29 찢긴 가운→EP31 backup gown 한 줄 / EP15 `Mine. The real one.`→`Say my name/Lena/Again` / 숫자 추가 흐림. **보류:** EP18 작은 회수(편지 복사본)=소품룰 충돌로 미적용. Verify: 91.1k·한국어0·HC49·50EP·truth 11→1·real 22→18. 잔여 P1: nobody/everyone/life 카운트 높으나 *전제 핵심어*(아무도 안 믿음/내 인생/진짜 Lena)라 load-bearing·기계 감축 X. **🔒 LOCK 확정 (2026-05-29):** 후크/VO 추상어 감축 1패스(반복 `MY LIFE` 후크 5→1·`life`22→18·`world`9→8·대사 본문은 유지) 후 production-lock. 사용자 최종 기준 락: **쉬운 도파민 > 논리·개연성 보강은 한 줄/한 행동·어려워지면 실패** → 신규 메모리 [[easy-dopamine-over-logic]]. 검토 5라운드(v30진단→v31재집필→v32구어→v33line-level→v34엔진락+lock). **+정합성 전수감사 fix (2026-05-29):** ①도어맨 Frank(EP04)↔Hector(EP09/50)→Hector 통일 ②EP48 자백(`it was supposed to be MINE`)↔EP49 회상 인용 정합 ③EP49 `first time Mara said out loud`(EP03 `best friend, Mara`와 충돌)+Ethan 조기 호명 제거→이름은 Lena 폭로(S#2)가 소스·EP03 "Mara"는 부메랑으로 잔존 ④EP04 엄마 웨딩드레스 회수(Lena가 들고 나옴→EP46 그 드레스로 결혼 명시) ⑤Noah `two years`=테이블 명료화·EP08 `Two hundred faces`→`Every face`. 보류: C-2 아파트 통제 브리지(설명 추가 회피)·D-2/3(작동). **+native-ear pass + 재감사 (2026-05-29):** 어색/번역투 10 라인 정리(`Off of me`→`A surgeon cut hers to match mine`·`I am the small things`→`I lived them`·`made me insane with them`→`make me look insane`·`took my name off the invitation`→`put my name on her invitation`·`carved your face`→`had surgery`·`about to look at her`→`turn on her`·`hear her face`→`hear her voice crack`·`get happy`→`be happy` 등). 재감사: 신규 정합성/논리/연속성 오류 0·엔진 유지. borderline 1: EP09 tenant `cut her own face`=의도적 mob 막말 유지. 91.3k·한국어0·HC49·50EP. **🔬 fresh-eyes 전수검사 (2026-05-29·8 독립검수자 병렬 Workflow):** 자가검수가 두 번 "클린" 한 본문에서 HIGH 3건 발견 → ①EP06 Tessa 자백이 EP01 클리닉·EP05 "old code"와 모순(내 수정이 만든 것) → Tessa가 "스케줄 비워주고 혼자 가게 함"으로 ②펜던트 회수 컷 누락 → EP50 INSERT 추가 ③`Not while I'm breathing` 3연속 틱 제거. MED~13(EP04 작가해설 지문 제거·`charity case`·`my bridal shower` 명확화·Noah epigram 다듬기 등)·LOW~15. 의도된 것 보존(EP16 흉터=엔진·EP13 도너·EP24 LUMEN MEUM·Eileen 명령조). 신규 메모리 [[fresh-eyes-full-inspection-method]]: LOCK 전 fresh-context 외부 패스 필수·self "clean" 단독 신뢰 X. Verify 90.7k·한국어0·HC49·50EP. **v35 (2026-05-30·사용자 락 해제·외부+내부 평가 반영):** 외부 fresh 2인(구조/native English)+내부(캐논·엔진·하드룰·easy-dopamine) 평가. 헤드라인 결론=**"시청자도 몰랐던 사실 갑툭튀" 안티패턴 0건**(엔진=극적 아이러니·EP01 전모 공개·truth-delay 2회는 세상이 따라잡는 지연). 실질 약점=중반 EP17-32 "잠입→모친/이름 주장→축출" 평평한 반복. 수술(화수 50 유지=캐논 Hard Lock·페이월): ①중반 공개-패배에 *기능 차별화 + Lena 작은 승점 사다리*(반복→축적·Lena 주체성룰)=EP17 기자 첫 의심+"comfortable people get sloppy" 복선·EP18 Marlow 체스로 첫 doubt+"구걸 그만, 가짜가 스스로 드러내게"(3rd-rejection 중복 제거·EP37 복선)·EP20 Mara 할머니이름 공개 오답(가짜 첫 공개 실수·EP36 회수 출처)·EP25 "진짜 중요한 건 못 찾는다"(EP46 복선)·EP27 한 명은 등 안 돌림(사적 동조 씨앗) ②Tessa 자백 EP01 정합(스케줄 정보만 넘김·기존 patch 미완 해소) ③LUMEN MEUM 정답 EP14 선공개→EP19/24 극적아이러니화 ④Noah 대구/잠언 2곳 평구어화(하드룰11)·EP04 평행구문 해체·months↔two years 통일·EP30 과한 작전동기 단순화·EP40 "for good"·altar→aisle(폐기어휘). Verify: 50EP·HC49·한국어0·폐기어휘0·영국식0·행정/법0·altar0·~16.7k words. 신규 grandmother 토큰(Rose 정답/Catherine 오답)=EP36 dangling 참조 해소. **→ 사용자 50화 유지 확정 (2026-05-30):** 길이↓·화수↑(~63-68, 유료 vertical hook/페이월 빈도=매출) 검토했으나 50 유지 선택. **v36 (2026-05-30·"사건 없는 씬=vertical 죄악" 패스):** 무드/세팅/대사만 있고 사건 없는 씬 제거. ①EP21 Mara 수동 공허 독백(EP31과 중복)→**엄마를 결혼식 테마로 강탈하는 능동 계획**(EP22 모친상실 비통·EP24 회수·EP36 sloppy 연결) ②EP44 seating-chart 순수 감상(빈 신부측은 EP46에 이미 존재)→**Mara가 Lena를 직접 찾아옴 + Lena가 "와서 망쳐봐" 미끼**(EP05 침입의 거울·Lena 주체성=의도적 미끼·EP47 검은옷/카메라 예언·EP48 "Noah가 올 줄 알았다" 복선). T2 intimacy 4건(EP15·23·38·45)=정서 payoff+분산이라 의도적 유지·EP31=유일 공허비트로 유지·EP10S3/EP35/EP41=정서/기능 있어 유지. **+톤 보정 (v36 내):** 내 v35/v36 수정이 '영리한 단서·체스·수사 서스펜스'로 드리프트(=흥미진진 미스터리) → 사용자 막장 톤 지시 반영. EP18 체스 장면→케이크 멍청이극(노인이 진짜 제자 대신 케이크 가져온 가짜 택함), EP17/20 수사·증거-쌓기 결 제거(빌런=뻔뻔/멍청·군중=더 멍청), EP44 Lena 미끼=영리한 전략 X→"쟨 질투나고 멍청해서 못 참아". 엔진 메모리 톤 섹션 보강. Verify: 50EP·HC49·한국어0·altar0·chess0·~16.8k words. **🔒 LOCK 확정 (2026-05-30):** 락 직전 fresh-eyes 외부 오류·정합성 전수감사([[fresh-eyes-full-inspection-method]] 룰) → 치명 구멍 0(흉터·펜던트·드레스·할머니이름 Rose정답/Catherine오답·Tessa↔EP01·LUMEN EP14→19→24·신부측 셋업/회수·[GRAPHIC] 훅번호 전부 정합). HIGH 1건 수정: EP43 훅 인과 역전(미끼 던지기 전 'she'll come, I knew it' 예언=EP44 능동화 충돌+유일 미스터리톤 잔재)→'못 막으면 안 막고 부른다' 결심톤 교체. +absurd-funny 4비트(EP18 Marlow가 마트 케이크에 울며 'Helena 손맛'·EP19 Mara가 제 펜던트 라틴어도 못 읽음·EP32 하객이 Mara가 방금 지어낸 거짓말을 진지하게 사실로 받아들임·EP35 Mara가 제 거짓말 모순에 'she got over it'·EP48 자멸 복선). MED 보류(엔진 의도): EP37 Noah 증거 미사용=진실은 증거X 자멸로만·EP02 병원 사전브리핑 타이밍=막장 허용. Verify 재확인: 50EP·HC49·한국어0·altar0·chess0·'I knew it'0·~17.0k words. **+뇌-오프 트림(사용자 "뇌빼고 봐도 알겠냐" 점검):** 유일 brain-on 잔재였던 LUMEN MEUM "진짜 뜻 기억시키기"(라틴어+추상의미+'유래만 틀림' 3단 추론) 제거 → "가짜가 제 목에 건 것도 모른다"는 즉발 코미디로(EP14 "한 단어도 못 댄다"·EP19 "She just knows it's shiny"). 극적 아이러니 유지·추적 부담 0. v36 = 정본 LOCK. **v37 (2026-05-30·외부 페르소나 4인 패널→척추 재설계):** 미국 여성 paid-vertical 시청자 페르소나 4인(복수 헤비층·BookTok 로맨스·장르 회의주의자·전환게이트[EP1-8+13]) 병렬 검수→만장일치: ①중반 EP17-32 반복(v35 차별화=invisible micro-win이라 체감0) ②Lena가 46화 내내 *보이는* 승리 0=수동·답답 ③EP8 페이월이 패배로 끝나 결제훅 약함(전환게이트 6/10) ④결말 펀치를 Noah가 가져감. +엔진 메모리 자가경고("line검수 돌리고 #1 구조 놓침")를 또 반복했음을 패널이 적발. **사용자 결정: 락 재오픈 + 결말 펀치=Lena 직접.** 척추: EP06 Tessa가 Mara 결핍(가짜로 들킬 공포)을 무기로 넘김→EP08 Lena 능동선언("카메라 앞에서 가면 깬다"·주먹·훅 'I'LL BREAK IT ON ONE')→EP24 갈라서 Lena 도발로 Mara 카메라 앞 첫 공개 균열(snarl)=*보이는* 승점→EP48 **Lena가 직접** 결핍 찔러 자백 유도(Noah는 판만 깔고 물러섬·"sobbing girl on a rug"=EP06 회수)→EP49 씨앗 회수(EP17 기자가 EP24 snarl 클립 틂·EP27 진주 노부인 등장). +EP05 전제충돌(부하가 얼굴 못 가림=nightmare 명시)·EP06 중복 Halloran 컷. **필수 정합성=fresh-eyes 외부 전수**→HIGH 1건(EP49 기자 'cemetery footage' vs EP17 '촬영 안 함' 모순) 수정. Verify: 50EP·HC49·한국어0·altar0·chess0·Halloran0·~17.4k words. **+언어 게이트(뇌-오프·spoken English·문학톤·fresh native-ear 패스):** 재집필이 도로 넣은 은유 3건(EP24·48 coat/seams/costume·EP06 seams) 리터럴화·토막나열(EP48 'the face. the ring. the house.'→한 흐름)·의인화(EP43 'cruelty wears Lena's name')·잠언버튼(EP49 'first…not last') 제거 + EP48 결정타 독백 5단추론→직설 압축·EP04 식별 디테일 4→2(뇌-오프)·EP21/EP04 staccato 나열 콤마화. voice_lint 결과: METAPHOR 1(premise `wearing my face`)·ANAPHORA 6(전부 자연 구어/의도된 빌런 명령·TV연기) = v32 락 베이스라인(7/1) 이내. 뇌-오프·spoken English·문학톤 3축 PASS. v37 = 정본 LOCK. **v38 (2026-06-01·vertical 재분절 — TV식→vertical식):** 사용자 진단: v37이 '한 화=자기완결 사건+새 장소'=TV 미니시리즈 분절(공간 hopping·단발 세트 ~10). 재분절 규칙: **묶음 4-5화 또는 7-8화 = 한 상황 milk·1-2 공간·펜트하우스 home-base·화마다 안 끝나는 훅·단발 세트 컷.** 맵 `06_she_stole_my_face_04b_resegmentation_map.md`(v2). 9묶음 **4·4·5·8·7·7·5·5·5=50**. v37 튜닝 대사·엔진·voice 보존하며 re-cut(병렬 3 에이전트 재단→메인 조립+QC). 주요 이동: swap EP1→**EP1-2 분산**·첫 공개 균열 EP24→**EP18**(추모 갈라 EP17-19 milk)·결혼식 EP33-34 milk·컨서버토리 EP46-49 milk·EP1 6공간 과밀 해소. **컷:** Aunt Bea·Marlow·파우더룸. **보존:** T2 EP15·23·38·45·EP48 Lena 직접 결정타·EP50 Mara 구원 X. fresh-eyes 재분절 QC: 치명 0(삭제잔존0·중복0·봉합정상·훅50/50·흉터/펜던트/드레스/Hector 일관)·HIGH 1(EP36 tribute→morning show)·잔재(EP04 forty·EP37 swim) 수정. Verify: 50EP·HC49·END1·훅42·한국어0·은유0·forty0·~14.5k words. **v38.1 (2026-06-01·"돈 되는가" 빡센 상업 판단→중반 cadence 수술):** 전편 정독 후 판정=**전환(EP8 그랩+부당함 최대)·피날레(EP46-50 환수)는 상위권이나, 유료 중반(EP20-39)이 거의 끊김 없는 굴욕 + 모든 중간승리 즉시 회수로 인당 구매화수 누수**(장르 매출 핵심변수=전환유저 1인당 구매화수·EP25 이탈≈17화 vs EP50≈42화=2.5배). 수술=중반에 *회수 안 되는* 쾌감 이식(엔진/극적아이러니/대사/T2/훅 불변): ①EP19 갈라 snarl 클립이 묻히지 않고 상시 유지(기자 게시·수천뷰·비주류지만 안 내려감)=첫 회수불가 승점 + EP49 기자 payoff 강화 ②EP26 적진(브라이덜 샤워) 신봉자 1명 게이트서 공개 합류("네가 Lena인 거 안다") + Mara 공개 손실(빈 의자=Helena 오랜 친구 퇴장)=shape-break(끌려나감 6연발 중 1회는 *얻고* 나감) + EP49 진주 노부인 선두 합류로 동기화 ③EP36 Mara 멍청함이 처음 가시적 대가(Halcyon 보드 제외·친구 이탈·snarl 클립 잔존=제국 균열 B-meter)=멍청이 향연이 *벌받기* 시작 ④EP49 Ethan "진짜를 버리고 이걸 골랐다" 후회 비트 살림(grovel 없이 압축). 게이트: 50EP·HC49·END1·한국어0·훅42·은유0·forty0·~14.5k words. **보류(리스크 대비 효과 낮음): Noah 위로비트 반복 압축**=차기 패스. **docs 재동기화(핸드오프/청사진/비주얼락) = v38.2에서 사용자 지시로 최신 대본 기준 동기화 완료 + 전수 정합성 수정 (아래 v38.2 docs-sync 참조 · v38.1 당시 '불필요' 판단은 정정됨).** **+fresh-eyes 전수 정합성 감사(독립 컨텍스트·엔진 가드레일 부여):** CRITICAL 0·HIGH 1 = EP49 Ethan "since the gates"(Ethan은 gate 장면 없음=steps/street/arch만)→"in months" 교체 · 내가 심은 orphan "Halcyon board/spring host list" 제거→"the charity that wanted you headlining their spring gala"(뇌-오프 자명화) · 타임라인 2단 클럭 정합(EP16 결혼前인데 "months"→"weeks"·EP49 갈라클립 "weeks back"→"months back"). 흉터(좌측 귀밑·Mara만)/펜던트(LUMEN MEUM·EP01→EP50 회수)/Hector/이름/훅 인과/T2(15·23·38·45)/막장 자기모순(수영·할머니이름·라틴어) 전부 clean·의도된 것 보존. 게이트: 50EP·HC49·END1·한국어0·은유0·orphan0. **v38.2 (2026-06-01·Noah 위로비트 반복 압축 — v38.1 보류 '차기 패스' 집행):** Noah가 '판 바꾸는 남자'로 읽히게 순수 verbal 반복 안심 틱만 외과 처치 6곳. ①EP08 filler "I know" 컷→Lena가 스스로 차갑게 결심(주체성↑) ②EP10 only-two-know 비트 "I know"→**"Two of us, then."**(엔진 강화·연속 EP 틱 제거) ③EP28 certainty 라인 EP46 공개선언과 중복→"The city's wrong about you. I'm not." ④EP42 이중 안심("I'm still here. I'm not going anywhere.")→"I'm still here." ⑤EP46 같은 씬 중복 "I know what I saw." 컷 ⑥EP50 서약 recycled "I know who I'm marrying."→**"Best thing it ever cost me."**(서약 3연 echo 제거+그녀 vow에 직접 응답하는 신선 payoff). **보존:** 엔진 앵커 `"I'm Lena." / "I know."`·경비 차단 행동(EP24·38)·`"Cry. I've got you. ... I do."`·공개 선언(EP46)·T2(15·23·38·45)·marry me. voice_lint: ANAPHORA 7·METAPHOR 2(전부 기존 의도된 빌런 명령/TV연기/premise·신규 라인 3개 전부 literal 무탐지)=v32 락 베이스라인(7/1) 이내. 게이트: 50EP·HC49·END1·한국어0·은유0·bare "I know" 틱 해소(엔진 앵커 1 + 계단 목격 구체 1만 잔존). **+docs 동기화 (사용자 지시·v38.1 'docs 불필요·폐기' 기록 정정 · 2026-06-01):** 핸드오프(→v38.2)·비주얼락(v5→v5.1)·청사진(v3→v3.1)을 v38.2 최신 대본 기준 환류 + 대본 전수 대조 정합성 수정 4건 — ①비주얼락 Eileen EP 마커 정정(EP28 폰 누락분 추가·물리[EP02·36·39]/전화음성[EP20·28·30] 구분) ②비주얼락 Conservatory EP43-44→EP44·46-49(결정 EP42-43) ③비주얼락 Cross Manor에 EP28 추가 ④청사진 Tessa TV배신 EP12→EP11(실측 토크쇼=EP11). 회귀단역(기자 EP14·18·19·49·진주노부인 EP26·49)·Hector(EP09·50)·펜던트(EP01→50)·드레스(EP05→46)·흉터·T2(15·23·38·45)·할머니(EP16→36) = 전수 대본 일치 확인. v38.2 = 현재 정본. |
| `_X_08_reborn_at_ten` | REBORN AT TEN | — | 폐기 |

새 작품 번호 = **09**.

> **현재본 단일 진실:** 각 작품의 `07_final/[작품]_FINAL_v{최신N}.md`. 메타 파일·CLAUDE.md 모순 시 → *파일 시스템 우선*. 메타 즉시 갱신.

> **메모리 위치 주의:** workspace 안에 `memory/` 폴더 *없음*. 실제 위치 = `C:/Users/Rowan/.claude/projects/C--Users-Rowan-scenario-automation/memory/`. `memory/feedback_*.md` 참조 = 그 위치를 의미.

---

## 룰

1. **묻지 말고 자율 진행.** 비가역 (캐논 변경·작품 이름 변경·대량 삭제·Hard Lock 변경)만 사전 확인.
2. **검증 보고서·테이블·자가 검수 풀이 = 본문 외 작성 금지.** 메타 분량 = 본문 톤 침투의 근본 원인.
3. **집필 컨텍스트 = raw drama prose 우선.** 매 phase_4 진입 시 매칭 히트작 3-5 EP + 이전 EP 3개 raw 정독 강제.
4. **EP 본문 = 영어 100% (한국어 0건).** EP 외 메타·footer·로그도 영어 권장.
5. **사용자 질문 시 PushNotification** (200자 이내·결정/입력값/블로커).

---

## 모델·세션

Opus / High effort. 시작 시 `/model` 확인. 본문 영어·대화 한국어.
