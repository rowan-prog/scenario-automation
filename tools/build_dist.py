#!/usr/bin/env python3
"""build_dist.py — 시나리오 자동화 배포 패키지 빌더

이 워크스페이스에서 "다른 사람 PC에서 그대로 돌아가는" 패키지를 만든다.
작품 본문(IP)과 개인 경로는 빼고, 워크플로우·룰·에이전트·메모리·도구·히트작 자산만 담는다.

사용:
    python tools/build_dist.py                     기본 빌드 (히트작 원본 포함)
    python tools/build_dist.py --no-assets         히트작 원본 제외 (외부 배포용)
    python tools/build_dist.py --out D:/some/path  출력 위치 지정
    python tools/build_dist.py --zip               빌드 후 zip 생성
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # 윈도우 cp949 콘솔 대응
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WS = Path(__file__).resolve().parent.parent
HOME = Path.home()
# 에이전트 정의: 저장소 안 사본이 정본. 없으면 개인 폴더로 폴백.
AGENTS_SRC = WS / "agents"
if not AGENTS_SRC.is_dir():
    AGENTS_SRC = HOME / ".claude" / "agents"
MEMORY_SRC = HOME / ".claude" / "projects" / "C--Users-Rowan-scenario-automation" / "memory"
DOCS_SRC = WS / "tools" / "dist_docs"

# 통째로 복사하되 아래 패턴은 제외
EXCLUDE_DIRS = {"_archive_2026-06-10", "__pycache__", "dist_docs", "orphaned_worktrees"}
EXCLUDE_FILE_PREFIX = ("_archived_",)

# IP·개인 정보라서 배포에서 빼는 메모리 (작품별 캐논)
MEMORY_EXCLUDE = {
    "project_locked_out_interactive_game.md",
    "project_she_stole_my_face_status.md",
    "project_offering_high_explicit_direction.md",
    "project_offering_isolde_character_charter.md",
    "project_offering_vael_character_charter.md",
    "project_offering_v34_writing_charter.md",
    "project_overview.md",
}

# 저작권 민감 자산 (--no-assets 로 제외)
ASSET_DIRS = ["config/vertical_drama_hit_scripts"]

# 개인 경로 → 배포용 표기 치환
PATH_SUBS: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"C:[\\/]Users[\\/]Rowan[\\/]\.claude[\\/]projects[\\/]C--Users-Rowan-scenario-automation[\\/]memory[\\/]?"),
        "<홈>/.claude/projects/<워크스페이스 슬러그>/memory/",
    ),
    (
        re.compile(r"C:[\\/]Users[\\/]Rowan[\\/]claude_localiation[\\/]projects[\\/]?"),
        "(원 작성자 로컬 참조 — 배포판 미포함. 아래 예문이 실물 기준)",
    ),
    (
        re.compile(r"C:[\\/]Users[\\/]Rowan[\\/]Downloads[\\/]"),
        "(원 작성자 로컬 파일 — 배포판 미포함) ",
    ),
    (
        re.compile(r"C:[\\/]Users[\\/]Rowan[\\/]scenario-automation[\\/]?"),
        "",
    ),
    (
        re.compile(r"C:[\\/]Users[\\/]Rowan[\\/]"),
        "<홈>/",
    ),
]

# 배포판에 없는 문서를 가리키는 참조 정리
PATH_SUBS += [
    (re.compile(r"`00_START_HERE\.md`"), "`CLAUDE.md`"),
    (re.compile(r" / CLAUDE\.md / PORTING\.md"), " / CLAUDE.md"),
    (re.compile(r"CLAUDE\.md와 PORTING\.md"), "CLAUDE.md"),
]

TEXT_EXT = {".md", ".txt", ".py", ".json"}

stats = {"files": 0, "dirs": 0, "sanitized": 0, "skipped": 0}


def sanitize(text: str) -> tuple[str, bool]:
    changed = False
    for pat, repl in PATH_SUBS:
        text, n = pat.subn(repl, text)
        if n:
            changed = True
    return text, changed


def copy_tree(src: Path, dst: Path, *, memory_mode: bool = False) -> None:
    if not src.exists():
        print(f"    [경고] 원본 없음: {src}")
        return
    for item in sorted(src.rglob("*")):
        rel = item.relative_to(src)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        if item.is_dir():
            continue
        if item.name.startswith(EXCLUDE_FILE_PREFIX):
            stats["skipped"] += 1
            continue
        if memory_mode and item.name in MEMORY_EXCLUDE:
            stats["skipped"] += 1
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if item.suffix.lower() in TEXT_EXT:
            try:
                raw = item.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                shutil.copy2(item, target)
                stats["files"] += 1
                continue
            cleaned, changed = sanitize(raw)
            target.write_text(cleaned, encoding="utf-8")
            if changed:
                stats["sanitized"] += 1
        else:
            shutil.copy2(item, target)
        stats["files"] += 1


def build_claude_md(out: Path) -> None:
    """CLAUDE.md 에서 작품 현황표(IP)를 걷어내고 신규 사용자용 안내로 교체."""
    src = (WS / "CLAUDE.md").read_text(encoding="utf-8")
    lines = src.splitlines()

    start = next((i for i, l in enumerate(lines) if l.startswith("## 현재 작품")), None)
    end = next((i for i, l in enumerate(lines) if l.startswith("새 작품 번호 =")), None)
    if start is None or end is None:
        print("    [경고] CLAUDE.md 작품 표 경계를 못 찾음 — 원본 그대로 복사")
        replacement = lines
    else:
        block = [
            "## 현재 작품",
            "",
            "없음 — 새로 시작하는 워크스페이스다. 작품이 생기면 아래 형식으로 이 표에 한 줄씩 쌓는다.",
            "",
            "| 폴더 | 작품 | 현재 상태 |",
            "|---|---|---|",
            "| `01_slug` | 타이틀 | 현재 phase · 정본 경로 · 잔여 과제 |",
            "",
            "**이 표에 쓰는 것 = 현재 상태 + 포인터뿐.** 이력은 누적하지 말고 `projects/[작품]/[작품]_00_meta.md` 에 쌓는다.",
            "",
            "새 작품 번호 = **01**.",
        ]
        replacement = lines[:start] + block + lines[end + 1 :]

    text = "\n".join(replacement)

    # 메모리 위치 안내 교체
    text = re.sub(
        r"> \*\*메모리 위치:\*\*.*",
        "> **메모리 위치:** 패키지 안의 `memory/` 가 원본이고, 설치 스크립트가 이를 "
        "`<홈>/.claude/projects/<워크스페이스 슬러그>/memory/` 로 복사한다(Claude Code가 실제로 읽는 위치). "
        "둘 중 하나를 고치면 다른 쪽도 맞춰줄 것.",
        text,
    )
    text, _ = sanitize(text)

    # 배포판 머리말 + 최초 실행 부트스트랩
    header = """<!-- Claude Code가 세션 시작 시 자동으로 읽는 파일. 작업 라우팅 표가 이 시스템의 심장이다. -->

# 0. 최초 실행 (세션 시작 시 이것부터 — 30초)

워크스페이스 루트에 `.setup_done` 파일이 **없으면 이번이 첫 세션**이다. 사용자에게 묻지 말고 아래를 순서대로 직접 실행한 뒤, 결과를 세 줄로 보고하고 원래 요청으로 넘어간다.

1. `python verify.py` — 패키지 무결성 확인.
2. 메모리 항목이 FAIL이면 설치한다. Windows = `powershell -ExecutionPolicy Bypass -File install.ps1 -Force` · macOS/Linux = `bash install.sh --force`.
3. `python verify.py` 재실행해 통과 확인.
4. 루트에 `.setup_done` 파일을 만든다 (내용 = 실행 날짜 한 줄).

설치가 실패해도 작업은 진행할 수 있다 — 이 패키지의 `memory/` 폴더를 상대경로로 직접 읽으면 된다. 실패 사실만 사용자에게 알리고 계속한다.

`.setup_done` 이 이미 있으면 이 섹션 전체를 건너뛴다.

---

"""
    (out / "CLAUDE.md").write_text(header + text, encoding="utf-8")
    print("    CLAUDE.md 변환 완료 (부트스트랩 삽입·작품 현황표 제거·경로 치환)")


def build_memory_index(out: Path) -> None:
    """MEMORY.md 의 작품 특수 섹션(IP) 교체."""
    p = out / "memory" / "MEMORY.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    start = text.find("## 작품 특수")
    anchor = text.find("**archive:**")
    if start != -1 and anchor != -1 and anchor > start:
        block = (
            "## 작품 특수\n\n"
            "작품별 캐논 메모리는 배포판에서 제외됨(IP). 새 작품을 시작하면 이 자리에 "
            "`project_[작품]_*.md` 형태로 쌓인다 — 엔진 규칙·확정 캐논·사용자 판정처럼 "
            "코드나 문서에서 되짚을 수 없는 것만.\n\n"
        )
        text = text[:start] + block + text[anchor:]
        p.write_text(text, encoding="utf-8")
        print("    MEMORY.md 인덱스 정리 완료")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(WS.parent / "scenario-automation-dist"))
    ap.add_argument("--no-assets", action="store_true", help="히트작 역대본 원본 제외")
    ap.add_argument("--zip", action="store_true", help="빌드 후 zip 생성")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    print()
    print("=== 배포 패키지 빌드 ===")
    print(f"    소스: {WS}")
    print(f"    출력: {out}")
    print(f"    히트작 원본: {'제외' if args.no_assets else '포함'}")
    print()

    if out.exists():
        print("    기존 출력 폴더 삭제 중...")
        shutil.rmtree(out)
    out.mkdir(parents=True)

    # 1. 코어 자산
    print("[1] 룰·절차·도구")
    for rel in ["config", "prompts", "tools"]:
        copy_tree(WS / rel, out / rel)
        n = sum(1 for _ in (out / rel).rglob("*") if _.is_file())
        print(f"    {rel:10s} {n:4d} 개")

    # 빌더 스크립트 자체는 배포판에 불필요
    for leftover in [out / "tools" / "build_dist.py"]:
        if leftover.exists():
            leftover.unlink()

    # 2. 히트작 원본
    print("[2] 히트작 자산")
    if args.no_assets:
        for rel in ASSET_DIRS:
            target = out / rel
            if target.exists():
                shutil.rmtree(target)
        print("    제외됨 (--no-assets)")
    else:
        for rel in ASSET_DIRS:
            n = sum(1 for _ in (out / rel).rglob("*") if _.is_file()) if (out / rel).exists() else 0
            print(f"    {rel} — {n} 개")

    # 3. 서브 에이전트
    print("[3] 서브 에이전트")
    copy_tree(AGENTS_SRC, out / ".claude" / "agents")
    n = sum(1 for _ in (out / ".claude" / "agents").glob("*.md"))
    print(f"    {n} 종")

    # 4. 메모리
    print("[4] 메모리")
    copy_tree(MEMORY_SRC, out / "memory", memory_mode=True)
    n = sum(1 for _ in (out / "memory").rglob("*.md"))
    print(f"    {n} 개 (작품 캐논 {len(MEMORY_EXCLUDE)} 개 제외)")

    # 5. 진입 문서
    print("[5] 진입 문서")
    build_claude_md(out)
    build_memory_index(out)
    for name in ["README.md", "CASE_STUDIES.md", "SETUP.md", "install.ps1", "install.sh", "verify.py"]:
        src = DOCS_SRC / name
        if not src.exists():
            print(f"    [경고] {name} 없음")
            continue
        if name.endswith(".ps1"):
            # PowerShell 5.1은 BOM 없는 UTF-8을 cp949로 오독한다 → 한글 깨짐 방지
            (out / name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8-sig")
        elif name.endswith(".sh"):
            # CRLF가 섞이면 bash가 죽는다
            (out / name).write_bytes(src.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8"))
        else:
            shutil.copy2(src, out / name)
        print(f"    {name}")

    # 6. 빈 작업 폴더
    print("[6] 작업 폴더")
    (out / "projects").mkdir(exist_ok=True)
    pr = DOCS_SRC / "projects_README.md"
    if pr.exists():
        shutil.copy2(pr, out / "projects" / "README.md")
    (out / "inbox").mkdir(exist_ok=True)
    (out / "inbox" / "README.md").write_text(
        "# inbox/\n\n작업 중 받은 임시 자료를 던져두는 곳. 시스템과 분리돼 있고 버전 관리도 안 한다.\n"
        "원작 대본·참고 자료·외부에서 받은 파일 등을 여기 두고 경로만 알려주면 된다.\n",
        encoding="utf-8",
    )
    print("    projects/ · inbox/ 생성")

    # 7. gitignore
    (out / ".gitignore").write_text(
        "\n".join(
            [
                "# OS",
                ".DS_Store",
                "Thumbs.db",
                "desktop.ini",
                "",
                "# Editor",
                ".vscode/",
                ".idea/",
                "*.swp",
                "",
                "# Secrets",
                ".env",
                "*.token",
                "credentials*",
                "*.pem",
                "*.key",
                "",
                "# Temp",
                "*.tmp",
                "*.bak",
                "~$*",
                "__pycache__/",
                "*.pyc",
                "",
                "# Claude Code 로컬 설정 (에이전트 정의는 .claude/agents/ 라서 커밋됨)",
                ".claude/settings.local.json",
                ".claude/worktrees/",
                "",
                "# 임시 자료 저장소",
                "inbox/*",
                "!inbox/README.md",
                "",
            ]
        ),
        encoding="utf-8",
    )

    total = sum(1 for p in out.rglob("*") if p.is_file())
    size_mb = sum(p.stat().st_size for p in out.rglob("*") if p.is_file()) / 1024 / 1024

    print()
    print("=== 빌드 완료 ===")
    print(f"    파일 {total} 개 · {size_mb:.1f} MB")
    print(f"    경로 치환된 파일 {stats['sanitized']} 개 · 제외 {stats['skipped']} 개")
    print(f"    {out}")

    if args.zip:
        archive = shutil.make_archive(str(out), "zip", root_dir=out)
        zmb = Path(archive).stat().st_size / 1024 / 1024
        print(f"    zip: {archive} ({zmb:.1f} MB)")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
