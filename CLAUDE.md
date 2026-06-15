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
| `06_she_stole_my_face` | SHE STOLE MY FACE | **정본 = `07_final/06_she_stole_my_face_FINAL_v57.md` (2026-06-15 · 🔒 LOCK · 기계게이트+fresh-eyes(opus·CRIT0)+cold-read(페이월 YES·피날레9) 통과[한국어0·HardCut49·END HOOK49·NAME7·PAYWALL1·ILY2·continuity PASS·88씬·50화·118,993자]).** 비차단 차기 최적화 = 중반(EP13-30) 디브리프 메트로놈 축소·EP25 샤워 차별화·레나 가시적 중반 승리 1개. v57 = **추리·수사·증거 엔진 전면 삭제 + 후회남 공식 + 입-폭로 피날레**: ①기자=수사관 전건 삭제(스너클립·창문·"돈 어디 갔나" 추적·이체서류·수술파일·노아 클리닉조사 전부 삭제)→마라 추락=*군중 앞 탐욕/잔인 자폭*만(갈라 라이브마이크 "It's MINE"·정크릿 "MY money"·재단 "Helena's daughter" 서명). ②EP8 6씬→3씬 압축(침투→마라 *자해/모함*→공개추락→폭한습격 절망훅 = 페이월; 녹음/슬랩 삭제·EP7 "쇼 안 준다" 회수). ③에단=마라 눈먼 사랑(의심 0)+레나 최대치 잔인+레나 집착(우아해진 레나 침꿀꺽/부정)→EP49 무릎꿇고 제뺨 때리며 피눈물, 레나 무시하고 노아 손잡고 퇴장. ④피날레 결정타=아일린 *제 입*으로 마라 팔아넘김(증거 0·라이브 방송)+레나 공개 이름/펜던트 회수. ⑤논리구멍(밤샘 전이→접근차단·no phone→잠긴폰·위조 비상연락처·훔친 유니폼)·문학대사(whole life/vows/name in mouth/wherever you go) 전건 삭제. 진주부인=사적 믿음→결혼식 공개 합류. 상세·이력 = `06_she_stole_my_face_00_meta.md`. **표준: [[face-theft-evidence-diet]]·[[vertical-regret-man]](눈먼사랑↑=후회↑·마라 의심0·레나 집착)·[[vertical-dialogue-dirty-fact-not-strong-sentence]]·추리/수사/증거 금지(군중 직접 목격+탐욕 자폭만).** **버전 룰: 메이저 = v{N+1} 복사 후 수정.** 핵심 메모리 = [[english-vertical-hit-dialogue-tone]] [[protagonist-not-villain-voice]] [[vertical-revenge-impostor-believed-engine]] [[vertical-regret-man]] |

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
