# 시나리오 자동화

AIGC 숏폼 vertical drama 시나리오 제작. 최종 산출 = `projects/[작품]/07_final/[작품]_FINAL_v{N}.md`.

---

## 핵심 문서 3개 (2026-06-10 일원화 — 사용 시점별)

| 시점 | 문서 |
|---|---|
| 모든 작업의 근본 원리 (작품 진입 시 1회) | **`config/00_vertical_dna.md`** — 8 매체 조건·모든 룰의 모체 |
| 집필·재집필·가필 | **`config/10_writing_standard.md`** — 진입 게이트·△ 양식·연속극 구조·대사·State Ledger·모욕 표준 |
| 검수·LOCK | **`config/20_review_standard.md`** — 2모드·Track A/B·토큰 회계(LOCK belt ≤6 호출)·쇼러너 merge |

구 문서(hard_rules·final_review_flow·agent_operating_rules·lock_pipeline_standard·phase_4 prompt) = 위 3개로 통합·스텁만 잔존 (`config/_archive_2026-06-10/` 원문 보존). master_guide_v3(5816줄) = 집필 컨텍스트 진입 금지.

## 보조 자료 (필요 시점만)

| 필요 | 위치 |
|---|---|
| 작품 진행 메타 (이력 단일 진실) | `projects/[작품]/[작품]_00_meta.md` |
| 검증 히트작 raw | `config/vertical_drama_hit_scripts/` (집필 진입 시 매칭 3-5 EP 강제 정독) |
| 히트작 분석 / 페르소나 / 평가위원 | `config/vertical_drama_hit_scripts_analysis/` · `config/personas/`(검토 시) · `config/evaluators.md`(피칭 시) |
| 타깃 자료 | `config/target_research/` |
| 템플릿 | `config/engine_brief_template.md` · `visual_lock_template.md` · `production_handoff_template.md` · `mkt_selling_points_template.md` · `meta_template.md` |
| Reference / 피칭 데이터 | `config/reference_scripts/INDEX.md` · `config/pitch_references/MASTER_DATASET.md` |
| 검수 agent 7종 정의 | `~/.claude/agents/` (운용 룰 = `config/20_review_standard.md` §7) |
| 기계 도구 | `tools/voice_lint.py` · `tools/continuity_lint.py` · `tools/format_pass_verify.py` |
| 장르·작품 특수 메모리 | `memory/` (MEMORY.md 인덱스·호출 트리거 기반) |

---

## 워크플로우

```
phase_0 (아이디어) → phase_1 (러프 청사진) → phase_2 (피칭) → 피칭 결과
  → phase_3 (완성 청사진 + visual lock + engine brief) → phase_4 (집필 = 10_writing_standard)
  → phase_5/6 (검토·패치 = 20_review_standard 경량) → phase_7 (LOCK = 20_review_standard 풀)

부가 트랙: phase_a (각색) / phase_b (외부 대본) / phase_c (외부 피드백)
```

## 작품 파일 명명 규칙 (필수)

`projects/[NN]_[slug]/[NN]_[slug]_[단계번호]_[단계명].md` — 폴더 prefix 동일·하위 폴더(`05_episodes/`·`06_reviews/`·`07_final/`)도 prefix 적용·폐기 폴더 = `_X_NN_slug`(자동 차단).

---

## 현재 작품 (2026-06-10)

| 폴더 | 작품 | 현재 상태 |
|---|---|---|
| `_X_01_titan_born` · `_X_02_the_offering` · `_X_04_heiress_clause` · `_X_08_reborn_at_ten` | (폐기 4종) | 🚫 작업 금지 — 이력은 각 meta 파일 |
| `03_most_wanted_ship` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | phase_2 완료 |
| `06_she_stole_my_face` | SHE STOLE MY FACE | **정본 = `07_final/06_she_stole_my_face_FINAL_v63.md` (2026-06-16 · 🔒 LOCK). v63 = v62에 외부 피드백 5라운드(feedback_01~05·~37라인) + LOCK 자체검수(opus fresh-eyes=블로커 0·opus native-ear 5라인 직역화) 반영 후 **잠금**. 게이트: 한국어0·50화·Hard Cut49·END HOOK49·PAYWALL@EP9·NAME7·전회차≥223w·continuity_lint PASS. 산출물: 핸드오프 `06_she_stole_my_face_production_handoff_v63.md`·비주얼락 `06_she_stole_my_face_visual_lock_v63.md`. ▼ v62(LOCK 직전 작업본) = EP1-9 무료퍼널 *제한 재배치*(초반 가속): 현 EP2+EP3(클리닉 계획+사고처리)→**신 EP2 1화 압축**(Eileen 1줄·사고 몽타주·**TV로 자기 얼굴 Mara가 약혼 자리에 선 충격으로 EP2 끝**)·현 EP4→신 EP3·현 EP6 front-steps 굴욕 **1→2 분할**(Ethan 거절\|Victoria 손찌검). **50화·paywall@EP9·EP10-50 무관 유지·전 회차 ≥238단어·기계게이트 PASS·NAME7.** 차기 = 사용자 cold-read(새 초반 리듬). v61 = 직전 앵커(中 플랫폼 2-wave 구조개정+라인 직역화·기계게이트 PASS). v60 = 🔒 LOCK 앵커 보존. v61 = 中 플랫폼(主编/감독) 피드백 필터 반영 구조개정: **P1 중반 공개대치 4→2 wave**(Wave A=엄마/재단 탐욕[gala·EP13 luncheon 흡수·공개=foundation 탐욕만/사적=face 자백 "This face got me Ethan"]·Wave B=결혼/신분 **가짜승리→역공**[Woman in Pearls 공개 편들기→방 첫 동요→Mara "내 엄마 친구까지 거짓말에 끌어들인다"로 역전+증인 입막음→Lena 다시 거짓말쟁이→EP27 살해 동기]) + **P2 살해 EP를 banquet|service-yard 클리프행어 분할** + P4 face=원인 재앵커링("used my face to take...") + P6 Noah 보호선택 + **기각: 기자/카메라/증거/조사/법절차/Noah단서/EP3결혼식/foundation절차**. **라벨링 모욕 금지([[vertical-dialogue-dirty-fact-not-strong-sentence]] 갱신: that thing/creature/it 금지·수위는 단어만 낮추고 은유 X).** 차기 = 사용자 cold-read(새 중반). 누적: v58=라인 대수술+엄마 디톡스, v59=구조 압축1(EP13+14·17+18·25+26 병합·EP22 삭제→백하프 클리프행어 분할). v60 = **회차 엔진 de-proof + 구조 압축2**: ①증인/기자/클립/돈자백 *기능* 제거(woman-in-pearls=감정 조력자·reporter=축하에 마라가 greed 자진 폭발·"say the money's yours"자백유도→"selling my mother's name"모욕·EP33 계단=리셋 아닌 마라 자멸 발악) ②정합성 버그(crying in bed→on TV·fiancé asleep→bathroom·salon 잔재·ring 좌표→name·Eileen 이미 코트·you all→too many of you) ③구조: EP12(스튜디오 조롱 중복) 삭제·EP38(아침쇼 victim+staff 중복) 삭제 → EP10/EP35 클리프행어 분할로 50화. **엔진 = "마라가 제 천성으로 자멸·레나는 제 자리 탈환"(단계별 증명 드라마 X).** 차기 = 사용자 cold-read.** 초반(EP1-9)·피날레(EP48-49) 감정축은 섰으나 **중반(EP10-20)이 카메라/클립/마이크/돈질문/누가봤다 엔진 + 문학대사 잔존.** 라인 패스 집행분: ①**vertical English 하드락**(ESL+직역생존 기준·[[vertical-dialogue-dirty-fact-not-strong-sentence]] 갱신) — shape-of-you/costume/you-don't-get-the-show/sound-like-me 등 직역붕괴 라인 전건 교체 ②**노아 '알아보는 남자' 축 제거**(EP9 belief=오늘밤 목격·3년은 집착 romance로) ③**카메라/마이크/장부 라인 컷**(mic-still-on·can't-edit-out·microphone·doctors-secrets) ④인간오류 13(Mrs.Cross/my wife/박스/Jane Doe/좌표) ⑤EP13 엔진브레이크(에단 가짜눈물 간파) 교체. **사용자 피드백=AI 가능성→타당성 필터링·기각 사유 명시 룰.** **차기(미완·외과): 중반 씬 압축(EP13/17-19 중복·EP22 삭제후보·EP40-45 wedding setup·진주부인 증인기능 단일화).** v57 = **추리·수사·증거 엔진 전면 삭제 + 후회남 공식 + 입-폭로 피날레**: ①기자=수사관 전건 삭제(스너클립·창문·"돈 어디 갔나" 추적·이체서류·수술파일·노아 클리닉조사 전부 삭제)→마라 추락=*군중 앞 탐욕/잔인 자폭*만(갈라 라이브마이크 "It's MINE"·정크릿 "MY money"·재단 "Helena's daughter" 서명). ②EP8 6씬→3씬 압축(침투→마라 *자해/모함*→공개추락→폭한습격 절망훅 = 페이월; 녹음/슬랩 삭제·EP7 "쇼 안 준다" 회수). ③에단=마라 눈먼 사랑(의심 0)+레나 최대치 잔인+레나 집착(우아해진 레나 침꿀꺽/부정)→EP49 무릎꿇고 제뺨 때리며 피눈물, 레나 무시하고 노아 손잡고 퇴장. ④피날레 결정타=아일린 *제 입*으로 마라 팔아넘김(증거 0·라이브 방송)+레나 공개 이름/펜던트 회수. ⑤논리구멍(밤샘 전이→접근차단·no phone→잠긴폰·위조 비상연락처·훔친 유니폼)·문학대사(whole life/vows/name in mouth/wherever you go) 전건 삭제. 진주부인=사적 믿음→결혼식 공개 합류. 상세·이력 = `06_she_stole_my_face_00_meta.md`. **표준: [[face-theft-evidence-diet]]·[[vertical-regret-man]](눈먼사랑↑=후회↑·마라 의심0·레나 집착)·[[vertical-dialogue-dirty-fact-not-strong-sentence]]·추리/수사/증거 금지(군중 직접 목격+탐욕 자폭만).** **버전 룰: 메이저 = v{N+1} 복사 후 수정.** 핵심 메모리 = [[english-vertical-hit-dialogue-tone]] [[protagonist-not-villain-voice]] [[vertical-revenge-impostor-believed-engine]] [[vertical-regret-man]] |

새 작품 번호 = **09**.

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

메인 = 세션 최상위 모델(현 Fable) / High effort — **집필·수술·쇼러너 판정 = 메인 직접, 위임 금지.** 검수 agent 모델 분담 = `config/20_review_standard.md` §7 (단독 정밀 판정 = opus / 반복 수렴·기계 작업 = sonnet — Agent 호출 시 `model` 명시). 시작 시 `/model` 확인. 본문 영어·대화 한국어.
