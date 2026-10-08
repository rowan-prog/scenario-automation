#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
episode_number_check.py — 화 결번·중복·순서·씬 번호 기계 검사 (2026-10-08 사용자 지시)
LLM 판단 0. 화 번호와 줄 번호만 낸다. 대본 검토에 들어가기 전에 먼저 돌린다.

사용자: "검토에서, 에피소드 누락 or 에피소드 넘버링 오류도 종종 있어서 주의."
  - 33번 작가본 = 22화 표제 두 번 · 19화 혼입 / 11번 = 변환 손실로 결번처럼 보임 / 씬 번호 앞자리 틀림.

읽는 화 표기 (줄 맨 앞 · 마크다운 #·** 무시):
  중문  第1集 / 第一集 / 第1话 / 第1回
  한국어 제1화 / 1화
  영어  EP01 / EP.01 / EP 1 / Episode 1
  우리 양식  ## EP2 - S#1 (화 헤더가 따로 없으면 씬 헤더 앞자리로 화를 센다)
씬 표기: 1-1 / 001-1 / EP2 - S#1 (앞자리 = 화 번호) · S#1 / 场1 / 씬1 / Scene 1 (화마다 1부터)

검사:
  ① 화 결번 · 중복 · 역순 · 첫 화가 시작 번호가 아님 · --expect 총 화수와 다름
  ② 한 파일에 중·한·영 화 표기가 같이 있으면 순서대로 번호가 서로 맞나
  ③ 개요 목록(「제1화: 요약…」처럼 긴 줄)과 본문 화 헤더를 따로 세고 개수·번호 대조
  ④ 씬 번호 앞자리가 그 화 번호와 다름 (예: 23화 안에 22-3)
  ⑤ 화 안에서 씬 번호 건너뜀·중복·역순·1이 아닌 시작
  ⑥ 화별 분량이 앞뒤 5화 중앙값의 35% 미만(내용 빠짐 의심) / 1.9배 초과(헤더 빠져 두 화가 붙음·다른 화 혼입 의심 · 1화 제외)
docx는 document.xml을 직접 읽는다 — 표·텍스트박스 포함 · 변경 이력 중 삭제분 제외 · 추가분 포함.

usage: python tools/episode_number_check.py <대본.md|.txt|.docx> [--expect 50] [--start 1]
exit 1 = 오류(✗) 있음 / 0 = 오류 없음(확인 사항 △는 사람이 본다)
"""
import sys, io, re, zipfile, html, statistics, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ---------- 읽기 ----------

def read_docx_lines(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    # 텍스트박스 대체본(mc:Fallback)은 같은 글이 두 번 들어 있으니 뺀다 · 이동 전 원위치(moveFrom)도 뺀다
    xml = re.sub(r"<mc:Fallback\b.*?</mc:Fallback>", "", xml, flags=re.S)
    xml = re.sub(r"<w:moveFrom\b.*?</w:moveFrom>", "", xml, flags=re.S)
    tok = re.compile(r"<w:p(?=[\s>/])[^>]*?(/?)>|</w:p>|<w:t(?:\s[^>]*)?>(.*?)</w:t>|<w:tab/>|<w:br[^>]*/>|<w:cr/>", re.S)
    out, stack = [], []
    for m in tok.finditer(xml):
        s = m.group(0)
        if s.startswith("<w:p") and not s.startswith("<w:pPr"):
            if m.group(1) == "/":
                out.append("")
            else:
                stack.append([])
        elif s == "</w:p>":
            if stack:
                out.extend("".join(stack.pop()).split("\n"))
        elif s == "<w:tab/>":
            if stack:
                stack[-1].append("\t")
        elif m.group(2) is not None:
            if stack:
                stack[-1].append(html.unescape(m.group(2)))
        else:  # br / cr = 줄바꿈
            if stack:
                stack[-1].append("\n")
    return out

def read_lines(path):
    if path.lower().endswith(".docx"):
        return read_docx_lines(path)
    for enc in ("utf-8-sig", "utf-8", "cp949", "gb18030"):
        try:
            with open(path, encoding=enc) as f:
                return f.read().splitlines()
        except UnicodeDecodeError:
            continue
    raise SystemExit(f"인코딩을 못 읽음: {path}")

# ---------- 패턴 ----------

FW = str.maketrans("０１２３４５６７８９－", "0123456789-")
CN_DIGIT = {"零": 0, "〇": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5,
            "六": 6, "七": 7, "八": 8, "九": 9}

def cn2int(s):
    if s.isdigit():
        return int(s)
    total, cur = 0, 0
    for ch in s:
        if ch in CN_DIGIT:
            cur = CN_DIGIT[ch]
        elif ch == "十":
            total += (cur or 1) * 10
            cur = 0
        elif ch == "百":
            total += (cur or 1) * 100
            cur = 0
    return total + cur

LEAD = re.compile(r"^[\s#*_>【\[（(「]+")
EP_CN = re.compile(r"^第\s*([0-9]+|[零〇一二两三四五六七八九十百]+)\s*[集话話回]")
EP_KR = re.compile(r"^(?:제\s*)?([0-9]{1,3})\s*화(?![가-힣])")
EP_EN = re.compile(r"^(?:EP|Ep|ep|EPISODE|Episode|episode)\s*[.#:\-]?\s*([0-9]{1,3})(?![0-9])")
SC_PREFIX = re.compile(r"^(?:EP\s*\.?\s*)?([0-9]{1,3})\s*-\s*(?:S#\s*)?([0-9]{1,3})(?![0-9])(?=[\s.:：/、,，|)）【\[（(一-鿿]|$)", re.I)
SC_PLAIN = re.compile(r"^(?:S\s*#|场景?|场次|씬|SCENE|Scene)\s*\.?\s*([0-9]{1,3})(?![0-9])")
HANGUL = re.compile(r"[가-힣]")
CJK = re.compile(r"[一-鿿]")
LANG_NAME = {"CN": "중문 第N集", "KR": "한국어 N화", "EN": "영어 EP N", "IMPLICIT": "씬 헤더 앞자리(EP N - S#)"}

def norm(line):
    return LEAD.sub("", line.translate(FW)).strip()

def script_lang(text):
    if HANGUL.search(text):
        return "KR"
    if CJK.search(text):
        return "CN"
    return "EN"

def parse_episode_header(line):
    t = norm(line)
    if not t or len(line.strip()) > 200:
        return None
    for lang, pat in (("CN", EP_CN), ("KR", EP_KR), ("EN", EP_EN)):
        m = pat.match(t)
        if not m:
            continue
        rest = t[m.end():]
        if lang == "EN" and re.match(r"\s*[-–—]\s*S#", rest, re.I):
            return None  # "EP2 - S#1" = 씬 헤더
        tail = re.sub(r"^[\s*_:：.\-–—|)）】\]」]+", "", rest).rstrip("*_ 】]」")
        return lang, cn2int(m.group(1)), len(tail)
    return None

def parse_scene_header(line):
    raw = line.translate(FW).strip()
    m = re.match(r"^#([0-9]{1,3})(?![0-9])\s*\S", raw)  # "#1 INT. 세탁실" (# 뒤 띄어쓰기 없는 씬 번호)
    if m:
        return ("plain", None, int(m.group(1)), script_lang(raw[m.end() - 1:]))
    t = norm(line)
    if not t or len(t) > 160:
        return None
    m = SC_PREFIX.match(t)
    if m:
        return ("prefix", int(m.group(1)), int(m.group(2)), script_lang(t[m.end():] or t))
    m = SC_PLAIN.match(t)
    if m:
        return ("plain", None, int(m.group(1)), script_lang(t[m.end():] or t))
    return None

# ---------- 검사 ----------

class Report:
    def __init__(self):
        self.err, self.warn = [], []
    def E(self, s): self.err.append(s)
    def W(self, s): self.warn.append(s)

def split_runs(seq, start):
    """번호가 시작 번호로 되돌아가면 새 묶음(개요 목록 → 본문 등)."""
    runs, cur = [], []
    for num, ln in seq:
        if cur and num == start and cur[-1][0] > start:
            runs.append(cur)
            cur = []
        cur.append((num, ln))
    if cur:
        runs.append(cur)
    return runs

def check_run(label, run, start, expect, rep):
    nums = [n for n, _ in run]
    lines_of = {}
    for n, ln in run:
        lines_of.setdefault(n, []).append(ln)
    lo, hi = min(nums), max(nums)
    if nums[0] != start:
        rep.W(f"{label}: 첫 화가 {start}화가 아니라 {nums[0]}화({run[0][1]}줄) — 일부 범위 원고면 --start {nums[0]}, 아니면 앞 화가 빠진 것")
    for n, lns in sorted(lines_of.items()):
        if len(lns) > 1:
            rep.E(f"{label}: {n}화 표제가 {len(lns)}번 — " + ", ".join(f"{x}줄" for x in lns))
    missing = [n for n in range(lo, hi + 1) if n not in lines_of]
    if missing:
        rep.E(f"{label}: 결번 " + ", ".join(f"{n}화" for n in missing))
    for (a, la), (b, lb) in zip(run, run[1:]):
        if b < a:
            rep.E(f"{label}: 순서가 거꾸로 — {a}화({la}줄) 다음에 {b}화({lb}줄)")
    if expect:
        if hi != expect or len(nums) != expect - start + 1:
            rep.E(f"{label}: 기대 {start}~{expect}화({expect - start + 1}개)인데 마지막 {hi}화 · 헤더 {len(nums)}개 · 서로 다른 화 {len(set(nums))}개")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--expect", type=int, default=0, help="기대 마지막 화 번호(총 화수)")
    ap.add_argument("--start", type=int, default=1, help="이 원고의 첫 화 번호")
    a = ap.parse_args()

    lines = read_lines(a.path)
    rep = Report()
    P = print
    P(f"파일: {a.path}")
    P(f"줄 {len(lines)}")

    # 1) 화 헤더 수집
    cands = {}  # lang -> [(num, line_no, tail_len)]
    scenes = []  # (line_no, style, prefix, sub, lang)
    for i, line in enumerate(lines, 1):
        h = parse_episode_header(line)
        if h:
            lang, num, tlen = h
            cands.setdefault(lang, []).append((num, i, tlen))
            continue
        s = parse_scene_header(line)
        if s:
            scenes.append((i,) + s)
    # 개요 목록 판별: 같은 표기 화 헤더가 3줄 이내 간격으로 3개 이상 붙어 있으면 목록 · 헤더 뒤 글이 30자 넘어도 목록
    eps = {}  # (lang, kind) -> [(num, line_no)]
    for lang, seq in cands.items():
        clusters, cur = [], []
        for c in seq:
            if cur and c[1] - cur[-1][1] > 3:
                clusters.append(cur)
                cur = []
            cur.append(c)
        if cur:
            clusters.append(cur)
        for cl in clusters:
            for num, ln, tlen in cl:
                kind = "list" if (len(cl) >= 3 or tlen > 30) else "body"
                eps.setdefault((lang, kind), []).append((num, ln))

    body_tracks = {lang: seq for (lang, kind), seq in eps.items() if kind == "body"}
    list_tracks = {lang: seq for (lang, kind), seq in eps.items() if kind == "list"}

    implicit = False
    if not body_tracks:
        pref = [(p, ln) for ln, st, p, sub, lg in scenes if st == "prefix"]
        if pref:
            implicit = True
            seq, last = [], None
            for p, ln in pref:
                if p != last:
                    seq.append((p, ln))
                    last = p
            body_tracks = {"IMPLICIT": seq}
    if not body_tracks and not list_tracks:
        P("화 표기를 하나도 못 찾음 — 양식이 다르면 헤더 줄을 직접 확인할 것")
        return 1

    # 2) 트랙별 결번·중복·순서
    P("")
    P("[화 번호]")
    body_runs = {}
    for lang, seq in body_tracks.items():
        runs = split_runs(seq, a.start)
        body_runs[lang] = runs
        for k, run in enumerate(runs, 1):
            label = f"{LANG_NAME[lang]} 본문" + (f" 묶음{k}" if len(runs) > 1 else "")
            check_run(label, run, a.start, a.expect, rep)
            P(f"  {label}: 헤더 {len(run)}개 ({run[0][0]}~{run[-1][0]}화 · {run[0][1]}~{run[-1][1]}줄)")
    for lang, seq in list_tracks.items():
        runs = split_runs(seq, a.start)
        for k, run in enumerate(runs, 1):
            label = f"{LANG_NAME[lang]} 개요 목록" + (f" 묶음{k}" if len(runs) > 1 else "")
            check_run(label, run, a.start, a.expect, rep)
            P(f"  {label}: {len(run)}개 ({run[0][0]}~{run[-1][0]}화 · {run[0][1]}~{run[-1][1]}줄)")
            # 개요 목록 ↔ 본문 대조
            target = body_runs.get(lang) or next(iter(body_runs.values()), None)
            if target:
                bnums = sorted({n for n, _ in target[-1]})
                lnums = sorted({n for n, _ in run})
                if bnums != lnums:
                    only_l = [n for n in lnums if n not in bnums]
                    only_b = [n for n in bnums if n not in lnums]
                    rep.E(f"{label} ↔ 본문 화 목록이 다름 — 개요에만 {only_l or '없음'} / 본문에만 {only_b or '없음'}")

    # 3) 언어 트랙끼리 번호 대조
    main_runs = {lang: runs[-1] if len(runs) > 1 else runs[0] for lang, runs in body_runs.items()}
    if len(main_runs) > 1:
        langs = list(main_runs)
        ref = langs[0]
        for other in langs[1:]:
            ra, rb = main_runs[ref], main_runs[other]
            if len(ra) != len(rb):
                rep.E(f"{LANG_NAME[ref]} {len(ra)}개 vs {LANG_NAME[other]} {len(rb)}개 — 화 헤더 개수가 다름")
            for (na, la), (nb, lb) in zip(ra, rb):
                if na != nb:
                    rep.E(f"같은 자리 화 번호 불일치 — {LANG_NAME[ref]} {na}화({la}줄) vs {LANG_NAME[other]} {nb}화({lb}줄)")
                    break

    # 4) 화 블록 = 주 트랙(헤더 가장 많은 본문 묶음)
    primary_lang = max(main_runs, key=lambda k: len(main_runs[k]))
    primary = main_runs[primary_lang]
    starts = [ln for _, ln in primary]
    nums = [n for n, _ in primary]
    run_end = len(lines)
    # 같은 트랙에 뒤 묶음이 있으면 거기서 끊는다
    for r in body_runs[primary_lang]:
        if r[0][1] > starts[-1]:
            run_end = r[0][1] - 1
            break
    bounds = [(nums[k], starts[k], (starts[k + 1] - 1) if k + 1 < len(starts) else run_end) for k in range(len(starts))]

    def block_of(line_no):
        for k, (n, s, e) in enumerate(bounds):
            if s <= line_no <= e:
                return k
        return None

    # 5) 씬 번호
    P("")
    P("[씬 번호]")
    other_runs = {lang: run for lang, run in main_runs.items()}

    def ep_for(line_no, lang):
        run = other_runs.get(lang) or primary
        cur = None
        for n, ln in run:
            if ln <= line_no:
                cur = (n, ln)
            else:
                break
        return cur

    seqs = {}  # (block, lang, style) -> [(sub, line)]
    n_scene = 0
    for ln, style, pre, sub, lg in scenes:
        k = block_of(ln)
        if k is None:
            continue
        n_scene += 1
        if style == "prefix" and not implicit:
            cur = ep_for(ln, lg)
            if cur and pre != cur[0]:
                rep.E(f"{ln}줄 씬 {pre}-{sub} — {cur[0]}화({cur[1]}줄 헤더) 안에 있는데 앞자리가 {pre}")
        seqs.setdefault((k, lg, style), []).append((sub, ln))
    if implicit:
        # 씬 앞자리로 센 화: 같은 화 번호가 다른 화를 사이에 두고 다시 나오면 중복
        seen = {}
        for n, ln in primary:
            if n in seen:
                rep.E(f"EP{n} 씬이 {seen[n]}줄과 {ln}줄 두 군데로 갈라져 있음 — 사이에 다른 화가 끼었음")
            seen[n] = ln
    # 화마다 1로 안 돌아가고 대본 전체로 이어 매긴 씬 번호(#1~#63 등)는 전체 이음으로 본다
    global_keys = set()
    for lg, style in {(lg, st) for (_, lg, st) in seqs}:
        if style != "plain":
            continue
        blocks = sorted(k for (k, l2, s2) in seqs if l2 == lg and s2 == style)
        if len(blocks) >= 3 and sum(1 for k in blocks if seqs[(k, lg, style)][0][0] == 1) <= 1:
            global_keys.add((lg, style))
            flat = [(s, ln, bounds[k][0]) for k in blocks for s, ln in seqs[(k, lg, style)]]
            P(f"  {lg} 씬 번호 = 대본 전체로 이어 매김 ({flat[0][0]}~{flat[-1][0]})")
            if flat[0][0] != 1:
                rep.W(f"씬 번호가 1이 아니라 {flat[0][0]}부터 시작 ({flat[0][1]}줄)")
            for (a1, l1, e1), (b1, l2, e2) in zip(flat, flat[1:]):
                if b1 == a1:
                    rep.W(f"씬 번호 {a1} 중복 ({e1}화 {l1}줄 · {e2}화 {l2}줄)")
                elif b1 < a1:
                    rep.W(f"씬 번호 거꾸로 {a1} → {b1} ({e2}화 {l2}줄)")
                elif b1 > a1 + 1:
                    rep.W(f"씬 번호 건너뜀 {a1} → {b1} ({e2}화 {l2}줄) — 씬이 빠졌거나 번호만 틀림")
    for (k, lg, style), seq in seqs.items():
        if (lg, style) in global_keys:
            continue
        ep = bounds[k][0]
        subs = [s for s, _ in seq]
        if subs[0] != 1:
            rep.W(f"{ep}화 씬이 1이 아니라 {subs[0]}부터 시작 ({seq[0][1]}줄)")
        for (a1, l1), (b1, l2) in zip(seq, seq[1:]):
            if b1 == a1:
                rep.W(f"{ep}화 씬 번호 {a1} 중복 ({l1}줄 · {l2}줄)")
            elif b1 < a1:
                rep.W(f"{ep}화 씬 번호 거꾸로 {a1} → {b1} ({l2}줄)")
            elif b1 > a1 + 1:
                rep.W(f"{ep}화 씬 번호 건너뜀 {a1} → {b1} ({l2}줄) — 씬이 빠졌거나 번호만 틀림")
    P(f"  씬 헤더 {n_scene}개 · 화 {len(bounds)}개에 배정")

    # 6) 화별 분량
    P("")
    P("[화별 분량]")
    sizes = []
    for n, s, e in bounds:
        body = "".join(lines[s:e])  # 헤더 줄 다음부터
        sizes.append((n, s, len(re.sub(r"\s", "", body))))
    if len(sizes) >= 4:
        med = statistics.median(x for _, _, x in sizes)
        P(f"  화당 글자 중앙값 {int(med)} (1화는 원래 길어서 '붙은 화' 판정에서 뺌 · 길이 판정은 앞뒤 5화 중앙값 기준)")
        for k, (n, s, x) in enumerate(sizes):
            near = [y for j, (_, _, y) in enumerate(sizes) if j != k and abs(j - k) <= 5]
            loc = statistics.median(near) if near else med
            if loc and x < loc * 0.35:
                rep.W(f"{n}화({s}줄) 분량 {x}자 = 앞뒤 화의 {x / loc:.0%} — 내용이 빠졌는지 원본과 대조")
            elif k > 0 and loc and x > loc * 1.9:
                rep.W(f"{n}화({s}줄) 분량 {x}자 = 앞뒤 화의 {x / loc:.1f}배 — 화 헤더가 빠져 두 화가 붙었거나 다른 화가 섞였는지 확인")
    else:
        P("  화가 4개 미만이라 분량 비교 생략")

    # 결과
    P("")
    for s in rep.err:
        P(f"✗ {s}")
    for s in rep.warn:
        P(f"△ {s}")
    if not a.expect:
        P("※ --expect 미지정 — 기획 총 화수와 마지막 화 번호를 직접 맞춰 볼 것")
    P(f"결과: 오류 {len(rep.err)} · 확인 {len(rep.warn)}")
    return 1 if rep.err else 0

if __name__ == "__main__":
    sys.exit(main())
