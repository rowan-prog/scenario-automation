---
name: project-dist-package
description: 이 워크스페이스를 사내 배포용 패키지로 굽는 방법과 그때 내린 결정들 (2026-08-05)
metadata: 
  node_type: memory
  type: project
  originSessionId: cdcb0cd6-e241-4283-b6c1-a453fcdf21ac
  modified: 2026-08-05T08:22:07.805Z
---

사내 배포용 패키지 빌더 = `tools/build_dist.py` · 배포판 전용 문서 원본 = `tools/dist_docs/` (README·SETUP·CASE_STUDIES·install.ps1·install.sh·verify.py·projects_README).

`python tools/build_dist.py --zip` → `../scenario-automation-dist/` + zip. `--no-assets` = 히트작 역대본 62개 제외(외부 배포용).

**2026-08-05 사용자 확정 = 사내 배포.** 따라서 히트작 원본·피칭 실적 데이터·타깃 리서치 전부 포함, 룰 문서의 작품 폴더명 근거 표기("12_hired 실증")도 그대로 유지.

빌더가 자동 처리하는 것 — CLAUDE.md 작품 현황표(IP) 제거 + 최초 실행 부트스트랩 섹션 삽입 / 개인 절대경로 치환 / 작품 캐논 메모리 7개 제외 + MEMORY.md 인덱스 정리 / 배포판에 없는 문서 참조 정리.

받는 사람 동선 = 압축 풀고 그 폴더에서 `claude` 실행뿐. 배포판 CLAUDE.md 최상단 부트스트랩이 `.setup_done` 없으면 에이전트가 스스로 verify → install → 재verify 하게 만든다.

**포팅 시 실제로 터졌던 것 2종(재발 주의):** ①PowerShell 5.1은 BOM 없는 UTF-8을 cp949로 오독 → `.ps1`은 `utf-8-sig`로 써야 한글이 안 깨짐 ②파이썬 콘솔 출력이 cp949라 em dash에서 죽음 → `sys.stdout.reconfigure(encoding="utf-8")` 필요. 또 `py_compile`에 `os.devnull`을 cfile로 주면 윈도우에서 실패한다(임시 디렉터리 사용).

메모리 설치 경로 슬러그 규칙 = 워크스페이스 절대경로에서 `: \ /` → `-` (`C:\work\x` → `C--work-x`). 이 PC의 기존 `~/.claude/projects/` 폴더명과 대조해 검증됨. **설치 후 폴더를 옮기면 메모리를 못 읽는다 — 옮겼으면 install 재실행.**

관련 = [[docx-conversion-drops-table-textbox-text]] [[path-discipline]]
