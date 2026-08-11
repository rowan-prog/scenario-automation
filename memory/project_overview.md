---
name: scenario-automation 프로젝트 개요
description: scenario-automation 작업 공간의 목적과 폴더 구조 — 어떤 워크플로우를 자동화하려는지 파악할 때 참고
type: project
originSessionId: 087d1256-7199-41d6-b823-241fa8462734
---
`C:\Users\Rowan\scenario-automation`은 AIGC 시나리오 제작 워크플로우 자동화를 위한 작업 공간이다.

워크플로우 단계:
1. 블루프린트 작성 (1.1 러프 → 1.2 풀 → 1.3 에피소드 집필)
2. 피치덱 (2.1)
3. 페르소나 검토 (3.1)
4. 개정 (4.1)

폴더 구조:
- `config/` — 모든 작품에 공유되는 공통 설정. `production_guide.md`(AIGC 제작 가이드), `visual_lock_template.md`(비주얼락 템플릿), `personas/`(검토 페르소나 정의), `reference_scripts/`(참고 대본)
- `prompts/` — 각 단계별 프롬프트 템플릿 (step_X_Y_*.md)
- `projects/` — 개별 작품 폴더가 들어가는 곳

**Why:** 사용자가 2026-05-07에 한국어로 직접 폴더 구조를 설계해 요청. 현재는 뼈대(placeholder)만 있고 내용은 추후 채워나갈 예정.

**How to apply:** 이 프로젝트에서 작업 요청을 받으면 한국어로 응답하고, 단계 번호(예: "1.2", "phase_2")를 위 매핑대로 해석할 것. 새 작품 작업은 `projects/<작품명>/` 아래에서 진행.
