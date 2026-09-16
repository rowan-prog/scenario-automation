# 34_storm_dragon_bride — meta

- 작품: **I Bought the Dragon Lord for One Night** (가제) / 원작 = 사내 히트작 《One Night with the Dragon Lord》 53화
- 장르·타깃: 여성향 다크 판타지 로맨스 · 북미/글로벌 여성 · EN 발화(AI 더빙) · 중국 제작
- 총 53화 · 무료 1~8화 · paid vertical
- 모드: ① verbatim 계승 + 껍데기 교체(이름·지명·용어·용의 색·공간 한 줄) — 청사진 = `34_storm_dragon_bride_01_adaptation_blueprint.md`
- 원작 사본: `reference/One Night with the Dragon Lord_FINAL_CN&EN.docx` · 추출 = `reference/..._source_CN&EN.txt`

## 이력
- 2026-09-15 사용자 지시: "이름, 약간의 배경만 바꾸고 흐름·인물구조 유지 · 어색한 EN 대사 워싱 · 토큰 최소 · 이름은 판타지풍 + AI가 이름으로 인식 + 발음 하나". Fable 설계 → python 기계 치환 → opus 2기 대사 워싱(old/new 쌍) → sonnet 1기 지문 공간 손질 → 게이트 → v1.

- 2026-09-15 **FINAL v1** = `07_final/34_storm_dragon_bride_FINAL_v1_CN&EN.md` + `.docx`. 결과: 대사 482줄 중 79줄 워싱(A 40·B 39 — 메인이 2줄 손봄: L609 "get away from me" · L757 "hold back the poison") · 지문 18줄(메인이 L1625 "港口礁石"로 수정) · 기계 치환 약 2,100건. 게이트: `name_leak_check.py` PASS(오탐 Cut만 allow) · 잔재 grep 0 · 한국어 0 · 53화 · 대사 줄수 원작과 동일. 변경 목록 = `34_storm_dragon_bride_v1_changelog.md`.

- 2026-09-15 사용자 반려 "Astrid 장난하냐. 영어권 이름으로 해라" → 전원 교체: Nora(诺拉)/Damon(达蒙)/Garrick 유지/Vivian(薇薇安)/Sabrina(萨布丽娜)/King Edmund(埃德蒙). md·docx·청사진·변경목록 전역 치환, name_leak PASS 재확인.

- 2026-09-15 사용자 지시 "작품개요 첫페이지에 요약적으로(타이틀·로그라인·무료회차·총회차·세계관·주요인물) 그러고 나서 대본" → opus 1기(정본 50_t1 Part 0·A + 대본 전량 정독)가 EN+CN 개요 작성, 메인이 저주 출처 한 문장 추가 → docx 첫 페이지 개요 + 페이지 나눔 + 대본. 중문 제목 후보 = 我买下的男人，是龙族领主 / 一夜买下龙主.

- 2026-09-16 **Codex 작업본 인입 = FINAL v3** (사용자: "이게 최종고" + "너의 34번 프로젝트에 옮겨놔"). 원본 = `C:/Users/Rowan/Documents/Codex/scenario-automation-codex/projects/33_storm_dragon_bride/adaptation/I Bought the Dragon Lord for One Night_다듬은대본_v003.docx`(원본은 그대로 두고 복사). 정본 = `07_final/34_storm_dragon_bride_FINAL_v3_CN&KO&EN.docx` + 추출본 `.md`(3,696문단 / 5,863줄 / 영어 대사 486줄). v1·v2 대비 달라진 것 = ①**3개 국어 병기**(중문 지문 + 한국어 + 영어 — v1/v2는 CN&EN) ②**인명 재교체: Nora→Ophelia(奥菲莉娅) · Damon→Dorian(多里安)** ③장면 7곳 수정(11·16·35·40·42·45·51화 — 전후 대조 = `34_storm_dragon_bride_v3_changes.md`). Codex v001·v002 + STATUS = `_work_codex/`.

## 제목 후보 (미확정)
1. I Bought the Dragon Lord for One Night (가제·문서 헤더)
2. The Stranger I Bought Was the Dragon Lord
3. One Night Before the Dragon
