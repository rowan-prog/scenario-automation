# Visual Appeal & Character Lock Auditor 검토 보고서 — THE OFFERING (Version B) EP01-EP08

## 검토 요약
비주얼 락 v5 (이솔데 어셋 + 룩 4단계 + sensual 표지 6 / 베일 어셋 + 단일 Dragon Lord + sensual 행동 모션) 본문 정합. 다크 로맨타지 대비 원칙 (브라이트 vs 다크) EP1·EP2 reveal 작동. 자국·표지 누적 (잇자국 / 손목 빛 / 드레스 끈 / 머리채) 본문 추적 가능. 다만 EP2 reveal 묘사에서 비주얼 락 명세 한 디테일(은빛 사슬) 누락 + EP4→EP5 손목 화염 자국 누락. 자동 trigger.

## 발견된 문제

### 🔴 즉시 수정 필요
없음.

### 🟡 약점 (수정 권장)

**1. EP02 Look 2 (Vael's Choice) reveal 묘사 — 비주얼 락 명세 디테일 누락**
- 위치: EP02 / S#3 / [Visual]
- 원문 FIND: `Isolde walks the long corridor toward the great hall in **the new gown — black silk over the floor, silver-and-pearl embroidery along the bodice and sleeves, oblique neckline baring the line of her collarbone, the porcelain inside of her wrists visible, dark-brown hair brushed long and loose down her back.**`
- 문제: 비주얼 락 v5 Look 2 명세 = "검은 비단 베이스 + 흰·실버 자수·진주 디테일·**은빛 사슬**". 본문에서 은빛 사슬 디테일 누락. EP3+ 다른 회차에서 이 detail이 화면에 보일지 안 보일지 모호.
- 수정 방향: 본문 묘사 끝에 `with a thin silver chain detail at the waist` 한 줄 추가.

**2. EP04 → EP05 손목 화염 자국 (scorched-line) 시각 표지 미회수**
- 위치: EP05 / S#1 / [Visual] + EP06 / S#3 / [Visual]
- 원문 FIND (EP05): `Her inner wrist glows faintly gold against the dark.`
- 원문 FIND (EP06): `The pale gold mark on her inner wrist is steady now — no flicker, no fade.`
- 문제: EP04 / S#4에서 추가된 "burned ash, not skin — sits over the mark"가 EP5·EP6 어디서도 묘사되지 않음 → 시각 자국 단명. 비주얼 락 sensual 표지 누적 원칙 (잇자국 등은 누적 reveal) 위반. AIGC 생성 시 자국 표지 일관 X.
- 수정 방향:
  - EP05 / S#1 [Visual]: `...glows faintly gold against the dark, **the thin scorched-line traced over the mark by Vael's flame yesterday still visible**.`
  - EP06 / S#3 [Visual]: `...steady now — no flicker, no fade — **the scorched-line above it from the council chamber unfaded**.`

### 🟢 선택적 개선

**1. EP01 / S#1 베일 머리 색 명세 — 비주얼 락 정렬**
- 위치: EP01 / S#1 / [Visual]
- 원문 FIND: `VAEL DRAKONIS ... lustrous black hair tied back, grey eyes, sharp jaw`
- 검토: 비주얼 락 v2 명세 = "흑갈색 머리 (어깨까지·뒤로 묶음)". 본문 "lustrous black hair tied back" — 색 톤 미세 차이 (흑갈색 vs 검은). AIGC 어셋 생성에서 흑갈색·검정 사이 미세 영향 가능. 정렬 권장.

**2. EP02 / S#3 머리 묘사 — 비주얼 락 헤어 어셋 충실**
- 위치: EP02 / S#3 / [Visual]
- 원문 FIND: `dark-brown hair brushed long and loose down her back`
- 검토: 비주얼 락 ISOLDE 어셋 = "윤기 진갈색 머리 (어깨 아래 흘러내림)". 본문 "long and loose down her back" 충실. 다만 "윤기"의 영문 표지 lustrous를 EP1처럼 일관 권장.

## 의심 지점 사전 스캔
1. EP01-EP08 ISOLDE 어셋 핵심 6 디테일 (윤기 진갈색 머리 / 회녹색 눈 / 도자기 흰 피부 / 갸름 V형 얼굴 / 가는 손목 / 곧은 자세) 본문 일관 → 처리: 검토했으나 유지 (EP1 / S#2 [Visual] 첫 등장 시 6 디테일 명시 — `mid-20s, lustrous dark-brown hair flowing past her shoulders, grey-green eyes, porcelain pale skin, slender wrists`).
2. EP01-EP08 VAEL 어셋 핵심 5 디테일 (검은 비늘 손등 / 큰 체격 / 회색 눈 / 검은 머리 / 검은 가죽 + 망토) 본문 일관 → 처리: 검토했으나 유지 (EP1 / S#1 첫 등장 시 5 디테일 명시 — `mid-30s, broad-shouldered, lustrous black hair tied back, grey eyes, sharp jaw — Dragon Lord` + `back of his hand is plated in obsidian-and-blood-red SCALES`).
3. EP02 Look 2 reveal 디테일 → 처리: 🟡 (위 1번).
4. EP04→EP05 손목 화염 자국 → 처리: 🟡 (위 2번).
5. EP03 / S#3 잇자국 + 드레스 끈 풀림 — 후속 회차에서의 일관 → 처리: 검토했으나 유지 (EP5 second bite-mark + EP6 deep-cut gown 노출 + EP8 공개 표지 모두 본문 묘사 일관).
6. EP07 / S#2 머리채 흐트러짐 — EP8에서의 연속 → 처리: 검토했으나 유지 (EP8 / S#4 `Vael's scaled fingers slide into her dark-brown hair at the side of her skull and TILT her head` — 머리채 표지 누적 작동).

## 검토했으나 유지
1. EP08 / S#4 — 의심: 베일 의식 의상 (검은 가죽 + 황금 자수 + 황금 왕홀)이 EP25부터인데 EP8 페이월에서 의식 의상 reveal 안 함 — 페이월 spectacle 약화? 검증 결과: 비주얼 락 v2 — Dragon Lord 단일 의상 유지 (Lord/King 통합) / 의식 의상은 EP25부터. EP8 페이월 = 일상 Dragon Lord 의상 유지가 정합. spectacle은 무릎+roar+banner+신부 선언 끊김으로 응축.
2. EP06 / S#1 — 의심: 이솔데의 deep-cut 의상이 비주얼 락 Look 2의 oblique neckline과 별개의 의상 변화? 검증 결과: Look 2 명세 = "**오블리크 네크라인이 쇄골 라인을 드러내는** + 우아한 신부급 가운 + 천사적 디테일 유지". 그 안에서 같은 Look 2의 다른 발화 = `the deep-cut neckline showing the marks on her neck` — Look 2 변형 X / Look 2 유지 + 머리 묶음 + 의상 선택의 농도 변화로 작동. 락 위반 X.
3. EP08 / S#3 — 의심: ash from burned banner clings to scales — 시각 표지의 회수가 EP9+에 어떻게 → 검증 결과: EP4 ash 표지가 EP8까지 회수 → EP8 페이월의 ash 시각 표지가 새로운 자국 (블루프린트 9-10+에서 회수). 누적 정합.

## 잘 작동하는 부분
- EP01-EP08 — 캐릭터 어셋 핵심 디테일 100% 본문 일관.
- 다크 로맨타지 대비 (브라이트 ISOLDE vs 다크 VAEL) — EP1 ivory gown + 검은 비늘 손, EP2 reveal 검은 silk + 흰·진주·실버 디테일 (다크 베이스 + 순수 표지 유지).
- 자국 누적 명확 — 손목 빛 (EP1 첫 → EP5 ignites → EP6 영구) / 잇자국 (EP3 첫 → EP5 둘째 → EP8 공개 표지).
- EP08 / S#4 페이월 핵심 비주얼 — `the bite-marks turned out toward the delegation` — 공개 마킹 컷 spectacle 작동.

## 검토 총평 (Verdict)

- **Verdict 4단계:** 패치 필수 (🟡 2건 — 자동 trigger 06 비주얼 락 정합)
- **LOCK / PATCH THEN LOCK / HOLD:** PATCH THEN LOCK
- 다음 단계: EP2 silver chain detail 추가 + EP5·EP6 손목 화염 자국 시각 표지 회수 후 LOCK.
