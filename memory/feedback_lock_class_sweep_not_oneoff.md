---
name: lock-class-sweep-not-oneoff
description: "LOCK 검수에서 같은 오류가 자꾸 새로 보이는 이유 = 패치가 시간표를 선명하게 할수록 숨은 모순이 드러나고, 초반 패스가 '패치 반영/큰 구조'만 봐서 저레벨 인간-동선·표현 클래스를 못 훑음. 해법 = 개별이 아니라 *클래스 단위 grep 전수*."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4aaa6296-8e27-427d-9e4e-a2b06585d6ce
---

사용자 제정(2026-06-17 · SHE STOLE MY FACE v63 LOCK 직전). **"왜 같은 류 오류가 자꾸 새로 발견되냐"의 근본 원인 + 해법.**

**🔒🔒 근본 원인 (가장 깊음·2026-06-17 사용자 격파): 이건 "검수 부실"이 아니라 *집필 보이스 문제*다.** 내(모델) 기본 prose 보이스는 문학(metaphor 지문·ledger triad·추상명사)으로 깔린다 — 내 귀엔 "잘 읽힘". paid vertical은 정반대(건조·직역생존)라, **쓸 때마다 문학이 새로 생산된다**(발견 X·생산 O). 게다가 ①패치 한 줄도 같은 보이스라 새 잔재 심음 ②렌즈가 단계마다 날카로워져 직전 통과층이 새로 드러남 ③내가 쓴 걸 *그 편향된 귀*로 판정→과소탐지. **결론: 자가검수로 "문학 0"은 점근적(asymptotic)·도달 불가·self-replenishing.** → 대응: (a) 내 "잘 읽힌다" vertical엔 무효·외부기준(직역테스트·ESL 1패스·독립 belt)만 판정 (b) **꼬리는 쫓지 말고 *자른다* — clear blocker + "명확히 좋아지나?" polish만·나머진 LOCK** (c) 근본예방=*집필 시점*에 건조하게(LOCK이 대수술이면 draft 보이스가 틀린 것). 관련: [[claude-voice-bias-vertical-failure]] [[english-vertical-hit-dialogue-tone]].

**🔒 제1원칙 (2026-06-17): 삭제 > 추가. 오류 막겠다고 설명/소품/정보경로 덧대면 *새 오류 프레임*이 생긴다.** 보강은 "그럼 이것도? 저것도?"를 부른다. 실증: ①`phone, bag, wallet, ID, keys` 뒤에 붙인 `Everything that says Lena Sterling leaves with her`(멋부림) → 삭제 ②열쇠 모순 닫으려 넣은 `Mara walks in with her own copy of the key` → "왜 copy가 있지?" 소품 프레임 → 삭제(문 unlocked면 그냥 들어옴) ③위치인지 닫으려 넣은 `I've got your name, your money, your necklace`(특히 `money`=돈 프레임 재발) → 삭제, `Staff talk` 한 줄만 남김. **판정 순서: (1) 삭제하거나 가만 두면 문제 안 되나? → 그러면 건드리지 마라. (2) 꼭 닫아야 하면 *최소 한 줄 구어*(소품/숫자/절차 단어 없이). 돈/키/전화/문/보안/직원 단어는 *정말 필요할 때만*.**

---


**왜 반복 발견되나:**
1. **패치가 시간표/설정을 선명하게 만들수록 *숨어 있던* 모순이 새로 보인다.** 예: EP7 헤딩을 `Next Day`로 명료화하니 그제서야 "가방·열쇠 다 뺏긴 Lena가 어떻게 제 아파트 문을 여나(`Lena's key still turns`)" 유령 열쇠 모순이 드러남. 시간선이 흐릿할 땐 안 보이던 게 선명해지면 튀어나온다.
2. **초반 검수 패스가 "패치가 제대로 들어갔나 + 큰 구조 안 무너지나"에 과집중**하면, 저레벨 인간-동선(소지품 소지/이동, *누가 그 정보를 어떻게 알았나*, 씬 간 인물 위치)과 표현 품질(문학 지문·관용구·`the [형용사] face` 물건라벨)은 패스가 좁아져 늦게 잡힌다.
3. **클래스 검사를 개별로 하면 변형이 빠져나간다.** `the face` bare grep은 `the stolen face`·`surgically-perfect face`(형용사 낀 변형)를 못 잡아서 또 남았다.

**해법 = LOCK 직전 *클래스 단위 grep 전수*(개별 패치 확인 말고):**
- **A. 로지스틱스 클래스:** ①소지품/접근(phone·bag·wallet·ID·keys·도어록) — 누가 가졌나↔다음 씬에 누가 쓰나 ②정보 획득("어떻게 알았나") — 즉석 결정/비공개 정보를 상대가 어떻게 아나(돈추적/수사 보강 말고 *한 줄 구어*로: "staff talk" 류) ③씬 간 인물 위치/제압 상태(끌려나간 뒤 어디·붙잡힌 채인가).
- **B. 표현 클래스:** ①문학/시적 지문(`taillights swallow`·`wind in her hair`·`like the floor is empty`·`reflection in a wig`) → 물리 동작 ②관용구(`under my skin`·`holding her up`·`glass house keeps me out`) → 직역생존 ③`X-as-object` 라벨 — **형용사 변형까지** grep(`the (stolen/surgically-perfect/...) face/hand/name`) → 인물/possessive로. (`her stolen name, her stolen face` 같은 *possessive 병렬*은 OK·`the stolen face [동사]` 관사 물건화가 문제.)

**원칙:** 전부 **한 줄 교체·새 씬 0**. 숏폼 속도/도파민 안 죽이고 LOCK 톤만 정리. 정보경로 메울 때 절차/경찰/장부 보강 금지([[face-theft-evidence-diet]]) — *악역 한 줄 구어*로.

관련: [[lock-fix-volume-writing-diagnostic]] [[human-first-action-not-explanation]] [[claude-voice-bias-vertical-failure]] [[vertical-dialogue-dirty-fact-not-strong-sentence]] [[bulk-script-verify-strict]]
