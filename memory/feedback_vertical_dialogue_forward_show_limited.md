---
name: vertical-dialogue-forward-show-limited
description: "\"Show, don't tell\"은 vertical drama에 한정적·기본값으로 쓰면 끔찍. Vertical = 대사-forward(인물이 말로 장면 소유·loud/직설/막장). 무성 show로 장면/감정/reveal/파워무브 carry = 비직관(모바일)+AI더빙 실패+광고컷 실패. 영화 \"show don't tell\" + claude 문학-show 편향 override. 단 지문은 여전히 clean action·대사-forward≠wordy."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2232c2a-2d77-4cdb-97dc-f680b25e871b
---

# "Show, don't tell"은 vertical엔 한정적 — vertical은 대사-forward (2026-06-10 사용자 명시)

> 사용자: "show and don't tell은 한정적이다. 끔찍한 문법이다. 대사 없이 끌고갈려는건 비직관적이다. 광고컷으로도 안 먹힌다. vertical을 이해하자."

## 핵심
- **"Show, don't tell" = 영화/프레스티지TV 문법. vertical엔 한정적 — 기본값으로 쓰면 끔찍.** 무성 비주얼/서브텍스트로 관객이 *추론*하게 하는 방식 = 모바일 vertical에서 비직관적.
- **Vertical = 대사-forward.** 인물이 *말로* 장면을 소유한다 — 갈등·감정·reveal·파워무브를 *소리내어 직설로*(loud·막장). 장면의 1차 엔진 = 대사.
- **무성 show로 carry하려는 것 = 3중 실패:** ①모바일 시청자 비직관(0.1초에 안 박힘) ②**AI 더빙(TTS)이 못 살림**(소리가 의미를 운반) ③**광고컷 안 먹힘**(피드 hook = 대사/소리로 잡힘·무성 비트 = 광고가치 0).
- **claude 문학-show 편향의 직격 교정.** 나는 restraint·subtext·visual로 default → vertical 정반대. [[claude-voice-bias-vertical-failure]]의 핵심 발현.

## 직관성의 진짜 정의 — cold-scene graspability test (2026-06-10 사용자)
- **"직관적·이해·설정 최소화"의 operational test:** 중간 *아무* EP/씬이나 잘라 *처음 보는 사람*에게 줘도, 어지간해선 ①앞에 무슨 일이 있었는지 ②앞으로 일어날 일 ③인물 관계를 *바로* 파악 가능해야 한다. **Vertical은 이래야 한다.**
- 왜: vertical 시청자는 광고/피드에서 *중간 진입*이 상시 → **매 씬이 스스로 오리엔트**(대사·상황이 backstory+stakes+관계를 그 자리서 전달).
- **"설정 최소화" ≠ 맥락 제거.** 복잡 lore/메커니즘을 최소화하라는 뜻이지, 맥락을 *빼라는* 게 아님 — 맥락은 *단순하게* + *매 씬 재전달*. (이래서 대사-forward 필수: 무성 show는 cold 시청자를 오리엔트 못 한다.)
- 검수: 임의 씬 1개를 cold로 읽어 before/after/관계가 안 잡히면 = 그 씬이 직관성 실패. funnel-cold-reader가 이 test의 도구.

## 단어 도배 금지 — 직설 ≠ 토막 (2026-06-10 사용자 재강조)
- **"말을 무작정 짧고 단어로 말하는 머저리같은 짓" 금지.** short는 목표가 아니다([[no-theater-tone]]: 인간 호흡 묶음 우선). 토막 나열(`One X. One Y. My Z.`)·단어 fragment = 자동 폐기.
- **대사-forward + 직설 = *자연스러운 완결 구어 문장*으로 한다**(인간이 실제로 말하듯). 짧게 *깎는* 게 아니라 쉽게·직설로.
- **🚨 spoken English에 사활.** 번역투/문어/연극투 0·원어민 귀로 자연([[spoken-english-native-polish]]·[[real-human-speech-01s-test]]·[[native-ear-reviewer]]).

## 혼동 금지 — 지문 vs 장면-carry
- **이건 "지문에 감정라벨 써라"가 아니다.** 지문(△)은 여전히 *clean functional action*(감정라벨·소설장식 X — [[emotion-to-action-aigc-writing]]).
- 차이: **지문은 대사를 *보조*하지 *carry* 안 한다.** 장면을 끄는 건 대사. "감정을 깨끗한 동작으로 쓴다"(지문 품질) ≠ "장면을 무성 동작으로 끈다"(함정).
- **대사-forward ≠ wordy.** 직설·짧음·쉬움·spoken 유지([[real-human-speech-01s-test]]·[[ai-dub-tone-independent-dialogue]]). 인물이 *그 말을 한다* — 단 plainly·막장으로.

## How to apply
- **집필:** 감정 turn·reveal·파워무브·관계 비트 = 인물이 *말로* 한다. "이건 보여주기만 하면 되지" 충동 = vertical에선 기각.
- **검수:** 무성 show가 장면/감정/reveal을 carry = B-failure(over-show) → 즉시 대사 부여(주인공이 owns). 단 막장/직설 한 줄(wordy X).
- **광고컷 선별:** hook 컷은 대사/소리 있는 비트 우선.

관련: [[claude-voice-bias-vertical-failure]] · [[vertical-protagonist-voice-ownership]](말로 장면 소유) · [[ai-dub-tone-independent-dialogue]] · [[emotion-to-action-aigc-writing]](지문=clean action·혼동 금지) · [[na-vertical-ad-creative-principles]] · [[lock-fix-volume-writing-diagnostic]].
