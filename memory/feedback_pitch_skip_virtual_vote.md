---
name: pitch-skip-virtual-vote
description: 사용자가 피칭덱 가상투표(evaluator-panel 위원 7인)·페르소나 자동검수를 원치 않음 — 피칭덱은 사용자가 직접 읽고 판단. 자동으로 돌리지 말 것.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 442bf4a9-1df5-4973-82d3-9c1240f3b5ca
---

2026-06-23 사용자: "가상투표 같은 거 하지마 그냥 내가 읽을라니까."

피칭덱(또는 청사진) 작성 후 evaluator-panel(위원 7인 가상투표)·페르소나 패널을 **자동으로 돌리지 않는다.** 사용자가 직접 읽고 평가한다.

**Why:** 가상투표 예측 정확도가 낮고(`config/pitch_references/MASTER_DATASET.md` §E — 사용자 "하나도 안 맞는다"), 사용자가 본인 직독 판단을 선호한다. [[pitch-master]]의 4단계 자동 워크플로우 중 3·4단계(위원·페르소나)는 *사용자 명시 요청 시에만* 수행.

**How to apply:** 피칭덱 산출 = 작성 + 비문/내적 정합성 자가검수까지만 하고 경로+한 줄로 보고. 위원 가상투표·시청자 페르소나 패널은 사용자가 명시적으로 요청할 때만. 관련 [[token-diet-70-percent]] [[no-ask-autonomous]].
