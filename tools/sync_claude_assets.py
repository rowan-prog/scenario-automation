#!/usr/bin/env python3
"""sync_claude_assets.py — 저장소 밖에 사는 Claude 자산을 저장소와 맞춘다

Claude Code 는 개인 폴더(`~/.claude/…`)를 읽는다. 그런데 거기는 git 밖이라
버전 이력도 없고 백업도 안 되고 남에게 넘길 수도 없다. 그래서 저장소 안에
사본을 두고 둘을 맞춘다.

    agents  — 저장소가 정본. 고칠 때 저장소를 고치고 --to-home 으로 내린다.
    memory  — 개인 폴더가 정본(Claude 가 실시간으로 쓴다). 저장소 쪽은 백업 사본이라
              --to-repo 방향으로만 올린다. 정기 커밋(09:00/21:00)이 자동으로 한다.

    python tools/sync_claude_assets.py                  차이 확인 (기본)
    python tools/sync_claude_assets.py --to-repo        개인 폴더 -> 저장소
    python tools/sync_claude_assets.py --to-home        저장소 -> 개인 폴더
    python tools/sync_claude_assets.py --only agents    한쪽만
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # 윈도우 cp949 콘솔 대응
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WS = Path(__file__).resolve().parent.parent
HOME = Path.home()
SLUG = "C--Users-Rowan-scenario-automation"

TARGETS = {
    "agents": (WS / "agents", HOME / ".claude" / "agents"),
    "memory": (WS / "memory", HOME / ".claude" / "projects" / SLUG / "memory"),
}


def files(root: Path) -> dict[str, Path]:
    if not root.is_dir():
        return {}
    return {str(p.relative_to(root)).replace("\\", "/"): p for p in sorted(root.rglob("*.md"))}


def mirror(src: Path, dst: Path) -> tuple[int, int]:
    """src -> dst 복사. (갱신 수, 전체 수). 지우지는 않는다."""
    s = files(src)
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for rel, sp in s.items():
        dp = dst / rel
        dp.parent.mkdir(parents=True, exist_ok=True)
        if not dp.exists() or dp.read_bytes() != sp.read_bytes():
            shutil.copy2(sp, dp)
            n += 1
    return n, len(s)


def report(name: str, repo: Path, home: Path) -> bool:
    r, h = files(repo), files(home)
    only_repo = sorted(set(r) - set(h))
    only_home = sorted(set(h) - set(r))
    differ = sorted(k for k in set(r) & set(h) if r[k].read_bytes() != h[k].read_bytes())

    print(f"[{name}]  저장소 {len(r)}개  /  개인 폴더 {len(h)}개")
    if not (only_repo or only_home or differ):
        print("   일치")
        return True
    for label, items in (("저장소에만", only_repo), ("개인 폴더에만", only_home), ("내용 다름", differ)):
        if items:
            head = ", ".join(items[:6])
            more = f" 외 {len(items) - 6}개" if len(items) > 6 else ""
            print(f"   {label}: {len(items)}개 — {head}{more}")
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--to-repo", action="store_true", help="개인 폴더 -> 저장소")
    g.add_argument("--to-home", action="store_true", help="저장소 -> 개인 폴더")
    ap.add_argument("--only", choices=sorted(TARGETS), help="한쪽만 처리")
    args = ap.parse_args()

    names = [args.only] if args.only else list(TARGETS)
    clean = True

    for name in names:
        repo, home = TARGETS[name]
        if args.to_repo or args.to_home:
            src, dst = (home, repo) if args.to_repo else (repo, home)
            if not src.is_dir():
                print(f"[{name}] 원본 없음 — 건너뜀: {src}")
                continue
            n, total = mirror(src, dst)
            arrow = "개인 -> 저장소" if args.to_repo else "저장소 -> 개인"
            print(f"[{name}] {arrow}  갱신 {n}개 / 전체 {total}개")
        else:
            clean &= report(name, repo, home)

    return 0 if (args.to_repo or args.to_home or clean) else 1


if __name__ == "__main__":
    raise SystemExit(main())
