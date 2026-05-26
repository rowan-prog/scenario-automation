# THE OFFERING — 진행 메타

## 🔒 v45 LOCK 직전 — 2026-05-22 후반 (EP01 dialogue 신화·voice memory 엔진 + EP46 회상 정합)

**제목:** `THE OFFERING: Crowned by the Dragon Lord` (v34부터 유지)

**정본 (LOCK 후보 FINAL):** `07_final/02_the_offering_FINAL_v45_clean.md` (v44 base + EP01/EP46 voice memory 정합 4건)

**v45 = v44 + 사용자 P0 4건 (2026-05-22 후반):**

**EP01 PRIEST VO fix (line 238):**
- `PRIEST (VO):  — IMPURE.` (깨진 줄) → `PRIEST (VO): IMPURE!` (광고 컷 적합·한 단어 강타)

**EP01 첫 만남 dialogue 교체 (line 55-58) — voice memory 엔진 신설:**
- 옛: `HIM: No name? / ISOLDE: No name. / HIM: One night? / ISOLDE: One.` (현대 원나잇 느낌)
- 신: `HIM: This is not my face. / ISOLDE: Nor mine. / HIM: Then remember my voice. / ISOLDE: Make me.`
- 이유: glamour 설정 활용·voice memory 엔진 박기·"Make me" = Isolde 선택/도발/성적 긴장 동시·EP46 voice reveal 회수 연결

**EP01 후반 voice 발화 교체 (line 131):**
- 옛: `HIM: Still one night? / ISOLDE (breath broken): Still one.`
- 신: `HIM: Will you remember? / ISOLDE (breath broken): Your voice.`
- 이유: 앞 4행 교체로 "one night" 반복 부적합·voice memory 엔진 재강조

**EP46 voice flashback 회수 (line 4873):**
- 옛: `His voice — *No name? No name. One night? One.*`
- 신: `His voice — *This is not my face. Nor mine. Then remember my voice. Make me.*`
- 이유: EP01 변경 → EP46 회상 정합 필수·voice 회수 + Isolde 몸이 먼저 알아봄 보상 강화

**v45 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어) ✅
- 허용 5종만 (블록 분포 v44 동일) ✅
- EP↔END HOOK = 50↔50 ✅
- EP01 voice memory 엔진 = 박힘 ✅
- EP46 voice flashback 정합 = 회수 ✅
- 본편 구조·T4/T5 분포·핵심 대사 = v44 그대로 유지

**상태: 🔒 LOCK 후보 FINAL.** 사용자 최종 확인 후 commit anchor + LOCK 선언.

---

## 🔒 v44 — 2026-05-22 후반 ([END HOOK] 정리 + first time 정합)

**Archive:** `07_final/02_the_offering_FINAL_v44_clean.md` (v45 base · END HOOK 9건 + first time 3건)

**v44 = v43 + 사용자 양식 룰 (2026-05-22 후반):**

**[END HOOK] 원칙 적용 (사용자 명시):**
> `[END HOOK]` 안에는 마지막 화면/행동만 둔다. 대사는 직전 `[DIALOGUE]` 블록에 두고, 대사 자체가 마지막 훅이면 [END HOOK]은 대사 직후의 최종 표정/정적/컷으로 처리.

**[END HOOK] 9건 정리 (대사 → [DIALOGUE] + 마지막 화면/행동 → [END HOOK]):**
- EP03 `STEPMOTHER: The dragon takes damaged things.` → 대사 [DIALOGUE]·END HOOK: `Isolde hears it through the door.`
- EP19 `ADELINE/ISOLDE first decision` → 대사 [DIALOGUE]·END HOOK: `The throne room stays silent around the new queen.`
- EP27 `ISOLDE/VAEL "That was clear"` → 대사 [DIALOGUE]·END HOOK: `The body stays on the road.`
- EP31 `VAEL/ISOLDE "three new house members / heads of state"` → 대사 [DIALOGUE]·END HOOK: `The three ridge dragons bow to Isolde.`
- EP33 `ISOLDE/VAEL "Who holds her first / No one"` → 대사 [DIALOGUE]·END HOOK: `His hand stays on her belly.`
- EP38 `VAEL/ISOLDE "At cycle eighteen"` → 대사 [DIALOGUE]·END HOOK: `The hall holds on the decision.`
- EP41 `VAEL/ISOLDE "You did not flinch / nineteen cycles"` → 대사 [DIALOGUE]·END HOOK: `Her hand stays steady on the child.`
- EP47 `ISOLDE/VAEL "I love you" labor eve` → 대사 [DIALOGUE]·END HOOK: `He stays at her side as the next contraction comes.`
- EP48 `HALREN: A girl, my lady.` → 대사 [DIALOGUE]·END HOOK: `Vael looks at Isolde before he looks at the child.`

**EP15·EP39·EP50 그대로 유지** (사용자 명시 — VO/마지막 화면/그래픽 성격 섞임·맛 유지)

**"first time" 표현 3건 정합 정정 (EP16/EP23 T4 추가 후):**
- EP17: `The chair beside the bed is closer now. He has not crossed into the bed. She has not invited him into it.` → `The chair is beside the bed again. He has not crossed into it since that night. She has not invited him again.` (EP16 T4 후 = "처음 안 들어옴" X)
- EP23: `The chair beside the bed empty for the first time.` → `The chair beside the bed sits empty.` (EP16 T4 직후라 first time 잘못)
- EP28: `They sleep three feet apart on the same cover for the first time.` → `They sleep three feet apart on the same cover.` (EP16/EP23 결합 후 first time 잘못)

**v44 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어) ✅
- 행정 어휘 = 0건 ✅
- 허용 5종만 (VISUAL/ACTION 445 · DIALOGUE 373 · END HOOK 50 · KEY CAMERA 28 · UI/GRAPHIC 20) ✅
- EP↔END HOOK = 50↔50 1:1 ✅
- [END HOOK] 안 대사 = 0 (EP15·39·50 제외 — 사용자 허용) ✅
- "first time" 의미 정합 = OK ✅
- 본편 구조·핵심 대사·T4/T5 분포 = v43 그대로 유지

**상태: 🔒 LOCK 후보 FINAL.** 사용자 최종 확인 후 commit anchor + LOCK 선언.

---

## 🔒 v43 — 2026-05-22 후반 (LOCK 직전 정정 — P0 논리 오류 2 + P1 반복/spoken 2)

**Archive:** `07_final/02_the_offering_FINAL_v43_clean.md` (v44 base · P0/P1 4건 정정)

**v43 = v42 + 사용자 P0/P1 4건 (2026-05-22 후반):**

**P0 논리 오류 2건:**
1. **EP23 line 3102** `another woman's house mark still on his throat` → `Sera's house mark still in my head` (Vael 목에 다른 여자 mark 있는 듯 읽히는 논리 오류. 사용자 추천대로 Isolde 머릿속 hatred로 변경)
2. **EP31 line 3700** Isolde "My window. My bed. My child. **You** gave them all three." → **She** gave them all three. (Vael에게 "네가 넘겼다" 잘못 읽힘 → Sera에 대한 분노 발화. Vael 응답도 "She answers for all three"로 정합)

**P1 반복/spoken 2건:**
3. **EP09** `The bed is mine. The door is mine. Tonight, both stay closed to everyone but you.` → `No one crosses that door tonight unless she asks.` (직후 "The bed is mine but I will not be in it tonight" 반복감 제거)
4. **EP12** `I am damaged goods by every measure your council values.` → `By your rules, I am damaged goods.` (긴 발화 spoken 압축)

**LOCK 차단 X 미세 사항 (점검 통과):**
- EP26 OUTER WALL: / CHAMBER: / SERA'S WING: 미니 라벨 = [VISUAL/ACTION] 안 plain text 허용 OK
- EP15 END HOOK 안 VO = 최종 컷 기능 OK

**v43 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어) ✅
- 행정 어휘 = 0건 ✅
- 허용 5종만 (블록 분포 v42 동일) ✅
- 본편 구조·핵심 대사·T4/T5 분포 = v42 그대로 유지
- 논리 오류 = 0 ✅

**상태: 🔒 LOCK 후보 (FINAL 가능권)** — 사용자 최종 확인 후 commit anchor + LOCK 선언.

---

## 🔒 v42 — 2026-05-22 후반 (S+ 디테일업 — P0/P2/P3 + EP16/EP23 T4 + micro 12)

**Archive:** `07_final/02_the_offering_FINAL_v42_clean.md` (v43 base · S+ 디테일 적용)

**v42 = v41 + 사용자 S+ 디테일업 (2026-05-22 후반):**

**P0 기계/정합성 7건:**
1. EP05 `box my father had built before he was born` → `long before I was born` (시간 정합)
2. EP19 `Hold her there until the next moon. Then we will decide.` → `Hold her there tonight. No one touches her until I decide.` (EP20 Drakonis 호송 시점 정합)
3. EP49 `S#1B` → `S#2` (S 순번 정리 + 기존 S#2 → S#3)
4. EP41 `No drugs for the pain.` → `Bandage it. Let her remember why.` (Isolde 가학 톤 완화)
5. [END HOOK] 뒤 새 블록 누수 정리 13건 (Python script): EP12·EP15·EP19·EP28·EP33·EP34·EP37·EP38·EP39·EP41·EP42·EP47·EP48·EP49 [END HOOK] 위치 이동 (각 EP 마지막 컷에만)
6. [DIALOGUE] 밖 발화 4건 → [DIALOGUE] 안으로: LORD CORVIN (memory)·ADELINE (Whore's daughter)·LORD CORVIN (She'll learn quiet)·MAID (Smile)·MIREILLE (off, soft)
7. [UI/GRAPHIC] 뒤 액션 누수 4건 → [VISUAL/ACTION] 헤더 추가: KING ALDRIC·SERA·VAEL·EP49 빈 [VISUAL/ACTION] 제거

**P2 EP16 S#3 T4 확장 (first paid full T4 — 정답 미공개 유지):**
- 사용자 명시 대사 + 구체적 행동: `You still won't answer. / Ask me anything but the festival. / Then don't talk. / I'll stop if you ask. / I didn't ask.`
- Isolde 먼저 선택 (의자에서 chair → bed로 끌어당김)·Vael 멈추고 물음·Isolde 거절 + 끌어당김
- 구체적 묘사: 양손 shirt grip·bed로 walking·lip bite·hand at back of head·scaled palm at ribs through shift·jaw·tongue·CUTAWAY 양식·결합 후 spoon position
- festival/pregnancy/mate/heir reveal 0
- 다음날 정답 미공개 유지

**P2 EP23 T4 추가 (EP16-EP29 13화 공백 해소 — 내 판단 적용):**
- INTERCUT 끝 + Isolde 자다 깸 + Vael bloodied hand 본 후 침대로 끌어당김
- 사용자 룰 = "부부싸움(분노/응징 폭발) 직후의 강렬한 결합" 정합 (Sera 편지 발각 + Vael L1 응징 후)
- 구체적 묘사: bloodied knuckles at her throat·hand at his shoulders·legs open around hips·forearm braced·headboard grip wood creaks·open mouth on jaw·bite at throat under scale·tongue·hair pulling·thigh hooking·bedsheet fisted·broken breath
- 정체 미공개 유지

**P3 micro 12개 추가 (1줄씩, 기존 장면 안에서):**
- EP09 VAEL: `The bed is mine. The door is mine. Tonight, both stay closed to everyone but you.`
- EP10 `His fingers close around her wrist. Not hard. Enough that she remembers the wall.`
- EP13 `The distance between the chair and the bed is no longer distance enough.`
- EP17 `The scale under her palm is warm in a place her body remembers before her head does.`
- EP20 `His arms hold her like a wall. Her body goes quiet before her grief does.`
- EP23 `His scale lifts once, then settles.` (자는 hand finds 비트 직후)
- EP28 `His hand stays on the stone because touching her stomach now would tell her everything.`
- EP31 ISOLDE: `My window. My bed. My child. You gave them all three.` + VAEL: `They were yours before I gave them.`
- EP33 `He waits for the child to move. She watches his mouth instead.`
- EP36 `Her hands on his scaled neck do what no command in the hall can do.`
- EP39 `His palm on her belly under the crown makes the hall disappear for one breath.`
- EP44 `Vael lies down behind Isolde. One hand on the child. His breath held at her neck.`

**T4/T5 최종 분포 (7개):**
| EP | T-Level | 기능 |
|---|---|---|
| EP01 | T4 | Festival night — first night·정체불명 |
| EP16 S#3 | T4 | First paid full — chair → bed·정답 미공개 |
| EP23 (NEW) | T4 | INTERCUT 후 첫 화해 결합·bloodied hand 안 묻고 끌어당김·정체 미공개 |
| EP29 | T4 | Cycle eight — eight cycles of holding back |
| EP40 | T4 | Crown 후 침실 — `The crown is the keep's. Tonight you are mine.` |
| EP43 | T4 | Sera 손 절단 직후 분노 → chamber strong-claim |
| EP46 | T5 | 정체 reveal + 첫 양방향 "I love you" + 결합 정점 |

**EP16-EP29 공백 해소:** 13화 → EP23 T4 추가로 7+6 분할.

**키스/베드씬 구체성 룰 적용 (사용자 명시):**
- 키스 = 입만 시늉 X. 혀 사용·부분 (jaw·throat·earlobe)·머리카락/뺨 거칠게 잡기·lip bite·open mouth
- 베드씬 = 침대 sheet 꽉 잡는 손·헤드보드 grip·양팔로 상체 끌어안기·다리로 hooking·머리카락/뺨 거칠게 잡기·broken breath·구체적 위치 묘사
- CUTAWAY 양식 = 노골적 신체 관음 X·Vael 반응 + Isolde 선택 + 구체적 행동 중심

**v42 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어) ✅
- 행정 어휘 = 0건 ✅
- 허용 5종만: VISUAL/ACTION (443) · DIALOGUE (367) · END HOOK (50) · KEY CAMERA (28) · UI/GRAPHIC (20) ✅
- 비표준 블록 = 0 ✅
- EP↔END HOOK = 50↔50 1:1 ✅
- VO 깨진 패턴 = 0 ✅
- 장면 헤더 빨림 = 0 ✅
- 본편 구조·핵심 대사 = v41 그대로 유지

**상태: 🔒 LOCK 가능권** (P0 기계 정합 + S+ 디테일업 완료)

---

## 🔒 v41 — 2026-05-22 후반 (FORMAT REPAIR)

**Archive:** `07_final/02_the_offering_FINAL_v41_clean.md` (v42 base · v40 변환 오염 정정)

**v41 = v40 + 사용자 P0 format repair (2026-05-22 후반):**

**P0 변환 오염 정정 (Python repair script — story·dialogue·scene order untouched):**

1. **`VO (VO): CHARACTER:` 중복 패턴 fix** (10건):
   - `VO (VO): ISOLDE: ...` → `ISOLDE (VO): ...` (line 637/682/707/710/946/1010/1198)
   - `ISOLDE (VO): ISOLDE: ...` → `ISOLDE (VO): ...` (line 2499)
   - `SERA (VO): SERA: ...` → `SERA (VO): ...` (line 2965)
   - `VAEL (VO): VAEL: ...` → `VAEL (VO): ...` (line 2976)

2. **장면 헤더가 VO 안으로 빨림 fix** (3건 — 치명적 오류):
   - `PRIEST (VO): ## S#5 — Veine Palace. Bridal Mirror Hall. Continuous.` (line 238) → 분리: `PRIEST (VO): THE BRIDE — IMPURE.` 직후 standalone `## S#5 — ...` 복구. **EP01 S#5 복구.**
   - `VO (VO): ## S#2 — Veine Palace. Outer Courtyard. Pre-Dawn.` (line 638) → 분리: standalone `## S#2 — ...` 복구
   - `VO (VO): ## S#2 — Wasteland. The Road. Late Afternoon.` (line 711) → 분리

3. **컷 지시 → VO 흡수 오류 fix** (1건):
   - `ISOLDE (VO): Hard Cut.` (line 2222) → plain text `Hard Cut.` (지문 복구)

4. **중간 [END HOOK] 제거** (3건 — 각 EP 마지막 컷에만 허용):
   - EP06 line 812 mid-EP [END HOOK] 제거 (S#1 끝 → 단순 Hard Cut.)
   - EP30 line 3535 mid-EP [END HOOK] 제거 (S#2 끝 → 단순 Hard Cut.)
   - EP50 line 5249 mid-EP [END HOOK] 제거 (S#1 끝 → 단순 Hard Cut.)
   - 결과: **EP 50개 ↔ [END HOOK] 50개 1:1 정합 ✅**

5. **블록 양식 통일** [GRAPHIC/UI] → [UI/GRAPHIC] (20개):
   - 사용자 명시 고정 양식 = `[UI/GRAPHIC]` (NOT `[GRAPHIC/UI]`)

**v41 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines ✅
- 행정 어휘 = 0건 ✅
- 허용 5종만: VISUAL/ACTION (422) · DIALOGUE (364) · END HOOK (50) · KEY CAMERA (27) · UI/GRAPHIC (20) ✅
- 비표준 블록 = 0 ✅
- VO 깨진 패턴 = 0 ✅
- 장면 헤더 빨림 = 0 ✅
- Hard Cut in VO = 0 ✅
- EP 개수 ↔ [END HOOK] = 50 ↔ 50 1:1 ✅
- [GRAPHIC/UI] 잔재 = 0 ✅
- 본편 구조·대사·scene order = v40 그대로 유지

**상태: 🔒 LOCK 가능.** Creative LOCK + Format LOCK 양쪽 통과. 사용자 최종 확인 후 commit anchor.

**Lessons learned (메모리 등재 예정):**
- 일괄 변환 script = 정규식 매칭 정확성 사전 dry-run 강제
- VO 변환 시 `[VO]` 단독 + 다음 라인 `CHAR: ...` 패턴 = 정확히 `CHAR (VO): ...`로 통합 (script 1회차 = `VO`를 char로 잘못 매칭)
- 일괄 변환 후 = 깨진 패턴 grep 검증 강제 (`VO (VO):`, `(VO): ## S#`, `(VO): Hard Cut`, 인물명 중복)
- [END HOOK] 카운트 ↔ EP 카운트 1:1 검증 강제

---

## v40 — 2026-05-22 후반 (블록 양식 P0 1차 시도 — 변환 오염 발생)

**Archive:** `07_final/02_the_offering_FINAL_v40_clean.md` (v41 base · 변환 오염 5건 포함 — v41에서 정정)

**v40 = v39 + 사용자 양식 P0 (2026-05-22 후반):**

**블록 양식 strict 5종만 허용 (Python script 일괄 변환):**
- `[VISUAL/ACTION]` (422)
- `[DIALOGUE]` (364)
- `[END HOOK]` (53)
- `[KEY CAMERA]` (27)
- `[GRAPHIC/UI]` (20)
- **비표준 블록 = 0** ✅

**변환 규칙 (Python script 적용):**
- `[VO — ISOLDE]` / `[VO — VAEL]` / `[VO — SERA]` 등 = `[DIALOGUE]` 안에 `ISOLDE (VO): ...` / `VAEL (VO): ...` / `SERA (VO): ...`
- `[FLASHBACK — Festival Night]` 등 = `[VISUAL/ACTION]` 안에 `Flashback — Festival Night.` plain prose
- `[FLASH CUT]` = `[VISUAL/ACTION]` 안에 `Flash cut.` plain
- `[BACK — Chamber]` / `[BACK TO FESTIVAL]` 등 = `[VISUAL/ACTION]` 안에 `Back in chamber.` / `Back to festival.`
- `[CUTAWAY]` / `[CUTAWAY — Three Days Ago]` = `[VISUAL/ACTION]` 안에 `Cutaway — three days ago.`
- `[INTERCUT — Outer Wall + Vael's Chamber + Sera's Wing]` 등 = `[VISUAL/ACTION]` 안에 `Intercut — outer wall + chamber + sera's wing.`
- `[CUT BACK — Chamber]` = `[VISUAL/ACTION]` 안에 `Back to chamber.`
- `[INSERT — page audience-visible]` = `[VISUAL/ACTION]` 안에 `Insert — page audience-visible:`
- `[MONTAGE — Five Weeks Compressed]` = `[VISUAL/ACTION]` 안에 `Montage — five weeks compressed:`
- `[CUT TO TITLE CARD]` = `[GRAPHIC/UI]`로 변환
- `[DIALOGUE — through the door]` 등 변종 = `[DIALOGUE]`로 통합
- `[END S#1]` 같은 의미 없는 헤더 = 삭제

**GRAPHIC/UI 인물·장소·시간점프 카드 추가 (13개 신규):**
- 인물 첫 등장 (이름 / 단순 호칭):
  - `ISOLDE / princess of veine` (EP01)
  - `KING ALDRIC / her father` (EP02)
  - `LORD CORVIN / her betrothed` (EP02)
  - `ADELINE / her half-sister` (EP02)
  - `STEPMOTHER / dowager queen` (EP02)
  - `KIRAN / dragon lord's captain` (EP06)
  - `SERA / volzaar daughter` (EP06)
  - `VAEL / dragon lord of drakonis` (EP08 — Vael 공식 첫 등장. festival night man = 정체 미공개 유지)
  - `HALREN / dragon healer` (EP28 cutaway)
  - `VEYRA / western lord's niece` (EP37)
  - `MIREILLE / their daughter` (EP49)
- 핵심 장소:
  - `VEINE / FIRE FESTIVAL NIGHT` (EP01)
  - `VEINE PALACE / BRIDAL MIRROR HALL` (EP02)
  - `DRAKONIS KEEP / outer gate` (EP06)
  - `DRAKONIS KEEP / inner garden` (EP50)
- 시간 점프:
  - `ONE MONTH LATER` (EP01 S#4 — 기존 유지)
  - `TWO AND A HALF YEARS LATER` (EP50 S#3)
- 타이틀 카드:
  - `THE OFFERING` (EP01)
  - `THE OFFERING: Crowned by the Dragon Lord — END` (EP50 끝)

**불필요 GRAPHIC/UI 제거:**
- 빈 GRAPHIC/UI 블록 (EP01) 제거
- `PAYWALL — EP09 →` (EP08 끝, 마케팅 카피·작가 메모) 제거

**v40 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines ✅
- 행정 어휘 = 0건 ✅
- 허용 외 블록 = 0건 ✅
- GRAPHIC/UI = 핵심 인물·장소·시간점프·타이틀 카드만 (마케팅 카피/작가 메모 0)
- 본편 구조·대사 intent·scene order = v39 그대로 유지

**남은 polish 영역 (별도 turn 가능):**
- KEY CAMERA 양식 사용자 표준 (EXTREME HIGH ANGLE / INSERT on / CLOSE on / 1-5 샷 정렬) 점검·정리
- 추가 인물 카드 (VOLMIR / WESTERN LORD / RIDGE DRAGON 등) — 사용자 명시 시
- 추가 장소 카드 (EASTERN RIDGE / GREAT HALL / VAEL'S CHAMBER 등) — 사용자 명시 시

---

## 🔒 v39 — 2026-05-22 후반 (외부 AI 영어 polish — 작가식 제도 영어 4표현 자연화)

**Archive:** `07_final/02_the_offering_FINAL_v39_clean.md` (v40 base · v38 + 영어 4표현 polish)

**v39 = v38 + 외부 AI 영어 polish (2026-05-22 후반):**

**작가식 제도 영어 4표현 자연화:**
- EP08 line 996: `She is not bridal grade, my lord.` → `She is not fit to be your bride, my lord.` (Sera 모욕어 자연화)
- EP09 line 1085: `she is not bridal grade.` → `she is not fit for this.` (Sera hedging 발화·line 1089 `She is not a bride` 직설로 자연 흐름)
- EP12 line 1654-1655: `The bride question stands. / The bride question is mine. Stand and answer the part that is yours.` → `Then we still have one question. What is she to this keep? / That is my decision. Answer the rest.` (작가 만든 의회 용어 → 직관)
- EP16 line 2211-2245: `withdrawal of common air rights` + `that is not refusing the air rights` 등 → `The council closes the eastern sky to Drakonis if you refuse.` + `Closes the sky?` + `That's not refusing. That's starting a war.` (행정/항공 용어 → 직관적 시각)

**EP16 council letter 비트 spoken English 수축형도 함께 적용** (해당 사적 위협 비트):
- `I will not give me to them. He is going to lose half` → `He won't give me to them. He'll lose half`
- `She does not say it. / Do not. / I did not say anything.` → `She doesn't say it. / Don't. / I didn't say anything.`
- `I would have said it in your chair.` → `I'd have said it in your chair.`
- `That is not refusing the air rights. That is starting a war.` → `That's not refusing. That's starting a war.`
- `They started it. I am finishing the sentence.` → `They started it. I'm finishing the sentence.`

**v39 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어) ✅
- 행정/제도 영어 = 0건 ✅ (bridal grade·bride question·air rights 모두 정리)
- 작가식 영어 잔재 = 0건 ✅
- 본편 구조 = v38 그대로 유지

---

## 🔒 v38 — 2026-05-22 후반 (사용자 final P1 — EP32 학대 1문장 삭제)

**Archive:** `07_final/02_the_offering_FINAL_v38_clean.md` (v39 base · v37 + EP32 patch)

**v38 = v37 + 사용자 final P1 (2026-05-22 후반):**

**P1 EP32 학대 톤 1문장 삭제:**
- `She has not eaten. She has not bathed. She has not been allowed to change clothes.` → 삭제
- Why: 70 miles 걷기 + lip split + dust + wrist black + 공개 편지 낭독 + kneeling만으로 굴욕 충분. `not bathed / not allowed to change clothes` = 학대 쪽으로 읽힘 + 추가 도파민 X = 하이리스크 로우리턴.

**평가자 최종 판정 (사용자 인용):**
- 구조 = **LOCK 가능**
- 핵심 쾌감 = **충분히 강함**
- 리스크 관리 = **대체로 적정**
- 한 줄: "EP32 한 문장 삭제만 권장. 더 이상 구조 건드리지 마라."

**v38 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어 = EP46+EP47+EP50) ✅
- 행정 어휘 = 0건 ✅
- 정답 4 미공개 EP10-EP45 ✅
- 정체 reveal = EP46 (silver+wooden bird + 분노+T5 폭발) ✅
- 임신 인지 = EP28 (둘만) ✅
- Sera 가학 톤 = 완전 안전권 ✅
- Isolde 취약+자존심 = 균형 ✅
- spoken English 수축형 사적 장면 = 적용 ✅
- 학대 톤 잔재 = 0건 ✅

**🔒 LOCK 상태:** 사용자 명시 "거의 FINAL LOCK 가능권" → 사용자 최종 확인 후 LOCK 선언 + commit anchor.

---

## 🔄 v37 — 2026-05-22 후반 (사용자 종합 톤 패스 — agency·완성형 톤 다운·spoken English 수축형)

**Archive:** `07_final/02_the_offering_FINAL_v37_clean.md` (v38 base · v36 + 톤 패스)

**v37 = v36 + 사용자 종합 피드백 (2026-05-22 후반·LOCK 가능권):**

**P0 (필수):**
- **EP10 agency 오해 fix:** `That man did not let me leave the bed.` → `That man made me forget there was a door.` (강제/비동의 뉘앙스 제거·EP01 선택 정합 유지)
- **EP50 Sera plural hands fix:** `Find work for her hands.` → `Find her work down there.` (Sera 한 손 잃음 → plural hands = 조롱 느낌 제거)

**P1:**
- **EP02 No fear 잔재 fix:** `No fear. No apology.` → `Fear flashes once. She hates it. No apology.` (취약+자존심 동시 진동)

**Isolde 공적 톤 다운 (3건 — 너무 완성형 여왕/페미니즘 히어로 톤):**
- EP25 `That is the order.` → `That's how we do it.`
- EP37 `You did not ask to be here. Go home. Marry whoever you choose. If any dragon house ever offers you to my husband again, I will hear about it before they finish the sentence — and the keep will answer.` → `You didn't ask to be here. Go home. If any dragon house offers you to my husband again — I'll hear about it before they finish the sentence.`
- EP41 `I am at cycle nineteen. I am done flinching.` → `I've been flinching for nineteen cycles. I'm tired of it.` (취약+자존심 톤)

**Spoken English 수축형 사적 장면 polish:**
- EP10 첫 침실 (`I am → I'm`·`That is → That's`·`I will → I'll`·`does not → doesn't`·`cannot → can't` 등)
- EP16 침실 chair closer 비트 + Visitor 후 VO
- EP28 임신 인지 사적 비트 (Vael "Yours" 선언 폴리시)
- EP29 침실 basin 비트
- EP46 reveal 사적 비트 (`Do not touch me.` → `Don't touch me.` / `I will not.` → `I won't.` / `I cannot decide` → `I can't decide` / `First time I have said it` → `First time I've said it` 등)
- EP47 labor eve 사적
- EP48 labor 침실
- EP49 birth aftermath 사적
- 의식/판결/왕권 (council·hall·throne·declaration·iron plate·crown ceremony) = 격식 유지

**v37 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어) ✅
- 행정 어휘 = 0건 ✅
- 정답 4 미공개 EP10-EP45 ✅
- 본편 구조 = v36 그대로 유지 (사용자 명시 "구조는 더 건드리지 마라")
- Isolde 톤 = 취약+자존심·결정은 빠른 (사용자 균형 명시)

**LOCK 가능권 도달.** 사용자 검토 후 최종 LOCK 또는 추가 turn.

---

## 🔄 v36 — 2026-05-22 후반 (사용자 P0/P1 patch — bird VO 정합 + Sera 에필로그 톤 다운)

**Archive:** `07_final/02_the_offering_FINAL_v36_clean.md` (v37 base · v35 + P0/P1 patch)

**v36 = v35 + 사용자 P0/P1 patches (2026-05-22 후반):**
- **P0-1 EP46 bird VO 정합 오류 fix:** `The same bird. Twice. One my mother died for. One his mother carved.` → `The same bird. Twice. One I left on the table the morning after. One his mother carved.` (Isolde 어머니 ≠ silver pin 설정. EP01 회수 감정 정확.)
- **P0-2 EP50 grey-haired Sera fix:** `a thin grey-haired figure in plain servant clothing. Her throat is bare. She does not look up at the bench.` → `a thin red-haired figure in plain servant clothing. Her throat is bare. She does not look up.` (2.5년 만에 회색머리 = 마법적 노화/학대 느낌. red-haired = Sera 알아보이되 망가뜨린 느낌 줄임.)
- **P1 EP50 smell of fear 삭제:** `She has not been allowed to wash since yesterday evening — she smells of her own fear.` 문장 삭제 (저급한 가학으로 읽힘)

**v36 자가 검증 추가:**
- bird VO 정합 = OK ✅
- Sera 에필로그 잔상 = 톤 다운 ✅
- "Smell of fear" 가학 라인 = 제거 ✅
- 본편 구조 = v35 그대로 유지 (사용자 명시 "그 외 구조는 더 건드리지 않는 게 맞다")

**별도 turn으로 보류 (사용자 결정 필요):**
- Spoken English 수축형 polish (사용자 인용한 두 번째 검토자 평가): 침실/상처/reveal/임신/출산 대사 한정으로 `I am not / I cannot / I have / First time I have` → `I'm not / I can't / I've / First time I've` 변환. 의식/처벌/왕권 선언은 격식 유지. 별도 명시 요청 시 진행.
- Corvin 회수 보강 (두 번째 검토자 지적): EP01 강한 setup 대비 후반 너무 조용히 사라짐. 단 사용자 본인 "그 외 구조 더 건드리지 마라" 명시 → 별도 turn.

---

## 🔄 v35 — 2026-05-22 후반 (사용자 종합 피드백 — EP46 reveal 강화 + Isolde 취약 톤 + Sera 가학 톤 다운)

**Archive:** `07_final/02_the_offering_FINAL_v35_clean.md` (v36 base · 5,310 lines · 사용자 P0/P1 patch 적용 전)

**Archive (옛 v33.5.7):** `07_final/02_the_offering_FINAL_v33_5_clean.md` (4,811 lines · 정합 완성 · 보상 너무 빠른 모델 · 참고용)

**⚠️ v34 base 단독 보존 X:** v34 (Turn 1-5 자율 작업 결과) → 사용자 종합 피드백 직접 덮어쓰면서 git commit 안 한 상태에서 분기 시점 놓침. v34 단독 file 보존 못 함. 다음부터 매 turn commit으로 anchor 잡기.

**v35 = v34 base + 사용자 종합 피드백 (2026-05-22 후반):**
- **EP46 reveal 대폭 강화** (얌전한 확인 대화 → 분노+배신감+몸의 기억+Vael 기다림+Isolde 다시 다가감+T5+I love you 한 장면 폭발)
  - 두 새 reveal + Isolde 충격
  - FLASHBACK festival night + Isolde 두 손가락 Vael 턱에 (몸의 기억)
  - 분노 dialogue (`A whole year. / You watched me want you. / You kept me starving.`)
  - Vael 자기 두려움 인정 (`I was afraid of you looking at me the way you are looking at me now.`)
  - `Do not touch me.` / `I will not.` / Vael 손 desk에 펴고 기다림
  - Isolde 분노한 채로 다시 다가감 → 첫 키스 + lip bite + `Make it up.`
  - T5 결합 (CUTAWAY: 신체+pin+wooden bird+tear가 Vael 손에 떨어짐)
  - 결합 후 양방향 `I love you`
- **EP49 Sera 가학 톤 다운:** "You watch my daughter / You die when I am done" 라인 제거 → "Without a name. Without a house. You are no one. She does not exist in this hall." + Isolde 더 이상 의식하지 않음
- **Isolde 취약 톤 보강 (6건):**
  - EP02 `She does not cry.` → `Her eyes shine. She does not let the tear fall.`
  - EP05 `She is not afraid. She is curious.` → `Fear crosses her face. Then something harder covers it. She is curious.`
  - EP06 `She does not flinch.` → `She flinches once at the sound. Hates that her shoulders moved.`
  - EP15 `She does not flinch.` → `Her hand grips the basin edge. White at the knuckle.`
  - EP35 `She does not cry. Does not raise her voice.` → `Her hand shakes once when she refolds the letter. Her voice still lands.`
  - EP42 `She does not cry. Does not yell.` → `Her eyes shine once. She does not let the tear fall.`

**v35 자가 검증:**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어 = EP46+EP47+EP50) ✅
- 행정/법/정치 어휘 = 0건 ✅
- 정답 4 미공개 EP10-EP45 ✅
- 정체 reveal = EP46 (silver+wooden bird + 분노+T5 폭발) ✅
- 임신 인지 = EP28 (둘만) ✅
- Sera 가학 톤 = 다운 완료 ✅
- Isolde 취약+자존심 톤 = 보강 완료 ✅

---

## 🔄 v34 (Turn 1-5 자율 작업 단계 — v35 base) — 2026-05-22

**v34 재기획 핵심 원칙 (사용자 + 외부 피드백 통합):**

1. **EP01-EP03 = 최대한 유지** (정합 보강만 · 사건 추가 X · 재구성 X)
2. **EP10-EP45 = 정답 0** (정체 / 임신 / mate / heir / queen / family 모두 미룸)
3. **EP46-EP49 = 보상 4 단계 폭발** (정체 → 사회 인정 → 출산 → queen + Sera 영원)
4. **EP50 = 짧은 family lock + 둘째 hint + Fade Out**
5. **중간 자극 = high-heat + 양방향 응징 (대놓고 + 남모르게) + Isolde 속마음 + denial + 거의-reveal**
6. **Vael = 차갑고 거칠고 강압적 + Isolde에게만 지극 + Dragon Shadow + 언령 마법**
7. **Isolde 속마음 = 짜증·부정·끌림·인정하기 싫은 욕망** (퉁명스러운 여성향 부정·trauma spiral X)
8. **소품 = 5-6 핵심만** (silver bird pin · wooden bird · silver crown · Volzaar mark · Veine 6-seal letter)

**보상 위치 매트릭스:**

| 보상 | EP | 비율 |
|---|---|---|
| Bride 공개 첫 선언 | EP09 | 18% |
| Isolde 임신 인지 (둘만) | EP28 | 56% |
| Public bride/mate/heir 공식 (외부 letter 응답) | EP41 | 82% |
| **정체 reveal (Isolde가 확정)** | **EP46** | **92%** |
| **마음 합일 (`I love you` 양방향)** | **EP46-47** | **92-94%** |
| 출산 + Mireille 명명 | EP48 | 96% |
| Public queen + Sera 영원 굴욕 | EP49 | 98% |
| Family lock + 둘째 hint | EP50 | 100% |

**응징 레벨 분포 (EP10-EP49):**
- L1 (남모르게·audience-only) = 50% · 매 2-3 EP마다
- L2-L3 (대놓고 small/medium) = 30%
- L4-L5 (대놓고 정점·hand 절단·영원 굴욕) = 20% (후반 집중)

**수위 분포 (T1-T5):**
- T4 (full 결합) = 5 비트 (EP01·EP18·EP24·EP29·EP43)
- T5 (정점·마음 합일 직전) = 1 비트 (EP46)
- T2-T3 (kiss·partial) = 약 12 비트 · 매 EP 마다 tension 누적
- T1 (touch·외부) = 약 20 비트

**진행 plan (5 turn 분할):**
- Turn 1 ✅ 완료: framework + title 변경 + meta + visual_lock title
- Turn 2 ✅ 완료 (2026-05-22): EP10 Isolde 부정 VO 추가·EP12 council mate 단정 → dragon shadow 위압 + 정답 미공개·EP14 임신 카드 → 자기 선언 카드·EP15-16 완전 재작성 (Volmir 손 burn·Sera corridor 위협·Council letter 거부·Visitor 호칭 박살·chair closer)·EP17-EP20 mate/heir 발화 제거·visual_lock props 19→5 축소
- Turn 3 ✅ 완료 (2026-05-22): EP22 MONTAGE 5주 압축·EP23 INTERCUT 3공간 + Vael/Sera VO 1회씩 (감정 엔진)·EP25 FLASHBACK festival night (basin)·EP26 외부 wall 침입 INTERCUT·EP28 임신 인지 첫 (CUTAWAY Halren) + Vael "Yours" 선언·헤더 cycle counting 복원
- Turn 4 ✅ 완료 (2026-05-22): EP37 Veyra "my queen" → "my lady" (외부 호칭 미공인)·EP41 Sera wrist burn·EP42 letter burn + 4 declarations·EP43 Sera 손 절단 + Vael 강제 echo·EP44 VO 3개→1개 통합
- Turn 5 ✅ 완료 (2026-05-22): EP46 정체 reveal 추가 (silver pin + wooden bird 둘 같이 + Isolde 확정 + Vael 1년 침묵 이유 설명) + 첫 양방향 "I love you"·EP47 두번째 "I love you" 추가·EP48 출산 + INTERCUT 침입·EP49 Mireille 명명·EP50 Sera 영원 servant + 둘째 hint + Fade Out + 새 title super

**자가 검증 (2026-05-22 v34 완료):**
- Korean = 0건 ✅
- Hard Cut = 49 + Fade Out 1 ✅
- "I love you" = 6 lines (3 페어 = EP46+EP47+EP50) ✅ (iloveyou_budget 정합)
- 행정/법/정치 어휘 = 0건 ✅
- 정답 4 미공개 EP10-EP45 ✅
- 정체 reveal = EP46 (silver+wooden bird 같이) ✅
- 임신 인지 = EP28 (둘만) ✅
- 첫 "I love you" 양방향 = EP46 ✅
- 비선형 연출 추가 = MONTAGE (EP22)·INTERCUT (EP23·EP26·EP48)·FLASHBACK (EP25·EP46)·CUTAWAY (EP28) ✅

**v34 캐릭터 charter 메모리:**
- `memory/project_offering_isolde_character_charter.md` (Isolde 본질: 취약+자존심+끌림 3중·festival night man 부정 루프·PC식 독립성 금지)
- `memory/project_offering_vael_character_charter.md` (Vael 본질: 거칠고 차가운 Dragon Lord·Isolde에게만 지극·말 1-5단어·Dragon shadow·언령)
- `memory/project_offering_v34_writing_charter.md` (집필 charter: 4 지연 질문·sex≠관계 정답·VO 절제·비선형 연출 강제·중반 욕망 엔진)

---

## 🔒 옛 정본 v33.5.7 — 2026-05-22 LOCKED (v34 base · archive 참고용)

**v33.5.7 patches (8 — 전수 검수 마감):**
- EP01 line 138 emotion-as-narration ban: `That breaks him.` → `He stops trying to slow down. His jaw goes hard against her mouth.` (action sequence)
- EP12 line 1572 article 누락 grammar: `That is not bride. That is mate.` → `That is not a bride. That is a mate.`
- EP12 line 1587 plural stiff: `There are no precedents.` → `There is no precedent for this.`
- EP16 line 2052 clunky construction: `the keep will not survive me being a stranger to it.` → `the keep will not survive a stranger in your chair.`
- EP23 line 2698 birth-cycle baseline 정합 (EP48 cycle 24 birth와 정합): `Real labor at twenty.` → `Real labor between twenty and twenty-four. Firstborns often wait.`
- EP29 line 3046 emotion-as-narration ban: `That is what breaks him.` → `He stops trying. His hand closes once at her waist. Tight.`
- EP32 line 3329 long anaphora 분리: comma → period (vertical 호흡 정정)
- EP50 line 4774 contraction polish: `That is all. We stop after this one.` → `That's all. We stop after this.`

**전수 검수 결과 (사용자 명시 = 치명적 정합·논리공백·논리오류·spoken 어색 only · 사소·연출팀 직관 가능 부분 제외):**
- 치명 정합 모순 = 0건 (모든 patches 후)
- 시간/캐릭터/소품/배경 정합 = 0 모순
- 캐릭터 voice 일관성 = 7 캐릭터 모두 일관 (Isolde·Vael·Sera·Kiran·Halren·Adeline·Aldric)
- 행정/법/정치 어휘 = 0건
- 단위 혼동 (cycle vs years old) = 0건
- emotion-as-narration ban = 0건 (EP01·EP29 patches 후)
- 부위 순회 tracking = 0건 (EP01·EP29 CUTAWAY patches 후)
- 정보 순서 모순 = 0건 (EP13 mother/wooden bird patches 후)
- spoken English 어색 = 0건 (모든 발견 patches 적용 후)

**LOCK Spec:**
```
v33.5.7 = 50 EP / 49 Hard Cut + 1 Fade Out / Korean 0 / "I love you" 3 instances (EP16·EP46·EP50)
정합 모순 0 · spoken 어색 0 · 단위 혼동 0 · 정보 순서 0 · emotion-as-narration 0 · 부위 순회 0 · 행정 어휘 0
```

**v33.5.6 patches (3) — cycle/years old 워싱 (외부 검토 P0):**
- EP37 line 3612 Western Lord: `She is twenty-two cycles old.` → `She is twenty-two years old.`
- EP37 line 3632 Isolde: `You brought a girl twenty-two cycles old` → `You brought a twenty-two-year-old girl`
- EP44 line 4229: `sixteen cycles old, barely past first transformation` → `sixteen years old, barely past first transformation`

**근본 인사이트:**
> `cycle` = 임신 진행 단위 (20 cycle baseline). `cycle` ≠ 사람/드래곤 나이 단위. 동일 단어를 두 의미로 쓰면 시청자가 즉시 "20 cycle 임신 ≈ 22 cycle 성인 여성 나이?" 산수 혼동. **사람/드래곤 나이 = `years old` 강제.** EP02 Isolde 발화 `at eight years old` 와 일관.

**v33.5.5 patches (10):**
- EP01 line 116-124 CUTAWAY 재구성: 부위 순회 (collarbone → throat → shoulder → ribs → hip) 제거 → Vael 통제 상실 + Isolde agency 우선
- EP01 line 151-158 CUTAWAY 재구성: throat/collarbone 중복 제거 + 자연 흐름
- EP09 line 1098 hand-brush 모순: "back of his hand brushes the back of hers" → "his sleeve brushes the back of her hand" (line 1129 "He does not offer his hand" 정합)
- EP19 line 2450: "for sixteen years" → "for years" (Isolde 8세 + 현재 23세 = 15년 차이 산수 모순 회피)
- EP20 line 2523: "for sixteen years" → "for years" (동일)
- EP20 line 2520 first reign: "first reign" → "first act as queen to be" (영어 자연)
- EP29 line 3013-3024 CUTAWAY 재구성: hip 반복 (2회→0회) 제거 + Vael forearm weight + Isolde 머리채 끌어당김
- EP29 line 3037 mouth-tracking: "His mouth slides from her throat down to where his palm is" → "His palm cradles her waist where she put it. He kisses where his palm is." (mouth-tracking 부위 순회 제거)
- EP33 line 3394 grammar: "His face, almost cries. Does not." → "His face almost cries. Does not." (불필요 comma 제거)
- EP50 line 4607 admin vocab: "Sera's Hearing." → "Sera's Reckoning." (vertical-no-admin-power 룰 "hearing" = 금지 어휘 직접 위반)

**v33.5.5 종합 검토 결과 (전수 4,818 lines · agent xhigh effort 분석):**
- 영어 자연성 = 대체로 자연 · 미세 polish 항목 patched
- 정합성 = 0 모순 · 시간/캐릭터/소품/배경 정합
- 북미 여성 paid vertical 적합성 = 강함 (label reversal · paywall · Sera 영원 라이벌)
- 여성향 핵심 만족 요소 = 강함 (alpha possessive · queen fantasy · 출산 보상 · family lock · "I love you" 3 instances · 둘째 hint)
- 남성향 섹슈얼 잔향 = EP01 + EP29 CUTAWAY patches 후 0 잔향 · EP47-49 labor = Female gaze masterclass
- 행정/법/정치 어휘 = "Sera's Hearing" 1건 patch 후 0건

**비주얼락 v5 (OEXZ 양식 영어 전면 재작성):**
- 0. Purpose / 1. Common Design Lock (1.1-1.6) / 2. Characters (Isolde·Vael·Sera·Kiran·Mireille·Halren·Adeline·Aldric·Stepmother·Corvin·Volzaar Cousins·Western Lord+Veyra·Keep Lords·Ridge Dragons) / 3. Props (19) / 4. Backgrounds (27) / 5. Must Generate First / 6. Final Read Test
- Look 형식 = "Isolde Look 1-10" 영어 명사 위주 · 의상 = 헤어+의상+신발+악세사리 한 셋트 · 사소한 변형은 새 look 안 만듬 · 헤어는 스토리 필요 시만 변경
- 옛 한국어 v4 = `_archive_versions/02_the_offering_04_visual_lock_v3.md` (이전 archive 잔존) + `_archive_versions/02_the_offering_04_visual_lock_v4_korean.md`로 추후 archive 권장

**v33.5.4 patches (5):**
- EP13 line 1651: `She also knows the bird. The same bird is carved into the small wooden one his mother made.` → `The carved bird matches the broken stone bird above the lower-city well.` (EP46 wooden bird 사전 노출 모순 제거)
- EP13 S#2 대화 순서 재배열: `Your mother.` 발화 = Vael의 `My mother left that pin there once. I still go back.` 다음으로 이동 (Isolde 정보 추론 모순 해소)
- EP19 line 2450: `watched her killed on the street with my eight-year-old eyes watching` → `watched men beat her to death in the street while I stood there at eight years old` (영어 watch/watching 중복 제거 + 분노 직접 표현)
- EP20 line 2523: 동일 패턴 patch
- EP49: `He followed her rag.` → `He followed the route she hid for him. Kiran found the rag under the stair after the ridge took him.` (rag 명사화 해소 + route/rag 분리 명확)

**근본 인사이트 (2026-05-21 후반·외부 검토 P0 2 + P1 1):**
> 본문에 정확한 cycle 숫자를 박을 때마다 산수 모순이 반복 발생. 근본 = **발화·서술의 산수 위험 숫자 = 자연 표현으로 통째 전환.** baseline 정보 (Halren·Adeline 등 fantasy device 설명) + letter 본문 + 시적 강조 발화만 숫자 유지. 모든 상대 시점 표현 ("X cycles left·X cycles ago·X cycles wearing 등") = 자연 표현 (rest of this carry·long enough·warning 등)으로 전환.

**v33.5.3 근본 patches (6):**
- EP14 ISOLDE-VAEL 대화: "nineteen cycles left" 등 숫자 → "this is not almost over / Council. Being hunted. Carrying her."
- EP41 Sera mark 강제 cycles: "nine cycles now" → "long enough now"
- EP50 Sera hearing throat: "thirteen cycles wearing past her shame" → "the mark she has worn past her shame"
- EP50 Sera stump 묘사: "wrist burned cycle nineteen, hand taken cycle twenty-one" → "wrist burned at the warning, hand taken after she ignored it"
- EP43 Sera bandage: "cycle nineteen bandage" → "bandage from the warning"
- EP16 운영 잔향 polish: "I ran the part that needed a woman's voice. The rest is yours. I need to learn the rest." → "I ran what was mine. The rest is yours. Teach me."

**유지된 cycle 숫자 (산수 안전):**
- Halren / Adeline baseline 정보 (Twenty cycles · ten or eleven body show)
- Sera letter 본문 (cycle ten · before the eleventh cycle is out · before cycle fifteen)
- 시적 강조 발화 (After twenty cycles · Eight cycles of holding back)
- 헤더 cycle 명시 (제작 참고용)

**외부 검토 patches 추가 (2026-05-21 후반):**
- EP01 S#1 동기 보강: FLASH CUT (Corvin memory "She'll learn quiet") + Isolde VO "In a month they sell me. Tonight is mine." + Vael VO "My mother left it here. I come every year." + silver pin / broken stone bird 시각
- EP13 hairpin reveal Vael 동기 직설 (어머니·매년·"You were why I stayed")
- EP18 Aldric 증언 추가 (Adeline 직접 증인) + EP19 "Adeline heard him" / five witnesses 삭제
- EP19 유언 "first lawful wife" 삭제 → "blood and name" 인정
- EP20 crown timing 통일 ("Not from Veine. From you. When the keep asks") + EP50 "again today" + "saw her crowned at cycle eighteen"
- EP49 "He followed her rag" (기존 "carried" → "followed" 정합)
- EP32 cycle 산수 제거 ("rest of this carry")
- EP48 cousin 보안 (bait path: "leaves his marked path... following the route Sera hid")
- EP29 Female gaze (Isolde 끌어당김·Vael 따라감)
- EP50 S#3 헤더 = "Two and a Half Years Later. Spring Morning." (Mireille age 정합)
- EP10 spoken polish ("ended up in that bed")
- EP34 spoken polish ("I do not need that speech anymore")

**제작용 정본 (clean):** `07_final/02_the_offering_FINAL_v33_5_clean.md` (50 EP / 49 Hard Cut / Fade Out 1 / End 1 / Korean 0 / 메타 헤더 제거)

**Pre-patch 본 (보존):** git HEAD (commit 31be65c) — 필요 시 `git show HEAD:projects/02_the_offering/07_final/02_the_offering_FINAL_v33_5_clean.md`로 복원

**v33.5 → v33.5.1 정합 patch (2026-05-21·사용자 피드백 P0 7 + P1 4):**
- EP10 spoken English (`if I had not` → `if I didn't`)
- EP14 fantasy cycles (`twenty months` → `Dragon cycles. Halren will count them.`)
- EP20 Adeline circlet (`regent` → `queen's`) + Stepmother 처형 시점 통일 (tower tonight → Drakonis 즉시 이송)
- EP32 cousin 보안 명시 (lower yard 인질 · inner stair X · Kiran 문 표시)
- EP34 Adeline mother 발화 정정 (감정 정리형)
- EP41 Sera 처벌 단계화 (Cycle 19 = wrist burn ring · warning) ↔ EP43 (Cycle 21 = hand 절단 재범 처치)
- EP42 Veine 편지 인장 (Adeline queen seal X → 옛 high court + inner cathedral) + 4 declaration priest 칭하기 + `advised/dissolve` → `commanded/sever`
- EP48 cousin 침입 위치 (corridor → first inner stair · ridge 즉시 제압)
- EP49 / EP50 증거물 통일 (yard-rag = labor week 이전 stair rail 아래 숨김 / "Second push. Inner stair." 통일)
- 추가 정합 정정: EP35/EP39/EP42 ridge dragons 숫자 직접 표기 → `surviving ridge dragons` · EP43 "nine cycles" → "two cycles ago" · EP50 Sera 왼팔 stump 명시 (wrist 19 burn + hand 20 taken) · EP50 Volzaar mark 강제 cycles 13 (cycle 11 → cycle 24) 정합 · EP48 body location "outer wall" 정합

**작업본 (메타 포함·archive):** `_archive_versions/02_the_offering_FINAL_v33_5_working_with_meta.md`

**상태:** 🔒 **Production LOCK 완료.** 본문 변경 금지. 추후 제작팀 요청 시만 재진입.

---

## v33.5 LOCK 핵심 구조

**Engine:** 다크 로맨스 슈퍼퀸 label reversal·"뇌 끄고 보는" 도파민 비트.

- 출산 EP48-49 (Cycle 24 첫째 carry)·Fantasy device 20-cycle 드래곤 임신
- EP01-08 free arc → EP09 "She is my bride" first paid payoff
- EP14-47 임신 엔진 + label reversal (impure→bride·concubine→wife·human womb→mother of heir·not queen→queen)
- Sera = 영원 라이벌 (회개 X·EP50 nameless servant 영원 굴복)
- 빌런 회개 폐기 (Stepmother EP21 처형·Corvin EP19 reference·Sera mark 강제 유지)
- 행정·법·정치·외교 어휘 본문 0건 (`memory/feedback_vertical_no_admin_power.md` 룰)
- "I love you" 3 instances (EP16 first morning·EP46 labor eve·EP50 garden 2년 후 final)
- 둘째 hint = EP50 한 줄만 (Mireille "For the baby" + Isolde 손 belly)

**핵심 보상 비트:** EP01 거울·EP09 bride·EP13 hairpin reveal·EP24 wrist crush·EP30 사막 사냥·EP32 letter 음독·EP37 손가락 4개·EP39 crown·EP41 손 절단·EP42 letter burn + 4 declarations·EP43 강제 echo·EP48 birth·EP50 Sera 영원 servant.

---

## LOCK 후 다음 단계

| # | 작업 | 상태 |
|---|---|---|
| 1 | 본문 only clean export | ✅ 완료 (`v33_5_clean.md`) |
| 2 | 메타 갱신 | ✅ 본 파일 |
| 3 | 00_START_HERE 갱신 | ✅ 완료 |
| 4 | **비주얼 락 v4 (AIGC 인물/소품/배경 어셋·EP 매핑)** | ✅ **완료 (`02_the_offering_04_visual_lock.md` · 2026-05-21)** · 옛 v3 = `_archive_versions/02_the_offering_04_visual_lock_v3.md` |
| 5 | **원어민 polish (내가 진행 · 4,771 lines · 50 EP)** | 🔄 **다음 단계 — 사용자 명시 "원어민 polish는 니가 해야지"** |
| 6 | EP별 90초 vertical 분할표 | ❌ 사용자 X (불필요) |
| 7 | AIGC asset prompt engineering | ❌ 사용자 X (= 비주얼 락 v4로 대체) |
| 8 | 시즌 트레일러 cut list | ❌ 사용자 X (불필요) |
| 9 | 다국어 자막 번역 | ❌ 사용자 X (불필요) |

**옛 정본 archive:** `07_final/_archive_versions/` (v33.4·v33.3·v33.2·v32.2·v31.4·v31.3·v31.2·v31.1·v31 series·v30 series·v20 외 11개 옛 정본 + `v33_5_working_with_meta.md` 작업본).

---

## 🗄️ 옛 정본 history (참고용)

### v20 — Production LOCK (2026-05-19 후반·v31 시리즈 진입 전)

**정본:** `07_final/02_the_offering_FINAL_v20.md` (archive)
**상태:** 🔒 LOCKED 였으나 사용자가 v30 시리즈에서 *마스크 setup·festival 톤·임신 위치* 전면 재기획 결정.

### V20 정정 6 P0 + 2 P1 (두 피드백 동의)

**P0 (필수·완료):**
1. **EP33 공간명 통일** — `cellar / lower cellar` 5건 일괄 → `Outer Guardhouse` (피드백 1: 외벽 잡힌 자객을 cellar로 끌고 옴 = 비논리)
2. **Harrin 손 처벌 INSERT → EP08 S#1 독립 scene 승격** — Lower Hall·dawn·"You spat at her. / You sent the knife. / Left hand or both. / That's mercy. Remember whose." + breach-mark + Border outpost (피드백 2 옵션 B 권장)
3. **EP30 body inventory 정정** — "Eight crescents visible — throat, collarbone, sternum, hip, thigh" → "Eight crescents visible across the water. Vael has counted them every night for a month." (피드백 2 권장 문장)
4. **EP15/EP45 breast routing 정정** — EP15 "to the underside of her breast through the tunic" → "to her sternum through the tunic" · EP45 "from her breast back down to her belly" → "from her ribs back down to her belly"
5. **flushed throat 5건 다양화** — EP14·EP15·EP26 S#2·EP42·EP46 5건 = Vael 신체 (jaw·tendon·pulse·breath·restraint) 우선. EP10·EP26 S#1·EP33·EP43 4건 = 모티프 보존
6. **Crescent ledger 제작/검수용 표** — `02_the_offering_05_crescent_ledger.md` (V20 12 crescent + tooth print + hidden band + Isolde→Vael 표지 통합·작중 본문 ledger catalog 삽입 0건 확인)

**P1 (선택·완료):**
7. **EP24 "wear his bed" → "share his bed"** (Sera 발화·관용 자연 정정)
8. **분할 권고선 5건 전면 폐기** (사용자 명시 "안하느니만 못해") — 본문 정합 유지

### 사용자 결단 (자율 판단 적용)
- **회차 재분할 = 분할 X.** 평균 EP 652단어 = 2분 premium vertical 정합. 가장 긴 EP16 (1544단어) 분할 시 회차 번호 재배치 → 본문 EP 인용 다수 깨짐 = 위험·실효성 X. 50화 유지·premium 2분형 라인 LOCK.
- **수위 = 유지.** V14→V20 거쳐 Female gaze polish 다수 적용 (EP15/EP45 breast routing·EP31 flank·EP30 body inventory·EP46 Isolde straddle/pin/rhythm·EP43 "He waits. She pulls him closer."·flushed throat 5건 다양화·Vael 신체 (jaw·tendon·pulse·knuckles) 우선). 남성향 잔재 = 매우 약함. 변경 X.
- **75분 / 50화** = 유지.

### LOCK 후 향후 작업
- 제작팀 stamps·beat·shot list 기반 90초 vertical 분할 (분할 권고선 활용)
- AIGC 어셋 생성 prompt engineering
- 원어민 polish 최종 1회 (외부 인력 권장)

**옛 정본 archive:** `07_final/_archive_versions/` (V19·V18·V17·V17_platform_safe·V16·V15·V14·V13·V12·옛 11개·`_v12_phase_sources/`).

## 🗄️ 정본 v19 (옛 archive — 2026-05-19 후반)

**정본:** `07_final/02_the_offering_FINAL_v19.md` (단일·V18 위 종합 clean pass·두 AI 마지막 피드백 + 내 추가 인사이트 통합)

**V19 정정 8 영역 (피드백 1·2 + 내 추가):**

### Spoken English 잔존 5건
- EP01 "twelve years" → "for twelve years" (전치사 누락)
- EP01 "they don't pay for talking" → "they don't pay you to talk"
- EP16 "the sight of me in his crown" → "I'm not wearing his crown for his court to gawk at"
- EP35 "the second she's coming" → "when it happens" (직역투 정정)
- EP39 "If she costs me you" → "If I lose you because of her" (관용 어색)

### 논리 오류 3건
- EP44 산수 (10년 - 5주 = 9년 10월 3주) → V17에서 이미 외부 보고 압축 시 발화 폐기·정합 OK 확인
- EP29 보안 비논리 (외벽 잡힌 자객을 cellar로) → **Outer Guardhouse**로 정정 (5건 일괄)
- 흑염 일관성 (slow black flame 침실 난방 vs 철 녹임 모순) → 침실 fireplace = **low fire / hearth fire** 통일 (5건). Vael 마법 흑염 = 의식·전투·iron plate·dagger melt 한정 보존

### Female Gaze EP31·EP45
- EP31 "underside of her left breast" → "side of her ribs" 또는 "flank" 우회
- EP31 "Slow tracking down her body" → Vael jaw·restraint·tendon·hand 우선
- EP45 "over her breasts under the water" / "breast to belly to hip" → "belly → ribs → back to belly" / Vael 신체 우선
- 부위 카탈로그 → 시선 우선화

### EP10 crescent 표기 모순
- "Five crescents — three under the jaw, fifth on the collarbone, sixth on the sternum, fourth hidden on the sternum" (6번 EP10 직전 set X·모순) → "Five crescents on her — three under the jaw, the hidden one on her sternum, and the fifth at the side of her neck Vael set the night before."

### 회수 부재 (Harrin·Midwife)
- EP08 Vael "Take him to the lower hall. ... Tomorrow." 약속 회수 → 짧은 [INSERT] 비트 추가 (lower hall·다음 dawn·Vael 손바닥·Harrin 손등 mark·3초)
- EP22 Midwife 사전 빌드업 → Kiran 통한 한 줄 ("The south-coast midwife arrived at the south wing last night. The one your lady's mother's house sent ahead.")

### EP30-37 영상 리듬 보강
- EP32 = MONTAGE (4 nights compressed) + VO + INSERT (Kiran 트레이) 추가 — 불면 반복 비트 1 montage로 흡수

### Male Gaze 카메라 균형 (EP03)
- "Her hair on the pillow / The three crescents on her throat" body close-up → Vael 신체 (jaw tendon·restraint·scaled knuckles white pinning) 우선 + Isolde 부분 보존

### 에피소드 분할 = 제작 단계 결정 영역 (메타 명시)
- 두 피드백 모두 EP01·EP03·EP04·EP16·EP18·EP39·EP46 분할 권장 (90초 vertical 기준 60-70화)
- V19 본문 = 단일 통합 유지 (분할 시 본문 EP 다수 인용·참조 깨짐 위험)
- **제작 단계 결정:** 영상 제작팀이 stamps·beat·shot list 기반 90초 vertical로 재분절. 본 V19 = 서사·정합 단위 master.

**옛 정본 archive:** `07_final/_archive_versions/` (V18·V17·V17_platform_safe·V16·V15·V14·V13·V12·옛 11개·`_v12_phase_sources/`).

## 🗄️ 정본 v18 (옛 archive — 2026-05-19 후반)

**정본:** `07_final/02_the_offering_FINAL_v18.md` (단 1개·V17 + V17_platform_safe 통합·Isolde agency 보강·영상 제작·AIGC 어셋 즉시 사용 가능)

**v18 = platform-safe 기반 + Isolde agency 보강 통합본:**

### 두 AI 피드백 통합
- 피드백 1 (V17/Safe 종합): Safe 채택·EP03·EP43·EP46 Isolde agency 2-3곳 복구 권장
- 피드백 2 (GREENLIT): Platform_Safe 채택·EP46 straddle·pin·rhythm 강화 권장

### V18 정정 3건 (피드백 1·2 통합)
- **EP03:** `Her free hand comes up off the sheet and locks in his hair at the back of his head — pulling him closer to her mouth.` 복구 (agency)
- **EP43:** `He waits. He does not move his weight onto her yet. She closes her arms around his back and pulls him closer. Only then does he cover her body with his.` (restraint·choice)
- **EP46:** `She straddles his hips. Both palms flat on his chest, pinning him down — scales under her hands, his heart against her right palm. She sets the pace. He does not take it from her. He lets his hands rest on her hips — flat, fingers spread, yielding. He lets her have it.` + `She sets the rhythm. He follows. He lets her.` (피드백 2 권장 straddle·pin·rhythm·yield 통합)

### V17 + V17_platform_safe → archive
- 두 파일 모두 `_archive_versions/` 이동
- 단일본 V18 유지 (사용자 결정)
- OSMU 필요 시 archive에서 V17 master 복원 가능

### 시스템 이원화 baseline 완화
- `feedback_master_platform_safe_dual_version.md` 정정: 이원화 = 옵션·작품별 사용자 결정. 단일본 + agency 보강 = production-ready 가능 명시.

**옛 정본 archive:** `07_final/_archive_versions/` (V17·V17_platform_safe·V16·V15·V14·V13·V12·옛 11개·`_v12_phase_sources/`).

## 🗄️ 정본 v17 (옛 archive — 2026-05-19 후반)

**정본 (2 파일·이원화 강제):**
- `07_final/02_the_offering_FINAL_v17.md` — master version (high-heat 보존·내부 baseline·다음 작품 학습)
- `07_final/02_the_offering_FINAL_v17_platform_safe.md` — platform-safe (영상화·플랫폼 송출용·body mechanics 우회)

**v17 정정 (피드백 1·2 통합·근본 문제 해결):**

### 시스템 v3.1 근본 정정 (집필 컨텍스트 위·다음 작품에도 적용)
- **EP 양식 v3 5블록 신설:** MONTAGE / VO / FLASHBACK / INSERT-CUTAWAY / INTERCUT (`config/hard_rules.md` 1번 룰 정정·`feedback_screen_rhythm_v3_blocks.md` baseline)
- **Female gaze baseline:** 부위 순회 tracking 금지·시선 우선화 (Vael 통제·forearm·Isolde agency·breath·firelight). `feedback_female_gaze_camera_polish.md`
- **Master + platform-safe 이원화 baseline:** 초고수위 작품 강제 이원화. `feedback_master_platform_safe_dual_version.md`
- **Spoken English 원어민 polish baseline:** 5단어 강제 신화 부정·5-10 단어 자연 default. `feedback_spoken_english_native_polish.md`
- **MEMORY.md 갱신** (호출 트리거 baseline 4개 추가)

### V17 본문 정정 (V16 위)
- **Spoken English 8건 정정:** EP07·EP08·EP16(2건)·EP17·EP20·EP31·EP39 (피드백 1 P0 ALL)
- **영상 리듬 4 핵심 위치 삽입:**
  - EP04 EP01 chain FLASHBACK (wrist 닦는 비트와 연결)
  - EP30 임신 build MONTAGE (10비트) + Isolde VO + Aldric letter INSERT
  - EP33 자객 처리 INTERCUT (cellar·chamber cross-cut)
  - EP48 EP05 road choice FLASHBACK (love confession 직전)
- **Female gaze 부위 반복 정정:**
  - EP28·EP43 mark ledger 카탈로그 명단 → 의미 우선 (`he knows each one by feel`)
  - EP34 ledger 명단 → hidden ones under cloth 우회
  - inner thigh = 결합 비트 위치 묘사만 (한도 내)·under breast = 1회 한도

### Platform-safe 별도 파일 정정
- EP03·EP21·EP43·EP10 결합 비트 → [CUTAWAY] 블록으로 우회 (firelight·sheet·hand·scale·breath·hair·crescent shift)
- EP46 Isolde on top → 명시적 자세 우회·face·hand·scale·breath 우선
- Master 정체성·Isolde agency·Vael 통제 상실·결합 함의 모두 유지

**옛 정본 archive:** `07_final/_archive_versions/` (v16·v15·v14·v13·v12·옛 11개·`_v12_phase_sources/`).

## 🗄️ 정본 v16 (옛 archive — 2026-05-19 후반)

**정본 위치:** `07_final/02_the_offering_FINAL_v16.md` (4,477 lines·V15 위 11건 정정·Korean 0·Hard Cut 49·EP50 Fade Out·블록 일관·자동 검증 16/16 ✅)

**V16 정정 (피드백 1·2 통합 + 내 추가):**
1. Mark Ledger 4번 통일 — "shoulder blade" carry over 5건 → "fourth hidden on the sternum" 일괄 정정 (피드백 2 P0)
2. EP21 6번 mark 위치 명시 — "lower sternum, below the fourth, between the lower ribs" (4번·6번 위치 차이 명확화)
3. Vael 잔존 발화 압축 — EP22·EP42 시적 잔존 (피드백 2 P1)
4. Vael trauma 후속 회수 3건 — EP18 dragon ("The scale under her cheek settles") / EP33 자객 후 cellar / EP39 출산 midwife (다른 사람 접촉 시 scales 반응·Isolde 손 settle)
5. EP42 cradle iron 회수 — EP01 chain 녹여 forge·"the same black iron from the chain that bound Isolde's wrists in EP01" (피드백 1 제안·정합 강함)
6. EP03·EP21 platform-safe 우회 — 직접 body mechanics → firelight·sheet·wrist·hair·breath cutaway (피드백 2 P0·master version 일부 유지)
7. EP14·EP21·EP43 Isolde agency — 그녀가 mark 위치 직접 지정 ("She takes his hand"·"She presses two of her fingers"·"She lifts her hand from his hair") (이전 turn 미룬 결함 정정)
8. EP44 외부 보고 4개 발화 → 3개 압축 (피드백 2 P1·"keep has not opened"·"southern houses 10 years" 반복 제거)

**옛 정본 archive:** `07_final/_archive_versions/` (v15·v14·v13·v12 + `_v12_phase_sources/` + 옛 11개).

## 🗄️ 정본 v15 (옛 archive — 2026-05-19 후반)

**정본 위치:** `07_final/02_the_offering_FINAL_v15.md` (V14 위 직접 정정·Korean 0건·Hard Cut 49·EP50 Fade Out 유지)

**v15 정정 (다른 AI V14 피드백 + 내 객관 추가):**
- **시스템 v3 개편 (집필 컨텍스트 위)** — CLAUDE.md 596줄→80줄·MEMORY.md always-load 17→3개·`config/hard_rules.md` 신규·`prompts/phase_4` raw script 룰 정정 (옛 "첫 1-2 씬만 Read" 폐기→매칭 히트작 3-5 EP raw + 이전 EP 3개 raw 강제)
- **spoken English clean pass** — 다른 AI 지적 4 위치 정정:
  - EP07 "She speaks for me. She names. I give the hand. She says no. No holds." → "She speaks for me. Her no holds. Her names cost hands."
  - EP07 "Because if I read them my father is bigger in this room than you." → "If I read them, he wins the room. He doesn't."
  - EP08 "My lords saw a woman at my table today..." → "My lords saw you. At my table. They asked you. Not me."
  - EP05 "Your father knew what he sent you to..." → "He knew. Harrin knew. Still they sent you."
- **중첩 사슬화** — EP29 자객·EP33 자객 = "Cousins of the cellar rider. They saw his mark on the cousin's door. They came anyway." = 같은 가문 사슬·재점화 cadence 명시 (다른 AI "중첩 작동" 평가 정합 강화)
- **AIGC 위험 잔존 정정** — EP29 단검 구부리기 → black fire melt (EP03와 일관성)
- **Vael trauma 메커니즘 후속 회수** — EP17 "Her own hands come down on top of his — over the scales. The scales on the back of his hands settle flat under her palms." / EP29 "The scales under her hands — still raised from the cellar wall — slide back flat under her palms." = EP04 도입 비트 사슬 연결
- **외부 상태 보고 압축** — EP34 외부 명단 4개 (midwife·my father·Sera·Harrin) → 2개 (midwife·my father) 압축
- **Vael 긴 발화 정정** — EP33 "I'm closing the dressing chamber..." → "Closing the dressing chamber. The laundry. Every door to the south wall. Food, linen, midwife — through Kiran only." / "I will until she is born and then..." → "Until she's born. Then until she walks. Then until she's grown."
- **Mark Ledger 정합 정정** — 옛 V13 ledger 4번 = 어깨 blade 잘못. V15 본문 정합 = 4번 = sternum hidden ("hers and his and no one else's"). ledger 정정 (`02_the_offering_06_v14_deliverables.md`)

**옛 정본 archive:** `07_final/_archive_versions/02_the_offering_FINAL_v14.md` + V13·V12·`_v12_phase_sources/` + 옛 11개.

**중복 vs 중첩 판정 (다른 AI + 내 객관):**
- ✅ 중첩 (유지): 임신 build·표지 누적·문 잠금·belly touch·과보호·chamber 반복·Sera 재등장·둘째 임신·Vael 불면·midwife 통제
- ⚠️ 중복 (V15 일부 압축): 외부 명단 보고 (EP34 일부 압축) / EP29-33 자객 사슬 = 중첩 사슬화 OK
- 옴니버스 X (V12 phase에서 이미 정정): EP27 throne hall southern houses·EP31·37 외부 처리 → 둘만의 사적 비트로 재구성됨

## 🗄️ 정본 v14 (옛 archive — 2026-05-19 후반)

**정본 위치:** `07_final/02_the_offering_FINAL_v14.md` (V13 위 직접 정정·Korean 0건·Hard Cut 49·EP50 Fade Out 유지)

**v14 정정 내용 (V13 + 사용자 시스템·작품 통합 피드백):**
- **Vael 시적·긴 발화 16+ 위치 정정 → spoken English ≤5단어 default** (산출물 06 참조)
  - EP01 "Little offering" → "Up." / "You walked through my gate. The yet is short." → "You're inside the gate."
  - EP05 long terrace monologue 분할
  - EP08 "You are not anyone else's anything." → "You're mine. No one else's."
  - EP10·14·16·21·22·28·29·39 등 시적·긴 발화 일괄 정정
- **EP04 Vael trauma 메커니즘 비트 신규** — 다른 사람 접촉 시도 → 본능적 폭발 (door shudder) / Isolde 손 = scales 가라앉음. 설명 대사 X·행동만 (危険な甘い檻 baseline).
- 12 Mark Ledger 재정비 (산출물 06 참조)
- 산출물 5 통합 등재 (`02_the_offering_06_v14_deliverables.md`)

**V14 라운드 2 / V15 권장 (사용자 결정 영역):**
- 후반부 정치 압축 (EP27 throne hall southern houses 폐기·EP31·34·37 외부 처리 1 줄로)
- Isolde agency beat 매 EP 1개+ 추가 (선택 행동: 먼저 손 뻗음·mark 위치 지정·문/열쇠 처리·Vael 멈춤/부추김)
- Vael trauma 메커니즘 후속 EP 회수 (EP12·EP17·EP18·EP31·EP33)
- **시스템 토큰 회계 개혁** — 사용자 진단: CLAUDE.md 596줄·메모리 always-load 17개·메타 산문 95% / raw drama 0.5% = 본문 톤 침투 근본 원인. CLAUDE.md 100줄·메모리 2-3개·hit script 3-5 EP raw 주입·이전 EP 3개 raw 주입 권장 (별도 시스템 작업)

**옛 정본 archive:** `07_final/_archive_versions/02_the_offering_FINAL_v13.md` + `_v12_phase_sources/` + V12·옛 11개.

## 🗄️ 정본 v13 (옛 archive — 2026-05-19 후반)

**정본 위치:** `07_final/02_the_offering_FINAL_v13.md` (4,460 lines·UTF-8 no BOM·Korean 0건·Hard Cut 49·EP50 Fade Out·블록 양식 v2 일관)

**v13 정정 내용 (V12 통합 피드백 반영):**
- EP01 Isolde 나이 SUPER "ISOLDE — 23" 추가·EP12·EP13 Aldric 대사 "You were eight when she died. You are twenty-three now. I stayed silent for fifteen years." (8+15=23 산술 명시)
- EP10 본문 전체 교체 (옛 Aldric box/letter 중복 사고 폐기 → Aldric 도착 전 새벽·둘만의 사적 불안·6번/7번 crescent·Isolde가 처음 Vael에게 표지 setting·초고수위 결합 비트)
- EP14 Aldric 질투 정정 (father-sexualization 비트 "his hand thought about you"·"he'll know it under his shirt"·Aldric 자기 가슴 손 폐기 → 소유권 분노 "He wrote your name like he still had the right.")
- EP20 Sera pregnancy recognition = Vael wing curve 무의식 보호 반응으로 인지 (옛 작위적 손 위치/배 각도 폐기)
- AIGC 위험 컷 6 정정 (strap snap→cut-away·dagger bending→black fire 녹임·lacing fingers→palm-over-hand·eighty heads bow→silhouette+representative close-up·tiny fist→scaled palm over swaddle)
- EP03·EP21·EP43·EP46 초고수위 결합 비트 4 씬 추가 (명시적 자세·신체 결합·감각 3축)
- EP46 둘째 임신 = Isolde 주도권 강화 B안 ("I waited. Long enough for me."·Isolde top position·자발 결정)

**시스템 v2.5 baseline 등재 (다른 작품 적용):**
- `feedback_dark_romance_v2_5_v13_lessons.md` (V12→V13 lessons·수위·father-sexualization·AIGC 위험 컷·후반부 압축·Crescent ledger·Sera body reaction)
- `feedback_dangerous_sweet_cage_insights.md` (BL captive 히트작 baseline·시적 톤 0·1-3 단어·양자택일 페이월·표지 12 다양·시그니처 소품 회수·trauma 메커니즘)
- `02_the_offering_05_crescent_ledger_v13.md` (12 crescent + tooth print + hidden band 위치·EP·기능·공개/숨김 명시)

**V14 검토 권장 (危険な甘い檻 baseline 적용·사용자 결정):**
- P0: Vael 발화 80% ≤5단어 (V13 시적 톤 잔존 정정)·EP8 양자택일 페이월·표지 12 다양화 (crescent 1개 + 11 추가 비트)·후반부 EP35-42 정치 ≤2 EP 압축·Isolde 매 화 반격 1개+
- P1: EP41-42 "함께 망하자" 비트·Vael trauma → 이졸데만 만질 수 있음·시그니처 소품 EP1·중반·EP50 3회 회수·EP32 sensory 통제 응용
- P2: 외부 관찰자 인증 시퀀스·EP18 다리 비트류 공공 통제

**옛 정본 archive:** `07_final/_archive_versions/02_the_offering_FINAL_v12.md` + `_v12_phase_sources/` + 옛 11개.

## 🗄️ 정본 v12 (옛 archive — 2026-05-19 후반)

**정본 위치:** `07_final/02_the_offering_FINAL_v12.md` (4,385 lines·UTF-8 no BOM·Korean 0건·Hard Cut 49·EP50 Fade Out·블록 양식 v2 일관)

**v12 핵심 정정:**
- v2.3 (`feedback_dark_romance_relationship_centered_v2_3.md`): 둘의 관계 70% / 외부 적 30%. 옛 v11 = "복수극의 탈을 쓴 로맨스" → v12 = 둘만의 사적 관계 사건 중심.
- v2.4 (`feedback_dark_romance_high_explicit_4_prescriptions.md`): 이졸데 23·표지 다양화 (12 crescent + tooth print·hidden band)·임신 Breeding/Overprotective·후반부 정치 완전 소거 (EP30+ 사적 공간 ≥80%).
- 청사진 v6 정합 (`02_the_offering_04_blueprint_v6.md`).
- EP12 이졸데 나이 22→23 정정 (Aldric "eleven years after that").
- EP04 Wall of Black Fire 폐기 / EP07 priest·하루글래스 폐기 / EP08 Servant Pretender Declaration 폐기 / EP09 Harrin 손가락 부러뜨림 폐기 / EP16 dais·gold circlet stacked 폐기 / EP19 stepmother execution 짧음 / EP32 Elara·EP34 Aldric letter·EP36 Harrin 무릎·EP41 throne hall ceremony·옛 후반부 정치 처리 다 폐기 → 둘만의 침실·욕실·밀실·정원으로.
- EP40 출산 = Vael 광기 보존 ("I would burn this room. I would burn the world if she was the cost of you.") + 산파 통제.
- EP48 첫 "I love you" / EP50 둘째 출산 후 inner garden HEA + Vael "Da" 인지.

**옛 정본 archive:** `07_final/_archive_versions/02_the_offering_FINAL_v11.md` + `07_final/_archive_versions/_v12_phase_sources/` (phase1-6 작업 파일 6개) + 옛 11개.

**v3 진단 + 시스템 v2 재설계 적용 정본:**
- 청사진 v5 (압력축 = "Vael의 선택·heir vessel 확정"·옛 v4 자리 회수 1축 폐기)
- EP21-43 전면 재집필 (Sera 도착·yield·임신 build·자객·Harrin 굴복·출산)
- EP44-50 사후·HEA 재집필 (첫 "I love you"·dragon 가문 인사·Aldric 사망·둘째 임신·HEA 자연 엔딩)
- EP01-20 부분 정정 유지 (시스템 v2 흡수 보고서·v3 진단 baseline)

**자동 검증 (정본 v11):**
- 3,206줄 / EP 헤더 50 / Hard Cut 49 / Fade Out 1 / End 1 / Korean 0건
- Far-east ships 0건 / council seat·water rights·iron mines·neutral seat 0건
- 블록 양식 v2 일관 (V 158·C 69·D 139·G·H 65)

**시스템 v2 재설계 적용 baseline:**
- v3 진단 10 자가 검수 통과
- Demon Lord 9 함정 회피
- 흡수 보고서 작성 후 재집필 (`00_immersion_report_v5_rewrite.md`)
- 청사진 v5 정합 (`02_the_offering_04_blueprint_v5.md`)

**옛 archive:**
- `_archived_ep21_43_v5_rewrite_source.md` (재집필 본문 임시 파일)
- `_archived_ep44_50_v5_rewrite_source.md` (재집필 본문 임시 파일)
- `02_the_offering_04_blueprint_v4_deprecated.md` (자리 회수 1축·정치극 후반)
- `07_final/02_the_offering_FINAL_v9_deprecated.md` (옛 v9 12 결함)

## 🚨 정본 v10 결함 진단 + 부분 정정 (2026-05-19 후반 — v3 진단 통합 보고서·v11로 대체됨)

**사용자 직접 진단 (2026-05-19 후반):** "offering은 수많은 검토과정을 통해 최종고를 냈음에도 불구하고 심각한 결함 투성이다. 근본적인 문제가 해결되어야한다."

**근본 진단 (v3 통합 보고서):** OFFERING 후반 = Demon Lord 실패 패턴 그대로 복제 (시스템물·정치물·능력물). **장르 정체성 오인 = 여성 독립 권력 획득물·복수극·정치 판타지로 변질.**

**시스템 baseline 등재:** `feedback_dark_romantasy_paid_vertical_v3_diagnosis.md` (모든 다크 로맨타지 paid vertical 작품 절대 baseline).

**청사진 갱신:**
- 옛 v4 = `02_the_offering_04_blueprint_v4_deprecated.md` (자리 회수 1축·정치극 후반)
- 새 v5 = `02_the_offering_04_blueprint_v5.md` (mate·heir 확정 1축·로맨스 후반)

**본문 부분 정정 (핵심 v3 위반 4건):**
- ✅ EP44 council water rights·iron mines → 사적 침실 임신 build
- ✅ EP46 far-east ships → 사적 inner ring + Vael 과보호 + Veine 자객 시도
- ✅ EP48 Sera 친구 (neutral seat) → throne hall Sera 공개 굴복
- ✅ EP50 "She'll sit both thrones" (queen title 보상) → "His bride. His mate. Mother of his heir." (mate·heir 보상)
- ❌ EP21-43 본문 (자리 회수·정치·전쟁·Aldric 처단·Sera 처단·Dragon Queen 즉위) = v5 청사진과 미정합 → **전면 재집필 필요 (사용자 결정 영역)**

**자동 검증 (정정 후):**
- 3,472줄 / EP 헤더 50 / Hard Cut 49 / Fade Out 1 / Korean 0 / Far-east ships 0건
- 잔존: council 8건·neutral seat 3건 (EP26-43 정치 본문 잔존)

## 🎯 정본 v10 LOCK (2026-05-19 오전 — 청사진 v4 / Round 2 + 4-Gate 통과)

**현재 정본:** `07_final/02_the_offering_FINAL.md` (3,476줄·50 EP·Korean 0·Hard Cut 49·Fade Out 1·EP50 자연 엔딩)

**진행 단계:**
- [x] 청사진 v4 전면 재설계
- [x] EP01-50 신규 집필 (옛 v9 폐기)
- [x] 자동 검증 PASS
- [x] **Round 1 풀 페르소나 검토 (8 페르소나 01-07 + 09 병렬)** — 총 21 🔴 + 65+ 🟡 발견 / 만장일치 PATCH THEN LOCK
- [x] **Round 1 패치 적용 23건** (시적 라인·작가 직술·환경 진동·Vael 절제·정사 진입·anaphora·메타 자기언급·Coronation 변형 10·EP47 후회톤·EP08 페이월 단일 약속·동선 점프 등)
- [x] **Round 2 ripple 검증 (4 페르소나 04·05·06·07)** — 잔존 7 🔴 + 23 🟡 발견
- [x] **Round 2 추가 패치 5건** (EP09 Vael anaphora·EP10 Aldric V.O. 시적·EP12 Aldric anaphora 잔존·EP09 Harrin 추상·EP42 Vael 포식자 baseline 위반)
- [x] **4-Gate 자체 평가:** Structure ✅ / Narrative ✅ / Script ✅ (조건부) / Production ✅
- [x] **LOCK 확정** (본문 자체) — `06_reviews/02_the_offering_4gate_final.md`

**잔존 결함 (사용자 인지·다음 작업 반영):**
- 히트작 대본 직접 정독 미수행 (시스템 1순위 룰 위반·CLAUDE.md `config/vertical_drama_hit_scripts/`)
- 패턴 모델링·매칭 장르 사고에 그침·실제 작품 흡수 X (사용자 핵심 지적 2026-05-19)
- 비주얼 락 환류 영역 (펜던트 위치·Vael 변신 단계·거대 흑룡 크기·변형 4·5·6·7 sub-variant·신규 인물 등재) — 사용자 결정 영역

**검토 보고서:**
- Round 1 종합: `06_reviews/round1/02_the_offering_review_round1_consolidated.md`
- 4-Gate 최종: `06_reviews/02_the_offering_4gate_final.md`

**잔존 결함 (사용자 인지·다음 작업 반영):**
- 히트작 대본 직접 정독 미수행 (시스템 1순위 룰 위반·CLAUDE.md `config/vertical_drama_hit_scripts/`)
- 패턴 추출·매칭 장르 모델링에 그침·실제 작품 흡수 X (사용자 핵심 지적 2026-05-19)
- 5개 한국·중국 히트작 분석 권장사항 일부만 적용

---

## 🚨 정본 v9 폐기 (2026-05-19 — 청사진 v4 전면 재설계)

**사용자 지시 (2026-05-19):** "1-10을 잠금 이지랄하고있네. 점검 안하냐. 수준 개떨어진다. 청사진단계부터 재점검해서 진행."

**옛 정본 v9 (`07_final/02_the_offering_FINAL.md`) = 결함 다중 폐기 / 역사 보존 (집필 baseline X):**

| # | 결함 | 위반 룰 |
|---|---|---|
| 1 | 시적·연극톤·작가 명문장 11+건 | `no-theater-tone` |
| 2 | 작가 시점 직술 4+건 ("He is a column of shadow" 류) | `ai-cinematic-trap` 2.7 |
| 3 | 환경 진동·신화 상징 누적 5+건 ("mountains breathing" 류) | `ai-cinematic-trap` |
| 4 | EP10 정보 폭격 5개 동시 (Aldric+Sera+두 펜던트+Unburied Line+"my daughter") | Sealed Bride F1 동일 함정 |
| 5 | 압력축 분산 6축 | `pressure-axis-stacking` |
| 6 | Vael 절제 표지 5+건 ("I will not collect tonight" 류) | `dark-romance-male-predator` |
| 7 | Isolde 1화 counter 3턴 과다 | `female-lead-rise-arc` |
| 8 | EP8 페이월 사건 진행 중 ("Yours" 이미 발화) | `paywall-promise-structure` |
| 9 | Harrin 5-8턴 모욕 EP04-05 부재 | `concrete-villain-humiliation-loop` |
| 10 | 감정 보상 EP09 (무료) 노출 | `dark-romantasy-intimacy-promise` |
| 11 | 거대 VFX 누적 | `fantasy-massive-vfx-scale` |
| 12 | V.O. 남용 다수 | `vo-flashback-pressure-tools` |

**현재 baseline:**
- 새 청사진 = `02_the_offering_04_blueprint_v4.md` (2026-05-19 전면 재설계)
- 새 정본 (집필 중) = `07_final/02_the_offering_FINAL.md` — **v9 폐기 후 신규 EP01-50 집필 진행**
- 옛 정본 v9 = `07_final/02_the_offering_FINAL_v9_deprecated.md`로 archive (집필 baseline X)

**옛 정본 잠금 표기 (2026-05-17) — 폐기 확정:**
~~정본 파일: `07_final/02_the_offering_FINAL.md` (옛 v9 = Conversion Runway — 정본 잠금 완료)~~

### 정본 v9 핵심 (체질 개선 v3)

**시스템:**
- **Conversion Runway** EP01-EP10 한 호흡 (옛 EP1-8 무료 분리 폐기)
- **EP08 = paywall cut** (완결 X / 끊는 지점)
- **EP09 = 즉시 보상** (집필 출발점)
- **EP10 = 더 큰 미지급 부채** (2차 페이월 향한 설계)

**캐릭터 캐논 (정정):**
- **HARRIN (이복오빠) = 메인 빌런 1명** (얼굴·이름·5-8턴 모욕·끝까지 가치 모름)
- **Queen Mireille (Isolde 친모 사망) / Queen (Harrin's mother·Isolde's stepmother) = 살아 있음 통일**
- **Aldric 왕 = 살아 있음** (1화 "Our parents died" 정합 정정 → "You fed me after my mother died")
- **Haldren = EP01·EP02 짧은 등장 심기** (EP06 자발 충성 전환)
- **Vael = 멈추지 못하는 포식자** (절제 X·짐승 직진·끈 풀어버림·연달아 mark)
- **Isolde = 1화 처절 + 반항 + 무시 받음** (완성형 X·무력 매달림 X)

**시그니처 호칭 3단계 진화:**
- "Little offering" (EP01-EP03)
- "Mine" (EP05-EP08)
- "My bride" (EP09-EP10 정식 발화·반복)

**정보 비대칭 2 차원:**
- 시청자 vs HARRIN/Aldric (정체·계약·산맥 = 드래곤 군단·진짜 핏줄)
- **시청자 vs 두 주인공 마음** (V.O. 10건 누설·둘은 서로 모름·"I love you" 0건 유예)

**거대 VFX 자연 흐름:**
- EP01 wing-shadow + Black Gates 자체 열림
- EP03 탑 전체 불 꺼짐·자객 손목 꺾기
- EP04 Wall of Black Fire 300ft·황무지 갈라짐
- EP07 ridge breathing 20+ wing-shapes
- **EP08 산맥 = 드래곤 군단 일제 일어남·sonic boom·12 기마 밀림·등 뒤 거대 wing 환영** (페이월 정점)
- EP09 breach-mark burn (HARRIN 손등)
- EP10 pendant click·Volzaar 깨어남

**최종 검증 (모두 PASS):**
- Korean 0 / Hard Cut 10 / EP 헤더 10 / 양식 v2 위반 0건 / I love you 0건 / V.O. 10건 / 시그니처 호칭 진화 정합 / Yours 3건 (EP08·EP09 한정)
- 분량 9,918 단어 / 1,245 줄 (미국 영어 vertical 정합)

### 옛 v3-v8 (폐기·역사 기록 유지)

- `02_the_offering_FINAL_FREE.md`·`v2`·`v2_dev`·`v3`·`v4`·`v5`·`v6`·`v7`·`v8` = **옛 시스템 산출물·시네마틱 함정·정본 X**
- Demon Lord 9 함정 다수 위반·EP1-8 완결 블록 구조 (Conversion Runway 위반)
- 옛 청사진 (`02_the_offering_04_blueprint_full.md`) = 역사 기록·집필 baseline X
- 새 청사진 = `02_the_offering_04_blueprint_v3_conversion_runway.md`

### 다음 단계
- EP11+ 유료회차 집필 (체질 개선 v3 — Conversion Runway 다음 단계·결제 루프 2-4)
- 또는 신규 작품 시작 (체질 개선 v3 baseline 처음부터)

---

## 옛 진행 기록 (역사·집필 baseline X)

**옛 상태 (2026-05-17 — v3-v8 진행 — 모두 폐기):** **무료 EP1-8 v4 patch 완료 (`FINAL_FREE_v4.md` 1,276줄·다크 로맨타지 intimacy 유예 + Vael 보호 동기 거부·거래/이용 정당화 + Isolde 생존·귀환 거부 / EP8 페이월 사이다 80%+충격 텐션 20% 재설계).**

**v4 핵심 정정:**
- 다크 로맨타지 intimacy 유예 룰 적용 (몸 가까움 유지 / 감정 합의 0건 / "I want you" "I love" "fate" "destiny" 0건)
- Vael "보호자" 동기 명시 거부 → 거래·이용·소유 정당화
- Isolde "If I go back without your mouth on me, they marry me off to the next altar by sundown" 류 생존·귀환 거부
- EP8 페이월: "Yours" 직후 키스 역방향 (감정 합의 거부 시그널) + "The show is finished. Clear the hall" + "Up the stair. My chamber. Not yours" + Stair throat measure + "I am not gentle on a stair you walked up of your own feet" + Hard Cut (암전 X)
- 좋은 긴 대사 3 패턴 활용 (사실 나열·조건부 허락·최후통첩)
- 9화 결제 동기 = "옷 한 겹 안에서 무엇을 하는가"

**버전 흐름:** v2_dev → v3 → v4 → v5 → v6 → **v7 (연극톤 cadence·formal 어휘 정리 + 4 레버 정합 + 잠금 후보)**.

**v7 핵심 정정 (vs v6):**
- formal 어휘 → 자연 contraction (I am not → I'm not / I will not → I won't / I do not → I don't / They will not → They won't)
- Parallel·triplet cadence 해소 (`Not for X. Not for Y. Not Z.` 류 정리)
- 시적 punchline 2개만 유지 (1-2/50 한도): EP2 `I'm not choosing. I'm taking. This seat is mine.` + EP3 `Drop it. Only I leave a mark here.`
- EP7 브릿지 청각 보강 (`Bring the grey one to my courtyard by sundown. Hand still on his arm. He's reading it out loud himself.`)

**4 레버 검증 (모두 PASS):**
- L1 서사 빠르게·감정 유예 (유료 EP9+ 약속)
- L2 9:16 물리 + 브릿지 청각 8/8 EP (멀티태스킹 정합)
- L3 저급 dirty talk 0 / 군주·괴물 통제 언어 유지
- L4 Isolde 취약·독기 모순 EP3·5·8 정합

**LOCKABLE 정본:** 시적·연극톤 ≤2 (한도 내), 양아치 0, Isolde 시각화 정합, 브릿지 청각 8/8, 청사진·비주얼 락·heat ladder 무손상.

**v6 검증 PASS:**
- Korean 0 / Hard Cut 8 / 양식 v2 / 파일 purity
- 시적 8 패턴 ≤2 (정체성 1회만: `I do not choose. I take. This chair is taken.`)
- count 어휘 ≤3 / 정치 축 = 압박만 / EP8 외부 ≤50%
- 브릿지 직관 청각 6+ 구간 (멀티태스킹 시청자)
- Isolde 취약 저항: EP3·EP5·EP8 (`Please don't` / `You're cruel`)
- 청사진 락·Physical heat ladder 무손상

**이전 (2026-05-16):** Lite Protocol v1 fresh 재작성 → G v2 디벨롭 (FINAL_FREE_v2_dev.md) → 청사진 v2 환류 (Soft Lock 갱신·Hard Lock 유지) | 옛 G FINAL_FREE_v2.md = 이전 버전·참고 자료.

**2026-05-16 비주얼 락 v3 — voice 한 줄 등재 (Vael·Isolde·Haldren·Kiran·Elara·Grey Envoy·Aldric).**

**2026-05-16 환류 적용 (Soft Lock):** 캐릭터 캐논 (Isolde counter 정체성·pendant·Vael 신체 baseline·voice·EP3 명대사·Haldren 충성 전환 가속·신규 인물 GREY ENVOY·Kiran·Elara 보강) / 결제 엔진 매핑 (5.5·5.2·3.6 메인 + 5.4·5.10 보조) / 6 conversion 패턴 매핑 / 시청자 심리 baseline / Ladder 7 단계 명시 / EP1-8 화별 락 + sensual 락 정밀화 / Aldric 음모 5번 분산 / pendant·twin crescents·wide pearl band·ridge breathing·black-wax sigil 등 비주얼 어셋 11개 추가 / 손목 long trace 절삭 / 의상 1차 변경 (검은 모피+핏빛 → 흰 모피+아이보리) / 색 팔레트 보강 / 환류 로그 v2 등재. **Hard Lock 유지 — 정체성·페이월 구조·메인 결제 트리거 변경 X.**

**백업:** `02_the_offering_04_blueprint_full_pre_v2_dev_backup.md` (v2 환류 전 v3 청사진 상태 보존).

### 적용 baseline (모든 청사진·집필 단계 — 2026-05-16 강제)
- `feedback_paid_vertical_viewer_psychology.md` (시청자 심리·욕망+해소 부끄러움)
- `feedback_paid_vertical_6_conversion_patterns.md` (메인 1-2 + 보조 1-2 매핑)
- `feedback_female_buy_engine_relational.md` (**OFFERING = A 엔진 — 다크 로맨타지+alpha**)
- `feedback_50_episode_serial_engines.md` (7 룰)
- `feedback_character_situation_appeal.md` (3축)
- `feedback_paid_vertical_intuitive_money_triggers.md` (G 7 버전 분석)
- `feedback_female_lead_agency_balance.md` (강한 여주 회피 X / 판결형만 회피)

### 옛 상태 (보존 — 비교 자료): (`premium_pilot_lite/` + `07_final/02_the_offering_FINAL_FREE_v2.md` 1,062줄 / Korean 0 / Hard Cut 8 / 양식 v2 / 33 씬 / 분량 약 17.9분). 다크 로맨타지 6 사이클 + mutual claim 곡선 + 수위 결제 엔진 + EP8 페이월 응축.

옛 산출물 (`premium_pilot/`·`premium_pilot_v2/`·`version_b/c/d/e/`) = 보존 (비교 자료). 유료 EP9-50 = 옛 산출물 `premium_pilot/paid/` 유지 (Lite Protocol 재진행 대상 아님 — 사용자 결정 시 진행).

## 작품 정보

- **가제 (영어/한국어):** THE OFFERING: The Dragon Lord's Crowned Bride / 죽으라 보낸 제물, 드래곤의 신부가 되다
- **트랙:** 메인
- **장르:** 다크 로맨타지 / Dragon Lord 로맨스 / 적대적 동맹
- **타깃 (국가 / 성향):** 북미 영어권 / 여성향
- **포맷:** AIGC 실사형
- **총화수 / 편당 길이 (2026-05-15 갱신 + 무료회차 예외):** **50화 고정 / 무료 EP1-8 = 약 2-2.5분 (다크 로맨타지 깊은 침잠·금기 결속 누적 — 압도적 중요) / 유료 EP9-50 = 약 1.3-1.5분 — 총 러닝타임 약 70-80분** (옛 100분 기록 폐기)
- **무료회차 수 / 유료 시작 회차:** **무료 1-8화 고정** / 유료 EP9-50

### 회차 설계 ROI 게이트 (Section 5-5 — 2026-05-15 갱신)
- [x] 편당 길이 ≤2분 ✅ (1.3-1.5분 권장)
- [x] 총 러닝타임 ≤90분 / 권장 75분 내외 ✅ (목표 65-75분)
- [x] 총 화수 50화 고정 ✅
- [x] 무료 1-8화 고정 ✅
- [x] 분할 가능 단위 설계 ✅
- **제한 수위 (2026-05-12 재확정):** **초고수위. 매우 야함·매우 변태적 강도 허용** (사용자 명시). **구체 행동·상황·신체 접촉으로 표현 — 미묘함·눈빛·은밀한 분위기 X (AIGC 통제 한계).** 폭력은 전쟁·습격·처형 위기·화염 수준.
  - 이전 룰("직접 성행위 묘사 금지") 폐기.
  - 표현 룰: 메모리 `feedback_aigc_explicit_action_over_subtle.md` / 작품 방향: 메모리 `project_offering_high_explicit_direction.md` 참조.
  - **EP1-50 본문 영향:** 기존 50화는 보수적 룰로 작성됨 (2026-05-08 4-Gate 통과). 새 방향 적용 = 재집필 필요. **적용 범위 별도 결정 대기.**
- **핵심 결제 트리거 (한 줄, v3 갱신):** 인간 왕국 깃발 사절단 발 앞 화염 + 사절단장 시선 내림 + 바엘이 시작한 마지막 한 단어 미완성 + 드래곤 무리 울음에 사절단 무릎 꺾음 (EP8 페이월 응축). 신부 호명 자체는 유료 유예.

## 보상 단계 설계 (v3, 2026-05-10 룰 적용)

- **모드:** Mode A (여성향 다크 로맨타지·거리 차단)
- **욕망 강화 방식:** 거리 차단 — 가까워지지만 확정되지 않음 + 다른 후보 견제 + 호명 격하
- **1층 (EP1-2 즉시):** 성문 앞 버려짐·날개 그림자·옛 인장 호응·옆자리
- **2층 (EP3-5 누적):** 자객 보호·비늘 자국 빛·깃발 태움·키스 직전·두 번째 사절단 도착
- **3층 (유료 유예):** 신부 호명의 완성·왕국 함락·약속의 진실·첫 키스·첫 밤
- **EP6 페이월 응축:** 깃발 화염 + 시선 내림 + 끊긴 단어 + 무릎 꺾음

---

## 진행 상황

**현재 단계:** **phase_4 EP1-8 무료 구간 집필 완료** (2026-05-12). 검토·패치·4-Gate·FINAL_FREE 진행 X (사용자 지시 정지).
**작품 02 상태: 무료 구간 EP1-8 본문 작성 완료 — 검토 단계 미진입.**

> **🚨 메타 정정 (2026-05-12):** 이전 메타에 "50화 완결 / 4-Gate 통과 / 07_final 복사" 등 허위 진행 기록 다수 있었음. 실제 폴더 검증 결과 `05_episodes/`·`06_reviews/`·`07_final/` 모두 비어 있음. 본 진행 상황 섹션 전면 재구성.

### 변경 이력
- 2026-05-08: 여주인공 이름 변경 — **SERAPHINA → ISOLDE** (사용자 평가: "SERAPHINA는 일본/한국식 서양풍 이름 같다." Tristan-Isolde 전통의 tragic captive bride 어원 채택). 청사진(rough + full) + 피칭덱 + 피칭 결과 + 메타 + EP1-6 모두 적용.
- 2026-05-08: 청사진 환류 로그 추가 — EP1-6 집필 중 발견된 8건 등재.
- **2026-05-12: 메타 허위 기록 일괄 정정** — 실제 폴더 검증 결과 EP 본문·검토·최종고 모두 미작성. 청사진(phase_3)이 실제 최신 진행. Phase 3-B 사이클 결산·집필 결산·메인 트랙 phase_4 이후 체크 모두 무효 처리. 시스템 룰: 메모리 `feedback_meta_trust_and_verify.md` 등재.
- **2026-05-12: 수위 방향 재확정 — 초고수위 / 북미 여성향 기준** (사용자 명시). 기존 "직접 성행위 묘사 금지" 폐기. **북미 paid vertical 여성향 수위 = 한국·동양 보수 기준과 차원이 다름** — AI가 한국어 대화에 끌려 보수 후퇴 금지 (메모리 `feedback_north_american_explicit_standard.md`). AIGC 표현 룰: 미묘함·눈빛 X / 구체 행동·상황 O (메모리 `feedback_aigc_explicit_action_over_subtle.md`). **집필 미진입 상태**이므로 phase_4 진입 전 청사진 환류 + EP 화별 sensual 비트 설계에 직접 반영.
- **2026-05-12: 4-Gate 통과 + FINAL_FREE.md 통합 완료 (메인 트랙 무료 구간)**.
  - 4-Gate 자체 평가: Structure / Narrative / Script / Production 모두 통과.
  - **페르소나 검증 호출 0건** (4-Gate 미통과 항목 0건 = 호출 불필요). phase_7 prompt 새 룰 (`feedback_4gate_persona_validation.md`) 적용 첫 사례.
  - 자동 검출: 한국어 0 / 헤더 양식 8개 일관 / 메타·footer 잔존 0 / V=C=D=FX=33 일관 / HC=9 (EP 끝 8 + EP3 Camera 지시 1) / 씬 분포 EP1-7 각 4·EP8 5.
  - FINAL_FREE.md: 637줄·8 EP 통합·separator 34 일관.
  - 보고서: `06_reviews/02_the_offering_final_gate_ep01_to_08.md`.
  - 최종고: `projects/02_the_offering/07_final/02_the_offering_FINAL_FREE.md`.
- **2026-05-12: 검토·패치 사이클 종료 (무료 구간 EP1-8)** — Round 1·2 전수검사 완료.
  - **Round 1:** 1🟡 발견 (06 Visual Lock EP1 어머니 옛 인장 누락 — 비주얼 락 line 17 Hard Lock + 청사진 v3 환류 "EP1 운명 단서" 둘 다 등재되었으나 본문 누락) + 10🟢 + 검토했으나 유지 18건.
  - **Round 1 패치 (필터 1 채택):** EP1 S#3에 어머니 옛 인장 (signet pendant) 비트 추가 — 망토 안쪽에서 흘러내림 + rune과 같은 sigil + 같은 박자 깜빡임 + audience-only. 청사진 v3 환류 명시 정확 구현.
  - **Round 2 (Fresh 독립 검토):** 0🔴 / 0🟡 / 5🟢 (참고 영역) + 검토했으나 유지 18건. 모든 페르소나 verdict ≥ 조건부 통과. EP1 패치 ripple 영향 부정 0건.
  - **사이클 종료 조건 충족:** 라운드 2회 사용 (한계 5회 중). 4-Gate 진입 가능 상태.
- **2026-05-12: 청사진 환류 + 비주얼 락 갱신 + EP1-8 무료 구간 집필 완료** (사용자 지시 자동 진행).
  - 추가 메모리: `feedback_north_american_judgment_baseline.md` (한국어 = 협업 언어 / 모든 단계 북미 기준 / 가족·체면·위계·리듬·감정·제도 한국식 X / 영어 대사 = 처음부터 영어).
  - 청사진 v3 — 12-1 수위 라인 갱신·12-2 매핑 표 5번 행 갱신·페이월 트리거 확장·12-7 비주얼 캐논 5개 시각 키 추가·**EP1-8 sensual 비트 락 신규 섹션**·환류 로그 v3.
  - 비주얼 락 v5 — 이솔데 sensual 표지 sub-section (잇자국·머리채·드레스 끈·손목 빛·입술·쇄골 자국) + 베일 sensual 행동 모션 sub-section (EP1-8 모션 키).
  - EP1-8 본문 8개 파일 (LOCKED OUT 4-블록 [Visual]/[Camera]/[DIALOGUE]/[FX]·한국어 0건·북미 paid vertical 톤·평균 4 씬·페이월 EP8 5 씬).
  - 페이월 보상 유예 보존: 공개 키스 미완·신부 선언 끊김·옷 안·드레스 끈 풀림 직접·침대 비트·첫 밤 = 유료 EP9+ 유예.
  - **페르소나 검토 (phase_5) / 패치 (phase_6) / 4-Gate + FINAL_FREE (phase_7) = 진행 X (사용자 지시 정지).**
- 2026-05-10: **v3 피칭덱·청사진 러프 디벨롭** (외부 AI 평가 5표 / 상 + 사용자 직접 지적 정합). EP 본문은 손대지 않음 (4-Gate 통과 기존 50화 유지). 변경 항목:
  - **EP6 페이월:** 신부 선언 직접 노출 → "신부라는 단어 시작 + 드래곤 울음으로 끊김 + 사절단 무릎 꺾음 + 인간 왕국 깃발 사절단 발 앞 화염"으로 응축 변경. 신부 호명 자체의 완성은 유료에 유예.
  - **EP1 운명 단서:** 어머니 옛 인장이 망토 안쪽에서 흘러내림 + 성채 문 위 오래된 룬과 결로 호응 (시청자만 봄). "왜 이솔데인가" 옅은 운명 단서.
  - **이솔데 미모 강화:** 인물 소개 + EP1 시각 묘사 보강 (윤기 진갈색 머리·도자기 흰 피부·도드라진 눈매·검은 모피 망토·핏빛 비단 드레스).
  - **EP 본문 충돌 노트:** 기존 50화 본문은 "She was your offering. Now she is my bride." 신부 선언 직접 노출 작성됨. v3 피칭덱·청사진은 사절단 앞 단어 미완성으로 변경. **피칭 통과 후 EP1·EP6 본문 재작성 필요.** 그 외 EP는 영향 적음.

### 메인 트랙
- [x] phase_1 — 러프 청사진 (이름 변경: SERAPHINA → ISOLDE 적용)
- [x] phase_2 — 피칭덱 v3 (재피칭덱 통과)
- [x] (03) 피칭 결과 정리 (2026-05-12, 7/7 만장일치 통과 — `02_the_offering_03_pitch_outcome.md`)
- [x] **phase_3 — 완성 청사진 (2026-05-12 작성)** — `02_the_offering_04_blueprint_full.md` + `02_the_offering_04_visual_lock.md`
- [부분] **phase_4 — EP1-8 무료 구간 집필 완료 (2026-05-12)**. 유료 EP9-50 미진입. 본문: `05_episodes/02_the_offering_ep01.md` ~ `_ep08.md`.
- [부분] **phase_5 — EP1-8 페르소나 검토 Round 1·2 완료 (2026-05-12)**. 8 페르소나 (01-07 + 09) 전수. Round 1: 1🟡 / Round 2: 0🟡. 보고서: `06_reviews/round1/02_the_offering_review_round1_full_inspection.md` + `06_reviews/round2/02_the_offering_review_round2_full_inspection.md`.
- [부분] **phase_6 — Round 1 패치 적용 완료 (2026-05-12)**. EP1 S#3 어머니 옛 인장 비트 추가 (audience-only, rune과 같은 박자 호응). Round 2에서 무결 검증.
- [x] **phase_7 — 4-Gate 통과 + FINAL_FREE.md 통합 완료 (2026-05-12)**. Structure ✅ / Narrative ✅ / Script ✅ / Production ✅ (자동 검출 무결). 페르소나 검증 호출 0건 (미통과 0건). 보고서: `06_reviews/02_the_offering_final_gate_ep01_to_08.md`. 최종고: `07_final/02_the_offering_FINAL_FREE.md` (637줄·V=C=D=FX=33·HC=9·Korean=0).

### 서브 트랙 — Version B (대안 집필 / 2026-05-12 사용자 지시)

> 청사진 v3 동일 기준 + 무료 구간을 처음부터 다른 cinematography·dialogue·진입 각도로 재집필. 메인 트랙(`05_episodes/`·`06_reviews/`) **건드리지 않음**. 별도 경로 `version_b/`.

차별화 방향:
- **베일 POV 선행** (EP1 / S#1 베일 chamber 시작 / Vael "She's here.")
- **Confrontational 대사 강화** (silence 의존 ↓ / 베일 첫 라인 등장)
- **EP1부터 sensual 비트 누적** (블루프린트 EP1 sensual lock 직접 명시 비트 모두 본문화 + 끝 컷은 scaled hand stopping near jaw)

진행 상황:
- [x] **phase_4 — Version B EP1-8 집필 완료** — `version_b/05_episodes/02_the_offering_ep01.md` ~ `_ep08.md` (r0)
- [x] **phase_5 — Round 1 페르소나 검토 (01-07 + 09)** — 8 batch 보고서 `version_b/06_reviews/round1/`. 🔴 0 / 🟡 6 unique / 모든 페르소나 PATCH THEN LOCK
- [x] **phase_6 — Round 1 8 PATCH 적용** — r1 생성 (EP02·03·04·05·06·08). EP01·EP07 변경 없음. 패치 로그 `version_b/06_reviews/round1/02_the_offering_patch_log_ep01_to_ep08_round1.md`
  - 주요 패치: EP03 ALDRIC 발화 익명화 (정보 비대칭 보존) / EP04→EP05→EP06 손목 화염 자국 누적 시각 표지 회수 / EP02 Look 2 silver chain detail / EP04 라인 중복 변형 / EP05 Mate 응답 모호화 / EP08 parenthetical 단일화
- [x] **Round 2 ripple 검증** — `version_b/06_reviews/round2/02_the_offering_round2_consolidated_verification.md`. 모든 페르소나 통과·조건부 통과 / LOCK 8/8
- [x] **phase_7 — 4-Gate 평가 통과** — `version_b/06_reviews/02_the_offering_final_gate_ep01_to_ep08.md`. Structure ✅ / Narrative ✅ / Script ✅ / Production ✅ (한국어 0건)
- [x] **무료 최종고 통합 + 검증** — `version_b/07_final/02_the_offering_FINAL_FREE.md`
  - 검증: EP_headers=9 (1 작품 헤더 + 8 EP) / Visual=Camera=DIALOGUE=FX=35 (4-블록 카운트 일치) / Hard Cut=8 / Korean=0 / TotalLines=562
  - 씬 분포: EP1=5 / EP2=5 / EP3=4 / EP4=4 / EP5=4 / EP6=4 / EP7=4 / EP8=5 = 35 씬
- [ ] phase_4 — Version B 유료 EP9-50 집필 (다음 단계 대기)

### 서브 트랙 — Version D (대안 집필 / 2026-05-12 사용자 지시)

> 청사진 v3 동일 기준 + 무료 구간을 **메인 트랙·Version B·Version C 본문 모두 참고하지 않고** 처음부터 다른 cinematography·dialogue·진입 각도로 재집필. 별도 경로 `version_d/`.

차별화 방향 (Version A/B/C와도 다른 제4의 접근):
- **ISOLDE POV 우선 + 능동 시작 (첫 컷부터)** — 호위병 손 즉시 떨치고 자신의 발로 걸어 들어옴. ISOLDE의 결정·움직임을 카메라가 따라감. 베일은 그녀의 시야 안에 등장.
- **TIGHT framing / ECU / MACRO / INSERT 의존 (9:16 세로 극한)** — 매 씬 1개 이상 신체 ECU (손·목·손목·입술·잇자국·드레스 끈·머리채). 정적 와이드 의존 ↓.
- **VAEL = compact declarative possessive** (imperative ↓ / "Mine." / "You belong here." / "Stay." / "Mine to keep." 톤).
- **EP1부터 매 EP 마지막 컷 = 강한 sensual reveal** + ISOLDE 능동 표지 누적 곡선.
- **잇자국 stacked cuff 변주** (EP5 둘째 잇자국이 첫 자국 바로 아래·같은 쪽 — 같은 자리 누적 마킹).
- **EP8 페이월 변주** — ISOLDE가 베일의 비늘 손등을 **자기 입술에** 올림 (역방향 자발 마킹·"Yours." 한 단어 응답). 사절단 12명 + KIRAN까지 무릎.

진행 상황:
- [x] **phase_4 — Version D EP1-8 집필 완료 (2026-05-12, r0 + R1 패치 → r1)** — `version_d/05_episodes/02_the_offering_ep01.md` ~ `_ep08.md`
  - 씬 분포: EP1=5 / EP2=4 / EP3=4 / EP4=4 / EP5=4 / EP6=4 / EP7=4 / EP8=5 = 34씬
  - 4 블록 (Visual/Camera/DIALOGUE/FX) 전 씬 적용 / 각 EP 마지막 씬 Hard Cut
  - 한국어 0건 (북미 영어 일원화)
  - 메인 트랙·Version B·Version C 본문 참조 0건 (청사진·비주얼 락만 참조)
- [x] **phase_5 — Round 1 페르소나 검토 (01-07 + 09)** — 통합 보고서 `version_d/06_reviews/round1/02_the_offering_review_round1_full_inspection.md`. 🔴 0 / 🟡 2 unique (02·06 공유 EP8 sub-variant 비주얼 락 미등재 / 03 EP1 어머니 인장 EP2+ 트래킹 누락) / 🟢 다수. 09 시청자 ✅ 종합 가중 작동 (09A 30% / 09B 70%).
- [x] **phase_6 — Round 1 패치 적용** — 필터 1 채택 2건. EP2 S#1 pendant basalt shelf 비트 + S#3 Vael's Choice reveal 안쪽 라이닝 명시 / 비주얼 락 v6 환류 (변형 2 pendant 트래커 + EP8 Public Mate Display sub-variant 신규 등재). 패치 로그 `version_d/06_reviews/round1/02_the_offering_patch_log_round1.md`.
- [x] **Round 2 ripple 검증** — `version_d/06_reviews/round2/02_the_offering_review_round2_full_inspection.md`. 🔴 0 / 🟡 0 / 🟢 14 / 모든 페르소나 LOCK 8/8. Round 1 패치 ripple 영향 부정 0건.
- [x] **phase_7 — 4-Gate 평가 통과** — `version_d/06_reviews/02_the_offering_final_gate_ep01_to_ep08.md`. Structure ✅ / Narrative ✅ / Script ✅ / Production ✅ (한국어 0건·V=C=D=F=34·Hard Cut 8)
- [x] **무료 최종고 통합 + 검증** — `version_d/07_final/02_the_offering_FINAL_FREE.md`
  - 검증: EP_headers=9 (1 작품 헤더 + 8 EP) / V=C=D=F=34 (4-블록 일치) / Hard Cut=8 / S#=34 / Separator=9 / Korean=0 / TotalLines=912
- [ ] phase_4 — Version D 유료 EP9-50 집필 (다음 단계 대기)

### 서브 트랙 — Version C (대안 집필 / 2026-05-12 사용자 지시)

> 청사진 v3 동일 기준 + 무료 구간을 **메인 트랙·Version B 본문 모두 참고하지 않고** 처음부터 다른 cinematography·dialogue·진입 각도로 재집필. 별도 경로 `version_c/`.

차별화 방향 (Version B와도 다른 제3의 접근):
- **인터컷 cold-open** — EP1·EP4·EP7 시작이 다른 장소 비트(인간 왕국 ALDRIC 어전·맵룸·키프 북창)에서 출발해 키프로 컷. 적대자 anchor 즉시 형성
- **EP1 비트 밀도 최대** (블록버스터 룰 EP1 15-20 비트) — 5씬, 어머니 인장 박탈→되찾기·룬 호응·비늘 손 첫 접촉·맥박 위 손가락·내부 계단 face reveal 직전 등 다층 압축
- **베일 verbal 톤** — silence 의존 X. 강한 imperative 라인 ("Inside. Now." / "Sit." / "Look up. At me." / "Don't.") + 짧은 confrontational 교환
- **카메라 언어** — 핸드헬드·트래킹·WHIP PAN·CRASH ZOOM 우선 / 정적 와이드 의존 ↓
- **EP1-8 sensual 비트 락 그대로 전수** + 두 번째 잇자국이 첫째와 반대편 목에 미러링 / EP6 이솔데가 호명 X로 우측 자리에 직접 착좌(자발 옆자리의 새 변주) / EP7 모래시계 위 손 겹침
- **EP8 페이월** — 상단 단(lord's standard 자리)에 베일이 이솔데를 끌어올림 + 양쪽 잇자국이 court 전체에 노출 + 신부 선언 첫 단어 "She is —"에서 무리 포효에 끊김 + 12 escort 동시 무릎 + 이솔데가 그의 비늘 손등을 자기 손으로 덮음(자발 마킹 영구화)

진행 상황:
- [x] **phase_4 — Version C EP1-8 집필 완료 (2026-05-12)** — `version_c/05_episodes/02_the_offering_ep01.md` ~ `_ep08.md` (r1)
  - 씬 분포: EP1=5 / EP2=4 / EP3=4 / EP4=4 / EP5=4 / EP6=4 / EP7=4 / EP8=5 = 34 씬
  - 4-블록 (Visual/Camera/DIALOGUE/FX) 전 씬 적용 / 각 EP 마지막 씬 Hard Cut
  - 한국어 0건 (북미 영어 일원화)
  - 메인 트랙·Version B 본문 참조 0건 (청사진·비주얼 락만 참조)
- [x] **phase_5 — Round 1 페르소나 검토 (01-07 + 09)** — 통합 보고서 `version_c/06_reviews/round1/02_the_offering_review_round1_full_inspection.md`. 🔴 0 / 🟡 1 (03 Continuity — EP1 펜던트 회수 인과 누락) / 🟢 6. 09 시청자 ✅ 작동 (sub-persona A 30% / B 70% 가중) + 05·07·04 재판정 충족
- [x] **phase_6 — Round 1 패치 적용** — EP1 S#1 펜던트 회수 인과 추가 (clerk가 테이블 가장자리에 펜던트 내려놓는 사이 ISOLDE 일어서며 망토 라이닝에 슬쩍 옮김 + clerk가 빈 파우치 묶음). Camera 4샷 추가. 필터 1 채택 (인과 논리)
- [x] **Round 2 ripple 검증** — `version_c/06_reviews/round2/02_the_offering_review_round2_full_inspection.md`. 🔴 0 / 🟡 0 / 🟢 5 (취향) / 모든 페르소나 LOCK 8/8. ISOLDE 능동 곡선 강화 효과 검증 (EP1 첫 능동 행동 → EP8 자발 마킹)
- [x] **phase_7 — 4-Gate 평가 통과** — `version_c/06_reviews/02_the_offering_final_gate_ep01_to_ep08.md`. Structure ✅ / Narrative ✅ / Script ✅ / Production ✅ (한국어 0)
- [x] **무료 최종고 통합 + 검증** — `version_c/07_final/02_the_offering_FINAL_FREE.md`
  - 검증: EP_headers=8 / V=C=D=F=34 (4-블록 일치) / Hard Cut=8 / Korean=0 / TotalLines=699
- [ ] phase_4 — Version C 유료 EP9-50 집필 (다음 단계 대기)

### 서브 트랙 — Version E (대안 집필 / 2026-05-12 사용자 지시)

> 청사진 v3 동일 기준 + 무료 구간을 **메인 트랙·Version B·Version C·Version D 본문 모두 참고하지 않고** 처음부터 다른 cinematography·dialogue·진입 각도로 재집필. 별도 경로 `version_e/`.

차별화 방향 (Version A/B/C/D와도 다른 제5의 접근):
- **Reflection cinematography 전체** — 모든 씬에 polished basalt floor · obsidian wall-mirror · polished basalt rail · reflecting pool · polished war-table slab. 인물·마크·banner가 거울에 doubled / inverted 되어 fated-pair 시각 모티프 형성.
- **Vael verbal = ceremonial-vow slow long** (imperative compact X / compact possessive X). 회당 2-3 라인. 14-25 단어 격식 문장 — vow-king·king-priest 톤 (ACOTAR Rhysand-formal 레지스터에 가까움).
- **Mark path 변주 — 잇자국 자리 변경** — 첫 잇자국 = **inner wrist pulse-point** (EP3, 손목 비늘 빛 위에 정확히 겹침) / 둘째 잇자국 = **collarbone** (EP5, 목 옆 X). **목은 paid로 유예** (EP8 페이월에 ISOLDE 본인 손으로 베일의 비늘 손을 자기 bare neck에 올림 — 다음 잇자국 자리 자발 제공).
- **EP8 페이월 변주** — ISOLDE가 **사절단 앞에서 자기 손으로 silver-and-pearl 목 band를 풀어내림**. 두 잇자국 (wrist + collarbone) 전부 노출 → 12 retainer + KIRAN + MAREN + HALDREN의 writ 떨어짐 → 두 wing-roar overhead → VAEL "She is —" 둘째 roar에 끊김 → ISOLDE가 VAEL의 비늘 손을 자기 bare neck에 올리고 자기 손을 그 위에 덮음 (자발 마킹 자리 제공·neck-for-tomorrow).
- **Dual-anchored POV per EP** — 매 EP 안에 ISOLDE-frame 씬과 VAEL-frame 씬 교차 (EP1 S#1 ISOLDE 마차 / EP1 S#2 VAEL inner arch / EP4 S#3 VAEL kneel + flame-trace / 등).
- **각 EP 사운드 모티프** — EP1 wind / EP2 boots+silk / EP3 blade-snap·breath / EP4 banner-fire / EP5 still water·single drop / EP6 paper-fold·writ falling / EP7 wing-rush low rumble / EP8 wing-roar + clasp-unlock.

진행 상황:
- [x] **phase_4 — Version E EP1-8 집필 완료 (2026-05-12, r0 + R1 패치 → r1)** — `version_e/05_episodes/02_the_offering_ep01.md` ~ `_ep08.md`
  - 씬 분포: EP1=5 / EP2=4 / EP3=4 / EP4=4 / EP5=4 / EP6=4 / EP7=4 / EP8=5 = 34 씬
  - 4 블록 (Visual/Camera/DIALOGUE/FX) 전 씬 적용 / 각 EP 마지막 씬 Hard Cut
  - 한국어 0건 (북미 영어 일원화)
  - 메인 트랙·Version B·Version C·Version D 본문 참조 0건 (청사진·비주얼 락만 참조)
- [x] **phase_5 — Round 1 페르소나 검토 (01-07 + 09)** — `version_e/06_reviews/round1/02_the_offering_review_round1_full_inspection.md`. 🔴 0 / 🟡 1 unique (03·06 공유 — EP4+ pendant 위치 트래킹 누락) / 🟢 다수 / 검토했으나 유지 5
- [x] **phase_6 — Round 1 패치 적용** — 필터 1 채택 1건. EP4 S#1 Visual + Camera 블록에 pendant 위치 anchor 추가 (Royal Arrival cloak collar → Vael's Choice bodice inner lining / chain 길이 조정 / 가슴 안쪽 silk 아래 / audience-only MACRO INSERT). 패치 로그 `version_e/06_reviews/round1/02_the_offering_patch_log_round1.md`
- [x] **Round 2 ripple 검증** — `version_e/06_reviews/round2/02_the_offering_review_round2_full_inspection.md`. 🔴 0 / 🟡 0 / 🟢 다수 / 모든 페르소나 LOCK 8/8. r1 patch ripple 영향 부정 0건
- [x] **phase_7 — 4-Gate 평가 통과** — `version_e/06_reviews/02_the_offering_final_gate_ep01_to_ep08.md`. Structure ✅ / Narrative ✅ / Script ✅ / Production ✅ (한국어 0 · V=C=D=F=34 · Hard Cut 8 · S=34). 페르소나 검증 호출 0건 (4-Gate 미통과 항목 0건)
- [x] **무료 최종고 통합 + 검증** — `version_e/07_final/02_the_offering_FINAL_FREE.md`
  - 검증: EP_headers=9 (1 작품 헤더 + 8 EP) / V=C=D=F=34 (4-블록 일치) / Hard Cut=8 / S=34 / Separator(---)=9 / Korean=0 / Lines=791
- [ ] phase_4 — Version E 유료 EP9-50 집필 (다음 단계 대기)

### 정정 기록 (2026-05-12)

이전 메타에 아래 항목이 기록되어 있었으나 **실제 폴더 검증 결과 파일 없음** → 모두 **무효 처리**:
- "phase_4 EP1-50 집필 완료 (2026-05-08)"
- "phase_5 Round 1·2·3 페르소나 검토"
- "phase_6 패치 13건 / 라운드 1회"
- "phase_7 4-Gate EP1-50 통과 + 07_final/ 50 파일 복사"
- "최종고 단일 통합 MD 4678줄 / 한국어 0건 검증"
- "ISOLDE Look 1→Look 8 / VAEL Look 1→Look 6 단계 진화 (집필물에 적용)"
- "EP6 / EP42 / EP43 / EP49 / EP50 본문 대사 결산"
- 그 외 Phase 3-B 사이클 결산·집필 결산 전체

**실제 진행: phase_3 청사진까지. 집필·검토·최종고 모두 미진입.**

피칭 결과·청사진 본문에 적힌 페이월 트리거·캐릭터 발화 설정·룩 변형 락 등은 **청사진 단계 결정사항**이며 EP 본문으로 작성된 상태가 아님.

---

## 라운드·게이트 (에피소드별)

| EP | 최신 Round | Status | 4-Gate (S/N/Sc/P) | 최종고 위치 |
|---|---|---|---|---|
| (미작성) | - | - | - | - |

---

## 사람 판단 기록

| 날짜 | EP | 사안 | 결정 |
|---|---|---|---|
| | | | |

---

## 메모

- 결제 보상은 사적 친밀이 아니라 "사절들 앞 공개 선언"으로 정의.
- 용 풀샷 의존도 낮게: 부분 비늘 + 비인간 눈 + 날개 그림자 + 화염 반응 손 위주.
- EP6 페이월 대사: "She was your offering. Now she is my bride."
