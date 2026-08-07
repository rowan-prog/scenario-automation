#!/usr/bin/env python3
"""verify.py — 시나리오 자동화 패키지 검증

패키지가 온전한지, 메모리가 설치됐는지, 도구가 돌아가는지 확인한다.
사용: python verify.py
"""
from __future__ import annotations

import os
import py_compile
import re
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # 한글 윈도우 cp949 콘솔 대응
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent

# (경로, 최소 개수, 설명)
EXPECTED_COUNTS = [
    (".claude/agents", 14, "서브 에이전트"),
    ("memory", 180, "메모리"),
    ("prompts", 15, "단계별 절차"),
    ("tools", 8, "기계 도구"),
    ("config/personas", 10, "검토 페르소나"),
]

REQUIRED_FILES = [
    "CLAUDE.md",
    "README.md",
    "config/00_vertical_dna.md",
    "config/10_writing_standard.md",
    "config/20_review_standard.md",
    "config/30_writer_feedback_standard.md",
    "config/evaluators.md",
    "config/vertical_drama_hit_scripts_analysis/hit_dna_priority8.md",
    "config/vertical_drama_hit_scripts_analysis/craft_lecture_liv_writersroom2.md",
    "memory/MEMORY.md",
]

OPTIONAL_ASSETS = [
    ("config/vertical_drama_hit_scripts", "히트작 역대본 원본 — 없으면 집필 품질 기준이 내려간다"),
    ("config/pitch_references", "피칭 실적 데이터"),
    ("config/target_research", "권역별 타깃 리서치"),
]

results: list[tuple[bool, str]] = []
warnings: list[str] = []


def ok(msg: str) -> None:
    results.append((True, msg))


def fail(msg: str) -> None:
    results.append((False, msg))


def warn(msg: str) -> None:
    warnings.append(msg)


def count_md(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for _ in path.rglob("*.md"))


def count_files(path: Path, pattern: str = "*") -> int:
    if not path.is_dir():
        return 0
    return sum(1 for p in path.rglob(pattern) if p.is_file())


print()
print("=== 시나리오 자동화 패키지 검증 ===")
print(f"    {ROOT}")
print()

# 1. 필수 파일
print("[1] 필수 파일")
for rel in REQUIRED_FILES:
    p = ROOT / rel
    if p.is_file():
        ok(f"{rel}")
        print(f"    OK   {rel}")
    else:
        fail(f"{rel} 없음")
        print(f"    FAIL {rel} — 없음")
print()

# 2. 자산 개수
print("[2] 자산 개수")
for rel, minimum, label in EXPECTED_COUNTS:
    p = ROOT / rel
    n = count_files(p, "*.md") if rel != "tools" else count_files(p, "*.py")
    if n >= minimum:
        ok(f"{label} {n}")
        print(f"    OK   {label:14s} {n:4d} 개")
    else:
        fail(f"{label} {n}/{minimum}")
        print(f"    FAIL {label:14s} {n:4d} 개 (기대 {minimum} 이상)")
print()

# 3. 선택 자산
print("[3] 선택 자산")
for rel, note in OPTIONAL_ASSETS:
    p = ROOT / rel
    n = count_files(p)
    if n > 0:
        print(f"    OK   {rel} — {n} 개")
    else:
        print(f"    --   {rel} — 미포함")
        warn(f"{rel} 미포함: {note}")
print()

# 4. 메모리 설치 상태
print("[4] 메모리 설치 (Claude Code가 읽는 위치)")
slug = re.sub(r"[:\\/]", "-", str(ROOT))
if os.name != "nt":
    # 윈도우 외 환경에서는 경로 그대로 슬러그화
    slug = re.sub(r"[:\\/]", "-", str(ROOT))
home_memory = Path.home() / ".claude" / "projects" / slug / "memory"
src_n = count_md(ROOT / "memory")
if home_memory.is_dir():
    dst_n = count_md(home_memory)
    if dst_n >= src_n * 0.9:
        ok(f"메모리 설치됨 {dst_n}")
        print(f"    OK   {dst_n} 개 설치됨")
        print(f"         {home_memory}")
    else:
        fail(f"메모리 부분 설치 {dst_n}/{src_n}")
        print(f"    FAIL {dst_n} 개만 있음 (패키지에는 {src_n} 개) — install 스크립트 재실행")
else:
    fail("메모리 미설치")
    print("    FAIL 설치 안 됨 — install.ps1 (Windows) 또는 install.sh 를 실행하세요")
    print(f"         기대 위치: {home_memory}")
print()

# 5. 도구 문법 검사
print("[5] 기계 도구")
tools = sorted((ROOT / "tools").glob("*.py")) if (ROOT / "tools").is_dir() else []
broken = []
with tempfile.TemporaryDirectory() as tmpdir:
    for t in tools:
        try:
            py_compile.compile(str(t), doraise=True, cfile=str(Path(tmpdir) / (t.stem + ".pyc")))
        except Exception as e:  # noqa: BLE001
            broken.append((t.name, str(e).split("\n")[0]))
if tools and not broken:
    ok(f"도구 {len(tools)}종 문법 정상")
    print(f"    OK   {len(tools)} 종 전부 문법 정상")
else:
    for name, err in broken:
        fail(f"{name} 문법 오류")
        print(f"    FAIL {name}: {err}")
    if not tools:
        fail("도구 없음")
        print("    FAIL tools/ 에 파이썬 파일이 없음")

try:
    import docx  # noqa: F401

    print("    OK   python-docx 설치됨 (docx 산출물 사용 가능)")
except ImportError:
    print("    --   python-docx 없음")
    warn("python-docx 미설치: 기획안·트리트먼트 docx 빌더를 쓰려면 `pip install python-docx`")
print()

# 6. 배포 위생 — 원 작성자 개인 경로 잔재
print("[6] 배포 위생")
leaked = []
pattern = re.compile(r"C:[\\/]Users[\\/]Rowan", re.IGNORECASE)
scan_targets = [ROOT / "CLAUDE.md", ROOT / "config", ROOT / "prompts", ROOT / "memory", ROOT / ".claude"]
for target in scan_targets:
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = [p for p in target.rglob("*") if p.suffix in {".md", ".py", ".txt"} and p.is_file()]
    else:
        continue
    for p in files:
        try:
            if pattern.search(p.read_text(encoding="utf-8", errors="ignore")):
                leaked.append(p.relative_to(ROOT))
        except OSError:
            continue
if leaked:
    warn(f"원 작성자 개인 경로가 남은 파일 {len(leaked)}개 (동작에는 영향 없음)")
    print(f"    --   개인 경로 잔재 {len(leaked)} 개")
    for p in leaked[:5]:
        print(f"         {p}")
else:
    ok("개인 경로 잔재 없음")
    print("    OK   개인 경로 잔재 없음")
print()

# 결과
passed = sum(1 for good, _ in results if good)
failed = [msg for good, msg in results if not good]

print("=" * 46)
if failed:
    print(f"결과: {passed} 통과 / {len(failed)} 실패")
    print()
    for msg in failed:
        print(f"  실패 - {msg}")
else:
    print(f"결과: 전부 통과 ({passed} 항목)")
if warnings:
    print()
    for w in warnings:
        print(f"  참고 - {w}")
print("=" * 46)
print()
if not failed:
    print("이 폴더에서 `claude` 를 실행하면 됩니다.")
    print()

sys.exit(1 if failed else 0)
