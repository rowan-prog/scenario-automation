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
| `02_the_offering` | THE OFFERING | **🔒 `07_final/02_the_offering_FINAL_v33_5_clean.md`** | **Production LOCK** (2026-05-21·v33.5·다크 로맨스 슈퍼퀸 label reversal·출산 EP48-49·후일담 EP50만·Sera 영원 라이벌·행정/정치 어휘 0건) |
| `03_most_wanted_ship` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | (07_final 확인 필요) | phase_2 완료 |
| `_X_04_heiress_clause` | I AM THE HEIR | — | 폐기 |
| `06_she_stole_my_face` | SHE STOLE MY FACE | (07_final 확인 필요) | phase_3 완료 |
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
