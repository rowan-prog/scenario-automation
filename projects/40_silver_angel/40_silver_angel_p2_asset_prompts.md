# 그가 버린 흑발의 연인 — 제작 참고 어셋 생성 지시서 (Codex · GPT Image)

- 작성 2026-11-05 · 기준 대본 = `C:\Users\Rowan\Downloads\_The Black-Haired Love He Threw Away_Script.docx` (최종고 · 50화)
- 뽑을 것 = **캐릭터 시트 15장**(5명 × 시안 3) + **배경 6장**(3곳 × 시안 2) = 21장
- 저장 = `C:\Users\Rowan\scenario-automation\projects\40_silver_angel\assets\` · 파일명 = `40_OLIVIA_A.png`, `40_BG1_A.png` 식

---

## 0. Codex에게 — 먼저 읽고 지킬 것

1. **한 장 = 새 대화 하나.** 앞 장에서 만든 얼굴이 다음 장에 섞이면 다 비슷해진다. 한 대화에서 여러 장을 뽑지 마.
2. 프롬프트 = **해당 시안 블록 + 맨 끝에 [공통 블록] 그대로 붙이기.** 공통 블록을 줄이거나 빼지 마.
3. 사이즈 = **가로 최대 해상도**(최소 1536×1024, 더 크게 되면 최대로). 캐릭터 시트는 패널이 많아서 작게 뽑으면 얼굴이 뭉개진다.
4. 15장 다 뽑으면 **얼굴만 잘라서 한 줄로 늘어놓고** 맨 아래 §4 확인표대로 본다. 걸리는 건 다시 뽑는다.
5. 실존 배우·셀럽 이름은 프롬프트에 쓰지 마.

### 지난번 시안이 망한 이유 — 이번엔 이렇게 막는다

지난번 실패본 = `C:\Users\Rowan\Downloads\ChatGPT 이미지 2026년 11월 5일 오후 09_06_03-1.png` ~ `…09_06_10-6.png` (6장)

| 지난번 문제 | 이번에 막는 법 |
|---|---|
| **아줌마·아저씨 얼굴**(제일 심각) | 나이를 숫자로 박는다(20~25살). "mature, older, middle-aged, wrinkles, eye bags"를 피할 것에 넣는다. 화면 나이가 26살 넘어 보이면 무조건 다시 |
| **못생김**(북미 여자들이 안 좋아하는 얼굴) | "넷플릭스 로맨스 주인공 / 패션 캠페인 모델급"으로 박는다. 깡마름·퀭함·거친 피부·젖은 머리·주근깨·모공을 피할 것에 넣는다 |
| **기괴함** | 귀는 작게 살짝만 뾰족하게. 화내거나 우는 표정도 예쁘게(입 크게 벌리기·찡그려 일그러지기 금지). 손가락 다섯 개. 패널마다 같은 얼굴 |
| **다 비슷하게 생김** | 사람마다 머리색·얼굴형·색깔을 아래 표대로 따로 박는다. 같은 금발 셋 금지 |
| **칙칙한 색** | 밝고 화사한 판타지. 어두운 무드·회색빛·세피아 금지 |
| 같은 테라스 배경 | 캐릭터 시트는 **배경 없는 밝은 회색 스튜디오** |

### 다섯 명 구분표 — 이 칸이 서로 안 겹쳐야 한다

| 인물 | 화면 나이 | 머리 | 색깔 | 한눈에 |
|---|---|---|---|---|
| 올리비아 (공작가 큰딸 · 여주) | 22 | **검은 긴 머리** (원래는 백금발 — 저주 팔찌 때문에 검게 됨) | 흰색·은색·잎사귀 초록 | 차갑고 센 미녀. 절대 안 비는 여자 |
| 가브리엘 (다크엘프 왕 · 남주) | 25 | **검은 머리** (올리비아보다 짧음) | 검정·보라·은색 | 눈가리개를 한 왕. 벗으면 보라빛 눈 |
| 데미안 (엘프 왕자 · 후회남) | 24 | **금갈색·갈색 계열** (제나 백금발과 확실히 다르게) | 아이보리·금색·청동·흙갈색 | 잘생긴 오만한 왕자. 바위·금빛 마법 |
| 제나 (공작가 작은딸 · 악녀) | 20 | **백금발** (사실은 염색 — 진짜는 검은 머리) | 연분홍·루비 빨강·금색 | 예쁜 척 우는 여우. 불 마법 |
| 다이앤 (공작 부인 · 새엄마 · 악녀) | **32로 보이게** | 와인빛 적갈색 업스타일 | 와인 레드·금색·검은 레이스 | 화려한 새엄마. 아줌마 느낌 0 |

> 다이앤은 제나 엄마지만 **화면 나이는 30대 초반**으로 간다(사용자 지시 = 전원 젊고 섹시하게). 공작은 이번에 뽑지 않는다(나이 든 아버지 역이라 아저씨 문제가 그대로 난다. 필요하면 따로 말할 것).

---

## 1. [공통 블록] — 캐릭터 시트 15장 전부 맨 끝에 그대로 붙인다

```
=== SHEET LAYOUT ===
One single large landscape character design reference sheet. Clean plain light-grey studio background, no scenery, no props in the background.
LEFT third: full-body turnaround of the SAME character, head to toe including shoes — front view, side profile view, back view — relaxed standing pose.
CENTER: one large bust shot (chest up), facing the camera, the most beautiful/handsome angle.
RIGHT third: a 3x3 grid of 9 face close-ups, each a different expression (listed above).
The face, hair, makeup, outfit and accessories are IDENTICAL in every panel — clearly the same person. Small clean name label at the top only.

=== LOOK ===
Photorealistic live-action fantasy romance, styled like the official cast photos of a big-budget streaming romance series. Bright, colorful, high-key lighting; soft flattering beauty light; vivid but tasteful color; crisp sharp focus.
The character is CLEARLY YOUNG — exactly the age stated above, fresh and youthful, an adult in their early twenties.
Strikingly attractive by North American standards: the kind of face women in the US swoon over. Women: gorgeous, sexy, glamorous romance-lead beauty. Men: handsome, sexy heartthrob, chiseled and clean-shaven.
Flawless healthy glowing skin, bright clear eyes, glossy thick voluminous hair, natural glam makeup (women), symmetrical refined features, fit attractive body.
Elf ears: small and only slightly pointed, mostly hidden by hair — subtle, elegant.
Even angry, cold or crying expressions stay beautiful: controlled, sharp, no distorted faces, no wide-open screaming mouths.
Correct anatomy, five fingers on each hand.

=== AVOID ===
middle-aged, older, mature-looking, matronly, motherly, fatherly, wrinkles, eye bags, dark circles, tired, gaunt, hollow cheeks, sunken eyes, weathered, gritty, rough skin, visible pores, freckles, oily skin, wet hair, stringy or greasy hair, thin hair, gray hair, beard, stubble, ethereal, otherworldly, alien, uncanny, grotesque, horror, big long elf ears, plastic doll skin, cartoon, anime, painting, desaturated, muted, dark moody grading, sepia, gloomy, low contrast, blurry face, mismatched faces between panels, extra fingers.
```

---

## 2. 캐릭터 시트 15장 — 시안 블록

시안 A·B·C는 **같은 인물의 다른 디자인 안**이다. 얼굴형·머리·의상이 셋 다 달라야 고르는 의미가 있다.

### 2-1. 올리비아 OLIVIA (여주)

꼭 지킬 것: **검은 긴 머리** · **오른쪽 손목에 가는 팔찌**(저주 팔찌) · **왼쪽 손바닥에 흰 붕대** · 세 시안 다 흰색·은색·초록 계열 · 차갑고 당당한 걸크러시 미녀(우는 얼굴이 기본값이 아님)

표정 9개 (세 시안 공통): 차갑게 내려다보기 / 비웃는 한쪽 입꼬리 / 싸울 때 매서운 눈(눈동자에 은빛이 번쩍) / 눈물을 참고 버티는 눈 / 가브리엘에게만 짓는 부드러운 미소 / 깜짝 놀람 / 명령하는 얼굴("벗어") / 이겼을 때의 여유로운 미소 / 유혹하는 눈빛

**OLIVIA_A — 클래식 로맨스**
```
Character: OLIVIA, elf duke's elder daughter, fantasy romance heroine. 22 years old.
Face: soft oval face, high cheekbones, large almond-shaped grey-green eyes with long lashes, small straight nose, full rosy lips, porcelain-fair glowing skin.
Hair: very long glossy jet-black hair in loose soft waves down to the waist, center part, with a faint silvery sheen where light hits it.
Outfit: pure white off-the-shoulder silk gown with a fitted corset bodice and delicate silver vine embroidery, flowing skirt, sheer white sleeves; elegant and sensual.
Accessories: a thin delicate silver bracelet on her RIGHT wrist; a clean white bandage wrapped around her LEFT palm.
Palette: white, silver, soft leaf green.
Expressions (9 close-ups): cold looking down, contemptuous half smirk, fierce battle glare with a silver glint in her eyes, eyes holding back tears without crying, soft tender smile, surprised, commanding stare, confident victorious smile, alluring seductive gaze.
```

**OLIVIA_B — 걸크러시 시크**
```
Character: OLIVIA, elf duke's elder daughter, fantasy romance heroine. 22 years old.
Face: heart-shaped face with a sharp elegant jawline, slightly upturned cat-eye shape, light silver-grey eyes, defined straight brows, fuller lower lip, warm ivory skin.
Hair: long sleek straight jet-black hair past the shoulders, deep side part, half-up with a slim silver hair pin, glossy and smooth.
Outfit: fitted deep emerald-green gown with a structured corset, high slit skirt over slim boots, ivory blouse sleeves with slashed cuffs, a short silver-trimmed cape on one shoulder; strong, sexy, girl-crush.
Accessories: a thin delicate silver bracelet on her RIGHT wrist; a clean white bandage wrapped around her LEFT palm.
Palette: emerald green, ivory, silver.
Expressions (9 close-ups): cold looking down, contemptuous half smirk, fierce battle glare with a silver glint in her eyes, eyes holding back tears without crying, soft tender smile, surprised, commanding stare, confident victorious smile, alluring seductive gaze.
```

**OLIVIA_C — 화려한 여왕풍**
```
Character: OLIVIA, elf duke's elder daughter, fantasy romance heroine. 22 years old.
Face: diamond-shaped face, prominent cheekbones, wide-set deep emerald eyes, softly arched brows, glossy nude-pink lips, light golden-ivory skin with a healthy glow.
Hair: long voluminous jet-black hair, a thin braided crown across the top, the rest falling in big glossy curls over one shoulder.
Outfit: champagne-silver gown covered in tiny sparkling beads like starlight, sweetheart neckline, fitted waist, sheer pale-green overlay cape trailing behind, delicate silver leaf circlet.
Accessories: a thin delicate silver bracelet on her RIGHT wrist; a clean white bandage wrapped around her LEFT palm.
Palette: champagne silver, pale sage green, white.
Expressions (9 close-ups): cold looking down, contemptuous half smirk, fierce battle glare with a silver glint in her eyes, eyes holding back tears without crying, soft tender smile, surprised, commanding stare, confident victorious smile, alluring seductive gaze.
```

### 2-2. 가브리엘 GABRIEL (다크엘프 왕 · 남주)

꼭 지킬 것: **검은 머리** · **보라빛 눈**(어두운 보라가 은은하게 빛남. 금색 눈 아님 — 최종고 기준) · **눈가리개 마스크**(눈만 가리는 얇고 고급스러운 띠. 괴상한 가면 아님) · 검정·보라·은색 · 소문엔 장애가 있다는 왕인데 실제로는 여유롭고 위험하게 섹시함

시트 구성 특별 규칙: **풀샷 3개 = 눈가리개 한 모습** · **바스트샷 = 눈가리개 벗은 얼굴(보라빛 눈)** · 표정 9개 중 앞 3개 = 눈가리개 한 채, 뒤 6개 = 벗은 채

표정 9개 (세 시안 공통): [눈가리개] 한쪽 입꼬리만 올린 미소 / [눈가리개] 차갑고 위험한 표정 / [눈가리개] 고개 살짝 기울인 여유 / [벗음] 올리비아만 보는 집착 어린 눈 / [벗음] 다정한 미소 / [벗음] 차가운 위협 / [벗음] 재밌다는 듯 웃음 / [벗음] 분노를 누른 눈 / [벗음] 유혹하는 눈빛

**GABRIEL_A — 근위대장 차림**
```
Character: GABRIEL, the Dark Elf King disguised as his own guard captain, fantasy romance male lead. 25 years old.
Face: strong square jaw, high cheekbones, straight nose, defined full lips, deep-set glowing dark violet eyes, fair cool-toned skin, clean-shaven.
Hair: short-to-medium jet-black hair, tousled and swept back, a few strands falling over the forehead.
Blindfold: a thin band of black silk with fine silver embroidery tied over his eyes, elegant, hair falling over it.
Outfit: fitted black guard-captain uniform — high-collared black doublet with silver buttons, black leather belt and gloves, a long black cape lined with deep violet, tall boots; broad shoulders, tall athletic build.
Palette: black, deep violet, silver.
Panel rule: full-body turnaround WITH the blindfold on; bust shot WITHOUT the blindfold showing glowing violet eyes; close-ups 1-3 with blindfold, 4-9 without.
Expressions (9 close-ups): one-sided smirk, cold dangerous look, amused head tilt, possessive intense gaze, tender smile, cold menace, laughing amused, suppressed anger, seductive smoldering gaze.
```

**GABRIEL_B — 왕의 정장**
```
Character: GABRIEL, the Dark Elf King, fantasy romance male lead. 25 years old.
Face: long oval face, sharp angular jawline, sculpted cheekbones, slightly hooded almond-shaped glowing violet eyes, straight dark brows, light olive skin, clean-shaven.
Hair: jet-black hair, longer, glossy, slicked back neatly to the nape with a slight wave.
Blindfold: an ornate band of fine silver filigree lace over the eyes, set with a small violet gem at the center, elegant and royal.
Outfit: royal long coat in black velvet with deep violet brocade and silver thread, structured shoulders, black high-collar shirt, a thin silver crown circlet, silver rings; regal, tall, broad-shouldered.
Palette: black, royal violet, silver.
Panel rule: full-body turnaround WITH the blindfold on; bust shot WITHOUT the blindfold showing glowing violet eyes; close-ups 1-3 with blindfold, 4-9 without.
Expressions (9 close-ups): one-sided smirk, cold dangerous look, amused head tilt, possessive intense gaze, tender smile, cold menace, laughing amused, suppressed anger, seductive smoldering gaze.
```

**GABRIEL_C — 섹시 캐주얼 왕**
```
Character: GABRIEL, the Dark Elf King, fantasy romance male lead. 25 years old.
Face: classic heartthrob face, softly square jaw, strong brow, deep glowing violet eyes with thick lashes, full lips with a natural smirk, warm fair skin, clean-shaven.
Hair: jet-black thick wavy hair, medium length, falling naturally around the face and ears, effortlessly messy.
Blindfold: a simple wide band of soft black leather over the eyes with a thin violet stitch line.
Outfit: black silk shirt open at the collar showing his collarbones and upper chest, fitted black trousers, long black leather coat with violet lining, black boots, a silver chain at the neck; sexy and dangerous.
Palette: black, violet, silver.
Panel rule: full-body turnaround WITH the blindfold on; bust shot WITHOUT the blindfold showing glowing violet eyes; close-ups 1-3 with blindfold, 4-9 without.
Expressions (9 close-ups): one-sided smirk, cold dangerous look, amused head tilt, possessive intense gaze, tender smile, cold menace, laughing amused, suppressed anger, seductive smoldering gaze.
```

### 2-3. 데미안 DAMIAN (엘프 왕자 · 후회남)

꼭 지킬 것: **잘생긴 오만한 왕자** · 금색·청동·흙갈색 · 머리는 **제나의 백금발과 확실히 다른 색** · 1화에 웃통을 벗고, 결투엔 갑옷과 망토(시트는 대표 의상 하나로)

표정 9개 (세 시안 공통): 오만하게 내려다보는 비웃음 / 분노한 눈 / 믿을 수 없다는 충격 / 제나를 보는 다정한 눈 / 올리비아에게 차가운 경멸 / 절박하게 매달리는 후회 / 눈물이 고인 상심 / 자신만만한 미소 / 멍하게 홀린 얼굴(달빛 아래 올리비아를 볼 때)

**DAMIAN_A — 황금 왕자**
```
Character: DAMIAN, the Elf Prince, arrogant handsome royal. 24 years old.
Face: classic oval face, strong straight jaw, bright amber-gold eyes, straight nose, confident full lips, sun-kissed light golden skin, clean-shaven.
Hair: warm honey-gold blond hair (golden, NOT platinum), short on the sides, longer textured top swept to one side.
Outfit: ivory royal tunic with gold embroidery of rock and leaf patterns, a gold-trimmed short cape over one shoulder, brown leather belt, fitted trousers, tall brown boots, gold signet ring; princely and athletic.
Palette: ivory, gold, warm brown.
Expressions (9 close-ups): arrogant sneer looking down, furious glare, shocked disbelief, tender gaze, cold contempt, desperate regret, heartbroken teary eyes, confident smile, dazed spellbound look.
```

**DAMIAN_B — 갑옷 기사 왕자**
```
Character: DAMIAN, the Elf Prince, arrogant handsome royal. 24 years old.
Face: angular face with a sharp chiseled jaw and slight cleft chin, deep hazel-gold eyes, strong brows, light warm tan skin, clean-shaven.
Hair: rich chestnut-brown hair with golden highlights, medium length, thick, tousled and pushed back.
Outfit: polished bronze-and-gold elven armor — sculpted breastplate, bracers on both forearms, pauldrons with leaf engraving — over a dark brown tunic, a long earth-brown cape, armored boots; heroic, broad-chested.
Palette: bronze, gold, earth brown.
Expressions (9 close-ups): arrogant sneer looking down, furious glare, shocked disbelief, tender gaze, cold contempt, desperate regret, heartbroken teary eyes, confident smile, dazed spellbound look.
```

**DAMIAN_C — 섹시 귀공자**
```
Character: DAMIAN, the Elf Prince, arrogant handsome royal. 24 years old.
Face: square face with high cheekbones, light green-gold eyes, full lips, fair skin with a healthy warm glow, clean-shaven.
Hair: dark ash-blond hair, slightly wavy, chin-length, tucked behind one ear.
Outfit: cream linen shirt half-unbuttoned showing a sculpted chest, fitted tan suede vest with gold buckles, dark brown trousers, knee boots, a gold cuff on one wrist; sexy, princely, relaxed arrogance.
Palette: cream, tan, gold.
Expressions (9 close-ups): arrogant sneer looking down, furious glare, shocked disbelief, tender gaze, cold contempt, desperate regret, heartbroken teary eyes, confident smile, dazed spellbound look.
```

### 2-4. 제나 JENNA (공작가 작은딸 · 악녀)

꼭 지킬 것: **긴 백금발**(가장 눈에 띄는 무기) · 연분홍·루비 빨강·금색 · 겉은 사랑스러운 공주, 속은 여우 · 손끝에 불꽃 마법 · **올리비아와 얼굴형이 확실히 달라야 함**(제나는 더 동그랗고 귀여운 쪽)

표정 9개 (세 시안 공통): 눈가가 빨개진 피해자 연기 / 혼자 있을 때의 차갑고 얄미운 미소 / 떼쓰며 화내기 / 이겼다는 듯 깔보는 얼굴 / 데미안에게 기대는 애교 / 질투로 굳은 얼굴 / 겁에 질림 / 손끝 불꽃을 보며 즐기는 얼굴 / 순진한 척 큰 눈

**JENNA_A — 핑크 공주**
```
Character: JENNA, the elf duke's younger daughter, beautiful two-faced villainess. 20 years old.
Face: round soft face, big round blue eyes, small button nose, plump glossy pink lips, rosy cheeks, porcelain skin — sweet doll-like prettiness (realistic, not plastic).
Hair: very long bright platinum-blonde hair, glossy, in big princess curls with a pink ribbon.
Outfit: blush-pink ball gown with a fitted off-shoulder bodice, layers of tulle, rose-gold embroidery, a small ruby necklace.
Palette: blush pink, ruby red, rose gold.
Expressions (9 close-ups): fake victim crying with red-rimmed eyes, cold smug smile, tantrum anger, gloating look down, clingy cute pout, frozen jealousy, terrified, delighted watching a flame on her fingertip, innocent wide eyes.
```

**JENNA_B — 루비 악녀**
```
Character: JENNA, the elf duke's younger daughter, beautiful two-faced villainess. 20 years old.
Face: petite heart-shaped face, large upturned hazel eyes, small nose, full red lips, sharp pretty chin, light peach skin.
Hair: long straight sleek platinum-blonde hair, worn half-up with a small gold-and-ruby tiara.
Outfit: fitted ruby-red velvet gown with a deep sweetheart neckline, gold corset lacing, long sheer red sleeves, gold jewelry; sexy and spoiled.
Palette: ruby red, gold.
Expressions (9 close-ups): fake victim crying with red-rimmed eyes, cold smug smile, tantrum anger, gloating look down, clingy cute pout, frozen jealousy, terrified, delighted watching a flame on her fingertip, innocent wide eyes.
```

**JENNA_C — 불꽃 아가씨**
```
Character: JENNA, the elf duke's younger daughter, beautiful two-faced villainess. 20 years old.
Face: soft oval face with dimples, large light-brown doe eyes, softly rounded nose, glossy coral lips, warm ivory skin.
Hair: platinum-blonde hair, shoulder-length, bouncy waves, with a side braid and small gold flower pins.
Outfit: short-sleeved coral-and-gold dress with a flared skirt to the ankles, fitted bodice embroidered with flame patterns, gold arm cuffs, tiny ruby earrings; cute and flirtatious.
Palette: coral, orange-gold, ruby.
Expressions (9 close-ups): fake victim crying with red-rimmed eyes, cold smug smile, tantrum anger, gloating look down, clingy cute pout, frozen jealousy, terrified, delighted watching a flame on her fingertip, innocent wide eyes.
```

### 2-5. 다이앤 DIANE (공작 부인 · 새엄마 · 악녀)

꼭 지킬 것: **화면 나이 30대 초반**(엄마 역이어도 젊고 화려하게) · 와인 레드·금색·검은 레이스 · 손수건을 든 우아한 악녀 · 보라·검정 마법(올리비아에게 저주 팔찌를 채운 사람)

표정 9개 (세 시안 공통): 우아하게 비웃기 / 꾸미는 미소 / 날카롭게 소리치기(예쁘게) / 가짜로 상냥한 미소 / 충격 / 차갑게 명령 / 손수건으로 입가를 가리고 웃음 / 경멸 어린 눈 / 겁먹고 굳은 얼굴

**DIANE_A — 와인빛 공작 부인**
```
Character: DIANE, the elf duchess, glamorous scheming stepmother. Looks 32 years old — youthful, ageless, sexy; NOT a mother-aged woman.
Face: elegant long oval face, high sharp cheekbones, slanted almond dark-brown eyes with winged liner, full wine-red lips, flawless fair skin.
Hair: rich wine-auburn hair in a sleek high updo with a few soft strands framing the face.
Outfit: deep wine-red satin gown with a plunging neckline edged in black lace, fitted silhouette, gold choker and drop earrings; holding a lace handkerchief.
Palette: wine red, gold, black lace.
Expressions (9 close-ups): elegant sneer, scheming smile, sharp shriek (still beautiful), fake sweet smile, shocked, cold commanding, laughing behind a handkerchief, contemptuous eyes, frozen in fear.
```

**DIANE_B — 검은 레이스 귀부인**
```
Character: DIANE, the elf duchess, glamorous scheming stepmother. Looks 32 years old — youthful, ageless, sexy; NOT a mother-aged woman.
Face: heart-shaped face, large hooded green-hazel eyes, arched brows, plump dark-rose lips, light olive skin.
Hair: dark chestnut hair with red tones, long, in old-Hollywood glossy waves swept over one shoulder.
Outfit: black lace gown over a wine-red underlayer, off-shoulder, fitted mermaid shape, long black lace gloves, a garnet necklace; dark glamour.
Palette: black, wine red, gold.
Expressions (9 close-ups): elegant sneer, scheming smile, sharp shriek (still beautiful), fake sweet smile, shocked, cold commanding, laughing behind a handkerchief, contemptuous eyes, frozen in fear.
```

**DIANE_C — 황금 사교계 여왕**
```
Character: DIANE, the elf duchess, glamorous scheming stepmother. Looks 32 years old — youthful, ageless, sexy; NOT a mother-aged woman.
Face: diamond-shaped face, sharp chin, cool grey-blue eyes, thin elegant nose, glossy berry lips, porcelain skin.
Hair: copper-red hair in a sculpted low chignon decorated with gold pins.
Outfit: gold brocade gown with a high open collar, fitted corset waist, wine-red velvet sash and train, heavy gold jewelry and rings; rich, proud, sexy.
Palette: gold, wine red.
Expressions (9 close-ups): elegant sneer, scheming smile, sharp shriek (still beautiful), fake sweet smile, shocked, cold commanding, laughing behind a handkerchief, contemptuous eyes, frozen in fear.
```

---

## 3. 배경 6장 — 3곳 × 시안 2

고른 이유: 장면이 제일 많이 나오는 세 곳이다.
① 서약식장(31~39화 · 9씬 · 클라이맥스) ② 공작 저택 연회장(7~13화 · 7씬) ③ 백란 저택 응접실(42~45화 · 7씬 + 14화)
※ 26~28화의 백란 저택 정문·마당(가운데 달빛 난초 나무)은 필요하면 따로 뽑으면 된다.

[배경 공통 블록] — 6장 전부 맨 끝에 붙인다
```
=== BACKGROUND RULES ===
Production design reference, photorealistic establishing shot for a live-action fantasy romance series. No people. One single wide landscape image at the largest size.
Bright, colorful, luxurious, romantic fantasy; vivid but tasteful color; clean beautiful architecture; crisp detail; inviting, not scary.
Leave clear open floor space where actors will stand.
AVOID: dark, gloomy, muted, desaturated, sepia, ruined, dusty, dirty, cobwebs, horror, heavy fog, grime, cluttered, people.
```

**BG1_A — 서약식장 · 흰 대리석 엘프 양식 (낮)**
```
Bonding Ceremony Hall, daytime, interior. A grand elven ceremony hall of white marble with tall slender pillars carved like trees, high arched windows pouring warm sunlight, a long central aisle with rows of guest seating on both sides, garlands of white flowers and silver vines. At the far end a raised dais with a single tall dark throne of black wood inlaid with violet crystal and silver filigree (the Dark Elf King's seat), and in front of the dais a white stone altar for the priest. Violet and silver banners. Solemn, grand, celebratory.
```

**BG1_B — 서약식장 · 다크엘프 양식 (낮)**
```
Bonding Ceremony Hall, daytime, interior. A grand dark-elf style hall of polished black and deep violet marble with silver veins, giant silver-white crystal chandeliers, an enormous round stained-glass window in violet and white letting colorful daylight fall across the floor. A tiered dais with a canopy and a tall black-and-silver throne, a silver altar with a silver basin in front of it, long rows of guest seating on both sides, tall arrangements of white and purple flowers. Bright and majestic, not dark.
```

**BG2_A — 공작 저택 연회장 · 금빛 (밤)**
```
Elf duke's banquet hall, night, interior. Lavish hall with cream and gold walls carved with leaf vines, many golden chandeliers full of glowing candles, polished marble floor with a wide open center for a crowd of nobles. Tall double doors at one end. Tall windows along one side letting in soft blue moonlight. A small raised platform holding a gold stand with a glass orb that has fire burning inside (the Judgment Orb). Long side tables with fruit, wine and crimson-and-white flowers. Warm, glamorous, festive.
```

**BG2_B — 공작 저택 연회장 · 아이보리·초록 (밤)**
```
Elf duke's banquet hall, night, interior. Ivory and soft sage-green hall with gold trim, a great glass dome ceiling showing the moon and stars, crystal chandeliers, walls of climbing white roses and greenery like an indoor garden, a grand double staircase on one side, polished pale marble floor with a wide open center. Tall double doors at one end, moonlit windows along the side. A raised platform with a gold stand holding a glass orb with fire burning inside (the Judgment Orb). Romantic, bright, elegant.
```

**BG3_A — 백란 저택 응접실 · 흰색·청자색 (낮)**
```
White Orchid Manor, side parlor, daytime, interior. An elegant white manor parlor with pale celadon-green walls, tall white pillars, tall windows full of soft sunlight, white orchids in celadon vases everywhere, cream silk sofas and a low marble table, gold-framed mirrors, sheer white curtains moving in the breeze. Calm, noble, refined, bright.
```

**BG3_B — 백란 저택 응접실 · 달빛 난초 정원풍 (낮)**
```
White Orchid Manor, drawing room, daytime, interior. A luminous drawing room opening onto a garden through tall glass doors, with a view of a large tree covered in white orchid-like blossoms in the courtyard. White and silver interior, carved orchid patterns on the ceiling, a crystal chandelier, light-blue velvet chairs, white orchids and green plants, polished white floor reflecting sunlight. Fresh, elegant, dreamy but bright.
```

---

## 4. 다 뽑은 뒤 확인표 — 하나라도 걸리면 그 장은 다시

| # | 볼 것 | 다시 뽑는 기준 |
|---|---|---|
| 1 | **나이** | 화면 얼굴이 26살 넘어 보이면(다이앤은 35살 넘어 보이면) 무조건 다시 |
| 2 | **예쁨·잘생김** | 넷플릭스 로맨스 포스터 옆에 놓으면 밀린다 싶으면 다시 |
| 3 | **닮음** | 15장 얼굴만 잘라 한 줄로 놨을 때 두 사람이 헷갈리면 나중에 만든 쪽을 다시(특히 올리비아↔제나, 가브리엘↔데미안) |
| 4 | **시트 안 일치** | 패널마다 얼굴·머리·옷이 다르면 다시 |
| 5 | **기괴함** | 손가락 수, 귀가 크고 길게 나옴, 눈 짝짝이, 화난 표정이 일그러짐 → 다시 |
| 6 | **색** | 칙칙하거나 회색빛이면 다시 |
| 7 | **소품** | 올리비아 = 오른손목 팔찌 + 왼손바닥 붕대 / 가브리엘 = 풀샷엔 눈가리개, 바스트샷엔 보라빛 눈 / 제나 = 백금발 / 데미안 = 백금발 아님 |
| 8 | **배경** | 사람이 있거나, 어둡거나, 서약식장에 옥좌·제단이 없거나, 연회장에 불 구슬이 없으면 다시 |
