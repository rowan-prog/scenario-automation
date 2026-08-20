# Vertical Drama 성공작 대본 — 검증 레퍼런스 라이브러리

> **사용자 검증 히트작 대본 전용 폴더.** 중국·일본·한국·미국 숏폼 vertical drama 검증작. *검증된 시장 신호*로 사용.
>
> **🚨 사용 룰 (2026-05-21 수정):** 본 raw 대본은 *기능 샘플 (functional sample)*. *모방·직접 복사 금지*. *기능 비교 후 변환*만 허용.
>
> **사용 프로토콜:** `config/reference_calibration_protocol.md` 정독·7 비트 비교표 작성 후 사용. raw 대본 직접 읽기 = reference card 부족 시만.
>
> **시장 톤 분리:** vertical drama 공통 문법은 학습 후 차이점만 인지. 톤·정서 표현은 시장별 (북미 여성향·북미 남성향·중국 가족극·한국 재벌극·일본 로판) 분리.

---

## 폴더 구조 (평평·단일)

```
vertical_drama_hit_scripts/
├── README.md                              본 파일 (룰)
├── INDEX.md                               등재 작품 통합 인덱스
└── [대본 파일들]                          국가별 분류 X / 평평한 단일 폴더
```

> **사용자 명시:** 국가별 폴더 분류 X. 평평한 단일 폴더 + 파일명에 국가 코드.

---

## 🚨 코퍼스 진입 규칙 (2026-08-20 제정 — 임의 선별 사고 재발 방지)

**읽는 순서가 고정돼 있다. 파일 크기·제목·직관으로 고르지 말 것.**
1. **INDEX.md 상단 '우선 8종'** — Bussy and the Beast · 약자의 가면 강자의 힘 · 신의한방 · 말할 수 없는 나의 신부 · 나의 토깽이 아가씨 · TITAN BORN · Owned by the Vampire King · Dragon Lord
2. **INDEX에 '검증 히트작'으로 명시된 것** (MY EX'S MAFIA UNCLE · 危険な甘い檻 · 도망쳐봐 내게서 · LOCKED OUT)
3. **최신 등재순**(파일 mtime 내림차순) — 사용자가 최근 넣은 것이 최근 판단의 기준이다
4. 그다음 나머지 전량

**docx·pdf도 반드시 포함한다.** md만 읽으면 이 장르의 실물(Bussy·TITAN BORN·LOCKED OUT·약자의 가면·Dragon Lord)이 통째로 빠진다 — python-docx / PyMuPDF로 추출해서 읽는다. ⚠️ docx는 표·텍스트박스가 누락되니 분량이 비정상적으로 작으면 pdf 판본을 쓴다([[docx-conversion-drops-table-textbox-text]]).
**분석 문서(`../vertical_drama_hit_scripts_analysis/`)를 원문 대신 쓰지 말 것** — 그건 색인이지 근거가 아니다.

> **2026-08-20 사고 기록:** 이 규칙이 없어서, 규격을 세우는 라운드에서 INDEX의 우선 8종을 안 보고 크기순으로 KR 역대본 6편(전부 INDEX '분석 대기' 상태)만 읽고 결론을 냈다. 사용자 판정 = *"무료런 정독은 좆같은 것만 모아서 했네"* · *"최신으로 넣은 것부터도 아니고, '모든' 것도 아니고."* 그 결론("EP1 도입 0")은 오답이었다.

---

## 등재 룰

### 1. 본 폴더 = 대본만
- 대본 파일 (원본 또는 번역본)
- 분석·메모·메타 = **별도 메모리 또는 INDEX**에
- 본 폴더 = pure script repository

### 2. 파일 명명 규칙
`[제목]_[플랫폼]_[원작국가코드].md` 또는 `.txt`

**🚨 중요 (사용자 명시 2026-05-17):** 국가 코드 = **원작 vertical 시장** (작품이 검증·히트된 시장). **대본 언어 ≠ 원작 국가.** 한국어로 번역·작성된 대본이라도 원작이 중국 vertical이면 `CN`·미국 vertical이면 `US`.

원작 국가 코드:
- `KR` — 한국 vertical
- `CN` — 중국 vertical
- `JP` — 일본 vertical
- `US` — 미국 vertical (ReelShort·DramaBox 등 북미 시장)
- `GL` — 글로벌 (다국가 동시 히트)

대본 언어는 파일 내부 메타에 별도 기재 (한국어·영어·중국어·일본어 번역본 등).

예시:
- `천재_아기의_인생역전_몰입_KR.md` (한국어 대본·한국 vertical)
- `attribute_seizer_dramawave_US.md` (한국어 번역 가능·**미국 vertical**)
- `[제목]_[플랫폼]_CN.md` (한국어 번역 가능·**중국 vertical**)

### 3. 루트 인박스

새 히트작 원본은 루트 `vertical_drama_hit_scripts_inbox/`에 먼저 넣는다.

- 원본은 그대로 보존한다.
- 분석 후 필요한 작품만 `config/vertical_drama_hit_scripts/`에 정리 등재한다.
- 성공작의 장면 보상 루프는 시스템 가이드에 반영한다.

### 4. 자동 등재 (사용자 새 대본 추가 시)
- AI가 자동으로 작품 메타 추출 (제목·플랫폼·국가·장르·욕망축·메인 빌런·여주 호·페이월 패턴 등 14 항목)
- INDEX.md에 한 줄 등재
- 별도 분석 메모리 작성 (중요 발견 시)

### 5. 활용 (모든 작품 baseline)
- **매 phase 진입 시 INDEX 참조** (작품 메타 매칭 — 장르·타깃·욕망축 / **국가 신경 X / vertical drama 특징 학습**)
- **압력축·모욕 루프·여주 호·남주 패턴 직접 모방**
- 작가 자기 분석·외부 AI 옵션 X / **검증 작품 패턴 우선**

### 6. Demon Lord's Marked Bride 류 실패작
- **절대 등재 X**
- 실패작 인사이트는 실패 postmortem으로만 보존
- `Demon Lord's Marked Bride`는 바람직 모델이 아니라 paid vertical 오독 사례다.
- 메모리 매출 검증 룰 정합

---

## 우선순위 (모든 시스템 자료 대비)

> **사용자 검증 성공작 대본 = 모든 다른 자료보다 우선.**

| 우선순위 | 자료 |
|---|---|
| 🥇 1순위 | **vertical_drama_hit_scripts_inbox/** 및 `config/vertical_drama_hit_scripts/` (사용자 검증 성공작) |
| 🥈 2순위 | `config/master_guide_v3.md` (최상위 가이드) |
| 🥉 3순위 | `CLAUDE.md` (시스템 룰) |
| 4순위 | `config/production_guide.md` (v2 보조) |
| 5순위 | 메모리 (1순위·2순위·3순위·4순위) |
| 6순위 | 각 phase prompt |

---

## How to apply

### 새 작품 phase_0~3
- INDEX에서 같은 욕망축·장르·타깃 작품 검색
- 해당 대본 정독·압력축·모욕 루프·여주 호·남주 패턴 직접 분석
- 새 작품 청사진에 그 패턴 직접 적용

### 기존 작품 (OFFERING 등) 재설계
- INDEX에서 다크 로맨타지·여성향·드래곤 mate 류 검색
- 검증 대본 패턴 직접 모방 (작가 분석·외부 AI 옵션 X)
- 옛 청사진 + 검증 대본 비교 → 결격 정정

### 검토 단계
- 페르소나가 검증 대본 패턴 vs 현재 대본 매트릭스 비교
- 패턴 차이 = 🟡 / 검증 결격 = 🔴

---

## 핵심 룰

> **사용자가 등재한 성공작 대본 = 절대 진리. AI 자기 분석·외부 AI 분석은 모두 검증 대본 앞에서 무력.** 검증 대본 패턴 직접 모방·무지성 적용 X (인사이트 추출 후 작품 정합).
