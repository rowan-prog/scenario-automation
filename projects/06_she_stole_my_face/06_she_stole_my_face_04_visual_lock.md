# SHE STOLE MY FACE - VISUAL LOCK

목적:

- 9:16 vertical 실사형 어셋 생성 기준
- 캐릭터 / 소품 / 배경의 반복 생성용 디자인 락
- 대본 기준 고정 (`07_final/06_she_stole_my_face_FINAL_v38.md` = v38.2)
- 프롬프트 원재료로 바로 쓸 수 있게, 명사 / 형태 / 색 / 소재 / 금지사항 중심으로 정리
- 은유적 분위기 설명보다 눈에 보이는 외형 정보 우선

장르: 현대 재벌가 신분도용 복수극 (막장). NA 여성향 25-45. 최대 수위 T2 (kiss·dressed, sex 직접 묘사 X).

---

## 1. 공통락

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
- 첫 컷은 풍경이 아니라 두 개의 똑같은 얼굴 (거울 앞 Lena와 마스크 벗는 Mara)로 시작

### 🔒 동일 얼굴 구별 락 (이 작품 최우선 — AIGC #1 제약)

Lena와 Mara는 **같은 얼굴**(시술로 동일)이다. 매 컷에서 둘이 한눈에 구별돼야 하며, 구별 수단은 다음 5가지뿐이다:

1. **시술 흉터 (Mara 전용)** — 좌측 귀 2cm 아래 곡선 1.5cm + 우측 손목 안쪽 직선 3cm. 평상시 헤어/각도로 가려지고 **근접 증거 컷에서만 노출.** EP01-50 동일 위치 유지 (Hard Lock).
2. **의상 팔레트** — Lena = 절제된 slate·navy·charcoal·ivory / Mara = 훔친 글로시 룩(navy·cream silk) → 후반 black(난입)·stripped(몰락).
3. **헤어 스타일링** — Lena 낮은 정돈(다운/낮은 묶음/단정 하프업) / Mara 더 윤기·화려한 셋업.
4. **태도·자세** — Lena 정적·자제·곧은 자세 / Mara 카메라 앞 sweet-victim 연기, 단둘이면 천박·비웃음·snarl.
5. **맥락** — 세상이 떠받드는 쪽 = Mara (EP1-48). 목에 펜던트 있는 쪽 = Mara (EP1-49).

- ❌ 두 얼굴을 **긴 정적 한 프레임**에 같이 넣어 "어느 쪽이 진짜?"를 시청자가 뜯어보게 만드는 컷 금지 (AIGC 동일인물 일관성 붕괴 위험).
- ✅ OTS · 컷 분리 · 위치 분리 · 한 명씩 close. 같은 프레임이 필요하면 흉터/의상/태도로 즉시 구별되게.

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

### Female gaze / 인티머시 (T2 한도)

- 페어: Lena ↔ Noah (T2 키스·내밀 접촉, 옷 벗기/sex 묘사 X). T2 비트 = **EP15·23·38·45**.
- Lena ↔ Ethan = T1 이하 (사고 전 짧은 손길·이후 0).
- 부위 순회 tracking 금지 · Noah forearm weight·gaze 우선 · Lena의 choice(먼저 손 닿느냐) 우선.
- 직설: `They kiss.` / `He kisses her, slow.` (은유 우회 X)

---

## 2. 인물별 락

## 2-1. LENA STERLING (주인공·진짜 약혼녀)

### 캐릭터 / 디자인 느낌

- 주인공 · 빼앗긴 진짜 상속녀
- 우아·자제력·관찰력 · 당하되 꺾이지 않음 · 매달림/질질 짜는 피해자 금지
- 후반부 = 수동 피해자 X → 가짜를 카메라 앞에서 깨는 능동 사냥꾼

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 1-1 Public Fiancée | EP01 (사고 전) | navy silk-wool suit, hair down, mother's pendant at throat |
| 1-2 Erased | EP01-04 (사고 후·비 도주) | white hospital gown under ivory cashmere coat, gauze at right temple, bare neck |
| 1-3 Infiltrator | EP05-08 | low ponytail, charcoal knit + slate coat / EP07-08 grey staff uniform + BRIDAL ROOM keycard, bare neck. (EP05 어머니 진짜 드레스 회수.) |
| 1-4 Fighting (Noah's world) | EP09-45 | restored tailored slate·navy, then soft ivory once engaged (EP41), bare neck still |
| 1-5 True Bride | EP46-50 | mother's ivory silk gown (the one Mara never found), slim gold band / EP50 pendant back at throat |

### 상세

- 나이: **30세** (NEVER late-20s)
- 키/비율: 가는 골격, 긴 목선, 곧은 어깨, 곧게 선 자세
- 헤어: ink-black soft straight hair to mid-back, 정돈 (다운 / 낮은 묶음 / 단정 하프업)
- 눈: 회녹색(moss-green), 차분한 시선
- 얼굴: 갸름한 V형, 도자기 흰 피부 (Mara와 동일 — 시술 표적)
- 몸: 가는 허리, 긴 다리, 절제된 자세
- 의상: slate·navy·charcoal 맞춤 정장 / 실크 / 캐시미어 → EP46+ ivory 실크 가운
- 신발: polished oxfords / low pumps
- 악세사리: 어머니 목걸이 (EP01 착용 → EP01 강탈 → **EP02-49 빈 목** → EP50 회수). 어머니 진주 귀걸이(작은 것).
- 표식: 흉터 없음 (이게 Mara와의 구별점 — Lena는 흉터가 없다)
- 색: black·navy·slate·charcoal·ivory
- AIGC Call (기본): `30-year-old woman, fine V-jaw, cool moss-green eyes, porcelain skin, ink-black straight hair to mid-back, slate-grey tailored suit, bare neck (no necklace). Calm contained posture.`
- 금지: 매달림/울음 default · 가짜 외모 차이(흉터는 Lena엔 없음) · 부위 순회 tracking · 시적/은유 대사 · 자기 연민 monologue

## 2-2. MARA VOSS / FAKE LENA (가짜 약혼녀·도둑)

### 캐릭터 / 디자인 느낌

- 신분도용 가해자 · Lena의 20년 친구 · 질투로 얼굴을 훔침 (**이복자매 아님 — 그냥 가짜·도둑**)
- 영리한 체스 플레이어 X → **뻔뻔·천박·멍청.** 카메라 앞 sweet-victim 연기 / 단둘이면 비웃음·자랑·snarl
- 가진 것 다 가졌는데 "내 것 같지 않다"는 공허 · 들킬까 늘 두려움

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 2-1 Imposter Bride | EP01-34 | Lena의 삶을 입음: navy·cream silk, STOLEN pendant at throat, diamond bracelet on left wrist, sweet public mask |
| 2-2 Mrs. Cross | EP35-46 | married polish, blush·cream, wedding ring + stolen pendant, growing hollow/strained under the smile |
| 2-3 Fallen | EP47-50 | EP47 black dress + cameraman (wedding crash) → EP50 stripped (pendant peeled off), alone in a cramped gray room |

### 상세

- 나이: **30세** (Lena와 동일)
- 얼굴/체형: Lena와 **완전 동일** (시술) — 표정만 다름(계산적·sweet 연기 / 천박)
- 헤어: ink-black straight hair to mid-back (염색·약간 더 윤기), 화려한 셋업
- 눈: 회녹색 (시술로 같은 색)
- 신체 우세: **시술 흉터** — 좌측 귀 2cm 아래 곡선 1.5cm + 우측 손목 안쪽 직선 3cm. 평상시 가려지고 근접 증거 컷에서만 노출. EP01-50 동일 위치 (Hard Lock).
- 의상: 훔친 navy·cream 실크·재벌가 룩 → EP35+ Mrs. Cross 광택 → EP47 black → EP50 stripped
- 악세사리: 빼앗은 어머니 목걸이(EP01-49 착용 → EP50 강제 회수), diamond bracelet(좌측 손목)
- 색: navy·cream·blush → black → drained gray
- AIGC Call (기본): `30-year-old woman, identical V-jaw and moss-green eyes to Lena, faint curved scar 2cm below left ear + straight scar on right inner wrist, ink-black styled hair, navy/cream silk, stolen gold-diamond pendant at throat, diamond bracelet on left wrist. Sweet performed face in public, vulgar smirk in private.`
- 금지: 흉터 사라짐·위치 이동 · 영리한 침착 빌런 톤 · 동정 가는 퇴장(EP50 = 아무도 없는 회색 방, 구원 X) · 시적/연극 대사

## 2-3. NOAH KEENE (새 남주)

### 캐릭터 / 디자인 느낌

- 사설 조사 전문가 · Lena를 믿는 유일한 사람 → 후반 **판을 깔아주는 남자**(자기 결혼식을 Lena가 이기는 방으로 만듦)
- 단순·강함·소유 · 든든한 벽 · 흔들림 없는 확신 (의심 X)

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 3-1 Investigator | EP04-45 | midnight-blue coat over dark sweater/knit, dark trousers |
| 3-2 Groom | EP46-50 | charcoal morning suit, gold band |

### 상세

- 나이: 30대 중반 · 키 큰 단단한 체격
- 헤어: cropped ink-black · 눈: deep grey, slight squint, faint laugh line
- 얼굴: granite jaw, 차분
- 의상: midnight-blue investigator coat, dark knit, 고급 수트 → EP49 charcoal morning suit
- 악세사리: vintage silver wristwatch, leather camera bag (직업 소품 — 증거 엔진 X)
- 색: black·midnight-blue·charcoal
- AIGC Call: `Mid-30s man, granite jaw, deep grey eyes with slight squint, cropped ink-black hair, midnight-blue coat over dark sweater. Calm, immovable.`
- 금지: 시적/연극 대사 · "I know / I saw it" 반복 의존 (중후반엔 행동으로) · Lena를 의심하는 비트(엔진 위반)

## 2-4. ETHAN CROSS (약혼남 → 잘못된 선택)

### 캐릭터 / 디자인 느낌

- 재벌 후계 · Lena의 전 약혼남 · **"편한 진실"을 택한 겁쟁이** (추리하는 남자 X, 체면 때문에 가짜 편)
- EP49 Mara에게 등 돌림 · 사과는 짧게·드물게 (매달림 X)

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 4-1 Cross Heir | EP01-50 | charcoal three-piece suit, silver tie bar / platinum band (EP01-34 결혼 후 wedding ring) |

### 상세

- 나이: 30대 초반 · 큰 키 · 정장 어울리는 어깨
- 헤어: short ink-black swept back · 눈: deep grey · 우측 눈썹 위 얇은 흉터
- 의상: charcoal/navy three-piece, 실크 타이, Patek 시계
- 색: charcoal·navy·silver
- AIGC Call: `Early-30s man, square jaw, deep grey eyes, thin scar above right brow, short ink-black hair swept back, charcoal three-piece suit, Patek watch.`
- 금지: 후회로 매달리는 처량함(Lena 거부) · 한 단어 사과 핑퐁 · 영리한 추리 톤

## 2-5. VICTORIA CROSS (크로스 가문 여주인)

### 캐릭터 / 디자인 느낌

- 크로스 가문 매트리아르크 · 빌런 · **품격 악녀 X → 상류층 권위로 막말** ("Get that thing away from my son")
- 진실: "몰랐다" 아닌 **"의심했지만 가문 지키려 외면"**

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 5-1 Matriarch | EP01-50 | charcoal Chanel-cut tweed suit, baroque pearl choker + earrings |

### 상세

- 나이: 50대 후반 · 우아한 자세
- 헤어: silver-streaked dark hair, French twist · 눈: pale grey, 바깥쪽 처진
- 의상: 어두운 트위드·실크 정장, 가문 진주·다이아
- 색: charcoal·dove grey·pearl
- AIGC Call: `Late-50s woman, sharp jaw, pale-grey eyes, silver-streaked dark hair in French twist, charcoal tweed suit, baroque pearl choker.`
- 금지: 의식문/판결문 cadence · tri-colon · 따뜻한 할머니 톤

## 2-6. EILEEN VOSS (Mara의 모친·배후)

### 캐릭터 / 디자인 느낌

- Mara의 실제 엄마 · 딸에게 가짜 삶을 계속 우겨넣는 독한 엄마 · 큰 설계자 X
- 일이 틀어지자 딸을 손절(EP39) · 글램 없음 (떠받들리는 건 Mara뿐)

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 6-1 Puppeteer | EP02·36·39 (화면 등장·렌더 필요) · EP20·28·30 (전화 음성만·비등장) | plain dark coat, hard practical look, no luxury |

### 상세

- 나이: 50대 후반 · 단단·실용
- 헤어: dull dark hair pulled back, 흰머리 약간 · 눈: hard
- 의상: 어두운 실용 코트·평범한 정장 (재벌 글램 X — 그녀는 바깥 사람)
- 색: dull dark·grey
- AIGC Call: `Late-50s hard-faced woman, dark hair pulled back, plain dark coat, no jewelry. Cold practical.`
- 금지: 우아한 상류층 룩 · 동정 가는 모성

## 2-7. TESSA HALE (배신한 친구)

### 캐릭터 / 디자인 느낌

- Lena의 친구·조수 · 도박 부채로 Mara에 Lena 일정 넘김 · EP06 자백(Lena가 Mara의 약점=무기를 캐냄) · EP12 TV 배신
- 복잡한 죄책감 X → 돈 받고 울며 배신

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 7-1 The Friend | EP01·EP06·EP11 | camel cardigan over cream camisole, soft casual / EP06 mascara-wrecked |

### 상세

- 나이: 20대 후반 · 보통 체격
- 헤어: shoulder-length auburn waves, copper highlights · 눈: warm hazel · 우측 입가 작은 점
- 의상: 부드러운 캐주얼 · EP06 흐트러진 모습
- 색: camel·cream·auburn
- AIGC Call: `Late-20s woman, oval face, warm hazel eyes, mole above right lip, shoulder-length auburn waves, camel cardigan over cream camisole.`
- 금지: EP12 이후 등장 비중 확대 · 한 단어 사과 핑퐁

## 2-8. DR. CELIA BRANDT (클리닉 의사·협력자)

### 캐릭터 / 디자인 느낌

- 미용 클리닉 의사 · Mara 시술 집도·협력자 · EP01 swap 현장

### 디자인룩

| 룩 | 적용 EP | 상태 |
|---|---|---|
| 8-1 Clinic Doctor | EP01 (+짧은 후속) | white medical coat over slate blouse |

### 상세

- 나이: 40대 · 마른 체형
- 헤어: short caramel bob · 눈: hazel behind thin gold-rim glasses
- 의상: 흰 가운·짙은 평상복 · 가슴 포켓 silver pen
- 색: white·slate
- AIGC Call: `Early-40s woman, narrow oval face, hazel eyes, thin gold-rim glasses, short caramel bob, white coat over slate blouse.`
- 금지: 의학 용어 dump · 영리한 공범 톤

## 2-9. 회귀 단역 (연속성-필수 · 동일 배우 유지)

- **THE CEMETERY REPORTER** (젊은 여기자) — EP14·18·19·49. 20대 후반, press lanyard·소형 카메라, 평범한 정장 코트. 군중과 달리 *촬영 안 하고 관찰*(EP14) → EP18부터 Mara를 찍는 쪽. 동일 배우.
- **THE WOMAN IN PEARLS** (Helena의 오랜 친구) — EP26·49. 60대, baroque 진주 목걸이·이브닝 가운, 품위. EP26 게이트서 사적 고백 → EP49 군중서 *선두로* Lena 곁. 동일 배우.

---

## 3. 소품별 락 — 생성용 표식, 서사 엔진 아님

원칙: **소품은 캐릭터 행동·관계·정체의 표식이지, 장면을 해결하거나 이야기를 끌지 않는다. 진실은 소품이 아니라 가짜의 자멸(자백)로 밝혀진다.**

진행 중심: Lena의 능동 선택, Mara의 뻔뻔/멍청, 세상의 외면, Noah의 공개 선택.

### 핵심 표식 소품

| 소품 | 디자인 | 룰 |
|---|---|---|
| 어머니 목걸이 (MOTHER'S PENDANT) | gold-diamond, 안쪽 라틴 각인 `LUMEN MEUM` | **감정·정체성 표식** (Hard Lock 예외). EP01 강탈 → Mara 목 EP01-49 → EP50 강제 회수 → Lena 목. **Reveal trigger 아님.** 각인 = Lena만 아는 것 / Mara는 모름 (멍청함의 바늘), 플롯-키 X. |
| 시술 흉터 (SURGICAL SCAR) | 좌측 귀 2cm 아래 곡선 1.5cm + 우측 손목 안쪽 직선 3cm | Mara 전용 · 두 얼굴의 유일한 시각 구별 · **근접 confirmation 컷만**, 세상을 뒤집는 trigger 아님(자백이 먼저). |
| 어머니 진짜 웨딩드레스 | 단순 ivory silk, no train | EP05 Lena가 false panel서 꺼내 들고 나옴(Mara가 못 찾은 것) → EP46 그 드레스로 결혼. 감정 회수. |
| 다이아 팔찌 (Mara) | diamond bracelet, 좌측 손목 | EP01 사고 현장 prop · 단발 시각 디테일 (CCTV-단서 엔진 아님). |

### 폐기된 소품 (이전 설계 잔재 — 사용 금지)

- ❌ CCTV 사고 영상 / 프레임 분석 · ❌ 삭제 예약표 · ❌ 테사 서명 증거 · ❌ MARA VOSS 본명 파일
- ❌ 브라이덜룸 카메라 → 대형스크린 연결 (진실-공개 장치) — 전부 제거됨. 진실은 EP48 Mara의 자백.

### 화면 증거 (소품 아닌 UI)

- TV chyron(`MR. & MRS. CROSS`·`STALKER INCIDENT`), 폰 피드/댓글, 군중 핸드폰, 자막 reveal(`SHE STOLE MY FACE`·`SHE FINALLY SAID IT HERSELF`) — 9:16 모바일에서 즉시 읽히게.

---

## 4. 대공간별 락

세부 방 이름보다 반복 출현하는 큰 공간감을 우선한다. 같은 대공간 안 세부 공간은 색·재질·구조 실루엣을 공유한다.

| 대공간 | 적용 구간 | 기능 | 큰 형태 / 실루엣 | 색 / 질감 | 세부 공간 |
|---|---|---|---|---|---|
| Cross Manor / Estate | EP04·07-08·20·25-26·28·29-34·36·39 | 계단 망신·페이월·Mara 스위트·브라이덜 샤워·결혼식 | 거대 대리석 발리룸, 무대 dais, 앞 계단, 정원, 차가운 금·유리 재벌 저택 | cold marble white, gold, deep navy, chandelier glare | ballroom, front steps, Mara's suite, bridal room, garden(shower·wedding), gates |
| Glenmoor Cemetery | EP01·EP14·EP50 | 어머니 묘소 (진짜 모친) | Sterling family plot, headstone, manicured grounds | grey stone, green, overcast soft light | graveside |
| Noah's Penthouse (home base) | EP08·10·15·21·23·24·32·35·38·40·41·45·50 외 | "여기선 안전한 나" · 로맨스·재정비·상시 base | floor-to-ceiling glass, Manhattan skyline, minimal warm interior | night city light, warm low lamp, glass black mirror | living room, kitchen, bedroom, terrace |
| Lena's Apartment / Sterling Bldg | EP05·EP09·EP50 | 도둑맞은 집 → Hector 거부(EP09)·회복(EP50) | marble lobby, modern high-floor apartment | warm neutral, marble, intruder's perfume | lobby (Hector EP09·50), 14B interior (EP05) |
| Brandt Clinic | EP01 | swap 현장 (얼굴 도둑) | mirror-wall back room, surgical light | clinical white, mirror, cold steel | mirror room |
| Swap-Night Sets (1회) | EP02·EP03 | 연출 사고·병원 탈출 | coastal road·diner·hospital room | rain night, wet asphalt, clinical | wreck, diner TV, Harbor General |
| Public Set-Pieces (milk) | 추모 오찬 EP13·추모 갈라 EP17-19·살롱 EP22·루프탑 EP28·자선 갈라 계단 EP37·모닝쇼 EP16·39·42 | Lena가 가짜를 공개서 흔드는 무대 | 행사장 홀·sweeping 계단·살롱·TV 스튜디오 | event lighting, press, raised phones | gala floor, grand staircase, salon mirror, talk-show set |
| The Glass Conservatory | EP44·EP46-49 (베뉴 결정 EP42 Noah 사무실·EP43 펜트하우스 / 컨서버토리 물리 등장 EP44부터) | Lena & Noah 결혼식 (진짜 회복) | wide glass hall over the sea, white peonies, aisle, tide behind | sea light, white, glass, gold band | aisle, bridal suite, steps |
| Somewhere Small | EP50 | Mara의 몰락 | cramped bare gray room, muted TV | drained gray, cold | — |

### 대공간 사용 규칙

- establishing wide는 대공간을 한 번 잠글 때만. 반복 컷은 빈 목·펜던트 위치·흉터·군중 반응·Mara 가면 균열 같은 권력 변화 중심.
- Cross Manor(가짜의 권력) vs Noah Penthouse(진짜의 안전) vs Conservatory(회복) = 색온도로 즉시 구별.
- 같은 대공간 안에서는 소품·조명만 바뀌고 건축 문법 유지.

---

## 5. 최종 폐기 기준

- 두 얼굴(Lena·Mara)이 한 컷에서 한눈에 구별 안 됨 / 긴 정적 같은-프레임에서 "누가 진짜?" 뜯어봐야 함.
- 쿨한 수사·미스터리·스릴러 무드 (이 작품은 막장 — 시청자는 1화부터 다 안다).
- 소품이 이야기를 끎 (CCTV·서류·증거·카메라 장치로 진실 폭로) — 진실은 가짜의 자백으로만.
- 빌런(Mara·Victoria·Eileen)이 영리·우아·동정 가게 보임 (천박·뻔뻔·멍청해야 함).
- Lena가 매달리고 질질 짜는 default 피해자로 보임 (당하되 꺾이지 않음).
- 인물이 시대극/판타지/애니/현대 클럽룩에 있음 (현대 재벌 글로시 실사).
- Mara 흉터가 사라지거나 위치가 흔들림.
- 펜던트가 reveal-key처럼 쓰임 / 각인이 플롯을 해결.
- 시적·연극·은유 대사 (`coat`·`seams`·`costume` 류).
- 예쁜데 무슨 일이 바뀌었는지 안 읽힘 (뇌-오프 실패).

---

## 환류 로그

- **2026-05-12 v1~v3:** 초기 6변형 캐릭터 어셋 + no-theater-tone 5차원 + 인티머시 카논. (구 증거-미스터리·이복자매 엔진 기준 — 폐기.)
- **2026-05-30 v4 (전면 재작성 · titan_born 양식 참조 · v37 동기화):**
  - 양식을 titan_born 비주얼락 lean 포맷으로 교체 (명사·외형·금지 중심·프롬프트 ready). 캐릭터별 🆕 비대 서브섹션 제거.
  - **v37 엔진 동기화:** 증거/수사/CCTV/삭제예약표/서명/브라이덜룸-카메라-폭로장치·이복자매(EP35 bloodline)·EP25 정체폭로 = 전부 제거. 진실 = EP48 Mara 자백(Lena가 결핍 찔러). 펜던트·흉터 = 표식(엔진 X).
  - **캐논 오류 수정:** Lena/Mara 나이 late-20s → **30세.** 펜던트 회수 EP9 → **EP50.** 인티머시 EP16/23/48/49 → **T2 EP15·23·38·45.**
  - **신규 락:** 🔒 동일 얼굴 구별 락(AIGC #1 제약·5수단·긴 같은-프레임 금지) · 시청자 이해도(뇌-오프) · 막장 톤(쿨 미스터리 금지·빌런 천박).
  - 룩 변형 v37 EP에 재정렬 (Lena 5룩·Mara 3룩·빈 목 EP02-49). 폐기 소품 명시.
- **2026-06-01 v5 (v38.1 환류):**
  - 소스 경로 v37→**v38**(=v38.1). swap EP01→EP01-02·드레스 회수 EP04→**EP05**·Noah 등장 EP03→**EP04**·Hector EP09·50 반영.
  - 공간 EP 마커 v38 재동기화: 묘지 EP01·14·50(EP17 오류 수정)·Cross Manor/Estate EP04·07-08·20·25-26·29-34·36·39·펜트하우스=home base·아파트 EP05·09·50. **Swap-Night Sets·Public Set-Pieces(milk)** 행 추가.
  - 캐릭터 EP 마커: Eileen EP02·20·30·36·39 · Tessa EP01·06·11.
  - **2-9 회귀 단역(동일 배우) 신규:** 묘지 기자(EP14·18·19·49)·진주 노부인(EP26·49).
  - Mara 펜던트 회수 "무대서"→"강제 회수"(EP50=몽타주).
- **2026-06-01 v5.1 (v38.2 환류 + 대본 전수 대조 정합성 수정):**
  - 소스 경로 v38.1→**v38.2**(Noah 위로비트 반복 압축 패스 반영 — 2-3 Noah "I know 반복 금지" 룰이 본문에 실제 적용됨).
  - **정합성 수정 (현재 대본 실측 기준):** ①6-1 Eileen "EP02·20·30·36·39" → **물리 등장 EP02·36·39 / 전화 음성만 EP20·28·30**(EP28 폰 V.O. 누락분 추가·렌더 불필요분 구분). ②§4 Conservatory "EP43-44" → **EP44·46-49**(EP42 사무실·EP43 펜트하우스서 베뉴 결정만·컨서버토리 물리 등장은 EP44부터). ③§4 Cross Manor에 **EP28**(Mara 스위트 S#2) 추가.
  - 검증: 묘지 기자(EP14·18·19·49)·진주 노부인(EP26·49)·Hector(EP09·50)·펜던트(EP01→50)·드레스(EP05→46)·흉터·T2(15·23·38·45) = 전부 대본 일치 확인.
