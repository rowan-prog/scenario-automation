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
| `06_she_stole_my_face` | SHE STOLE MY FACE | **🎬 `07_final/06_she_stole_my_face_FINAL_v30.md`** (FINAL · 50화 완성 · 2026-05-29) | v28 thriller skeleton 폐기·전면 reset. 50화 emotion-engine + Mara = 절친 (시기·질투) + Noah = firm CEO 트로피 (Keene) + 사회 인식 reveal EP49로 lock + Mara villain 유지 (구제 X). 외부 리뷰 v30(2) 12 fix 모두 적용 (요일 통일·차량·heel snaps·blessing 명명·평판 음해 출처 완화·scar photo 인정·numbing/sedative·diner livestream·Tessa 부채·service route). **구조 reset 핵심:** ①Halcyon trust·federal/subpoena/board takeover apparatus 전수 제거 ②Mara EP01 face reveal = surgical mask drop (early appearance X) ③EP01-48 = 안 뒤집힌 판에서 Lena/Noah 한 장면씩 이기기·EP49 = 진짜 회수 (boardroom + cemetery) ④Mara 7단계 추락 ladder (승자→가짜→균열→cornered→토사구팽→매달림→매장) ⑤Eileen 죽음 = 환경적 (legal X) ⑥T2 sex 4건 (EP15·23·38·48) ⑦무대 5종 기능 분리 (가족모임·동창회·Cross 행사·약혼·결혼식). Verification: 50 EP·0 Korean·99,977 char·0 thriller words·scar 2cm below left ear 통일·Keene 통일. 이전 트랙: v25 외부 리뷰 / v26 compound 톤 / v27 flashback / v28 정합성 36 + Halcyon (구조 reset으로 폐기). |
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
