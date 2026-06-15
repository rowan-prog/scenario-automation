# 영어 vertical 히트작 대사 — 사용자 필사 reference (charge 표준)

> **출처:** 사용자가 직접 필사한 북미 영어권 vertical 히트작 대사 (2026-06-13 세션). 진짜 히트작들에서 일부만 발췌.
> **대소문자·구두점 = 필사 원형 그대로 보존** (사용자가 빠르게 소문자로 옮긴 것 — 다듬지 마라). 화자명은 일부러 거의 안 적혀 있음 — **인물 매핑이 아니라 영어 "톤"을 보라는 것**(사용자 명시: "인물은 지칭 안함 영어 톤을 말하는 거임").
> **핵심 thesis: 모든 라인이 charge(극적 기능)를 가진다. 중립 정보 0.**

---

## ⚠️ 사용법 (먼저 읽어라)

이 필사본은 **표준 그 자체**다. 평가 대상이 아니라 학습 대상.

- ❌ **하지 마라:** 이 대사들을 내 자가 검수 기준(`voice_lint`·"spoken이냐 번역투냐")으로 채점. (사용자 격노 이력: "내 잣대로 따지랬냐, 히트작 대사를 평가하고 배우랬지.")
- `voice_lint`는 **기계 게이트**(한국어 수·Hard Cut 수·중복 카운트)에만 쓴다. **대사 톤 품질 판정엔 쓰지 마라.**
- 우리 영어 대본의 평탄함 = "spoken이냐"의 문제가 아니라 **라인이 극적 일을 안 함(charge 0)**이 진짜 원인.
- 관련 메모리: `feedback_english_vertical_hit_dialogue_tone.md` · `feedback_protagonist_not_villain_voice.md` · `feedback_vertical_name_card_format.md` · `feedback_claude_voice_bias_vertical_failure.md`
- 관련 룰: `config/10_writing_standard.md` §D-0(모든 대사=기능) · §D-6(천박함 보존) · §D-6-1(번역-초월) · §F(모욕 표준).

---

## 0. charge란 무엇인가 — 대사의 "크기"가 아니라 장면 안에서 "끌어당기는 힘"

> 🚨 가장 중요. **charge = 센 대사가 아니다.** 그 줄이 **장면 안에서 힘의 방향을 바꾸는가**이다. 작고 평범한 줄도 charge가 있고, 멋있는 한 방도 charge 0일 수 있다.

**한 줄의 charge = 보통 다음 중 하나(센 말일 필요 없음):**
1. **시선을 꽂는다** — 관객·군중의 관심을 한 지점으로 모음. (`uh... who is she?`)
2. **관계를 드러낸다** — 이름 하나·호칭 하나로 과거 친밀/위계를 터뜨림. (`Jere...`)
3. **지위를 바꾼다** — 누가 위고 누가 아래인지 즉시 보이게 함.
4. **상처를 낸다** — 모욕·오해·배신·성적/계급적 수치심을 직접 누름.
5. **다음 행동을 강제한다** — 명령·협박·질문·거절·폭로가 다음 컷을 밀어냄. (`who let you in here?`)
6. **리듬을 끊는다** — 장면을 멈추거나 전환하거나 새 인물을 들여보냄.
7. **정보를 무기로 바꾼다** — 정보 "전달"이 아니라 "정보가 무기로 쓰이는 순간"을 만듦.

**작은 줄이 큰 일을 하는 예:**
- `Jere...` = 그냥 이름 부르기가 아님. 앞에 군중 조롱 + 남자가 그녀를 알아보는 상황이 깔리면 한 단어가 "나는 너를 안다 / 너에게 빌러 왔다 / 우리 사이 과거가 있다 / 군중 앞에서 너만은 내 말을 들어달라"를 **동시에** 건다. 문장은 작지만 장면 압력은 크다.
- `the next.` = 두 단어. charge = 정보량이 아니라 **압축된 지배감**. "나는 싸우는 중이 아니라 처리 중이다." 긴 승리 선언보다 차갑고 빠르다.
- `uh... who is she?` = 펀치라인이 아님. 관객 질문을 군중 입에 넣고 다음 줄 가십 폭로의 문을 연다.
- `who let you in here?` = 평범한 문장. 폭행 위협 장면에선 제3자 진입 + 권력 충돌 + 구조 가능성 + 다음 액션을 동시에 만든다. 장면의 문이 열리는 줄.

**🚨 반대 함정 — 모든 줄을 "멋있는 한 방"으로 만들지 마라.** 그러면 또 AI식으로 망한다: 다들 서로 명언을 던지고 아무도 실제로 듣거나 반응하지 않는 느낌. 좋은 vertical = 강한 줄 + 그 사이의 **반응줄·인식줄·숨막힘줄·전환줄**. 단, 그 짧은 줄들도 일을 해야 한다(위 7종 중 하나).

**charge 0에 가까운 줄(겉은 멀쩡):** `I came here to explain what happened last year.` — 정보는 있는데 장면 안에 상처·압박·구걸·거절·위험이 없다. → 히트작 감각: `please, jere, just let me explain... just once. please.` 같은 기능("설명 기회를 달라")인데 훨씬 charged — 설명 "요청"이 아니라 **굴욕적 애원**이고 `just once`가 이미 계속 거절당했다는 감각까지 싣는다.

### 0-1. 삭제 테스트 (가장 정확한 판별기)

그 줄을 **빼본다.**

- 빼도 — ①누가 누구를 어떻게 보는지 같고 ②다음 행동 같고 ③감정 온도 같고 ④관객이 아는 정보 같고 ⑤장면 리듬 안 변하면 → **죽은 줄**(아무리 자연스러워도).
- 빼면 — ①다음 폭로가 덜 세지거나 ②인물 사이 과거가 사라지거나 ③군중의 잔인함이 덜 보이거나 ④위협이 추상이 되거나 ⑤컷 전환의 힘이 빠지거나 ⑥주인공의 굴욕/공포/강단이 약해지면 → **살아 있는 줄**(짧고 평범해 보여도).

**한 줄 요약: charge는 대사의 크기가 아니라 장면 안에서 그 줄이 잡아당기는 힘. 센 말이 아니어도 된다. 하지만 빠지면 장면이 그대로면 안 된다.**

> **수술 함의:** flat한 줄을 고친다 = 무조건 더 세게/멋있게가 아니다. (a) 삭제 테스트로 **죽은 줄**이면 → charge를 넣거나(7종 중 하나) 삭제. (b) 이미 **반응/인식/숨막힘/전환** 기능을 하는 줄이면 → **그대로 둔다.** 평범하다고 펀치라인으로 바꾸지 마라(그게 AI식 망함).

---

## 1. 네임카드 (화면 자막) 표준

실제 히트작 자막 예시:

```
Jeremy Whitmore / Bears Captain
Naomi Sinclair / Bears Manager
```

**양식: 풀네임 / 짧은 직함·관계(1-2단어).** chyron처럼 한 눈에 읽힌다.

- 주인공 = 이름만으로 충분(직함 잉여면 생략).
- ❌ 잉여 정보: 주인공에 `bride-to-be` 같은 기계적 설명 (사용자: "씨팔 무슨 정보야. 기계적이잖아").
- ❌ 서술형 역할: `who knows the truth` 같은 문장형 역할 (사용자: "드라마 화면 자막에. 개병신인가").
- 핸드오프의 드라마틱 on-screen title(`MARA / THE FACE THIEF`류)은 **내부 제작메모용**이지 화면 네임카드가 아님.
- 본문 영어 100% 룰 → 네임카드도 영어.

> SHE STOLE MY FACE v54 적용: `[NAME] Lena Sterling`(이름만) · `[NAME] Mara Voss / Lena's Friend` · `Ethan Cross / Lena's Fiancé` · `Noah Keene / Investigator` — 첫 등장 1회만.

---

## 2. 필사 전문 (genre case별 · verbatim)

화자 구분은 ` / `로 줄을 나눈 필사 원형 그대로. 각 case 아래 craft 주석.

### CASE A — 현대물 (스포츠 / 아이비 캠퍼스 복수극)

> 군중이 몰락한 옛 매니저를 알아보는 도입 + 다툼 위로 깔리는 회상 VO.

```
oh my god!
no way... that's the bears!
the state champions!
yeah! all of them got d1 scholarships because of basketball.
uh... who is she?
she looks like a homeless person. this is an ivy campus not a shelter.
wait, i know her. she used to be the bears' manager, samantha reed! i heard she drugged her own team and got thrown out!
Jere...
Sam? what are you doing here? what do you want?
please, jere, just let me explain... just once. please.

[화면자막: one year earlier]
Naomi? what are you doing?!
[VO·속마음, 둘이 다투는 장면 위로 깔림:] before the state qualifiers in senior year, i caught naomi putting stimulants into the team's drinks. i tried to stop her, because i knew she was going to destroy the whole team.
Sam! why would you put something in everyone's drinks?!
Sam?! are you out of your mind?! do you realize this could ruin our record and get the whole team suspended?!
it wasn't me!
```
> (사용자 메모: "이게 엔딩인 건 아님" — 도입부 발췌)

**craft:**
- **군중 리액션이 곧 exposition.** "who is she?" → "i heard she drugged her own team and got thrown out!" = **이름 + 과거 + 몰락 + 군중 경멸**을 한 줄에, **가십으로** 던짐. 설명을 평탄하게 깔지 않고 가십·고발에 실어 던진다.
- **잔인/직설을 그냥 박는다.** "she looks like a homeless person. this is an ivy campus not a shelter." — 부드럽게 안 감싼다.
- **stakes = 형용사가 아니라 구체적 결과.** "this could ruin our record and get the whole team suspended."
- **미스터리는 다음 호흡에 회수.** "who is she?" → 두 줄 안에 "samantha reed... drugged her own team."
- **감정은 raw + 반복.** "please, jere, just let me explain... just once. please." / "it wasn't me!"
- **회상 진입은 화면자막 한 장("one year earlier") + 다툼 위로 깔리는 속마음 VO.** 설명 VO 도배가 아니라 장면이 굴러가는 위에 한 겹.

### CASE B — 판타지물 (소유욕 알파 / 납치 협박)

```
i'm already engaged. jason and i, we love each other.
then call it off. he can't protect you. i can. be my woman, and the world will kneel for you.
you sick bastard. is this just a game to you? kidnap me, ruin my life, and brand me like cattle?
if i wanted to destroy you, angel... you wouldn't even have time to cry. say no... he'll never even get the chance to miss you. your call.
good girl. you'll stay here until the bonding ceremony. now, take off your clothes.
```

**craft:**
- **권력은 구체적 이미지로 선언.** "be my woman, and the world will kneel for you." — 추상 "지켜줄게"가 아니라 **세상이 무릎 꿇는 그림**.
- **위협 = 구체적 결과 + 시간 압축.** "you wouldn't even have time to cry." / "he'll never even get the chance to miss you." — "죽이겠다"를 한 번도 안 쓰고 더 무섭게.
- **여주 저항도 charged·구체.** "kidnap me, ruin my life, and brand me like cattle?" — 가축 낙인 이미지로 굴욕을 명명.
- **마지막에 명령으로 판을 닫는다.** "good girl. ... now, take off your clothes." — 호칭("good girl")으로 지배 + 다음 행동 명령.

### CASE C — 현대물 (폭행 / 위협)

```
somebody... help me, please. somebody help me!
show me a good time.
no! somebody help me!
come on, sweetheart. show me a good time.
who let you in here?
```

**craft:**
- **공포 = raw + 반복, 유려함 0.** "somebody help me!" 그대로 두 번. 문장 다듬으면 죽는다.
- **가해자 대사는 태연·역겹게 짧다.** "show me a good time." / "come on, sweetheart." — 감미로운 호칭 위에 폭력.
- **장면을 끊는 한 줄.** "who let you in here?" — 제3자 진입으로 판 전환.

### CASE D — 여성향 현대판타지 (오메가 / 소유 알파 · 고수위)

```
i hate these scars. every single one... left 'cause of her.
that's ancient history. means nothing now.
you bad, bad boy... that pathetic little omega bitch has zero clue. we're tangled like this right now.
what matters now... is breeding a strong, pure-blood heir. meaning, i'm fucking you, gorgeous.
you promised your brother you'd take care of me. for the future of the bloodline. now. please me.
```

**craft:**
- **과거·상처도 charge로 운반.** "i hate these scars. every single one... left 'cause of her." — 정보(상처·원인 인물)를 증오에 실어.
- **직설 성적 선언을 그냥 박는다.** "meaning, i'm fucking you, gorgeous." — 에두르지 않음. 천박·직설이 곧 톤.
- **관계·판돈을 한 줄에.** "you promised your brother you'd take care of me. for the future of the bloodline." = 형제 약속 + 혈통 의무 + 강제를 동시 운반.
- **명령으로 닫음.** "now. please me." — 짧은 명령. (여성향이어도 톤이 무르지 않음.)

### CASE E — 판타지물 (전투)

```
kill him! seize aurellian!
attack!
you came here to die, and i shall grant your wish.
Rose Knight! prepare to die!
the next.
we will definitely seize aurellian.
```

**craft:**
- **전투 외침 = 짧고 구체적 목표.** "seize aurellian!" — 지명/대상이 박혀 있다("attack!"만으로 안 끝냄).
- **조롱 + 선고를 한 줄에.** "you came here to die, and i shall grant your wish."
- **"the next." 같은 극단 압축.** 무자비함을 두 단어로.

---

## 3. 필사본에서 추출한 craft 규칙 (집필·수술 시 적용)

1. **모든 라인이 charge를 가짐 — 중립 정보 0.** 매 라인에 물어라: 이 줄이 무슨 극적 일을 하나? — 가십 / 도발 / 지위 선언 / 구체 stakes / 감정 타격 / plant(심기) 중 **최소 하나**는 해야 한다. 안 하면 charge를 넣거나 버려라.
2. **exposition을 평탄하게 깔지 마라 — 가십·도발·고발·증오에 실어 던진다.** ("who is she?" → "drugged her own team and got thrown out!")
3. **잔인/직설을 그냥 박는다.** 부드럽게 감싸지 마라. ("homeless person. this is an ivy campus not a shelter." / "brand me like cattle" / "i'm fucking you, gorgeous.")
4. **권력·위협은 추상이 아니라 구체적 이미지·결과로.** ("the world will kneel for you" / "you wouldn't even have time to cry" / "ruin our record and get the whole team suspended.")
5. **감정은 raw + 반복, 유려함 X.** ("somebody help me!" / "it wasn't me!" / "just let me explain... just once. please.")
6. **미스터리는 다음 한두 호흡에 회수.** 끌지 마라.
7. **행복한·정보 전달 셋업조차 charged.** 친절한 셋업 잡담 = 작위적. 행복 셋업도 다크아이러니·plant로 charge를 입힌다.
8. **명령·호칭으로 판을 닫는다(빌런 측).** "good girl. now, take off your clothes." / "now. please me." — 호칭으로 지배, 명령으로 다음 행동.

---

## 4. 적용 체크리스트

집필·수술 시 매 대사 라인에:

- [ ] **삭제 테스트(마스터):** 이 줄을 빼면 장면이 달라지나? 안 달라지면 죽은 줄(§0-1). 단 — 반응/인식/숨막힘/전환 기능을 하면 평범해도 살아 있음·펀치라인으로 바꾸지 마라.
- [ ] 이 라인이 charge가 있나? (시선/관계/지위/상처/다음행동강제/리듬절단/정보무기화 중 1+ — §0)
- [ ] exposition이면 — 평탄한가, 아니면 가십·도발·증오에 실렸나?
- [ ] 잔인/직설 라인을 내가 "세련되게" 무르게 만들지 않았나?
- [ ] 권력·위협이 추상어("destroy you")에 머물지 않고 구체 이미지·결과로 갔나?
- [ ] 감정 라인이 다듬여서 raw함을 잃지 않았나?
- [ ] (주인공) 부·지위를 **자기 입으로** 자랑하지 않나? (그 정보는 조연 입으로 — `feedback_protagonist_not_villain_voice.md`)
- [ ] 천박·뻔뻔·잔인은 **빌런 몫**, 주인공은 kind/innocent + 강단.
