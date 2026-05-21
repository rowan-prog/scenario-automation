# Reference Calibration Protocol — 히트작 raw 대본 사용 룰

> **히트작 raw 대본은 *절대 진리*가 아니라 *기능 샘플*이다. *모방*이 아니라 *기능 비교 후 변환*만 허용.**

---

## 0. 룰의 배경

이전 `vertical_drama_hit_scripts/README.md`는 "절대 우선·직접 모방" 톤이었다. 그 결과 Claude가 *raw 대본의 문장·구조를 직접 복사*하는 위험이 있었다. 본 프로토콜은 그 위험을 방지한다.

**핵심 원칙:** raw 대본 = *기능 샘플 (functional sample)*. 작품의 *시청자 결제 동력*을 분석하기 위한 데이터. *내 작품에 그대로 옮기는 템플릿* X.

---

## 1. 작품 진입 전 의무 (phase_1·3·4 모두 적용)

### 1-1. Reference 작품 1-3개 선정 (사용자 또는 작가 명시)

다음 *동일* 조건의 작품 1-3개:
- **타깃 시청자 일치** (북미 여성 20-40·중국 vertical 시장·일본 BL 등)
- **장르 일치** (다크 로맨스·werewolf romance·power fantasy·romance fantasy 등)
- **회차 분량 일치** (50화 ±5·60화 ±5 등)
- **결제 모델 일치** (free arc + paywall + paid arc)

→ 사용자 직접 지정이 default. 자동 선정은 *후보 5개 → 사용자 확인* 절차.

### 1-2. 7 비트 기능 비교표 작성

선정 reference 1-3개에서 다음 7 비트를 *작품 매칭*으로 비교:

| 비트 | Reference A | Reference B | Reference C | 내 작품 |
|---|---|---|---|---|
| **첫 10초** | (구체 시각·대사·인물 위치) | | | (내 EP01 첫 10초 비트 비교) |
| **첫 모욕/위협/욕망/권력 이동** | (어떤 인물에 어떤 사건) | | | |
| **회차 끝 hook** | (마지막 컷·대사·행동) | | | |
| **paywall 직전 행동** | (EP6-8 마지막 컷) | | | |
| **EP9 or 첫 유료 보상** | (첫 폭발 비트) | | | |
| **대사 길이·turn rhythm** | (문장당 단어·turn당 단어) | | | |
| **소품·몸·문서·권한 이동** | (소품 활용·신체 비트·서류·권한 변경) | | | |

→ 작품 phase_1·3·4 진입 시 *위 표를 작품 reference memo로* 작성 (`projects/[작품]/[작품]_07_reference_calibration.md`).

→ 이 표가 *없으면* 작업 중단·먼저 작성.

---

## 2. Raw 대본 사용 제약

### 2-1. Raw 대본 직접 읽기 금지 (default)

대신 *reference card* (구조화된 분석본) 우선 사용:

```
config/vertical_drama_hit_scripts_analysis/[작품명]_reference_card.md
```

reference card 형식:
- 작품 정보 (제목·플랫폼·국가·회차)
- 7 비트 기능 (위 비교표 양식)
- 시청자 반응 데이터 (있는 경우)
- 주의사항 (변환 시 risks)

→ raw 대본 직접 읽기 = *reference card 부족 시만*. 정독 후 즉시 card 작성.

### 2-2. Raw 대본 *복사 금지*

- 문장·대사·구조 *직접 복사* 금지
- 발화 패턴 *모방* 금지 (예: 같은 turn rhythm)
- 캐릭터 이름·소품·세팅 *재사용* 금지

→ 변환 (transformation) 만 허용. *기능을 추출하고 내 작품에 맞게 재창조*.

### 2-3. "절대 진리·직접 모방" 표현 폐기

이전 README의 "AI 분석·외부 AI 옵션보다 절대 우선" 표현 = 너무 강함. 새 표현:

> "검증된 시장 신호. 단 *내 작품에 그대로 옮기지 말 것*. 기능 비교 후 변환."

---

## 3. 국가별·장르별 톤 분리

### 3-1. 시장 톤 차이 인지

다음은 *공통 vertical 문법* 외에 *구분*되는 톤 요소:

| 시장 | 톤 특성 |
|---|---|
| **북미 여성향** | female gaze·consent·heroine agency·dark romance 기본 |
| **북미 남성향** | power fantasy·hierarchy disruption·서비스컷·준하렘 신호 |
| **중국 가족극** | 가족 갈등·세대 충돌·복수 카타르시스·정서 통제 |
| **한국 재벌극** | 계급 갈등·계약 결혼·차가운 남주·신데렐라 변주 |
| **일본 로판** | 회귀·천재 아기·악역 영애·황실 권력극 |

→ 작품 타깃에 따라 *해당 시장 톤 우선*. 다른 시장의 raw 대본 참조 시 *톤 변환* 필수.

### 3-2. "국가 신경 X" 룰 폐기

이전 README의 "국가 신경 X" 표현 = 너무 거침. 새 표현:

> "vertical drama 공통 문법은 학습 후 차이 점만 인지. 톤·정서 표현은 시장별 분리."

---

## 4. 분석 폴더 단일화

현재 분석본이 두 곳에 존재:
- `config/vertical_drama_hit_scripts_analysis/` (별도 폴더)
- `config/vertical_drama_hit_scripts/_analysis/` (raw 폴더 안)

**결정:** `config/vertical_drama_hit_scripts_analysis/`를 *canonical*로. `_analysis/` 안 내용은 `_deprecated/`로 이동 또는 통합.

→ 다음 패스에서 실행 (사용자 확인 후).

---

## 5. 작품별 reference memo 의무 결과물

phase_1 진입 시:
```
projects/[작품]/[작품]_07_reference_calibration.md
```

phase_3 진입 시 갱신.
phase_4 진입 시 *집필 직전 1회 재정독* + 갱신.

내용:
- 선정 reference 1-3개 (제목·플랫폼·국가·이유)
- 7 비트 비교표
- 변환 결정 (어떤 기능을 어떻게 내 작품에 적용)
- 변환 *금지* 결정 (어떤 raw 요소는 *복사 안 함*)

---

## 6. 한 줄

> **Raw 대본 = 기능 샘플. 직접 모방 금지. 7 비트 비교표 작성 후 변환. 시장 톤 분리. Reference card 우선·raw 정독 보조.**

마지막 갱신: 2026-05-21
