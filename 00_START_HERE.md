# 00_START_HERE — Workspace 진입 점

> **모든 작업 시작 시 본 파일을 먼저 정독. CLAUDE.md는 인덱스·룰 자료. 본 파일은 *현재 상태*의 단일 진실.**

---

## 즉시 확인 (매 세션 진입 시)

### 0. 세션 모델 확인 (🚨 2026-07-10 사용자 재확인 — 반복 지적 사항)
**파이프라인은 opus/sonnet/haiku만으로 자급되게 설계돼 있다 — Fable은 구조·룰·워크플로우 자체를 개정할 때만 1회성 투입.** 지금 세션이 Fable이고 이번 요청이 구조/룰 개정이 아니면(집필·각색·검수 등 실무) → 사용자에게 "opus로 충분합니다" 고지. **세션 모델이 무엇이든, 프로스 실무(EP 본문·대사 생성)는 메인이 직접 하지 않고 항상 별도 opus agent에 위임한다** (`config/10_writing_standard.md` §A 진입게이트 0번 · `config/20_review_standard.md` §7 · memory `feedback_fable_structure_only.md`). 이 룰은 이미 3중으로 문서화돼 있었는데도 실무에서 스킵됐던 전례가 있다 — 매 집필 요청마다 실제로 위임했는지 자문할 것.

### 1. 현재 작업 가능 프로젝트 (활성)

**단일 진실 = `CLAUDE.md` "현재 작품" 표.** 이 표를 여기 복제하지 않는다(2026-07-10 — 두 곳에 같은 표를 두면 한쪽이 갱신될 때 다른 쪽이 stale해지는 게 반복된 실패 패턴이었다. 실제로 이 표는 2026-05-21 이후 갱신이 안 돼 활성 작품 5개 중 2개만 반영하고 있었다). `CLAUDE.md`를 열어 "현재 작품" 섹션을 확인할 것.

### 2. 폐기 프로젝트 (작업 금지)

| 폴더 | 사유 |
|---|---|
| `projects/_X_01_titan_born/` | 외부 별도 진행 — `_X_` prefix·자동 차단 (2026-06-02) |
| `projects/_X_02_the_offering/` | 외부 별도 진행 — `_X_` prefix·자동 차단 (2026-06-02) |
| `projects/_X_04_heiress_clause/` | 폐기 — `_X_` prefix·자동 차단 |
| `projects/_X_08_reborn_at_ten/` | 폐기 — `_X_` prefix·자동 차단 |
| `projects/_X_09_scarred_bride/` | 폐기 — `09_ashen_bride`와 번호 충돌로 발견·동일 컨셉 후속안에 밀림 (2026-07-10) |

### 3. 현재 작품 내 폐기·실험·아카이브 (작업 금지)

`projects/02_the_offering/_deprecated/` 안:
- `premium_pilot/`·`premium_pilot_lite/`·`premium_pilot_v2/` (옛 premium pilot 시도 — 폐기)
- `version_b/`·`version_c/`·`version_d/`·`version_e/` (옛 version 시도 — 폐기)
- `v30_episodes/` (v30 episode split 폴더 — 폐기·통합본은 v32 사용)
- `_archived_ep21_43_v5_rewrite_source.md` 등 옛 rewrite source

`projects/02_the_offering/07_final/_archive_versions/` 안:
- v31.4·v31.3·v31.2·v31.1·v31·v30·v20·v19·v18·v17·v16·v15·v14·v13·v12·11개 옛 정본
- *작업 금지·참고용*

**원칙:** `07_final/[작품]_FINAL_v{N}.md` 1개만 활성. 모든 V 이전 본·실험본·split 본은 `_deprecated/` 또는 `_archive_versions/`.

---

## 메모리 위치 (중요)

**`memory/` 폴더는 workspace 안에 없음.** 실제 위치:

```
C:/Users/Rowan/.claude/projects/C--Users-Rowan-scenario-automation/memory/
```

`CLAUDE.md`·기타 문서가 `memory/feedback_*.md`라고 참조할 때 = *위 위치*를 의미.

**Always-load 목록 = `memory/MEMORY.md` "🥇 매 작업 진입 시" 섹션이 단일 진실.** 여기 별도 목록을 복제하지 않는다(2026-07-10 — 구 목록이 2026-06-10 메모리 v4 개편 이후 갱신 안 돼 `config/hard_rules.md`처럼 이미 스텁으로 바뀐 파일을 "12 hard rule 정독 대상"으로 지목하고 있었다 — 같은 stale-duplicate-table 패턴).

**호출 트리거 baseline:** `memory/MEMORY.md` 참조

---

## 작업 시작 전 의무 체크리스트

매 phase 진입 시 다음 5가지를 *순서대로* 확인:

1. **본 파일 (`00_START_HERE.md`) 정독** — 현재 상태 파악 (§0 세션 모델 확인 포함)
2. **CLAUDE.md 인덱스 확인** — 자료 위치 + 핵심 문서 3개(`00_vertical_dna`·`10_writing_standard`·`20_review_standard`)
3. **`memory/MEMORY.md` "🥇 매 작업 진입 시" 정독**
4. **집필 진입이면 `10_writing_standard.md` §A 진입게이트(0번 프로스 위임 확인 포함) 전항 통과**
5. **작품 진입 시 `projects/[작품]/[작품]_00_meta.md` 정독** — 작품 현재 상태

→ 1개라도 SKIP = 작업 중단·먼저 정독.

---

## 새 작품 진입 시 추가 의무

6. **시장 reference raw 대본 3-5 EP 정독** — `config/vertical_drama_hit_scripts/` 매칭 장르
   - 다크 로맨스: `[말할 수 없는 나의 신부]` 등
   - 남성향 power fantasy: 별도 매칭
7. **장르 매칭 호출 트리거 baseline 정독** — `memory/MEMORY.md` 참조

---

## 작업 완료 후 의무 갱신

작품을 새 버전 (v32 → v33 등)으로 진척 시:

1. **본 파일 (`00_START_HERE.md`) 즉시 갱신** — 현재본 V 번호·다음 작업 표시
2. **`projects/[작품]/[작품]_00_meta.md` 즉시 갱신** — 정본 V 번호·상태
3. **`CLAUDE.md` 작품 status table 갱신** — 현재본 V 번호
4. **옛 본은 즉시 `_archive_versions/`로 이동** — `07_final` 안에 V 한 개만
5. **실험/폐기본은 즉시 `_deprecated/`로 이동** — `projects/[작품]/` 최상위에서 제거

→ 위 5 갱신을 *작업과 같은 turn에* 수행. 다음 turn에 미루지 말 것.

---

## 권한 설정

`.claude/settings.local.json` 정책:

**허용:**
- `mkdir -p *`·`cp *`·`mv *` (안전 파일 작업)
- `python3 *`·`awk *`·`sed -n *` (안전 분석)
- `grep *`·`cat *`·`ls *`·`wc -l *` (읽기 전용)

**금지:**
- `rm -rf *`·`rm -fr *` (대량 삭제)
- `pip install *` (전역 환경 변경)
- `git push --force*`·`git reset --hard*` (Git 파괴적 작업)

→ 폐기/실험본 정리 시도 `mv` (이동)만 사용. `rm -rf` 절대 X. 사용자 명시 요청만 예외.

---

## 워크플로우 (참조)

```
phase_0 (아이디어) → phase_1 (러프 청사진) → phase_2 (피칭) → 피칭 결과
  → phase_3 (완성 청사진 + engine brief) → phase_4 (Conversion Runway 집필)
  → phase_5 (페르소나 검토) → phase_6 (패치) → phase_7 (최종고)
```

상세: `CLAUDE.md` 워크플로우 섹션.

---

## 한 줄

> **본 파일 = 현재 상태 단일 진실. 작업 시작 = 본 파일 정독. 작업 완료 = 본 파일 갱신.**

마지막 갱신: 2026-07-10 — 세션 모델 확인(§0) 신설·활성 프로젝트 표/always-load 목록 중복 제거(CLAUDE.md·memory/MEMORY.md 단일 진실로 통일, 7주 stale 상태였음)·`_X_09_scarred_bride` 반영
