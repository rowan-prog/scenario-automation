---
name: project-locked-out-interactive-game
description: "LOCKED OUT 인터랙티브 게임 개발 — 작업 폴더는 이 workspace가 아니라 Codex workspace(`C:\\Users\\Rowan\\Documents\\Codex\\scenario-automation-codex\\projects\\_reference\\07_locked_out\\`). 진입 시 그쪽 00_START_HERE부터."
metadata: 
  node_type: memory
  type: project
  originSessionId: 354a1572-5387-414c-adff-b50a56ce2a32
  modified: 2026-08-06T02:31:52.243Z
---

# LOCKED OUT 인터랙티브 게임 (2026-08-05 기준)

**작업 폴더 = `C:\Users\Rowan\Documents\Codex\scenario-automation-codex\projects\_reference\07_locked_out\`** — scenario-automation workspace 밖. 진입 시 `00_START_HERE.md` → `00_STATUS.md` 정독 (단 둘 다 스테일할 수 있음 — 아래 참조).

## 산출물 지도 (`07_final/`)

- `01_PRODUCTION_SCRIPTS/` — 영문·한국어 제작 대본 v001 (57화 재구성본·△ 양식). 영문본 사본이 이 workspace `config/vertical_drama_hit_scripts/07_locked_out_02_PRODUCTION_SCRIPT_EP57_v001.docx`로도 등재됨.
- `02_INTERACTIVE_WRITING_BLUEPRINT/` — EP·씬 집필 설계안. 정식+라이트 v016 (2026-08-03) + **v017 (2026-08-04 밤 재설계·최신)**.
- `03_PLAYABLE_WORLD_TREE/` — 전체 조감도+게임 맛보기 HTML. v019(+zip·이미지 21개 내장) + **v020 (2026-08-04 저녁·최신)**.
- `04_MARKETING/` — 셀링포인트 v001.
- `05_APPS_SCRIPT_AUTHORING_TOOL/` — **세계수 집필 에디터** (Google Apps Script 웹앱·범용 멀티작품 브랜칭 저작 도구·2026-08-04 22시 최종 = 가장 최근 산출물). Code.gs / Index.html / SEED_DATA.gs(LOCKED OUT 시드 v018 = **분기 44·선택지 112·엔딩 21** — 서비스컷 트랩 3 포함. 2026-08-05 실측 정정: 헤더/README의 109·18은 trap_add 이전 숫자였음) / README_설치.md / `_src/`(빌드 스크립트). DB 스프레드시트 지정돼 있음(README에 URL). 헬스체크 = `cd _src && node smoke_appscript.js ".."` → 2026-08-05 전량 PASS(50항목).

## V넘버 재분절 체계 (2026-08-05 사용자 확정 — 대본·앱 공통 정본)

- **에피소드 개념 폐기. 통대본을 분기 지점에서만 잘라 영상 단위로 넘버링** — V0=프롤로그(신규·추후 집필) · 공통=V단독 · 분기 갈래=V{n}-{k}(**원작 진행 쪽도 별도 번호** — 편집 컷이니까) · 엔딩 갈래="V{n}-{k} · BAD ENDING m"(이후 없음) · 막(ACT) 구분 유지. 결과 = **V0~V88** (공통 44·분기점 44·갈래 112·엔딩행 12).
- 분기 카테고리 3종: 다지선다 / QTE1(제한시간 클릭 — N04 저격) / QTE2(연타 — N01 배수구). 선택 제한시간 10초. **⭐히든 선택지** = 매우 중요 분기에서 타이머 후반 갑자기 등장(트루 지향) — 인프라만 깔림, 지정은 작가 리터치 때. ♥ UI = 변화 시에만 2~3초 노출 후 사라짐.
- 원작 표기 3단 분리(사용자 지적으로 신설): **[원작]**(대사가 대본에 실존·기계 검증됨) / **[원작 진행 · 대사 신규 ⚠]**(스토리는 원작 루트인데 대사는 지어낸 것 — 7건: N09·N12·N18·N20·N26·N28·N33의 A) / **[신규]**. `origv` 필드로 기계 검증.
- 산출물: `01_PRODUCTION_SCRIPTS/07_locked_out_04_BRANCH_MASTER_SCRIPT_v001.docx`(통대본 재분절판) · `…_SEGMENTS_v001.json`(개발 핸드오프 — 사용자가 미리 요청) · `_src/segmentation_map.md`(컷 44건 ±맥락 검증 지도) · 빌더 = `_src/build_branch_master.py`(재실행 멱등·시드에 vnum/mech/origv/ui_spec 환류).
- 검토 이력: 기계 3종 대조 = 불일치 0 / fresh-eyes 컷 감사 = CRITICAL 5·HIGH 9 → **매니페스트로 컷 교정 반영**(핵심 발견 = 이 대본 포맷은 [Visual]에 씬 결말까지 몰아 적어서 대사 라인 컷이 결과 선공개가 됨 → atline-text/insert-before-text 모드로 해결). 기계로 못 고치는 20건 = **리터치 안건**으로 docx·JSON·지도에 ⚑ 표기 (대표: N04 A대사 화자가 아리엘 / N32 NTR 엔딩 X1 고정 / N16 애프터매스 갈래 종속 / N26 갈래 성립 손질).
- 앱 v2: 세로 트리(1단→2단→3단·좌우 폐기)·V넘버 표시(vnum 시드 환류 = 정본, 없으면 순차 자동)·QTE/히든/원작 배지·JSON 내보내기·선택지 추가 버튼 방어+window.onerror 토스트. 스모크 v2 전량 PASS(앱 V넘버 = 빌더 JSON 대조 포함).
- **2026-08-05 저녁 사용자 지적 3건 반영:** ①**분기 ID = 진행순 재부여**(V순서와 단조 일치 — "V6인데 분기34" 제거. 구 N34~N44 무대사 노드가 본선 사이로 흡수됨. ⚠ 빌더 딕셔너리(MANIFEST 등)는 ID가 아니라 **노드 제목 키워드가 안정 키** — ID 하드코딩이 재실행 시 시드 오염시킨 실증 있음) ②**선택지 추가 버그 근본 수정** = PEND 전역(미저장 편집 상태) + 전체 재렌더 방식(outerHTML 치환 폐기)·저장 = 로컬 즉시 반영(왕복 제거) ③**타임코드 칸**(노드별 tc·작가 기입 공란·docx "타임코드: ___") ④**"(원작 그대로)" 선택지 → 게이머용 동작 라벨 11종**("고개만 끄덕이고 곧장 돌입한다" 등·alabel 필드 = 대사 검증 제외). ⑤사용자 쿠사리: docx가 [Visual]/[Camera] 블록 양식 그대로 = 병신 — **사람이 읽는 대본류 산출물은 무조건 씬헤더+지문+화자대사 양식** — [Visual]/[Camera] 같은 기계 블록 양식을 산출물에 끌고 오는 것 자체가 금지, 예외·확인 절차 없음 (2026-08-05 사용자 재확인). 구 ID로 쓴 집필 본문은 리매핑으로 연결 안 됨(현재 본문 0건이라 무해).

## 에디터 형상 관리 (2026-08-06 확정)

- **개발자 공유 = Apps Script 프로젝트 공유로 충분** (개발자 확인) — script.google.com 프로젝트에 이메일 초대(뷰어/편집자). 코드 이력 = "프로젝트 기록"(배포 버전별). GitHub 분리 리포·clasp = 불요 판정.
- 코드 이력 실태: git(codex 리포) = 하루 1회 auto-backup 스냅샷 · Apps Script = 배포 누른 판만 · 그 사이 중간 상태는 어디에도 없음. ⚠ codex 리포 GitHub 푸시가 5/22부터 인증 만료로 끊겨 있음(로컬 커밋만 쌓임) — 사용자가 `git push origin backup` + 재인증 필요.

## 멀티작품 운용 룰 (2026-08-05 사용자 확정)

- **P01 = LOCKED OUT(시드 기반) / P02 = 신작.** 새 작품(P02~)은 **구조(양식)만** P01을 따라가고, **설계(분기·선택지·엔딩·트리트먼트)는 도구가 부어주지 않는다** — 사람이 P01 보면서 직접 채움. 시드 = P01 전용.
- 2026-08-05 도구 반영: ①구조 최신화(재시드) = 시드 기반 작품에서만 노출 + 서버 가드(assertSeedTarget_) ②'빈 작품'→'구조만' 템플릿 라벨 ③작품별 작법 메모(rules) 편집·개요 표시 ④원작 트리트먼트 일괄 붙여넣기(설정 탭·`번호 제목 — 요약`). META에 template 키(lockedout/empty) 기록. 스모크 62항목 PASS.

## 확정 룰 (2026-08-05 사용자)

- **선택 주체 = 잭(플레이어) 단독. 다른 캐릭터 시점에서 고르는 선택지는 없고, 없어야 한다.** 히로인의 자율 행동(꼬드김 듣기·♥3 생환·EP55 이탈)은 전부 잭의 누적 선택이 계산돼 나오는 결과로만 표현 — 별도 선택 UI 금지. 도구 스키마도 화자 필드 없음(구조적으로 1인 고정 유지).
- 원작 대사 선택지 구분 = CHOICES `orig` 필드(boolean)·문서 [원작] 배지·에디터 "원작 진행 선택지" 체크박스 3중 표기. 원작 선택지는 항상 A 자리. 44개 노드 중 39개 = A가 원작, 5개(N11·N17·N23·N27·N32) = 전 선택지 신규(원작에 대응 대사가 없는 삽입 분기 — 관계 선언 2·꼬드김 채널·NTR 회복·세라프 신뢰).
- 상태 변수 4종 고정(♥×3·생존·채널·선언) — 서브스탯 추가 요청은 기각이 기본값(설계안 §8). 아이템/인벤토리 개념 없음.

## 주의

- `00_STATUS.md`·`LATEST_MANIFEST.json`·`00_START_HERE.md` = 2026-08-04 13시 기준이라 **v017 설계안·v020 HTML·05 저작 도구가 미반영(스테일)**. 최신본 판정은 파일 시스템 타임스탬프 우선.
- 규모 숫자 두 벌 존재: 구 조감도(v018/v019 데이터) = 결정 88·선택지 243·엔딩 33 / 8-4 재설계 시드 v018 = 분기 44·선택지 109·엔딩 18. 재설계에서 축소된 것으로 보이나 미확정 — 필요 시 `_work/interactive_redesign_v017_20260804/`에서 확인.
- Story Contract·가드레일(히로인=전투원·잭 육체 우위 유지·EP56 경계 위반=즉시 배드엔딩·NTR-ALL 구성 등) = `00_STATUS.md`에 있음. 구버전 = `_archive/interactive_design_versions/v011~v018`.
- 원작 = 남성향 검증 성공작(중박+) — [[locked-out-success-insights-2026-05-17]].
