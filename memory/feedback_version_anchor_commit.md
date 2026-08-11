---
name: anchor-commit
description: 정본 file에 큰 변경 (사용자 피드백·turn 단위) 적용 시 사전에 git commit 또는 새 버전 file로 분기 강제. v34→v35 분기 시점 놓침 학습.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5b24965b-34a4-4256-9501-24e4b73f8ff5
---

**룰: 정본 file에 turn 단위·사용자 피드백 단위 변경 적용 시 사전에 version anchor 잡기.**

**Why:**
> 2026-05-22 OFFERING v34 작업 중 — Turn 1-5 자율 작업으로 v34_clean.md 만들고 (untracked) → 사용자 종합 피드백 받자마자 같은 file에 직접 덮어씀 → v34 base 단독 보존 못 함 (git history 없음). 사용자 "v35 또는 v34_2 했어야지" 지적. 분기 시점 놓침 = 큰 실수.

**How to apply:**

1. **새 정본 file 첫 생성 시** = 즉시 git commit 으로 base anchor 잡기. (untracked로 두지 X)
2. **사용자가 종합 피드백·새 charter·전면 수정 요청할 때** = 적용 전 새 버전 file로 분기 (v34 → v35_clean.md cp 후 v35에 작업).
3. **Turn 단위 큰 작업 (5+ EP 재작성) 시작 시** = 직전 commit anchor 잡고 진행. 끝나면 다시 commit.
4. **사용자 명시 "버전 관리해" 룰**: 메이저 변경 = `v{N+1}_clean.md`로 cp 후 작업. 마이너 patch = `v{N}_clean.md` 그대로.

**판단 기준:**
- 메이저 (= 새 버전): EP 전면 재작성·구조 변경·캐릭터 charter 신규·플랜 전환·사용자 종합 피드백 단위 patch
- 마이너 (= 같은 버전): 단어 1-2개·헤더 조정·typo·grammar·인용 한 줄

**관련:** [[meta-trust-and-verify]] · [[no-ask-autonomous]]
