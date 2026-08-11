---
name: docx-conversion-drops-table-textbox-text
description: "python-docx 변환은 표/텍스트박스 대사 + 수락 안 된 변경 이력(w:ins) 삽입 텍스트를 흘린다 → 유령 \"결번·공란·문장 파손\" 오진. 결손 지적은 원본 docx raw XML로 대조 후 보고."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d81b8c00-7c08-475f-b086-032c4cd3601e
---

외부 docx 대본을 `python-docx` `doc.paragraphs`(또는 그 계열 paragraphs-only 추출)로 변환하면 **표(table)·텍스트박스(w:txbxContent) 안에 든 대사·지문이 통째로 사라진다.** 본문 문단만 긁고 표/도형 안 텍스트는 건너뛰기 때문.

**실증 (11_the_outcast, 2026-07-08):** v1 검토가 `source_CN.md`(python-docx 변환본) 기준으로 "EP34 통째 결번 + EP21~28 스켈레톤 공란 + EP37 리빌씬 대사공란"을 완성성 미달의 근거로 잡았는데, **원본 docx엔 50화 대사가 전부 있었다.** 그 구간 대사가 docx의 표/텍스트박스에 들어 있어 변환에서 누락됐을 뿐. "미완성·구조파탄" 판정 자체가 파생본 오류 위에 세워짐.

**두 번째 실증 — 변경 이력 (16_moses, 2026-08-03):** 작가 회수본을 python-docx로 뽑아 검토했더니 "이 왕국의 로 ." "△ 델릴라가 " "왕도로 !" 처럼 문장이 잘린 곳이 다섯 군데. **"이번 수정 중 생긴 파손"으로 사용자에게 보고했는데, 실제 파손은 한 곳뿐이었다.** 나머지 넷은 그 docx에 **수락되지 않은 변경 이력(`<w:ins>`, 작성자 = 사용자 본인) 8건**이 남아 있었고, python-docx의 `paragraph.text`가 `<w:p>` 직속 `<w:r>`만 읽어 `<w:ins>` 안의 삽입 텍스트를 통째로 건너뛴 것. 즉 **paragraphs-only뿐 아니라 python-docx 자체가 "변경 내용을 거부한 상태"의 본문을 보여준다.** 표·텍스트박스를 다 훑는 전체 `<w:p>` 순회로 고쳐도 이건 안 잡힌다.

**Why:** 파생 텍스트(변환본)를 원본으로 착각하면, 변환기의 결함이 대본의 결함으로 둔갑한다. 특히 "없다/빠졌다/공란이다"류 결손 지적은 심각도가 높아 판정을 뒤집는데, 그 근거가 가장 취약(추출 커버리지 문제)하다.

**How to apply:**
1. **결손 지적(결번·공란·누락)은 원본 docx raw XML로 반드시 재대조 후 보고.** 방법 = docx unzip → `word/document.xml` → `ET.fromstring(...).iter(W+'p')` 로 **모든** `<w:p>`(표·텍스트박스 포함) 문서순 순회. paragraphs-only보다 완전.
2. **작가/외부 회수본은 열자마자 `<w:ins>`·`<w:del>` 개수부터 센다.** 있으면 판정 전에 변경 이력을 수락한 텍스트(= `<w:t>` 전량 포함, `<w:delText>` 제외)를 만들어 그걸로 읽는다. 산출물로 되돌려 줄 때도 수락 후 내보내야 작가가 깨끗한 파일을 받는다. 실물 = `16_moses/04_스크립트/_build_comments_v11.py` 0단계.
3. EP별 char/line 수를 세서 이상 구간(0~극소)이 진짜 빈지, 추출 손실인지 먼저 판별. **"문장이 중간에 끊겼다"류 지적도 같은 등급** — 조사만 남고 명사가 사라진 패턴(`의 로 `, `국의 가 `)은 십중팔구 추출 손실이다.
4. 심각도를 올리는(CRITICAL/🔴/완성성 판정) 지적일수록 파생본 말고 원본 콜드리드로 검증 — [[bulk-script-verify-strict]] [[external-korean-script-review-belt]] 연장선.
5. 작업 텍스트가 손실본이면 **완전추출본으로 교체**하고, 정본 대조는 항상 원본 파일 기준.

블라인드 콜드리드 > 종이 사실 > 프레임워크 순의 증거 신뢰([[ad-hook-novelty-over-proven-trope]])와 같은 결: 이 경우 "원본 docx" > "변환본". 파생본 신뢰가 자기 검토를 오염시킨 사례.
