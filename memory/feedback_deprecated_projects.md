---
name: 폐기 프로젝트 리스트 + 자동 차단 룰 (필수, 2026-05-12)
description: 폐기된 프로젝트 폴더 _X_ prefix. 사용자가 잘못 호출해도 작업 진행 X / 폐기 알림. 폐기 인사이트는 보존 (다른 프로젝트 폐기 방지)
type: feedback
originSessionId: 4c7933e7-5184-4f06-90d5-47f598aaf3dc
---
# 폐기 프로젝트 리스트 + 자동 차단

## 폴더 명명 규칙

폐기 프로젝트 = **`_X_NN_slug`** prefix (짧음·토큰 최소·알파벳 정렬 맨 아래)

## 폐기 프로젝트 리스트

| 번호 | 슬러그 | 폴더 (현재) | 폐기일 | 폐기 사유 (요약) | 인사이트 |
|---|---|---|---|---|---|
| **04** | heiress_clause | `_X_04_heiress_clause` | 2026-05-12 | AI 약점 카테고리 (모던 현실 코드 + 여주 감정 몰입) / 위원 1/6 / 디벨롭 후 SHE STOLE 중복 | `feedback_pitch_pass_fail_judgment.md` |
| **08** | reborn_at_ten | `_X_08_reborn_at_ten` | 2026-05-15 | 사용자 명시 폐기. 부가 A 각색 작품 (REBORN AT TEN: My Stepfather Buried My Mother. I'll Bury His Empire.) — phase_2 피칭덱 완료 후 정체. 사용자 결정으로 폐기 | `feedback_v3_adaptation_11_slots.md` (각색 룰 신규 등재 후 사용자 판단) |

## 슬롯 재사용 / 미생성 슬롯 (2026-05-13 audit 발견)

폐기와 별개로 다음 슬롯들도 자동 차단 대상이거나 옛 계획 잔존:

| 번호 | 옛 계획 | 현재 상태 | 처리 |
|---|---|---|---|
| **03** | black_core (I AM THE EMPIRE) | **폴더 미생성** → 03 슬롯 `03_most_wanted_ship`으로 재사용됨 (다른 컨셉) | 옛 03_black_core 호출 시 → "03 슬롯은 03_most_wanted_ship으로 재사용됨" 알림 |
| **05** | last_key (THE LAST KEY) | **폴더 미생성** (CLAUDE.md 옛 계획 잔존) | 호출 시 → "05_last_key는 미생성 슬롯입니다. 신규로 시작하려면 phase_0부터 진입" 알림 |
| **07** | every_monday_manhattan_dies (EVERY MONDAY, MANHATTAN DIES) | **폴더 미생성** (CLAUDE.md 옛 계획 잔존) | 호출 시 → "07_every_monday_manhattan_dies는 미생성 슬롯입니다" 알림 |

**다음 신규 작품 번호:** **09** (04·08 폐기 영구 비움 / 05·07은 재사용 가능하나 옛 컨셉 회피 권장).

## 자동 차단 룰 (필수)

사용자가 다음 방식으로 폐기 프로젝트 호출 시 **작업 진행 X / 폐기 알림 즉시 반환:**

### 차단 트리거
1. **번호 호출** — "04", "4번 작품", "프로젝트 4" 등
2. **슬러그 호출** — "heir", "heiress", "heiress_clause"
3. **작품명 호출** — "I AM THE HEIR", "시아버지 유언", "HEIR" 등
4. **잘못된 번호·이름 호출** (사용자 실수 가능성)

### 차단 응답 형식
> "⛔ 04_heiress_clause (I AM THE HEIR)는 2026-05-12 폐기 결정된 프로젝트입니다.
> 폐기 사유: [한 줄]
> 인사이트: `feedback_pitch_pass_fail_judgment.md` (HEIR 사례) 참조.
> 진행하시려면 폐기 재검토 명시 필요."

## 폴더 보존 정책

- 폐기 폴더 = **삭제 X / 보존** (인사이트 자료)
- 폴더 내 파일 (러프 청사진·피칭덱·피칭 결과) = 향후 같은 카테고리 작품 회피·디벨롭 참고용
- 메타 파일 = "폐기" 상태 명시 + 폐기 사유 + 인사이트 보존

## 폴더 번호 정책

- 폐기 후 같은 번호 재사용 **X**
- 다음 신규 작품 = 다음 번호 (현재 진행 중 작품 + 1)
- 04 폐기 = 04 번호 영구 비움 / 신규 작품은 09부터

## 폐기 인사이트 보존 (다른 프로젝트 폐기 방지)

폐기 인사이트는 다음 메모리에 누적 보존:
- `feedback_pitch_pass_fail_judgment.md` — 폐기 vs 디벨롭 5 자가 검증
- `feedback_male_target_pitch_lessons.md` — 남성향 작품 카테고리 본질 판단
- `feedback_pitch_male_target_education.md` — 피칭덱 교육 섹션
- `feedback_dark_romantasy_engine.md` — 다크 로맨타지 공식
- 본 메모리 — 폐기 작품 리스트 + 인사이트 매핑

→ **신규 작품 기획 시 본 폐기 리스트 + 폐기 인사이트 메모리 자동 참조.** 동일 약점 카테고리 회피.

## How to apply

- 사용자가 작품 호출 시 본 리스트 자동 매칭
- `_X_` prefix 폴더 발견 시 자동 차단
- 차단 시 사용자에게 짧은 알림 + 인사이트 메모리 참조
- 사용자가 "폐기 재검토" 명시 시에만 진행

## 핵심 한 줄 결론

> **폐기 프로젝트 = `_X_` 폴더 + 자동 차단 + 인사이트 보존.**
