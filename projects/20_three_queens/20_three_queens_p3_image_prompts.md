# THE HIDDEN ARCHMAGE'S THREE QUEENS — 이미지 프롬프트 52컷

인물 설정 = `20_three_queens_p2_character_sheet.md`

## 0. 공통 블록 (모든 컷 앞에 붙인다)

**[FIX]**
```
live-action photography, shot on a full-frame cinema camera, 85mm prime lens, natural optics, single subject, seamless neutral mid-grey studio backdrop, no background props, no set, no environment, eye-level camera, sharp focus, real skin with visible pores, fine peach fuzz, natural subsurface scattering, subtle skin tone variation, no retouching, no airbrush, real materials with true physical texture, practical lighting
```

**[NEG-공통]**
```
deformed face, asymmetric eyes, uneven eyes, cross-eyed, malformed nose, plastic waxy skin, over-smoothed, perfectly symmetrical face, mask-like face, waxwork, uncanny valley, dead eyes, blank vacant stare, angular chiselled face, sharp protruding cheekbones, bad hands, extra fingers, fused fingers, extra limbs, bad anatomy, blurry, lowres, cartoon, anime, 2d, illustration, 3d render, cgi, octane render, unreal engine, blender, digital painting, digital art, concept art, key visual, video game screenshot, cel shading, airbrushed, plastic skin, waxy skin, doll skin, porcelain doll, figurine, sculpture, over-smoothed, beauty filter, instagram filter, doll, mannequin, watermark, text, logo, multiple views, collage, split panel, grid, duplicate figure, second person, mirror reflection, child, teenager
```

**워크플로** — ①F1 얼굴 한 장을 합격시킨 뒤에야 나머지 컷을 돌린다 ②확정 얼굴을 레퍼런스로 물리고 B·D 생성 ③컷 사이엔 seed만 바꾼다(프롬프트를 고치면 시트 정합이 깨진다).

## 9. 캐릭터 레퍼런스 시트 — 컷 리스트 & 프롬프트

### 공통 규격

**[FIX] 전 컷 고정 문구 (52컷 전부에 그대로 들어간다 — 이미 각 프롬프트 앞머리에 박아 뒀다)**
```
[FIX] unretouched photograph, fine film grain
```
> 앞머리 4토큰이 매체를 사진으로 못박고, 뒤쪽 피부 6토큰이 완벽한 피부를 금지한다. **`photorealistic`은 쓰지 않는다** — 렌더 어휘라 CG로 빠진다.

**[MAT] 재질 앵커 — 의상이 들어가는 전 컷(B·D)에 해당 항목만 인라인**
```
real woven fabric texture with visible weave and natural creasing
hand-forged steel with fine scratches, worn edges and uneven patina
genuine leather grain with natural creases
real silk with true drape and soft wrinkles
crushed velvet with a real nap that eats the light
individually set stone and hand-chased goldwork with tool marks
real black lace with a visible knit and scalloped edges
dry pale bone and pared white living wood, matte and slightly grained
gossamer veil netting, weightless and transparent
pierced silver filigree with visible file marks
```
> 금속엔 잔기스, 가죽엔 결, 천엔 짜임과 주름을 반드시 명시한다(무결점 매끈한 갑옷·천 = 게임 에셋).
> **한 벌 안에 성질이 다른 재질이 최소 3종 부딪쳐야 한다** — 광택(금속·비늘·새틴) · 무광(가죽·벨벳·뼈) · 투명(레이스·베일·거즈)이 한 화면에 같이 있어야 눈이 안 지친다. 단일 소재 + 단색 = 실패컷.

**[SIL] 실루엣 시그니처 — B 컷 전신에 반드시 읽혀야 하는 형태 (인물별 1개 · 다섯이 겹치지 않는다)**
```
카타리나 = 어깨   — a pair of thin blade-like pauldrons sweeping low and back behind the shoulders
탈리아   = 머리   — two panels of gossamer veil falling from a crown circlet to the floor, split either side of the spine
프레이야 = 목     — a fan-shaped crest collar rising behind the head from the two shoulder points
비비안   = 허리 뒤 — a silver filigree arch at the small of the back launching a cathedral train spread wide across the floor
모르가나 = 팔     — two panels of black lace falling from the elbows to the floor and trailing behind
에이든   = 없음   — no structure at all, a plain vertical rectangle of coarse cloth
```
> 역광 그림자만 보고 누군지 갈려야 한다. **구조물은 어깨·칼라·트레인·오버스커트처럼 몸통 바깥에만 얹고, 몸통은 여전히 [FIT] second-skin이다** — 구조를 얹는다고 몸을 가리면 실패컷.
> **얼굴 근처는 비운다.** 세공·보석·자수 밀도는 몸통·허리·소맷단에 몰고 목·쇄골·턱 아래는 열어 둔다(시선이 얼굴로 가야 한다).

**[FIT] 밀착 앵커 — 여성 5인 의상이 들어가는 전 컷(B·D)에 인라인 (덮되 붙는다)**
```
moulded to the body like a second skin, skin-tight, figure-hugging, contoured, second-skin fit, the material follows every curve, sculpted narrow waist, the full silhouette of the bust, waist and hips reads clearly through the material
```
> 덮는 **면적**은 그대로 두고 **핏**만 올린다. 천·강철·비늘이 몸을 *가리는* 순간 실제 중세 복식이 되고 판타지가 죽는다 — 실루엣이 안 읽히는 컷은 실패컷이다.

**[LIGHT-N] 중립 조명 — B·D 컷 전용 고정 (얼굴 컷만 인물별 무드 조명 허용)**
```
flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light
```

**[POSE-N] 중립 포즈 — B 컷 전용 고정**
```
neutral relaxed A-pose, arms slightly away from the body, palms in, weight even on both feet, chin level, calm neutral expression
```

**[BEAUTY] 미모 앵커 — F1~F3 전 인물 공통 골격 (인종 중립 · 실제 프롬프트에는 인물별 외모 방향 토큰과 함께 인라인돼 있다)**
```
refined balanced facial proportions, beauty-first casting, large expressive eyes with a clean upper-lid crease, slightly deep-set, long dark lashes, high straight nose bridge with a refined tip, defined brow line, tapered oval jawline, refined chin, full well-shaped lips with a soft natural sheen, clear even complexion, striking symmetry without being mask-like, real skin with visible pores and fine peach fuzz, warm living gaze
```
> **[FACE-DIR] 인물별 외모 방향 토큰 — F1~F3에만 인라인 (B·D 컷에는 절대 넣지 않는다).**
> ```
> 에이든  = european features, eyes set deep under a defined brow ridge, defined brow line, clear even complexion, striking symmetry without being mask-like
> 카타리나 = fair northern colouring with a cool undertone, slightly deep-set eyes, defined brow line, clear even complexion, striking symmetry without being mask-like
> 탈리아  = otherworldly non-human features tied to no region, wide-set expressive eyes, delicately defined brow line, clear even complexion, striking symmetry without being mask-like
> 프레이야 = striking exotic features tied to no single region, wide-set eyes, strongly defined brow line, clear even complexion, striking symmetry without being mask-like
> 비비안  = european features, eyes set deep under a clearly defined brow ridge, high straight nose bridge running straight down from the brow, strongly defined brow line, clear even complexion with a cool undertone, striking symmetry without being mask-like
> 모르가나 = southern european features with a warm olive complexion, deep-set eyes, defined brow line, striking symmetry without being mask-like
> ```
> **`striking symmetry without being mask-like`는 [NEG-UNCANNY]의 `perfectly symmetrical face` · `flawless symmetry`와 짝으로 쓴다 — 네거티브를 빼지 않는다.**

**[NEG-CG] CG/게임 렌더 차단 — 전 인물 NEG에 병합 완료**
```
3d render, cgi, octane render, unreal engine, blender, digital painting, digital art, illustration, concept art, key visual, video game screenshot, anime, cel shading, airbrushed, plastic skin, waxy skin, doll skin, porcelain doll, figurine, sculpture, over-smoothed, beauty filter, instagram filter
```

**[NEG-SKIN] 노출 하향 차단 — 여성 5인 전원 NEG에 병합 완료**
```
nude, topless, exposed nipples, lingerie as outerwear, stripper outfit, chainmail bikini, cheap costume, tacky, vulgar
```

**[NEG-FIT] 헐렁함 차단 — 여성 5인 전원 NEG에 병합 완료**
```
loose fabric, baggy, shapeless, boxy silhouette, bulky armour, heavy layered robes, historically accurate medieval clothing, modest, frumpy, oversized garment, hidden figure
```

**[NEG-UNCANNY] 언캐니 차단 — 여성 5인 전원 NEG에 병합 완료**
```
perfectly symmetrical face, flawless symmetry, mask-like face, waxwork, uncanny valley, dead eyes, blank vacant stare, hollow gaunt cheeks, angular chiselled face, heavy square jaw, sharp protruding cheekbones, alien features, ageless inhuman face, dry taut leathery skin, sun-weathered skin, androgynous, 2d, illustration
```

**[NEG+ / F] F1~F3 전 인물 공통**
```
full body, wide shot, hands in frame, armour, pauldrons, crest collar, standing collar, veil, circlet, crown, train, staff, fan, weapon, hat, glowing marks on the face
```
> **실루엣 구조물은 F 컷에 하나도 넣지 않는다** — 견갑·칼라·베일·아치·레이스 패널 전부 B 컷부터다. 얼굴 컷에 들어오면 헤어라인·턱선·이마 비율을 먹는다.
**[NEG+ / B3] 후면 컷 공통**
```
face visible, head turned to camera, over-the-shoulder look
```
**[NEG+ / D] D1~D3 공통**
```
head in frame, face, full figure, weapon, sword, staff, fan, crown, cloak, second figure
```

**워크플로 4줄**
1. **F1 한 장을 먼저 합격시킨다.** F1이 안 나오면 나머지 51컷은 손대지 않는다 — 이 시트는 전부 F1의 얼굴을 물려 쓰는 구조다.
2. **F1을 reference / IP-adapter / face-swap으로 물려 F2·F3.** 세 장 나란히 놓고 같은 사람으로 읽히는지 먼저 본다(광대·콧대·인중 길이 3점 대조).
3. **확정 얼굴로 B1~B3 → D1~D3.** B·D 프롬프트에는 얼굴 묘사가 한 토큰도 없다(`same face as reference`뿐) — 얼굴을 다시 쓰면 그 컷만 다른 사람이 된다.
4. **컷 사이에 바꾸는 건 seed뿐.** [FIX]·[LIGHT-N]·렌즈·배경은 절대 건드리지 않는다. 실패컷은 프롬프트를 고치지 말고 seed만 돌린다(프롬프트를 고치면 시트 전체 정합이 깨진다).

**컷 번호 규칙**

| 코드 | 내용 | 비율 | 적용 |
|---|---|---|---|
| **F1·F2·F3** | 얼굴 정면 / 3⁄4 / 정측면 | 3:4 | 전원 |
| **B1·B2·B3** | 전신 정면 / 3⁄4 / 후면 | 9:16 | 전원 |
| **B4** | 전신 정면 (2벌째 의상) | 9:16 | 비비안만 |
| **D1·D2·D3** | 상반신 / 허리·골반 / 힙 3⁄4후면 | 1:1 · 1:1 · 3:4 | 여성 5인 |

에이든 6컷 · 카타리나 9 · 탈리아 9 · 프레이야 9 · 비비안 10 · 모르가나 9 = **총 52컷**.
비율 표기(`3:4` 등)를 안 읽는 툴이면 `--ar 3:4`로 옮기고, 네거티브를 안 받는 툴이면 `[NEG]`를 `--no a, b, c`로 옮긴다.

---

### 1. 에이든 (Aiden) — 먼지 밑에 숨긴 정면 미남

**[NEG]**
```
[NEG-공통] + lazy eye, crooked teeth, heavy wrinkles, sagging skin, jowls, gaunt, sunken cheeks, heavy square jaw, sun-weathered skin, dull grey lifeless skin, hair covering the eyes, long fringe, curtain bangs, greasy hair, matted hair, dirty hair, dishevelled, homeless, beard, stubble, moustache, makeup, grime smeared on the face, soot, emaciated, oversaturated, bright colours, jewelry, glowing eyes
```

| 컷 | 내용 |
|---|---|
| F1 | 얼굴 정면 클로즈업 |
| F2 | 얼굴 3⁄4 (사측면) |
| F3 | 얼굴 정측면 프로필 |
| B1 | 전신 정면 (사서복 + 앞트임 로브) |
| B2 | 전신 3⁄4 |
| B3 | 전신 후면 |

**F1 · 얼굴 정면 클로즈업**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, front angle, extremely handsome young man, refined balanced facial proportions, beauty-first casting, european features, eyes set deep under a defined brow ridge, defined brow line, clear even complexion, striking symmetry without being mask-like, dark ash-brown medium-length hair pushed back off the forehead, brows fully exposed, a few loose strands at the temple, large expressive dark iron-grey eyes, clean upper-lid crease, long dark lashes, half-lidded but clearly alive gaze, high straight nose bridge with a refined tip, smooth cheek line, clean slim jawline, well-shaped calm mouth, real fair indoor skin, visible pores, fine skin texture, never dull or grey, no retouching, no makeup, single soft key from the left through a large diffusion frame, cool low-key grey grade
```

**F2 · 얼굴 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, three-quarter angle, head turned 45 degrees to camera left, same face as reference, european features, eyes set deep under a defined brow ridge, defined brow line, clear even complexion, striking symmetry without being mask-like, dark ash-brown medium-length hair pushed back off the forehead, forehead and brows exposed, large expressive dark iron-grey eyes half-lidded with long dark lashes, high straight nose bridge and a clean tapered jawline reading in three-quarter, real fair indoor skin, visible pores, fine skin texture, no retouching, single soft key from the left through a large diffusion frame, cool low-key grey grade
```

**F3 · 얼굴 정측면 프로필**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, strict side profile, 90 degrees to camera left, same face as reference, european features, eyes set deep under a defined brow ridge, defined brow line, clear even complexion, striking symmetry without being mask-like, clean silhouette of a high straight nose bridge with a refined tip, well-shaped lip line and a slim jaw-to-neck line, ear fully exposed, dark ash-brown medium hair swept back behind the ear, hair just touching the nape, long dark lashes reading in profile, real fair indoor skin, visible pores, fine skin texture, no retouching, single soft key from the left through a large diffusion frame, cool low-key grey grade
```

**B1 · 전신 정면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, palms in, weight even on both feet, chin level, calm neutral expression, tall long-limbed frame with broad shoulders and a narrow waist entirely buried under three layers of the same drab cloth, an open-weave linen shirt under a heavier archivist tunic under a knee-length open overrobe, all of it dust-grey and faded brown with no ornament of any kind, real woven fabric texture with a coarse open weave and natural creasing, loose threads unravelling at the cuffs, a frayed picked-apart hem, a patch of slightly different cloth set into one knee, the seams faded to different shades from years of washing, sleeves rolled past the elbows leaving the forearms bare, a single genuine leather cord with visible grain at the waist, open collar showing the neck and collarbone, ink-stained fingers, worn plain silver ring threaded on a leather cord at the throat, matte lead-grey rank badge at the chest, wax and ink stains, no metalwork, no embroidery, no buckles
```

**B2 · 전신 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body three-quarter view, body turned 45 degrees to camera left, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, calm neutral expression, the same three layers of drab cloth, open-weave linen shirt under a heavier archivist tunic under a knee-length open overrobe, real woven fabric texture with a coarse open weave and natural creasing, loose threads at the cuffs and a frayed hem, a patch of different cloth at one knee, seams faded to different shades, sleeves rolled past the elbows, genuine leather waist cord with visible grain, silver ring on a leather cord at the throat, lead-grey rank badge, the overrobe hanging open so the side silhouette of the shoulder line reads through the cloth, dust-grey and faded brown, no metalwork, no embroidery
```

**B3 · 전신 후면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body back view, facing fully away from camera, same figure as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, standing straight, arms slightly away from the body, weight even on both feet, dark ash-brown medium hair swept back, ending just at the nape, knee-length open overrobe seen from behind, hanging as a plain vertical rectangle of cloth with no structure of any kind, real woven fabric texture with a coarse open weave and natural creasing, a frayed picked-apart hem and loose threads at the cuffs, seams faded to different shades, broad shoulder line reading through the loose cloth down to a narrow waist, genuine leather cord with visible grain knotted at the back of the waist, rolled sleeves, dust-grey and faded brown, wax and ink stains, no metalwork, no embroidery
```
**[NEG+]** `face visible, head turned to camera, over-the-shoulder look`

**[NOTE]** 레퍼런스 시트는 A-포즈 고정(캐논의 웅크린 자세는 연기 컷에서만 — 웅크리면 어깨 폭이 매 컷 달라진다). **머리는 절대 눈을 가리지 않는다** — 이마와 눈썹을 드러내고 떡진 머리·기름기·앞머리 커튼 전부 금지, 허름함은 옷·자세·색보정이 맡는다. 피부는 무광이되 톤은 살린다(`matte sunless skin` 금지 — 얼굴이 회색으로 죽는다).
힘을 드러내는 지정 컷을 따로 뽑을 때만 F1에 `thin gold ring around the iris` 한 토큰 추가.

---

### 2. 카타리나 (Katarina) — 차가운 조각 미인

**[NEG]**
```
[NEG-공통] + crooked teeth, over-smoothed doll skin, heavy wrinkles, gaunt, sunken cheeks, flawless symmetry, hollow gaunt cheeks, ageless inhuman face, dry taut leathery skin, sun-weathered skin, masculine jaw, square heavy jaw, strong wide jaw, thick neck, adams apple, androgynous, tomboy, facial hair, bodybuilder, bulging muscles, visible abs on the face crop, veiny arms, broad masculine shoulders, bangs, blunt fringe, slicked-back severe hairline, short hair, smiling, tattoos, warm colour grade, jewelry, crown, bikini armour, nude, topless, exposed nipples, lingerie as outerwear, stripper outfit, chainmail bikini, cheap costume, tacky, vulgar, loose fabric, baggy, shapeless, boxy silhouette, bulky armour, heavy layered robes, historically accurate medieval clothing, modest, frumpy, oversized garment, hidden figure
```

| 컷 | 내용 |
|---|---|
| F1 | 얼굴 정면 클로즈업 |
| F2 | 얼굴 3⁄4 |
| F3 | 얼굴 정측면 프로필 |
| B1 | 전신 정면 (**뒤로 뻗은 칼날 견갑** + 하프플레이트 + 벨트 + 진홍 망토 + 대검) |
| B2 | 전신 3⁄4 (견갑 실루엣 · 대검) |
| B3 | 전신 후면 (견갑이 뒤로 벌어진 형태 · 망토 젖힘 · 견갑골 사이 좁은 열림 · 검 제외) |
| D1 | 상반신 타이트 — 흉갑 몰드 · 문장 각인 · 얕은 넥라인 · 갈비뼈 아래 절단선 · 견갑 밑동 |
| D2 | 허리·골반 타이트 — **맨 복부·복근** · 골반에 낮게 걸친 버클 셋 벨트 · 포드런 |
| D3 | 힙 타이트 3⁄4 후면 (청흑 가죽 · 벨트 아랫단) |

**F1 · 얼굴 정면 클로즈업**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, front angle, breathtakingly beautiful woman, refined balanced facial proportions, beauty-first casting, fair northern colouring with a cool undertone, slightly deep-set eyes, defined brow line, clear even complexion, striking symmetry without being mask-like, platinum ash hair in a soft high ponytail with volume at the crown and fine baby hairs at the hairline, two long face-framing strands falling in front of the ears down past the jawline, large expressive pale steel-grey eyes with a dark limbal ring, clean upper-lid crease, long dark lashes, calm cool gaze that is alive not blank, high straight nose bridge with a refined tip, tapered oval jawline, refined chin, full well-shaped lips with a soft natural sheen, unsmiling, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush, no scars, cool soft overcast daylight through a large north window, bluish-neutral grade
```

**F2 · 얼굴 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, three-quarter angle, head turned 45 degrees to camera right, same face as reference, fair northern colouring with a cool undertone, slightly deep-set eyes, defined brow line, clear even complexion, striking symmetry without being mask-like, refined balanced facial proportions, platinum ash high ponytail with soft crown volume, one long face-framing strand falling in front of the near ear past the jawline, large expressive pale steel-grey eyes with a dark limbal ring, clean upper-lid crease, long dark lashes, calm cool living gaze, high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen, unsmiling, tapered oval jawline reading in three-quarter, refined chin, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush, cool soft overcast daylight through a large north window, bluish-neutral grade
```

**F3 · 얼굴 정측면 프로필**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, strict side profile, 90 degrees to camera right, same face as reference, fair northern colouring with a cool undertone, slightly deep-set eyes, defined brow line, clear even complexion, striking symmetry without being mask-like, platinum ash ponytail falling straight from the crown with soft volume, blunt cut ends, one long face-framing strand hanging in front of the ear down past the jawline, clean silhouette of a high straight nose bridge with a refined tip, full well-shaped lips and a softly tapered oval chin, long dark lashes reading in profile, long neck fully exposed, unsmiling, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush, cool soft overcast daylight through a large north window, bluish-neutral grade
```

**B1 · 전신 정면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, chin level, calm neutral expression, tall toned hourglass with no bulk, straight clean shoulder line, extremely narrow waist, flat stomach with firm clearly defined abdominal muscles, long slender firm legs, platinum ash high ponytail with two long face-framing strands at the jawline, a three-layer costume in crimson, blackened silver and midnight blue-black, blackened silver half-plate cuirass moulded to the body like a second skin, the steel taking the exact shape of the bust and drawing in hard under the ribs, contoured, the full silhouette of the bust reading clearly through the steel, a shallow neckline stopping just below the collarbones with nothing at all at the throat, the cuirass ending in a clean cut edge just beneath the ribcage, the whole midriff bare from that edge down past the navel, firm defined abdominal muscles and a sculpted narrow waist reading across the bare skin, thin figure-hugging plate with no bulk, small conquered-kingdom crests chased one by one across the breastplate surface, a pair of thin blade-like pauldrons sitting on the shoulder caps and sweeping low and back behind her, flat and bladed with no bulk, a fine silver chain swagged along their lower edge, the tops of the shoulders and the whole arms otherwise bare, a wide belt of overlapping steel scales backed with leather wrapped twice low across the hipbones well below the navel with a short steel fauld hanging from it, three buckles and a row of rivets, hand-forged steel with fine scratches, worn edges and uneven patina, skin-tight midnight blue-black leather bodysuit sheathing the body from the hipbones down to the ankles, one side cut away in a high slit rising to the top of the thigh so the bare leg reads the whole way up, genuine leather grain with natural creases, the leather moulded to the thigh and calf on the closed side so the full line of the leg reads, a steel thigh greave on the closed leg, crimson velvet cloak with a real nap hanging from both shoulders behind the pauldrons and pushed back clear of the torso, midnight-black lining and fine silver-thread embroidery along its edge, a magnificent greatsword nearly her own height held point-down beside her right foot, blade clear of the body, a mirror-bright silver-platinum blade that throws back the light, a fullered channel down its centre inlaid with fine engraved runes glowing a soft blue, an ornate hand-chased gold filigree hilt wound with wire, a crossguard flaring outward into a pair of stylised wings, individually set gemstones studding the grip and pommel, unmistakably a priceless sacred blade, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush
```

**B2 · 전신 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body three-quarter view, body turned 45 degrees to camera left, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral A-pose, weight even on both feet, calm neutral expression, toned hourglass with no bulk, straight clean shoulder line dropping into an extremely narrow waist, platinum ash high ponytail with a long face-framing strand at the jawline, blackened silver cuirass moulded to the body like a second skin, the steel following every curve of the bust and drawing in hard under the ribs so the shape reads clearly through it in profile, the cuirass ending in a clean cut edge just beneath the ribcage with the whole side of the midriff bare from there down past the navel, firm defined abdominal muscles and the sculpted narrow waist reading across the bare skin in three-quarter, thin figure-hugging plate with no bulk, small chased crests across the breastplate surface, hand-forged steel with fine scratches, worn edges and uneven patina, a thin blade-like pauldron on the near shoulder cap sweeping low and back behind her and reading clearly against the body in three-quarter, flat and bladed with no bulk, a fine silver chain along its lower edge, bare shoulder top and bare arm beneath it, nothing at the throat, a wide belt of overlapping steel scales backed with leather wrapped twice low across the hipbones with three buckles, a row of rivets and a short steel fauld, skin-tight midnight blue-black leather bodysuit moulded to the body from the hipbones to the ankles, a high slit on the near side rising to the top of the thigh baring the leg, genuine leather grain with natural creases, a thigh greave on the closed leg, crimson velvet cloak with a real nap and a midnight-black lining pushed back off the shoulder nearest camera, silver-thread embroidery along its edge, a magnificent silver-platinum greatsword held point-down at her side, a fullered channel down its centre with fine engraved runes glowing soft blue, an ornate gold filigree hilt with a crossguard flaring into wings, gemstones set into the grip and pommel, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush
```

**B3 · 전신 후면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body back view, facing fully away from camera, same figure as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, standing straight, arms slightly away from the body, weight even on both feet, platinum ash ponytail falling straight down the back with soft crown volume, a pair of thin blade-like pauldrons on the shoulder caps sweeping low and back so the shoulder line reads as a swept arrowhead from behind, flat and bladed with no bulk, a fine silver chain swagged along each lower edge, the tops of the shoulders and the arms bare beneath them, the steel backplate moulded to the body like a second skin, following the taper from the straight shoulder line into a sculpted narrow waist and out again over the hip, cut away in one narrow opening between the shoulder blades with a strip of bare back showing through it, the pauldrons clear of that opening, hand-forged steel with fine scratches, worn edges and uneven patina, a wide belt of overlapping steel scales backed with leather wrapped twice low across the hips beneath the narrow waist, crimson velvet cloak with a real nap and a midnight-black lining swept off and hanging from one shoulder so the opening reads clearly, silver-thread embroidery along its edge, skin-tight midnight blue-black leather bodysuit moulded over the hip and down both legs, a high slit rising to the top of the thigh visible along the near leg, the material following every curve, genuine leather grain with natural creases, a thigh greave on the closed leg, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush, no weapon
```
**[NEG+]** `face visible, head turned to camera, over-the-shoulder look, sword`

**D1 · 상반신 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, tight upper-torso crop framed from the jawline down to the lower ribs, face out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, shoulders square to camera, blackened silver cuirass moulded to the exact shape of the chest like a second skin, the steel taking the full form of the bust and drawing in under the ribs, the silhouette reading clearly through the metal, a shallow neckline stopping just below the collarbones with the throat and collarbones completely bare and unornamented, the plate closed all the way down the chest and ending in a clean cut edge just beneath the ribcage at the bottom of frame with a strip of bare stomach showing below it, thin figure-hugging plate with no bulk, small conquered-kingdom crests chased one by one across the breastplate surface in fine tooled line work, hand-forged steel with fine scratches, worn edges and uneven patina catching the light along the moulded curve, the root of a thin blade-like pauldron entering frame at each shoulder cap and angling back and out of frame, a fine silver chain swagged from it, straight clean shoulder line with no bulk, bare smooth shoulders and delicate collarbones, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush, no scars
```
**[NEG+]** `head in frame, face, cloak, sword`

**D2 · 허리·골반 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, hips-and-waist crop framed from just below the ribcage to above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, the cut lower edge of the blackened silver cuirass crossing the top of frame just beneath the ribcage, the whole midriff bare below it, firm clearly defined abdominal muscles across a flat stomach, a taut sculpted narrow waist and the navel fully visible, bare skin running from the cut steel edge down to the hipbones, thin figure-hugging plate with no bulk above, chased crest work in fine tooled line along its lower edge, a wide belt of overlapping steel scales backed with dark leather wrapped twice low across the hipbones well below the navel with a short steel fauld hanging from it, three heavy buckles set off-centre and a close row of rivets running its length, hand-forged steel with fine scratches, worn edges and uneven patina, genuine leather grain with natural creases, skin-tight midnight blue-black leather bodysuit starting at the hipbones under the belt and moulded to the leg from there down, a high slit on one side rising to the top of the thigh baring the leg, the narrowest point of the waist sitting far above the widest point of the hip and read entirely on bare skin, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush
```
**[NEG+]** `head in frame, face, cloak, sword`

**D3 · 힙 타이트 3⁄4 후면**
```
[FIX] unretouched photograph, fine film grain, 3:4, rear three-quarter crop framed from the mid-back down to just above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight with weight even on both feet, skin-tight midnight blue-black leather bodysuit moulded over the hip and thigh, a high slit rising to the top of the thigh on the near side baring the leg, second-skin fit, the material following every curve, genuine leather grain with natural creases, the seam running from the small of the back into the hip curve, the lower edge of a riveted steel-scale belt crossing the top of frame with one buckle visible, hand-forged steel with fine scratches and uneven patina, firm round hip flaring from a very narrow waist read entirely through the fitted leather, long slender thigh, real light golden-wheat skin, visible pores, fine peach fuzz, no airbrush, the top edge of the thigh greave at the lower edge of frame, no cloak
```
**[NEG+]** `head in frame, face, cloak, sword`

**[NOTE]** F 컷에 `broad shoulders`·`abs`를 넣지 않는다(턱과 목이 남자로 넘어간다) — 어깨 라인은 갑옷 실루엣과 B 컷에서만 만든다. 차가움은 시선의 온도와 조명(bluish-neutral)이 만들고, 골격을 각지게 하지 않는다.
B3는 검을 빼야 등이 보인다(§8 식별자 3개 중 대검은 B1·B2가 담당).
**흉갑은 갈비뼈 아래에서 깨끗하게 끊고 벨트는 골반에 낮게 건다** — 배꼽 위아래 맨 복부와 복근이 이 인물의 노출 지점이다(`bare midriff` 계열 네거티브는 이 인물에만 걸지 않는다). 다리는 한쪽 옆선이 허벅지 위쪽까지 하이컷으로 시원하게 트이고(`high-cut leg opening`은 [NEG]에서 제외), `bikini armour`·`chainmail bikini` 등 저급 노출은 [NEG] 유지.
**검은 은백·백금 도신 + 금세공 힐트 + 날개형 가드 + 푸르게 빛나는 룬 각인으로 고정** — 흑철·투박한 대검류 어휘는 쓰지 않는다(칙칙하고 밋밋하면 실패컷, 반드시 값비싸고 신성해 보여야 한다).
**견갑은 두께가 아니라 각도로 만든다** — `thin blade-like`·`flat and bladed`·`no bulk`를 반드시 붙이고, 부풀면 [NEG]의 `bulky armour`로 잡는다. 어깨 윗면과 팔은 맨살로 남긴다(견갑이 팔을 덮으면 노출 캐논이 깨진다). 목·쇄골 위는 어떤 컷에서도 비운다 — 밀도는 흉갑 각인·벨트 버클·리벳으로만 올린다.

---

### 3. 탈리아 (Thalia) — 인간이 못 닿는 미모의 엘프 여왕

**[NEG]**
```
[NEG-공통] + crooked teeth, over-smoothed doll skin, heavy wrinkles, skeletal, emaciated, sickly, hollow cheeks, flawless symmetry, tiny pinpoint pupils, heavy square jaw, alien face, inhuman face, ageless inhuman face, creepy, unsettling, oversized eyes, glowing skin, glowing veins on the face, veins on the cheeks, dry taut leathery skin, corpse pale, round short ears, tan skin, gold jewelry, metal ornaments, see-through front panel, sheer fabric over the chest, transparent bodice, slit opening above the hip, heavy makeup, masculine jaw, thick neck, androgynous, nude, topless, exposed nipples, lingerie as outerwear, stripper outfit, chainmail bikini, cheap costume, tacky, vulgar, loose fabric, baggy, shapeless, boxy silhouette, bulky armour, heavy layered robes, historically accurate medieval clothing, modest, frumpy, oversized garment, hidden figure
```

| 컷 | 내용 |
|---|---|
| F1 | 얼굴 정면 클로즈업 |
| F2 | 얼굴 3⁄4 |
| F3 | 얼굴 정측면 프로필 (귀 실루엣 확정 컷) |
| B1 | 전신 정면 (**정수리→바닥 두 폭 베일** + 뼈 늑골 프레임 + 실크 드레이프 + 수정 지팡이) |
| B2 | 전신 3⁄4 (베일 기둥 실루엣 · 골반 아래까지 옆트임) |
| B3 | 전신 후면 (머리 앞으로 넘김 · **베일 두 폭 사이로 맨 등** · 지팡이 제외) |
| D1 | 상반신 타이트 — 대각 드레이프 · 갈비뼈 위 뼈 프레임 · 어깨선 |
| D2 | 허리·골반 타이트 — 뼈 고리 세 개 · 호박 구슬 · 좁은 골반 |
| D3 | 힙 타이트 3⁄4 후면 (베일 두 폭 사이 척추) |

**F1 · 얼굴 정면 클로즈업**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, front angle, breathtakingly beautiful elf queen, refined balanced facial proportions, beauty-first casting, otherworldly non-human features tied to no region, wide-set expressive eyes, delicately defined brow line, clear even complexion, striking symmetry without being mask-like, pale gold-green hair falling straight past the shoulders, long pointed ears, large expressive jade-green eyes ringed with gold, clean upper-lid crease, long dark lashes, calm faraway gaze that is still warm and alive, high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen, tapered oval jawline, refined chin, real fair skin with the faintest green undertone, visible pores, fine peach fuzz, natural subsurface scattering, no facial markings, soft high diffuse daylight through a scrim, very low contrast, faint cool green bounce
```

**F2 · 얼굴 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, three-quarter angle, head turned 45 degrees to camera left, same face as reference, otherworldly non-human features tied to no region, wide-set expressive eyes, delicately defined brow line, clear even complexion, striking symmetry without being mask-like, refined balanced facial proportions, pale gold-green hair, long pointed ear fully visible, large expressive jade-green eyes ringed with gold, clean upper-lid crease, long dark lashes, calm living gaze, high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen, tapered oval jawline, refined chin, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, no facial markings, soft high diffuse daylight through a scrim, very low contrast, faint cool green bounce
```

**F3 · 얼굴 정측면 프로필**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, strict side profile, 90 degrees to camera left, same face as reference, otherworldly non-human features tied to no region, wide-set expressive eyes, delicately defined brow line, clear even complexion, striking symmetry without being mask-like, clean silhouette of a high straight nose bridge with a refined tip, full well-shaped lips and a softly tapered oval chin, long pointed ear in full profile, long dark lashes reading in profile, two fine braids running back from the temple, pale gold-green hair falling far below the frame, long slender neck, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, no facial markings, soft high diffuse daylight through a scrim, very low contrast, faint cool green bounce
```

**B1 · 전신 정면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, chin level, calm neutral expression, tallest and slimmest silhouette in the cast, long smooth neck arms and legs, narrow shoulders, small narrow hips, high clearly shaped bust reading clearly through the clinging silk, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, a three-layer costume with no thickness anywhere, an ivory silk sheath worn next to the skin as a single thin opaque layer with a deep V neckline baring the cleavage, one continuous pale-green silk drape wrapped over it from the left shoulder across to the opposite hip, real silk with true drape and soft wrinkles pulled wet-look tight to the body, the material following every curve so the full silhouette of the bust, waist, hips and legs reads clearly through the silk, matte ivory leaf-vein embroidery worked across the drape, and over both a rib-cage frame woven from fine pared white living wood and dry pale bone, matte and slightly grained, curving along the ribs and drawing in hard at the waist, small amber sap beads set at its joints, the right side caught by three small bone loops with the slit opening high up the outside of the thigh all the way to the hipbone, sheer only at the veil, the back panel and the lower hem, a slender bone circlet at the crown with two panels of gossamer veil netting falling from it all the way to the floor, weightless and transparent, one panel outside each arm and hanging behind the arms so neither ever crosses the chest, dried leaves and seed pods stitched along the veil hem, pale gold-green hair falling below the knee, leaf-veined sheer thigh-high stockings, faint pale vein pattern along the collarbone, the throat and jaw completely clear, ivory, bone, pale green and amber, no metal, a slender staff of platinum-pale living wood spiralling upward, its tip splitting into branch-like fingers that cradle a large glowing crystal with light slowly swirling inside it, faint runes traced down the shaft, tiny leaves and seed motes hovering weightlessly around the crystal, held upright at her side
```

**B2 · 전신 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body three-quarter view, body turned 45 degrees to camera right, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral A-pose, weight even on both feet, calm neutral expression, extremely long-limbed slim silhouette, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, an ivory silk sheath next to the skin with a deep V neckline baring the cleavage, the pale-green silk drape crossing diagonally over it from shoulder to opposite hip in a single thin opaque layer, real silk with true drape and soft wrinkles clinging wet-look to the body, matte ivory leaf-vein embroidery across it, a rib-cage frame of pared white living wood and dry pale bone curving along the ribs over the silk and drawing in at the waist, matte and slightly grained, amber sap beads at its joints, the unsewn side held by three bone loops with the slit opening high up the outside of the thigh all the way to the hipbone so the whole length of one leg reads, the material following every curve so the bust, the long waist and the line of the hip and thigh read clearly through the clinging silk rather than bared, a slender bone circlet at the crown with two panels of gossamer veil netting falling from it to the floor, weightless and transparent, reading as one unbroken column from crown to floor in profile, dried leaves and seed pods stitched along the hem, leaf-veined sheer thigh-high stocking, hair falling below the knee, nothing at the throat, a slender staff of platinum-pale living wood spiralling upward, its tip cradling a large glowing crystal with light swirling inside it, faint runes down the shaft, tiny leaves and seed motes hovering around the crystal, held upright at her side
```

**B3 · 전신 후면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body back view, facing fully away from camera, same figure as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, standing straight, arms slightly away from the body, pale gold-green hair swept entirely over one shoulder to the front so the back is clear, back open from the nape down past the waist, long clean spine line, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, narrow shoulders, small narrow hips, a slender bone circlet at the crown with two panels of gossamer veil netting falling from it to the floor, weightless and transparent, the two panels split wide either side of the spine so the whole centre of the bare back is left completely open between them, the bare skin and the spine line reading clearly in the gap, the back of the rib-cage frame in pared white living wood and dry pale bone arcing over the ribs and drawing in at the waist, matte and slightly grained, dried leaves and seed pods stitched along the veil hem, the silk drape crossing low across the hip and sheer only here at the back, real silk with true drape and soft wrinkles moulded to the hip so the curve reads clearly through it, leaf-veined sheer thigh-high stockings, no staff
```
**[NEG+]** `face visible, head turned to camera, hair covering the back, veil covering the spine, single wide veil panel, cape, staff`

**D1 · 상반신 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, tight upper-torso crop framed from the jawline down to the lower ribs, face out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, shoulders square to camera, an ivory silk sheath next to the skin cut in a deep V neckline baring the cleavage, a single thin pale-green silk panel drawn diagonally over it from the left shoulder across the chest, opaque and skin-tight, real silk with true drape and soft wrinkles pulled wet-look over the body, fabric tension lines radiating from the shoulder knot, matte ivory leaf-vein embroidery worked across the panel, the material following every curve so the high clearly shaped bustline reads clearly, the deep V baring skin at the cleavage, a rib-cage frame of fine pared white living wood and dry pale bone laid over the silk and curving along the ribs, matte and slightly grained against the soft silk, small amber sap beads at its joints, one shoulder and arm completely bare, narrow shoulder line, delicate collarbones and the base of the throat left completely clear, faint pale vein pattern tracing the collarbone, a panel of transparent gossamer veil netting hanging past the shoulder at the edge of frame, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering
```
**[NEG+]** `head in frame, face, staff`

**D2 · 허리·골반 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, hips-and-waist crop framed from just below the ribcage to above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, the right side of the silk drape held closed by three small bone loops at rib, waist and hipbone with the slit below them opening high up the outside of the thigh all the way past the lowest loop to the hipbone itself, a long strip of bare thigh and hip showing down the open side, a single thin opaque layer of silk covering the torso and clinging wet-look so the long flat waist and small narrow pelvis read completely through the cloth, real silk with true drape and soft wrinkles, second-skin fit, the material following every curve, matte ivory leaf-vein embroidery across the silk, the lower ribs of a frame in pared white living wood and dry pale bone converging over the silk and cinching hard at the narrowest point of the waist, matte and slightly grained, small amber sap beads set where the ribs meet, gentle shallow waist-to-hip taper, a panel of transparent gossamer veil netting hanging past the hip at the edge of frame, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, the top edge of a leaf-veined sheer stocking at the lower edge of frame
```
**[NEG+]** `head in frame, face, staff, wide hips`

**D3 · 힙 타이트 3⁄4 후면**
```
[FIX] unretouched photograph, fine film grain, 3:4, rear three-quarter crop framed from the mid-back down to just above the knee, head out of frame, hair swept forward out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, bare smooth back down past the waist, long clean spine line, real fair skin, visible pores, fine peach fuzz, natural subsurface scattering, two panels of transparent gossamer veil netting hanging either side of the spine and leaving the whole centre of the bare back open between them, weightless and see-through where they fall over the skin, dried leaves and seed pods stitched along their hems, the back of a rib-cage frame in pared white living wood and dry pale bone crossing the small of the back and cinching at the waist, matte and slightly grained, small high narrow hip, the pale-green silk crossing low across the hip and covering it, moulded skin-tight to the hip so the curve reads clearly through the cloth, the side slit opening high up the outside of the thigh all the way to the hipbone, real silk with true drape and soft wrinkles, very long thigh, the top edge of a leaf-veined sheer stocking at the lower edge of frame
```
**[NEG+]** `head in frame, face, hair covering the back, veil covering the spine, single wide veil panel, staff`

**[NOTE]** 잎맥 문양은 절대 얼굴에 올리지 않는다 — 쇄골 아래·다리에만 아주 옅게, 안 되면 후보정으로 얹는다. `alien`·`inhuman`·`creepy`는 네거티브 고정.
**베일은 두 폭이고 척추 양옆으로 갈라진다** — 한 폭짜리 넓은 베일이 나오면 등 노출 캐논이 죽는다(B3·D3 NEG+에 `single wide veil panel`·`veil covering the spine` 고정). 베일은 `gossamer veil netting, weightless and transparent`로만 쓰고 두꺼워지면 실패컷. **뼈·생목 프레임은 갑옷이 아니다** — 갈비뼈를 따라 흐르는 가는 가지 구조이고 몸통을 판으로 덮지 않는다(덮는 순간 정면 실루엣이 죽는다). 금속은 여전히 0.
지팡이는 백금빛 생목 + 빛이 도는 수정 + 룬으로 고정 — 소박한 생목 막대기 어휘는 쓰지 않는다(칙칙하면 실패컷). 마름은 `slim`류 형용사가 아니라 긴 사지 + 낮은 대비 조명으로 만든다(마름 토큰을 밀면 병약해진다). 투명감은 `natural subsurface scattering` + 초저대비 확산광이 만들지 `dewy luminous`가 만들지 않는다.

---

### 4. 프레이야 (Freya) — 야성 관능형

**[NEG]**
```
[NEG-공통] + slit pupils, vertical pupils, reptilian eyes, extra pupils, fangs, visible canines, open mouth showing teeth, snarling, feral, savage grimace, scales on the face, horns, wings, tail, over-smoothed doll skin, heavy wrinkles, gaunt, masculine jaw, heavy square jaw, thick neck, androgynous, chubby, overweight, fat, thick waist, heavy build, plump face, double chin, belly fat, thick heavy thighs, stocky, muddy underexposed skin, dark muddy skin, pale skin, dry taut leathery skin, sun-weathered skin, cheap costume, stripper outfit, plastic, tacky, chainmail bikini, harness, bikini top, bare stomach, exposed midriff, thick chunky chains, plate armour, steel armour, gorget, neck brace, spiked collar, sword, staff, silver jewelry, nude, topless, exposed nipples, lingerie as outerwear, stripper outfit, chainmail bikini, cheap costume, tacky, vulgar, loose fabric, baggy, shapeless, boxy silhouette, bulky armour, heavy layered robes, historically accurate medieval clothing, modest, frumpy, oversized garment, hidden figure
```

| 컷 | 내용 |
|---|---|
| F1 | 얼굴 정면 클로즈업 (둥근 동공 고정) |
| F2 | 얼굴 3⁄4 |
| F3 | 얼굴 정측면 프로필 |
| B1 | 전신 정면 (**머리 뒤 부채꼴 크레스트 칼라** + 비늘 세공 보디피스 + 용금 사슬 벨트 + 잉걸 주홍 실크 자락) |
| B2 | 전신 3⁄4 (칼라 옆면 실루엣) |
| B3 | 전신 후면 (칼라가 척추에서 떠 있고 **등판 없음**) |
| D1 | 상반신 타이트 — 비늘 보디피스 · 깊은 넥라인(가슴골) · 금세공 테두리 · 칼라 밑동 |
| D2 | 허리·골반 타이트 — 옆구리·허리 열림 · 용금 사슬 벨트 · 최소 허리 · 탄탄한 힙 |
| D3 | 힙 타이트 3⁄4 후면 (맨 등 + 사슬 벨트) |

**F1 · 얼굴 정면 클로즈업**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, front angle, wildly beautiful woman, refined balanced facial proportions, beauty-first casting, striking exotic features tied to no single region, wide-set eyes, strongly defined brow line, clear even complexion, striking symmetry without being mask-like, tousled molten copper-red waves, dark red roots brightening to fire at the ends, large expressive slightly upturned molten gold eyes, round pupils, clean upper-lid crease, long dark lashes, hungry gaze but warm and alive, high straight nose bridge with a refined tip, tapered oval jawline, refined chin, softly rounded cheeks, full well-shaped lips slightly parted with a soft natural sheen, teeth not visible, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush, clean skin on the face, warm golden key one stop up from a practical tungsten source, soft warm amber bounce fill
```

**F2 · 얼굴 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, three-quarter angle, head turned 45 degrees to camera right, same face as reference, striking exotic features tied to no single region, wide-set eyes, strongly defined brow line, clear even complexion, striking symmetry without being mask-like, refined balanced facial proportions, tousled molten copper-red waves pushed back off the temple, large expressive molten gold eyes, round pupils, clean upper-lid crease, long dark lashes, full well-shaped lips slightly parted with a soft natural sheen, teeth not visible, high straight nose bridge with a refined tip, tapered oval jawline, refined chin, softly rounded cheeks, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush, clean skin on the face, warm golden key one stop up from a practical tungsten source, soft warm amber bounce fill
```

**F3 · 얼굴 정측면 프로필**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, strict side profile, 90 degrees to camera right, same face as reference, striking exotic features tied to no single region, wide-set eyes, strongly defined brow line, clear even complexion, striking symmetry without being mask-like, clean silhouette of a high straight nose bridge with a refined tip, full well-shaped slightly parted lips and a tapered oval jawline with a refined chin, teeth not visible, long dark lashes reading in profile, tousled copper-red waves piled back with loose strands escaping, ear visible, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush, clean skin on the face and neck, warm golden key one stop up from a practical tungsten source, soft warm amber bounce fill
```

**B1 · 전신 정면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, chin level, calm neutral expression, the most extreme hourglass in the cast built on a tiny waist, full firm high bust, extremely slim waist, tight round hips, long toned smooth legs, narrow smooth shoulders, a finely goldsmithed obsidian dragon-scale bodypiece covering the front of the torso from the collarbones down over the ribs and stomach to the hipbones, moulded to the body like a second skin, each scale individually set and following every curve so the drop from the full high bust into the tiny waist and out again over the round hips reads entirely through the scalework, gold filigree edging on every panel, hand-chased goldwork with visible tool marks, a deep neckline plunging low between the breasts baring a deep line of cleavage, both sides open so a wide band of bare skin shows down each flank and around the waist between the front panel and the hip panel, crossed only by two hair-fine gold wires, no back panel at all, expensive jeweller's craftsmanship rather than a costume, a fan-shaped crest collar of larger obsidian scale plates springing from the two shoulder points and rising in a wide radiating fan behind her head, every plate edged in dragon gold with visible chisel marks and growing larger toward the top, the throat and the whole front of the neck completely bare and unornamented, a dragon-gold chain belt wrapped twice low across the hips pulling the scale panels tight, a long ember-scarlet real-silk drape with true drape and soft wrinkles falling from the waist to the floor and split up one side only to mid-thigh, barefoot, fine gold rings at the ankles, faint same-tone scales along the outer arms, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush, obsidian black, dragon gold and ember scarlet, no weapon
```

**B2 · 전신 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body three-quarter view, body turned 45 degrees to camera left, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral A-pose, weight even on both feet, calm neutral expression, extreme hourglass on a tiny waist, full firm high bust, extremely slim waist, tight round hip, long toned smooth legs, the goldsmithed obsidian scale bodypiece covering the front of the chest, ribs and stomach, moulded to the body like a second skin, a deep neckline plunging low between the breasts baring a deep line of cleavage, the flank and the whole waist left bare between the front panel and the hip panel with two hair-fine gold wires crossing the opening, gold filigree edging and hand-chased goldwork with visible tool marks, each scale following every curve so the full bust and the round hip read clearly through the scalework while the sculpted narrow waist reads on bare skin, a fan-shaped crest collar of larger obsidian plates rising from the shoulder points behind her head, edged in dragon gold with visible chisel marks, reading as a raised fan against the sky in three-quarter with the throat and the front of the neck left completely bare, a dragon-gold chain belt wrapped twice low across the hips, an ember-scarlet real-silk drape with true drape and soft wrinkles split up one side only to mid-thigh and trailing behind, barefoot, fine gold ankle rings, faint same-tone scales along the spine and outer arms, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush, no weapon
```

**B3 · 전신 후면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body back view, facing fully away from camera, same figure as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, standing straight, arms slightly away from the body, tousled copper-red waves falling to mid-back, a fan-shaped crest collar of larger obsidian plates edged in dragon gold springing from the two shoulder points and rising behind the head, standing well clear of the spine and touching the back nowhere, the bodypiece has no back panel at all, only two hair-fine gold wires crossing the completely bare smooth back beneath the raised collar, deep spine line with faint same-tone scales along it fully visible under the collar, tight round hip below an extremely slim waist, a dragon-gold chain belt wrapped twice low across the hips, goldsmithed obsidian scalework closing low across the pelvis with hand-chased tool marks, moulded to the hip so the curve reads clearly through it, an ember-scarlet real-silk drape with true drape and soft wrinkles falling from the waist to the floor, barefoot, fine gold ankle rings, long toned smooth legs, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush
```
**[NEG+]** `face visible, head turned to camera, back panel, collar covering the back, cape, wings`

**D1 · 상반신 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, tight upper-torso crop framed from the jawline down to the lower ribs, face out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, shoulders square to camera, the finely goldsmithed obsidian dragon-scale bodypiece covering the front of the chest and ribs, gold filigree edging, individually set stone and hand-chased goldwork with visible tool marks, a deep neckline plunging low between the breasts with a deep line of cleavage showing between the gold-edged scale panels, the scalework moulded to the body like a second skin, each scale following every curve so the full firm high shape reads entirely through the goldwork, the panel stopping at the side seam with bare skin showing along the flank at each edge of frame, the root of a fan-shaped obsidian crest collar entering frame at each shoulder point and angling up and out of frame, its plates edged in dragon gold with visible chisel marks, the base of the throat and the collarbones left completely bare and unornamented between them, narrow smooth shoulder line, delicate collarbones, expensive jeweller's craftsmanship rather than a costume, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush, faint same-tone scales along the outer arms
```
**[NEG+]** `head in frame, face, plate armour, steel armour, weapon`

**D2 · 허리·골반 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, hips-and-waist crop framed from just below the ribcage to above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, the finely worked obsidian scalework running down the front of the stomach and closing low across the pelvis, moulded to the body like a second skin, gold filigree edging and hand-chased tool marks, both sides open so a wide band of bare skin runs down each flank and around the waist between the front panel and the hip panel, two hair-fine gold wires crossing the opening, an extremely slim waist read on bare skin above a tight round hip read through the shaped scale panels, a dragon-gold chain belt wrapped twice low across the hips and pulling the scale panels tight, fine linked goldwork with visible tool marks, long toned smooth thigh, the ember-scarlet real-silk drape split up one side only, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush
```
**[NEG+]** `head in frame, face, plate armour, steel armour, weapon, thick chunky chain`

**D3 · 힙 타이트 3⁄4 후면**
```
[FIX] unretouched photograph, fine film grain, 3:4, rear three-quarter crop framed from the mid-back down to just above the knee, head out of frame, hair swept forward out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, completely bare smooth back with two hair-fine gold wires crossing it, the bare skin continuing round the flank and the waist to the edge of the front scale panel, deep spine line, a dragon-gold chain belt wrapped twice low across the hips with fine linked goldwork and visible tool marks, the goldsmithed obsidian scalework moulded low over the hip like a second skin with hand-chased tool marks, tight round hip flaring from an extremely slim waist and read entirely through the scalework, long toned smooth thigh, an ember-scarlet real-silk drape with true drape and soft wrinkles hanging from the waist behind, real sun-kissed golden tan skin, visible pores, fine peach fuzz, no airbrush
```
**[NEG+]** `head in frame, face, back panel, plate armour, steel armour, weapon, thick chunky chain`

**[NOTE]** F 컷에 `round pupils` + `teeth not visible` 고정 — 세로 동공·긴 송곳니는 얼굴을 즉시 괴물로 만든다. 필요하면 눈만 잡는 인서트나 후보정에서만 세로 동공을 넣는다. **크레스트 칼라는 F 컷에 넣지 않는다**(얼굴 컷의 [NEG+/F]에 이미 `armour`·`crown`이 걸려 있고, 칼라가 들어오면 헤어라인과 턱선을 먹는다 — 칼라는 B 컷부터).
**칼라 3원칙:** ①어깨 두 점에서만 솟는다(목을 감아 올리지 않는다 — 목 앞·턱 아래는 언제나 비운다) ②척추에서 띄워 세운다(등판 0 캐논이 살아야 한다 — B3·D3 NEG+에 `collar covering the back` 고정) ③비늘 판이 위로 갈수록 커지는 부채이지 뿔·날개·목가리개가 아니다(`horns, wings, gorget, neck brace, spiked collar` 네거티브 고정).
피부는 톤만 밝게 가고 오일 광택은 넣지 않는다(모공·솜털 유지). 굴곡 최대치는 살이 아니라 **허리를 더 조이고 다리를 더 길게** 해서 만든다 — `chubby` 계열 네거티브 고정.

---

### 5. 비비안 (Vivian) — 비싸게 만들어진 인공 미인

**[NEG]**
```
[NEG-공통] + crooked teeth, over-smoothed doll skin, caked makeup, clown makeup, smeared lipstick, heavy wrinkles, gaunt, flawless symmetry, masculine jaw, heavy square jaw, thick neck, androgynous, dry taut leathery skin, tan skin, freckles, messy flyaway hair, frizzy hair, visible wig line, scowl, sneer, chubby, plump face, thick waist, wide hips, neckline plunging to the navel, hip-high slit, robe hanging fully open, staff, wand, nude, topless, exposed nipples, lingerie as outerwear, stripper outfit, chainmail bikini, cheap costume, tacky, vulgar, loose fabric, baggy, shapeless, boxy silhouette, bulky armour, heavy layered robes, historically accurate medieval clothing, modest, frumpy, oversized garment, hidden figure
```

| 컷 | 내용 |
|---|---|
| F1 | 얼굴 정면 클로즈업 (관 제외) |
| F2 | 얼굴 3⁄4 (관 제외) |
| F3 | 얼굴 정측면 프로필 (관 제외) |
| B1 | 전신 정면 — **취임식 예복** (보닝 코르셋 + **허리 뒤 은세공 아치** + 삼각 캐서드럴 트레인) |
| B2 | 전신 3⁄4 — 예복 (아치·트레인 옆면 실루엣) |
| B3 | 전신 후면 — 예복 (**은세공 아치 + 바닥에 삼각으로 펼친 트레인**) |
| B4 | 전신 정면 — **란제리 (4~5화)** |
| D1 | 상반신 타이트 — 보닝 코르셋 · 청보라 보석 열 · 가슴골까지 V · 어깨선 (예복) |
| D2 | 허리·골반 타이트 — 코르셋 보닝 · 허벅지 위쪽까지 슬릿 (예복) |
| D3 | 힙 타이트 3⁄4 후면 — 코르셋 레이싱 · 아치 밑동 · 트레인 발사점 (예복) |

**F1 · 얼굴 정면 클로즈업**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, front angle, exquisitely glamorous woman, refined balanced facial proportions, beauty-first casting, european features, eyes set deep under a clearly defined brow ridge, high straight nose bridge running straight down from the brow, strongly defined brow line, clear even complexion with a cool undertone, striking symmetry without being mask-like, glass-smooth jet black hair parted and pinned back, not a single loose strand, large expressive cool violet-blue eyes, clean upper-lid crease, long dark lashes, sharp winged liner, high arched brows, alive appraising gaze, high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen, tapered oval jawline, refined chin, real cream ivory skin, visible pores, fine peach fuzz, a light natural sheen from skincare not from retouching, chin lifted a fraction, gaze angled slightly down, bright cold beauty lighting, large frontal softbox, silver reflector under the chin
```

**F2 · 얼굴 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, three-quarter angle, head turned 45 degrees to camera left, same face as reference, european features, eyes set deep under a clearly defined brow ridge, high straight nose bridge running straight down from the brow, strongly defined brow line, clear even complexion with a cool undertone, striking symmetry without being mask-like, refined balanced facial proportions, glass-smooth jet black hair pinned back with no loose strands, large expressive cool violet-blue eyes, clean upper-lid crease, long dark lashes, sharp winged liner, arched brows, high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen, tapered oval jawline, refined chin, real cream ivory skin, visible pores, fine peach fuzz, a light natural sheen from skincare not from retouching, chin lifted a fraction, bright cold beauty lighting, large frontal softbox, silver reflector under the chin
```

**F3 · 얼굴 정측면 프로필**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, strict side profile, 90 degrees to camera left, same face as reference, european features, eyes set deep under a clearly defined brow ridge, high straight nose bridge running straight down from the brow, strongly defined brow line, clear even complexion with a cool undertone, striking symmetry without being mask-like, clean silhouette of a high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen and a tapered oval jawline with a refined chin, long dark lashes reading in profile, glass-smooth jet black hair with a mirror-bright sheen pinned at the back of the head, long clean neck, real cream ivory skin, visible pores, fine peach fuzz, a light natural sheen from skincare not from retouching, bright cold beauty lighting, large frontal softbox, silver reflector under the chin
```

**B1 · 전신 정면 (취임식 예복)**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, chin level, calm neutral expression, slim glamorous figure, narrow shoulders, very small waist, straight legs, small firm hip, a three-layer pearl-white ceremonial gown, a pearl-white satin sheath worn skin-tight next to the body, over it a silver-thread embroidered corset bodice with the boning exposed on the outside and a close row of ice-violet stones set along every seam, a V neckline plunging deep into the cleavage with dense silver embroidery filling the line below it, the corset moulded to the torso like a second skin, lifting the bust into a high rounded line above a sculpted narrow waist, bare shoulders, the throat and collarbones left completely bare with no necklace, long white gloves ending well past the elbow with a row of small pearl buttons down the back of each hand, real woven silk satin with a visible weave and natural creasing, the satin skirt cut skin-tight over the hip and thigh so the full silhouette of the waist, hips and legs reads clearly through it, skirt slit high on one side, opening up the outside of the thigh all the way to the hipbone so the whole line of one leg reads, a pierced silver filigree arch with visible file marks rising from the small of the back in the same spire vocabulary as her crown and standing clear of the body, a three-metre silver-white cathedral train launching from that arch and spreading into a wide triangle across the floor behind her, ice-violet lining and a lattice of silver thread along its edge, silver stiletto heels, silver spire crown pinned into the glass-smooth black hair, gold dust on the collarbones, real cream ivory skin, visible pores, fine peach fuzz, no airbrush
```

**B2 · 전신 3⁄4 (예복)**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body three-quarter view, body turned 45 degrees to camera right, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral A-pose, weight even on both feet, calm neutral expression, slim glamorous figure, narrow shoulders, very small waist, a pearl-white satin sheath next to the body under a silver-embroidered corset bodice moulded to the torso like a second skin, the boning exposed on the outside with a row of ice-violet stones along every seam, a V neckline plunging deep into the cleavage under dense silver embroidery, bare shoulders and upper back, nothing at the throat, long white gloves past the elbow with pearl buttons down the back of the hand, real woven silk satin with a visible weave and natural creasing, the satin figure-hugging over the hip and thigh so the whole line of the body reads in profile, the skirt slit running high up the near side all the way to the hipbone, a pierced silver filigree arch with visible file marks rising from the small of the back and reading clear of the body in three-quarter, the three-metre silver-white cathedral train launching from it and spreading wide across the floor behind, ice-violet lining and a silver-thread lattice along its edge, silver stiletto heels, silver spire crown pinned into the glass-smooth black hair, real cream ivory skin, visible pores, fine peach fuzz, no airbrush
```

**B3 · 전신 후면 (예복)**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body back view, facing fully away from camera, same figure as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, standing straight, arms slightly away from the body, glass-smooth jet black hair half-pinned under a silver spire crown seen from behind, silver-thread corset lacing running down the bare smooth upper back with ice-violet stones along the boning either side of it, the bodice moulded to a sculpted narrow waist, the upper back left completely bare above the lacing, real woven silk satin with a visible weave and natural creasing, the satin pulled skin-tight over a small firm hip so the curve reads clearly through it, real cream ivory skin, visible pores, fine peach fuzz, no airbrush, a pierced silver filigree arch with visible file marks rising from the small of the back in the same spire vocabulary as the crown, standing clear of the body and low enough to leave the whole upper back open, the three-metre silver-white cathedral train launching from that arch and spreading into a wide triangle across the floor behind, ice-violet lining showing where it turns and a lattice of silver thread along its edge, long white gloves, silver stiletto heels
```
**[NEG+]** `face visible, head turned to camera, over-the-shoulder look`

**B4 · 전신 정면 (란제리 · 4~5화)**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, chin level, calm neutral expression, slim glamorous figure, narrow shoulders, very small waist, straight legs, black silk lingerie set, thin strap bra with fine black lace edging, garter belt, sheer stockings, a black real-silk robe worn off one shoulder with the sash tied at the waist so the robe falls closed over the torso and only one shoulder and the line of one leg are open, black thread embroidery worked along the robe hem and cuffs only, the thin silk clinging to the waist and hip so the full silhouette reads clearly through it, real silk with true drape and soft wrinkles, barefoot, silver spire crown still pinned into the glass-smooth jet black hair, real cream ivory skin, visible pores, fine peach fuzz, no airbrush
```
**[NEG+]** `ceremonial gown, corset, white gloves, train, filigree arch, heels, warm lamplight`

**D1 · 상반신 타이트 (예복)**
```
[FIX] unretouched photograph, fine film grain, 1:1, tight upper-torso crop framed from the jawline down to the lower ribs, face out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, shoulders square to camera, pearl-white silver-thread embroidered corset bodice moulded to the torso like a second skin, a V neckline plunging deep into the cleavage with dense silver embroidery filling the line below it, real woven fabric texture with a visible weave, the boning exposed on the outside of the satin with a close row of small ice-violet stones set along every seam, the boning lifting and rounding the bust into a high line, the satin pulled taut so the full shape of the bust and ribcage reads through it, bare narrow shoulders and collarbones with the throat left completely bare and no necklace, long white gloves entering the frame at the upper arms with a row of small pearl buttons down the back of the hand, gold dust on the collarbones, real cream ivory skin, visible pores, fine peach fuzz, no airbrush
```
**[NEG+]** `head in frame, face, crown, lingerie`

**D2 · 허리·골반 타이트 (예복)**
```
[FIX] unretouched photograph, fine film grain, 1:1, hips-and-waist crop framed from just below the ribcage to above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, exposed silver-thread corset boning with a close row of small ice-violet stones along every seam tapering to a sculpted very small waist, the corset point ending low at the front of the pelvis, narrow straight hip with almost no flare, pearl-white satin skirt cut skin-tight over the hip and upper thigh, the material following every curve, slit high on one side, opening up the outside of the thigh all the way to the hipbone with the bare leg showing the whole way, real woven silk satin with a visible weave and natural creasing, the lowest run of the silver-white train falling away at the far edge of frame, real cream ivory skin, visible pores, fine peach fuzz, no airbrush, the satin pulling smooth and taut across the front of the hip
```
**[NEG+]** `head in frame, face, crown, wide hips, lingerie`

**D3 · 힙 타이트 3⁄4 후면 (예복)**
```
[FIX] unretouched photograph, fine film grain, 3:4, rear three-quarter crop framed from the mid-back down to just above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, silver-thread corset lacing running down the back between rows of exposed boning set with small ice-violet stones, small firm hip under skin-tight pearl-white satin moulded to the curve, with a visible weave and natural creasing, real cream ivory skin, visible pores, fine peach fuzz, no airbrush, the foot of a pierced silver filigree arch with visible file marks anchored at the small of the back at the top of frame, the silver-white cathedral train launching from it and falling away across the floor out of frame with its ice-violet lining showing where it turns, the high slit opening along the near side all the way to the hipbone
```
**[NEG+]** `head in frame, face, crown, wide hips, lingerie`

**[NOTE]** 첨탑 관은 F 컷에서 뺀다 — 헤어라인을 먹고 이마 비율을 망친다(관은 B 컷부터, §8 식별자는 B가 담당).
**은세공 아치는 허리 뒤에서만 솟는다** — 어깨나 목에서 뻗으면 카타리나(어깨)·프레이야(칼라)와 실루엣이 겹치고, 등 상부 노출 캐논도 죽는다. 아치는 몸에서 떨어져 서고, 트레인은 거기서 **삼각으로 펼쳐진다**(케이프처럼 몸을 덮으면 실패컷). 밀도는 코르셋 보닝·보석 열·장갑 단추로만 올리고 **목·쇄골은 비운다** — 목걸이 금지.
오만함은 `sneer`·`frown`이 아니라 살짝 든 턱 + 내리깐 시선으로만 만들고, 인공 광택은 쇄골·가슴 윗면 하이라이트로만 얹는다(얼굴에 밀면 밀랍 인형). 이 인물은 "비싼 피부"가 컨셉이라 가장 CG로 빠지기 쉽다 — 모공을 지우지 않는다.

---

### 6. 모르가나 (Morgana) — 농익은 관능형

**[NEG]**
```
[NEG-공통] + crooked teeth, over-smoothed doll skin, elderly, old woman, middle-aged, grandmother, deep wrinkles, fine lines, crows feet, deep nasolabial folds, sagging jawline, sagging bust, jowls, crepey neck, frail, fully grey hair, dowdy, matronly, high hard cheekbones, masculine jaw, heavy square jaw, thick neck, androgynous, dry taut leathery skin, sun-weathered skin, chubby, overweight, plump face, double chin, thick waist, heavy build, slim boyish figure, bare arms, neckline plunging to the navel, harsh flash, nude, topless, exposed nipples, lingerie as outerwear, stripper outfit, chainmail bikini, cheap costume, tacky, vulgar, loose fabric, baggy, shapeless, boxy silhouette, bulky armour, heavy layered robes, historically accurate medieval clothing, modest, frumpy, oversized garment, hidden figure
```

| 컷 | 내용 |
|---|---|
| F1 | 얼굴 정면 클로즈업 |
| F2 | 얼굴 3⁄4 (은빛 새치 쪽) |
| F3 | 얼굴 정측면 프로필 |
| B1 | 전신 정면 (자수정 벨벳 + 흑레이스 + **양 팔꿈치에서 바닥까지 레이스 패널** + 흑금 벨트 + 부채) |
| B2 | 전신 3⁄4 (레이스 패널 날개 실루엣) |
| B3 | 전신 후면 (허리 바로 위까지 파인 등 · 레이스 패널이 뒤로 끌린다) |
| D1 | 상반신 타이트 — 데콜테 · 레이스 · 오프숄더 (넥라인 가장자리는 비운다) |
| D2 | 허리·골반 타이트 — 흑금 세공 벨트 · 덩굴 자수 · 코르셋 조임 · 머메이드 |
| D3 | 힙 타이트 3⁄4 후면 (레이스 패널 밑단) |

**F1 · 얼굴 정면 클로즈업**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, front angle, stunningly beautiful noblewoman, refined balanced facial proportions, beauty-first casting, southern european features with a warm olive complexion, deep-set eyes, defined brow line, striking symmetry without being mask-like, dark wine-black waves swept to one side, one single silver streak falling from the temple, large expressive heavy-lidded garnet-brown eyes, clean upper-lid crease, long dark lashes, half-closed appraising gaze that is warm and alive, high straight nose bridge with a refined tip, tapered oval jawline, refined chin, softly full cheeks, full well-shaped lips with a soft natural sheen with a faint knowing curve, real honey-olive skin, visible pores, a fine loose-powder finish, no airbrush, no lines, soft warm side key from a practical candle-toned source, gentle falloff, warm shadow side
```

**F2 · 얼굴 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, three-quarter angle, head turned 45 degrees to camera right so the swept side and the single silver temple streak face camera, same face as reference, southern european features with a warm olive complexion, deep-set eyes, defined brow line, striking symmetry without being mask-like, refined balanced facial proportions, dark wine-black waves, large expressive heavy-lidded garnet-brown eyes, clean upper-lid crease, long dark lashes, full well-shaped lips with a soft natural sheen, high straight nose bridge with a refined tip, tapered oval jawline, refined chin, softly full cheeks, real honey-olive skin, visible pores, a fine loose-powder finish, no airbrush, no lines, soft warm side key from a practical candle-toned source, gentle falloff
```

**F3 · 얼굴 정측면 프로필**
```
[FIX] unretouched photograph, fine film grain, 3:4, head-and-shoulders close-up, strict side profile, 90 degrees to camera right, same face as reference, southern european features with a warm olive complexion, deep-set eyes, defined brow line, striking symmetry without being mask-like, clean silhouette of a high straight nose bridge with a refined tip, full well-shaped lips with a soft natural sheen and a tapered oval jawline with a refined chin, heavy-lidded eye with long dark lashes in profile, single silver streak running back from the temple through dark wine-black waves, waves swept forward over the near shoulder, long neck, real honey-olive skin, visible pores, a fine loose-powder finish, no airbrush, no lines, soft warm side key from a practical candle-toned source, gentle falloff
```

**B1 · 전신 정면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body front view, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral relaxed A-pose, arms slightly away from the body, weight even on both feet, chin level, calm neutral expression, full ripe hourglass, full firm high bust, corset-cinched tiny waist, smooth round hips, long smooth legs, real honey-olive skin, visible pores, no airbrush, a three-layer gown, an under-layer of real black lace with a visible knit covering the neckline opening and running down both arms into long black gloves ending above the elbow, over it a boned deep amethyst velvet bodice with a wide off-shoulder neckline framing the collarbones and décolletage and the V plunging deep down into the cleavage, crushed velvet with a real nap that eats the light, the neckline edge left plain with lace only and no stones on it, off-shoulder cut leaving both shoulders and collarbones bare, the boned velvet bodice moulded to the body like a second skin, dark gold vine embroidery running from the waist down over the hip, a chased dark gold belt with visible tool marks clasping the waist and set with small garnet stones, mermaid skirt gripping the hip and thigh skin-tight and flaring only at the knee, the velvet pressed to the body so the full silhouette of the bust, waist and hips reads clearly through it, a back slit, two long panels of black lace falling from the elbows all the way to the floor and trailing behind her, scalloped at the hem, black ribbon choker holding a signet ring at the throat, closed ebony folding fan held down at her side, amethyst purple, black lace, dark gold and garnet
```

**B2 · 전신 3⁄4**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body three-quarter view, body turned 45 degrees to camera left, same face as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, neutral A-pose, weight even on both feet, calm neutral expression, full ripe hourglass, full firm high bust above a corset-cinched tiny waist, smooth round hip, real honey-olive skin, visible pores, no airbrush, deep amethyst velvet gown with a wide off-shoulder neckline framing the décolletage and the V plunging deep down into the cleavage under an under-layer of real black lace with a visible knit that runs on down both arms into long black gloves above the elbow, crushed velvet with a real nap that eats the light, the neckline edge left plain with lace only, off-shoulder cut, the boned velvet bodice moulded to the body like a second skin, dark gold vine embroidery running from the waist over the hip, a chased dark gold belt with garnet stones at the waist, skin-tight mermaid skirt gripping from waist to below the knee and flaring only at the knee, the velvet following every curve of the hip and thigh, two long panels of black lace falling from the elbows to the floor and trailing behind, reading as a wing shape against the body in three-quarter, black ribbon choker with a signet ring, closed ebony fan at her side, velvet nap catching light along the curve of the waist
```

**B3 · 전신 후면**
```
[FIX] unretouched photograph, fine film grain, 9:16, full-body back view, facing fully away from camera, same figure as reference, flat even studio key plus fill from a large softbox, bounce-card fill from front-left, real practical light sources, no colour cast, no rim light, standing straight, arms slightly away from the body, dark wine-black waves swept entirely over one shoulder to the front so the back is clear, the amethyst velvet gown cut open all the way down to the waistline, the whole back left bare and smooth above that edge, crushed velvet with a real nap that eats the light, real honey-olive skin, visible pores, no airbrush, long black gloves above the elbow, two long panels of real black lace with a visible knit falling from the elbows outside the arms all the way to the floor and pooling behind her, scalloped at the hem, hanging clear of the bare back and never crossing it, a chased dark gold belt with garnet stones at the waist and dark gold vine embroidery running down over the hip, mermaid skirt pulled skin-tight over a smooth round hip and long thigh, the velvet moulded to the curve below a sculpted narrow waist, back slit closed while standing, no fan
```
**[NEG+]** `face visible, head turned to camera, hair covering the back, lace covering the back, cape, fan`

**D1 · 상반신 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, tight upper-torso crop framed from the jawline down to the lower ribs, face out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, shoulders square to camera, deep amethyst velvet bodice with a wide off-shoulder neckline framing the collarbones and décolletage, the V plunging deep down into the cleavage, a black lace panel laid over the opening so the line beneath reads through it, real black lace with a visible knit and a scalloped edge, crushed velvet with a real nap that eats the light, the neckline edge left plain with lace only and no stones, embroidery or ornament on it, full firm bust held high by the boned bodice, the velvet moulded to the body like a second skin so the full shape of the bust and the drop into the ribcage reads clearly through it, off-shoulder cut leaving both smooth shoulders and delicate collarbones bare, matte velvet against transparent lace against bare skin in one frame, long black gloves entering the frame at the upper arms with the lace under-layer continuing into them, the top of a lace panel falling away from the elbow at the edge of frame, real honey-olive skin, visible pores, a fine loose-powder finish, no airbrush
```
**[NEG+]** `head in frame, face, fan, choker, necklace, bare arms`

**D2 · 허리·골반 타이트**
```
[FIX] unretouched photograph, fine film grain, 1:1, hips-and-waist crop framed from just below the ribcage to above the knee, head out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, deep amethyst velvet cinched hard into a sculpted tiny waist by corset boning, crushed velvet with a real nap that eats the light, a chased dark gold belt with visible tool marks clasping the narrowest point of the waist and set with a row of small garnet stones, dark gold vine embroidery spilling from under the belt down over the hip, the velvet moulded to the body like a second skin and flaring immediately below into a smooth round hip, skin-tight mermaid skirt gripping the hip and long smooth upper thigh, the material following every curve, the velvet nap catching light along the whole curve, a panel of real black lace with a visible knit hanging past the hip at the edge of frame, gloved hands out of frame
```
**[NEG+]** `head in frame, face, fan, flared skirt`

**D3 · 힙 타이트 3⁄4 후면**
```
[FIX] unretouched photograph, fine film grain, 3:4, rear three-quarter crop framed from the mid-back down to just above the knee, head out of frame, hair swept forward out of frame, same body and costume as reference, flat even studio key plus fill from a large softbox, bounce-card fill, real practical light sources, no colour cast, standing straight, the amethyst velvet gown open down to the waistline leaving the whole back bare and smooth above that edge, crushed velvet with a real nap that eats the light, real honey-olive skin, visible pores, no airbrush, a chased dark gold belt with garnet stones at the waist and dark gold vine embroidery running down over the hip, the mermaid skirt pulled skin-tight over a full round hip above a long smooth thigh, the velvet moulded to the curve so the whole line reads through it, the back slit closed and running down the centre, two panels of real black lace with a visible knit and scalloped hems falling outside the arms and pooling on the floor behind, hanging clear of the bare back, long black glove entering the frame at one side
```
**[NEG+]** `head in frame, face, hair covering the back, lace covering the back, cape, fan`

**[NOTE]** 숫자 나이는 물론 `mature`·`faint smile lines` 같은 성숙 토큰도 넣지 않는다 — 성숙함은 관자놀이 은빛 새치 한 줄기·팔꿈치 위 장갑·촛불 톤 사이드 키·반쯤 감긴 시선 넷이 전부 만든다. 주름 0이되 모공은 남긴다.
**레이스 패널은 팔꿈치에서 시작한다** — 어깨나 목에서 시작하면 케이프가 되고(그럼 등 노출 캐논이 죽는다), B3·D3 NEG+에 `lace covering the back`·`cape` 고정. 패널은 팔 **바깥**으로 떨어져 등을 스치지 않는다. **넥라인 가장자리는 레이스만 두고 비운다** — 보석·자수는 벨트와 장갑 끝단으로만 몰고, 얼굴 아래는 초커 하나만 남긴다.
딸(비비안)과 같은 프레임에 넣을 땐 키라이트를 모르가나 쪽에 준다.

---

## 10. 생성기 판별 테스트 (2단계)

캐릭터를 뽑기 전에 **툴이 뭘 못하는지부터** 가른다. 프롬프트를 아무리 다듬어도 툴 한계는 못 넘는다.

### 테스트 A — 실사 질감이 나오는가 (가장 중요)

```
live-action photography, shot on a full-frame cinema camera, 85mm prime lens, natural optics, candid editorial portrait of a beautiful young woman, front angle, long black hair, large bright eyes, full lips, real skin with visible pores, fine peach fuzz, natural subsurface scattering, subtle skin tone variation, no retouching, no airbrush, soft window light, shallow depth of field, fine film grain
```
```
NEG: 3d render, cgi, octane render, unreal engine, blender, digital painting, digital art, illustration, concept art, key visual, video game screenshot, anime, cel shading, airbrushed, plastic skin, waxy skin, doll skin, figurine, beauty filter, over-smoothed, blurry, lowres, watermark
```

**판정** — 뽑은 이미지를 100% 확대해서 **볼과 콧등의 모공·솜털**을 본다.
- 모공이 보이고 피부에 미세한 색차가 있으면 → **실사 통과.** §9로 진행.
- 피부가 균질하게 매끈하고 조명이 CG처럼 깨끗하면 → **툴이 실사를 못 낸다.** 프롬프트로는 못 고친다. 생성기를 바꾸거나, 실사 특화 모델·LoRA를 물려야 한다.

### 테스트 B — 미모가 나오는가

테스트 A를 통과한 뒤에만 의미가 있다. A와 같은 프롬프트에 아래를 더한다.

```
+ refined balanced facial proportions, large expressive eyes with a clean upper-lid crease, slightly deep-set, long dark lashes, high straight nose bridge with a refined tip, defined brow line, tapered oval jawline, refined chin, full well-shaped lips, clear even complexion, striking symmetry without being mask-like
```

- 얼굴이 확 올라가면 → 툴 정상. 문제는 프롬프트였고 §9로 해결된다.
- 이목구비가 여전히 무너지거나 언캐니하면 → **툴 한계.** 얼굴 특화 모델로 바꾸거나, 얼굴만 따로 뽑아 합성하는 파이프라인이 필요하다.

> 두 테스트 모두 **캐릭터와 무관한 중립 프롬프트**여야 판별이 된다. 여기에 캐릭터 설정을 섞으면 뭐가 원인인지 못 가른다.
