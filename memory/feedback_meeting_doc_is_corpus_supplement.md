---
name: meeting-doc-is-corpus-supplement
description: "사용자가 미팅 문서(피칭덱·기획안 실물)를 \"하나 더 준다, 참고하라\"고 주면 = 같은 양식의 데이터 보완. 코퍼스에 넣고 사람들이 실제로 쓰는 근거·숫자를 뽑아 표준에 보탠다. 새 규칙 발명·다른 양식 취급 금지."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: dedf0c27-08b7-4376-8681-598c5d78ac84
  modified: 2026-09-07T10:12:37.385Z
---

2026-09-07 「2026-09-03 신규 작품 제작 결정 미팅」 Confluence 내보내기를 받았을 때 사용자 교정 2건:
- *"같은 양식인데, 데이터 보완하란 의미야."*
- *"인사이트 얻어서 제대로 쓰라고. AI같이 이상한 논리, 이상한 데이터 끌고와서 이상한 글 써대지 말라고."*

**Why:** 표준(`config/60_pitch_page_standard.md`·`pitch_page_examples.md`·`pitch_page_corpus/`)은 실물 census 위에 서 있다. 실물이 하나 더 오면 할 일은 ①코퍼스에 추가 ②사람들이 실제로 어떤 근거·숫자를 갖고 오는지(자사 광고 지표·원작 플랫폼 실적·자사 설문·시즌 연속) 뽑아 표에 보태기 ③기존 규칙과 어긋나는 실물이 있으면 그 자리만 고치기. 목적은 내가 피칭 페이지를 쓸 때 AI스러운 논리(대본 장면 상찬·성장 일반론·검증됐다는데 대상 없음)와 발명한 숫자를 안 끌고 오는 것이다.

**How to apply:**
- 미팅 .doc(MHTML) → `python tools/confluence_mhtml_to_txt.py <doc> config/pitch_page_corpus/deck_YYYY-MM-DD.txt` → `tools/pitch_page_lint.py` CORPUS_FILES에 추가 → `--stats`로 실측.
- 표준 갱신 = §0 표에 엔트리 행 추가 + "보탠 것" 불릿(새 규칙 아님) + 어긋난 임계값만 재보정(사용자 본인 실물이 FAIL이면 게이트가 틀린 것) + §8 TBD에 사용자 실물끼리 충돌한 것만 올린다.
- 예시 파일엔 원문 verbatim만 옮기고 판단은 표준 §에 적는다.
- 한 문서에 다른 팀 양식(CD2 영문·실사팀)이 섞여 있으면 참고로만 적고 우리 양식(CD1 한국어)만 규격 대상으로 센다.
- 관련: [[t1-page-exemplars-whole-learning]] [[proposal-is-the-writers-spec]] [[audit-must-pass-hit-scripts-first]]
