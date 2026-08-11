---
name: spoken-english-native-polish
description: "영어 대본 Spoken English 원어민 polish 룰. 5단어 이하 강제 X (원시인 영어·코미디 위험). 5-10 단어 자연 spoken default·핵심 결정 발화만 1-3단어. 문법 정확·관용 자연. 2026-05-19 V16 통합 피드백."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2d65e927-1cd5-4df0-bd23-1493c3adfb18
---

> **근본 진단:** OFFERING V14·V15·V16에서 "Vael 발화 80% ≤5단어" 룰 적용 결과 = "If she cost me you." (문법 오류·`If she costs me you.`가 정확)·"Her no holds. Her names cost hands." (부자연 압축)·"It isn't a court piece. It's a piece." (번역투) 같은 위반. 5단어 강제 = "원시인 영어" 신화.

## 룰

**Spoken English default = 5-10 단어 자연 spoken English.** 핵심 결정 발화만 1-3 단어. 짧음·자연·문법·관용 모두 충족.

### 5단어 이하 적용 시점

| 시점 | 예시 |
|---|---|
| 권력자 단일 명령 | "Up." / "Sit." / "Stop." / "Out." / "Mine." |
| 결정 발화 | "Wife." / "Tonight." / "Done." / "Yes." |
| 즉각 응답 | "I won't." / "I do now." / "All right." |
| 양자택일 강요 직전 정지 | "Stay. Or go." |
| 광기·억압 발화 | "No one looks." / "Touch her and you die." |

→ 자연 spoken English 안에서 짧음. **억지 압축 X.**

### 5-10 단어 default 사용 시점

| 시점 | 예시 |
|---|---|
| 일반 dialogue | "He doesn't get to look at you." (8단어·자연) |
| 감정 표현 | "I have wanted you for nine weeks." (8단어·자연) |
| 정보 전달 | "Your father's two corridors away. Writing your name." (분할·자연) |
| 관계 발화 | "I'd burn this room. The keep. Your father's wing. The world. If she costs me you." (분할·자연) |

## 회피 패턴

### 패턴 1: 부자연 압축
- ❌ "Her no holds. Her names cost hands." (관용 X·코미디 위험)
- ✅ "If she says no, it's no. She names you, I take the hand." (자연 spoken·12단어)

### 패턴 2: 번역투
- ❌ "It isn't a court piece. It's a piece." ("piece"의 의미 모호)
- ✅ "It's not a crown. It's just a mark." (10단어·명확)

### 패턴 3: 문법 오류
- ❌ "If she cost me you." (시제 오류)
- ✅ "If she costs me you." (조건문 현재 시제)

### 패턴 4: 의미 오독 위험
- ❌ "He doesn't get the look." ("look" = 외모/시선 둘 다)
- ✅ "He doesn't get to look." (의미 명확)

### 패턴 5: 코미디 톤
- ❌ "I saw your hand on you. I saw his eye watching me see your hand on you yesterday." (반복·우스움)
- ✅ "I saw where your hand was. I saw him watching me figure it out." (자연·15단어)

### 패턴 6: 깨진 파편 영어
- ❌ "Hide you. Mine. No one." (원시인 영어)
- ✅ "Hide you. Mine. No one else looks." (자연·짧지만 문법 OK)

## 자가 검수 (영어 대본 모든 발화)

1. **이 발화 = 자연 spoken English인가?** (배우가 낮은 소리로 말해도 자연)
2. **문법 정확한가?** (시제·관용·전치사)
3. **5단어 이하 = 권력자 명령·결정·즉각 응답 한정인가?** (일반 dialogue까지 5단어 강제 X)
4. **번역투·관용 부재·의미 오독 위험 0건인가?**
5. **깨진 파편 영어·원시인 영어 0건인가?**

→ 1개라도 NO = 발화 정정.

## 원어민 polish 절차

1. 본문 모든 영어 발화 검수
2. 5단어 이하 강제 = 명령·결정·응답 한정 적용
3. 일반 dialogue = 5-10 단어 자연 spoken으로 정정
4. 문법·관용·번역투 일괄 점검
5. 최종 = 원어민 1회 polish (외부 인력 또는 별도 검수)

## OFFERING V16 → V17 정정 항목 (참고)

| EP | V16 | V17 |
|---|---|---|
| EP07 | "She speaks for me. Her no holds. Her names cost hands." | "She speaks for me. If she says no, it's no. She names you, I take the hand." |
| EP08 | "My lords saw you. At my table. They asked you. Not me." | "They saw you at my table. They asked for your name. Not mine." |
| EP16 | "I don't owe his court the picture of his crown on my head." | "I don't owe his court the sight of me in his crown." |
| EP16 | "It isn't a court piece. It's a piece." | "It's not a crown. It's just a mark." |
| EP17 | "He doesn't get the look." | "He doesn't get to look." |
| EP20 | "I saw your hand on you. I saw his eye watching me see your hand on you." | "I saw where your hand was. I saw him watching me figure it out." |
| EP31 | "Every day I look like this." | "I look at you like this every day." |
| EP39 | "If she cost me you." | "If she costs me you." |

## 옛 시스템 룰과 정합

- `feedback_dark_romance_v2_5_v13_lessons.md` (V13 시적 톤 정정) — 본 룰과 정합·"≤5단어 강제" 완화.
- `feedback_dangerous_sweet_cage_insights.md` (BL captive baseline·1-3 단어 명령형) — 권력자 명령 한정·일반 dialogue는 5-10 단어.
- `config/hard_rules.md` 룰 8 (Spoken English 원어민 polish).

## 절대 한 줄

> **Spoken English default = 5-10 단어 자연. 1-3 단어 = 명령·결정·즉각 응답만. 5단어 강제 = 원시인 영어 신화.**

관련: [[dark-romance-v2-5-v13-lessons]] / [[dangerous-sweet-cage-insights]] / [[screen-rhythm-v3-blocks]] / [[female-gaze-camera-polish]]
