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
| 타깃 자료 | `config/target_research/[성별]_target_research.md` · 권역 인사이트 = `es/jp_region_insights_2026-06.md` |
| 비주얼 락 템플릿 | `config/visual_lock_template.md` |
| Reference 인덱스 | `config/reference_scripts/INDEX.md` |
| 시스템 baseline 메모리 | `memory/` (always-load 3개만·MEMORY.md 참조) |
| 상태·정합성 도구 | `prompts/status.md` · `prompts/audit.md` |
| 검수 agent 7종 + 운용 룰 | `~/.claude/agents/` (정의) · **`config/agent_operating_rules.md` (운용 단일 진실)** (LOCK 전 최소 = voice_lint + fresh-eyes-auditor + cold-read 3회 수렴) |
| 최종고 검수 흐름 | **`config/final_review_flow.md`** (10+3패스·단일/sub-agent 모드 기준·쇼러너 merge·**절대 규칙: 천박함 ≠ 싸구려**) |
| 핸드오프 템플릿 | `config/production_handoff_template.md` (titan v169 양식·영어·LOCK 후 환류 시) |
| 마케팅 셀링포인트 템플릿 | `config/mkt_selling_points_template.md` (BUMP 엑셀 양식·전회차 트리트먼트+MKT IDEA·LOCK 후 마무리 산출물) |

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
| `_X_01_titan_born` | TITAN BORN | (외부 진행) | **🚫 폐기 — 외부 별도 진행 (2026-06-02)·작업 금지** |
| `_X_02_the_offering` | THE OFFERING: Claimed by the Dragon Lord | **🎬 `07_final/02_the_offering_FINAL_v68_dialogue_surgery.md`** | **🚫 폐기 — 외부 별도 진행 (2026-06-02)·작업 금지.** v68 = 대사·VO surgery 최종본(5217 lines·Korean 0·EP 50/50·sex scene 7건 보존). 상세 이력 = `02_the_offering_00_meta.md`(CLAUDE.md 원문 이관 포함). |
| `03_most_wanted_ship` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | (07_final 확인 필요) | phase_2 완료 |
| `_X_04_heiress_clause` | I AM THE HEIR | — | 폐기 |
| `06_she_stole_my_face` | SHE STOLE MY FACE | **🎬 `07_final/06_she_stole_my_face_FINAL_v47.md`** (2026-06-08) | **현행 정본 = v47 = v46 사용자 diff 검토 반영 (12곳).** ①EP49 흉터를 결정타에서 제외(Lena 'look under her ear' 증거제시 삭제 → Mara *무의식* hand-to-ear 자기배반 tell만·결정타=자백) ②EP49 펜던트 회수 주체화(EP50 'security peels' 몽타주 삭제 → Lena가 무너진 Mara 목에서 직접 풀며 "This was always mine") ③EP49 Ethan 굴욕(매달림 → Lena 무시 + Noah "She's done talking to you" 냉대) ④EP10 DNA/랩 4줄 과설명 경량화(labs/hospitals/psych-hold 행정어 제거·"cameras first") ⑤EP07 hair 연속성 오류 수정("releases the hair"→"steps back") + 씬명 The Scar→The Real Face ⑥EP08 wiped 라인 첩보톤 축소 ⑦EP37 "whole staircase"→"a stretch of marble" ⑧EP50 "surgeon's bill"(미장전 정보)→"calls her Mara" ⑨EP45 기자 초대 개연성 1줄(맨 앞줄=의심한 자 보상) ⑩EP14 Noah 1줄 정리. 기계 게이트 = 101,093 chars·HC49·END HOOK49·Korean0·MICRO_ACTING0·METAPHOR3. **검수 정책 교정(2026-06-08 사용자): 일상 "검토"=diff 경량(바뀐 구간+파급+기계 게이트)·무거운 병렬 검수단=LOCK 직전만 (`config/final_review_flow.md`).** pre-LOCK 보류 과제: EP24-36 gloat-call/venue 반복 collapse·피날레 응징 体感 보강(cold-read 3회 수렴). v46: 톤-독립 디벨롭+보조 22곳 / v45: 3차 16 / v44: 2차 31 / v43: 1차(상세 = meta). **docs: 핸드오프 v42·비주얼락 v6.1·청사진 v4.1 = LOCK 신호 후 일괄 환류 (기자 6회·EP49 리액션샷·EP37 의상 대비 노트).** 엔진 = impostor-believed 막장(시청자는 EP01부터 전모를 앎·세상은 EP48까지 가짜를 믿음·진실은 증거 X Mara 자백으로만·악역 = 천박/뻔뻔/멍청·중반 균열 = 호감 균열이지 swap 발각 아님). 50EP·페이월 EP8·T2 EP15/23/38/45·HC49·END HOOK 49(EP50 자연 END.)·~100k chars·voice_lint v42 베이스라인 동일. cold-read 수렴: EP1 9·EP1-8 9·페이월 8·EP9-12 6(=엔진 고정 비용·더 깎으면 엔진 훼손). 물증형 보증 2자루(흉터·각인) EP1-3 장전. 핵심 메모리 = [[vertical-revenge-impostor-believed-engine]]·[[easy-dopamine-over-logic]]. **전체 버전 이력(v30→v42)·수술 상세 = `06_she_stole_my_face_00_meta.md` 단일 진실(CLAUDE.md 원문 이관 포함).** |
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
