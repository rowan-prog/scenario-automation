# 자동 커밋 · 백업 설정

이 저장소는 두 갈래로 자동 커밋되고, **커밋 직후 GitHub 원격까지 push** 합니다.
원격 = `https://github.com/rowan-prog/scenario-automation.git` (비공개)

> 2026-08-11 이전에는 push가 안 됐습니다. `~/.gitconfig` 에 `credential.interactive=never` ·
> `credential.modalprompt=false` 가 있어서 자격증명 프롬프트가 통째로 꺼져 있었고,
> 그 탓에 로컬 커밋만 쌓이며 원격이 7/31 에 멈춰 있었습니다. 두 줄을 해제해 복구했습니다.
> 다시 끊으려면 그 두 줄을 되돌리면 됩니다.

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

작업 스케줄러 설정: 놓친 작업 따라잡기 켬(PC가 꺼져 있었으면 다음 로그온 때 실행), 배터리에서도 실행. 단 **로그온 상태에서만** 돕니다 — 로그아웃 중에는 안 돕니다.

## 한계 — 이건 실시간 백업이 아닙니다

- 원격에 올라가는 시점은 **세션 종료 시 + 09:00 + 21:00** 뿐입니다. 그 사이 작업은 로컬에만 있습니다.
- `.gitignore` 가 막는 것은 안 올라갑니다: `.claude/`, `inbox/`, `*.log`
- 따라서 **메모리(`~/.claude/projects/.../memory/`)와 훅 스크립트는 백업 대상이 아닙니다.**

## 확인하는 법

```powershell
# 다음 정기 실행 시각
Get-ScheduledTaskInfo -TaskName 'ScenarioAutoCommit' | Select NextRunTime

# 최근 자동 커밋 이력
git log --oneline -10

# 정기 커밋 로그
Get-Content .auto_push.log -Tail 10
```
