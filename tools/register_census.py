#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
register_census.py — 인물별 대사 코퍼스 레지스터 검사 (10_writing_standard §D-5-0)
LLM 판단 0. 인물별 분포 숫자만 낸다.

배경 (2026-07-10 — SHE STOLE MY FACE v70 Noah 코퍼스 실증):
개별 라인은 spoken 테스트를 통과하는데 한 인물의 전 대사를 모아 읽으면
단일 레지스터(저음-확신-통제 코치봇)로 수렴하는 결함 — per-line 검수(native-ear·
voice_lint)가 구조적으로 못 잡는 클래스. 코퍼스 통계로 잡는다.

검사 (인물별):
  - 톤 지문 분포 — 최빈 톤 계열(cool 계열: low/flat/even/certain/level/calm/steady/quiet)
    비율 60%+ = FLAG (코치봇/쿨슬롭 의심)
  - 오프너 반복 — 대사 첫 단어 동일 4회+ = FLAG (구문 tic — "Then ..." 류)
  - 문장 형태 비율 — 의문/감탄/파편(미완성)/대시 절단 비율 (전부 낮으면 = 항상 완성문
    아포리즘 = 사람 말 아님)
  - 평균 단어 수

usage: python tools/register_census.py <script.md> [--min-lines 8] [--cool-cap 60] [--opener-cap 3]
"""
import sys, io, re
from collections import defaultdict, Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DIA = re.compile(r"^([A-Z][A-Z0-9'’.\- ]*?)\s*(?:\(([^)]*)\))?:\s*(.+)$")
COOL_TONES = {"low", "flat", "even", "certain", "level", "calm", "steady", "quiet", "cold", "cool", "measured"}
# 대명사/관사 오프너는 영어 자연 빈도라 tic 아님 — 구문형 오프너(Then/Not/Every/So…)만 tic 후보
OPENER_STOPLIST = {"i", "i'm", "i'll", "you", "you're", "she", "she's", "he", "he's", "it", "it's",
                   "we", "they", "the", "a", "that", "that's", "this", "there", "there's", "and",
                   "but", "what", "why", "how", "where", "who", "no", "yes", "don't", "do"}

def main():
    path = sys.argv[1]
    def arg(flag, default, cast=int):
        return cast(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default
    min_lines = arg("--min-lines", 8)
    cool_cap = arg("--cool-cap", 60)
    opener_cap = arg("--opener-cap", 3)

    chars = defaultdict(lambda: {"lines": [], "tones": [], "openers": Counter()})
    with open(path, encoding="utf-8") as f:
        for ln in f:
            s = ln.strip()
            m = DIA.match(s)
            if not m:
                continue
            name, cue, text = m.group(1).strip(), (m.group(2) or ""), m.group(3).strip()
            if name.lower().startswith(("on-screen", "hard cut")):
                continue
            # V.O. 포함 — 같은 인물 보이스
            base = re.sub(r"\s*\(.*$", "", name).strip()
            c = chars[base]
            c["lines"].append(text)
            for t in re.split(r"[,;/]", cue.lower()):
                t = t.strip()
                if t:
                    c["tones"].append(t.split()[0] if t.split() else t)
            first = re.sub(r"[^A-Za-z']", "", text.split()[0]) if text.split() else ""
            if first:
                c["openers"][first.lower()] += 1

    P = print
    P("=" * 60); P(f"register_census :: {path}"); P("=" * 60)
    flags = 0
    for name in sorted(chars, key=lambda n: -len(chars[n]["lines"])):
        c = chars[name]
        n = len(c["lines"])
        if n < min_lines:
            continue
        words = [len(t.split()) for t in c["lines"]]
        avg_w = sum(words) / n
        q = sum(1 for t in c["lines"] if "?" in t)
        ex = sum(1 for t in c["lines"] if "!" in t)
        frag = sum(1 for t in c["lines"] if re.search(r"(—\s*$|\.\.\.\s*$|…\s*$)", t))
        tone_n = len(c["tones"])
        cool = sum(1 for t in c["tones"] if t in COOL_TONES)
        cool_pct = round(100 * cool / tone_n) if tone_n else 0
        top_openers = [(w, k) for w, k in c["openers"].most_common(8)
                       if k > opener_cap and w not in OPENER_STOPLIST]
        cool_flag = tone_n >= 5 and cool_pct >= cool_cap
        opener_flag = bool(top_openers)
        flat_flag = n >= 15 and q == 0 and ex == 0 and frag == 0  # 항상 완성 평서문 = 아포리즘 봇
        noblow_flag = n >= 30 and ex == 0  # 감정 폭발 0 — 주연급이면 D-1-1 위반 신호
        f = cool_flag or opener_flag or flat_flag or noblow_flag
        flags += 1 if f else 0
        P(f"\n{name}: {n} lines · avg {avg_w:.1f}w · ?:{q} !:{ex} 파편/절단:{frag} "
          f"· cool-tone {cool}/{tone_n} ({cool_pct}%)" + ("  <== FLAG" if f else ""))
        if cool_flag:
            P(f"  [COOL-REGISTER] 톤 지문 {cool_pct}% cool 계열 (cap {cool_cap}%) — 코치봇/쿨슬롭 의심 (§D-5-0)")
        if opener_flag:
            for w, k in top_openers:
                P(f"  [OPENER-TIC] \"{w.capitalize()} ...\" 오프너 {k}회 (cap {opener_cap})")
        if flat_flag:
            P(f"  [NO-MESS] 의문 0·감탄 0·파편 0 in {n} lines — 항상 완성 평서문 = 사람 말 아님 의심")
        if noblow_flag and not flat_flag:
            P(f"  [NO-BLOWUP] {n} lines 감탄 0 — 감정 폭발 부재 (주연급이면 §D-1-1 형식-감정 위반 신호)")
        tone_top = Counter(c["tones"]).most_common(6)
        if tone_top:
            P("  tones: " + "  ".join(f"{t}:{k}" for t, k in tone_top))

    P(f"\n[SUMMARY] FLAG 인물: {flags}  => {'PASS' if flags == 0 else 'FLAG (§D-5-0 코퍼스 판정 — 쇼러너가 해당 인물 전 대사 정독 후 수술 여부 결정)'}")

if __name__ == "__main__":
    main()
