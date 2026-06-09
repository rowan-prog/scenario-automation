# -*- coding: utf-8 -*-
"""Format-pass verifier: v41 vs v42 — dialogue/action 무손실 검증.

포맷 패스(헤더·톤 지문·타이틀 카드만 변경)가 본문을 건드리지 않았는지 기계 검증.
usage: python tools/format_pass_verify.py <old.md> <new.md>
"""
import sys, re, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BLOCK_RE = re.compile(r"^\[(VISUAL ?/ ?ACTION|DIALOGUE|KEY CAMERA|VO|INSERT/CUTAWAY|INTERCUT|FLASHBACK[^\]]*|GRAPHIC ?/ ?UI|END HOOK|ON-SCREEN TITLE|UI ?/ ?GRAPHIC)\]\s*$")
PAREN_RE = re.compile(r"\([^)]*\)")


def parse(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    mode = None
    dlg, act, hooks = [], [], []
    counts = {"ep": 0, "scene": 0, "hardcut": 0, "endhook": 0, "korean": 0, "ostitle": 0}
    for ln in lines:
        s = ln.strip()
        if re.match(r"^#{1,2} .*EP\d+", s) and "S#" not in s:
            counts["ep"] += 1
            mode = None
            continue
        if re.match(r"^#{2,3} S#", s):
            counts["scene"] += 1
            mode = None
            continue
        m = BLOCK_RE.match(s)
        if m:
            tag = m.group(1)
            mode = ("DLG" if tag == "DIALOGUE" else
                    "OST" if tag == "ON-SCREEN TITLE" else
                    "ACT" if tag.replace(" ", "") in ("VISUAL/ACTION",) else "OTHER")
            if tag == "END HOOK":
                counts["endhook"] += 1
            if tag == "ON-SCREEN TITLE":
                counts["ostitle"] += 1
            continue
        if s == "Hard Cut.":
            counts["hardcut"] += 1
            mode = None
            continue
        if re.search(r"[가-힣ㄱ-ㆎ]", ln):
            counts["korean"] += 1
        if not s or s == "---":
            continue
        if s.startswith(">"):
            hooks.append(re.sub(r"\s+", " ", s))
            continue
        if mode == "DLG":
            t = PAREN_RE.sub(" ", s)
            t = re.sub(r"\s+", " ", t).strip()
            if t and not t.endswith(":"):
                dlg.append(t)
        elif mode == "ACT":
            act.append(re.sub(r"\s+", " ", s))
    return dlg, act, hooks, counts


def main():
    old_p, new_p = sys.argv[1], sys.argv[2]
    od, oa, oh, oc = parse(old_p)
    nd, na, nh, nc = parse(new_p)
    ok = True

    def seq_diff(name, a, b):
        nonlocal ok
        if a == b:
            print(f"PASS {name}: identical ({len(a)} lines)")
            return
        ok = False
        sa, sb = set(a), set(b)
        dropped = [x for x in a if x not in sb]
        added = [x for x in b if x not in sa]
        print(f"FAIL {name}: old {len(a)} vs new {len(b)} | dropped {len(dropped)} | added {len(added)}")
        for x in dropped[:8]:
            print(f"  - DROPPED: {x[:110]}")
        for x in added[:8]:
            print(f"  - ADDED:   {x[:110]}")

    seq_diff("DIALOGUE(words, parens stripped)", od, nd)
    seq_diff("ACTION", oa, na)
    seq_diff("HOOK CARDS(>)", oh, nh)
    print(f"counts old={oc}")
    print(f"counts new={nc}")
    for k, want in (("ep", 50), ("hardcut", 49), ("endhook", 49), ("korean", 0)):  # endhook = EP수-1 (마지막 EP = 자연 엔딩 END.)
        flag = "PASS" if nc[k] == want else "FAIL"
        if flag == "FAIL":
            ok = False
        print(f"{flag} {k}: {nc[k]} (want {want})")
    if nc["scene"] != oc["scene"]:
        ok = False
        print(f"FAIL scene count: old {oc['scene']} vs new {nc['scene']}")
    else:
        print(f"PASS scene count: {nc['scene']}")
    print("RESULT:", "ALL PASS" if ok else "FAILURES FOUND")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
