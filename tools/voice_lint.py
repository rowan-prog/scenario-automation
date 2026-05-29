#!/usr/bin/env python3
"""voice_lint.py - mechanical detector for literary / theatrical / poetic tics
in NA vertical-drama scripts. No LLM. A cheap first-pass that filters a script
BEFORE the human reads it, so attention is spent only on real problems.

Catches the exact failure patterns the memory files document:
  HIGH  ANAPHORA   - "One name. One face. My life." / "You took X. You took Y."
        METAPHOR   - event replaced by a figure ("wearing her dead sister's smile")
        KOREAN     - any Hangul (EP body must be English 100%)
  MED   NEG_PIVOT  - rhetorical "..., not ..." / "no X, no Y"
        TRICOLON   - three-beat list cadence "X, Y, and Z."
        THERAPY    - "part of me / the version of me / who I was"
        MIRROR     - possession declaration "you are mine / I am yours"
        CLINICAL   - clinical verb inside human anger (dispose of / eliminate)
        EM_DASH    - 2+ em-dashes on one line (poetic asides)
  LOW   BRITISH    - grey / colour / cancelled / whilst ... (NA spelling only)
        BREATH     - "takes a breath / steadies her breath" stage tic

Usage:
  python tools/voice_lint.py <file.md>
  python tools/voice_lint.py <file.md> --full           # every hit, not just HIGH samples
  python tools/voice_lint.py <file.md> --cat ANAPHORA,METAPHOR
  python tools/voice_lint.py <file.md> --ep 9-50         # only scan those EP headers
"""
import re
import sys
import argparse

sys.stdout.reconfigure(encoding="utf-8")

# ---- simple per-line regex detectors: (category, severity, regex, note) -------
PATTERNS = [
    ("METAPHOR", "HIGH", re.compile(
        r"\b(the shape of|the weight of|the architecture of|a structure|"
        r"like wearing|wears? (it|her|his|my|your)? ?like a|to wear like a|"
        r"a costume|a mask of|stitched together|"
        r"wearing (her |his |my |your |someone|the dead|a dead))\b", re.I),
     "metaphor standing in for the actual event"),
    ("THERAPY", "MED", re.compile(
        r"\b(part of me|some part of|a part of (her|him|me)|"
        r"what i (wanted|needed) was|the version of|a version of (her|him|me|myself)|"
        r"who i (was|am|used to be)|the person i (was|am)|i used to be)\b", re.I),
     "therapy-speak / abstract self-narration"),
    ("MIRROR", "MED", re.compile(
        r"\b(you are mine|i am yours|you'?re mine|i'?m yours|"
        r"you belong to me|mine to (keep|break|ruin))\b", re.I),
     "mirror / possession declaration"),
    ("NEG_PIVOT", "MED", re.compile(
        r",\s+(not|never|nor)\s+\w+|\bno \w+, no \w+\b", re.I),
     "rhetorical negation pivot"),
    ("TRICOLON", "MED", re.compile(
        r"\b[a-z]+,\s+[a-z]+,\s+(and\s+)?[a-z]+[.?!]", ),
     "three-beat list cadence"),
    ("CLINICAL", "MED", re.compile(
        r"\b(dispose of|eliminate|terminate|neutraliz\w*|neutralis\w*|liquidate)\b", re.I),
     "clinical verb inside human anger"),
    ("BRITISH", "LOW", re.compile(
        r"\b(grey|colour|favour|honour|realise|recognise|cancelled|travelled|"
        r"theatre|centre|defence|licence|apologise|organis\w*|whilst|learnt|"
        r"spelt|towards|metre|litre)\b", re.I),
     "British spelling - NA only"),
    ("BREATH", "LOW", re.compile(
        r"\b(takes? a breath|a steadying breath|steadies? (her|his|my|the) breath|"
        r"steadying breath|breathes out|lets out a breath|a shaky breath)\b", re.I),
     "breath-stabilization stage tic"),
]

KOREAN = re.compile(r"[가-힣㄰-㆏]")
EP_HEADER = re.compile(r"\bEP\s?(\d{1,2})\b")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"[A-Za-z']+")
SKIP_PREFIX = ("#", ">", "[", "-", "(", "|", "=")
SEV_RANK = {"HIGH": 0, "MED": 1, "LOW": 2}


def first_word(s):
    m = WORD.search(s)
    return m.group(0).lower() if m else None


def is_speech(line):
    t = line.strip()
    if not t or t.startswith(SKIP_PREFIX):
        return False
    if t.isupper():            # speaker cue / scene slug
        return False
    return any(c.islower() for c in t)


CUE = re.compile(r"^[A-Z][A-Z0-9 .,'’()/&-]{1,38}$")


def is_cue(line):
    """Speaker cue line: LENA / MARA / EILEEN (V.O.) / NOAH (CONT'D)."""
    t = line.strip()
    return bool(CUE.match(t)) and sum(c.isalpha() for c in t) >= 2


def find_anaphora(lineno, text):
    """Within-line anaphora across short fragments: 'One name. One face.'
    Fires only on a run of >=3, OR a run of >=2 where every fragment is <=3
    words (the tight poetic cadence). Natural consecutive 'I ...' speech with
    real clauses does not trip it."""
    sents = [s for s in SENT_SPLIT.split(text.strip()) if s.strip()]
    hits, run = [], []          # run = list of (firstword, wordcount)
    fws = [(first_word(s), len(WORD.findall(s))) for s in sents]

    def flush(r):
        if len(r) >= 3 or (len(r) >= 2 and max(w for _, w in r) <= 3):
            hits.append(("ANAPHORA", "HIGH", lineno, text.strip(),
                         f"anaphora x{len(r)} on '{r[0][0]}'"))

    for fw, wc in fws:
        if run and fw == run[-1][0] and wc <= 6:
            run.append((fw, wc))
        else:
            flush(run)
            run = [(fw, wc)] if fw and wc <= 6 else []
    flush(run)
    return hits


def scan(path, cats, ep_range):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    findings = []
    speech_run = []          # (lineno, firstword, text) for cross-line anaphora
    dialogue = False         # are we inside a spoken-dialogue/VO block?
    cur_ep, in_range = 0, (ep_range is None)
    stats = {"chars": 0, "eps": set(), "hardcut": 0, "iloveyou": 0, "korean": 0}

    for i, raw in enumerate(lines, 1):
        stats["chars"] += len(raw)
        m = EP_HEADER.search(raw)
        if m and raw.lstrip().startswith("#"):
            cur_ep = int(m.group(1))
            stats["eps"].add(cur_ep)
            in_range = ep_range is None or (ep_range[0] <= cur_ep <= ep_range[1])
        if "HARD CUT" in raw.upper():
            stats["hardcut"] += 1
        stats["iloveyou"] += len(re.findall(r"\bi love you\b", raw, re.I))
        if KOREAN.search(raw):
            stats["korean"] += len(KOREAN.findall(raw))
            if in_range:
                findings.append(("KOREAN", "HIGH", i, raw.strip()[:90], "Hangul in body"))
        stripped = raw.strip()
        if not stripped:
            dialogue = False
        elif is_cue(raw):
            dialogue = True
        elif stripped.startswith(("#", "[", ">", "|", "=")):
            dialogue = False
        elif stripped.startswith("("):
            pass                                  # tone tag, keep block state
        # else: plain line keeps current state (dialogue content vs direction)

        if not in_range:
            continue

        text = raw.rstrip("\n")
        for cat, sev, rx, note in PATTERNS:
            if cats and cat not in cats:
                continue
            if rx.search(text):
                findings.append((cat, sev, i, text.strip()[:110], note))

        if (not cats or "ANAPHORA" in cats) and dialogue:
            findings.extend(find_anaphora(i, text))
            # cross-line anaphora over consecutive short dialogue lines
            if is_speech(text) and len(WORD.findall(text)) <= 7:
                fw = first_word(text)
                if speech_run and speech_run[-1][0] == i - 1 and speech_run[-1][1] == fw:
                    speech_run.append((i, fw, text.strip()))
                else:
                    if len(speech_run) >= 3:
                        ln, _, t = speech_run[0]
                        findings.append(("ANAPHORA", "HIGH", ln, t[:110],
                                         f"anaphora over {len(speech_run)} lines"))
                    speech_run = [(i, fw, text.strip())]
            else:
                if len(speech_run) >= 3:
                    ln, _, t = speech_run[0]
                    findings.append(("ANAPHORA", "HIGH", ln, t[:110],
                                     f"anaphora over {len(speech_run)} lines"))
                speech_run = []

        if (not cats or "EM_DASH" in cats) and text.count("—") >= 2:
            findings.append(("EM_DASH", "MED", i, text.strip()[:110], "2+ em-dashes (poetic aside)"))

    return findings, stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--cat", default="")
    ap.add_argument("--ep", default="")
    a = ap.parse_args()

    cats = {c.strip().upper() for c in a.cat.split(",") if c.strip()} or None
    ep_range = None
    if a.ep:
        lo, _, hi = a.ep.partition("-")
        ep_range = (int(lo), int(hi or lo))

    findings, stats = scan(a.file, cats, ep_range)

    counts = {}
    for cat, sev, *_ in findings:
        counts.setdefault(sev, {}).setdefault(cat, 0)
        counts[sev][cat] += 1

    print(f"VOICE LINT  -  {a.file}")
    print(f"chars {stats['chars']:,}   EPs {len(stats['eps'])}   "
          f"HARD CUT {stats['hardcut']}   Korean {stats['korean']}   "
          f"\"I love you\" {stats['iloveyou']}")
    print("=" * 64)
    for sev in ("HIGH", "MED", "LOW"):
        if sev in counts:
            row = "   ".join(f"{c} {n}" for c, n in sorted(counts[sev].items(), key=lambda x: -x[1]))
            print(f"[{sev}] {row}")
    print("=" * 64)

    findings.sort(key=lambda x: (SEV_RANK[x[1]], x[0], x[2]))
    shown = {}
    for cat, sev, lineno, text, note in findings:
        if not a.full:
            if sev != "HIGH":
                continue
            shown.setdefault(cat, 0)
            if shown[cat] >= 6:
                continue
            shown[cat] += 1
        print(f"{sev:4} {cat:10} L{lineno}: {text}")
    if not a.full:
        print("\n(HIGH samples only; run with --full for every hit, "
              "--cat X to filter, --ep 9-50 to scope.)")


if __name__ == "__main__":
    main()
