# 00_START_HERE — Workspace 진입 점

> **모든 작업 시작 시 본 파일을 먼저 정독. CLAUDE.md는 인덱스·룰 자료. 본 파일은 *현재 상태*의 단일 진실.**

---

## 즉시 확인 (매 세션 진입 시)

### 1. 현재 작업 가능 프로젝트 (활성)

| 폴더 | 작품 | 현재본 (정본) | 단계 | 다음 작업 |
|---|---|---|---|---|
| `projects/02_the_offering/` | THE OFFERING | **🔒 `07_final/02_the_offering_FINAL_v33_5_clean.md` (Production LOCK 2026-05-21)** | v33.5 LOCKED + 비주얼 락 v4 완료 | 원어민 polish (내가 진행·다음 단계) |
| `projects/01_titan_born/` | TITAN BORN | (07_final 확인 후 갱신) | 완결 ✅ | 없음 |
| `projects/03_most_wanted_ship/` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | (07_final 확인 후 갱신) | phase_2 완료 | phase_3 진입 대기 |
| `projects/06_she_stole_my_face/` | SHE STOLE MY FACE | (07_final 확인 후 갱신) | phase_3 완료 | phase_4 진입 대기 |

### 2. 폐기 프로젝트 (작업 금지)

| 폴더 | 사유 |
|---|---|
| `projects/_X_04_heiress_clause/` | 폐기 — `_X_` prefix·자동 차단 |
| `projects/_X_08_reborn_at_ten/` | 폐기 — `_X_` prefix·자동 차단 |

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

`CLAUDE.md`·`hard_rules.md`·기타 문서가 `memory/feedback_*.md`라고 참조할 때 = *위 위치*를 의미.

**Always-load 3개 (매 phase 진입 시 절대 정독):**
1. `feedback_no_theater_tone.md` — 시적·연극톤 절대 금지
2. `feedback_dark_romance_relationship_centered_v2_3.md` — 둘의 관계 70% / 외부 적 30%
3. `config/hard_rules.md` (workspace 내) — 12 hard rule 1페이지

**호출 트리거 baseline:** `memory/MEMORY.md` 참조

---

## 작업 시작 전 의무 체크리스트

매 phase 진입 시 다음 5가지를 *순서대로* 확인:

1. **본 파일 (`00_START_HERE.md`) 정독** — 현재 상태 파악
2. **CLAUDE.md 인덱스 확인** — 자료 위치
3. **`config/hard_rules.md` 정독** — 12 hard rule
4. **memory/ always-load 3개 정독**
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
  → phase_3 (완성 청사진 + visual lock) → phase_4 (Conversion Runway 집필)
  → phase_5 (페르소나 검토) → phase_6 (패치) → phase_7 (최종고)
```

상세: `CLAUDE.md` 워크플로우 섹션.

---

## 한 줄

> **본 파일 = 현재 상태 단일 진실. 작업 시작 = 본 파일 정독. 작업 완료 = 본 파일 갱신.**

마지막 갱신: 2026-05-21
