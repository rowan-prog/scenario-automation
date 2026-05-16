# Paid Vertical 시장 인사이트 (2026-05-16)

> **입력:** `vertical_hit_library_2026-05-15.xlsx` (287작 / 5개 플랫폼 / 81 ranked tropes / 2025-06 ~ 2026-05).
>
> **한계 (사용자 명시 인용):** "내용 밀도가 높지 않고 풀대본도 아니니 한계가 있지만, 이 시장을 이해하는 데는 도움이 될 수 있다."
>
> **데이터 한계 명시:** evidence_score 100점이라도 그 100점이 매출(view·결제·랭킹) 검증 100점은 아님. `runtime XX min`이 `XX.0M`으로 잘못 파싱되는 케이스가 다수 있어 매출 수치 인용 시 시트 자체의 `reaction_signal`을 우선. 본 라이브러리는 **공식 페이지 노출·SNS 신호·언론·재유통 흔적** 기반 큐레이션 (월별 공식 매출 랭킹 X).

---

## 0. 데이터 구조 한눈에

| 항목 | 수치 |
|---|---|
| Total rows | 287 |
| A_Core (evidence 85+) | 106 |
| B_Strong | 125 |
| C_Watch | 42 |
| D_Verify | 14 |
| AIGC flagged | 42 |
| target = Female / Romance | 137 (48%) |
| target = Female / Family-romance | 40 (14%) |
| target = Family regret / mixed | 36 (13%) |
| target = Male / Power fantasy | 30 (10%) |
| target = Mixed / General | 29 (10%) |
| target = Female / Revenge-SFL | 13 (5%) |
| target = BL/Queer | 2 (0.7%) |

**한 줄로:** 라이브러리의 **75%가 여성향 + 가족(여성 결제 권역)**. 남성향은 10% 미만, BL은 거의 0.

플랫폼 분포는 균질 (NetShort 61 / DramaWave 60 / ReelShort 56 / GoodShort 56 / DramaBox 54).

---

## 1. 매출 신호 강한 작품 (정량 view metric 검증)

`reaction_signal` 또는 `performance_signal`에 명시적 "X.XM views/followers/subscribers" 가 있는 작품. 그 외는 "Release date / runtime XX min" 같은 출시 메타만 있어 매출 검증 X.

### 정량 검증 상위 (실제 view 신호)

| view | 플랫폼 | target | 작품 | desire engine | conversion engine |
|---|---|---|---|---|---|
| **191.9M** | ReelShort | Female/Romance | **Fated To My Forbidden Alpha** | Hidden-identity + High-status partner | 정체/권력 공개 직전 결핍 누적 |
| **114.7M** | ReelShort | Female/Family-romance | **Accidental Surrogate for the Alpha** | High-status partner + Child/family reunion | 정체/권력 공개 직전 결핍 누적 |
| **76.6M** | ReelShort | Female/Romance | **Your Husband Is Mine** / **Sisterhood of Lies** | Revenge/regret + Campus/sports heat | 굴욕/배신 후 첫 반격 예고, 본격 응징 지연 |
| **46.0M** | ReelShort | Female/Romance | **Fated to My Homeless Billionaire Alpha** | High-status partner | 강한 케미·보호/소유 신호 + 감정 확정 지연 |
| **22.7M** | GoodShort | Family regret | **A Blind Date with my Mr. Meant-to-Be** | Child/family reunion | 무료=결핍·예고 / 유료=보상·진실·역전 |
| **5.3M** | GoodShort | Family regret | **Blood and Bones of the Disowned Daughter** (Natalie) | Hidden-identity + Revenge + Child reunion | 정체/권력 공개 직전 결핍 누적 |
| **3.0M** | DramaBox | Female/Romance | **Summer Honeymoon with My Secret Billionaire** | Hidden-identity + High-status partner | 정체/권력 공개 직전 결핍 누적 |
| **2.0M** | NetShort | Male/Power fantasy | **One Move God Mode** | Revenge/regret + Progression | 굴욕/배신 후 첫 반격 예고 |
| **2.0M** | ReelShort | Female/Family-romance | **Fated Mate of the Nine-Tailed Fox** | Hidden-identity + Child reunion | 정체/권력 공개 직전 결핍 누적 |
| **1.3M** | ReelShort | Female/Romance | **The Last Time I Forgive** | Revenge/regret | 굴욕/배신 후 첫 반격 예고 |
| **1.0M+** | NetShort | Male/Power fantasy | **The Legend of A Bastard Son / Iron Fist** | Hidden-identity + Child reunion / Core melodrama | 정체 공개 지연 / 결핍-보상 |
| **3M in 24h** | DramaBox | Female/Romance | **Summer Honeymoon with My Secret Billionaire** | Hidden-identity + High-status | 정체 공개 지연 (#2 New Releases) |
| **#100millionclub** | ReelShort | Female/Romance | **Taming My Bullies** | Revenge + Campus/sports heat | 굴욕/배신 후 첫 반격 |
| **438.7K / 60화** | ReelShort | Female/Romance | **I'm Done Being Your Simp** | Revenge + High-status partner | 굴욕/배신 후 첫 반격 |
| **App 50M+ DL 슬레이트** | NetShort | Male/Power fantasy | **The Discarded Ace** (AI 직접작) | Hidden + Revenge + Progression | 정체 공개 지연 |

**관찰:**
- ReelShort 매출 1군 = **Werewolf · Alpha · Fated Mate** (191M / 114M / 46M — 거의 모두 fated mate 운명짝 변주).
- ReelShort 매출 2군 = **Campus revenge / sisterhood / Toxic relationship 복수** (76M / 100M+).
- GoodShort = **Disowned Daughter + Fake Heiress + 가족 재상봉** (5.3M·22.7M, Natalie 시리즈가 가장 강함).
- DramaBox = **Secret Billionaire / CEO Hidden Identity + Flash Marriage**.
- NetShort = 대량 카탈로그 (release date 메타만 노출, 실제 view 정량 검증 약함 — 단 AI 직접작 슬레이트 = `App 50M+ 다운로드`라는 외부 신호).

### 정성 강력 (대형 플랫폼·SNS·언론 노출 + 매출 신호)

- **GoodShort**: 22.7M / 2.6M followers — `A Blind Date with my Mr. Meant-to-Be`
- **DramaBox**: Business Insider 노출 + 24h 3M views #2 New Releases — `Summer Honeymoon with My Secret Billionaire`
- **ReelShort**: 53.6M/56M 검색 노출 + Facebook 강력 댓글 — `The Cooking Queen: A Recipe for Divorce`
- **DramaBox**: 61eps + homepage Must-sees — `Faking It with the Hockey Captain`
- **DataEye 2026 Q1 hotness 15.516M·소재 4만+** — NetShort AI 직접작 슬레이트 (`The Discarded Ace` 등)

---

## 2. 메이저 트로프 매트릭스 (매출·등장 빈도 통합)

`04_TROPE_INDEX` 81 ranked tropes 중 등장 빈도 + 매출 신호 매핑.

### Tier S — 매출 검증된 메이저 트로프 (15+ 작품 + 정량 view 검증)

| 트로프 | 등장 | 플랫폼 분포 | 매출 검증 | target |
|---|---|---|---|---|
| **Revenge** (대문자/소문자 합) | 26 | 5개 플랫폼 전부 | 76.6M (Sisterhood) / 100M+ (Taming Bullies) / 1.3M (Last Time I Forgive) | Female |
| **CEO** | 17 | 5개 플랫폼 | DramaBox Summer Honeymoon 24h 3M | Female |
| **Werewolf / Fated Mate / Alpha** | 14+5 (mate)+5 (academy) = 24 | DramaBox·Wave·Good·ReelShort | **191.9M / 114.7M / 46M** (전부 ReelShort top) | Female |

### Tier A — 매출 강한 메이저 (10+ 작품, 일부 정량 검증)

| 트로프 | 등장 | 플랫폼 | 매출 신호 | target |
|---|---|---|---|---|
| Mafia | 10 | 4개 | DramaWave Mafia King 5.0M | Female |
| Karma Payback | 10 | NetShort 집중 | 100점 + AI 슬레이트 | Female / Mixed |
| All-Too-Late | 8 | DramaBox·NetShort·ReelShort | 정성 검증 | Female |
| Enemies-to-Lovers | 8 | DramaBox·NetShort·ReelShort | DramaBox 61eps Faking It | Female |
| Fantasy (남성 포함) | 8 | 5개 플랫폼 | AI 슬레이트 50M+ App DL | Male / Mixed |
| Second Chance | 8 | 5개 플랫폼 | NetShort Till We Meet Again | Female |
| **BL** | 8 | DramaWave·GoodShort·ReelShort | hockey 변주 (Pucked) | BL/Queer (소수지만 강력) |
| Regret | 8 | DramaBox·DramaWave·GoodShort | His Love Was A Lie homepage feat. | Female |
| Contract Marriage | 7 | 4개 플랫폼 | Married for Greencard 322.6K stars / 58 eps | Female |

### Tier B — 보조 변주 (3-7 작품)

Hidden Identity / Forbidden Love / Pregnancy / Heiress / Family Revenge / Hockey / Disowned Daughter / Fake Dating / Hidden CEO / Fated Mate / Substitute Bride / Strong Female Lead / Stepbrother / Multiple Identity / Age Gap.

### Tier C — Niche 또는 신소재 (1-2 작품)

Wish-Fulfillment / Sleeping Beauty Inversion / Mute Wife / Nine-Tailed Fox / Mature Romance (Love at Fifty) / Eastern Fantasy / Action (King of Guns 류).

### 카테고리 분리

| 분류 | 트로프 클러스터 |
|---|---|
| **여성향 메인 결제 엔진** (압도적 매출) | Revenge / CEO / Werewolf·Fated Mate·Alpha / Mafia / Hidden Identity / Hidden CEO / Contract Marriage / Fake Heiress |
| **여성향 보조 변주** | All-Too-Late / Enemies-to-Lovers / Second Chance / Substitute Bride / Pregnancy / Stepbrother / Forbidden Love |
| **남성향 메인** (AIGC 후보 집중) | Fantasy-Male / System / Underdog Rise / Return King / Karma Payback / Progression/spectacle |
| **남성향 보조** | Eastern Fantasy / Martial Arts / Multiple Identities / Gambling / Otome (역하렘) |
| **가족극 (믹스)** | Disowned Daughter / Fake Heiress / Child Recognition / Family Separation / Child Swap / Hidden Heir |
| **AIGC 후보 트로프** | Fantasy-Male / System / Werewolf / Beast Awakening / AI Microdrama / Direct/Explicit AI |

---

## 3. 카테고리·타깃·플랫폼 매출 분포

### 플랫폼별 강세 카테고리 (A_Core 기준)

| 플랫폼 | A_Core | 강세 카테고리 |
|---|---|---|
| **NetShort** | 42 | Female/Romance (18) + Male/Power fantasy (12) — **양극단 강세**. AI 직접작 슬레이트의 본진. 단 매출 검증은 release date 메타만 |
| **GoodShort** | 32 | Family regret (9) + Female/Romance (11) + Family-romance (6) + Male (6). **가장 균형 + 명시적 view 신호 (22.7M·5.3M)**. Titan Era 시리즈 = AIGC/판타지 핵심 |
| **ReelShort** | 17 | Female/Romance (10) — 좁지만 **정량 view 1군** (191M·114M·76M·46M). werewolf·alpha·fated mate·campus revenge |
| **DramaBox** | 9 | Female/Romance (6) — Hockey BL·Hidden CEO·Cheating regret. **Business Insider 노출 + homepage Must-sees** |
| **DramaWave** | 6 | 가장 약한 A_Core — 단 **AI 직접작 (When the Moon Hides Crown)** + Hockey + Mafia. 5.31M subscriber base |

### Target × 플랫폼 인사이트

| target | 압도 플랫폼 | 매출 1군 트로프 |
|---|---|---|
| **Female / Romance** | NetShort(18) · GoodShort(11) · ReelShort(10) · DramaBox(6) | Werewolf+Fated Mate / Revenge / CEO / Contract Marriage / Substitute Bride |
| **Female / Family-romance** | GoodShort(6) · ReelShort(3) · NetShort(2) | Disowned Daughter / Fake Heiress / Mafia Majesty / Nine-Tailed Fox |
| **Family regret / mixed** | GoodShort(9) · NetShort(5) | Disowned Daughter (Natalie) / Bricklaying Worker Hero / 가족 재상봉 |
| **Male / Power fantasy** | NetShort(12) · GoodShort(6) · ReelShort(2) | Fantasy-Male+System / Return King / Karma Payback / AI Direct |
| **Female / Revenge-SFL** | NetShort(2) only | Corporate Warfare / Eastern Fantasy |

**핵심:** 라이브러리에서 **가장 명확히 매출 검증된 1군 = ReelShort Female/Romance Werewolf/Alpha/Fated Mate**. 191.9M·114.7M·76.6M·46M 모두 ReelShort 여성향.

---

## 4. AIGC 트랙커 (42 작품) — 후보 + 약점

### AIGC-friendly·Direct/Explicit AI·AIGC/Animation candidate

| 라벨 | 작품 (priority 상위) |
|---|---|
| **AIGC/Animation candidate** (high VFX leverage) | NetShort: My Wife Cheated→God / OMG Demon's Husband / One Move God Mode / 1000 Years in Loop / Godmaker's Return / Lv.1 Legend / Limitless Evolution / Betrayed I Rule the Ocean / GoodShort: Titan Era (Ten Divine Beasts) / Bite to the Top |
| **Direct/Explicit AI** (AI 직접 제작 명시) | NetShort: **The Discarded Ace** / 說好的乙遊戀愛呢？(Chinese otome) — DataEye 2026 Q1 hotness 15.516M / DramaWave: **When the Moon Hides Crown** (Werewolf Academy) |
| **AIGC-friendly genre** | GoodShort: My Exclusive Wish Granter / Romance System in a Dead World / NetShort: Baby Tycoon & Reward System / After My Slumber Gods Repent / The 5-time rejected luna / DramaWave: Attribute Seizer Undead Overlord |
| **AI-theme only** | NetShort: Divorced & Unmasked: The AI Queen Rules |

### 매출 검증된 AIGC (정량)

- **The Discarded Ace** (NetShort, Male/Power fantasy, Direct AI) — DataEye 2026 Q1 hotness 15.516M / TopMarketing AI 대표작 명시
- **Titan Era: Ten Divine Beasts Rise with Me** (GoodShort, Male/Power fantasy) — Creation 2026-01, 2.3K+ GoodShort views, Dailymotion 재유통 활발
- **One Move God Mode** (NetShort, Male) — YouTube playlist 141K+ / 일부 재업로드 2M
- **When the Moon Hides Crown** (DramaWave, AI-generated) — 평가 score 78 / Werewolf Academy 변주 (여성향이지만 platform side는 mixed)

### AIGC 약점 (라이브러리 관찰)

1. **AIGC 1군 = 남성향 판타지 / 시스템 / 무쌍·먼치킨에 집중**. 여성향 다크 로맨타지·후회남·재벌극은 AIGC 사례 거의 0 (When the Moon Hides Crown 정도).
2. **DramaWave가 AIGC/AI 직접작 비중 가장 큼** (10건) 그러나 매출 검증 약함 (Born with Magic은 D_Verify 52점).
3. NetShort AI 직접작 슬레이트는 **App 다운로드 50M+ 슬레이트 노출**이라는 신호 있으나, **개별 작품 view 수치 검증은 어려움**.
4. **AIGC 강점 (시트 일관 기재):** "VFX·세계관·시스템 UI·비현실 스케일을 직접 보상화 → High leverage" — 즉 **시각 보상 큰 장르 (판타지·시스템·진화·괴수)** 가 AIGC 정합.
5. **AIGC 약점 (시트 일관 기재):** "아이/가족 감정은 직관화하되 섬세한 연기는 과신 금지 → Medium leverage" — 즉 **세밀한 표정·관계 깊이 의존 장르는 AIGC 약점**.

---

## 5. desire_engine × conversion_engine 패턴 (A_Core 106작)

### Desire engine 분포 (compose count, 중복 가능)

| engine | A_Core 등장 |
|---|---|
| **Revenge/regret payoff** | 51 |
| **Hidden-identity reveal** | 42 |
| **High-status partner/authority** | 34 |
| **Child/family reunion** | 30 |
| Core melodrama hook | 13 |
| Progression/spectacle | 13 |
| Campus/sports heat | 4 |

### 핵심 조합 (실제 등장 빈도)

| 조합 | 등장 | 대표작 |
|---|---|---|
| Hidden-identity + Revenge + High-status | 15 | Step Aside King of Capital / Godmaker's Return / Cooking Queen |
| Hidden-identity + Revenge + Child/family | 12 | Blood and Bones / 불꽃 속의 귀환 / Family Framed Me |
| Hidden-identity + Revenge | 11 | Marry Father-in-Law for Revenge |
| Hidden-identity + High-status | 19 | Summer Honeymoon Secret Billionaire / Fated To My Forbidden Alpha |
| Hidden-identity + Child/family | 10 | Fated Mate of Nine-Tailed Fox / Till We Meet Again |
| Revenge + Child/family | 15 | Daddy Can You Hear Me Cry / My Family Framed Me |
| Revenge + High-status | 10 | Cooking Queen / I'm Done Being Your Simp |
| Single Revenge only | 32 | His Love Was A Lie / No More Love Just Trillions |
| Single High-status only | 24 | From Victim to Mrs. CEO / Fated to My Homeless Billionaire Alpha |

**관찰:** **결제 엔진 = "Hidden-identity reveal" + "Revenge/regret payoff" + "High-status partner"** 의 3개 핵심 atom 결합이 압도적. **Child/family reunion**은 가족극·후회극에서 강력하나 다크 로맨타지에서는 약함.

### Conversion engine 분포 (6 패턴 — 시트가 표준화)

| pattern | A_Core | 핵심 메커니즘 |
|---|---|---|
| **정체/권력 공개 직전까지 결핍·오해를 누적** | 88 | 가장 메이저. Hidden-identity 결합 |
| **무료=결핍·예고 / 유료=보상·진실·역전** | 79 | 보편 phase 분리 모델 |
| **굴욕/배신 후 첫 반격 예고, 본격 응징 지연** | 51 | 복수극 핵심 |
| **강한 케미·보호/소유 신호 + 감정 확정 지연** | 38 | 다크 로맨타지·후회남 |
| **첫 각성·첫 스킬만 보여주고 상위 보스·진짜 권위는 유료로 이월** | 18 | 남성향 progression |
| **혈연/아이 진실 반쯤 드러내고 대면·인정은 지연** | 13 | 가족극·아이물 |

→ 6 패턴 = **paid vertical conversion 시장의 거의 모든 결제 트리거를 포괄**.

---

## 6. 본 시스템 baseline 정합·반증

### 정합 (라이브러리 데이터로 검증됨)

#### a. `feedback_paid_vertical_viewer_psychology` — 사적 즐김·직접 욕망 자극

**정합 강함.** Tier S 트로프 (Revenge / Werewolf-Fated Mate / CEO Hidden Identity) 모두 **사적 욕망·금기 끌림·통쾌함의 환상**. "옳은 메시지" 톤 작품 0. 도덕 우위·예술 톤 작품 거의 없음 (있다면 매출 부진 슬롯 — Demon Lord류).

#### b. `feedback_50_episode_serial_engines` — 50화 = 작은 보상 + 큰 욕망 확장

**부분 정합.** 라이브러리 작품 중 50화 운영 명시 작품 = 60화 (Sisterhood of Lies / Last Time I Forgive / Faking It with Hockey Captain) · 68화 (Fated Mate Nine-Tailed Fox) · 41화 (I'm Done Being Your Simp) · 100화 (Pengantin CEO). **즉 paid vertical 표준 = 50-100화**. 시트가 회차별 비트 데이터를 안 담고 있어 "매화 7 쾌감" 직접 검증은 X.

#### c. `feedback_female_buy_engine_relational` — 구매 엔진 5 (위험 끌림·관계 변화·공개 선택·육체 긴장·상호 claim)

**정합 강함.** 매출 1군 ReelShort werewolf/alpha = **Possessive Claim / Fated Mate / High-status partner + 압도적 매력 + 공개 마킹** 의 직접 결제 엔진. `Strong Female Lead` 트로프는 5개만 등장 — 매출 1군과 거리 (Watch Out I'm The Lady Boss / Queen Mom Rules / Delta Force Queen Returns — 모두 중간 매출 또는 검증 약함).

#### d. `feedback_character_situation_appeal` — 3축 (캐릭터·상황·관계)

**정합 + 보강.** 라이브러리 상위 작품 = 상황 매력 (재벌·werewolf·mafia·드래곤·전이) + 관계 변화 (fated mate·flash marriage·return king) + 캐릭터 매력 (alpha·CEO·disowned daughter·secret heir). **상황 매력이 가장 큰 결제 트리거 — 시청자가 "이 세계에 들어가고 싶다" 신호**.

#### e. `feedback_reference_market_verification` — Demon Lord 매출 부진

**정합.** Demon Lord-tagged 작품은 본 라이브러리 상위에 없음. **OMG! I Become a Demon's Husband** (NetShort) = 100점 / 男主·하렘·Martial Arts 톤이지 다크 로맨타지 X. "Demon" 키워드 자체는 회피 대상 X — **"Demon Lord 마크 의존·계약·장부·판결 여주" 운영 방식이 회피 대상**.

#### f. `feedback_paid_vertical_intuitive_money_triggers` — 직관 신체 장치·EP8 5미완성·무료 보상 균형

**정합.** ReelShort 매출 1군 werewolf/fated mate = **fated mate bite·alpha mark·possessive claim**의 직관 신체 장치. **손목 룬·trace·glow 식 장치 의존 작품은 라이브러리 상위에 없음**.

### 반증·정정 권고

#### 반증 1 — **여성향 "강한 여주" 회피는 일률 적용 위험**

`feedback_female_buy_engine_relational`은 "Strong Female Lead·판결형 여주 → 매출 약화" 명시. 그러나 라이브러리 정량 검증 1군 중:
- **I'm Done Being Your Simp** (ReelShort 438.7K 41화 / 100점) = 환생 + 여성 CEO와 손잡고 복수 — 강한 여주
- **Marry Me? No, Killed Me!** (NetShort 100점) = Corporate Warfare 강한 여주
- **No More Love, Just Trillions** (NetShort 100점) = Corporate Warfare 강한 여주
- **Lv.1 Legend? Sweet** (NetShort Female/Revenge-SFL 100점) = 판타지 세계 강한 여주
- **Queen Mom Rules** (Strong Female Lead 명시 / 100점 슬롯) = 강한 어머니 여주

→ **"강한 여주 자체가 X"가 아니라 "판결형·도덕 우위·욕망 부재 강한 여주가 X"**. 본 메모리는 정확하나, 적용 시 "강한 여주 = 회피" 식 과잉 적용 가능성 — **트로프 자체 X / 운영 방식이 매출 결정** 룰 강조 권고.

#### 반증 2 — **AIGC 1군 = 남성향이며 여성향 AIGC 매출 검증 약함**

본 시스템은 OFFERING (여성향 AIGC 다크 로맨타지)이 핵심 작품. 그러나 라이브러리에서:
- AIGC 검증 1군 = **모두 남성향 판타지·시스템·무쌍** (Titan Era / Discarded Ace / One Move God Mode / 1000 Years Loop)
- 여성향 AIGC 검증 = **거의 없음** (DramaWave When the Moon Hides Crown 78점 정도)

→ **OFFERING (여성향 AIGC 다크 로맨타지) = 시장 검증 매우 약한 카테고리**. 시스템이 OFFERING의 비주얼·tone 설계 시 **레퍼런스 부재 + 첫 진입 리스크 인지** 권고. 실패하면 페이오프가 큰 빈 슬롯, 그러나 검증된 신호 없음.

#### 반증 3 — **메모리 baseline은 다크 로맨타지·CEO 한정 — 가족극·복수극 보강 부재**

본 시스템 메모리는 다크 로맨타지·high-heat·sensual·alpha 중심. 그러나 라이브러리 매출 검증 강세:
- **GoodShort 22.7M** = `A Blind Date with my Mr. Meant-to-Be` — 가족극·아이 재회 (sensual·alpha X)
- **GoodShort 5.3M** = `Blood and Bones of the Disowned Daughter` — Disowned Daughter 복수극 (sensual·alpha X)
- **DramaWave 580K** = `Daddy, Can You Hear Me Cry?` — 가족 분리·아이 swap 비극 멜로

→ **여성향이지만 sensual·heat·alpha 약하고 "아이 재상봉·가족 화해·복수 회수"가 결제 엔진**인 슬롯 = **`Child/family reunion` desire engine 30 등장**. 시스템에 이 슬롯 baseline 부재 — `feedback_female_buy_engine_relational`은 sensual·dark romantasy 중심. 가족극·후회 멜로는 **다른 결제 엔진** 가능.

→ 권고: `feedback_female_buy_engine_relational` 또는 신규 메모리에 **여성향 두 엔진 분리** 명시.
- **A 엔진:** Werewolf·Alpha·CEO·Dark romantasy = 압도적 매력 + 위험 끌림 + 육체 긴장 + 공개 소유 + 상호 claim
- **B 엔진:** 가족극·아이 재회·후회 멜로·Disowned Daughter = 결핍 누적 + 가족 분리·재상봉 + 정체 공개 지연 + 굴욕→통쾌 회수

#### 반증 4 — **AI 직접작 슬레이트가 정량 view 검증 약하나 외부 신호 강함**

본 시스템 메모리는 AIGC의 매출 검증을 "TITAN BORN 50화 완결" 수준으로만 보유. 라이브러리에서:
- NetShort `The Discarded Ace` = **DataEye 2026 Q1 hotness 15.516M / TopMarketing AI 대표작**
- NetShort `說好的乙遊戀愛呢？` = 같은 슬레이트 / 중화권 AIGC + otome 역하렘
- DramaWave `When the Moon Hides Crown` = AI-generated + Werewolf Academy

→ **AIGC = 시장 진입기 / 외부 매체 (DataEye·TopMarketing·Business Insider)는 AIGC를 대표작으로 인식**. 그러나 시청자 view·결제 정량 검증은 약함 → **마케팅·언론·플랫폼은 AIGC를 강하게 푸시하나 시청자 매출은 아직 검증되지 않은 단계**. 시스템 메모리 보강 권고.

---

## 7. 50화 운영 인사이트 (라이브러리 관찰)

데이터 한계: 라이브러리는 logline·desire/conversion engine만 보유. EP별 비트는 없음. 단 다음 운영 신호 추출 가능:

### 회차 분량 신호 (정량)
- ReelShort `Sisterhood of Lies` = **60화 완결** (76.6M views)
- ReelShort `Faking It with Hockey Captain` (DramaBox) = **61 eps homepage Must-sees**
- ReelShort `Fated Mate of Nine-Tailed Fox` = **68 eps / 2M views**
- ReelShort `The Last Time I Forgive` = **60 eps / 1.3M**
- ReelShort `I'm Done Being Your Simp` = **41 eps / 438.7K**
- GoodShort `Married for Greencard` = **58 eps / 322.6K stars**
- GoodShort `Pengantin CEO Yang Bisu` = **100 eps / 3M likes** (장기 시리즈)

→ **paid vertical 회차 = 40-100화 범위. 평균 60-70화 메이저. 50화는 표준이라기보다는 작품별 가변**.

### 무료 vs 유료 conversion engine 일관성
시트의 모든 conversion engine = "**지연**" 패턴 명시:
- "감정 확정은 지연"
- "본격 응징은 지연"
- "유료부로 이월"
- "결핍·예고"·"보상·진실·역전"

→ 본 시스템 `feedback_paywall_force_protection` (8화 페이월 약화 X / 정보 비대칭) 정합 강함. **paid vertical 보편 룰 = 무료에서 첫 증거만 / 큰 보상은 유료로 유예**.

---

## 8. 트로프 자체 vs 운영 인사이트

### 트로프 자체 X / 운영이 매출 결정 — 사례

#### CEO·재벌 트로프
- **매출 강세:** Summer Honeymoon with My Secret Billionaire (DramaBox 24h 3M) — 정체 숨김 + 플래시 결혼 + 정체 공개 지연
- **매출 검증 약함:** 단순 CEO 로맨스 — 정체 숨김 없이 빠른 관계 확정
- **차이:** 같은 CEO도 **Hidden Identity + Flash Marriage + 정체 공개 지연**으로 운영하면 매출 ↑

#### Revenge 트로프 (가장 메이저, 26 등장)
- **매출 강세:** Sisterhood of Lies (76.6M) — Campus + Twin revenge + 굴욕/배신 후 첫 반격 예고
- **매출 강세:** The Last Time I Forgive (1.3M) — Cheating + Flash Marriage + 굴욕 후 첫 반격
- **차이:** Revenge 단독 X / **굴욕 누적 → 첫 반격 → 본격 응징 지연** 운영 룰이 핵심

#### Werewolf·Fated Mate 트로프 (Tier S)
- **매출 1군:** Fated To My Forbidden Alpha (191.9M) — Hidden Identity + Love Triangle + High-status partner
- **매출 2군:** Accidental Surrogate for the Alpha (114.7M) — Accidental Pregnancy + Alpha Baby Daddy
- **공통 운영:** **fated mate 운명 표지 (mark/bond)를 관계 변화·소유 선언·신체 결속의 직접 신호**로 운영. 시스템·설정 설명 X.

### 운영 약점이 매출 약화 — 사례

#### Demon Lord (시스템 메모리·라이브러리 둘 다 명시)
- 트로프 자체 (demon + mark + 다크 로맨타지) X
- 운영 = **mark 의존 + 판결형 여주 + 계약·장부 메타 누적 + 시스템 해설자 남주** = 매출 약화

#### Strong Female Lead 트로프 (5개만 등장)
- Watch Out I'm The Lady Boss / Queen Mom Rules / Delta Force Queen Returns / Love Is a Game I Play for Power / 5개
- 매출 검증은 모두 중간 또는 약함
- 단 Queen Mom Rules 100점 슬롯 = **여성 강함 + 가족 보호 + Family Revenge 결합** 운영 — 트로프 자체 X / 가족 회수·복수 운영

---

## 9. 신규 발견 인사이트 (3-5건)

### 인사이트 1 — **ReelShort werewolf/alpha/fated mate = 검증된 글로벌 매출 1군**

191.9M (Fated To My Forbidden Alpha) + 114.7M (Accidental Surrogate for the Alpha) + 46M (Fated to My Homeless Billionaire Alpha) = ReelShort 여성향 매출 압도. 트로프 클러스터:
- **Werewolf + Fated Mate + Alpha Possessive Claim**
- **High-status partner (Billionaire / King 결합 가능)**
- **Hidden Identity reveal (Mate 진정성·신분 공개 지연)**

→ 본 시스템 `feedback_dark_romantasy_engine` 의 Fated Encounter → Forbidden Bond → Possessive Claim 사이클과 정합. **OFFERING은 같은 카테고리이나 AIGC 진입 — 검증 ReelShort 룰 차용 가능**.

### 인사이트 2 — **GoodShort = 가족극·Disowned Daughter·아이 재회의 매출 본진**

GoodShort A_Core 32 / Family regret 9 / Female Family-romance 6 / 매출 검증 (22.7M·5.3M). **`Blood and Bones of the Disowned Daughter` (Natalie)는 7회 reference 등재 — 사실상 GoodShort 대표 모델**. 라이브러리에서 GoodShort = **"굴욕 누적 → 정체 공개 → 가족 복수 회수"** 가 카테고리 본질.

→ 본 시스템에 **가족극·Disowned Daughter slot 강화 권고**. 여성향이지만 다크 로맨타지·sensual·alpha X.

### 인사이트 3 — **conversion_engine 6 패턴이 paid vertical 보편 룰**

라이브러리 287작 중 conversion engine 6 패턴 외에는 거의 없음:
1. 정체/권력 공개 직전까지 결핍·오해 누적 (88) 
2. 무료=결핍·예고 / 유료=보상·진실·역전 (79)
3. 굴욕/배신 후 첫 반격 예고, 본격 응징 지연 (51)
4. 강한 케미·보호/소유 신호 + 감정 확정 지연 (38)
5. 첫 각성·첫 스킬만 보여주고 상위 보스는 유료로 이월 (18)
6. 혈연/아이 진실 반쯤 드러내고 대면·인정 지연 (13)

→ **paid vertical 시스템의 전체 결제 메커니즘이 6개**. 시스템 메모리에 **"6 conversion 패턴"을 표준화** 권고. 작품 phase_3 청사진 단계에서 6 중 어떤 패턴을 메인 + 보조로 운영하는지 명시 의무화 권고.

### 인사이트 4 — **AIGC = 남성향 판타지·시스템 1군 / 여성향 다크 로맨타지 미검증**

AIGC 검증 1군:
- **NetShort 남성 AI 직접작 슬레이트** (Discarded Ace / 說好的乙遊戀愛呢? / Limitless Evolution) = DataEye 2026 Q1 hotness 15.5M
- **GoodShort 남성 Titan Era** (Ten Divine Beasts) = AIGC 대표 모델
- **DramaWave AI Microdrama Global Expansion cluster**

여성향 AIGC 검증 = `When the Moon Hides Crown` (Werewolf Academy / 78점) 정도. **OFFERING과 직접 비교 가능 작품 없음 → 여성향 AIGC 다크 로맨타지는 시장 진입기 빈 슬롯**. 페이오프 큼 / 그러나 검증 신호도 큼·매출 보장도 X.

### 인사이트 5 — **여성향 결제 엔진 = 두 종류로 분리해야 함**

라이브러리 데이터로 명확히 분리됨:

**A 엔진 (High-heat / Dark romantasy / Alpha):**
- desire = High-status partner / Hidden Identity reveal / 압도적 매력
- conversion = 강한 케미·보호/소유 신호 + 감정 확정 지연
- 검증: ReelShort werewolf 1군 (191M·114M·46M)
- 트로프: Werewolf · Fated Mate · Alpha · CEO Hidden Billionaire · Mafia

**B 엔진 (Revenge / Family / Disowned Daughter / 가족 회수):**
- desire = Revenge/regret payoff + Child/family reunion + Hidden Identity reveal
- conversion = 굴욕/배신 후 첫 반격 예고 + 정체 공개 지연 + 혈연·아이 진실 지연
- 검증: GoodShort Natalie (5.3M) · DramaWave Daddy Can You Hear (580K) · NetShort Marry Father-in-Law (100점)
- 트로프: Disowned Daughter · Fake Heiress · Karma Payback · Substitute Bride · Family Revenge

OFFERING (다크 로맨타지) = A 엔진 / SHE STOLE MY FACE (여성향 현대 복수극) = B 엔진.

→ **시스템 메모리에서 두 엔진을 분리 명시 권고**. `feedback_female_buy_engine_relational`은 A 엔진 중심 — B 엔진 baseline 부재.

---

## 10. 시스템 메모리 갱신 권고 (우선순위 순)

### P1 — 신규 메모리 (지금 없는 baseline)

**`feedback_paid_vertical_6_conversion_patterns.md`** 신규 작성 권고.
- paid vertical 287작에서 검증된 6개 conversion 패턴 표준화
- 모든 phase_3 청사진에서 6 중 메인 + 보조 명시 의무

### P2 — 기존 메모리 보강

**`feedback_female_buy_engine_relational.md` 보강**:
- "여성향 두 엔진 분리" 명시 (A=Dark romantasy / B=Revenge·가족 회수)
- B 엔진 baseline 추가 — 트로프 (Disowned Daughter·Fake Heiress·Karma Payback) + conversion (혈연·아이 진실 지연 + 굴욕→통쾌 회수)
- 사례: GoodShort Natalie 시리즈 / DramaWave Daddy Can You Hear / NetShort Marry Father-in-Law

**`feedback_female_lead_agency_balance.md` 정정**:
- "강한 여주 = X" 과잉 적용 회피
- 라이브러리에서 100점 강한 여주 작품 5+ 존재 (I'm Done Being Your Simp / Marry Me No Killed / Lv.1 Legend / Queen Mom Rules)
- 룰: **트로프 X / 운영이 매출 결정** — 판결형·도덕 우위·욕망 부재 강한 여주만 회피

**`feedback_reference_market_verification.md` 보강**:
- 라이브러리 정량 검증 상위 작품 list 추가:
  - ReelShort 1군: Fated To My Forbidden Alpha (191.9M) / Accidental Surrogate (114.7M) / Sisterhood of Lies (76.6M)
  - GoodShort 1군: A Blind Date with my Mr. Meant-to-Be (22.7M) / Blood and Bones (5.3M)
  - DramaBox 1군: Summer Honeymoon Secret Billionaire (24h 3M)
  - DataEye 검증 AIGC: The Discarded Ace (Q1 hotness 15.5M)

### P3 — 기존 메모리 정합 확인

**`feedback_dark_romantasy_engine.md` 검증**:
- Fated Encounter → Forbidden Bond → Possessive Claim → Bond Deepens → Public Recognition → Mate Sealed 사이클은 라이브러리 ReelShort 1군과 정합
- 단 라이브러리 1군은 모두 ReelShort 실사 — **OFFERING은 AIGC = 검증 1군과 포맷 차이**. 진입기 리스크 명시 권고.

**`feedback_50_episode_serial_engines.md` 검증**:
- 라이브러리 회차 = 40-100화 가변. 50화는 표준이 아닌 가변 슬롯.
- "50화 = 작은 보상 + 큰 욕망 확장" 룰은 정합. 다만 회차 자체는 작품별 결정.

### P4 — 신규 메모리 (선택)

**`feedback_aigc_market_entry_signal.md` 신규 (선택)**:
- AIGC 1군 = 남성향 판타지·시스템·무쌍 (검증)
- 여성향 AIGC 다크 로맨타지 = 검증 1군 부재 (진입기)
- 외부 매체 (DataEye·TopMarketing·Business Insider)는 AIGC 강하게 푸시 / 시청자 매출 검증은 약함
- AIGC 강점 = "VFX·세계관·시스템 UI·비현실 스케일 직접 보상" / 약점 = "섬세한 표정·관계 깊이 의존 장르"

---

## 핵심 한 줄 (시장 baseline 결론)

> **paid vertical 시장 = 6 conversion 패턴 + Hidden Identity·Revenge·High-status·Child/family·Possessive Claim 5개 desire atom의 조합 시장.**
>
> **여성향 매출 = 두 엔진 (A: Dark romantasy + Alpha / B: Revenge + 가족 회수). 단일 baseline로 묶지 말 것.**
>
> **AIGC = 남성향 판타지·시스템 검증 / 여성향 다크 로맨타지는 진입기 빈 슬롯. OFFERING은 검증 1군과 포맷 차이 인지 필요.**
>
> **메이저 트로프 자체 X / 운영 방식이 매출 결정 — Demon Lord = 트로프 X / 운영 약점이 매출 약화 원인.**
