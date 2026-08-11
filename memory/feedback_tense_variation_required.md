---
name: tense-variation-required
description: 🚨 대사·VO에서 현재형 시제만 반복 금지 (2026-05-27 사용자 명시). 상황에 맞게 미래형·과거형·과거완료·미래완료·현재완료·현재진행형 적절히 활용. 모든 영어 대본 적용.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 822d9a9c-17d7-46a8-b0d9-5716ec65a086
---

# 🚨 시제 다양성 필수 — 영어 대본·VO

## 사용자 명시 (2026-05-27)

> *"대사/VO가 법칙마냥 현재형 시제만 쓰는 것 주의. 상황에 맞게, 미래형, 과거형, 과거완료, 미래완료, 현재완료, 현재진행형 등을 적절히 활용해야함."*

## Why

Claude default voice가 영어 대본에 **현재형 simple present (`I want / I love / She knows`) + present continuous (`I'm telling / I'm asking`)**만 반복 사용하는 경향. 결과:
- 시제 차이로 표현되는 감정·시간 거리·예측·후회·계획 등이 평면화
- 모든 캐릭터가 같은 시간 layer에서 말하는 느낌
- 인간 대화가 절대 그렇지 않음·시제는 자연스럽게 섞임

## 적용 시제 7+ 카테고리

자연 spoken English는 한 대화에서 여러 시제를 자연스럽게 섞는다:

1. **Simple Present** — 현재 상태·일반 사실 (`I want this. / She knows.`)
2. **Present Continuous** — 진행 중 행동·일시적 상태 (`I'm working on it. / She's not answering.`)
3. **Present Perfect** — 과거에서 현재까지 (`I've been waiting. / She has done this before.`)
4. **Present Perfect Continuous** — 지속 진행 (`I've been thinking about it. / She's been watching us.`)
5. **Simple Past** — 완료된 과거 사건 (`I told you. / She left.`)
6. **Past Continuous** — 과거 진행 (`I was driving when... / She was about to leave.`)
7. **Past Perfect** — 과거의 과거 (`I had already left when... / She had warned me.`)
8. **Past Perfect Continuous** — 과거의 지속 (`I had been waiting for two hours. / She had been planning this.`)
9. **Simple Future** — 미래 사건 (`I will. / She'll call you.`)
10. **Future Continuous** — 미래 진행 (`I'll be working all night. / She'll be expecting you.`)
11. **Future Perfect** — 미래의 완료 (`I will have finished by then. / She'll have left by morning.`)
12. **Future Perfect Continuous** — 미래의 지속 완료 (`I will have been waiting six hours. / She'll have been doing this for years.`)
13. **Modal phrases** — 가능성·의무·후회 (`I should have. / She might have known. / We could have stopped it.`)

## ❌ 평면적 (현재형 일변도)

```
LENA: I know. I see what she does. I want my name back.
NOAH: She knows you're here. She sees us. She wants this.
LENA: I'm telling you, I'm asking you to stop her.
```

→ 모든 turn 현재형·시간 layer 단일·감정 평면화.

## ✅ 자연 (시제 자연스럽게 섞임)

```
LENA: I knew the moment she stepped out of the elevator. I'd been afraid of that face for weeks before I ever saw it again.
NOAH: She's been watching us since Tuesday. Whoever sent her will have moved by tomorrow morning.
LENA: I should have asked you sooner. I'd have done this differently.
```

→ Past·past perfect continuous·simple past·present perfect continuous·future perfect·modal perfect 자연 섞임. 인간 호흡.

## 시제 활용 매트릭스 (상황별)

| 감정·상황 | 자연 시제 |
|---|---|
| 회상·후회 | Past perfect / Modal perfect (`I should have / I had been / We could have`) |
| 예측·계획 | Future / Future perfect (`I will / I'll have / She'll be`) |
| 지속된 부담 | Present perfect continuous (`I've been waiting / She's been watching`) |
| 완료된 결단 | Simple past (`I told her / She left`) |
| 진행 중 | Present continuous (`I'm doing / She's calling`) |
| 일반 사실·현재 상태 | Simple present (`I want / She knows`) |

대본 작성 시 한 캐릭터의 turn 안에서도 시제 섞임이 자연·인접 turn 간 시제 다양성 필수.

## 자가 검사 (매 EP scan)

1. 한 EP에서 simple present + present continuous 비율이 70%+ 인가? → 다른 시제 적극 도입
2. 회상·예측·후회 비트인데 simple present 사용? → past perfect / future / modal perfect 등으로 교체
3. 같은 turn 안에 시제 1개만? → 자연 spoken English는 2-3 시제 섞임 빈번
4. VO에 simple present 일변도? → past·present perfect로 시간 거리 부여

## 적용 범위

✅ EP 본문 모든 dialogue·VO
✅ VO·monologue
✅ 모든 캐릭터 (Lena·Noah·Mara·Victoria·Ethan·Eileen·Julian 등 균등)
✅ Lower-third graphic·END HOOK 텍스트도 적용

## 연관

`[[no-theater-tone]]` (7 차원·시적/연극톤 금지) · `[[spoken-english-native-polish]]` (자연 spoken English) · `[[claude-voice-bias-vertical-failure]]` (default voice 편향)
