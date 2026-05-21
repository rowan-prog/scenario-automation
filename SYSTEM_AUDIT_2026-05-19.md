# 시스템 정합성 진단 보고서 (2026-05-19)

> 사용자 지시 (2026-05-19): "시스템이 지금 너무 다 안 맞는다. 정합성에 오류가 나는 듯 하다. 시스템 메모리나 claude.md 등 참조나 이런 것들이 부정합이 과하다. 시스템이 정합적으로 돌아가는지, 불필요한, 아카이브도 필요없는 자료들이 넘치진 않는지 점검이 필요하다."

---

## 1. 점검 결과 요약

### ✅ 정합 OK (정합성 양호)
- **MEMORY.md ↔ memory/ 폴더 = 89:89 완전 일치** (broken link 0건·미인덱스 0건)
- **memory/archive/ = 46 파일** (옛 마스터 흡수본·보관 분류 OK)
- **projects/ = 6 폴더** (_X_ prefix 폐기 명확)
- **config/ = 14 항목** (신규 자료 ai_writing_guide·pitch_references 등재 OK)
- **prompts/ = 17 파일** (_archived_ prefix 명확)

### 🚨 정합성 오류 (즉시 정정 필요)

**CLAUDE.md 자체 모순 — 체질 개선 v3 (2026-05-17) 신규 룰과 옛 룰 동시 잔존:**

| Line | 문제 | 체질 개선 v3 룰 |
|---|---|---|
| 88-97 | 워크플로우 다이어그램에 옛 19-step + FINAL_FREE/PAID 분리 | Conversion Runway 7 step + FINAL.md 1종 |
| 94-95 | "산출물: FINAL_FREE.md + Pilot Bible" / "FINAL_PAID.md" | 1종 FINAL.md만 |
| 102 | "무료회차 EP1-8 → Lite Protocol 자동 분기 / 유료 EP9-50 = phase_4~7" | Conversion Runway 한 호흡 / 회차 가변 |
| 271-295 | "최종고 = 3종 통합 MD (FINAL_FREE/FINAL_PAID/FINAL)" 섹션 | 1종 FINAL.md |
| 295 | "무료-only 작품 = FINAL_PAID 생략" | 옛 룰 |

**같은 파일 안에 모순 명시:**
- Line 115: "**최종고 1종** (FINAL.md만 — 옛 3종 폐기)"
- Line 271-295: "**3종 통합 자동 생성**" 섹션 존재

→ 이 모순이 OFFERING 작업 시 메타 잘못 표기 (잠금 표기 등) 원인의 하나.

### ⚠️ 옛 룰 잔존 메모리 (archive 이동 후보)

| 파일 | 옛 룰 | 체질 개선 v3 대체 |
|---|---|---|
| `feedback_episode_split_and_runtime.md` | 50화 고정·EP1-8 무료·편당 분량 룰 | `feedback_episode_count_flexibility.md` (가변) |
| `feedback_final_consolidation_three_files.md` | FINAL_FREE/PAID/FINAL 3종 | `feedback_unified_writing_flow.md` (1종) |
| `feedback_writing_default_full_run.md` | "집필 = 전 화수 50화 자동" | `feedback_episode_count_flexibility.md` + `feedback_conversion_runway_writing.md` |

### ⚠️ 옛 룰 잔존 prompts (검토 후 정리 또는 표기 명확화)

| 파일 | 잔존 룰 | 처리 |
|---|---|---|
| `prompts/protocol_premium_pilot_lite.md` | 옛 Lite Protocol 7 step (무료회차 한정) | Conversion Runway 7 step으로 대체 / archive |
| `prompts/phase_4~7` | 본문 안 무료/유료 분리 룰 가능성 | grep 검사 후 정리 (옛 잔존 있으면 갱신) |
| `prompts/status.md` | 옛 룰 표기 가능성 | grep 검사 |

---

## 2. 정정 작업 순서

### Phase A — CLAUDE.md 정정 (즉시)
1. Line 88-99 워크플로우 다이어그램 — 체질 개선 v3 통합 (Conversion Runway·FINAL.md 1종)
2. Line 102 무료회차 protocol 라우팅 — Conversion Runway로
3. Line 271-295 최종고 3종 섹션 — 1종 FINAL.md로 정정
4. 옛 룰 잔존 라인 제거 / archive 표기

### Phase B — 메모리 archive 이동 (3건)
- `feedback_episode_split_and_runtime.md` → archive
- `feedback_final_consolidation_three_files.md` → archive
- `feedback_writing_default_full_run.md` → archive
- MEMORY.md 인덱스 정리

### Phase C — prompts archive (1건 + grep 검사)
- `prompts/protocol_premium_pilot_lite.md` → `_archived_protocol_premium_pilot_lite.md` (옛 무료 분리 룰)
- phase_4~7 본문 grep으로 옛 잔존 발견 시 갱신

---

## 3. 실행 완료 (2026-05-19)

### ✅ Phase A — CLAUDE.md 정정 완료
- Line 88-99 워크플로우 다이어그램 → Conversion Runway 7 단계 + FINAL.md 1종으로 갱신
- Line 102 무료회차 protocol 라우팅 → "옛 premium_pilot / Lite 폐기" 표기로 갱신
- Line 271-295 최종고 3종 섹션 → 1종 FINAL.md로 정정 (체질 개선 v3)
- prompts 트리 표기 (Line 56) → archive 3종 분류 명확화

### ✅ Phase B — 메모리 archive 이동 완료 (3건)
- `feedback_episode_split_and_runtime.md` → archive/ (옛 50화·EP1-8 무료 분리)
- `feedback_final_consolidation_three_files.md` → archive/ (옛 3종)
- `feedback_writing_default_full_run.md` → archive/ (옛 50화 자동)
- MEMORY.md 인덱스 정정 (3건 제거 + archive 안내 추가)
- 메인 폴더: 89 → 86 / archive: 46 → 49

### ✅ Phase C — prompts archive 이동 완료 (1건)
- `prompts/protocol_premium_pilot_lite.md` → `prompts/_archived_protocol_premium_pilot_lite.md`
- 사유: 체질 개선 v3에서 Conversion Runway 7 단계로 대체

### ✅ Phase D — prompts/ 본문 옛 룰 정정 완료 (사용자 지시 2026-05-19 "당연히 옛 룰은 정정해야지")

| 파일 | 정정 항목 |
|---|---|
| `prompts/phase_7_final_gate.md` | 3종 분리 4-Gate (line 1-77) → 1종 FINAL.md 4-Gate / line 195 정정 |
| `prompts/phase_4_episode_writing.md` | 무료/유료 분리 진행 → 전 회차 1개 자연 흐름·Conversion Runway 7 단계 |
| `prompts/phase_5_persona_review.md` | 무료회차 라우팅 헤더 → 체질 개선 v3 안내 / line 420 EP1-8 무료 → Conversion Runway 구간 |
| `prompts/phase_6_revision.md` | 무료회차 라우팅 헤더 → 체질 개선 v3 안내 |
| `prompts/phase_0_idea_submission.md` | "무료-유료 구조 EP1-8/EP9+" → "결제 루프 구조 (자연 흐름·EP5-15 분포)" |
| `prompts/phase_1_rough_blueprint.md` | "50화 고정 / 무료 1-8화 고정" → "회차 수 가변·페이월 위치 가변" / line 158 EP1-8 무료 → Conversion Runway 구간 |
| `prompts/phase_2_pitch_deck.md` | line 322 EP1-8 무료 → Conversion Runway 구간 |
| `prompts/phase_3_full_blueprint.md` | line 116-118 50화 확장·무료 1-8화 → 전 회차 확장 (가변)·Conversion Runway 구간 |
| `prompts/phase_a_1_adaptation_blueprint.md` | Section 5-5 옛 50화 고정 → 가변 룰 |
| `prompts/phase_b_external_script_intake.md` | Section 5-5 옛 50화 고정 → 가변 룰 |
| `prompts/status.md` | 상태 표·라우팅 룰 전면 정정 (Conversion Runway / 1종 FINAL.md / phase_8 폐기) |

**최종 검증 (grep 결과):**
- 옛 무료/유료 분리 본문 라인 = 0건
- FINAL_FREE/PAID 본문 라인 = 0건
- premium_pilot 본문 라인 = "옛...폐기" 안내 컨텍스트만 잔존 (의도된 안내)
- archive 파일 (_archived_*) = 보존 OK (역사 자료)

## 4. 검증 (정정 후)
- MEMORY.md 링크 ↔ 실제 파일 매칭 = 86:86 일치 (3 archive 이동 후)
- CLAUDE.md 내부 1종 vs 3종 모순 = 해소
- 체질 개선 v3 (Conversion Runway + 1종 FINAL.md + 회차 가변 + 페이월 자연 흐름) 일관성 = CLAUDE.md 핵심 부분 일관
