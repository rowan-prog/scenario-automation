# 12_hired_to_ruin_me — 폴리시 수술 계획서 (FINAL_v1 → v2)

작성 2026-07-14 · §4-1 수술 파이프라인 · 원본 = `07_final/12_hired_to_ruin_me_FINAL_v1.md` (50화·불변)

> 목적 = FINAL_v1 폴리시 미결 5건 처리. **범위 = 대사/스테이징 tic 제거 위주(고가치·저위험).** 구조 seam은 오탐 판정 → 수술 안 함(§5 "밋밋하게 다림질" 금지).

---

## 1. 판정 (기계 실측 + 원문 대조)

| # | 항목 | 판정 | 실측 근거 |
|---|---|---|---|
| A | **"Then [전제뒤집기]" 오프너 tic** | **수용(최우선)** | register_census: CLAIRE 17회 · EVE 14회 = 31회 (cap 3). D-5-0 코치봇 시그니처와 동일 패턴. |
| B | 로맨스 스테이징 반복 | **수용** | grep: throat 29 · counter-lift 준동일 3(L1050/L1753 거의 verbatim) · wall-pin 로맨스 5 · "No camera reaches…I checked" 준동일 4-5(L336/652/826/1094) |
| C | 반복 클로징 장치(스크린/피드) | **부분수용** | pacing_lint [4]: 13화(cap 8)·EP38-40 3연속 런. 감시카메라=엔진이라 일부는 의도 → 런 해체 + 제네릭 2-3화만 다양화 |
| D | 단발 room | **부분수용** | pacing_lint [1]: 13(cap 3). **단 home-base drift PASS·전부 Ashford estate 내부** = occasion-hopping 아님(저택=방 많음). 무상 통합만 소폭 |
| F | Claire 감정-형식 평탄 | **부분수용** | census: 194라인 중 !2 ?3 파편4 · quiet:61. 배신발각·대면·클라이맥스 핵심 비트만 형식 감정 점검(전면 톤개조 X) |
| — | 리셋-오프닝 스트릭 3구간 | **기각(오탐)** | pacing_lint [5] FLAG이나 seam 정독: EP16→17=플랜 실행 급행·EP38→39=같은 study NIGHT→DAY 연속. home-base drift PASS. 06 v70(occasion-hopping 동반)과 상황 다름 → 침습 수술 = 역효과. 문서화만 |
| — | cool-tone(Claire45/Eve39) | **기각(의도+미달)** | census 60% cap 미달 · Eve 알파/Claire 복수자 = 의도 레지스터(meta 수용). F로 Claire 핵심 비트만 보강 |

기계 게이트 원본(v1): pacing_lint = [1]FLAG(13) [2]PASS [3]PASS [4]FLAG(13,EP38-40) [5]FLAG(오탐) [6]PASS · register_census = CLAIRE/EVE FLAG(Then tic).

---

## 2. 수술 항목 · 분담

| 유닛 | 항목 | 지시 |
|---|---|---|
| **script-surgeon #1 (opus)** | **A. "Then" 오프너 감축** | 31회 → 캐릭터당 최강 ≤3만 존치, 나머지 ~25 varied 오프너로 교체. **교체안끼리 새 tic 금지**(구문형 오프너 반복 X). 비트/의미/톤 지문 보존. old/new 대조표 |
| **script-surgeon #2 (opus)** | **B+F. 스테이징 de-dup + Claire 감정 비트** | throat 부위-순회 thinning(다른 감각/동작 대체)·counter-lift 준동일 2건 리블록·wall-pin 5→2-3·"No camera reaches" 대사 4-5 phrasing 다양화(엔진 보존). Claire 핵심 감정 비트 3곳 형식-감정 점검. old/new 대조표 |
| **script-surgeon #3 (opus)** | **C. 클로징 장치** | EP38-40 3연속 스크린-클로징 런 해체 + 제네릭 스크린/피드 END HOOK 2-3화 다른 절단(대사/행동/제3자)로 교체. **엔진(카메라 되받기) 훅은 보존** |
| **메인 직접** | **D+E. 헤더 소통합** | 무상 단발 room 통합(study doorway→study·east wing sitting room→sitting room 등)·같은 위치 연속 EP에 Continuous 태그 정정(EP38→39 study 등). 비트 손상 시 미시행 |

## 3. 보존 리스트 (하드 — 침해 시 기각)
- **엔진:** 감시 카메라 이중생활(카메라앞 가짜/사각지대 진짜)·극적 아이러니·강탈 사다리(금고16→명의20→드라이브31→암호38→차단40→동결41)·"카메라 되받기" 참교육
- **시그니처 훅:** EP8 페이월·EP23 이름 봉인-파열·EP49 "Nora" 해금·EP34 위기/구출
- **형식:** 2부 구성·END HOOK·Hard Cut·본문 영어100%·Continuous 태그 정확성

## 4. 게이트 (v2 마감 전)
- register_census: CLAIRE/EVE "Then" 오프너 ≤3 · 새 오프너 tic 0
- pacing_lint: [4] EP38-40 런 해체 확인 · [1] 무상통합분 감소
- grep: throat 대폭 감소 · counter-lift verbatim 0 · 한국어 0 · 원작잔재 0
- continuity_lint PASS · voice_lint · 화수 50 · HardCut 49 · END 1
- 러닝타임 비퇴행(터치 화 순삭제 X)

## 5. 상태 (완료 2026-07-14)
- [x] v2 분기
- [x] surgeon #1/#2/#3 산출
- [x] 머지(§4-1 6번) — 총 40건 적용. **거부 1건 = #3 EP34**(SIMONE 폰버즈 제거 시 Richard "Right on time." 참조 붕괴 + EP35 Simone 브리지 절단 = 연속성 위반). #2 L2206 = 에코(L1098 "down into 침대") 회피 위해 "fits her mouth…slow and deep"로 미세조정.
- [x] 게이트 스윕 — register_census FLAG 0 PASS(Then 31→6)·pacing[4] EP38-40 런 해체·throat 12→5·counter-lift dup 0·voice HIGH 88=88 MED 36→34·continuity=v1 baseline(제1부 포맷 아티팩트)·제1부 훅 4건(EP18/39/40/43) sync·word 17398→17377(비퇴행)
- [x] 마감 — meta·CLAUDE.md·본 계획서 갱신

**미개입(문서화):** 단발 room 13(전부 한 저택·home-base drift PASS=occasion-hopping 아님) · 리셋오프닝 스트릭 3(오탐=같은 저택 시간전진·plot 연속) · cool-tone(cap 미달+의도 레지스터). §5 "밋밋하게 다림질" 회피.
**정본 = `07_final/12_hired_to_ruin_me_FINAL_v2.md`.**
