# 시나리오 자동화

AIGC 숏폼 vertical drama 시나리오 제작. 최종 산출 = `projects/[작품]/07_final/[작품]_FINAL_v{N}.md`.

> **대본 문서 = 제1부(기획·개요) + 제2부(정식 회차 대본) 2부 구성 — 각색·신규 공통 필수** (2026-07-02). 상세 = `config/10_writing_standard.md` §B-0.

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
| 검수·집필지원 agent 9종 정의 | `~/.claude/agents/` (운용 룰 = `config/20_review_standard.md` §7 — 3-tier 모델맵·직교 sweep·집필지원 W1-W3 = `10_writing_standard.md` §A-1) |
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
| `09_ashen_bride` | THE BEAST KING'S WOUNDED BRIDE / 야수왕의 상처입은 신부 | phase_2 (피칭덱) — 미녀와야수 역전 고수위 몬스터 로맨스·정서 레퍼런스 Broken Vows |
| `06_she_stole_my_face` | SHE STOLE MY FACE | **정본 = `07_final/06_she_stole_my_face_FINAL_v70.md` (48화).** v63 LOCK 이후 사용자 cold-read 라운드(v64~v70): ①초반 가속 — EP1-3→2화 + 계단 EP3+EP4 병합 → **50→48화**(무료런 8→7·Noah 구원/희망 EP7·PAYWALL@EP8) ②대사 census de-rhythm(소유/나열 tic ~19→북엔드2+클라이맥스1) ③모녀=한 몸 공범(아일린 함께 침몰) ④goad 중복 해소(아파트=사회적 말살) ⑤노아 de-parrot(확신=행동) ⑥청중 스케일 표준화 ⑦프레임-탈피 소수정(on repeat→live·EP45 범죄자 선퇴장 등). 타임라인=이른 오후 클리닉→저녁 크래시→밤. 게이트: 한국어0·48화·HardCut47·END HOOK47·PAYWALL@EP8·END1. 상세 이력 = `06_she_stole_my_face_00_meta.md`. **버전 룰: 메이저 = v{N+1} 복사 후 수정.** 핵심 메모리 = [[vertical-rhythmic-list-fuel-only-in-scarcity]] [[english-vertical-hit-dialogue-tone]] [[protagonist-not-villain-voice]] [[vertical-revenge-impostor-believed-engine]] [[vertical-regret-man]] |

새 작품 번호 = **10**.

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

메인 = 세션 최상위 모델(현 Fable) / High effort — **집필·수술·쇼러너 판정 = 메인 직접, 위임 금지.** 검수 agent 모델 분담 = `config/20_review_standard.md` §7 **3-tier 맵**(2026-07-02): **티어는 중요도 아닌 업무 성격이 정한다** — 단독 정밀 발견/하드블록 = **opus** / 반복 수렴·중난도 추출 = **sonnet** / 기계+naive-proxy(뇌오프 시청자·flat-TTS·무맥락 이미지생성기 — *덜 이해해야 정확*) = **haiku**. Agent 호출 시 `model` 명시(미지정 = 비싼 상속). 영상·음성 = AIGC라 생성기 프록시(`aigc-draw-auditor`·`tts-literal-ear` = haiku) 상설. 시작 시 `/model` 확인. 본문 영어·대화 한국어.
