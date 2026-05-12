# THE OFFERING — Version D / Round 1 페르소나 검토 (EP01-08 전수)

> 8 페르소나 통합 보고서 — 01 인티머시 / 02 AIGC 제작감독 / 03 연속성·논리 / 04 영어 대사 / 05 상업성 / 06 비주얼 락 / 07 장르 쾌감 / 09 여성 시청자
> 검토 강도: 엄격 (default)
> Fresh 독립 검토 — 메인 트랙·B·C 본문 미참조. Version D r0 단일 검토.

## 자동 검출 (02·06 트리거)

| 항목 | 결과 | 판정 |
|---|---|---|
| 한국어 검출 (`\p{IsHangulSyllables}`) | 0건 | ✅ |
| EP 본문 메타 헤더 (`**Function:**`, `**Information:**`, `**Cut:**`, `**Power Stage:**`) | 0건 | ✅ |
| EP 본문 footer (`**Episode Update:**`, `**Series Update:**`) | 0건 | ✅ |
| Hard Cut 카운트 | 8 (각 EP 1) | ✅ |
| 4 블록 [Visual]/[Camera]/[DIALOGUE]/[FX] 일관 | EP1=20·EP2-7=16·EP8=20 (V=C=D=F 일치) | ✅ |
| 씬 수 분포 | EP1=5 / EP2-7=4 / EP8=5 = 34씬 (표준 1-6 범위) | ✅ |

---

## 01 인티머시 검토

### 의심 지점 사전 스캔
1. EP1 S#3 — 첫 접촉이 "비늘 손이 손목 안쪽 잡아 들어올림 + 맥박" 정도. 다크 로맨타지 첫 만남으로 sensual 강도 충분한가?
2. EP3 S#3 — 침실 벽 키스의 sensual 비트 ("드레스 어깨 끈 풀림 / 잇자국 / 손목 빛 위 입맞춤") — 청사진 EP3 락의 모든 비트 충족하나, 묘사 응축이 짧음.
3. EP5 S#3 — 둘째 잇자국이 첫째 자국 "바로 아래"에 stacked. Version 차별화 의도. 정합?
4. EP6 S#3 — 손등 입맞춤 → 손목 빛 따라감 → 머리채 sheath-slide 흐름이 한 씬에 3 비트. 응축 vs 흩어짐 균형?
5. EP8 S#3 — "altered overnight" 의상 변형. 비주얼 락 v5의 Vael's Choice 변형 2 디테일 내 변경인지 새 변형인지 모호.

### 발견
**🟢 1. EP3 S#3 시야 비트 응축**
- 위치: EP3 / S#3 / [Visual]
- 원문 FIND: `"His **scaled fingers find her jaw**, lift it. He looks at her throat where the assassin's blade would have gone. There is no cut, but a thin red line has bloomed under the skin in the fear."`
- 판정: 자객 위협 직후 fear의 신체 흔적(thin red line)으로 키스 전 sensual tension 응축. 의도 작동.
- 수정 X.

**🟢 2. EP5 S#3 stacked cuff 변주**
- 위치: EP5 / S#3 / [Visual]
- 원문 FIND: `"a **second crescent, smaller, deliberately placed just under the first, the two crescents stacking like a cuff of red marks** on the same side"`
- 판정: 같은 쪽 누적 = possessive 마킹의 시각 표지. 의도 작동.
- 수정 X.

### 검토했으나 유지
1. EP1 S#3 의심: 첫 접촉이 약하지 않나? — 검증 결과: 청사진 EP1 락 ("비늘 손이 손목 안쪽 잡아 들어올림 / 비늘 손가락이 손목 안쪽 맥박") 정확 구현. 첫 화의 sensual 비트는 누적 시작점이므로 강도 점층의 1차 트리거로 충족.
2. EP6 S#3 의심: 한 씬에 3 비트 — 검증 결과: ECU·MACRO·INSERT 매크로 카메라 12 shot 분할로 비트가 흩어지지 않음. 응축 작동.

### Verdict
- 4단계: **조건부 통과** (🟢만)
- LOCK / PATCH THEN LOCK / HOLD: **LOCK**

---

## 02 AIGC 제작감독 검토

### 의심 지점 사전 스캔
1. EP1 S#1 ISOLDE 첫 등장 의상 묘사 — Royal Arrival (비주얼 락 변형 1) 정합?
2. EP2 S#1 의상 변경 트리거 — Vael's Choice (변형 2) 변경 트리거 정합?
3. EP2 S#3 reveal 의상 통합 묘사 — 비주얼 락 변형 2 매핑?
4. EP8 S#3 "altered overnight" 의상 변경 — 락 등재된 변형인가 vs 새 sub-variant?
5. 4 블록 (Visual·Camera·DIALOGUE·FX) 모든 씬 완비?
6. 헤더 양식 일관 (`S#N — LOCATION / SUB / TIME`)?
7. Hard Cut 모든 EP 마지막 표기?

### 발견
**🟡 1. EP8 S#3 의상 sub-variant 비주얼 락 미등재**
- 위치: EP8 / S#3 / [Visual]
- 원문 FIND: `"**Vael's Choice silk — but altered overnight: the black silk gown now has fine silver-and-pearl trim down the shoulder seams, the silver chain at the collarbones replaced with a wider band of pearl and silver, hair half-pinned with pearl at the crown**"`
- 문제: 사절단 앞 공개 reveal 자리에서 의상 변경 발생. 청사진 룩 변형 (Vael's Choice EP1-12) 내 디테일이지만 "altered overnight"이라는 명시적 변경이 비주얼 락 v5에 sub-variant로 등재 X. EP8 페이월 = 공개 reveal 씬 = 통합 묘사 + 락 등재 필요.
- 원인 판정: 비주얼 락 환류 누락 (집필 중 도입된 sub-variant 등재 X).
- 수정 방향 (필터 1·정합성): 비주얼 락 v5 → v6 환류 — "Vael's Choice EP8 sub-variant (Public Mate Display)" 신규 sub-section 등재. EP8 본문 [Visual]에서 묘사 그대로 유지.

### 검토했으나 유지
1. EP2 S#3 reveal 의상 통합 묘사 의심: 변형 2 트리거 ("EP1 후반 베일이 도착 의상 거부·새 의상 지시·reveal scene")가 EP2 S#3에서 발생 = 변형 2 트리거가 청사진은 "EP1 후반"이지만 본문에서 EP2 S#3에 등재 — 검증 결과: 청사진 12-7 비주얼 캐논 "검은 비단 신부 의상 EP15+ 정식 신부 시각 표지"는 분리. Vael's Choice 변형 2는 EP1 후반 ~ EP12 범위 — EP2 S#3은 그 범위 안. EP1 후반 vs EP2 S#3 차이는 청사진 자체의 의상 트리거 표현 모호함이고 비주얼 락 v2 정정에서 "EP1 후반 ~ EP12"로 범위 확장됨. EP2 S#3 등재 OK.
2. 모든 EP의 Hard Cut 표기 일관 — 검증 결과: 8/8 모두 마지막 씬 End Image + Hard Cut. 정합 OK.

### Verdict
- 4단계: **패치 필수** (1🟡)
- LOCK / PATCH THEN LOCK / HOLD: **PATCH THEN LOCK**

---

## 03 연속성·논리 검토

### 의심 지점 사전 스캔
1. EP1 S#2 어머니 인장 + 룬 매치 — pendant가 EP1 이후 어디로? 회수 인과 누락?
2. EP3 S#1-2 assassin 사체 처리 — KIRAN "Take them. / Alive? / One." — 한 명만 살리고 한 명은 죽은 채. EP4 회수?
3. EP3 S#3 드레스 어깨 끈 풀림 — EP4 등장 시 끈 상태? 복구·교체?
4. EP4 S#2 standard 태움 — 두 번째 standard(EP8)와 구분? linen·sigil 일관?
5. EP4 S#4 → EP5 S#1 시간 점프 — 인과 명확?
6. EP5 S#4 iron rail "faint print of light" 잔존 — EP6+ 회수? 아니면 단일 비트?
7. EP6 S#4 HALDREN envoy 체인 "unhooked at the link" — EP4와 EP6 사이 변화 인과?
8. EP6 S#4 → EP7 S#1 시간 점프 — 인과?
9. EP7 S#4 → EP8 S#1 시간 — 드래곤 무리 그림자 등장 후 EP8 페이월까지 시간 흐름?
10. EP8 S#3 의상 "altered overnight" — 누가 만들었나·언제·재료?

### 발견
**🟡 1. EP1 어머니 인장 EP2+ 미회수**
- 위치: EP1 / S#2 / [Visual]
- 원문 FIND: `"A silver chain slips loose from the inner lining of the collar — **her mother's old signet pendant**, a faded sigil engraved on its face. It catches the last gate-light for one breath."`
- 문제: EP1에서 audience-only로 첫 등장 + 룬과 박자 매치. 그러나 EP2-8 본문에 pendant의 위치·상태 회수 0건. 의상이 EP2 S#1에서 Vael's Choice로 갈아입혀짐 — pendant도 함께 옮겨졌는가, 회수됐는가, 누가 보관하나? 청사진 12-3 ISOLDE 캐논 "어머니 목걸이 (Hidden Identity 단서)" Hard Lock — Hidden Identity Reveal Arc 5에서 핵심 단서. EP1-8 동안 위치 불명 = 연속성 공백.
- 원인 판정: 비주얼 락 갱신 + EP2 의상 reveal 씬에 pendant 처리 명시 누락.
- 수정 방향 (필터 1·정합성): EP2 S#1 [Visual]에 한 줄 추가 — pendant가 새 의상 안쪽 라이닝으로 옮겨지는 비트 (또는 ISOLDE가 직접 옮기는 비트). 단일 줄 패치.

**🟢 2. EP3 드레스 어깨 끈 풀림 EP4 복구 인과 모호**
- 위치: EP3 / S#4 [Visual] + EP4 / S#1 [Visual]
- 원문 FIND (EP3 S#4): `"He does not put the strap back."` / `"The strap is still off her shoulder."`
- 원문 FIND (EP4 S#1): `"ISOLDE stands one pace behind his right shoulder, in Vael's Choice silk."` (의상 복구 후·끈 상태 미언급)
- 판정: EP3 끝에서 끈은 풀린 채. EP4 S#1에서 ISOLDE가 회의 자리에 있을 때는 묵시적으로 복구됨 (의상 일관). 명시적 처리는 없으나 EP3→EP4 사이 야간 시간 = 자체 복구 가능. 비주얼 락 v5에 "EP3 단일 reveal / 한 회차만 / 이후 회차 복구"로 등재됨 — 정합 OK.
- 수정 X (락에 등재된 룰 정합).

### 검토했으나 유지
1. EP3 assassins 처리 의심: 한 명만 alive로 / 다른 한 명 사체 — EP4 회수 없음 = 누락? — 검증 결과: EP3 S#2 KIRAN "Take them. / Alive?" → VAEL "One." 명시. 한 명은 죽은 채. ISOLDE 라인 "Send the body home." = 인간 왕국에 사체 회신 명시. EP4 S#1 인간 왕국 envoy 도착에 사체 회신 결과 함축 (HALDREN의 envoy 체인 reaction). 인과 충족. 명시 묘사 부족하나 정보 운반 OK.
2. EP5 S#4 iron rail "print of light" 잔존 — EP6+ 회수 X = 단일 비트로 작동 가능. ISOLDE 자체의 wrist-glow 누적 표지가 본 plot 라인, rail은 부수 비트. 의심하되 유지.
3. EP6 S#4 HALDREN envoy 체인 "unhooked at the link" — EP4 envoy 행 끝 직후 HALDREN의 충성 전환 표지가 EP6에서 발생. EP4 S#4 라인 "He'll send another envoy. / Let him."에 HALDREN의 위치 변화가 인과적으로 시작됨 (EP6에 도착). 인과 충족.

### Verdict
- 4단계: **패치 필수** (1🟡)
- LOCK / PATCH THEN LOCK / HOLD: **PATCH THEN LOCK**

---

## 04 영어 대사·보이스 검토

### 의심 지점 사전 스캔
1. EP1 첫 라인 ISOLDE "I'll walk." / CLERK "They are watching." / ISOLDE "Then let them." — 첫 등장 톤이 너무 짧은가? 캐릭터 voice 즉시 형성?
2. EP2 S#3 ISOLDE "That's not a question." / VAEL "No." — 자연 영어 (네이티브 cadence)?
3. EP3 S#4 ISOLDE "Why stop." / VAEL "Not the way it ends." — declarative compact. 베일의 voice (compact possessive) 일관?
4. EP4 S#4 VAEL "They will not call you that again." — 청사진 EP4 절단 라인 정확 구현. 자연 cadence?
5. EP5 S#3 VAEL "Not yet your mouth." / "Where your pulse is." — 자연스러운가? 너무 시적이지 않나?
6. EP6 S#3 VAEL "Mine." 반복 — 청사진 캐논 일관 / 너무 짧은가?
7. EP7 S#3 ISOLDE "Tell my father the seat is taken." — declarative possessive. 일관?
8. EP8 S#5 NEW ENVOY "I — I cannot —" / ISOLDE "He will." — 페이월 마지막 라인. 자연 cadence?

### 발견
**🟢 1. EP5 S#3 VAEL "Not yet your mouth."**
- 위치: EP5 / S#3 / [DIALOGUE]
- 원문 FIND: `"VAEL: Not yet your mouth."`
- 판정: 짧고 강한 declarative. 영어 syntax상 "Not yet your mouth" = "Not [going to take] your mouth yet" 축약. 다크 로맨타지 alpha possessive에 어울리는 cadence — 시적이나 자연스럽다. 비교: ACOTAR Rhysand voice의 compact declarative. 작동.
- 수정 X.

**🟢 2. EP6 S#3 VAEL "Mine."**
- 위치: EP6 / S#3 / [DIALOGUE]
- 원문 FIND: `"VAEL: (in the hall's hearing) Mine. / ISOLDE: Say it again. / VAEL: Mine."`
- 판정: 청사진 12-3 VAEL 캐논 "달콤한 말 X / 행동·보호·공개 선언으로 의사 전달" 일관. 단음절 declarative possessive 반복 = 다크 로맨타지 검증 cadence. 자연스럽다.
- 수정 X.

### 검토했으나 유지
1. EP1 첫 라인 "I'll walk." 의심: 첫 등장 라인이 너무 짧지 않나? — 검증 결과: 청사진 12-3 ISOLDE 캐논 "매달림·울음·자기 연민 X / 성문 앞에서도 애원하지 않음". 첫 라인이 contraction "I'll walk." = compact spoken cadence. 다음 라인 "Then let them." = 능동 declarative. 캐논 + 영어 자연성 둘 다 충족.
2. EP4 S#4 VAEL "They will not call you that again." — 짧지 않고 풀어쓴 라인. 청사진 캐논의 "선언으로 의사 전달" 정확 구현. 7 단어 = LOCKED OUT 표준 (3-10 단어) 안.
3. EP3 S#3 VAEL "Look at me." / "Mine to keep." — 베일 voice 일관 + ACOTAR alpha 톤 정합. OK.

### Verdict
- 4단계: **조건부 통과** (🟢만)
- LOCK / PATCH THEN LOCK / HOLD: **LOCK**

---

## 05 상업성·마케팅 검토

### 의심 지점 사전 스캔
1. EP1 페이드 직전 face reveal 정지 — 1화 후킹 충분?
2. EP3 S#4 키스 끊김 — 회차 후킹 작동?
3. EP4 S#2 standard 태움 — 광고 컷 후보로 충분?
4. EP5 S#4 베일이 어둠 속으로 — 결제 동력 약화 아닌가? 시청자 frustration 적정?
5. EP6 S#3 공개 마킹 — 광고 컷 후보?
6. EP8 페이월 5씬 응축 — 결제 격차 최대?
7. EP8 마지막 컷 "She is —" 끊김 + 이솔데 자발 마킹 — 다음 화 견인 충분?
8. 페이월 milestone 유예 (공개 키스·신부 선언 완성·첫 밤·옷 안 직접) 보존?

### 발견
**🟢 1. EP1 face reveal 정지 후킹**
- 위치: EP1 / S#5 / End Image
- 원문 FIND: `"End Image: VAEL turned toward ISOLDE, jaw catching fire-light, face still in shadow. Her inner wrist glows once. His scaled hand glows once. Same beat."`
- 판정: 다크 로맨타지 검증작 EP1 후킹 = 남주 얼굴 reveal 직전 정지 + 운명 짝 신호. 페이드 vertical 표준 후킹. 작동.
- 수정 X.

**🟢 2. EP4 standard 태움 광고 컷**
- 위치: EP4 / S#2 / [Visual]
- 원문 FIND: `"He opens his **left palm flat over the standard** — and the **dark-red flame** blooms again, dropping in a slow curtain from his palm to the linen. The standard catches in a single low whoosh. The silver-crown sigil chars first"`
- 판정: 광고 컷 후보 1번 — 검붉은 화염·왕국 sigil 타는 시각. 페이드 vertical 광고 컷 표준. 작동.
- 수정 X.

**🟢 3. EP8 페이월 결제 격차**
- 위치: EP8 / S#3-5 / 페이월 응축
- 원문 FIND (S#4): `"VAEL: She is — (roar) / ISOLDE: (after she lifts her mouth) Yours."`
- 판정: 신부 선언 미완성 ("She is —" / 드래곤 포효에 끊김) + 이솔데 자발 마킹 (그의 손등 비늘을 자기 입술에) + 사절단 12명 무릎 + 새 envoy의 iron staff fallen. 페이월 milestone 유예 (공개 키스 완성·신부 선언 완성·첫 밤) 보존. 결제 격차 최대화. 작동.
- 수정 X.

### 검토했으나 유지
1. EP5 S#4 베일이 어둠 속으로 — 결제 동력 약화? — 검증 결과: VAEL의 거리감(EP3 S#4와 동일 패턴)이 ISOLDE의 wrist-glow rail 잔존 + ISOLDE의 능동 응답으로 보상 격차 유지. 다음 화 견인 = "VAEL의 비밀". 정합 OK.
2. EP6 S#3 공개 마킹 광고 컷 의심: 시각 강도 — 검증 결과: 머리채 sheath-slide + 손목 빛 입맞춤 + dais lamps 어두워짐 = 광고 컷 후보 2번. 작동.

### Verdict
- 4단계: **조건부 통과** (🟢만)
- LOCK / PATCH THEN LOCK / HOLD: **LOCK**

---

## 06 비주얼 어필·캐릭터 락 검토

### 의심 지점 사전 스캔
1. EP1 ISOLDE 첫 등장 묘사 — Royal Arrival (변형 1) 정합?
2. EP1 VAEL 첫 등장 (얼굴 X / 손등만) — 비주얼 락 일관?
3. EP2 ISOLDE 의상 변경 — Vael's Choice (변형 2) 정합?
4. EP2 VAEL 첫 face reveal 묘사 — 비주얼 락 일관?
5. EP1 S#1 escort 12명 + clerk 비락 묘사 — 짧고 명료 룰?
6. EP3 assassins 비락 묘사 — 짧고 명료?
7. EP4 HALDREN 첫 통합 묘사 — 비주얼 락 변형 1 정합?
8. EP6 HALDREN 변형 2 변경 (envoy 체인 unhooked) — 비주얼 락 v5 정합?
9. EP7 new envoy 비락 묘사?
10. EP8 ISOLDE "altered overnight" sub-variant — 비주얼 락 미등재?

### 발견
**🟡 1. EP8 S#3 ISOLDE sub-variant 비주얼 락 미등재** (02 페르소나와 중복 — 정합성 영역 겹침)
- 위치: EP8 / S#3 / [Visual]
- 원문 FIND: `"Vael's Choice silk — but altered overnight: the black silk gown now has fine silver-and-pearl trim down the shoulder seams, the silver chain at the collarbones replaced with a wider band of pearl and silver, hair half-pinned with pearl at the crown"`
- 문제: 비주얼 락 v5 변형 2 (Vael's Choice EP1-EP12) 어셋 base와 다른 sub-variant. 페이월 reveal 씬 = 통합 묘사 + 비주얼 락 등재 필요. 어셋 일관성 위해.
- 원인 판정: 비주얼 락 환류 누락.
- 수정 방향 (필터 1·정합성): 비주얼 락 v5 → v6 환류 — Vael's Choice 변형 2에 "EP8 Public Mate Display sub-variant" 추가 (색·디테일 명시).

**🟢 2. EP4 HALDREN 첫 통합 묘사**
- 위치: EP4 / S#1 / [Visual]
- 원문 FIND: `"**HALDREN — grey-haired, hard cheekbones, the human-kingdom envoy coat in slate wool with the silver crown sigil at the breast, the envoy's chain at the collar**"`
- 판정: 조연급 (락 등재) 첫 통합 묘사 + 비주얼 락 변형 1 정합. 작동.
- 수정 X.

**🟢 3. EP6 HALDREN 변형 2 변화**
- 위치: EP6 / S#4 / [Visual]
- 원문 FIND: `"**HALDREN** enters — alone this time, no escort, the envoy chain still at his collar but **unhooked at the link**, hanging open."`
- 판정: 비주얼 락 v5 HALDREN 변형 2 (EP6+ "왕국 인장 제거 → 베일 측 충성 표지") 부분 구현 — 인장 제거는 EP6에서 시작 (체인 unhooked 단계) → EP6 후반 drake-feather 첨가 (EP8 S#1 "drake-feather pinned" 등장). 단계 진행 정합. 작동.
- 수정 X.

### 검토했으나 유지
1. EP1 S#1 escort 12명 + clerk 비락 묘사 의심: 너무 간략? — 검증 결과: `"Twelve human-kingdom guards in grey livery"` + `"A clerk in a grey wool coat"` = 짧고 명료 룰 (1줄·5-10단어) 정확. 비락 묘사 룰 충족.
2. EP3 S#1 assassins 비락 묘사: `"**Two assassins — black hoods, faces wrapped in grey cloth, narrow killing blades drawn**"` = 짧고 명료 룰 충족.
3. EP7 S#1 new envoy 비락 묘사: `"**The new envoy — middle-aged, severe, the human-kingdom diplomat's heavy black cloak with double-silver-crown sigil at the breast, an iron staff in his right hand**"` = 짧고 명료 (한 줄) 충족.

### Verdict
- 4단계: **패치 필수** (1🟡 — 02·06 공유)
- LOCK / PATCH THEN LOCK / HOLD: **PATCH THEN LOCK**

---

## 07 장르 쾌감·캐릭터 매력 검토

### 의심 지점 사전 스캔
1. EP1 ISOLDE 능동 시작 — 다크 로맨타지 능동적 여주 핵심 충족?
2. EP3 키스 끊김 — alpha possessive + restraint = 다크 로맨타지 cadence?
3. EP5 베일이 어둠 속으로 — alpha 거리감 = 다크 로맨타지 욕망 강화?
4. EP6 자발 옆자리 — Bond 자발 인식 (다크 로맨타지 4번 사이클) 작동?
5. EP7 무릎 위 자세 — 공개 possessive 표지 강도?
6. EP8 페이월 — 다크 로맨타지 6 사이클 응축 (Fated → Forbidden → Possessive → Bond Deepens → Public Recognition 시작)?
7. ISOLDE 매달림·울음·자기 연민 비트 검출?
8. VAEL의 약함 발화 ("사실 나도 두려워") 검출?

### 발견
**🟢 1. EP1 ISOLDE 능동 시작**
- 위치: EP1 / S#1 / [Visual]
- 원문 FIND: `"A guard reaches inside the wagon for ISOLDE's wrist [...] twists her wrist out of his grip without looking at him. She steps down on her own."`
- 판정: 능동적 여주 핵심 (다크 로맨타지 검증작 ACOTAR·Fourth Wing 표준). 첫 컷부터 능동 = Version D 차별화 핵심. 작동.
- 수정 X.

**🟢 2. EP8 페이월 다크 로맨타지 6 사이클 응축**
- 위치: EP8 / S#3-S#5
- 원문 FIND (S#4): `"ISOLDE: (after she lifts her mouth) Yours."`
- 판정: 청사진 12-2 다크 로맨타지 매핑 5번 (Forbidden Touch + Erotic Permission) + 6번 (Public Recognition of Bond) 모두 EP8 페이월에 응축. ISOLDE의 자발 마킹 + "Yours." 한 단어 = 운명 짝 능동 응답. 다크 로맨타지 cadence 작동.
- 수정 X.

### 검토했으나 유지
1. EP5 베일이 어둠 속으로 의심: alpha 거리감 → ISOLDE를 약하게 만드나? — 검증 결과: EP5 S#4 라인 `"ISOLDE: (to herself) Two now. / VAEL (O.S., from shadow): Two now."` = 거리에서도 운명 짝 동조 표지. ISOLDE의 wrist-glow가 rail에 print 잔존 = 능동 표지 누적. 약화 X.
2. ISOLDE 매달림·울음·자기 연민 검출: EP1-8 전수 — 0건. 청사진 12-3 캐논 "절대 하면 안 되는 행동" 위반 X.
3. VAEL 약함 발화 검출: EP1-8 전수 — 0건. 청사진 12-3 캐논 "절대 하면 안 되는 행동" 위반 X.

### Verdict
- 4단계: **조건부 통과** (🟢만)
- LOCK / PATCH THEN LOCK / HOLD: **LOCK**

---

## 09 여성 시청자 진단 (활성화 — 작품 = 여성향)

> **Sub-persona 분리:** 09A 제너럴 30% / 09B 다크 로맨타지 니치 70% (작품 카테고리 = 다크 로맨타지). 두 sub-persona 모두 진단 참여 + 가중 종합.

### 시청 진단 한 줄
다음 화를 누르고 싶은가? **09A 약함 / 09B Y / 종합 가중 Y** — 다크 로맨타지 운명 짝 사이클·alpha possessive 작동. 제너럴 시청자에게는 비주얼 응축·여주 매력이 다소 응축됨.

### 장면별 시청 반응 (요약)

| EP / S# | 09A 제너럴 (30%) | 09B 다크 로맨타지 니치 (70%) | 종합 |
|---|---|---|---|
| EP1 S#1-2 능동 시작·인장 | 🟡 약함 (능동 시작 OK / 신화 단서가 빠름) | ✅ 작동 (운명 짝 첫 신호 즉시) | ✅ 작동 |
| EP1 S#3 비늘 손 손목 안쪽 | 🟡 약함 (sensual 강도 응축) | ✅ 작동 (mate-check beat) | ✅ 작동 |
| EP1 S#5 face reveal 정지 | ✅ 작동 | ✅ 작동 | ✅ 작동 |
| EP2 S#3 옆자리 + 머리채 첫 접촉 | ✅ 작동 | ✅ 작동 | ✅ 작동 |
| EP3 S#3 침실 벽 키스 | 🟡 약함 (sensual 응축이 짧음) | ✅ 작동 (alpha possessive + 잇자국) | ✅ 작동 |
| EP3 S#4 키스 끊김 | ✅ 작동 (frustration 결제 동력) | ✅ 작동 | ✅ 작동 |
| EP4 S#2 standard 태움 | ✅ 작동 | ✅ 작동 | ✅ 작동 |
| EP4 S#3 회랑 화염 손 | ✅ 작동 | ✅ 작동 | ✅ 작동 |
| EP5 S#3 테라스 입술 직전 → 귓불·목·맥박 | 🟡 약함 (입술 미완성 frustration 누적이 좀 길음) | ✅ 작동 (stacked cuff + alpha tension) | ✅ 작동 |
| EP6 S#3 공개 마킹 | ✅ 작동 | ✅ 작동 (다크 로맨타지 ritualistic) | ✅ 작동 |
| EP6 S#4 HALDREN 인정 | ✅ 작동 (공개 지위 회복 부수 비트) | ✅ 작동 | ✅ 작동 |
| EP7 S#2 무릎 위 자세 | ✅ 작동 (alpha possessive 시각) | ✅ 작동 | ✅ 작동 |
| EP7 S#4 드래곤 무리 첫 그림자 | ✅ 작동 | ✅ 작동 (mythic awe) | ✅ 작동 |
| EP8 페이월 5씬 | ✅ 작동 (다음 화 결제 즉시) | ✅ 작동 (모든 사이클 응축) | ✅ 작동 |

### 진단 항목별

| 항목 | 09A | 09B | 종합 |
|---|---|---|---|
| 1. 다음 화 누르고 싶은가 | 🟡 약함 | Y | Y |
| 2. 다크 로맨타지 6 사이클 작동 | 🟡 약함 | ✅ | ✅ |
| 3. 알파 possessive 매혹 | ✅ | ✅ | ✅ |
| 4. 능동적 여주 매력 | ✅ | ✅ | ✅ |
| 5. 공개 지위 회복 (부수) | ✅ | ✅ | ✅ |
| 6. 운명 짝 신호 누적 | ✅ | ✅ | ✅ |

### 의심 지점 사전 스캔
1. ISOLDE의 신체 매력 카메라 — 비주얼 매혹 충족?
2. VAEL의 매혹 카메라 — 다크 alpha 매혹 충족?
3. 친밀 비트 응축 — 다크 로맨타지 검증작 ACOTAR·Demon Lord 톤과 비교 시 적정?
4. 페이월 격차 — 결제 동기 작동?
5. ISOLDE의 매달림·약화 — 0건?

### 이탈 코드 (🟡/🔴 발견 시 표기)
없음 — 모든 항목 ✅ 또는 🟡 (수정 의무 아님).

### 검토했으나 유지
1. 09A 친밀 응축이 짧음 — F-J (alpha possessive 약함)으로 분류 가능? — 검증 결과: 09B (니치 70%) 시점에서는 응축이 다크 로맨타지 ritualistic 톤과 정합. 09A 가중 30%에서만 약함 — 종합 가중 ✅ 작동 유지.
2. EP5 베일 어둠 속 — F-E (남주 변질·약함)? — 검증 결과: 09B 시점에서 alpha 거리감 = possessive frustration 강화 사이클. 운명 짝 신호 잔존. F-E 비매칭.

### 진단 종합

다음 화 시청 동기 작동. 다크 로맨타지 운명 짝 6 사이클이 EP1-8 동안 단계적으로 누적되며 EP8 페이월에서 사이클 5 (Public Recognition of Bond) 시작 + 사이클 6 (Mate Sealed) 유예. ISOLDE의 능동 응답이 매 EP에 누적되어 다크 로맨타지 검증작 ACOTAR·Fourth Wing 톤 정합. 09A 제너럴 시청자에게는 친밀 비트가 다소 응축되어 약함으로 분류되나 09B 니치 가중 70% 종합 시 ✅.

### 재판정 요청 (시청자 페르소나 단독 통과 불가)
모든 EP "✅ 작동" 판정 → 05 (Commerciality) + 07 (Genre Pleasure) + 04 (Dialogue Voice) 중 최소 2명 재판정 필요. 본 보고서에서 05·07·04 모두 LOCK 판정 → 시청자 작동 판정 정합 확인.

---

## 전체 종합

### Verdict 합계

| 페르소나 | Verdict | Lock 판정 | 발견 |
|---|---|---|---|
| 01 인티머시 | 조건부 통과 | LOCK | 0🔴 / 0🟡 / 2🟢 |
| 02 AIGC 제작감독 | 패치 필수 | PATCH THEN LOCK | 0🔴 / **1🟡** / 0🟢 |
| 03 연속성·논리 | 패치 필수 | PATCH THEN LOCK | 0🔴 / **1🟡** / 1🟢 |
| 04 영어 대사·보이스 | 조건부 통과 | LOCK | 0🔴 / 0🟡 / 2🟢 |
| 05 상업성·마케팅 | 조건부 통과 | LOCK | 0🔴 / 0🟡 / 3🟢 |
| 06 비주얼 어필·캐릭터 락 | 패치 필수 | PATCH THEN LOCK | 0🔴 / **1🟡** (02와 공유) / 2🟢 |
| 07 장르 쾌감·캐릭터 매력 | 조건부 통과 | LOCK | 0🔴 / 0🟡 / 2🟢 |
| 09 여성 시청자 | ✅ 작동 (종합) | (시청자 진단 — 처방 X) | 모든 EP ✅ |

### 🟡 unique 발견 = 2건 (02·06 공유로 실질 1건 + 03 1건)

1. **EP8 S#3 ISOLDE sub-variant 비주얼 락 미등재** (02·06) — 비주얼 락 v5 → v6 환류 필요. EP 본문 [Visual] 묘사 유지.
2. **EP1 어머니 인장 EP2+ 미회수** (03) — EP2 S#1 [Visual]에 pendant 처리 한 줄 추가 (의상 라이닝 이동).

### 4-Gate 진입 조건

모든 페르소나 verdict ≥ "조건부 통과" 충족. "패치 필수" 3건 (02·03·06) — phase_6 패치 후 Round 2 fresh 검토 → 4-Gate 진입.

### 다음 단계
phase_6 Round 1 패치 (필터 1 채택: 인과 논리·정합성) → Round 2 fresh 검토 → 4-Gate.
