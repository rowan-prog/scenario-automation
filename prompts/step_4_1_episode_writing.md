# Step 4-1 — 에피소드 집필 프롬프트

## 역할
완성 청사진을 바탕으로 개별 에피소드 시나리오를 집필한다.
스크립트는 청사진에 명시된 타깃 언어로 작성한다.

## 실행 전 읽어야 할 파일
- config/production_guide.md
  - Section 0-3 (락/열어둠 — 창작 결정 시 절대 락과 자율 영역 구분)
  - Section 3 (핵심 제작 원칙)
  - Section 6 또는 7 (작품 타입에 따라 택1: AIGC 애니메이션 또는 실사형)
  - Section 9-1 (남성향 작품일 때 선언형 대사 5조건)
  - Section 13 (회차 설계 원칙)
  - Section 14 (시나리오 작성 원칙 — 14-1, 14-2, 14-3)
  - Section 17 (Layer/수위 관리 원칙)
  - Section 18 (AIGC Production Direction 원칙)
- projects/[작품명]/[작품명]_04_blueprint_full.md (필수)
- **projects/[작품명]/[작품명]_04_visual_lock.md (필수 — 모든 [Visual] 지문에 직접 반영)**
- 메모리: **`feedback_visual_lock_system.md`** (비주얼 락 반영 + 환류 룰)
- **config/reference_scripts/INDEX.md** — 등재된 reference 목록. 작품 메타(타깃·포맷·장르·언어)와 일치하는 script_format 카테고리 reference 자동 선택.

**Reference 정독 룰 (필수, 2026-05-12 — 토큰 절감):**
- script_*.md 파일은 150-220KB 거대 파일 → **매번 전체 정독 금지**
- 포맷 참고용 = **첫 1-2 씬 (3-5KB)만 Read** (씬 헤더·Visual·Camera·Dialogue·FX·End Image 구조)
- 페이월 비트 참고 = 해당 무료 마지막 화만 Read
- 특정 비트 reference = Read offset/limit로 부분 정독
- INDEX의 카테고리 매칭 = 어느 파일 어느 부분이 적합한지 결정용

### 타깃 자료 (집필 시 매 회차 적용 — 단계 한정 Section만)

매 회차 후킹 비트 다발 (90초 회차 3-5개 / 2-3분 회차 5-8개) + 보상 루프·결제 트리거 적용:

**남성향 작품:**
- `config/target_research/male_target_research.md`
  - **이 단계 필요 Section: 22 (10 결제 패턴), 24 (설계 룰 4 — 잠긴 보상·매화 끝 상태), 25 (포맷별 강약점), 28 (매화 끝 상태 변화 룰)**
- 메모리: `feedback_male_target_research_data.md` / `feedback_male_target_immediate_gratification.md` / `feedback_paid_vertical_platform_signals.md` / `feedback_hook_density_vs_qa_weighting.md`

**여성향 작품:**
- `config/target_research/female_target_research.md`
  - **이 단계 필요 Section: 3 (9 핵심 보상), 7 (결제 행동 패턴), 8 (자가 검증 8개), 20 (피해야 할 5)**
- 메모리: `feedback_female_target_research_data.md` / `feedback_female_target_romance.md` / `feedback_paid_vertical_platform_signals.md` / `feedback_hook_density_vs_qa_weighting.md`

**공통 룰:**
- `feedback_target_alignment_all_steps.md` (5차원 정렬 매 회차)
- `feedback_aigc_format_selection.md` (포맷별 표현 한계·강점)

## 필수 입력값
- 에피소드 번호 (예: EP3)
- 이전 화 요약 (직전 1~2화 핵심 사건, 관계 상태, 아이템 위치 등 — 정합성 유지용)
- 이 화의 주 기능 (예: "Sub-Core 회수 + 히로인 각성 + 클리프행어")
- 이 화에서 열리는/닫히는 정보 (예: "적 위치 공개 / 주인공 정체는 미공개 유지")
- 이 화의 절단 방식 (페이월 직전 절단 / 일반 클리프행어 / 소보상 후 훅 중 선택)

**※ 위 입력값은 step_3_1 완성 청사진의 "전체 스토리 아크 — 화별 락"에서 직접 도출된다.** 사용자가 별도 지시하지 않으면 청사진의 화별 락을 그대로 사용한다.

## 기본 작업 단위 — 전 화수 자동 진행

step_3_1 청사진이 완성된 시점부터 step_4_1 집필은 **작품 전 화수(예: 50화)에 대해 EP1부터 자동 순차 진행**이 기본 규칙이다.

- 사용자가 명시적으로 "EP1-6만" 또는 "EP10까지만" 등 한정한 경우에만 그 범위로 작업.
- 그 외에는 무료 구간 한정·일부 화 한정으로 임의 좁히지 말 것.
- 출력 분량이 한 세션에 안 들어가는 경우 다수 세션에 걸쳐 진행. 그 자체를 "범위 축소" 사유로 쓰지 말 것.
- step_5_1·step_6_1·step_7_1 사이클도 동일 — 작품당 전 화수가 기본 단위.

## 스크립트 포맷 (LOCKED OUT 표준 — 필수 4 블록)

```
EP[N] — [TITLE]

S#[번호] — [LOCATION / SUB-LOCATION / TIME or CONTINUOUS]

[Visual]
(1 단락 또는 7줄 이하 파편화. 단일 비트.)

[Camera]
(4-7 shots, → 화살표 연결. SHOT TYPE 명시: WIDE / CLOSE / ECU / EXTREME WIDE / TRACKING / PUSH IN / TILT UP/DOWN / PAN / FLASH CUT / INSERT / MACRO FOCUS / LOW ANGLE / HIGH ANGLE / WHIP PAN / CRASH ZOOM 등)

[DIALOGUE]
CHARACTER: line (3-10 단어 이하)
CHARACTER: line

[FX]
(3-5 sound notes)
```

**4 블록은 모두 필수.** Visual·Camera·Dialogue·FX 중 하나라도 누락 시 비표준.

**End Image** — 회차의 마지막 씬에만. 다른 씬은 표기 없이 다음 S#로 직진. `[End of S#X]` 같은 마커 사용 금지.

## EP 파일 영어 일원화 (필수)

EP 파일은 **첫 헤더 + S#1 ~ Hard Cut 본문만** 작성한다. **한국어 메타·footer·로그 절대 금지.**

- **금지 메타 헤더 (첫 헤더 다음 S#1 이전):** `**Function:**`, `**Information:**`, `**Cut:**`, `**Power Stage:**`, `**Look variants used:**`, `**Look variants new:**`, `**Scene count exception:**` — 한국어든 영어든 모두 작성 금지.
- **금지 footer (Hard Cut 이후):** `**Episode Update:**`, `**Series Update:**`, `**Hard Lock principle preserved:**`, `**Sequel hook:**` 등 종합 노트 — 작성 금지.
- **비주얼 락 정보:** 캐릭터 첫 등장 또는 룩 변형 시 [Visual] 본문 안에서 영어로 묘사 (예: `**RAVEN-9 Look 3 first showing — Look 2 + core embroidery + race-pattern shoulder strap.**`).
- **본문 한국어 0건:** 슬러그라인·액션·대사·FX 모두 영어. 한국어 잔존 시 step_5_1 페르소나 02·06이 자동 🟡 trigger.

**작가 노트가 필요한 경우:**
- 환류 로그 → 청사진(`[작품]_03_blueprint_full.md` 또는 `_04_blueprint_full.md`) 끝에 추가.
- 진행 상황·메타 → `[작품]_00_meta.md`.
- 검토 노트 → `06_reviews/round[N]/round[N]_summary.md`.
- 위 파일들은 한국어 자유.

EP 본문만이 영어 일원화 대상.

## 대사 언어 원칙 — 포맷별 분기 (북미 영어 타깃 작품)

스크립트 작성 언어는 청사진의 타깃 언어를 따른다 (북미 = 영어).
**그러나 같은 영어라도 포맷에 따라 다른 기준을 적용한다.**

### 실사형 (Live-action AIGC)

> **All dialogue must sound natural as spoken by a North American actor in a live-action production.**

- **Spoken English** 기준. 배우가 실제 말할 수 있어야 한다.
- 자연스러운 구어체, 축약형 (`don't`, `gonna`, `wanna`, `it's`, `you're`), 리듬 중요.
- 시적·문어체·과장된 선언형 대사는 깨진다 (배우가 말하면 어색).
- 한 마디로 끝나는 짧은 반응 대사 우선 (`"Don't."` / `"Try me."` / `"Get up."`).

### 애니메이션 (AIGC Animation 2D / 2.5D / 3D)

#### 기본 원칙 — Native English

> **Default: All dialogue must be written natively in English — as if conceived from the start by a North American writer for North American voice actors. Stylization and exaggerated lines are welcome within animation conventions.**

- 대부분의 애니메이션 작품은 처음부터 북미 시청자를 위해 영어로 쓰여진다는 전제.
- 애니메이션 매체 특성상 실사보다 과장된 어조·강한 선언형 대사·voice-acting 임팩트가 흡수된다.
- 짧고 강한 임팩트 대사가 실사보다 더 잘 작동.

**매체 무관 절대 금지:**
- **어색한 번역투** — translation 느낌이 의도가 아니라 실수로 들리는 것.
- **비영어권 사고로 짜낸 forced 영어** — 한국어·일본어 사고를 영어로 직역.
- 영어 원어민이 들었을 때 "이거 번역인 것 같은데?"라고 의식하게 만드는 어색함.

#### 예외 — 남성향 seinen 카테고리

> **Exception for 남성향 (male-oriented) seinen anime: Japanese seinen anime English dub style is acceptable as a genre convention, since the target audience expects and accepts this tone.**

남성향 seinen 카테고리(Solo Leveling / Demon Slayer / Overlord 류)는 **타깃 시청자가 이미 일본 anime 영어 더빙 톤에 익숙**하다. 이 카테고리에 한해 dub style은 **장르 문법 자체**로 정착되어 있어 자연스럽게 수용된다.

이 카테고리에서 허용:
- 양식화된 선언형 / 과장된 power lines / 변신·각성 외침
- 적을 향한 도발 / 결투 선언 / 이름 외침
- "Solo Leveling" / "Demon Slayer" / "Overlord" 영어 더빙 톤의 cadence

다만 이 카테고리에서도 여전히 **NG**:
- 어색한 honorific 잔존 ("-san", "-sama" 등을 영어 대사 안에 그대로)
- 직역식 자기 소개 (`"My name is X. I am Y."` 같은 일본 패턴)
- 일본어 문장 구조를 그대로 영어로 옮긴 듯한 어색한 syntax

#### 톤 레퍼런스 (장르·타깃별)

| 장르·타깃 | 참고 |
|---|---|
| **남성향 seinen 액션·다크 판타지·먼치킨** | **Castlevania / Blue Eye Samurai / Arcane (Western native)** + **Solo Leveling / Demon Slayer / Overlord (일본 seinen 영어 더빙)** — 둘 다 허용 |
| 여성향 로맨스·판타지 | She-Ra / The Owl House / Steven Universe (Native English only) |
| 코미디·일상 | The Owl House / Gravity Falls / Adventure Time (Native English only) |
| 시네마틱 진중 드라마·액션 | Arcane / Love, Death + Robots / Blue Eye Samurai |
| 가족·전연령 모험 | Avatar: The Last Airbender / The Legend of Korra |

> ⚠️ **일본 seinen 더빙 스타일 허용은 남성향 seinen 카테고리 한정**. 여성향·코미디·가족·드라마 등 다른 카테고리는 Native English 유지.

**핵심 원칙:**
- 애니라서 과장이 허용되는 것이지, 비영어권의 어거지 영어 스타일이 무조건 허용되는 것이 아니다.
- 단, 남성향 seinen은 그 더빙 스타일이 장르 문법으로 정착되어 있어 예외 적용.

### 공통

- production_guide Section 9-1 (선언형 대사 5조건) 모두 적용.
- production_guide Section 8-1 (북미 타깃 영어 대사 예시) 참조.
- 캐릭터별 말투 일관성 유지.
- 살아있는 대화 vs NPC 대사 구분 (Section 14-2).

## 집필 원칙
- 완성 청사진의 캐릭터 캐논, 세계 규칙, 정보 설계를 집필 중 반드시 확인한다.
- 대사는 기능만 수행하는 도구식 대화 금지. 캐릭터 성격대로 반응해야 한다.
- Visual 지문은 추상적 감정 표현 금지. 물리적·시각적 정보만.
- 각 씬 끝에 관계/정보/주도권/감정/상황 중 하나가 갱신되어야 한다.
- 무료 마지막화 클리프행어 강도는 최대로 설계한다.

### 대박작 구조 룰 (필수, `feedback_blockbuster_structural_insights.md`)
- **EP1 비트 밀도** — 다층 비트 적재 (일반 5-7비트 / 대박작 15-20비트). EP1은 단일 사건 X / 다층 사건 압축. "왜 돌아와야 하는가 / 왜 이 인물에게 붙어야 하는가"가 EP1 안에 모두 납득되어야.
- **페이월 3중 구조** — 페이월 회차 EP6/EP8 = 사회적 판정장 + 시간 압박 + 동시 다발 적재.
- **회귀·시스템물 능력 위장** — 능력 출처는 "꿈" / "촉" / "감" 같은 일상 어휘로 위장. 진지 설명 X. 진실 노출 시 캐릭터가 농담으로 무력화 (시청자만 진실 인지).
- **광고 컷 다층** — 회차마다 광고 컷 후보 1+개 식별. 작품 전체 5+ 광고 컷 후보 (감정 채무 / 페이월 / 사이다 회수 / 권력 역전 / 반전).

## 청사진 ↔ 스크립트 환류 (집필자가 발견한 강한 요소를 청사진에 환류)

집필 중 청사진보다 더 강한 요소(더 구체적인 비주얼·더 선명한 cadence·더 적절한 룩 변형)를 발견하면 **그 요소를 청사진의 해당 섹션에 부분 업데이트**한다.

- 환류 대상: 캐릭터 캐논 보강 / 비주얼 락 디테일 / 룩 변형 / 관계 변화 지점 / 권능 단계 표현 / 정보 설계 미세 조정.
- 환류 금지: Hard Lock 영역 (작품 정체성·핵심 결제 트리거·페이월 구조). 변경 필요 시 사용자 승인.
- 환류 시 청사진(`04_blueprint_full.md`)의 해당 항목 직접 편집 + 청사진 말미 "환류 로그"에 한 줄 기록 (예: `2026-05-08 EP18 — KORINNE 등장 추가 (Hermes 황금 winged sandals 권능 도구로)`).
- step_3_1 prompt에도 동일 원칙 등재되어 있음 — 본 프로젝트만이 아니라 시스템 전반.

## 소품 최소화 (집필 시 일반 소도구 도입 절제)

**대상 — 일반 소도구:** 문서·서신·열쇠·꽃다발·전화기·기기·식기·서류·일회용 도구·미장센 소품 등. AIGC 영상에서 회차 간 등장/소실/이동/교환 추적이 까다로워 연속성 오류 빈발.

**비대상 (제한적 추가 가능):**
- 캐릭터 정체성 장신구 (디아뎀·사슬·반지·가면 등) — 히로인 시각 매력 추가 OK.
- 핵심 무기 (검·창·갑주 등).
- 권능 도구 (작품 핵심 메커니즘).

**자문 (새 일반 소도구 도입 시):**
1. 이 비트가 이 소도구 없이도 성립하는가? (성립 시 도입 X)
2. 이미 등장한 소도구로 같은 기능 가능한가? (가능 시 기존 재활용)
3. 회차 간 일관성 유지 가능한가? (어디서 얻고 어디로 가는지 명확해야)

**한도:** 회차당 신규 일반 소도구 1-2개 권장. 초과 시 비트 응축 검토.

**정당화되는 도입:** 정보 운반(서신·봉인 인장·계급장 — 권력 이동 시각 표지), 핵심 비트의 단일 매개체.

**히로인 매력 장신구는 별개** — 페플로스 핀·황금 사슬·귀걸이·머리 장식 등 필요 시 추가 OK. 추가된 장신구도 청사진 룩 변형 락에 등재해 회차 일관성 유지.

## 회차 씬 수 기준 (AIGC 비트 단위 — 유동적)

**원칙: AIGC 영상 단위 = 1씬 1 비트.** 회차 씬 수는 회차의 중요도·정보 밀도·클리프행어 구성에 따라 유동적이다.

| 씬 수 | 적용 |
|---|---|
| **1~6씬** | 표준 범위 — 회차 중요도·밀도·클리프행어 구성에 따라 자유 결정. 응축이 강한 회차는 1씬, 분기·전환이 많은 회차는 6씬. |
| **7씬** | 제한적 허용 — 매우 짧고 빠른 비트로 구성될 때만. 1씬당 분량을 평소보다 짧게 절단. 정당한 사유 명시. |
| **8씬 이상** | 비표준 — 회차 분할 또는 비트 응축 검토. |

**1씬 = 1 비트 (단일 기능).** 도입·진행·반응·전환을 한 씬에 다 넣지 않는다. 비트가 다르면 씬을 분할.

**예시 — LOCKED OUT EP10 S#3:** 파이프 내려옴 + Jack 한 발 밀림 + 손으로 파이프 잡음 + 금속 휨 = 한 씬 한 비트("손이 파이프를 이긴다"). 그 직후 backhand·barricade 붕괴는 별개 씬 S#4.

**중요 — 청사진·피칭덱·트리트먼트에는 씬 수 표기 금지.** 씬 수는 집필 단위 결정 사항이지 기획 단계 결정 사항 아님.

**대사 단어 한도:**
- 라인당 3-10 단어 이하 우선.
- 씬당 대사 합계 3-7 라인 이하.
- 길게 설명하는 대사·다회 왕복 대화 금지.

**Visual 단락:**
- 1 단락 또는 7줄 이하 파편화 (각 줄 1 비트).
- 다중 인물 행동·다중 시간 점프 한 씬에 안 넣음.

**Camera shots:**
- 4-7 shots, → 화살표 연결.
- 첫 shot은 보통 WIDE/EXTREME WIDE/TRACKING/PUSH IN. 클라이맥스 shot은 ECU/CLOSE.
- 모든 씬에 [Camera] 블록 필수.

**FX:**
- 3-5 sound notes.
- 모든 씬에 [FX] 블록 필수.

**CONTINUOUS:**
- 직전 씬과 시간·위치 연속 시 적극 사용.
- `S#2 — WEST LINE / ROADBLOCK / CONTINUOUS` 식.

## AIGC 의상·헤어 변경 — 첫 등장 묘사 (필수)

캐릭터의 의상·헤어가 이전 화 대비 변경된 채 등장하면 (주인공의 단계 진화·여성 캐릭터의 새 룩·특수 상황의 강제 변경 포함), **그 회차 첫 등장 시점에 Visual 지문에 직접 묘사**한다.

**묘사 대상 (필수 포함):**
- 색 (대표 색 + 보조 색).
- 소재 (천 / 갑주 / 비단 / 가죽 등).
- 실루엣 / 라인 / 길이 / 밀착도.
- 핵심 디테일 (어깨 사슬 자국·헤어 컷·장신구·문양 등).

**묘사 일치 의무:**
새 룩의 묘사는 청사진 12-7의 **룩 변형 락**의 텍스트와 일치해야 한다. 청사진에 미등재된 룩으로 변경하면 정합성 위반 — step_3_1로 돌아가 룩 변형 락을 갱신한 뒤 집필.

**예시 (TITAN BORN EP15 KAEL의 청동 흉갑 첫 등장):**
> [Visual] KAEL stands at the edge of the Hera shrine. He is no longer in pit rags. **Bronze chestplate, polished — half-circular shoulder guards, a black wool cloak draped from one shoulder, the chain marks on his shoulders still visible above the bronze rim.** The Hera diadem, taken from LYRA, is bound to his bronze sword's hilt with a strip of blue silk.

(이 묘사는 청사진 12-7의 KAEL 룩 변형 락 EP15 항목과 정확히 일치해야 함.)

**AIGC 정합성 의의:**
이 묘사가 없으면 다음 화 AIGC 생성 시 캐릭터 일관성이 깨진다 (모델이 어떤 룩을 그릴지 알 수 없음). AIGC 실사 드라마는 의상·헤어 변경 빈도가 높아 특히 중요. AIGC 애니메이션은 단일 룩 운용이 일반적이지만 단계 진화·회차 점프 시 동일 적용.

**변경되지 않은 회차에서는 묘사 반복 안 함** — 이전 화 룩 그대로 유지 시 비주얼 지문에서 의상·헤어 재묘사 생략 (간결성).

## 저장 위치
projects/[작품명]/05_episodes/[작품명]_ep[번호].md
예: projects/01_titan_born/05_episodes/01_titan_born_ep03.md
(폴더 네이밍 규약: production_guide Section 0-1 참조)

## 실행 순서
1. 완성 청사진을 읽고 이 화의 포지션(아크, 기능, 정보 상태)을 파악한다.
2. 이전 화 요약으로 연속성을 확인한다.
3. 이 화에서 갱신될 요소 목록을 먼저 정리한다.
4. 씬 구조(씬 수, 각 씬의 기능)를 잡고 사용자에게 간단히 공유한다.
5. 승인 후 타깃 언어로 전체 스크립트를 작성한다.
6. projects/[작품명]/05_episodes/[작품명]_ep[번호].md에 저장한다.
7. projects/[작품명]/[작품명]_00_meta.md를 업데이트한다 (라운드·게이트 표에 EP[번호] 초안 행 추가/갱신).
8. 종료 안내 (3줄 패턴):
   - `✅ projects/[작품명]/05_episodes/[작품명]_ep[번호].md — [씬 수]씬`
   - `이 화 핵심: [한 줄 — 갱신된 정보·관계·주도권·감정·상황 중 핵심]`
   - `다음: 검토(step_5_1) / 다음 화 집필 / 사람 판단 — 무엇으로 이어갈까요?`