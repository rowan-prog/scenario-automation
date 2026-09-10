---
name: adaptation-rename-entire-cast
description: 각색·인명 치환 작품은 원작 인물 이름(성·이름·조연·유료 인물·아이까지) 하나도 남기지 말 것 — 2026-09-10 29번 사고
metadata:
  type: feedback
---

"인명 치환"이라고 써 놓고 원작 이름을 남기면 안 된다. 성(姓) 하나, 조연 하나, 유료 구간 인물, 아이 이름까지 전부다.

**Why:** 2026-09-10 29번(마지막 날이 보이는 남자) 작가 1차 대본에서 사용자가 "Jack Reed면 Zion Reed 원작 성씨 따왔잖아"라고 격노. 대조해 보니 Reed·Chloe·Lance Cromwell·Mike·Lucas·Charles Waldorf·Joseph Quinn·Tyson 전부 원작 Countdown King 이름이었고, 출처는 작가가 아니라 **우리 러프 기획안 v6**(CLAUDE.md엔 "인명 치환"이라 적혀 있었음). 작가는 우리 걸 복사했을 뿐.

**How to apply:** 각색 기획안 게이트에 원작 EN/CN 텍스트 전수 grep 추가 — 우리 인물명(영문·한글·중문) 각각을 원작 원문에서 `\b이름\b`로 검색해 0회여야 통과. 성과 이름을 따로 검색한다(Reed처럼 성만 남는 사고). 유료 트리트먼트 인물·아이·조직명(Cromwell Group·Waldorf)까지 대상. 새 이름은 [[names-must-survive-ai-dubbing]] 4검사 + 첫소리 전원 상이. 관련 = [[dubbing-safe-character-names]] [[world-swap-acts-must-translate]]
