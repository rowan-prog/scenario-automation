---
name: 인물 이름·성씨 다양화 (필수)
description: 작품 간 인물 이름·성씨 겹침 회피. 새 작품 작성 시 기존 작품 이름과 충돌 검사
type: feedback
originSessionId: 777f324e-1f92-4184-bc4e-b1985877fe24
---
# 규칙

새 작품의 인물 이름 작성 시 **기존 진행 중인 모든 작품의 이름·성씨와 충돌 회피**.

## 1. 충돌 검사 강제

새 인물 이름 결정 전:
- `projects/[모든 작품]/[작품]_00_meta.md` 또는 `[작품]_04_blueprint_full.md`에서 캐릭터 이름·성씨 추출
- 같은 이름·성씨가 다른 작품에 있으면 회피
- 비슷한 음운(LIVIA / LYRA / LENA 등)도 가급적 회피

## 2. 다양화 가이드

- **장르별 이름 풀 구분:**
  - 그리스 신화 (TITAN BORN): Greek 어원 (KAEL·LYRA·SELENE·RHEA·CIRCE·ZEUS·ARES 등)
  - 드래곤 로맨타지 (THE OFFERING): 중세 판타지 어원 (ISOLDE·VAEL·HALDREN·KIRAN·ELARA 등)
  - 모던 콥/재벌 (I AM THE HEIR): 영어권 모던 (LIVIA·DECLAN·ADRIAN·MIRA·VIVIAN·SILAS·RYDER 등)
  - 코스믹 호러 (LAST KEY): 봉인·제의 어원 (ARDIS·MALACHI·THERON·LYRA·GALEN 등) — 단 LYRA 충돌 회피 권장
  - 모던 스릴러 (SHE STOLE MY FACE): 영어권 모던 (LENA·MARA·ETHAN·NOAH·VIVIAN 등) — VIVIAN 충돌 회피 권장
  - SF·루프 (EVERY MONDAY): 영어권 모던 (CAL·SLOANE·MARCUS·ILYA 등)

- **성씨도 작품 간 분리:** KORVIN(04) / CROSS(06) / ASTERION(07) 등 가문·기업명도 같은 시스템에 두지 않음

## 3. 검증 시점

- phase_1 (러프 청사진) 작성 시 1차 점검
- phase_3 (완성 청사진) 작성 시 2차 점검
- 새 인물 추가될 때마다 점검

## 4. 충돌 발견 시 처리

- 신규 작품 측에서 양보 (먼저 등재된 작품 우선)
- 어원·음운 모두 다른 이름으로 변경
- 변경 후 청사진·트리트먼트·스크립트 모두 일괄 업데이트

## Why
2026-05-09 사용자 피드백:
- "그리고 작품마다 인물들 이름이 너무 겹쳐 성씨랑!!!"
- 실제 충돌 사례:
  - LYRA: TITAN BORN (헤라 가문 후계) ↔ LAST KEY (어머니/사제) — 같은 이름
  - VIVIAN: I AM THE HEIR (시어머니) ↔ SHE STOLE MY FACE (재벌가 어머니) — 같은 이름
  - LIVIA / LYRA / LENA — 비슷한 음운

## How to apply
- phase_1·phase_3 작성 시 자동 충돌 검사
- 검출 시 즉시 신규 작품 측 이름 변경
- 한 번 결정한 이름은 청사진·트리트먼트·스크립트에 동시 반영 (나중에 일괄 변경하면 누락 위험)

## 사고 사례 누적 (2026-05-11 추가)

**2. JAX MERCER 충돌 (2026-05-11):**
- 신규 03_most_wanted_ship 주인공을 JAX MERCER로 작성
- 기존 07_my_map 주인공도 JAX MERCER — 완전 동일 이름·성씨
- 사용자 비판: "내가 하고 있는 my map 주인공 이름이 jax mercer임"
- 해결: 신규 작품 양보 → AXEL THORNE
- **원인:** 신규 작품 인물 이름 작성 시 다른 작품 grep 검사 누락

**3. LYRA 충돌 (2026-05-11):**
- 신규 03_most_wanted_ship의 LYRA VEX
- 기존 01_titan_born의 LYRA (리라) — 동일 이름
- 해결: 신규 → ASTRA VEX

## 신규 작품 인물 이름 자동 grep 검사 (필수, 2026-05-11)

**작성 직전 절차:**
1. `Grep` 또는 `Glob`으로 `projects/*/0*_*_02_pitch_deck.md` + `0*_*_01_blueprint*.md` 전체에서 후보 이름 검색
2. 영어 + 한국어 표기 둘 다 검사
3. 같은 또는 유사 음운 이름 발견 시 즉시 변경

**작품 간 인물 이름 풀 (2026-05-11 누적):**
| 작품 | 인물 이름 |
|---|---|
| 01 TITAN | KAEL, LYRA, SELENE, RHEA, CIRCE, DEIMOS, ZEUS |
| 02 OFFERING | ISOLDE, VAEL, HALDREN, ALDRIC, KIRAN, ELARA |
| 03 MOST WANTED SHIP | AXEL THORNE, ASTRA VEX, RAVEN NOX, ZIA LUMEN, LUNA VESPER, DRAGO |
| 04 HEIR | LIVIA, DECLAN, ADRIAN, ASHLEY, VIVIAN, SILAS, RYDER |
| 06 FACE | LENA, MARA, ETHAN, NOAH, VICTORIA, CELIA, TESSA |
| 07 MY MAP | JAX, MAYA, SIENNA, VICTOR |
| 08 GENIUS BABY | ELI MERRICK |

**유사 음운 회피:**
- LYRA / LIRA / LIRIA / LIVIA
- KAEL / KAI / CALEB
- VERA / VESPA / VEGA
- ZIA / SIA / ZARA
