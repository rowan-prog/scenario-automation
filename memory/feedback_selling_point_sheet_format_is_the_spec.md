---
name: selling-point-sheet-format-is-the-spec
description: "CD1 셀링포인트는 팀 공용 xlsx 템플릿의 서식이 곧 규격이다 — 내가 두 번 빠뜨린 MKT Idea 섹션과, 손으로 만들면 반드시 깨지는 것들"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d6cd8dd0-c132-4beb-bbd3-7a9c8b7d16b0
  modified: 2026-08-19T09:59:04.238Z
---

CD1 셀링 포인트 작업은 **팀 공용 템플릿(`[EN_AI] Selling Point_Template`)의 실측 서식이 규격**이고, 우리 탭은 마케팅팀 마스터(`US Marketing Selling Point.xlsx`, 작품당 탭 80여 개)에 붙는다. 규격 본문 = `config/40_selling_point_standard.md`.

**Why:** 2026-08-19 템플릿 전수 실측으로 확인한 것 — 내 지난 산출물 2개(TITAN BORN·Dragon Lord)에서 같은 결함이 반복됐다.

- **MKT Idea 섹션(실제 장면 묶음)을 두 번 통째로 빠뜨렸다.** Fake MKT Idea만 채웠다. 템플릿은 두 섹션이 별개다 — MKT Idea = ★ 회차에서 뽑아 파는 축으로 묶은 실물 컷(마케터가 통으로 집어 가는 단위·KR/EN/CN), Fake = 창작. G열 회차 카드가 이걸 대신하지 못한다(회차별 단서 ≠ 캠페인 묶음, G열은 한국어 전용).
- **손으로 만들면 서식이 반드시 어긋난다.** 실제로 어긋난 것: 섹션 밴드가 Arial 15 Bold여야 하는데 기본 10으로 나감 / 회색 소제목 가운데 정렬 안 됨 / 53화인데 템플릿의 EP 54~60 빈 행이 테두리째 잔존 / Title Overview C열의 회색 9pt 이탤릭 예시문 서식 위에 우리 EN을 덮어써서 주석처럼 보임.
- Title Overview C열은 템플릿상 **회색 예시문 열**이다. 우리는 여기를 EN으로 쓰되 서식을 검정 10pt로 되돌려야 한다.

**How to apply:** 시트는 손으로 만들지 말고 `tools/build_cd1_sheet.py`(spec.json → 서식 전량 재적용) → `tools/cd1_validate.py`(G1~G17) 전항 통과 → 파일 열어 눈으로 확인. 검증기 G13이 MKT Idea 블록 누락을, G17이 밴드 글꼴·예시문 잔존·열 너비를 잡는다. 작성 원칙은 [[no-abstract-evasive-writing]]·[[dialogue-direct-register-wit-ration]]과 같은 방향 — 정사·폭력 완곡어는 스타일이 아니라 결함이고, 편집자가 그 문장으로 컷을 못 찾으면 실패다. 짧다고 직관적인 게 아니다([[rough-proposal-is-a-pitch-doc]]의 "읽는 재미" 판정과 같은 축).
