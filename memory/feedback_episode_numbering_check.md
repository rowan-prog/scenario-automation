---
name: episode-numbering-check
description: 대본 검토 첫 단계 = 화 목록(결번·중복·역순·씬 번호 앞자리·언어별 화 번호·내용 혼입) — 기계 tools/episode_number_check.py
metadata:
  node_type: memory
  type: feedback
  originSessionId: 34a1dd1e-7380-4343-a610-1d0c36087754
  modified: 2026-10-08T07:33:01.117Z
---

대본을 검토·각색·재분할하면 장면 연결 장부를 들기 전에 화 목록부터 센다. 빠진 화, 두 번 나온 표제, 뒤집힌 순서, 기획 총 화수와 다른 마지막 화, 화 번호와 안 맞는 씬 번호 앞자리, 화 안에서 건너뛴 씬 번호, 중·한·영 병기본의 언어별 화 번호 차이, 1부 개요 목록과 2부 본문 화 목록 차이를 본다. 번호가 맞아도 다른 화 내용이 섞인 경우가 있어서, 분량이 튀는 화와 트리트먼트상 첫 장면·끝 대사가 안 맞는 화는 원본과 대조한다.

**Why:** 2026-10-08 사용자: "검토에서, 에피소드 누락 or 에피소드 넘버링 오류도 종종 있어서 주의." 실물 = 33번 작가본 22화 표제 두 번·19화 혼입·8화 씬이 S#2부터 / 11번 37화 안 씬 번호 35-1·24화 씬이 024-2부터. 반대로 11번 v1은 docx 변환 손실을 결번으로 오판했다([[docx-conversion-drops-table-textbox-text]]).

**How to apply:** `python C:\Users\Rowan\scenario-automation\tools\episode_number_check.py <대본 md·txt·docx> --expect <마지막 화>` 먼저 돌린다(docx는 document.xml 직접 읽음 — 표·텍스트박스 포함, 변경 이력 삭제분 제외). ✗는 오류로 내고 △는 원문을 열어 가린다. 결번은 원본 docx로 변환 손실부터 배제한다. 보고 맨 앞에 "1~N화 결번 0 · 중복 0 · 순서 0 · 씬 번호 앞자리 불일치 0"을 쓴다. 규칙 본문 = `config/20_review_standard.md` §0-1 0번 · 전역 CLAUDE.md 대본 검토 0번. 화 합치기·나누기 뒤에도 돌린다(34번 53→50, 06번 50→48 같은 재분할).
