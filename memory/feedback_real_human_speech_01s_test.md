---
name: real-human-speech-01s-test
description: "모든 대사·VO에 적용되는 0.1초 perception test. \"모바일 화면으로 보는 시청자가 이 대사를 듣는 0.1초 순간에 진짜 사람이 화내고/절망하고/협박하는 것처럼 느끼는가.\" Vertical drama 필수 lens."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37994db2-a795-4d48-9fe7-5e1a796a2110
---

# Real Human Speech — 0.1초 Test

**룰:** 모든 대사·VO 작성·검토 시, "모바일로 이 영상을 보는 시청자가 이 대사를 듣는 **0.1초 순간**에 '진짜 사람이 화내고/절망하고/협박하는 것'처럼 느끼는가" 를 단일 판단 기준으로 적용한다.

**Why:** 사용자 명시 (2026-05-28·SHE STOLE MY FACE v25 외부 review 모델 정리). Vertical drama = 모바일 짧은 호흡·1-2초 안에 감정 와닿아야 결제·시청유지. "작가가 키보드를 두드리며 머리로 써낸 티 (Written to sound cool)" = 매출 직격타. Claude default voice = 문학적·세련된 톤이라 자동으로 fail 함 — 외부 layer로 강제 필요.

**How to apply:** 매 phase_4 (집필)·phase_5 (검토)·phase_6 (패치)·LOCK 직전 → 모든 대사 줄 단위로 0.1초 test 통과 여부 판단. 3 카테고리 시그니처가 잡히면 즉시 패치.

---

## 3 자동 폐기 카테고리

### ① Therapy-speak / 자기 심리 분석 monologue
**시그니처:**
- "part of me", "some part of me", "the part of you that"
- "what I wanted/needed/felt was X"
- "I realized I had been X-ing myself"
- 위기 상황·감정 폭발 순간에 자기 심리를 논리적·세련되게 분석하는 문장
- 추상 명사 (loss, grief, control, betrayal, validation, identity) in mouth

**왜 fail:** 실제 사람은 위기·분노·절망 순간에 자기 감정을 이렇게 정리된 문장으로 분석해서 말하지 않음. 악당 변명·정신과 상담실·드라마 작가 톤.

**Real human:** 이기적이고 실용적인 진짜 변명. 추상 → 구체 행동.
- ❌ "통제할 수 없는 딸 대신 통제하기 쉬운 사람으로 교체되어 내심 다행이었다."
- ✅ "걔가 너보다 다루기 쉬웠으니까. 굳이 깊게 생각하고 싶지 않았어."

---

### ② Slogan / Tagline / Animation-style aphorism
**시그니처:**
- 평행 구조 ("You X, I Y" / "오늘 X, 내일 Y")
- 미래 예언형 declaration ("From now on", "Tomorrow you will")
- Tri-colon anaphora ("One X. One Y. My Z.")
- 영화 예고편 카피·만화책 대사 같은 운율
- Aphoristic 짧은 선언 — 사투를 막 끝낸 사람 입에서 안 나옴

**왜 fail:** 북미 실사 드라마에서 이런 대사 = "오글거린다" 반응. 영화 trailer copy·만화책 대사지 진짜 구어체 아님. Demon Lord·THE OFFERING 초기본 패배 패턴.

**Real human:** 힘 빼고 날것의 위협. 운율 깨고 정보 + cold 톤만.
- ❌ "너는 공포를 따르게 했지만, 나는 문을 열게 한다."
- ✅ "넌 공포를 썼지. 난 그냥 문을 연 거고."
- ❌ "오늘 넌 내 뒤로 기어갔지만, 내일은 스스로 내 앞에 무릎 꿇을 것이다."
- ✅ "오늘 내 뒤에 숨은 거, 기억해 둬라."

---

### ③ Poetic / Literary 비유
**시그니처:**
- 신체 metaphor (wearing dead X, swallowing Y, breathing Z, took X out of my mouth)
- 건축/구조 metaphor (built a structure, designed a framework, set up an architecture)
- 자연 metaphor in emotional context (storm inside me, drowning in)
- 추상 인과 ("That changed your feet" / "That broke him")

**왜 fail:** 종이 책에서는 멋진 은유지만 배우가 입으로 뱉으면 입에 안 감기고 붕 뜸. 대사가 *script*가 아니라 *prose*처럼 들림.

**Real human:** 문자 그대로 (literal)·행동 시각화.
- ❌ "누군가 내 죽은 엄마를 입고(wearing) 사람들을 매수하고 있어."
- ✅ "누군가 내 죽은 엄마 이름을 팔아서 사람들을 사고 있어."
- ❌ "Mother built a structure for somebody trying this."
- ✅ "Mom set up the trust to protect me."
- ❌ "그게 네 발을 바꾸게 했지."
- ✅ "그게 널 뒷걸음질 치게 한 거지."

---

## 추가 시그니처 (Bonus — 2026-05-28 v25 patches 학습)

### ④ Lawyer-syntax 중첩 가정·이중 부정
**시그니처:** "asked one question someone who knew me would" 같은 nested clause·hypothetical embedded
**왜 fail:** 배우 입에 mouthful·저문해율 시청자 0.1초 안에 못 따라감
**Real human:** flat 문장 + 명확한 주어/동사
- ❌ "None of you asked one question someone who knew me would."
- ✅ "You didn't ask her one question to check if she was me."

### ⑤ Wordy 협박·standoff 문장
**시그니처:** "Tell them to stand down. Or I send this photo to every reporter outside in sixty seconds." — 단위 시간 명시·조건절·다중 절
**왜 fail:** 빠른 호흡 스탠드오프에서 stilted. 진짜 협박은 더 짧고 cold.
**Real human:** 압축 + 명령형 + "Now"
- ❌ "Tell them to stand down. Or I send this photo to every reporter outside in sixty seconds."
- ✅ "Call them off. Or this goes to every reporter outside. Now."

### ⑥ 헤드리스 동사 fragment exposition
**시그니처:** "Assumes…", "Chosen…", "Built…" — 주어 dropped한 verb-headed sentence가 emotional reveal에 등장
**왜 fail:** 로봇·legal brief 톤. 사람 말 X.
**Real human:** 명확한 주어 복귀
- ❌ "Assumes in the first two years of the marriage you'd no longer be a problem. Chosen the method."
- ✅ "She assumed you'd be dead within two years of the wedding. She even picked how."

### ⑦ Clinical·corporate 동사 in personal anger
**시그니처:** "dispose of", "eliminate", "process", "neutralize" 등 corporate/operational verb이 가족·연인 대상으로
**왜 fail:** 진짜 분노·배신 감정 죽임. 거리감 큼.
**Real human:** 일상 동사 ("get rid of", "kill", "lose")
- ❌ "She was going to dispose of me too."
- ✅ "She was going to get rid of me too."

---

## 검수 protocol (모든 작품·LOCK 직전 필수)

1. 모든 대사·VO 줄 단위로 0.1초 test 1회 통과
2. 7 시그니처 grep 자동 sweep:
   - `part of me|some part of me|what I (wanted|needed) was`
   - `^(You |Today |Tomorrow )[^.]+\. (I |I'?ll )` (slogan 평행)
   - `wearing (my|her) (dead|name|face)|swallowed|drowning in|built (a|the) structure`
   - `^(Assumes|Chosen|Built|Picked|Planned|Designed) `
   - `dispose of|eliminate|process|neutralize` (in dialogue context)
   - `in sixty seconds|in [0-9]+ minutes|stand down|cease and desist` (협박 stilted)
   - nested hypothetical ("X someone who Y would")

3. 잡힌 line — keep/patch 판단 3 질문:
   - 이 대사 듣는 0.1초 안에 진짜 사람이 화내는/위협하는/절망하는 게 보이는가?
   - 작가의 머리에서 써낸 *글*인가, 인물 입에서 나온 *말*인가?
   - 배우가 이 줄을 받으면 한 번에 자연스럽게 칠 수 있는가, 입에 안 감기는가?

4. 예외 (villain·specific characterization 의도된 톤):
   - 차갑고 clinical한 빌런 (Eileen·THE OFFERING Vael) → 어느 정도 elevated 톤 허용
   - 단, "0.1초 test" 통과 = villain voice라도 essential. *진짜 villain*이 *진짜로* 차갑게 말하는 것처럼 들려야 함.

---

## 관련 메모리

- [[no-theater-tone]] — 7 차원 (연극톤·시적·대구·티키타카·short 목표·은유·암시)
- [[claude-voice-bias-vertical-failure]] — Claude default = 문학적·자가 평가 신뢰 X
- [[vertical-structure-hit-script-lesson]] — *글*처럼 잘 쓰임 = 셰익스피어 = 박살
- [[vertical-no-metaphor-dodging]] — 은유가 사건 본체 대신하면 금지
- [[revision-meta-principles]] — 수정 메타 원칙
