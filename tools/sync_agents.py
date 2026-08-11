#!/usr/bin/env python3
"""sync_agents.py — 에이전트 정의 동기화

Claude Code 는 `~/.claude/agents/` 를 읽는다. 그런데 그 폴더는 git 밖이라
버전 이력도 없고 남에게 넘길 수도 없다. 그래서 저장소 안 `agents/` 를 정본으로 두고
둘을 맞춘다.

    python tools/sync_agents.py             차이만 확인 (기본)
    python tools/sync_agents.py --to-repo   개인 폴더 -> 저장소  (내가 고친 걸 커밋할 때)
    python tools/sync_agents.py --to-home   저장소 -> 개인 폴더  (클론 받은 사람이 쓸 때)
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # 윈도우 cp949 콘솔 대응
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parent.parent / "agents"
HOME = Path.home() / ".claude" / "agents"


def read(p: Path) -> dict[str, str]:
    if not p.is_dir():
        return {}
    return {f.name: f.read_text(encoding="utf-8") for f in sorted(p.glob("*.md"))}


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--to-repo", action="store_true", help="개인 폴더 -> 저장소")
    g.add_argument("--to-home", action="store_true", help="저장소 -> 개인 폴더")
    args = ap.parse_args()

    src, dst = (HOME, REPO) if args.to_repo else (REPO, HOME)

    if args.to_repo or args.to_home:
        if not src.is_dir():
            print(f"원본 폴더가 없습니다: {src}")
            return 1
        dst.mkdir(parents=True, exist_ok=True)
        n = 0
        for f in sorted(src.glob("*.md")):
            target = dst / f.name
            if not target.exists() or target.read_text(encoding="utf-8") != f.read_text(encoding="utf-8"):
                shutil.copy2(f, target)
                n += 1
        print(f"{src}  ->  {dst}")
        print(f"갱신 {n}개 / 전체 {len(list(src.glob('*.md')))}개")
        return 0

    # 확인 모드
    r, h = read(REPO), read(HOME)
    only_repo = sorted(set(r) - set(h))
    only_home = sorted(set(h) - set(r))
    differ = sorted(k for k in set(r) & set(h) if r[k] != h[k])

    print(f"저장소  {REPO}  — {len(r)}개")
    print(f"개인    {HOME}  — {len(h)}개")
    if not (only_repo or only_home or differ):
        print("\n일치합니다.")
        return 0
    if only_repo:
        print("\n저장소에만 있음:")
        for k in only_repo:
            print("  -", k)
    if only_home:
        print("\n개인 폴더에만 있음  (--to-repo 로 저장소에 반영):")
        for k in only_home:
            print("  -", k)
    if differ:
        print("\n내용이 다름:")
        for k in differ:
            print("  -", k)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
