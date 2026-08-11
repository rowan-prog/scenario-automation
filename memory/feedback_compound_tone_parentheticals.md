---
name: compound-tone-parentheticals
description: "중요 대사·핵심 씬·캐릭터 결을 드러내는 라인에는 compound 톤 지문 필수. `(sweet, cruel)` 처럼 두 단어 paradox로 캐릭터의 본질 capture."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37994db2-a795-4d48-9fe7-5e1a796a2110
---

# Compound Tone Parentheticals — 중요 대사 톤 지문

**룰:** 모든 작품 대본에서 다음 3 조건 중 하나라도 해당하는 대사에는 톤 지문 (parenthetical direction) 필수:
1. **중요 대사** — paywall payoff·reveal·cliffhanger·승부 라인
2. **중요 씬** — 약혼 파국·정체 폭로·인질 협박·고백·결말
3. **캐릭터 결이 분명하게 드러나는 라인** — 빌런의 본질·주인공 변곡·페르소나 contradiction

**Why:** 사용자 명시 (2026-05-28). 좋은 대사도 톤 지문 없으면 배우/AI 보이스가 잘못 해석할 위험. 특히 vertical drama = AIGC 보이스 합성·배우 단명 컷·0.1초 안에 캐릭터 voice 전달. Compound paradox (`sweet, cruel`) = 한 단어로는 못 잡는 캐릭터 본질 capture. Stage direction 부족 = director's coverage 부족 = 매출 약화.

**🚨 2026-06-05 사용자 강화 (커버리지·적확성·차별화):**
1. **커버리지 확대:** "중요 라인만" → **정말 평이한 기능 라인을 제외한 모든 대사에 1-2단어 지문.** 비영어권 제작자의 톤 오생성 사고가 실제로 왕왕 발생 — 지문이 유일한 방어선. 생략 기준 = "어떤 톤으로 읽어도 같은 장면이 되는 라인"만.
2. **적확성 > 평이함:** 지문 단어는 짧고 쉬운 단어에 혈안되지 말 것 — 그 뉘앙스를 정확·적확하게 전달하는 단어로. `(wistful)` `(seething)` `(brittle)` OK / `(angry)` `(sad)` 뭉툭 도배 금지. **대사 본문 = 짧고 쉬운 직설 / 톤 지문 = 적확한 단어 — 두 기준을 섞지 않는다.**
2-1. **진짜 목적 = 오독 쉬운 층위 (같은 날 사용자 정정):** 기본 감정(화남·슬픔)은 오독이 어렵다 — 액션/문맥이 운반하면 생략 가능. 지문이 반드시 잡아야 하는 건 **비아냥·음흉함·통제된 욕망·상처를 숨긴 말투·장난과 위협이 섞인 층·섹드립·섹시·요염함·한 차원 위 복합 감정**. 이런 라인의 지문 누락 = 결함·기본 감정 도배 = 잡음.
3. **캐릭터 간 보이스 차별화 연동:** 역할이 전혀 다른 인물이 같은 말투 = 집필 실패. 영어 자연스러움과 별개 검사 축. engine brief §3 보이스 락에 인물별 말투+톤 지문 어휘대 고정·**name-cover test**(이름 가리고 화자 구분)·검수 = native-ear voice-collision 항목. 집필+검토 양쪽 적용.

**How to apply:** 매 phase_4 (집필)·phase_5·6 (검토·패치) 시 다음 grep + 3 조건 sweep:
- paywall EP·hook end 줄 화자 라인 → 톤 지문 100%
- 빌런 등장 시 → 톤 지문 90%+ (`sweet, cruel` 류 paradox 강력 추천)
- 메인 캐릭터 첫 등장·첫 declaration → 캐릭터 voice 정의하는 톤 지문 필수
- 짧은 declaration·single-line 큰 비트 → 톤 지문 우선

---

## 사용자 명시 예시 (모델)

```
SERA (sweet, cruel): He'll use you once and send you downstairs.
```

→ 두 형용사 compound paradox로 빌런 voice 본질 (다정한 톤으로 잔인한 진실 던지기) 한 줄 capture.

---

## Compound 톤 카테고리 (작성 시 참고)

### 빌런 voice (paradox 권장)
- `(sweet, cruel)` — 다정한 톤으로 잔인한 말 (대표 패턴)
- `(soft, possessive)` — 모성·소유욕 동시
- `(calm, clinical)` — 차분한 작전가
- `(matter-of-fact)` — 비즈니스 톤 살인 결정
- `(quiet command)` — 부드러운 지시·복종 압박
- `(maternal, menacing)` — 어머니인 척 위협

### 주인공 변곡 voice
- `(quiet)` — 큰 분노가 작은 목소리로 (frozen fury)
- `(small, direct)` — 약함과 정직 동시
- `(cracking)` — 무너지는 중간 지점
- `(barely audible)` — 무너진 직후
- `(level)` — 모든 감정 잠근 후의 통제
- `(flat)` — ice block

### 거짓말·연기 voice
- `(calm, lying)` — 침착하게 공개 거짓말
- `(thin, daring)` — 약한데 도발
- `(in [name]'s voice, [adj])` — 다른 사람 흉내내기
- `(flat, public)` — 공적 자리의 차가운 인정

### 약자·궁지 voice
- `(brittle)` — 곧 깨질 우아함
- `(small)` — 무너진 자존심
- `(coaxing)` — 사람 다루는 톤 (manipulative)
- `(blank)` — 영혼 빠진

---

## SHE STOLE MY FACE v25 → v26 적용 예시 (2026-05-28·20 패치)

| EP | 화자 | 라인 | 톤 지문 |
|---|---|---|---|
| EP01 | LENA (cemetery) | Mom. I'm getting engaged tonight. | `(quiet)` |
| EP01 | ETHAN | You're late. | `(flat)` |
| EP01 | ETHAN | For me. | `(coaxing)` |
| EP01 | MARA (reveal) | Looks better on me anyway. | `(sweet, cruel)` ⭐ |
| EP08 | MARA (paywall) | Don't have to say anything. | `(thin, daring)` |
| EP10 | LENA | No. You knew. | `(quiet)` |
| EP10 | VICTORIA | I had questions. Not knowledge. | `(brittle)` |
| EP10 | VICTORIA | You are your mother's daughter. | `(small)` |
| EP10 | VICTORIA | I wasn't being kind. | `(flat)` |
| EP10 | MARA (on screen) | She paid me. Lena paid me. | `(calm, lying)` |
| EP15 | VICTORIA (press) | Woman at the reception was not Lena. | `(flat, public)` |
| EP15 | VICTORIA | I chose not to see her. | `(small, direct)` |
| EP15 | VICTORIA | Part of me was glad… | `(barely audible)` |
| EP15 | MARA (playback) | Hi sweetheart. Borrowed a sweater. | `(in Lena's voice, cheerful)` |
| EP37 | EILEEN | I gave you a purpose. | `(sweet, cruel)` ⭐ |
| EP37 | EILEEN | Has to sound like you for one news cycle. | `(matter-of-fact)` |
| EP37 | EILEEN | Sit down, Mara. | `(quiet command)` |
| EP37 | EILEEN | You'll come back. You always have. | `(soft, possessive)` |
| EP40 | EILEEN (threat) | You choose. Come to the building. | `(calm, clinical)` |
| EP40 | EILEEN | Mara was always going to die in a fire. | `(soft)` |

---

## 금기

0. **🚨 cue는 상위 룰 [[ai-dub-tone-independent-dialogue]]의 *하위 층*이다 (2026-06-08).** cue는 *이미 한 가지 의미로 수렴한 문장* 위에 얹는 색칠/안전망일 뿐이다. **톤이 의미를 결정하는 문장(반어·이중의미·의미심장·애매)을 cue로 구제하려 하지 마라** — AI 더빙은 cue 뉘앙스도 못 살릴 수 있다. 순서 = ①문장을 톤-독립 단일 의미로 먼저 고친다 → ②그 위에 1-2단어 톤 cue를 얹는다. cue가 없으면 의미가 뒤집히는 대사 = 집필 실패(문장을 고칠 것).
1. **지문 폭주 금지** — 매 줄 지문 X. 대화 흐름 self-evident할 때는 skip. 평균 EP당 2-4개 정도가 healthy.
2. **부사 1개 짜리 지문 약함** — `(angry)`·`(sad)` 같은 단순 형용사 X. 구체적·paradox·물리적 (예: `(jaw tight)`·`(hand on phone)`).
3. **씬 지문이 대신 못 함** — 액션·지시 라인 (`Slams door.`)은 dialogue 톤 지정 못함. dialogue 자체에 톤 지문 필요.
4. **Voice character 일관성** — 한 캐릭터의 톤 지문은 series 전체에서 voice 일관성 유지. Eileen은 `(sweet, cruel)`·`(soft, possessive)`·`(calm, clinical)` 계열. Victoria는 `(brittle)`·`(small)`·`(flat)` 계열.

---

## 관련 메모리

- [[ai-dub-tone-independent-dialogue]] — 🚨 상위 룰. cue 이전에 문장 자체가 톤-독립 단일 의미여야 (AI 더빙 제약)
- [[real-human-speech-01s-test]] — 0.1초 perception test (대사 자체 검토)
- [[no-theater-tone]] — 연극톤 회피
- [[revision-meta-principles]] — 캐릭터별 voice 차별화 (룰 #9)
- [[claude-voice-bias-vertical-failure]] — Claude default = 문학적 편향
