---
name: hit-library-v2-2026-05-19
description: Vertical Hit Library v2 (2026-05-19 corrected) — 325 작품 + 88 트로프 + 43 AIGC. 모든 phase (개발·집필) 참조 baseline. 옛 v1 (2026-05-15) 폐기.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2d65e927-1cd5-4df0-bd23-1493c3adfb18
---

> **사용자 지시 (2026-05-19):** "히트작 라이브러리 업데이트했다. 이걸 기준으로 하라. 피칭덱 내 레퍼런스 매칭 뿐만아니라, 개발, 집필 단계에서 스토리, 트롭, 타이틀 스타일 참고하라."

## 라이브러리 위치

**현재 활성 = 버전 고정 금지.** 단일 진실 = `config/hit_library/current_hit_library.md` (이 포인터 파일이 활성 xlsx를 지정).
- 활성본 (2026-06-08 기준): `config/hit_library/vertical_hit_library_2026-06-05_updated.xlsx` (349행·시트 10개·`08_0605_UPDATE_LOG` 갱신 로그).
- archive: `_archived_vertical_hit_library_2026-05-15.xlsx`, `_archived_vertical_hit_library_2026-05-19_corrected_v2.xlsx`.
- 보조: `config/hit_library/market_insights_2026-05-16.md`.

## 시트 구조 (9개 — 06-05 updated는 `08_0605_UPDATE_LOG` 포함 10개)

| 시트 | 행 | 컬럼 | 용도 |
|---|---|---|---|
| **00_README** | 36 | 8 | 라이브러리 안내·KPI·Hard Rules |
| **01_FINAL_LIBRARY** | 325 | 26 | **메인 작품 목록** (Base + Merged + Supplement) |
| 02_REPLACEMENT_VALIDATION | 76 | 13 | 교체 검증 |
| **03_AIGC_TRACKER** | 43 | 12 | **AIGC 작품 추적** |
| **04_TROPE_INDEX** | 88 | 6 | **트로프 인덱스 (rank·count·platforms·example_titles)** |
| 05_SOURCE_REGISTER | 218 | 8 | 출처 등록 |
| 06_WEB_CHECK_NOTES | 12 | 5 | 웹 체크 |
| 99_LOOKUPS | 8 | 7 | 룩업 테이블 |
| **07_0519_NETSHORT_FIX** | 71 | 8 | 2026-05-19 NetShort/AIGC refresh |

## 01_FINAL_LIBRARY 핵심 컬럼 (참조 우선순위 — Hard Rule #4)

> **"기획 참조 시 title 자체보다 desire_engine·conversion_engine·aigc_leverage를 우선 읽을 것."**

1. **title / clean_title** — 작품명
2. **genre_trope** — 트로프 분류
3. **desire_engine** — 욕망 엔진 (시청자 보고 싶은 것)
4. **conversion_engine** — 결제 엔진 (페이월 동력)
5. **aigc_leverage** — AIGC 활용도
6. **logline** — 로그라인
7. **target_bucket** — 타깃 (북미 여성/남성·연령 등)
8. **priority** — A_Core (≥85점) 우선 / B_Standard / C_Reference
9. **performance_signal** — 성과 신호 (뷰·랭킹)
10. **format_aigc_flag** + **aigc_status** — AIGC 분류 (Direct/Explicit AI vs AI-theme only — Hard Rule #2 분리)

## 5 플랫폼

ReelShort · DramaBox · GoodShort · NetShort · DramaWave

## 04_TROPE_INDEX — Top 트로프 (count 순)

| Rank | 트로프 | Count | 플랫폼 | planning_note |
|---|---|---|---|---|
| 1 | Revenge | 19 | 5개 | (전 플랫폼 핵심) |
| 2 | CEO | 17 | 5개 | 여성향 결제 |
| 3 | Werewolf | 14 | 4개 | (여성향 다크 로맨타지·여기) |
| 4 | Romance | 11 | 5개 | 보조 |
| 5 | Karma Payback | 10 | NetShort | NetShort 핵심 |
| 6 | Mafia | 10 | 4개 | |
| 7 | All-Too-Late | 8 | 3개 | |
| 8 | Enemies-to-Lovers | 8 | 3개 | |
| 9 | Fantasy | 8 | 5개 | |
| 10 | Second Chance | 8 | 5개 | |
| 11 | BL | 8 | 3개 | |
| 12 | Regret | 8 | 3개 | 여성향 결제 엔진 기본축 |
| 13 | Contract Marriage | 7 | 4개 | |
| 14 | Fantasy-Male | 7 | GoodShort | AIGC/남성향 |
| 15 | Fake Heiress | 7 | GoodShort | |
| 17 | Hidden Identity | 6 | 2개 | |
| 19 | Underdog Rise | 6 | NetShort | |
| 20 | Pregnancy | 5 | 4개 | |
| 21 | Forbidden Love | 5 | 2개 | |
| 22 | Strong Female Lead | 5 | 2개 | |
| 24 | AI Microdrama | 5 | DramaWave | AI 카테고리 |
| 47 | Fated Mate | 3 | 2개 | |
| 81 | **2026-05-19 NetShort/System-AIGC** | **18** | NetShort | **신규 클러스터** |
| 82 | Rejected Luna/Alpha Queen/Werewolf regret | 4 | 2개 | 강한 werewolf 시그널 |
| 84 | Dragon/Zeus/divine daughter/royal crown | 5 | NetShort | AIGC/남성향 확장 |
| 85 | Captive/beast-world romance | 3 | NetShort | 야수·이세계·강제혼 |
| 87 | Mafia/court/historical power romance | 3 | NetShort | 권력 상속·금지된 사랑·궁정 복수 |

## Hard Rules (00_README)

1. **공식 platform/source URL 없으면 A_Core 승격 금지.** 강한 커뮤니티/광고 신호는 C/B까지 가능.
2. **AIGC 분류 분리:** Direct/Explicit AI · AIGC candidate · AI-theme only — AI 소재와 AI 제작 혼동 금지.
3. **보강자료는 월간 공식 랭킹 X / 공개근거 기반 큐레이션.** 기존행 삭제보다 병합·추가·교체후보 표기 우선.
4. **기획 참조 우선순위:** title 자체 X → **desire_engine·conversion_engine·aigc_leverage 우선**.

---

## 룰

**모든 phase 진입 시 라이브러리 자동 참조 baseline.**

### phase_0 (아이디어 제출)
- 04_TROPE_INDEX → 같은 욕망축·장르·타깃 작품 검색
- 03_AIGC_TRACKER (AIGC 작품 시) → 매칭 작품 정독
- 핵심 = desire_engine + conversion_engine 일치 작품 트로프 차용

### phase_1 (러프 청사진) / phase_3 (완성 청사진)
- 01_FINAL_LIBRARY → 같은 트로프·타깃 작품 logline·desire_engine·conversion_engine 정독
- title 자체보다 **엔진** 우선

### phase_2 (피칭덱)
- 01_FINAL_LIBRARY → 레퍼런스 매칭 (장르·타깃·desire_engine 일치 2-4편 + 매핑 키워드)
- `config/pitch_references/` 11개 통과 피칭덱과 함께 직접 대조

### phase_4 (집필 = Conversion Runway)
- 01_FINAL_LIBRARY → A_Core 작품 (≥85점) logline·conversion_engine 정독
- `config/vertical_drama_hit_scripts/` 실제 대본 정독과 결합
- **스토리·트롭·타이틀 스타일** 직접 참고 (사용자 명시)

### phase_5·6 (검토·패치)
- 결함 발견 시 같은 트로프 작품과 비교

## 옛 v1 (2026-05-15) 처리

- 옛 라이브러리 `_archived_vertical_hit_library_2026-05-15.xlsx`로 archive
- 옛 v1 참조 시스템 룰 (`feedback_hit_scripts_folder_priority.md`) = 그대로 유지 (`config/vertical_drama_hit_scripts/` 실제 대본 폴더 1순위)
- 본 v2 라이브러리 = `vertical_drama_hit_scripts/`와 보완 관계 (대본 = 실제 본문 / 라이브러리 = 325 작품 메타·트로프·엔진 매핑)

관련: [[hit-scripts-folder-priority]] / [[pitch-pass-fail-inference]] / [[ai-writing-guide-reference]] / [[paid-vertical-master]]
