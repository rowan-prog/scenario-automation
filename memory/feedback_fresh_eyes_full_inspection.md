---
name: fresh-eyes-full-inspection-method
description: 진짜 전수검사 = diff/체크리스트/자가재독 X → 사전결론 모르는 fresh-context 검수자 병렬(Workflow) + 메인이 원문 대조 종합. 자가검수는 같은 사각 반복. (2026-05-29 사용자 명시)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2d145cfe-e9c6-438b-bd5e-5d876492e4d8
---

자가 "전수검사"는 스캔이지 심문이 아니다. **같은 모델이 같은 눈으로 다시 봐도 자기 사각(문학편향)은 매번 그냥 통과시킨다.** diff는 *바뀐 줄*만, 체크리스트 대조는 *목록에 있는 것*만 본다 → **안 바뀐 줄에 원래 있던 문제는 영영 못 잡음.** 그건 전수검사가 아니다.

**진짜 전수검사 프로토콜:**
1. 내 사전 결론을 *전혀 모르는* **fresh-context 검수자 여러 명 병렬**(Workflow): 구간별 line-by-line(native English/logic/voice/쾌감) + 전편 횡단 1명(연속성·타임라인·셋업/회수·소품·부상 연속성).
2. 각 검수자 = adversarial("문제 있다고 가정, 그냥 넘기지 마라"). 의도된-설계 목록을 줘서 거짓양성 줄임.
3. **그다음 메인 에이전트가 전 지적을 원문과 1:1 대조** → 거짓양성 제거 + 의도된 것 보존 + 종합.

**증거(SHE STOLE v34):** 내가 *두 번* "클린"이라 한 본문에서 fresh eyes가 **HIGH 모순 3건** 잡음 — 그중 둘은 *내 수정이 만든 것*(EP06 Tessa 자백이 EP01 클리닉·EP05 "old code"와 모순) + 펜던트 회수 컷 누락. 71 raw findings 중 HIGH 3·MED ~13·LOW ~15 실제 수정, 나머지는 의도된 것/거짓양성.

**룰:** 어떤 작품이든 LOCK 선언 전 최소 1회 fresh-context 외부 패스. self "clean" 도장 단독 신뢰 금지. (사용자: "니가 똑같은 문장을 보고도 이전엔 몰랐다가 다시 알 수 있잖아 — 그 전수검사를 했냐고.")

**정식 agent화 (2026-06-05):** 이 프로토콜은 `~/.claude/agents/fresh-eyes-auditor.md` 전용 agent로 정착 (횡단 스윕 체크리스트 9항 내장·가드레일 입력·보고-전용). 운용 = [[agent-roster-orchestration]]. Link [[claude-voice-bias-vertical-failure]] [[voice-lint-gate-pass]] [[easy-dopamine-over-logic]].
