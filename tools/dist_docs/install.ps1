# install.ps1 — 시나리오 자동화 메모리 설치 (Windows)
#
# 하는 일: 이 패키지의 memory/ 185개를 Claude Code가 읽는 위치로 복사한다.
# 그 외 자산(룰·에이전트·프롬프트·도구)은 이 폴더 안에 있어서 복사가 필요 없다.
#
# 사용: .\install.ps1          (기존 파일 있으면 물어봄)
#       .\install.ps1 -Force   (묻지 않고 덮어씀)

param([switch]$Force)

$ErrorActionPreference = "Stop"

# 한글 출력이 깨지지 않도록 콘솔 인코딩 고정
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $OutputEncoding = [System.Text.Encoding]::UTF8
} catch { }

$root = $PSScriptRoot

Write-Host ""
Write-Host "=== 시나리오 자동화 설치 ===" -ForegroundColor Cyan
Write-Host ""

# 1. 소스 확인
$srcMemory = Join-Path $root "memory"
if (-not (Test-Path $srcMemory)) {
    Write-Host "[실패] memory/ 폴더가 없습니다. 패키지가 온전한지 확인하세요." -ForegroundColor Red
    exit 1
}
$srcCount = (Get-ChildItem $srcMemory -Recurse -File -Filter *.md).Count
Write-Host "  소스 메모리: $srcCount 개" -ForegroundColor Gray

# 2. Claude Code 프로젝트 슬러그 계산
#    규칙: 워크스페이스 절대경로에서 : \ / 를 - 로 치환
#    예) C:\Users\kim\scenario-automation  ->  C--Users-kim-scenario-automation
$slug = $root -replace '[:\\/]', '-'
$projectsDir = Join-Path $env:USERPROFILE ".claude\projects"
$destDir = Join-Path $projectsDir $slug
$destMemory = Join-Path $destDir "memory"

Write-Host "  워크스페이스: $root" -ForegroundColor Gray
Write-Host "  메모리 설치 위치: $destMemory" -ForegroundColor Gray
Write-Host ""

# 3. 슬러그 검증 — Claude Code를 한 번이라도 이 폴더에서 실행했다면 폴더가 이미 있다
if (Test-Path $destDir) {
    Write-Host "  [확인] 기존 프로젝트 폴더를 찾았습니다 — 경로가 맞습니다." -ForegroundColor Green
} else {
    Write-Host "  [안내] 프로젝트 폴더가 아직 없어 새로 만듭니다." -ForegroundColor Yellow
    if (Test-Path $projectsDir) {
        $existing = Get-ChildItem $projectsDir -Directory | Select-Object -First 5 -ExpandProperty Name
        if ($existing) {
            Write-Host "         참고 - 이 PC의 기존 프로젝트 폴더 형식:" -ForegroundColor Gray
            $existing | ForEach-Object { Write-Host "           $_" -ForegroundColor DarkGray }
        }
    }
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

# 4. 기존 메모리 백업
if (Test-Path $destMemory) {
    $existingCount = (Get-ChildItem $destMemory -Recurse -File -Filter *.md -ErrorAction SilentlyContinue).Count
    if ($existingCount -gt 0) {
        Write-Host ""
        Write-Host "  [경고] 이미 메모리 $existingCount 개가 있습니다." -ForegroundColor Yellow
        if (-not $Force) {
            $answer = Read-Host "         백업 후 덮어쓸까요? (y/N)"
            if ($answer -ne "y" -and $answer -ne "Y") {
                Write-Host "  중단했습니다. 아무것도 바뀌지 않았습니다." -ForegroundColor Yellow
                exit 0
            }
        }
        $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $backup = "$destMemory`_backup_$stamp"
        Move-Item $destMemory $backup
        Write-Host "  백업 완료: $backup" -ForegroundColor Gray
    }
}

# 5. 복사
Copy-Item $srcMemory $destMemory -Recurse -Force
$copied = (Get-ChildItem $destMemory -Recurse -File -Filter *.md).Count
Write-Host ""
Write-Host "  메모리 $copied 개 설치 완료" -ForegroundColor Green

# 6. 결과
Write-Host ""
Write-Host "=== 설치 끝 ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "  다음:" -ForegroundColor White
Write-Host "    1) python verify.py     설치 검증" -ForegroundColor Gray
Write-Host "    2) claude               이 폴더에서 실행" -ForegroundColor Gray
Write-Host ""
Write-Host "  docx 산출물(기획안·트리트먼트)을 쓸 거면:" -ForegroundColor White
Write-Host "    pip install python-docx" -ForegroundColor Gray
Write-Host ""
