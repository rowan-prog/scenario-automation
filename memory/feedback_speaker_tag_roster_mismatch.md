---
name: speaker-tag-roster-mismatch
description: 병렬 배치 집필 시 화자 태그가 로스터의 다른 인물명으로 오기되면 전 기계 게이트를 통과한다 — 번역/정독 fresh-read만 잡음
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8ddc1a10-12e6-4c29-878c-eac0b7928eee
---

병렬 배치 집필(아크별·EP범위별 동시 집필)은 한 인물의 대사를 **로스터에 실존하는 *다른* 인물명**으로 화자 태그를 잘못 달 수 있고, 이 오류는 모든 기계 게이트를 통과한다.

**실증 (12_hired_to_ruin_me FINAL_v2·2026-07-14):** EP20 S#1에서 Delphine(명의자 전향 씬)의 대사 3줄이 화자 태그 `NORA`로 오기 — 등장인물 줄·모든 △는 Delphine인데 대사 태그만 NORA. 심각도 = Nora는 Eve의 봉인명(EP49 해금)이라 최대 반전을 스포일. v1 8아크 병렬집필 잔재였고 **v1 크로스아크 수술 + v2 폴리시 게이트(register_census·pacing·voice·continuity) 전부 통과**했다. 한국어 참고본 번역 에이전트가 처음 잡아냄.

**왜 게이트가 못 잡나:**
- `register_census`: 오기된 이름(NORA)의 대사가 min-lines(8) 미만이면 스킵 → 3줄짜리 오기는 안 보임.
- `continuity_lint` char-complete: 잘못 쓴 이름도 로스터에 실존하는 인물(Nora=Eve)이라 "미등장 인물" 아님 → 통과.
- `voice_lint`·native-ear: per-line spoken 검수라 화자 귀속 오류는 대상 아님.

**How to apply:** ①LOCK/참고본 전 **화자 태그 vs 씬 등장인물(Characters:) 로스터 교차 검증** — 씬의 대사 화자가 그 씬 Characters에 없거나, △/지문이 부르는 이름과 대사 태그가 불일치하면 FLAG. 간단 grep/스크립트로 가능(로스터 스윕 = consistency-sweeper 몫). ②**번역/타언어 참고본 패스 = 강력한 fresh-eyes 감사** — 인물 귀속·이름 일관을 강제로 재검하게 되어 원어 검수가 놓친 오기를 잡는다(부수효과지만 실질 QA층). [[bulk-script-verify-strict]] [[fresh-eyes-full-inspection]] [[docx-conversion-drops-table-textbox-text]]
