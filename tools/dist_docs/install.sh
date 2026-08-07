#!/usr/bin/env bash
# install.sh — 시나리오 자동화 메모리 설치 (macOS / Linux / Git Bash)
#
# 하는 일: 이 패키지의 memory/ 185개를 Claude Code가 읽는 위치로 복사한다.
# 그 외 자산(룰·에이전트·프롬프트·도구)은 이 폴더 안에 있어서 복사가 필요 없다.
#
# 사용: bash install.sh          (기존 파일 있으면 물어봄)
#       bash install.sh --force  (묻지 않고 덮어씀)

set -euo pipefail

FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo ""
echo "=== 시나리오 자동화 설치 ==="
echo ""

# 1. 소스 확인
SRC_MEMORY="$ROOT/memory"
if [ ! -d "$SRC_MEMORY" ]; then
  echo "[실패] memory/ 폴더가 없습니다. 패키지가 온전한지 확인하세요."
  exit 1
fi
SRC_COUNT=$(find "$SRC_MEMORY" -name '*.md' -type f | wc -l | tr -d ' ')
echo "  소스 메모리: $SRC_COUNT 개"

# 2. Claude Code 프로젝트 슬러그 계산
#    규칙: 워크스페이스 절대경로에서 : \ / 를 - 로 치환
#    예) /Users/kim/scenario-automation  ->  -Users-kim-scenario-automation
WSPATH="$ROOT"
# Git Bash에서 실행 시 윈도우 경로로 환산 (C:\Users\... 형태를 기준 슬러그로 맞춘다)
if command -v cygpath >/dev/null 2>&1; then
  WSPATH="$(cygpath -w "$ROOT")"
fi
SLUG="$(printf '%s' "$WSPATH" | sed 's/[:\\/]/-/g')"

PROJECTS_DIR="$HOME/.claude/projects"
DEST_DIR="$PROJECTS_DIR/$SLUG"
DEST_MEMORY="$DEST_DIR/memory"

echo "  워크스페이스: $WSPATH"
echo "  메모리 설치 위치: $DEST_MEMORY"
echo ""

# 3. 슬러그 검증
if [ -d "$DEST_DIR" ]; then
  echo "  [확인] 기존 프로젝트 폴더를 찾았습니다 — 경로가 맞습니다."
else
  echo "  [안내] 프로젝트 폴더가 아직 없어 새로 만듭니다."
  if [ -d "$PROJECTS_DIR" ]; then
    echo "         참고 - 이 PC의 기존 프로젝트 폴더 형식:"
    ls -1 "$PROJECTS_DIR" 2>/dev/null | head -5 | sed 's/^/           /'
  fi
  mkdir -p "$DEST_DIR"
fi

# 4. 기존 메모리 백업
if [ -d "$DEST_MEMORY" ]; then
  EXISTING=$(find "$DEST_MEMORY" -name '*.md' -type f 2>/dev/null | wc -l | tr -d ' ')
  if [ "$EXISTING" -gt 0 ]; then
    echo ""
    echo "  [경고] 이미 메모리 $EXISTING 개가 있습니다."
    if [ "$FORCE" -eq 0 ]; then
      read -r -p "         백업 후 덮어쓸까요? (y/N) " ANSWER
      case "$ANSWER" in
        y|Y) ;;
        *) echo "  중단했습니다. 아무것도 바뀌지 않았습니다."; exit 0 ;;
      esac
    fi
    STAMP=$(date +%Y%m%d_%H%M%S)
    mv "$DEST_MEMORY" "${DEST_MEMORY}_backup_${STAMP}"
    echo "  백업 완료: ${DEST_MEMORY}_backup_${STAMP}"
  fi
fi

# 5. 복사
cp -R "$SRC_MEMORY" "$DEST_MEMORY"
COPIED=$(find "$DEST_MEMORY" -name '*.md' -type f | wc -l | tr -d ' ')
echo ""
echo "  메모리 $COPIED 개 설치 완료"

# 6. 결과
echo ""
echo "=== 설치 끝 ==="
echo ""
echo "  다음:"
echo "    1) python3 verify.py    설치 검증"
echo "    2) claude               이 폴더에서 실행"
echo ""
echo "  docx 산출물(기획안·트리트먼트)을 쓸 거면:"
echo "    pip install python-docx"
echo ""
