---
name: ai-dub-tone-independent-dialogue
description: AIGC = AI 영상 + AI 더빙(TTS) 둘 다. 대사는 톤과 무관하게 한 가지 의미로 수렴해야 한다. 톤이 의미를 결정하는 대사(반어·이중의미·의미심장·애매)는 AI 더빙이 못 살림. 짧음과 무관. 미세 표정연기 의존 지문도 제한.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2232c2a-2d77-4cdb-97dc-f680b25e871b
---

# AI 더빙 톤-독립 대사 — AIGC 집필 최상위 제약

**룰 (2026-06-08 사용자 명시·전 작품·집필+검토 양쪽):**
우리 산출물은 **AI 영상 + AI 더빙(TTS)** 둘 다로 제작된다. 두 가지를 동시에 제한해야 한다:

1. **대사 = 톤과 무관하게 한 가지 의미로 수렴(tone-independent / single-meaning).** flat하게 읽혀도 의미가 안 바뀌는 문장. 위협은 위협으로, 고백은 고백으로, 조롱은 대상을 호명하며 읽힌다. **톤이 *의미*를 결정하는 대사(반어·sarcasm·이중의미·의미심장·불분명·withheld subtext)는 AI 더빙이 의도대로 못 낸다.** cue를 붙이면 일부 보정되나, **문장 자체가 톤 의존적이면 cue로도 못 살린다.** → 의미를 톤이 아니라 *단어 + 물리적 행동*이 운반하게 쓴다.
2. **미세·섬세 표정연기 의존 지문 제한.** AI 영상은 베테랑 최상급 배우만 소화할 미묘한 미세 표정을 못 낸다. "묘한 표정"·"복잡한 얼굴"·"의미심장한 미소"·"unreadable"·"faint smile" 류에 *핵심 의미*를 걸지 마라. 서브텍스트는 무성 facial **insert + V.O.**로 외화하고 특정 샷(ECU 눈·crash zoom 등)으로 귀결시킨다.

**🚨 절대 오해 금지:** 이건 **"짧은 대사가 좋다"가 절대 아니다.** 긴 문장도 직설이면 한 의미로 수렴한다(히트작 다수가 3-6절 직설 대사). 반대로 짧아도 의미심장·암시형이면 실패다(危険な甘い檻 ML의 1-3단어 대사도 전부 *문자 그대로*의 명령/답/라벨이라 안전했다). 기준은 길이가 아니라 **의미 수렴**이다. 또 [[easy-dopamine-over-logic]]의 "어려운 문장 제거"와 결이 같지만 동일하지 않다 — 여기 핵심은 *톤 의존*이지 어휘 난이도가 아니다.

**Why:** AI TTS는 반어/풍자/이중의미/의미심장/애매를 신뢰성 있게 못 낸다. AI 영상은 미세 표정연기를 못 낸다. 둘 다 vertical 매출 라인을 0.1초 안에 전달해야 한다. 톤이 의미를 운반하면 그 대사는 제작 파이프라인에서 깨진다.

**How to apply (집필 phase_4 + 검토 패스 7·8):**
- 매 대사 3문 테스트: ①flat하게(무표정 TTS) 읽어도 같은 뜻인가 ②의미가 *톤*이 아니라 *단어+행동*에서 나오는가 ③지문이 "의미심장/묘한/복잡한 표정"에 핵심을 걸지 않는가. 하나라도 NO = 수술.
- 서브텍스트가 필요하면 톤에 맡기지 말고 **히트작 4 해소법** 중 하나로 외화: (a)짧은 톤 cue, (b)바로 다음 대사가 평문으로 재진술, (c)V.O./내레이션이 반어를 직접 말함, (d)이미 보여준 물리적 행동이 진의를 고정. (10개 히트작 전부 이 방식, 톤에 안 맡김.)
- cue(괄호 톤 지문)와의 관계 = **층위가 다르다.** cue는 *이미 한 의미로 수렴한 문장* 위의 색칠/안전망이다. **cue로 톤 의존적 문장을 구제하려 하지 마라** — 문장을 먼저 단일 의미로 고친 뒤 cue를 얹는다. 상세 = [[compound-tone-parentheticals]].
- 기계 1차 = `voice_lint.py` (MICRO_ACTING 지문 + 톤 의존 surface 탐지) → 사람/agent 의미 패스(native-ear-reviewer + 쇼러너)가 본질 판정. 톤 의존 *의미*는 기계가 못 잡으니 의미 패스 필수.

**실증 (2026-06-08·히트작 10개·미국 5 필수 포함):**
LOCKED OUT·Married the Don·How To Break My Best Friend's Dad·Billionaire Ex-Wife·Alta Reborn(이상 US 영어) / 도망쳐봐 내게서·추락한 K-pop·말할 수 없는 나의 신부·오늘 한류스타와 이혼하겠습니다(KR) / 危険な甘い檻(JP). **10/10 작품 모두 대사의 ~85-93%가 톤-독립 한 의미.** 반어/서브텍스트(~7-12%)는 예외 없이 위 4 해소법으로 외화. 짧음≠한의미 확인(危険 ML). cue 빈도는 작품마다 다르나(미국=희소·한국=조밀) 전부 1-4단어이며 *의미 운반자가 아니라 색칠/안전망*. 미세 표정은 무성 insert+V.O.로 외화. 분석 원본 = 본 메모리(요약) + 각 작품 `config/vertical_drama_hit_scripts_analysis/`(해당분).

## 관련 메모리
- [[compound-tone-parentheticals]] — 톤 cue(이 룰의 하위 층·문장이 먼저 단일 의미여야)
- [[easy-dopamine-over-logic]] — 어려운 문장/장치 제거(인접하나 축이 다름: 톤 의존 vs 어휘 난이도)
- [[real-human-speech-01s-test]] — 0.1초 perception test
- [[claude-voice-bias-vertical-failure]] — Claude default = 문학·서브텍스트 편향(이 룰의 정반대)
- [[vertical-protagonist-voice-ownership]] — reveal은 물건/암시 아닌 대사로
