---
name: fable-structure-only-pipeline-self-sufficient
description: 파이프라인은 opus/sonnet/haiku로 자급 — Fable은 구조·룰 개정 때만 1회성. 판정 = 체크리스트 명문화(20_review §4-1).
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3aeff9c0-83f4-4500-aec7-c6aa7899e985
  modified: 2026-07-22T09:35:08.401Z
---

사용자 지시 (2026-07-06): "fable5로 구조를 다 짜라. 이후에는 fable이 할 필요 없게. 내가 모델을 opus로 바꿔도 동작하도록. opus이하/opus/sonnet/haiku로만 굴러가게. fable 너무 많이 쓴다."

**Why:** Fable은 비싸고, 구조가 제대로 짜였다면 실행·판정은 절차로 내려갈 수 있다. "메인의 감으로 판정"이 남아 있는 상태 = 구조가 덜 짜였다는 신호다. 같은 날 실증: 38화 교체안 "넌 안 무너져"를 내 감으로 통과시켰다가 사용자에게 은유("빗댄 말")로 잡힘 → 은유 판정 기준("물리 동작/사물로 직접 그려지는가")을 §4-1 체크리스트에 명문화.

**How to apply:** ①감으로 판정한 게 있으면 그 판정 기준을 즉시 workspace 룰로 명문화(실증 = `config/20_review_standard.md` §4-1 수술 파이프라인·머지 체크리스트) ②세션 모델이 Fable이면 "구조/룰 개정 작업인가?" 먼저 물을 것 — 아니면 opus 이하로 충분한 일 ③문서의 역할 규정은 모델명이 아니라 "세션 모델(opus 기준 설계)"로 쓴다. 관련: [[agent-orchestration-tier-map]] [[token-diet-70-percent]] [[bulk-script-verify-strict]].

**개정 (2026-07-22 사용자):** "내가 모델 fable5할 땐 니가 판단해서 subagent는 fable / opus / sonnet 알아서 배분하쇼." — 세션 모델이 Fable이면 그건 사용자가 이미 비용을 선택한 것이므로, subagent 배분에 Fable 티어를 **포함해** 내 판단으로 배분한다(단독 정밀 발견·프로스 집필/수술 최상급 = fable 승격 후보, 나머지는 기존 티어맵 유지). agent frontmatter 핀은 호출 시 `model:` 파라미터로 override. 기존 원칙(세션이 opus 이하일 땐 opus/sonnet/haiku 자급)은 그대로 유효.

**실증 판례 (같은 날 · 14 While My Wife's Away phase_p):** fable 유닛 승격 2건 중 트리트먼트는 보강 0 반환(= "덜 쓰는 게 정답"인 유닛 — 가드레일이 품질을 만들지 티어가 만들지 않음), 창작 코어도 로드베어링 결정(주체·심리 결·내용요건 기준·문체)은 전부 사용자 문답에서 나왔고 메인 단독 감-판정은 오판(남성향 판타지 문법). → **phase_p = Fable 불요 확정·트리트먼트 = sonnet 하향·0단계 설계 확정 문답 신설**(`prompts/phase_p_platform_proposal.md`). 승격 판단 기준: "가드레일·선행 문답으로 환원 안 되는 단독 창작 정밀도"가 증명된 업무만 — 티어를 올릴 돈으로 선행 문답을 사라.
