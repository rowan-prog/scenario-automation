---
name: script
description: "정규식 일괄 변환 후 깨진 패턴 grep 검증 강제. v40 VO 변환에서 `VO (VO):`·`(VO): ## S#`·`(VO): Hard Cut`·인물명 중복 패턴 발생 학습. 사용자 매우 빡침."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5b24965b-34a4-4256-9501-24e4b73f8ff5
---

**룰: 일괄 변환 script (Python/sed/regex) 실행 후 = 깨진 패턴 grep 검증 강제 + 사전 dry-run.**

**Why:**
> 2026-05-22 OFFERING v40 작업 중 — 블록 양식 strict 5종 cleanup Python script 실행. VO 변환 정규식 매칭 부정확 → `VO (VO): ISOLDE: ...` (VO를 char로 잘못 매칭) / `PRIEST (VO): ## S#5 — ...` (장면 헤더가 VO 본문에 빨림) / `ISOLDE (VO): Hard Cut.` (컷 지시가 VO에 빨림) / `SERA (VO): SERA: ...` (인물명 중복) 등 13건 변환 오염 발생. 사용자 빡침: "양식 망가졌다. 빡친다." v41에서 repair pass로 정정.

**How to apply:**

1. **사전 dry-run**: 변환 script 실행 전 = 입력에서 모든 변환 대상 패턴을 grep으로 추출 + 변환 후 형태 미리 출력. 사용자에게 sample 5-10건 보여주고 OK 받은 후 실행.

2. **사후 grep 검증 (필수 패턴 0건 확인)**:
   - 잘못 변환된 prefix 흡수: `VO \(VO\):` / `(\(VO\):\s*##)` / `(\(VO\):\s*Hard Cut)`
   - 인물명 중복: `([A-Z]+) \(VO\):\s*\1:`
   - 장면 헤더 본문 빨림: `^##\s*S#` 카운트가 변환 전·후 같은지 확인
   - 컷 지시 본문 빨림: `(VO\):\s*Hard Cut)` / `(VO\):\s*Fade Out)` 0건
   - 허용 외 블록 0건 확인: `^\[[^]]+\]` sort+uniq → 허용 set과 비교

3. **세그먼트 1:1 정합**: EP 카운트 ↔ [END HOOK] 카운트 ↔ Hard Cut 카운트 = 1:1 정합 확인 (변환 시 중간 [END HOOK] 누락/추가 가능).

4. **블록명 통일성**: 사용자 명시 양식 = `[UI/GRAPHIC]` vs 내부 표기 `[GRAPHIC/UI]` 같은 약간 다른 표기 = 일관성 깨짐. 변환 후 = 사용자 정확 표기와 일치 확인.

5. **검증 실패 시 = 즉시 새 버전 branch (vN+1) + repair pass**. 옛 버전 그대로 두기.

**관련 메모리:** [[meta-trust-and-verify]] · [[version-anchor-commit]] · [[no-ask-autonomous]]

**+ 2026-09-01 (29번) — 한국어 문서에서 이름을 통째 치환하면 조사가 전부 깨진다.** 「엘레나」(모음 끝) → 「레이첼」(받침 끝)로 replace 하니 뒤따르던 조사가 13곳에서 깨졌다(레이첼**가**·레이첼**를**). 받침 유무가 바뀌는 치환은 **이/가 · 을/를 · 은/는 · 와/과 · (으)로 · 아/야**를 전수 재검사해야 한다. grep 패턴 = `<새이름>[가를는와]`(받침 있는 이름으로 바꿨을 때) / `<새이름>[이을은과]`(받침 없는 이름으로 바꿨을 때). 사용자가 계속 지적하던 "이상한 문장"을 수정 작업이 새로 만들어 넣는 전형 — **치환 후 검증 없이 보고하지 말 것.**
