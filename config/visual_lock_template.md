# 캐릭터 비주얼 락 템플릿 (v2 / 2026-05-27 개정)

**🎯 본질 (2026-05-15 정정 · 2026-05-27 강화):** 비주얼 락 = **AIGC 어셋 생성 고정용 DB.** 대본 `[VISUAL/ACTION]` · `[KEY CAMERA]`는 어떤 어셋을 호출하는지 식별 가능해야 한다. 첫 의상·변경·재착용 시 묘사 필수 / 직전과 동일 = 비묘사 (반복 묘사 = 산업 비용·집중 분산). 상세: 메모리 `feedback_visual_lock_system.md`.

이 템플릿은 주요 캐릭터 한 명의 비주얼을 잠그기 위한 기본 양식이다.
**핵심 필수 항목 = 1·1-5·2·3-1·5·6·8-2·9.** (3·4·7은 작품·캐릭터에 필요 시만.)
판타지·로맨타지·드래곤·신화·마법·왕실 장르에서는 **7-1도 필수**로 본다.
다크 로맨스·로맨타지·다크 판타지에서 키스·내밀 접촉 신이 있으면 **7-2도 필수**.

원칙:

* 한 컷에서 다른 캐릭터와 구분되어야 한다.
* 미모는 추상적으로 쓰지 않는다. 화면에 보이는 얼굴형, 눈매, 헤어, 피부 질감, 실루엣, 의상, 소재로 고정한다.
* 모든 항목을 억지로 채울 필요는 없다.
* 무기 / 장비 / 특수 소품은 작품과 캐릭터에 필요한 경우에만 작성한다.
* 빈 칸은 미정 상태로 남겨두고, 확정된 것만 채운다.
* **AIGC 어셋 생성에 필요한 정보가 모두 담겨야 한다** (어셋 호출 시 식별 가능).

---

## 1. 기본 정보

* 캐릭터명:
* 역할 / 포지션:
* 작품 내 기능:

---

## 1-5. AIGC Asset Call Signature (필수 — 2026-05-27 신설)

> 한 줄 callable signature. 어셋 호출 시 이 한 줄로 캐릭터가 식별되어야 한다.
> 형식: `[성별·연령대], [얼굴 코어 2-3 항], [헤어 코어 1-2 항], [의상 코어 1-2 항], [소품/표지 1 항].`

* AIGC Asset Call Signature (한 줄):
  * 예: `Late-20s woman, fine V-jaw with cool moss-green eyes and porcelain skin, ink-black soft straight hair to mid-back, dark slate slip dress, mother's diamond necklace.`
  * 예: `Mid-30s man, slate-grey eyes and a faint vertical scar above the right brow, short ink-black hair swept off the forehead, charcoal three-piece suit, silver tie bar.`
  * 예: `Early-30s man, granite jaw under deep grey eyes with a permanent slight squint, cropped ink-black hair, midnight-blue investigator coat, leather camera bag.`

---

## 2. 인상 / 신체

* 얼굴 인상:
* 나이대 인상:
* 체형:
* 실루엣:
* 신체 우세 포인트:

---

## 3. 얼굴 디테일

* 얼굴형:
* 눈매:
* 눈 (색 / 형태):
* 입가:
* 피부 질감:

---

## 3-1. Voice / 음색 (필수 — 2026-05-16 / 2026-05-27 강화)

> **주역 (주인공·여주·특히 남주) 한 줄 voice 설계.** 복잡 X. 타깃·캐릭터·장르 적합.
> 🆕 **no-theater-tone 5 차원 자가 검사 의무** (`memory/feedback_no_theater_tone.md`):
>  ① 연극톤 X ② 시적 X ③ 대구·운율·낭송형 X ④ 1-3 단어 단독 턴 3턴 이상 핑퐁 X ⑤ short 추구 X / 인간 호흡 묶음.
> 상세: 메모리 `feedback_character_voice_one_line.md`.

* Voice / 음색 (한 줄):
  * 예: `Low, grave baritone — full sentences when calm, half-sentences when furious; no recitation cadence.`
  * 예: `Warm and measured — speaks in natural paragraphs, not staccato; sarcasm sits inside long lines, not as one-word punchlines.`
  * 예: `Quiet alto with a flat plate — clipped only at moments of physical decision; otherwise gives the listener a full breath.`

* Voice 금지 패턴 (캐릭터별 명시):
  * 예: 작가가 정리한 punchline·tri-colon anaphora·mirror echo·`A. B. C.` 시적 fragment·정전 쓰레기 형태 (`One X. One Y. My Z. Now I N. The A was not B. ...`) 0건.

---

## 4. 헤어

* 헤어 길이 / 컷:
* 헤어 색:
* 헤어 질감 / 스타일링:

---

## 5. 컬러 / 소재 캐논

* 대표 색:
* 보조 색:
* 대표 소재:
* 소재 질감 / 톤:

---

## 6. 의상

* 의상 구조:
* 의상 우세 포인트:
* 의상 디테일 (실루엣 / 라인 / 밀착도):
* 액세서리 / 장신구:

**대본 묘사 룰 (필수):**
- 첫 등장 시 의상 디테일 명시 (Visual 지문)
- 직전 컷과 동일 시 = 비묘사 (산업 비용·집중 분산 방지)
- 변형 첫 등장 시 = 8-2 변형 락 텍스트와 일치하여 묘사
- 같은 EP 내 동일 변형 반복 묘사 = 금지 (정보 0건)

---

## 7. 장비 / 무기 / 소품

(필요한 경우에만 작성)

* 장비:
* 무기:
* 주요 소품:
* 장비·무기·소품의 시각적 우세 포인트:

### 🆕 소품 plot 의존 금지 (2026-05-27 신설)

> 사용자 명시: *"어지간하면 '소품'에 목매여 전개하지마라."* 상세: `memory/feedback_vertical_protagonist_voice_ownership.md` 룰 5.

* **금지:** 동일 prop이 3+ 장면에 plot driver·reveal trigger·관계 변환 anchor·갈등 동력으로 반복 등장 (motif 욕심)
* **허용:** 단발 증표 / 기능적 prop / Paywall hook 1회 / Setup-5화 룰 정합 payoff 1회
* **Hard Lock plot prop 예외:** 작품 정체성을 지탱하는 단 1-2개 핵심 소품 (예: SHE STOLE MY FACE 어머니 목걸이 = Identity 단서)은 반복 등장 허용·단 reveal trigger는 캐릭터 dialogue/VO로

* 본 캐릭터의 핵심 plot prop 1-2개 (그 외 prop = 단발 증표):
* Prop이 reveal trigger인가 dialogue·VO trigger인가:

---

## 7-1. 판타지 대형 시각 보상 락 (필요 시 필수)

판타지·로맨타지·다크 판타지·신화·수인·드래곤·마법·던전·왕실 작품은 캐릭터 룩만 잠그면 부족하다. 현대물에서는 줄 수 없는 대형 화면 보상이 작품 초반부터 식별 가능해야 한다.

* 핵심 대형 공간 (성채 / 신전 / 거대한 문 / 왕좌 / 지하 의식장 / 계단 / 하늘 등):
* 핵심 비인간 존재 (드래곤 / 괴물 / 변신체 / 신화적 존재 / 군대 등):
* 핵심 VFX 규칙 (불 / 얼음 / 저주 / 마법진 / 의식 / 날개 / 세계 위계 표현 등):
* 첫 1-3화 또는 무료 초반에서 반드시 보여줄 판타지 스케일 컷:
* 인물 관계·권력 변화와 직접 연결되는 방식:
* 금지할 축소 방향 (예: 소품·seal·문장 반응만으로 판타지 약속을 처리):

---

## 🆕 7-2. Intimacy KEY CAMERA 락 (키스·내밀 접촉·sex 작품·2026-05-27 신설)

> 키스·내밀 접촉 신·sex 신이 있는 작품은 KEY CAMERA shot size를 미리 락한다.
> 상세: `memory/feedback_t4_sex_scene_standard.md` (T4 sex scene 가이드라인).
> 본 작품 수위 표기: T0 (touch X) / T1 (touch·dressed) / T2 (kiss·dressed) / T3 (kiss·undressed) / T4 (sex direct) / T5 (sex extended).

* 본 작품 최대 수위 (T0-T5):
* 적용 캐릭터 페어:

### Shot size 카논 (인티머시 신·필수)

각 인티머시 신마다 `[KEY CAMERA]` 블록 안에 명시:
- **ECU (Extreme Close-Up):** 입술·눈·손·목 등 부위 < 5cm
- **CU (Close-Up):** 얼굴 어깨 위·손 hand
- **MCU (Medium Close-Up):** 가슴 위
- **OTS (Over-The-Shoulder):** 한 캐릭터 어깨 너머
- **High Angle / Low Angle:** 권력 dynamic 표현
- **POV:** 1인칭 시선 (선택적)

### 🆕 Female gaze 룰 (다크 로맨스·여성향 강제·`memory/feedback_female_gaze_camera_polish.md`)

* ❌ 부위 순회 (thigh → ribs → throat → collarbone 류 male gaze tracking) 금지
* ✅ 통제 상실·forearm weight·breath·firelight·sheet·hand·choice 우선
* ✅ 주인공 agency·시선 우선

### 🆕 No metaphor dodging (T2+ 강제·`memory/feedback_no_theater_tone.md` · `feedback_vertical_no_metaphor_dodging.md`)

* `They kiss.` / `He kisses her. Deep, open mouth. Tongues slide.` / `They have sex.` 직설 선언
* 은유로 사건 본체 대신 X (반응 보조 OK)

---

## 8. 공간별 룩

(작품 내에서 캐릭터의 룩이 공간/상황별로 달라지는 경우)

* 공간 / 상황 1:
  * 변화 포인트:
* 공간 / 상황 2:
  * 변화 포인트:

---

## 8-2. 룩 변형 락 (Look Variants) — AIGC 정합성 필수

작품 진행 중 캐릭터의 의상·헤어가 변경되는 모든 단계를 미리 락한다.
AIGC 실사 드라마: 의상·헤어 변경 빈도가 높아 필수.
AIGC 애니메이션: 일반적으로 단일 룩이지만 단계 진화·특수 상황 시 락 필요.

각 변형마다 다음 5요소를 명시:

* **변형 1 — [이름·식별자]**
  * 등장 회차 / 시점 (예: EP15부터 / Arc 2 진입 시점부터):
  * 색 (대표 + 보조):
  * 소재:
  * 실루엣 / 라인 / 길이 / 밀착도:
  * 핵심 디테일 (장신구·문양·흉터·사슬 자국 등):
  * 변경 트리거 (어떤 사건으로 룩이 바뀌는가):
  * 이전 변형과의 차이 (한 줄):
  * 🆕 AIGC Asset Call Signature (이 변형 한 줄):

* **변형 2 — [이름·식별자]**
  (동일 양식 반복)

(필요한 만큼 반복)

**대본 일치 의무:**
대본(phase_4)은 새 변형의 첫 등장 시점에 Visual 지문에 직접 묘사하며, 그 묘사는 위 락의 텍스트와 일치해야 한다.

---

## 9. 금지 사항

### 9-1. 디자인·시각 금지

* 금지되는 디자인 방향:
* AIGC 제작 금지 사항:
* 절대 바꾸면 안 되는 핵심 락 (실루엣 / 색 / 소재 등):
* 룩 변형 시에도 절대 바꾸면 안 되는 표지 (예: 어깨 사슬 자국·헤어 색·눈 색):

### 🆕 9-2. Voice·Dialogue 금지 (no-theater-tone 5 차원 자동 적용·2026-05-27 신설)

본 캐릭터에 대해 다음 패턴 자동 금지 (`memory/feedback_no_theater_tone.md`):

* ❌ 시적 cadence·rhyme·작가 punchline
* ❌ 연극톤·셰익스피어식·낭송형
* ❌ Tri-colon anaphora (`A. B. C.` 동일 cadence 3 fragment)
* ❌ Mirror echo (`X. / Y. / X. / Y.` 핑퐁)
* ❌ Parallel structure 시적 (`The X was Y. The X will be Z.`)
* ❌ 정전 쓰레기 형태 (`One X. One Y. My Z. Now I N. The A was not B. The C will not be D.`)
* ❌ 1-3 단어 단독 턴 3턴 이상 연속 (기능 턴 외)
* ❌ 같은 화제 4 턴 이상 짧은 핑퐁

### 🆕 9-3. Prop 의존 금지 (2026-05-27 신설·`memory/feedback_vertical_protagonist_voice_ownership.md` 룰 5)

* ❌ 본 캐릭터의 prop이 3+ 장면에서 motif 반복 (Hard Lock plot prop 1-2개 예외)
* ❌ 본 캐릭터 reveal trigger = prop matching (jaw·tattoo·mark·ring·pin)
* ❌ 본 캐릭터 관계 변환 anchor로 prop 주고받기·떨어뜨림 반복
* ✅ Reveal trigger = 본 캐릭터 또는 상대 캐릭터의 dialogue·VO

---

## 환류 로그

* v1 — 초안.
* v2 (2026-05-27) — no-theater-tone 5 차원 통합 + 1-5 AIGC Asset Call Signature 신설 + 7-2 Intimacy KEY CAMERA 락 신설 + Female gaze·No metaphor dodging 통합 + 9-2 Voice 금지·9-3 Prop 의존 금지 신설.
