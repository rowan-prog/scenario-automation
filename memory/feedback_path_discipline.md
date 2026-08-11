---
name: path-discipline
description: 사용자에게 경로를 말할 때는 언제나 절대경로 — 모든 작업 공통. 파일 생성 시에도 프로젝트 루트 기준 절대경로로 검증
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 87890a95-6938-4d92-9f90-4a8451f3f413
  modified: 2026-08-07T04:12:04.199Z
---

**경로를 사용자에게 보고·언급할 때는 예외 없이 절대경로로 쓴다.** `06_reviews/foo.md`가 아니라 `C:\Users\Rowan\scenario-automation\projects\25_billion_dollar_reset\06_reviews\foo.md`. 산출물 보고, 대화 중 언급, 문서 안의 포인터 전부 해당한다. **이 워크스페이스만이 아니라 모든 작업에 적용된다** (2026-08-07 사용자 재지시 — 반복 지적).

**Why:** 상대경로는 내 cwd를 아는 사람에게만 유효하다. 사용자는 탐색기·다른 창·다른 세션에서 그 파일을 여는데, 상대경로는 거기서 못 쓴다. 매번 루트를 되짚게 만드는 비용을 사용자에게 떠넘기는 것이고, 이미 여러 번 지적받았다.

**How to apply:**
1. 작업 결과 보고에 경로가 들어가면 **무조건 풀 경로.** "문서는 `06_reviews/...`에 있습니다" 금지.
2. 파일 생성·저장 시에도 프로젝트 루트(`C:\Users\Rowan\scenario-automation`) 기준 절대경로로 도구를 호출한다. prompt 템플릿이 `projects/...` 상대표기를 써도 호출 시엔 변환.
3. 생성 직후 위치를 검증한다 — 한 단계 더 들어가 있으면 즉시 정정.
   - 실증(2026-05-07): cwd가 `projects/03_black_core/`인 상태에서 상대경로 `projects/04_buried_heir/`를 써서 `projects/03_black_core/projects/04_buried_heir/`에 빈 골격만 생성. 사용자가 발견할 때까지 묻혀 있었다.
4. 다른 작품 폴더 안에서 작업 중이라도 새 작품 골격은 루트의 `projects/` 직속에 만든다.

관련 = [[script-file-zero-meta]] [[no-ai-korean-jargon]]
