# Version D — Round 1 패치 로그

## 발견 (Round 1 통합 보고서 기반)

| ID | 페르소나 | 등급 | 영역 | 위치 |
|---|---|---|---|---|
| R1-1 | 02·06 (공유) | 🟡 | 비주얼 락 정합 | EP8 S#3 ISOLDE altered overnight sub-variant 락 미등재 |
| R1-2 | 03 | 🟡 | 연속성·인과 논리 | EP1 어머니 인장 EP2+ 위치 미회수 |

## 필터 판정

| ID | 필터 1 (정합성·논리·언어 — 채택 필수) | 필터 2 (프로덕션 가이드 위반·핵심 쾌감 약화·캐릭터 매력 약화 — 채택 거부) | 채택 |
|---|---|---|---|
| R1-1 | ✅ 비주얼 락 정합 위반 | (필터 1 매칭 — 필터 2 검사 X) | **채택** |
| R1-2 | ✅ 인과 논리 누락 (Hidden Identity Hard Lock 단서 트래킹) | (필터 1 매칭 — 필터 2 검사 X) | **채택** |

## 적용

### R1-1: EP8 sub-variant 비주얼 락 등재
- **파일:** `projects/02_the_offering/02_the_offering_04_visual_lock.md`
- **변경:** ISOLDE 변형 2 (Vael's Choice) 아래에 신규 sub-variant 등재 — **변형 2-Public Mate Display (EP8 sub-variant)**. silver-and-pearl trim·wider pearl-silver band·hair pearl pin·chain band cut low. 변경 트리거 EP7→EP8 야간.
- **EP8 본문 변경 X** — [Visual] 묘사 그대로. 락 등재만 추가.
- **환류 로그 v6** 등재.

### R1-2: EP1 어머니 인장 EP2+ 트래킹
- **파일 1:** `version_d/05_episodes/02_the_offering_ep02.md`
  - **S#1 [Visual] 패치:** "At the mirror's foot, the silver chain with her mother's signet pendant lies coiled on a small basalt shelf — she has just unpinned it from the Royal Arrival cloak." 한 단락 추가.
  - **S#1 [Camera] 패치:** "MACRO INSERT on the silver chain and signet pendant coiled on the basalt shelf" 한 shot 추가.
  - **S#3 [Visual] 패치:** ISOLDE Vael's Choice reveal에 "Her mother's signet pendant has been moved to the **inner lining of the new gown's bodice** — invisible to the hall, but its outline catches the lamp-light against the silk for one breath as she crosses the floor." 한 단락 추가.
- **파일 2:** `projects/02_the_offering/02_the_offering_04_visual_lock.md`
  - ISOLDE 변형 2 본체에 "어머니 signet pendant 위치 (EP2+)" 트래커 등재.
- **환류 로그 v6** 등재.

## ripple 영향 예상

- EP2 S#1 패치 = pendant 처리 비트 추가. 씬 비트 수 변화 1개. 씬 기능 변경 X (의상 결정·갈아입기 비트 그대로).
- EP2 S#3 패치 = ISOLDE Vael's Choice reveal 통합 묘사에 한 문장 추가. 의상 묘사 일관성 강화. 다른 씬 영향 X.
- 비주얼 락 v6 등재 = EP8 sub-variant 명시화. EP8 본문 변경 X. 향후 EP9+ 집필 시 의상 일관성 참조 자료 확보.

## Round 2 fresh 검토 예상
- 패치 ripple 영향 확인 — EP1 → EP2 pendant 트래킹 정합 / EP2 reveal 통합 묘사 자연성 / EP8 본문-락 정합 검증.
- 매 페르소나 fresh 독립 검토 — Round 1 발견·판정 참조 X.
