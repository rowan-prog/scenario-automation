# SETUP — 설치 상세

## 1. 준비물

| 필요 | 확인 |
|---|---|
| [Claude Code](https://claude.com/claude-code) | `claude --version` |
| Python 3.9+ | `python --version` |
| python-docx (선택) | 기획안·트리트먼트 docx 산출물을 쓸 때만. `pip install python-docx` |

Claude Code 모델은 **Opus 권장**. 이 시스템은 Opus/Sonnet/Haiku 세 티어만으로 자급되게 설계돼 있고, 어느 작업에 어느 티어를 쓸지는 `CLAUDE.md` 라우팅 표에 이미 박혀 있다.

## 2. 폴더 위치 정하기

**설치 후에는 폴더를 옮기지 마라.** 메모리 설치 경로가 워크스페이스 절대경로에서 계산되기 때문에, 옮기면 Claude Code가 메모리를 못 읽는다. 옮겼다면 install 스크립트를 다시 돌리면 된다.

경로에 한글·공백이 있어도 동작하지만, 짧고 단순한 영문 경로를 권한다. 예: `C:\work\scenario-automation` · `~/work/scenario-automation`

## 3. 설치

```powershell
cd C:\work\scenario-automation
.\install.ps1
```

```bash
cd ~/work/scenario-automation
bash install.sh
```

스크립트가 하는 일은 **메모리 복사 하나뿐**이다. 어디로 복사하는지 화면에 찍히니 확인하면 된다.

```
<홈>/.claude/projects/<워크스페이스 경로를 -로 치환한 슬러그>/memory/
```

기존 메모리가 있으면 타임스탬프 붙여 백업한 뒤 덮어쓴다. 지우지 않는다.

## 4. 검증

```bash
python verify.py
```

6개 항목을 본다 — 필수 파일 / 자산 개수 / 선택 자산 / 메모리 설치 / 도구 문법 / 배포 위생.
전부 통과하면 이 폴더에서 `claude` 를 실행하면 끝이다.

## 5. 첫 실행 때 확인할 것

Claude Code를 띄우고 이렇게 물어보면 설치가 제대로 됐는지 바로 안다.

```
지금 워크플로우 문서랑 메모리 다 읽히는지 확인해줘. 에이전트 몇 종 있는지도.
```

기대 답: 룰 문서 4종 + 메모리 약 178개 + 서브 에이전트 14종.

메모리를 못 읽는다고 하면 → `install` 스크립트가 찍어준 경로와, Claude Code가 실제 쓰는 경로가 다른 것이다. Claude Code에서 `/memory` 를 쳐서 실제 경로를 확인하고 거기로 `memory/` 폴더를 복사하면 된다.

## 6. 문제 해결

| 증상 | 원인·해결 |
|---|---|
| 서브 에이전트가 안 보인다 | `.claude/agents/` 가 워크스페이스 루트에 있어야 한다. 반드시 **이 폴더에서** `claude` 를 실행할 것 |
| 메모리를 못 읽는다 | 폴더를 옮겼거나 슬러그가 다른 경우. install 스크립트 재실행 |
| docx 빌더가 죽는다 | `pip install python-docx` |
| 히트작 원본이 없다 | `--no-assets` 로 빌드된 패키지다. 분석본·craftcard 로 대체되지만 집필 품질 기준이 내려간다 |
| 한국어가 깨진다 | 터미널 인코딩 UTF-8 확인. PowerShell: `chcp 65001` |

## 7. 이 패키지를 다시 만들 때 (원 작성자용)

```bash
python tools/build_dist.py                # 히트작 원본 포함
python tools/build_dist.py --no-assets    # 외부 배포용
python tools/build_dist.py --zip          # zip까지
```

빌더가 자동으로 처리하는 것:
- `CLAUDE.md` 의 작품 현황표(IP) 제거 → 신규 사용자용 안내로 교체
- 개인 절대경로 치환
- 작품별 캐논 메모리 제외 + `MEMORY.md` 인덱스 정리
- 아카이브·`__pycache__`·구버전 폴더 제외

배포판 문서(README·SETUP·CASE_STUDIES·install·verify)의 원본은 `tools/dist_docs/` 에 있다. 고칠 일이 있으면 거기서 고치고 다시 빌드하면 된다.

## 8. 라이선스

내부 작업 도구. `config/vertical_drama_hit_scripts/` 는 외부 저작물이라 사내 참고용으로만 쓰고, 공개 저장소에 올리지 말 것. `config/pitch_references/` (실제 심사 통과·탈락 데이터)와 `config/target_research/` 도 대외비.
