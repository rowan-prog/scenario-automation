# 34_storm_dragon_bride — meta

- 작품: **I Bought the Dragon Lord for One Night** (가제) / 원작 = 사내 히트작 《One Night with the Dragon Lord》 53화
- 장르·타깃: 여성향 다크 판타지 로맨스 · 북미/글로벌 여성 · EN 발화(AI 더빙) · 중국 제작
- 총 53화 · 무료 1~8화 · paid vertical
- 모드: ① verbatim 계승 + 껍데기 교체(이름·지명·용어·용의 색·공간 한 줄) — 청사진 = `34_storm_dragon_bride_01_adaptation_blueprint.md`
- 원작 사본: `reference/One Night with the Dragon Lord_FINAL_CN&EN.docx` · 추출 = `reference/..._source_CN&EN.txt`

## 이력
- 2026-09-15 사용자 지시: "이름, 약간의 배경만 바꾸고 흐름·인물구조 유지 · 어색한 EN 대사 워싱 · 토큰 최소 · 이름은 판타지풍 + AI가 이름으로 인식 + 발음 하나". Fable 설계 → python 기계 치환 → opus 2기 대사 워싱(old/new 쌍) → sonnet 1기 지문 공간 손질 → 게이트 → v1.

- 2026-09-15 **FINAL v1** = `07_final/34_storm_dragon_bride_FINAL_v1_CN&EN.md` + `.docx`. 결과: 대사 482줄 중 79줄 워싱(A 40·B 39 — 메인이 2줄 손봄: L609 "get away from me" · L757 "hold back the poison") · 지문 18줄(메인이 L1625 "港口礁石"로 수정) · 기계 치환 약 2,100건. 게이트: `name_leak_check.py` PASS(오탐 Cut만 allow) · 잔재 grep 0 · 한국어 0 · 53화 · 대사 줄수 원작과 동일. 변경 목록 = `34_storm_dragon_bride_v1_changelog.md`.

## 제목 후보 (미확정)
1. I Bought the Dragon Lord for One Night (가제·문서 헤더)
2. The Stranger I Bought Was the Dragon Lord
3. One Night Before the Dragon
