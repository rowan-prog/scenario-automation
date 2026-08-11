---
name: emotion-to-action-aigc-writing
description: 감정 문장 ("That breaks him") 금지·AIGC 작업자가 직접 찍을 수 있는 행동 문장으로 전환. 핵심 장면은 인물 위치·행동 순서·카메라 포인트·물체 명시.
metadata:
  type: feedback
  originSessionId: 2026-05-21-the-offering-v32
---

# VISUAL/ACTION 문법 — 감정 → 행동 전환 룰

## 핵심 룰

**감정 결과 문장 ("That breaks him." / "He hesitates." / "She melts.")는 [VISUAL/ACTION] 블록에서 금지.**

**대신:** 턱·손·거리·시선·재접근의 *보이는 행동 sequence*로 풀어 쓴다.

**Why:** v31.2 EP22의 "He hears it. Stops fighting himself for one second too long." 같은 문장은 *문학적*으로는 OK이지만 AIGC 작업자에게 "그래서 화면에 뭐가 보이나?"를 다시 해석시킨다. 외부 평가: "감정 문장이 화면 지시를 대신하는 경우가 있음." 결과: AIGC 작업자가 *감상*하거나 *해석*해서 만드는 컷이 생긴다 = 평면적 결과물.

## 🆕 단일 원칙 (2026-06-09 사용자 최종 확정·"앞으로 지문 기준") — 감정 = *장면 구조*에서, 동작 줄이 아니라

(AI 자가판정이 계속 점잖은/소설적 쪽으로 새서 `angry`→`jaw tight`→`instead of looking away`→"물리형이 감정을 운반" 순으로 *네 번* 빗나갔고 사용자가 매번 잡아 최종 확정. 교훈: **동작 한 줄엔 특정 감정이 안 담긴다** — 같은 동작이 상황 따라 정반대로 읽힘[쿨레쇼프]. 그래서 라벨·표정·서술·'물리형' 전부 실패.)

> **지문은 감정을 *설명하지 않는다.* 깨끗한 동작 + 그 동작이 만든 *반응*만 쓴다. 감정은 ①직전 대사/상황 ②행동(중립 축) ③주변 반응 ④그 반응이 만든 위험/권력/긴장 에서 온다.**

✅ 원본형(작동함): `Isolde steps toward Adeline.` / `The guard moves.` / `Aldric lifts one hand.` / `The guard stops.` — "빡쳤다" 안 써도 *반응*이 다가감을 세게 만듦.
❌ 의미 덧칠(대본 지문으로 별로): `for the first time`·`instead of looking away`·`angry now`·`jaw tight, eyes wet`·`steps into her space`.

**컷이 밍밍하면 지문에 감정 형용사 바르지 말고 대사/상황/반응을 고친다.** 솔로 비트(반응자 없음)면 ③ 빠지고 ①②④+VO. 단일 진실 = `config/lock_pipeline_standard.md` Phase 2B △.

---

**How to apply:** [VISUAL/ACTION] 블록 작성 시 모든 감정 결과 문장을 다음 4 카테고리 행동으로 전환:

| 감정 결과 | 행동 전환 |
|---|---|
| "He breaks." | "His jaw tightens. His hand leaves the wall. Closes at her waist." |
| "She melts." | "Her shoulders drop. Her hand finds the small of his back. Stays." |
| "He hesitates." | "His hand stops one inch from her face. Does not move." |
| "She decides." | "She lifts her chin. Takes one step forward." |
| "He surrenders." | "His scaled forearm softens against her palm. The scales flatten." |
| "She wants him back." | "Her hand tightens in his hair. Pulls his mouth back to hers." |
| "He loses control." | "His scales rise at his neck. Black fire down his arm." |

## 핵심 4 정보 (각 [VISUAL/ACTION]에 필수)

| 정보 | 예 |
|---|---|
| **공간** | chamber / hall / yard / carriage / windowsill |
| **인물 위치** | Isolde at altar, Vael three paces behind, Sera at side |
| **행동 순서** | she steps / he stops / she turns / he catches |
| **화면 포인트 (물체·시각)** | black mirror, hand on wrist, scale flicker, broken parchment |

→ 4 정보 중 *2개 이상 부재* = 다시 작성.

## 실측 사례

### ❌ v31.2 EP22 (감정 문장)
```
She breaks first. Not from fear. From wanting him back.
He hears it. Stops fighting himself for one second too long.
```

### ✅ v31.4 EP22 → v32 EP29 (행동 sequence)
```
Her hand tightens in his hair.
He tries to slow down.
She pulls him back before he can.

[DIALOGUE]
ISOLDE: Don't stop.

[VISUAL/ACTION]
That is what breaks him.
```

→ 감정 결과 문장 1개 (마지막 "That is what breaks him.")만 *명확한 대사 직후 결과*로 허용. 나머지는 행동.

### ❌ v31.2 EP36 (너무 thin)
```
He turns her. Kisses her. Slow.
```

### ✅ v31.4 EP36 (보강)
```
He turns her by the hip — slow, one hand only. 
Her back leaves the windowsill. 
Her hand leaves the glass — leaves a faint print of warmth on the cold pane.
He stops one inch from her mouth. 
Waits.
She closes the distance. 
Her mouth on his first.
Only then does he kiss her back. 
Slow. Hand at the small of her back. 
Other hand at her jaw.
```

→ 8 행동 단계로 풀어쓰기. AIGC 작업자가 frame-by-frame 가능.

## 핵심 장면 디테일 보강 룰 (15-25% 확장)

**모든 장면을 길게 쓰지 말 것** — 핵심 9 장면만 보강.

| 핵심 장면 | 이유 |
|---|---|
| EP01 첫 컷 (콜드 오픈) | 첫화 retention 핵심 |
| EP01 마지막 black mirror 엔딩 | 첫 모욕 + Isolde 결연 |
| EP08 paywall 직전 | 유료 전환 핵심 |
| EP09 첫 유료 보상 ("She is my bride" 등) | 결제 도파민 |
| 첫 full bed scene | 장르 약속 |
| 임신 reveal | 시리즈 엔진 시작 |
| Mate reveal / 공개 claim | 관계 코어 |
| 출산 | 후반 클라이맥스 |
| Queen ceremony | Status payoff |
| Finale (last 30 seconds) | 최종 family lock |

→ 위 장면들만 *현재의 15-25% 더 구체화*. 나머지는 기존 톤 유지.

## 금지 — 과잉 보강

| 금지 | 이유 |
|---|---|
| 모든 지문을 길게 풀기 | 회차 늘어짐 |
| 문학적·시적 묘사 | AIGC 도움 안 됨 (e.g. "그녀의 눈물이 별처럼 흘러내린다") |
| 감정 해설 | 시청자 지문 안 봄 |
| 카메라 용어 과잉 ([KEY CAMERA]·[CUTAWAY] 외) | 제작 혼란 |
| 모든 컷 세세히 지정 | 작업자 자율성 사라짐 |

## 권장 — 디테일 보강 방향

| 할 것 | 방식 |
|---|---|
| 핵심 장면만 구체화 | 위 9 장면 |
| 감정 문장 → 행동 문장 | 위 표 참조 |
| 누가 먼저 움직이는지 명확히 | female gaze 유지 |
| AIGC 볼 수 있는 물체 추가 | mirror, chain, bed, door, crown, scale |
| 같은 장소 반복 시 변주 | window, bed edge, floor, bath, hall, gate |

## 한 줄

> **감정은 행동으로. AIGC 작업자가 *해석* 없이 *촬영* 가능해야. 핵심 9 장면만 15-25% 보강.**

관련: [[screen-rhythm-v3-blocks]] [[female-gaze-camera-polish]] [[no-theater-tone]]
