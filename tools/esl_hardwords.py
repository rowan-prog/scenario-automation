"""ESL 어휘 결정론 스캐너 — 대사 직관성 기계 게이트 (2026-07-15 신설).

왜 스크립트인가: 모델은(haiku조차) cede/usurp/prenup 같은 단어를 이미 알아서
안 걸린다 — 어휘 난이도는 모델 이해력이 아니라 빈도 사전으로 재야 한다.
localization 워크스페이스 esl_hardwords.py에서 포팅 (Zipf 빈도 컷).

Zipf 감: ~6=최빈(the) · ~4.5=흔함(alive, kiss) · ~3.0=A2-B1 밖(usurp) · <2.5=어려움(prenup).
기본 컷 3.7.

대상: 대본 .md의 대사 라인(`SPEAKER (cue): text` / `SPEAKER: text`)만. △·헤더 제외.
고유명사: Characters: 라인 + 문중 대문자 다수결 휴리스틱으로 면제.

Usage:
  python tools/esl_hardwords.py <script.md> [--threshold 3.7] [--min-pct 70]
출력: hard word 목록(빈도·zipf·예시 라인#) + intuitive_pct(어려운 단어 0인 대사 라인 비율).
exit 1 = intuitive_pct < min-pct.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict

try:
    from wordfreq import zipf_frequency
except ImportError:
    sys.exit("wordfreq 미설치: pip install wordfreq")

DIALOGUE_RE = re.compile(r"^([A-Z][A-Z .'\-]{1,30}?)\s*(?:\(([^)]*)\))?\s*:\s*(.+)$")
CHARACTERS_RE = re.compile(r"^Characters:\s*(.+)$")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")
# 빈도 사전이 이상하게 매기는 축약/기능어
ALWAYS_OK = {
    "im", "ive", "id", "ill", "youre", "youve", "youll", "youd", "hes", "shes",
    "its", "were", "weve", "theyre", "theyve", "dont", "doesnt", "didnt",
    "cant", "wont", "wouldnt", "couldnt", "shouldnt", "isnt", "arent", "wasnt",
    "werent", "hasnt", "havent", "thats", "whats", "theres", "heres", "lets",
    "gonna", "gotta", "wanna", "aint", "os", "vo",
}


def norm(w: str) -> str:
    return re.sub(r"[^a-z]", "", w.lower())


def best_zipf(key: str) -> float:
    """소유격/축약 접미 오탐 방지: prenups→prenup, theyll→they 등 변형 중 최고 빈도."""
    cands = {key}
    for suf in ("s", "ll", "d", "ve", "re"):
        if key.endswith(suf) and len(key) - len(suf) >= 3:
            cands.add(key[: -len(suf)])
    return max(zipf_frequency(c, "en") for c in cands)


def collect_proper_nouns(lines: list[str], dialogue_texts: list[str]) -> set[str]:
    allow: set[str] = set()
    for line in lines:
        m = CHARACTERS_RE.match(line.strip())
        if m:
            for part in re.split(r"[,()/\s]+", m.group(1)):
                p = norm(part)
                if len(p) > 1:
                    allow.add(p)
    # 문중 대문자 다수결: 문장 중간에서 과반 대문자로 등장 + 2회 이상 = 이름 취급
    cap_mid: dict[str, int] = defaultdict(int)
    mid_total: dict[str, int] = defaultdict(int)
    for text in dialogue_texts:
        for sent in re.split(r"[.!?…]+", text):
            toks = WORD_RE.findall(sent)
            for i, t in enumerate(toks):
                if i == 0:
                    continue
                key = norm(t)
                if not key:
                    continue
                mid_total[key] += 1
                if t[0].isupper():
                    cap_mid[key] += 1
    for key, tot in mid_total.items():
        if tot >= 2 and cap_mid[key] * 2 > tot:
            allow.add(key)
    return allow


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--threshold", type=float, default=3.7)
    ap.add_argument("--min-pct", type=float, default=70.0)
    args = ap.parse_args()

    raw = open(args.file, encoding="utf-8").read().splitlines()
    dialogues: list[tuple[int, str, str]] = []  # (line#, speaker, text)
    for i, line in enumerate(raw, 1):
        s = line.strip()
        if s.startswith(("△", "#", "[", "Hard Cut")):
            continue
        m = DIALOGUE_RE.match(s)
        if m:
            dialogues.append((i, m.group(1).strip(), m.group(3)))

    if not dialogues:
        sys.exit("대사 라인 0 — 파일/포맷 확인")

    proper = collect_proper_nouns(raw, [t for _, _, t in dialogues])

    hard: dict[str, dict] = {}
    clean_lines = 0
    for ln, _spk, text in dialogues:
        line_hard = []
        for tok in WORD_RE.findall(text):
            key = norm(tok)
            if len(key) < 3 or key in ALWAYS_OK or key in proper:
                continue
            z = best_zipf(key)
            if 0 < z < args.threshold:
                line_hard.append((key, z))
        if not line_hard:
            clean_lines += 1
        for key, z in line_hard:
            e = hard.setdefault(key, {"zipf": z, "count": 0, "lines": []})
            e["count"] += 1
            if len(e["lines"]) < 3:
                e["lines"].append(ln)

    pct = 100.0 * clean_lines / len(dialogues)
    print(f"dialogue lines: {len(dialogues)}  |  intuitive: {clean_lines}  |  intuitive_pct: {pct:.1f}%  (min {args.min_pct}%)")
    print(f"hard words (zipf < {args.threshold}): {len(hard)} unique")
    for key, e in sorted(hard.items(), key=lambda kv: kv[1]["zipf"]):
        print(f"  {e['zipf']:.2f}  {key:<20} x{e['count']:<3} lines {e['lines']}")
    sys.exit(0 if pct >= args.min_pct else 1)


if __name__ == "__main__":
    main()
