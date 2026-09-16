# v9 변경 목록 (2026-09-16)

정본 = `07_final/34_storm_dragon_bride_FINAL_v9_CN&KO&EN.docx` (v8 기준)

외부 AI 2차 리뷰를 사용자 기준("더 나빠질 의견은 제외 · 42화는 톤 정리")으로 걸러 반영 + 사용자 추가 지시(단일 동작 고열감 비트 · 뺀 두 동작의 새 자리 · 중간 회차 절절함 한 방).

게이트: 53화 · 영어 대사 488줄(+1) · 의도 밖 원문 손실 0줄 · 새 문장 24줄 전수 확인 · `name_leak_check.py` PASS.

---

## 1. 42화 톤 정리 — 삭제 2비트

선택 → 치유 → 고백 사이에 낀 정사 비트를 뺐다. 남긴 것 = 자기 입술 물기 · 손목 맥박 · 다리로 허리 감기 · "다시 말해 줘. 이번엔 내 귀에 대고."

```
△多里安的唇沿着奥菲莉娅的脖子往下，含住她的胸口，舌头慢慢碾过湿透的皮肤。奥菲莉娅仰起头，一只手向后抓住池边的黑石，呻吟压不住。
△도리안의 입술이 오필리아의 목을 따라 내려가 오필리아의 가슴을 문다. 도리안의 혀가 젖은 피부를 천천히 문지른다. 오필리아가 고개를 젖히고 한 손을 뒤로 뻗어 수조 가장자리의 검은 돌을 움켜쥔다. 신음이 참아지지 않는다.
△Dorian's mouth moves down Ophelia's neck and CLOSES over her breast, his tongue dragging slow across the wet skin. Ophelia's head TIPS back, one hand REACHING back to GRAB the black stone at the pool's edge, and she can't hold the moan back.
△奥菲莉娅张口含住多里安的指尖，舌尖扫过一下才松开，眼睛一直看着他。多里安的呼吸一滞。
△오필리아가 입을 벌려 도리안의 손끝을 문다. 혀끝으로 한 번 훑고 놓아주면서도 눈은 계속 도리안을 본다. 도리안의 숨이 멎는다.
△Ophelia takes his fingertip into her mouth, her tongue brushing it once before she lets go, her eyes never leaving his. His breath STOPS.
```

## 2. 오류 4건 수정

- 전: `△도리안의 눈에 광희가 폭발한다. 도리안은 몸을 숙여 오필리아의 입술에 깊게 입을 맞춘다.`
- 후: `△도리안의 눈에 광희가 폭발한다. 도리안은 몸을 숙여 오필리아의 입술을 향해 다가간다.`

- 전: `△Joy floods Dorian's eyes. Dorian leans down, pressing a deep, loving kiss to Ophelia's lips.`
- 후: `△Joy floods Dorian's eyes. Dorian leans down, moving in to kiss Ophelia's lips.`

- 전: `△도리안은 충격에 그녀를 바라본다. 오필리아는 허리를 굽혀 용골 단검을 집고, 손등으로 단검을 탁자에 세게 꽂는다.`
- 후: `△도리안은 충격에 그녀를 바라본다. 오필리아는 허리를 굽혀 용골 단검을 집고, 손을 뒤집어 단검을 탁자에 세게 꽂는다.`

- 전: `△Garrick puts on a look of great magnanimity, STEPPING toward Ophelia twice. Garrick holds out a hand, falsely gentle.`
- 후: `△Garrick puts on a look of great magnanimity, taking two steps toward Ophelia. Garrick holds out a hand, falsely gentle.`

- 전: `△Dorian's whole body STIFFENS. Dorian STARES in disbelief at Ophelia, wanting Dorian first, in Dorian's arms. Dorian's throat BOBS hard, Dorian's voice hoarse.`
- 후: `△Dorian's whole body STIFFENS. Dorian STARES in disbelief at Ophelia in his arms, reaching for him first. Dorian's throat BOBS hard, Dorian's voice hoarse.`

## 3. 삽입 7비트

### A-3 4화 칼날 — v8 L602 뒤
- 앞 줄: `△Dorian IGNORES the dagger and STEPS forward abruptly. The blade SLICES his neck, drawing blood — Dorian doesn't even flinch.`
- 왜: 무료 4화 신방 단검 대치 — 긴장만 있고 접촉이 늦은 자리. 그가 그녀 손을 덮어 칼날을 자기 목에 더 밀어 넣는 동작 하나. 바로 뒤 "그 칼은 안 아파, 네가 차가워지는 게 아파"가 세진다.
```
△多里安用自己的手覆住奥菲莉娅握着刀柄的手背，把刀刃往自己的咽喉里又推进去一点。奥菲莉娅的手指僵住，再也推不动。
△도리안이 자기 손으로 칼자루를 쥔 오필리아의 손등을 덮어, 칼날을 자기 목 안쪽으로 더 밀어 넣는다. 오필리아의 손가락이 굳어 더는 움직이지 못한다.
△Dorian COVERS Ophelia's hand on the hilt with his own and PUSHES the blade deeper into his own throat. Ophelia's fingers LOCK, and she can't move them.
```

### A-1 10화 목덜미 — v8 L1320 뒤
- 앞 줄: `△Dorian carefully UNDOES Ophelia's clothes, fingertips brushing Ophelia's bare back, sending a shiver through Ophelia.`
- 왜: 드레스 입혀주며 등이 드러났는데 손끝만 스치던 자리. 목덜미 윗등뼈에 입술 하나. 뒤 V.O. "네가 내 것이기만 하면"에 붙는다.
```
△多里安低下头，嘴唇按在奥菲莉娅后颈最上面的那节脊骨上，停了一下。奥菲莉娅的肩膀猛地缩起来。
△도리안이 고개를 숙여 오필리아의 목덜미 맨 윗등뼈에 입술을 대고 잠시 멈춘다. 오필리아의 어깨가 움츠러든다.
△Dorian LOWERS his head and PRESSES his lips to the top knob of Ophelia's spine, holding there. Ophelia's shoulders HITCH up.
```

### B-1 10화 가슴 — v8 L1348 뒤
- 앞 줄: `△Ophelia's fingers move slightly, letting one strap of the gown slide off on purpose. Pale skin and deep cleavage are bared right in front of Dorian.`
- 왜: 42화에서 뺀 가슴 비트의 새 자리. 그녀가 일부러 어깨끈을 내린 직후라 그가 무는 게 자연스럽고, 주도권은 그녀에게 남는다(발끝 세워 "권리를 일찍 행사하고 싶지 않냐").
```
△多里安低下头，一口咬住那片刚露出来的肌肤，舌头压着咬痕缓缓碾过一次。奥菲莉娅的呼吸猛地一乱。
△도리안이 고개를 숙여 방금 드러난 살결을 한입에 문다. 도리안은 문 자리를 혀로 천천히 한 번 문지른다. 오필리아의 숨이 크게 흐트러진다.
△Dorian DUCKS down and BITES the bared skin, his tongue DRAGGING once, slow, over the mark. Ophelia's breath BREAKS apart.
```

### B-2 23화 엄지 — v8 L2684 뒤
- 앞 줄: `△Dorian LIFTS Ophelia's chin with his thumb. Their lips stop a breath apart, his breathing landing on hers. Ophelia smiles.`
- 왜: 42화에서 뺀 손끝 비트의 새 자리. 그의 엄지가 이미 턱에 있어 동작을 새로 만들 필요가 없고, 이 한 번이 "As you wish, my Queen"을 항복으로 만든다.
```
△奥菲莉娅偏过头，用嘴唇裹住多里安抵在她下巴上的拇指，舌头贴着指腹压了一下，才让它滑出来。多里安的呼吸停住。
△오필리아가 고개를 살짝 돌려, 턱을 받치고 있던 도리안의 엄지를 입술로 감싼다. 오필리아는 혀로 엄지 안쪽을 한 번 누른 뒤 천천히 빠져나가게 둔다. 도리안의 숨이 멎는다.
△Ophelia TURNS her head and CLOSES her lips around the thumb propping up her chin, her tongue PRESSING flat against the pad once before she lets it slide free. Dorian's breath STOPS.
```

### A-2 26화 과즙 — v8 L2984 뒤
- 앞 줄: `△Ophelia's cheeks flush pink. Ophelia obediently bites down, juice spreading between her lips.`
- 왜: 신혼 일상 낮 장면 — 접촉 없이 다정하기만 한 자리에 혀 한 번. 바로 뒤 장군의 밀담이 끊고 들어와 여운이 남는다.
```
△多里安低下头，把奥菲莉娅嘴角的那滴果汁舔走。奥菲莉娅咬到一半僵住。
△도리안이 고개를 숙여 오필리아의 입가에 맺힌 과즙 한 방울을 혀로 핥아 간다. 오필리아는 과육을 씹다 말고 굳는다.
△Dorian leans in and LICKS the drop of juice from the corner of Ophelia's mouth. Ophelia FREEZES mid-bite.
```

### D-1 41화 어머니 — v8 L4643 뒤
- 앞 줄: `△Wrapped in a gentle glow of icy blue light, Mother slowly FADES away.`
- 왜: 어머니가 빛이 되어 사라지는 것과 비명 사이에 잡으려다 놓치는 손 하나. 로맨스 상징 없이 상실 반응만. 41화 죽음 → 42화 정사 전환이 급하다는 지적의 답.
```
△奥菲莉娅一只手臂还抱着多里安，另一只手猛地伸向那团正在散开的冰蓝色光。光从她的指缝里穿了过去，她什么也没抓到。
△오필리아는 한 팔로 도리안을 안은 채 다른 손을 흩어지는 얼음빛 푸른 광채로 뻗는다. 빛은 오필리아의 손가락 사이로 그대로 빠져나가고, 오필리아는 아무것도 잡지 못한다.
△Ophelia, one arm still around Dorian, THROWS her free hand out toward the scattering icy blue light. The light PASSES straight through her fingers. Ophelia catches nothing.
```

### C-1 30화 절절함 — v8 L3462 뒤 (대사)
- 앞 줄: `△Dorian's chest is bloodied and covered in poison. Dorian breathes hard, leaning weakly against the bedside to watch Ophelia's calm, sleeping face, a relieved smile touching Dorian's pale lips.`
- 왜: 그가 자기 심장에 독을 옮긴 직후, 잠든 그녀 얼굴을 보며. 그녀가 못 듣는 두 마디 — 34화 발견을 안 깨면서 이 작품에서 그가 사랑을 말로 못 하는 이유(비밀)가 가장 아프게 보이는 자리.
```
多里安（声音极轻）: 不会再疼了。我拿过来了。
도리안: (아주 낮은 목소리로) 이제 안 아플 거야. 내가 가져왔어.
DORIAN: (barely a whisper) It won't hurt anymore. It's in me now.
```

## 4. 외부 리뷰에서 뺀 것

- 9화 5컷 — 넣지 않음. "원하는 건 뭐든 가져가"는 자신을 내주는 말이고 끝 V.O.를 쥔 쪽이 오필리아여야 한다. 원작 그대로.
- 24화 추가 압축 — 구체적 자리 없음. v7에서 이미 셋 뺐고 더 빼면 열감이 준다.
- 35화 떠나다 멈칫 — 작별 반복 위험(리뷰 자신도 경고).
- 27·31·38·49·50화 애틋함 — 리뷰 판단대로 불필요. 50화는 내 전제(손을 건네는 동작이 없다)가 틀렸음 — 이미 손을 꼭 붙잡고 있다.
- 채택 안 한 후보 = 11화 가슴(10화와 연속) · 22화 손끝(23화와 연속) · 34화 독문 위에 손 · 31화 정수리에 얼굴 묻기(절절함은 하나만).
