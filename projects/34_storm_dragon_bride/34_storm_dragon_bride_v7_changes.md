# v7 변경 목록 (2026-09-16)

정본 = `07_final/34_storm_dragon_bride_FINAL_v7_CN&KO&EN.docx` (v6 기준 · 줄 편집 39개 = 축약 10건 · 삭제 2건 · 순서 조정 1건)

사용자 판단 = "타당한 부분도 있다. 그러나 **열감이 너무 주는 건 별로**다. **같은 반응을 연속컷으로 확인하는 듯한 불필요한 것은 걷어내는 게 맞다.** fable로도 판단해본 다음 수정 진행."

절차 = 외부 AI 전편 리뷰(정리 권고 1·11·24·42화 / 가벼운 정리 23·35·51화) → fable 항목별 판정 14건 → 메인이 "열감 유지·두 번째 반응만 걷기" 기준으로 재판정(채택 10 · 수정 채택 2 · 기각 2).

게이트: 53화 · 영어 대사 487줄 · 의도 밖 원문 손실 0줄 · 편집 후 문장 33줄 전수 확인 · 24화 용비늘 가라앉음 3회 → 2회 · `name_leak_check.py` PASS.

---

## A-1 · 1화 — 목울대→턱 혀 비트에서 도리안 반응 구절을 뺐다

- 출처: 추가(v4) · v6 L171~L173
- 이유: 바로 다음 원문 줄 "당황했다가 짐승 같은 포효"가 같은 접촉에 대한 도리안의 반응이다. 혀 동작은 그대로
- 수정 전:
```
△奥菲莉娅的舌尖从多里安的喉结一路舔到下巴。多里安的喉咙滚了一下，呼吸变粗。
△오필리아의 혀끝이 도리안의 목울대에서 턱까지 훑고 올라간다. 도리안의 목이 한 번 울리고 숨이 거칠어진다.
△Ophelia's tongue DRAGS from Dorian's throat up to his chin. Dorian's throat BOBS once and his breathing turns rough.
```
- 수정 후:
```
△奥菲莉娅的舌尖从多里安的喉结一路舔到下巴。
△오필리아의 혀끝이 도리안의 목울대에서 턱까지 훑고 올라간다.
△Ophelia's tongue DRAGS from Dorian's throat up to his chin.
```

## A-3 · 1화 — 가슴골 혀 비트에서 "손가락을 어깨에 박는다"를 뺐다

- 출처: 추가(v5) · v6 L186~L188
- 이유: 바로 다음 줄 손깍지가 같은 손 반응이다. 혀 동작·숨 끊김은 그대로
- 수정 전:
```
△多里安的舌头顺着奥菲莉娅的胸口中间往下压，一路舔过汗湿的皮肤。奥菲莉娅的呼吸一断，手指抠进多里安的肩膀。
△도리안의 혀가 오필리아의 가슴 사이 골을 누르며 아래로 훑어 내려간다. 땀에 젖은 피부를 그대로 따라간다. 오필리아의 숨이 한 번 끊기고, 오필리아가 손가락을 도리안의 어깨에 박는다.
△Dorian's tongue PRESSES into the hollow between Ophelia's breasts and DRAGS down through the sweat on her skin. Ophelia's breath CATCHES and her fingers DIG into Dorian's shoulder.
```
- 수정 후:
```
△多里安的舌头顺着奥菲莉娅的胸口中间往下压，一路舔过汗湿的皮肤。奥菲莉娅的呼吸一断。
△도리안의 혀가 오필리아의 가슴 사이 골을 누르며 아래로 훑어 내려간다. 땀에 젖은 피부를 그대로 따라간다. 오필리아의 숨이 한 번 끊긴다.
△Dorian's tongue PRESSES into the hollow between Ophelia's breasts and DRAGS down through the sweat on her skin. Ophelia's breath CATCHES.
```

## B-2 · 11화 — 쇄골 혀 비트에서 "손톱이 석주를 긁는다"를 뺐다

- 출처: 추가(v5) · v6 L1423~L1425
- 이유: 두 컷 앞 "등 옷자락을 움켜쥔다"(v6 요청분)와 손 반응이 겹친다. 옷자락 쪽을 살렸다
- 수정 전:
```
△多里安的舌尖抵住奥菲莉娅的肩头，沿着锁骨的骨线慢慢滑到锁骨窝，停在那里。奥菲莉娅的肩膀抖了一下，指甲刮在石柱上。
△도리안의 혀끝이 오필리아의 어깨 끝에 닿는다. 도리안이 쇄골 뼈를 따라 아주 천천히 혀를 밀어, 쇄골 아래 움푹한 곳에서 멈춘다. 오필리아의 어깨가 한 번 떨리고, 오필리아의 손톱이 석주를 긁는다.
△Dorian's tongue tip LANDS at the end of Ophelia's shoulder and SLIDES slow along the line of her collarbone, stopping in the hollow at its base. Ophelia's shoulder JERKS once and her nails SCRAPE the stone pillar.
```
- 수정 후:
```
△多里安的舌尖抵住奥菲莉娅的肩头，沿着锁骨的骨线慢慢滑到锁骨窝，停在那里。奥菲莉娅的肩膀抖了一下。
△도리안의 혀끝이 오필리아의 어깨 끝에 닿는다. 도리안이 쇄골 뼈를 따라 아주 천천히 혀를 밀어, 쇄골 아래 움푹한 곳에서 멈춘다. 오필리아의 어깨가 한 번 떨린다.
△Dorian's tongue tip LANDS at the end of Ophelia's shoulder and SLIDES slow along the line of her collarbone, stopping in the hollow at its base. Ophelia's shoulder JERKS once.
```

## B-1 · 11화 — 귓가 숨결 비트에서 "무릎이 풀려 석주에 기댄다"를 뺐다

- 출처: 추가(v4) · v6 L1431~L1433
- 이유: 원문 "입맞춤에 다리가 풀려 어깨를 붙든다"와 같은 반응이다. 귓가 숨결은 그대로
- 수정 전:
```
△多里安把嘴贴在奥菲莉娅的耳边，热气全喷在她耳廓上。奥菲莉娅的膝盖一软，只能靠着石柱撑住。
△도리안이 오필리아의 귀에 입을 붙인다. 뜨거운 숨이 오필리아의 귓바퀴에 그대로 쏟아진다. 오필리아의 무릎이 풀려 석주에 기대 겨우 버틴다.
△Dorian PRESSES his mouth to Ophelia's ear, his hot breath spilling over it. Ophelia's knees GIVE and she leans on the stone pillar to stay up.
```
- 수정 후:
```
△多里安把嘴贴在奥菲莉娅的耳边，热气全喷在她耳廓上。
△도리안이 오필리아의 귀에 입을 붙인다. 뜨거운 숨이 오필리아의 귓바퀴에 그대로 쏟아진다.
△Dorian PRESSES his mouth to Ophelia's ear, his hot breath spilling over it.
```

## C-1 · 23화 — 마지막 컷의 "눈을 감는다 / 눈을 뜨지 않는다"를 합쳤다

- 출처: 추가(v6) · v6 L2696~L2698
- 이유: 같은 정보가 한 컷 안에서 두 번 나왔다
- 수정 전:
```
△【特写】奥菲莉娅闭上眼，睫毛抖个不停，一直没有睁开。
△【클로즈업】오필리아가 눈을 감는다. 속눈썹이 쉬지 않고 떨린다. 오필리아는 눈을 뜨지 않는다.
△CLOSE-UP — Ophelia's eyes close, her lashes trembling without stop. She doesn't open them.
```
- 수정 후:
```
△【特写】奥菲莉娅一直没有睁眼，睫毛抖个不停。
△【클로즈업】오필리아는 눈을 감은 채 뜨지 않는다. 속눈썹이 쉬지 않고 떨린다.
△CLOSE-UP — Ophelia keeps her eyes shut, her lashes trembling without stop.
```

## D-1 · 24화 — "피부가 맞붙고 숨이 한 박자 멎고 부드러운 신음, 심장이 부딪힌다" 비트를 삭제했다

- 출처: 추가(v4) · v6 L2759~L2761
- 이유: 네 컷 앞 "참던 숨이 새어 나온다"와 같은 반응이고, 심장은 원문 "손바닥을 뛰는 심장 위에"와 겹친다. 부드러운 신음은 뒤 "신음이 부드러웠다 날카로워진다" 비트에 남는다
- 수정 전:
```
△两人的皮肤贴在一起，奥菲莉娅的呼吸停了一拍，随后在多里安的颈窝里发出一声轻软的呻吟。她的胸口能感到他的心跳在撞。
△두 사람의 피부가 맞붙는다. 오필리아의 숨이 한 박자 멎었다가, 도리안의 목덜미에 낮고 부드러운 신음이 새어 나온다. 오필리아의 가슴에 도리안의 심장이 부딪히는 것이 느껴진다.
△Their skin PRESSES together. Ophelia's breath CATCHES for a beat, then a soft moan slips out against Dorian's neck. Ophelia can feel Dorian's heart slamming against her chest.
```
- 수정 후:
```
(삭제)
```

## D-2 · 24화 — 갈비뼈 혀 비트에서 "혀가 지나간 자리마다 용비늘이 물러난다"를 뺐다

- 출처: 추가(v5) · v6 L2778~L2780
- 이유: 같은 화 원문에 용비늘이 가라앉는 장면이 이미 두 번 있다(3회 → 2회). 혀 동작과 도리안 반응은 그대로
- 수정 전:
```
△奥菲莉娅的舌尖抵在多里安的一根肋骨上，顺着骨头一寸一寸往腰侧滑，很慢。舌头走过的地方，龙鳞一片片退下去。多里安的腹肌绷紧，呼吸停了半拍。
△오필리아의 혀끝이 도리안의 갈비뼈 하나에 닿는다. 오필리아가 그 뼈를 따라 아주 천천히 허리 옆까지 혀를 밀고 간다. 혀가 지나간 자리마다 용비늘이 한 장씩 물러난다. 도리안의 배 근육이 조여들고, 도리안의 숨이 반 박자 멎는다.
△Ophelia's tongue tip PRESSES against one of Dorian's ribs and MOVES slow along the bone, all the way to the side of his waist. Wherever her tongue passes, the dragon scales RETREAT one by one. Dorian's stomach muscles LOCK tight and his breath STOPS for half a beat.
```
- 수정 후:
```
△奥菲莉娅的舌尖抵在多里安的一根肋骨上，顺着骨头一寸一寸往腰侧滑，很慢。多里安的腹肌绷紧，呼吸停了半拍。
△오필리아의 혀끝이 도리안의 갈비뼈 하나에 닿는다. 오필리아가 그 뼈를 따라 아주 천천히 허리 옆까지 혀를 밀고 간다. 도리안의 배 근육이 조여들고, 도리안의 숨이 반 박자 멎는다.
△Ophelia's tongue tip PRESSES against one of Dorian's ribs and MOVES slow along the bone, all the way to the side of his waist. Dorian's stomach muscles LOCK tight and his breath STOPS for half a beat.
```

## D-3 · 24화 — 정지 포옹을 한 칸 앞으로 옮기고, 원문 줄은 "땀에 젖은 머리채를 잡아 뒤로 당긴다"만 남겨 뒤로 보냈다

- 출처: 원문 1 + 추가(v4) 1 · v6 L2826~L2831
- 이유: 원래 원문 순서는 "그녀가 머리채를 당겨 떼어낸다 → Now, please me"였는데 v4에서 그 사이에 정지 포옹을 끼워 논리가 깨졌다. 원문 줄의 "상체 밀착·땀방울·두 팔로 목 두르기"는 포옹·앞선 땀 묘사와 겹쳐서 덜었다. 결과 순서 = 키스 → 미소 → 정지 포옹 → 머리채 당겨 떼어냄 → "Now, please me"
- 수정 전:
```
△两人上半身紧紧贴合，汗珠随着身体的律动滑落，奥菲莉娅双臂环绕着多里安的脖颈，一只手抓住他汗湿的头发，迫使他后撤了一些。
△두 사람의 상체가 바싹 붙어 있다. 몸의 움직임을 따라 땀방울이 흘러내린다. 오필리아가 두 팔을 도리안의 목에 두르고, 한 손으로 땀에 젖은 도리안의 머리카락을 잡아 조금 뒤로 물러나게 한다.
△Ophelia's and Dorian's upper bodies PRESS tight together, sweat trickling down with each motion. Ophelia WRAPS both arms around Dorian's neck, one hand GRIPPING Dorian's sweat-soaked hair, pulling Dorian back a little.
△多里安双臂环住奥菲莉娅的后背，用力抱紧，一动不动。两人贴着彼此喘气，谁都没有说话。
△도리안이 두 팔로 오필리아의 등을 감아 힘껏 끌어안고 움직이지 않는다. 두 사람은 서로에게 붙은 채 숨만 몰아쉰다. 아무도 말하지 않는다.
△Dorian's arms WRAP around Ophelia's back and CRUSH her against him, and he holds still. They breathe against each other, neither of them speaking.
```
- 수정 후:
```
△多里安双臂环住奥菲莉娅的后背，用力抱紧，一动不动。两人贴着彼此喘气，谁都没有说话。
△도리안이 두 팔로 오필리아의 등을 감아 힘껏 끌어안고 움직이지 않는다. 두 사람은 서로에게 붙은 채 숨만 몰아쉰다. 아무도 말하지 않는다.
△Dorian's arms WRAP around Ophelia's back and CRUSH her against him, and he holds still. They breathe against each other, neither of them speaking.
△奥菲莉娅一只手抓住多里安汗湿的头发，迫使他后撤了一些。
△오필리아가 한 손으로 땀에 젖은 도리안의 머리카락을 잡아 조금 뒤로 물러나게 한다.
△Ophelia GRIPS Dorian's sweat-soaked hair and pulls him back a little.
```

## F-1 · 35화 — 작별 키스 지문에서 "다시 품으로 끌어안는다·어깨에 기댄다"를 뺐다

- 출처: 원문(v3 Codex) · v6 L3960~L3962
- 이유: 바로 뒤 대사 "조금만 더 안고 있게 해 줘"와 그 뒤 포옹을 먼저 써 버린다. 키스 → 대사 → 포옹으로 포옹이 한 번만 나온다
- 수정 전:
```
△奥菲莉娅深吸一口气，缓缓直起身。她双手捧起多里安的脸，深深吻住他。双唇分开后，她又将他揽进怀里。多里安靠在她的肩上。
△오필리아는 깊이 숨을 들이쉬고 천천히 몸을 일으킨다. 두 손으로 도리안의 얼굴을 감싸 깊게 입을 맞춘다. 입술을 뗀 뒤 그를 다시 품으로 끌어안는다. 도리안은 그녀의 어깨에 기댄다.
△Ophelia draws a deep breath and slowly sits up. She cups Dorian's face in both hands and kisses him deeply. When their lips part, she draws him back into her arms. Dorian leans against her shoulder.
```
- 수정 후:
```
△奥菲莉娅深吸一口气，缓缓直起身。她双手捧起多里安的脸，深深吻住他。
△오필리아는 깊이 숨을 들이쉬고 천천히 몸을 일으킨다. 두 손으로 도리안의 얼굴을 감싸 깊게 입을 맞춘다.
△Ophelia draws a deep breath and slowly sits up. She cups Dorian's face in both hands and kisses him deeply.
```

## E-1 · 42화 — "손바닥이 가슴으로 미끄러지고 심장이 부딪힌다" 비트를 삭제했다

- 출처: 추가(v4) · v6 L4713~L4715
- 이유: 바로 앞 "손목 맥박에 입술"과 맥박 반응이 연속으로 겹친다. 더 센 손목 쪽을 남겼다
- 수정 전:
```
△奥菲莉娅的手掌从多里安的脸滑到他的胸口，掌心下的心跳撞得很重。他的呼吸抖了一下。
△오필리아의 손바닥이 도리안의 얼굴에서 가슴으로 미끄러진다. 손바닥 아래에서 도리안의 심장이 세게 부딪힌다. 도리안의 숨이 한 번 떨린다.
△Ophelia's palm slides from his face down to his chest. Under it, his heart is slamming. His breath shakes.
```
- 수정 후:
```
(삭제)
```

## E-2 · 42화 — 물속 포옹 비트를 "다리로 허리를 감는다"만 남기고 줄였다

- 출처: 추가(v4) · v6 L4743~L4745
- 이유: 앞(그가 가슴에 세게 눌러 안음)과 뒤(몸이 빈틈없이 맞붙음)가 원문 포옹이라, "팔로 목을 조이듯 끌어안는다"가 세 번째 밀착이었다. 다리로 감는 그림은 열감이 있어 살렸다
- 수정 전:
```
△奥菲莉娅的双腿在水下缠上多里安的腰，双臂勒住他的脖子，抱得死紧。水从两人身上淌下去。
△오필리아의 두 다리가 물속에서 도리안의 허리를 감고, 두 팔이 도리안의 목을 조이듯 끌어안는다. 물이 두 사람의 몸을 타고 흘러내린다.
△Under the water, Ophelia's legs wrap around his waist, her arms locking around his neck, holding on as tight as she can. Water RUNS off both of them.
```
- 수정 후:
```
△奥菲莉娅的双腿在水下缠上多里安的腰。
△물속에서 오필리아의 두 다리가 도리안의 허리를 감는다.
△Under the water, Ophelia's legs wrap around his waist.
```

## G-1 · 51화 — "두 손으로 용발을 감싼다"를 빼고 눈물·미소만 남겼다

- 출처: 원문(v3 Codex) · v6 L5733~L5735
- 이유: 두 컷 앞 "두 손을 뻗어 차가운 용비늘 손을 꼭 붙잡는다"와 같은 동작이다. 뒤의 번개가 맞잡은 손을 비추는 컷은 그대로
- 수정 전:
```
△奥菲莉娅双手握住多里安的龙爪，眼泪砸在他的手背上，绽放出一个明媚的笑容。
△오필리아는 두 손으로 도리안의 용발을 감싼다. 눈물이 그의 손등에 떨어지고, 그녀는 환하게 미소 짓는다.
△Ophelia CUPS Dorian's dragon claw in both hands. Tears FALL onto Dorian's hand — and Ophelia BREAKS into a bright smile.
```
- 수정 후:
```
△奥菲莉娅的眼泪砸在多里安的手背上，她绽放出一个明媚的笑容。
△오필리아의 눈물이 그의 손등에 떨어지고, 그녀는 환하게 미소 짓는다.
△Tears FALL onto Dorian's hand — and Ophelia BREAKS into a bright smile.
```

---

## 기각한 것 (그대로 둠)

- **1화 "발가락이 확 오그라들며 시트를 파고든다"** (fable 삭제 권고) — 사용자가 v6에서 직접 요청한 "시트·옷을 꽉 쥐는 모먼트"이고, 발·등·숨은 서로 다른 신호라 같은 반응의 반복이 아니다.
- **42화 "손끝을 입에 물고 혀로 한 번 훑는다"** (fable 삭제 권고) — 경고 대사 *앞*에서 도리안의 쉰 목소리 경고를 끌어내는 원인이고, 원문 "입술 깨물기"는 경고 *뒤*의 대답이라 기능이 다르다. 사용자가 남기라고 한 혀 비트이기도 하다.

## 수정해서 채택한 것

- **24화 원문 줄** — fable은 통째 삭제를 권했다. 메인은 원문의 "머리채를 당겨 떼어낸다 → Now, please me" 논리를 살리려고 해당 구절만 남기고 순서를 바꿨다(D-3).
- **42화 물속 포옹** — fable은 통째 삭제를 권했다. 메인은 "다리로 허리를 감는다"는 그림을 살리고 겹치는 포옹 구절만 뺐다(E-2).
