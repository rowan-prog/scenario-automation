---
name: script-file-zero-meta
description: FINAL/EP 대본 파일 = 타이틀 + 본문만. 헤더 spec·버전 노트·작업 과정 설명 일절 금지 (2026-06-04 사용자 지적)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 34f9a729-3a27-46b3-88c6-6adbcdc42e22
---

FINAL/EP 대본 파일 안에는 **타이틀과 본문 외에 아무것도 넣지 않는다.** 헤더 spec 라인(화수·페이월·타깃), 버전·양식 패스 작업 노트, 검증 수치, 환류 로그 전부 금지. 그런 정보는 `00_meta.md`·CLAUDE.md·핸드오프 문서에만 쓴다.

**Why:** 2026-06-04 사용자 직접 지적 ("대본에 메타적인 이상한 거 넣지 말아줄래? 작업 과정이나, 이런"). SHE STOLE MY FACE v39 양식 패스 때 내가 파일 머리에 박은 2줄 blockquote(spec + 재태깅 작업 설명)를, 그 후 "철저한 전수 검토"를 자처한 패스들(자가 QC + fresh-eyes 6렌즈 포함)이 한 번도 못 잡았다. 변명 불가 — "전수"라면서 파일 머리/꼬리를 스코프에서 빼고 본문 차원만 검수 설계한 내 잘못. 사용자가 직접 발견했다.

**How to apply:** ①정본/EP 파일 생성·통합 시 첫 줄 = `# [작품명]`, 둘째 비트 = 바로 EP01 본문 ②양식/버전 정보는 meta 파일에만 ③**모든 전수 검토·QC·LOCK 직전에 파일 위생 스윕 의무화: 파일 head/tail 직접 Read + 본문 블록([VISUAL/ACTION] 등·GRAPHIC/UI 훅 제외) 밖 blockquote/로그/spec 라인 grep — 10초짜리 기계 점검을 스코프에 박는다** ④발견 즉시 제거. [[no-ai-korean-jargon]] [[fresh-eyes-full-inspection-method]]
