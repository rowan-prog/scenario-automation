# 자동 커밋 설정

이 저장소는 두 갈래로 자동 커밋됩니다. 둘 다 **로컬 커밋만** 합니다 — 원격(GitHub) 연결은 끊어둔 상태라 push는 조용히 넘어갑니다.

## 1. Claude Code 세션이 끝날 때

| | |
|---|---|
| 스크립트 | `~/.claude/hooks/session-commit.ps1` |
| 등록 위치 | `~/.claude/settings.json` → `hooks.Stop` |
| 동작 | 세션 종료 시 변경분을 커밋하고, 커밋 해시를 화면에 한 줄로 알림 |

**옵트인 방식입니다.** 저장소 루트에 `.claude-autocommit` 파일이 있는 저장소에서만 동작합니다. 전역 훅이라 아무 저장소에나 커밋하면 남의 코드나 비밀키까지 올라가기 때문에 표식을 둔 것입니다.

- 켜기: 저장소 루트에서 `New-Item .claude-autocommit`
- 끄기: 그 파일 삭제

rebase·merge·cherry-pick 진행 중이거나 detached HEAD면 건드리지 않고 넘어갑니다.

## 2. 매일 아침·저녁 정기 커밋

| | |
|---|---|
| 스크립트 | `~/.scenario_scripts/auto_commit_push.ps1` |
| 등록 위치 | 작업 스케줄러 `ScenarioAutoCommit` |
| 시각 | 매일 **09:00 / 21:00** |
| 로그 | 저장소 루트 `.auto_push.log` (gitignore됨) |

Claude Code 밖에서 손으로 고친 것까지 받아내는 뒷단입니다. 커밋 메시지에 바뀐 상위 폴더 목록이 요약으로 들어갑니다.

## push를 다시 켜려면

원격은 `https://github.com/rowan-prog/scenario-automation.git` 이고 인증이 끊겨 있습니다. 되살리려면 한 번만:

```
gh auth login
```

그 뒤로는 두 스크립트가 알아서 push까지 합니다. 로그에 `PUSH 완료`로 찍히면 붙은 것입니다.

## 확인하는 법

```powershell
# 다음 정기 실행 시각
Get-ScheduledTaskInfo -TaskName 'ScenarioAutoCommit' | Select NextRunTime

# 최근 자동 커밋 이력
git log --oneline -10

# 정기 커밋 로그
Get-Content .auto_push.log -Tail 10
```
