---
name: hit-scripts-folder-priority-2026-05-17
description: vertical_drama_hit_scripts 폴더 = 사용자 검증 성공작 대본 전용. 모든 시스템 자료 대비 절대 우선. 매 phase 진입 시 INDEX 참조. AI 자기 분석·외부 AI 옵션은 검증 대본 앞에서 무력.
metadata: 
  node_type: memory
  type: reference
  originSessionId: 462b4a02-4290-4164-a105-ac1f2ff0ecca
---

# 🥇 Vertical Drama 성공작 대본 폴더 (절대 우선)

## 사용자 명시 (2026-05-17)

> **"vertical drama 성공작 대본 폴더가 따로 있는 게 좋아 보인다. 대본만 넣는 곳으로. 중국숏폼·일본숏폼·한국숏폼에서 히트한 것들이다."**

## 위치

`C:\Users\Rowan\scenario-automation\config\vertical_drama_hit_scripts\`

구조:
- `README.md` — 폴더 룰
- `INDEX.md` — 등재 작품 통합 인덱스
- `01_korea/` — 한국 숏폼 히트작
- `02_china/` — 중국 숏폼 히트작
- `03_japan/` — 일본 숏폼 히트작

## 우선순위 (모든 자료 대비 절대 1순위)

| 순위 | 자료 |
|---|---|
| 🥇 **1순위** | **vertical_drama_hit_scripts/** (사용자 검증 성공작) |
| 🥈 2순위 | `config/master_guide_v3.md` |
| 🥉 3순위 | `CLAUDE.md` |
| 4순위 | `config/production_guide.md` (v2 보조) |
| 5순위 | 메모리 (1·2·3·4순위) |
| 6순위 | 각 phase prompt |

## 핵심 룰

### 1. 검증 대본 = 절대 진리
- 사용자가 검증한 히트작 = 모든 자료보다 우선
- AI 자기 분석·외부 AI 분석·작가 자기 평가 = 검증 대본 앞에서 무력
- 단 **무지성 적용 X** — 인사이트 추출 후 작품 정합 후 적용

### 2. 새 대본 자동 등재
사용자가 새 대본 폴더에 추가 시 AI 자동 진행:
1. 작품 메타 추출 (제목·플랫폼·장르·타깃·매출 / 원작 국가 = 있으면 좋음 / 분석 본질 X)
2. **3축 분석 (캐릭터·이야기 구조·대사 스타일)** + 14 세부 항목 (욕망축·압력축·메인 빌런·보조 빌런·여주 호·남주 패턴·모욕 루프·VO·페이월·무료 N화·거대 VFX·수위 등)
3. INDEX.md에 한 줄 등재
4. 별도 분석 메모리 작성 (필요 시·중요 발견 시)

> **🚨 핵심 룰 (2026-05-17 사용자 명시):** "한국어 대본이 어느 나라인지는 알 필요 없다." → **국가 신경 X / vertical drama 특징 학습 우선.** 분석 본질 = **구조·캐릭터·대사 패턴 추출**. "국가 초월" 류 과도한 일반화 X (사용자 정정 2026-05-17).

### 3. 매 phase 진입 시 자동 참조
- **phase_0 (아이디어):** INDEX에서 같은 욕망축 검색·아이디어 검증
- **phase_1 (러프 청사진):** 같은 장르 검증 대본 정독
- **phase_2 (피칭덱):** 레퍼런스 매핑·매출 검증
- **phase_3 (완성 청사진):** 검증 대본 패턴 직접 모방·압력축·모욕 루프
- **phase_4 (집필):** 검증 대본 voice·티키타카·VO·페이월 직접 모방
- **phase_5 (검토):** 검증 대본 vs 현재 대본 매트릭스 비교

### 4. 실패작 절대 등재 X
- Demon Lord's Marked Bride 류 실패작 절대 X
- 성공작만 (사용자 검증 필수)

### 5. 작품 phase 결정 시 직접 적용
- "이 작품은 한국 [X]와 중국 [Y]를 합친 패턴으로 간다" 식 명확화
- 추상 분석 X / **구체 대본 직접 참조**
- "검증 대본 [X]에서는 EP3에 이런 비트 있었음" 식 직접 인용

## 활용 예시 (OFFERING 1-8화 재설계 시)

1. INDEX에서 다크 로맨타지·여성향·드래곤 mate·werewolf 등 매칭 대본 검색
2. 매칭 대본 3-5편 직접 정독
3. 14 항목 추출 후 OFFERING 청사진 vs 검증 대본 매트릭스 비교
4. 결격 항목 발견 시 검증 대본 패턴으로 정정
5. 무료 EP1-8 = 검증 대본 패턴 직접 모방 (단 작품 정체성 유지)

## 회피 (절대 X)

- 검증 대본 무시 / AI 자기 분석으로 진행
- 외부 AI 옵션 우선 (검증 대본 앞에서)
- 실패작 패턴 (Demon Lord 류) 모방
- 무지성 모방 (작품 정합 X)

## 채택 (절대)

- 검증 대본 직접 정독 → 패턴 추출 → 작품 정합 후 적용
- INDEX 매 phase 자동 참조
- 작품 정체성 + 검증 패턴 결합

## 정합 (기존 메모리)

- `feedback_pitch_2_stage_evaluation.md` (피칭 2단계 평가·레퍼런스 필수) — 정합
- `feedback_paid_vertical_master.md` (매출 baseline) — 정합
- `feedback_pressure_axis_stacking_vs_dispersion.md` — 검증 대본 압력축 직접 추출
- `feedback_clip_reward_loop.md` — 검증 대본 클립 보상 패턴 직접 모방
- `feedback_concrete_villain_humiliation_loop.md` — 메인/보조 빌런 검증 대본 직접 추출

## 핵심 한 줄 (절대)

> **사용자 검증 성공작 대본 = 절대 1순위. AI 자기 분석·외부 AI 옵션은 검증 대본 앞에서 무력. 매 phase 자동 참조·직접 모방 (작품 정합 후).**
