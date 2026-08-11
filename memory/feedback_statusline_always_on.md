---
name: Statusline 잔여 context·token 항상 표시
description: Statusline에 잔여 context %·잔여 토큰 수 항상 표시 유지. 사라지면 즉시 복구
type: feedback
originSessionId: 1bbee5e9-3d1c-4a80-988f-8c0f01afdca3
---
Statusline은 항상 잔여 context %와 잔여 토큰 수를 표시해야 한다. 사용자가 별도 지시하지 않아도 사라진 것이 확인되면 즉시 복구.

**Why:** 사용자가 작업 중 남은 컨텍스트·토큰을 실시간으로 확인하기 위해. 표시가 빠지면 작업 페이스 판단이 어렵다.

**How to apply:**
- 세션 시작 시 또는 사용자가 statusline 이상을 언급하면 `C:\Users\Rowan\.claude\settings.json`의 `statusLine` 항목과 `C:\Users\Rowan\.claude\statusline-command.ps1`이 정상인지 확인
- 표시 형식: `Claude … | effort: … | ctx: XX% left (~Xk rem / 200k) | …`
- 실행 경로(예: `시나리오작업.bat`)는 단순 `claude` 호출이므로 전역 settings.json만 정상이면 자동 적용
- 묻지 말고 자율 복구
