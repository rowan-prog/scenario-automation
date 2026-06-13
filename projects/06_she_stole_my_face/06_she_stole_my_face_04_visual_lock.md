# SHE STOLE MY FACE — VISUAL LOCK
**v53 LOCK 기준 · 2026-06-12 갱신**

목적:

- 9:16 vertical 실사형 어셋 생성 기준
- 캐릭터 / 소품 / 배경의 반복 생성용 디자인 락
- 대본 기준 고정 (`07_final/06_she_stole_my_face_FINAL_v53.md` = 현재 정본)
- 프롬프트 원재료로 바로 쓸 수 있게, 명사 / 형태 / 색 / 소재 / 금지사항 중심으로 정리
- 은유적 분위기 설명보다 눈에 보이는 외형 정보 우선

장르: 현대 재벌가 신분도용 복수극 (막장). NA 여성향 25-45. 최대 수위 T3 (sex·undressed — EP38 직접 묘사).

---

## 1. 공통 락

### 문서 언어 원칙

- 비주얼락은 해석문이 아니라 어셋 생성 기준이다.
- 각 항목은 얼굴, 헤어, 피부톤, 체형, 의상, 신발, 악세사리, 소품, 색, 소재를 직접 말한다.
- `미스터리한 분위기`, `진실을 품은 눈빛`, `가면 같은 삶` 같은 추상/은유 문장 금지. (`wear like a costume`·`coat that doesn't fit`·`see the seams` 류 본문에서도 금지.)
- 필요하면 `차가운 회녹색 눈`, `검은 롱스트레이트`, `slate-grey tailored suit`, `gold-diamond pendant`처럼 바로 보이는 말로 쓴다.
- 의상 변화는 완전히 다른 룩일 때만 에피소드 범위를 표시한다. 같은 의상의 찢김 / 젖음 / 피 묻음은 제작 처리로 두고 락 문서에 반복 표기하지 않는다.

### 첫 판매 기능 자막

- 주요 인물 첫 판매 기능 컷에서만 사용
- 형식: `NAME / SELLING TAG` · 2-4 단어 · 흰색 또는 금색 얇은 대문자 · 화면 하단 1/3 안쪽
- 얼굴 / 몸 실루엣 가리지 말 것 · 반복 금지 · 긴 설정 설명 금지 · 행정/제도어 금지
- 태그: `LENA / ERASED HEIRESS`, `MARA / THE FACE THIEF`, `NOAH / THE ONLY ONE WHO KNOWS`, `ETHAN / THE WRONG CHOICE`, `VICTORIA / CROSS MATRIARCH`, `EILEEN / THE PUPPETEER`, `TESSA / THE FRIEND WHO SOLD HER`
- EP01 첫 15초 = `LENA / ERASED HEIRESS` + 클리닉 reveal에서 `MARA / THE FACE THIEF`만 먼저. 나머지는 각자 첫 기능 컷에서 분산.

### 장소 UI / GRAPHIC

- 매우 중요한 장소 첫 등장 때만 사용 · 장소명 짧은 대문자 · 상단 또는 하단 1/3 안쪽
- 인물 얼굴 / 핵심 소품 가리지 말 것 · 모든 씬 반복 금지 · 세계관 설명 subtitle 금지
- 예시: `CROSS MANOR — BALLROOM`, `GLENMOOR CEMETERY`, `BRANDT CLINIC`, `THE GLASS CONSERVATORY`

### 전체 디자인 톤

- 현대 재벌가 · 글로시 프리미엄 부의 미감 (펜트하우스 유리, 대리석, 금, 맞춤 정장, 드레스)
- 실사형 · 최상위 캐스팅 미모
- **막장 멜로 톤** — 고조된 감정, 천박한 빌런, 뻔뻔한 거짓말. 우아한 표면 + 추한 속내.
- ❌ 쿨한 수사물 / 미스터리 / 스릴러 무드 (이 작품은 추리극 아님 — 시청자는 1화부터 다 안다)
- ❌ HBO식 회색 리얼리즘 · 다큐 톤
- ❌ 시대극 / 판타지 / 마법 · ❌ 애니메이션 / 3D 렌더 · ❌ 코스프레 · ❌ 게임 시네마틱
- EP01 콜드오픈 구조: Brandt Clinic 백룸 — 의자에 앉은 Lena(pendant at throat) + 마스크 쓴 어시스턴트(뒤돌아 섬). 마스크 내리는 중 **좌측 귀밑 fresh 곡선 흉터(still pink) ECU = 타이틀 직전 마지막 이미지**. EP01 엔드훅 = 클리닉 미러 월에 비친 두 개의 동일한 얼굴. Mara 얼굴 풀 리빌은 EP01 엔드훅.

### 🔒 동일 얼굴 구별 락 (이 작품 최우선 — AIGC #1 제약)

Lena와 Mara는 **같은 얼굴**(시술로 동일)이다. 매 컷에서 둘이 한눈에 구별돼야 하며, 구별 수단은 다음 5가지뿐이다:

1. **시술 흉터 (Mara 전용)** — 좌측 귀 2cm 아래 곡선 1.5cm + 우측 손목 안쪽 직선 3cm. 평상시 헤어/각도로 가려지고 **근접 증거 컷에서만 노출.** EP01-50 동일 위치 유지 (Hard Lock). EP01-03 = 시술 직후라 fresh·pink / 이후 faint silver line. **의도 노출 3컷 (물증형 보증 — 시청자 전용 plant):** ①EP01 콜드오픈 마스크 내리는 중 흉터 ECU(타이틀 직전 마지막 이미지) ②EP01 엔드훅 — 거울 미소 연습 중 흉터 발견·미소 정지·머리카락 한 가닥으로 가림·미소 재시작 ③EP03 — 대형 생중계 스크린서 바람에 머리 들리자 빠르고 연습된 손길로 귀 가림. (회수 = EP49 — 군중 앞 Mara 자신이 손으로 가리는 순간 포착.)
2. **의상 팔레트** — Lena = 절제된 slate·navy·charcoal·ivory / Mara = 훔친 글로시 룩(navy·cream silk) → 후반 black(난입)·stripped(몰락).
3. **헤어 스타일링** — Lena 낮은 정돈(다운/낮은 묶음/단정 하프업) / Mara 더 윤기·화려한 셋업.
4. **태도·자세** — Lena 정적·자제·곧은 자세 / Mara 카메라 앞 sweet-victim 연기, 단둘이면 천박·비웃음·snarl.
5. **맥락** — 세상이 떠받드는 쪽 = Mara (EP1-48). 목에 pendant 있는 쪽 = Mara (EP1-49).

- ❌ 두 얼굴을 **긴 정적 한 프레임**에 같이 넣어 "어느 쪽이 진짜?"를 시청자가 뜯어보게 만드는 컷 금지 (AIGC 동일인물 일관성 붕괴 위험).
- ✅ OTS · 컷 분리 · 위치 분리 · 한 명씩 close. 같은 프레임이 필요하면 흉터/의상/태도로 즉시 구별되게.
- EP01 SPLIT SCREEN (클리닉 미러 컷): `[SPLIT SCREEN] Top: Mara's face, calm. Bottom: Lena's face going slack. Identical, every angle.` — 이 컷 외 이후 1인 2역 동시 컷은 OTS/위치 분리 원칙 적용.

### 시청자 이해도 락 (뇌-오프)

- 한 컷만 봐도 누가 안 믿기고(Lena), 누가 떠받들리고(Mara), 다음 목표가 뭔지 읽혀야 한다.
- 정보는 말로만 처리하지 않는다: TV 자막(chyron), 폰 피드, 군중 핸드폰, 펜던트 위치, 빈 목, 흉터 반응으로 화면에서 확인.
- 관계 보상은 표정만으로 처리하지 않는다: 손 위치, 옆자리, 공개 선택(Noah가 Lena 막아섬), 목걸이 이동으로 보이게.
- 약한 장면 금지 신호: 예쁜데 뭐가 바뀌었는지 모름 / 대사 없이는 못 알아봄 / 두 얼굴 구별이 한눈에 안 됨.
- 플래시백 / 폰 영상 / TV 재현 컷은 대본 SOURCE 태그 유지 (제작 참조용, 화면 자막 노출 X).

### 얼굴 공통

- 주연 기준 최상위 미모 · 선명한 이마-눈썹뼈-콧대 · 정리된 입술선 · 프리미엄 피부
- 사각턱 금지 · 낮은 콧대 금지 · 평균적 현실 배우 얼굴 금지
- 나이 설정 있는 인물(Victoria·Eileen·Celia)은 개별 락 우선

### 체형 / 비율 공통

- 9:16 전신에서 키·비율 즉시 읽힘 · 긴 목 · 좋은 자세
- Lena/Mara는 동일 체형(시술 표적) · 그 외 여성은 실루엣 서로 다르게
- 땅딸막·짧은 다리·머리 큰 비율 금지

### 의상 공통

- 현대 럭셔리: 맞춤 정장, 실크 블라우스, 이브닝 드레스, 재벌가 패션, 캐시미어 코트
- ❌ 시대극 / 판타지 / 갑주 / 스트리트웨어 / 클럽룩 / 란제리룩

### 대사 cadence 금지 (전 캐릭터 · no-theater-tone)

- ❌ 시적 cadence·rhyme·작가 punchline·연극톤·낭송형
- ❌ Tri-colon anaphora·mirror echo·은유·정전 쓰레기 형태(`One X. One Y. My Z.`)
- ❌ 1-3 단어 단독 턴 3턴 이상 핑퐁 · 같은 화제 4턴 이상 짧은 핑퐁
- ✅ 자연 spoken English 5-15 단어 한 호흡 · 막장 직설 · 빌런은 천박·뻔뻔

### Female gaze / 인티머시 (T3 — EP38 직접 묘사)

- 페어: Lena ↔ Noah (T3). **인티머시 EP = EP15·EP23·EP38·EP45.**
- Lena ↔ Ethan = T1 이하 (사고 전 짧은 손길·이후 0).
- 부위 순회 tracking 금지 · Noah forearm weight·gaze 우선 · Lena의 choice(먼저 손 닿느냐·먼저 올라타느냐) 우선.
- 직설: `They kiss.` / `They have sex.` (은유 우회 X)
- **EP38 KEY CAMERA 락 (추가분):** `[CU] headboard knocking against the wall` / `[ECU] Lena's hands flat on Noah's bare chest, pinning him down` / `[ECU] Noah's palm spread wide between Lena's shoulder blades, pulling her down onto him` — 세 컷 모두 올라타기(Lena on top)·pinning 배치 고정.

### V.O. 더빙 트랙 노트

총 13건. 캐릭터별:
- **Lena V.O. 9건:** EP14(묘지 — `My mother hated lilies`), EP17(갈라 — `She's using my dead mother`), EP31(웨딩 전야 — `The night before she marries Ethan`), EP32(웨딩 당일 — `Today the whole country watches`), EP33(`She's saying my vows`), EP35(`She's not smart`), EP39(`She has my whole life`), EP41(`She took my name`), EP43(`She'll come to wreck it`)
- **전화/장외 음성 (V.O., tone) 10건 별도:** EILEEN 8(EP3×2·20×2·28·30×3 — 전화 지시) · CLIENT 1(EP16) · HELENA 1(EP21 플래시백 음성) — 내면 독백 트랙과 분리 녹음
- **Ethan V.O. 2건:** EP27(`I just checked her out. The stalker.`), EP32(`Her neck was red.`)
- **Mara V.O. 2건:** EP11(`How does she know which wrist?`), EP37(`They believed her. Fine. Watch this.`)
- 더빙: Lena·Ethan·Mara 각 배우 별도 레코딩. Mara V.O.는 내면 독백 — 카메라 sweet-victim 페르소나 아닌 real voice 톤.

---

## 2. 인물별 락

### 2-1. LENA STERLING (주인공·진짜 약혼녀)

**캐릭터 / 디자인 느낌**

- 주인공 · 빼앗긴 진짜 상속녀
- 우아·자제력·관찰력 · 당하되 꺾이지 않음 · 매달림/질질 짜는 피해자 금지
- 후반부 = 수동 피해자 X → 가짜를 카메라 앞에서 깨는 능동 사냥꾼

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 1-1 Public Fiancée | EP01 (사고 전) | navy silk-wool suit, hair down, mother's pendant at throat |
| 1-2 Erased | EP01-08 (사고 후·탈출·잠입) | EP01-04: 병원 IV·붕대·bare neck / EP04-06 Cross Manor 난입~끌려나감: **hospital gown 위에 coat grabbed off café chair · barefoot(맨발 — EP6 'bare heels scraping' 지문 고정)** · rain / EP05-07: low ponytail, charcoal knit + slate coat / **EP08: catering uniform (white) + dark wig + apron** / EP08 S#6: catering jacket ripped at blouse strap ("No purse, no phone, no name") — bare neck EP02-49 유지 |
| 1-3 Infiltrator / Noah base | EP09-45 | restored tailored slate·navy (Noah 제공). 잠입 시: catering apron + pinned wig (EP26·EP28·EP33·EP36 등). bare neck still |
| 1-4 True Bride | EP46-50 | Helena의 ivory silk 웨딩드레스 (no train — EP05 false panel서 회수·Mara 못 찾음) / slim gold band / EP49 pendant back at throat / EP50 pendant at throat |

**상세**

- 나이: **30세** (NEVER late-20s)
- 키/비율: 가는 골격, 긴 목선, 곧은 어깨, 곧게 선 자세
- 헤어: ink-black soft straight hair to mid-back, 정돈 (다운 / 낮은 묶음 / 단정 하프업)
- 눈: 회녹색(moss-green), 차분한 시선
- 얼굴: 갸름한 V형, 도자기 흰 피부 (Mara와 동일 — 시술 표적)
- 몸: 가는 허리, 긴 다리, 절제된 자세
- 의상: slate·navy·charcoal 맞춤 정장 / 실크 / 캐시미어 → EP46+ Helena ivory 실크 가운
- 신발: polished oxfords / low pumps
- 악세사리: 어머니 목걸이 (EP01 착용 → EP01 강탈 → **EP02-48 빈 목** → EP49 회수). 어머니 진주 귀걸이(작은 것).
- 표식: **흉터 없음** (이게 Mara와의 유일한 물리 구분자 — Lena는 흉터가 없다)
- 색: black·navy·slate·charcoal·ivory
- AIGC Call (기본): `30-year-old woman, fine V-jaw, cool moss-green eyes, porcelain skin, ink-black straight hair to mid-back, slate-grey tailored suit, bare neck (no necklace). Calm contained posture. No scar.`
- 금지: 매달림/울음 default · 흉터 추가 금지(Lena엔 없음) · 부위 순회 tracking · 시적/은유 대사 · 자기 연민 monologue

---

### 2-2. MARA VOSS / FAKE LENA (가짜 약혼녀·도둑)

**캐릭터 / 디자인 느낌**

- 신분도용 가해자 · Lena의 20년 친구 · 질투로 얼굴을 훔침 (**이복자매 아님 — 그냥 가짜·도둑**)
- 영리한 체스 플레이어 X → **뻔뻔·천박·멍청.** 카메라 앞 sweet-victim 연기 / 단둘이면 비웃음·자랑·snarl
- 가진 것 다 가졌는데 "내 것 같지 않다"는 공허 · 들킬까 늘 두려움

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 2-1 Imposter Bride | EP01-34 | Lena의 삶을 입음: navy·cream silk, **stolen pendant at throat (EP01-49)**, sweet public mask. **EP02-03 = Lena 약혼 가운 복제본** (Eileen 세단 garment bag → 차 안에서 갈아입음·헤어 미리 매칭). **Helena 다이아 팔찌 = 틀린(좌측) 손목 · EP10-11만 착용** → EP11 이후 영구 미착용(Lena 문자 → Mara 차단 후 팔찌 리사이즈·우측 손목으로 이동·이후 미착용·의상 연속성 락). |
| 2-2 Mrs. Cross | EP35-46 | married polish, blush·cream, wedding ring + stolen pendant, growing hollow/strained under the smile. **EP33 웨딩드레스 = white gown with long lace sleeves down to wrists** (팔뚝 상처 은폐 기능 — 어셋 동기화 필수). |
| 2-3 Fallen | EP47-50 | EP47+ black dress + cameraman (wedding crash) → EP49 pendant peeled off · EP50 alone in a cramped gray room, stripped |

**상세**

- 나이: **30세** (Lena와 동일)
- 얼굴/체형: Lena와 **완전 동일** (시술) — 표정만 다름(계산적·sweet 연기 / 천박)
- 헤어: ink-black straight hair to mid-back (염색·약간 더 윤기), 화려한 셋업
- 눈: 회녹색 (시술로 같은 색)
- **신체 우세 표식 (Mara 전용·Hard Lock):** 좌측 귀 2cm 아래 곡선 흉터 1.5cm (silver line) + 우측 손목 안쪽 직선 흉터 3cm. 평상시 가려지고 근접 증거 컷에서만 노출. EP01-03 fresh·pink → 이후 faint. 의도 노출 3컷(콜드오픈 ECU · EP01 엔드훅 거울 · EP03 스크린 바람) = §1 구별 락 참조.
- 의상: 훔친 navy·cream 실크·재벌가 룩 → EP33 long-lace-sleeve 웨딩드레스 → EP35+ Mrs. Cross 광택 → EP47 black → EP50 stripped
- 악세사리: 빼앗은 어머니 목걸이(EP01-49 착용 → EP49 강제 회수·Lena hand), Helena 다이아 팔찌(좌측 손목 = 틀린 손목 · **EP10-11만** 착용 → EP11 리사이즈 후 우측 손목 1회 post → 이후 미착용)
- 색: navy·cream·blush → black → drained gray
- AIGC Call (기본): `30-year-old woman, identical V-jaw and moss-green eyes to Lena, thin curved scar 2cm below left ear + straight scar on right inner wrist (silver, faint after EP03), ink-black styled hair (more lustrous, elaborate set), navy/cream silk, stolen gold-diamond pendant at throat. Sweet performed face in public, vulgar smirk in private.`
- AIGC Call (EP33 웨딩): add `white lace gown with long lace sleeves covering wrists — scar on right wrist concealed.`
- AIGC Call (EP10-11 팔찌): add `diamond bracelet on the wrong/left wrist` — EP12+ 이후 drop entirely.
- 금지: 흉터 사라짐·위치 이동 · 영리한 침착 빌런 톤 · 동정 가는 퇴장(EP50 = 아무도 없는 회색 방, 구원 X) · 시적/연극 대사

---

### 2-3. NOAH KEENE (새 남주)

**캐릭터 / 디자인 느낌**

- 사설 조사 전문가 · Lena를 믿는 유일한 사람 → 후반 **판을 깔아주는 남자**(자기 결혼식을 Lena가 이기는 방으로 만듦)
- 단순·강함·소유 · 든든한 벽 · 흔들림 없는 확신 (의심 X)
- **EP08: catering event 현장 — dark suit over open collar** (Cross Manor 파티 하객으로 진입 후 Lena 구출)

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 3-1 Investigator | EP04(등장)-45 | midnight-blue coat over dark sweater/knit, dark trousers |
| 3-2 Groom | EP46-50 | charcoal morning suit, gold band |

**상세**

- 나이: 30대 중반 · 키 큰 단단한 체격
- 헤어: cropped ink-black · 눈: deep grey, slight squint, faint laugh line
- 얼굴: granite jaw, 차분
- 의상: midnight-blue investigator coat, dark knit, 고급 수트 → EP46+ charcoal morning suit
- 악세사리: vintage silver wristwatch, leather camera bag (직업 소품 — 증거 엔진 X)
- 색: black·midnight-blue·charcoal
- AIGC Call: `Mid-30s man, granite jaw, deep grey eyes with slight squint, cropped ink-black hair, midnight-blue coat over dark sweater. Calm, immovable.`
- 금지: 시적/연극 대사 · "I know / I saw it" 반복 의존 (중후반엔 행동으로) · Lena를 의심하는 비트(엔진 위반)

---

### 2-4. ETHAN CROSS (약혼남 → 잘못된 선택)

**캐릭터 / 디자인 느낌**

- 재벌 후계 · Lena의 전 약혼남 · **"편한 진실"을 택한 겁쟁이** (추리하는 남자 X, 체면 때문에 가짜 편)
- EP27 V.O. + EP32 V.O. = 내면 의심 암시 (화면 밖 독백 · 행동 없음)
- EP49 Mara에게 등 돌림 · 사과는 짧게·드물게 (매달림 X)

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 4-1 Cross Heir | EP01-50 | charcoal three-piece suit, silver tie bar / platinum band (EP34 결혼 후 wedding ring) |

**상세**

- 나이: 30대 초반 · 큰 키 · 정장 어울리는 어깨
- 헤어: short ink-black swept back · 눈: deep grey · 우측 눈썹 위 얇은 흉터
- 의상: charcoal/navy three-piece, 실크 타이, Patek 시계
- 색: charcoal·navy·silver
- AIGC Call: `Early-30s man, square jaw, deep grey eyes, thin scar above right brow, short ink-black hair swept back, charcoal three-piece suit, Patek watch.`
- 금지: 후회로 매달리는 처량함(Lena 거부) · 한 단어 사과 핑퐁 · 영리한 추리 톤

---

### 2-5. VICTORIA CROSS (크로스 가문 여주인)

**캐릭터 / 디자인 느낌**

- 크로스 가문 매트리아르크 · 빌런 · **품격 악녀 X → 상류층 권위로 막말** ("Get that thing away from my son")
- 진실: "몰랐다" 아닌 **"의심했지만 가문 지키려 외면"**

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 5-1 Matriarch | EP01-50 | charcoal Chanel-cut tweed suit, baroque pearl choker + earrings |

**상세**

- 나이: 50대 후반 · 우아한 자세
- 헤어: silver-streaked dark hair, French twist · 눈: pale grey, 바깥쪽 처진
- 의상: 어두운 트위드·실크 정장, 가문 진주·다이아
- 색: charcoal·dove grey·pearl
- AIGC Call: `Late-50s woman, sharp jaw, pale-grey eyes, silver-streaked dark hair in French twist, charcoal tweed suit, baroque pearl choker.`
- 금지: 의식문/판결문 cadence · tri-colon · 따뜻한 할머니 톤

---

### 2-6. EILEEN VOSS (Mara의 모친·배후)

**캐릭터 / 디자인 느낌**

- Mara의 실제 엄마 · 딸에게 가짜 삶을 계속 우겨넣는 독한 엄마 · 큰 설계자 X
- EP39 Mara 손절·퇴장 · EP48 Noah에게 끌려와 clinic intake photo 목격·폭로 완성
- 글램 없음 (떠받들리는 건 Mara뿐)

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 6-1 Puppeteer | EP02 (물리 등장) · EP36·EP39 (물리 등장) · EP48-49 (Noah에 끌려옴) · EP20·EP28·EP30 (전화 음성만·비등장) | plain dark coat, hard practical look, no luxury |

**상세**

- 나이: 50대 후반 · 단단·실용
- 헤어: dull dark hair pulled back, 흰머리 약간 · 눈: hard
- 의상: 어두운 실용 코트·평범한 정장 (재벌 글램 X — 그녀는 바깥 사람)
- 색: dull dark·grey
- AIGC Call: `Late-50s hard-faced woman, dark hair pulled back, plain dark coat, no jewelry. Cold practical.`
- 금지: 우아한 상류층 룩 · 동정 가는 모성

---

### 2-7. TESSA HALE (배신한 친구)

**캐릭터 / 디자인 느낌**

- Lena의 친구·조수 · 도박 부채로 Mara에 Lena 일정 넘김 · EP06 자백(Lena가 Mara의 약점=무기를 캐냄) · EP11 TV 배신
- 복잡한 죄책감 X → 돈 받고 울며 배신

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 7-1 The Friend | EP01·EP06·EP11 (+EP50 = EP11 토크쇼 클립 재생만·신규 렌더 불필요) | camel cardigan over cream camisole, soft casual / EP06 mascara-wrecked |

**상세**

- 나이: 20대 후반 · 보통 체격
- 헤어: shoulder-length auburn waves, copper highlights · 눈: warm hazel · 우측 입가 작은 점
- 의상: 부드러운 캐주얼 · EP06 흐트러진 모습
- 색: camel·cream·auburn
- AIGC Call: `Late-20s woman, oval face, warm hazel eyes, mole above right lip, shoulder-length auburn waves, camel cardigan over cream camisole.`
- 금지: EP12 이후 등장 비중 확대 · 한 단어 사과 핑퐁

---

### 2-8. DR. CELIA BRANDT (클리닉 의사·협력자)

**캐릭터 / 디자인 느낌**

- 미용 클리닉 의사 · Mara 시술 집도·협력자 · EP01 swap 현장
- 수술 마스크 = EP01-02 클리닉 씬 전용 소품 (그 외 화수 마스크 소품 없음)

**디자인룩**

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 8-1 Clinic Doctor | EP01 (+짧은 후속) | white medical coat over slate blouse |

**상세**

- 나이: 40대 · 마른 체형
- 헤어: short caramel bob · 눈: hazel behind thin gold-rim glasses
- 의상: 흰 가운·짙은 평상복 · 가슴 포켓 silver pen
- 색: white·slate
- AIGC Call: `Early-40s woman, narrow oval face, hazel eyes, thin gold-rim glasses, short caramel bob, white coat over slate blouse.`
- 금지: 의학 용어 dump · 영리한 공범 톤 · 클리닉 씬 외 마스크 소품 등장

---

### 2-9. 회귀 단역 (연속성-필수 · 동일 배우 유지)

- **THE CEMETERY REPORTER** (젊은 여기자) — EP14·18·19·47·49. 20대 후반, press lanyard·소형 카메라, 평범한 정장 코트. 군중과 달리 *촬영 안 하고 관찰*(EP14) → EP18 Mara snarl 촬영 → EP19 클립 게시(소수 의심·회수불가) → **EP47 Lena 결혼식 하객석**(EP14 회수·촬영 X) → EP49 그 클립을 방에 틂. 동일 배우 5회. (게시한 클립 자체는 EP30·35서 stitched/split-screen으로 자라며 화면 등장 — 기자는 비등장.)
- **THE WOMAN IN PEARLS** (Helena의 오랜 친구) — EP26·47·49. 60대, baroque 진주 목걸이·이브닝 가운, 품위. EP26 게이트서 사적 고백·샤워 일찍 퇴장 → **EP47 Lena 결혼식 신부측 하객석** → EP49 군중서 *선두로* Lena 곁. 동일 배우 3회.
- **NOAH'S AUNT** (Noah 가족 노부인) — EP46만·1회. 브라이덜 스위트서 Lena 베일 고정·신부측 유일 가족. 재등장 불요.
- **MARA'S PRESS CONTACT** — 음성/오프스크린 단역(EP14 묘지 연출 지시 전화·EP45 폰 화면 번호). 렌더 불필요(폰 화면만).
- **THE TWO WOMEN AT THE TV STUDIO** (EP12·20-30대·커피) — Lena를 *콘텐츠*로 소비하며 촬영. 1회·재등장 불요.

---

## 3. 소품별 락 — 생성용 표식, 서사 엔진 아님

원칙: **소품은 캐릭터 행동·관계·정체의 표식이지, 장면을 해결하거나 이야기를 끌지 않는다. 진실은 소품이 아니라 가짜의 자멸(자백)로 밝혀진다.**

진행 중심: Lena의 능동 선택, Mara의 뻔뻔/멍청, 세상의 외면, Noah의 공개 선택.

### 핵심 표식 소품 3종 상태 추적

| 소품 | 디자인 | 상태 추적 | 룰 |
|---|---|---|---|
| **어머니 목걸이 (MOTHER'S PENDANT)** | gold·diamond, 안쪽 라틴 각인 **`LUMEN MEUM`** ("my light") | EP01 Lena 착용 → EP01 강탈 → Mara 목 EP01-48 → **EP49 Lena 손으로 회수**(unclasps from Mara's throat) → EP49-50 Lena 목 | **감정·정체성 표식** (Hard Lock 예외). Reveal trigger 아님. 각인 = Lena만 아는 것 / Mara는 모름(멍청함의 바늘). **각인 물증 시퀀스 (EP01-03·시청자 전용):** EP01 묘지 — Lena 엄지가 *안 보고도* 각인 찾음 → EP02 세단 — Eileen "What does it say inside?" / Mara "Something in Latin. Who cares." → EP03 Eileen 테스트 / Mara 회피. (회수 = EP14·19·48 코미디·EP49 공개선언.) |
| **시술 흉터 (SURGICAL SCAR)** | 좌측 귀 2cm 아래 곡선 1.5cm + 우측 손목 안쪽 직선 3cm | EP01-03 fresh·pink → 이후 faint silver line. 분장 고정 = EP01-50 동일 위치 (Hard Lock). | Mara 전용 · 두 얼굴의 **유일한 물리 구분자** · 근접 confirmation 컷만, 세상 뒤집는 trigger 아님(자백이 먼저). 의도 노출 3컷(콜드오픈 ECU·EP01 엔드훅 거울·EP03 스크린 바람) = §1 참조. |
| **Helena 다이아 팔찌** | diamond bracelet, clasp = **우측 손목 전용**(Helena 좌측 손목 부러진 적 — 헬렌 좌완 clasp 안 닫힘) | EP10-11: Mara 좌측(틀린) 손목 착용 → EP11 Lena 문자 후 Mara 차단·**리사이즈** → Mara 우측 손목으로 이동(1회 포스트) → **EP12+ 영구 미착용** (의상 연속성 락). 소품 2가지 상태 필요: ①좌측(wrong wrist — EP10-11) ②우측 리사이즈 후 (EP11 post — 1컷). | 증거 prop 아님 — Lena+시청자만 아는 확인. |

### 폐기된 소품 (이전 설계 잔재 — 사용 금지)

- ❌ CCTV 사고 영상 / 프레임 분석 · ❌ 삭제 예약표 · ❌ Tessa 서명 증거 · ❌ MARA VOSS 본명 파일
- ❌ 브라이덜룸 카메라 → 대형스크린 연결 (진실-공개 장치) — 전부 제거됨. 진실은 EP48 Mara 자백+Eileen 폭로.

### EP48 특수 소품

- **클리닉 intake photo (Mara의 수술 전 얼굴):** Noah 폰 화면으로만 노출. 장내 카메라 차단 연출 — `[ECU] The phone screen, shielded from the room's lenses — a clinic intake photo: Mara's old face, the before-face, clipped to a surgery consent form.` 별도 분장/배우 또는 합성 어셋 필요. 실물 prop 화면 단독 노출.

### 화면 증거 (소품 아닌 UI)

- TV chyron(`MR. & MRS. CROSS`·`STALKER INCIDENT`·`SHE FINALLY SAID IT HERSELF`), 폰 피드/댓글, 군중 핸드폰, 자막 reveal — 9:16 모바일에서 즉시 읽히게.
- **The doubter-clip account (회수불가 승점 스레드):** 기자가 게시한 작은 계정(EP19). snarl 클립 → EP30 stitched(snarl+묘지+"screams") 댓글 climb → EP35 split-screen(swim vs scared-of-water) → EP49 방에서 재생. 매번 *small, won't come down* = 화면에 폰 피드/댓글/follower count로.
- **모닝쇼 red-light tell (EP09·16·39·42):** off-air = Mara 무표정/지루 → red light pop on 그 프레임에 sweet-tearful 전환. 화면 연출 device.

---

## 4. 대공간별 락

세부 방 이름보다 반복 출현하는 큰 공간감을 우선한다. 같은 대공간 안 세부 공간은 색·재질·구조 실루엣을 공유한다.

| 대공간 | 적용 구간 | 기능 | 큰 형태 / 실루엣 | 색 / 질감 | 세부 공간 |
|---|---|---|---|---|---|
| Cross Manor / Estate | EP04·07-08·13·14·17-19·20·22·25-26·28·29-34·36-37·39·48 | 계단 망신·페이월·Mara 스위트(아침/민낯)·브라이덜 샤워·결혼식·EP37 대계단 | 거대 대리석 발리룸, 무대 dais, **grand staircase (커브 = 최상단 근처·커브 위는 플로어 시야 사각·EP37 Mara 자작 낙하 연출 전제)**, 정원, 차가운 금·유리 재벌 저택 | cold marble white, gold, deep navy, chandelier glare | ballroom, front steps, Mara's suite, bridal room, garden(shower·wedding), gates |
| Glenmoor Cemetery | EP01·EP14·EP50 | 어머니 묘소 (진짜 모친) | Sterling family plot, headstone, manicured grounds | grey stone, green, overcast soft light | graveside |
| Noah's Penthouse (home base) | EP08(구출)·09·10·11·15·16·21·23·24·27·32·35·38·39·40·41·45·50 외 | "여기선 안전한 나" · 로맨스·재정비·상시 base | floor-to-ceiling glass, Manhattan skyline, minimal warm interior | night city light, warm low lamp, glass black mirror | living room, kitchen, bedroom (EP38 침실 씬 — headboard·sex), terrace (EP40 프로포즈) |
| Lena's Apartment / Sterling Bldg | EP05·EP07·EP09·EP50 | 도둑맞은 집 → Hector 거부(EP09)·회복(EP50) | marble lobby, modern high-floor apartment | warm neutral, marble, intruder's perfume | lobby (Hector EP09·50), 14B interior (EP05·07) |
| Brandt Clinic | EP01-02 | swap 현장 (얼굴 도둑) | mirror-wall back room, surgical light. **수술 마스크 소품 = 이 씬 전용** | clinical white, mirror, cold steel | mirror room |
| Swap-Night Sets (1회) | EP02·EP03 | 연출 사고·병원 탈출 | coastal road·diner·hospital room | rain night, wet asphalt, clinical | wreck, diner TV, Harbor General |
| Public Set-Pieces (milk) | 추모 오찬 EP13·추모 갈라 EP17-19·살롱 EP22·루프탑 EP28·자선 갈라 계단 EP37·모닝쇼 EP09·16·39·42·TV 스튜디오 거리 문 EP12 | Lena가 가짜를 공개서 흔드는 무대 | 행사장 홀·sweeping 계단·살롱·TV 스튜디오·스튜디오 거리 유리문 | event lighting, press, raised phones, daylight sidewalk | gala floor, grand staircase, salon mirror, talk-show set + 백스테이지(red-light tell), studio street doors (EP12) |
| The Glass Conservatory | EP44·EP46-50 (베뉴 결정 EP42 Noah 사무실·EP43 펜트하우스 / 컨서버토리 물리 등장 EP44부터) | Lena & Noah 결혼식 (진짜 회복) / EP48 폭로 무대 | wide glass hall over the sea, white peonies, aisle, tide behind | sea light, white, glass, gold band | aisle, bridal suite (EP46 Noah's Aunt), steps |
| Somewhere Small | EP50 | Mara의 몰락 | cramped bare gray room, muted TV | drained gray, cold | — |

### 대공간 사용 규칙

- establishing wide는 대공간을 한 번 잠글 때만. 반복 컷은 빈 목·펜던트 위치·흉터·군중 반응·Mara 가면 균열 같은 권력 변화 중심.
- Cross Manor(가짜의 권력) vs Noah Penthouse(진짜의 안전) vs Conservatory(회복) = 색온도로 즉시 구별.
- 같은 대공간 안에서는 소품·조명만 바뀌고 건축 문법 유지.
- **EP37 대계단 기하 고정:** 커브 = 최상단 근처. 커브 위는 아래 플로어에서 시야 사각. Mara가 커브 상단까지 후퇴 후 자작 낙하하는 동선 전제. 추락 후 [HIGH ANGLE] = 아래 군중이 Lena를 올려다보는 샷.

---

## 5. 최종 폐기 기준

- 두 얼굴(Lena·Mara)이 한 컷에서 한눈에 구별 안 됨 / 긴 정적 같은-프레임에서 "누가 진짜?" 뜯어봐야 함.
- 쿨한 수사·미스터리·스릴러 무드 (이 작품은 막장 — 시청자는 1화부터 다 안다).
- 소품이 이야기를 끎 (CCTV·서류·증거·카메라 장치로 진실 폭로) — 진실은 가짜의 자백+Eileen 폭로로만.
- 빌런(Mara·Victoria·Eileen)이 영리·우아·동정 가게 보임 (천박·뻔뻔·멍청해야 함).
- Lena가 매달리고 질질 짜는 default 피해자로 보임 (당하되 꺾이지 않음).
- 인물이 시대극/판타지/애니/현대 클럽룩에 있음 (현대 재벌 글로시 실사).
- **Mara 흉터가 사라지거나 위치가 흔들림.** (분장 Hard Lock)
- **EP33 Mara 웨딩드레스에 long lace sleeves 없음** (팔뚝 흉터 은폐 기능 — 어셋 동기화 의무).
- **EP08-09 의상 = catering uniform 체계** (구본 오류 어셋 사용 금지 — §2-1 룩표 1-2 참조).
- 펜던트가 reveal-key처럼 쓰임 / 각인이 플롯을 해결.
- 시적·연극·은유 대사 (`coat`·`seams`·`costume` 류).
- 예쁜데 무슨 일이 바뀌었는지 안 읽힘 (뇌-오프 실패).
- **클리닉 수술 마스크가 클리닉 외 씬에 등장.**

---

## 환류 로그

- **2026-05-12 v1~v3:** 초기 6변형 캐릭터 어셋 + no-theater-tone 5차원 + 인티머시 카논. (구 증거-미스터리·이복자매 엔진 기준 — 폐기.)
- **2026-05-30 v4 (전면 재작성 · titan_born 양식 참조 · v37 동기화):** 양식 교체·v37 엔진 동기화·캐논 오류 수정·신규 락 추가.
- **2026-06-01 v5 (v38.1 환류):** 소스 경로 v37→v38·드레스 회수 EP05·Noah 등장 EP04·Hector EP09·50·공간 EP 마커 재동기화·회귀 단역 신규.
- **2026-06-01 v5.1 (v38.2 환류 + 대본 전수 대조):** 정합성 수정·Eileen 물리/음성 구분·Conservatory EP44+ 확정.
- **2026-06-04 v6 (FINAL v41 환류):** EP01 콜드오픈 정확 구조·팔찌 룰 정정·doubter-clip·red-light tell·신규 공간 추가.
- **2026-06-05 v6.1 (v41 후속 패스 환류):** 콜드오픈 정정·물증형 보증 2자루·회귀 단역 EP 정정·Mara EP02-03 약혼 가운 복제본·Tessa EP50 클립만.
- **2026-06-12 v7 (FINAL v53 전면 갱신 — v53 LOCK 기준):**
  - **EP08-09 의상 체계 전환:** 구본 오류 어셋(gown류·맨발·코트) 전부 제거 → Lena EP08 = catering uniform(white)+dark wig+apron / EP08 S#6 = catering jacket ripped at blouse strap ("No purse, no phone, no name"). Noah = EP08 dark suit(Cross Manor 파티 진입). Lena 룩표(1-2 Erased) 재작성.
  - **EP33 Mara 웨딩드레스 = long lace sleeves** 추가 + 어셋 동기화 필수 노트(팔뚝 흉터 은폐). Mara 룩표(2-2 Mrs. Cross) + AIGC Call 웨딩 변형 신설.
  - **수술 마스크 소품 범위 명시:** EP01-02 클리닉 씬 전용 (그 외 화수 등장 없음). §2-8 Celia 섹션 + §5 폐기 기준에 반영.
  - **핵심 소품 3종 상태 추적표 갱신:** ①pendant = `LUMEN MEUM` 각인 명시·EP49 회수 경로 정확화. ②Helena 다이아 팔찌 = 소품 2가지 상태(좌측 wrong wrist / 우측 리사이즈 후)·Lena EP11 문자 trigger·EP12+ 영구 미착용. ③시술 흉터 = 분장 Hard Lock·EP01-03 fresh pink → 이후 faint silver line.
  - **EP48 클리닉 intake photo 소품:** 폰 화면 전용·장내 카메라 차단 연출·별도 분장/배우 또는 합성 어셋 명시. §3 신규 항목.
  - **EP38 침실 씬 KEY CAMERA 추가:** headboard·pinning(Lena on top)·shoulder-blade pull. §1 Female gaze/인티머시 수위 T2→T3 갱신.
  - **EP37 대계단 기하 명시:** 커브 위치·플로어 시야 사각 구조·Mara 자작 낙하 연출 전제. §4 Cross Manor 행 + 사용 규칙에 추가.
  - **V.O. 13건 더빙 트랙 노트 신설:** Lena 9·Ethan 2(EP27·32)·Mara 2(EP11·37)·EP별 대사 인용. §1 신규 항목.
  - **Ethan V.O. EP 명시:** §2-4 Ethan 섹션.
  - 검증: 구본 오류 어셋 키워드 0건·"catering" 등장·"long lace sleeves" 등장·"Lumen meum" 등장·"Lena V.O. 9건" 등장 확인.
