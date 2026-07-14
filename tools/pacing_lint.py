#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pacing_lint.py — 연속극 구조(10_writing_standard.md §C) 기계 검사
LLM 판단 0. 숫자 + EP번호만 낸다. "괜찮다" 금지 — 분모/카운트로 증명.

배경 (2026-07-10 — SHE STOLE MY FACE FINAL_v70 사후분석):
§C-2(시간 점프 예산 3~5회/50화)·§C-3(단발 공간 금지)는 집필 표준에 명시돼 있었지만
검수·LOCK 어느 단계에도 이를 세는 기계 게이트가 없었다. 그 결과 EP13~40 구간이
갈라/기부만찬/스튜디오/테라스/현관/전망대 같은 1회성 "행사" 공간을 순회하며
펜트하우스 컴포트 씬으로 돌아오는 TV드라마식 구조로 8회 LOCK 사이클(v37~v70)을
통과했다. Track A(재미) 판단은 반복해서 이 패턴을 놓쳤다 — 카운팅 문제는
기계가 잡아야 사람/LLM이 반복해서 놓치지 않는다.

검사:
  1. SINGLE-USE VENUES — 정확히 1개 화에만 등장하는 공간 (§C-3 단발 공간).
     grace zone = 도입 EP1-2 + 에필로그 마지막 2화 (사건 발화/정리부의 정당한 1회성 —
     카운트 제외·별도 보고). cap은 mid-run에만 적용.
  2. TIME-JUMP BUDGET — 화 헤더 시간 필드의 "큰 점프" 표현 총량 (§C-2, 50화 기준 3~5회)
  3. HOME-BASE DRIFT — 연속 N화(기본 5·배치 게이트 주기와 동일) 블록마다 전역 top-2 공간이
     단 한 번도 등장하지 않는 구간 ("행사 순회" 패턴 탐지)
  4. REPEATED CLOSING DEVICE — 화를 닫는 마지막 △ 1~2개가 특정 키워드(기본: 미디어/화면
     인서트)를 반복 사용하는 화 수 (구조적 tic — D-5-2 장치 반복 금지)
  5. EP-BOUNDARY CONTINUATION — 화 첫 씬 헤더의 Continuous 비율 + 비연속 오프닝 5화+
     스트릭 (§C-2 "다음 화 = 직전 상태 그대로" — 스트릭 = 닫힌 EP병 의심 구간.
     v70 실측: EP29-41 13화 연속 리셋 = 행사 순회 구간과 정확히 일치)
  6. PROTAGONIST PRESENCE — Characters: 로스터 최빈 인물이 빠진 EP 목록 (§C-3 인물 운용
     "거의 모든 회차에 주인공 등장" — 라이터스룸 강의록 §11. 2화+ 연속 부재 = FLAG)

usage: python tools/pacing_lint.py <script.md> [--single-use-cap 3] [--jump-cap 5]
                                    [--homebase-window 5] [--closer-keywords "tv;screen;chyron"]
"""
import sys, io, re
from collections import OrderedDict, Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()

SCENE = re.compile(r"^##\s*EP\s*(\d+)\s*-\s*S#\s*(\d+)\s+(.*)$", re.I)
HARDCUT = re.compile(r"^Hard Cut\.?", re.I)
ACTION = re.compile(r"^△")

JUMP_RE = re.compile(
    r"\b(Next Day|Next Morning|Next Night|Next Week|Following Morning|Following Day|"
    r"Following Night|Another Morning|Another Day|Another Night|The Next Week|A Week Later|"
    r"\d+\s+(Days?|Weeks?|Months?|Years?)\s+Later|Days?\s+Later|Weeks?\s+Later|Months?\s+Later|"
    r"Years?\s+Later)\b", re.I)

DEFAULT_CLOSER_KEYWORDS = ["tv", "screen", "chyron", "headline", "feed", "broadcast", "channel", "phone screen"]

def parse_header(rest):
    """rest = header text after '## EPn - S#n  '. Returns (time_raw, venues[list of base-venue strings])."""
    parts = [p.strip() for p in rest.split(" / ")]
    time_raw = parts[0] if parts else ""
    loc_parts = parts[2:] if len(parts) > 2 else parts[1:]
    venues = []
    for lp in loc_parts:
        for sub in lp.split("/"):
            base = sub.split("·")[0].strip()
            if base and base.lower() not in ("interior", "exterior", "int", "ext", "montage", "intercut"):
                venues.append(base)
    return time_raw, venues

def main():
    path = sys.argv[1]
    def arg(flag, default, cast=int):
        return cast(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default
    single_use_cap = arg("--single-use-cap", 3)
    jump_cap = arg("--jump-cap", 5)
    homebase_window = arg("--homebase-window", 5)
    closer_rate_cap = arg("--closer-rate-cap", 0)  # 0 => auto: ~15% of episode count
    closer_kw = DEFAULT_CLOSER_KEYWORDS
    if "--closer-keywords" in sys.argv:
        closer_kw = [k.strip().lower() for k in sys.argv[sys.argv.index("--closer-keywords") + 1].split(";") if k.strip()]

    lines = load(path)

    # --- parse scenes into per-episode venue sets + time-jump hits ---
    ep_venues = OrderedDict()   # ep -> set(venue)
    venue_first_last = OrderedDict()  # venue -> [ep,...] in order encountered
    jump_hits = []  # (line#, ep, time_raw)
    ep_last_action_before_cut = {}  # ep -> list of last 1-2 △ lines before Hard Cut / EOF
    ep_first_header = OrderedDict()  # ep -> full header text of that EP's FIRST scene
    ep_roster = {}  # ep -> set(first-name tokens from Characters: lines)

    cur_ep = None
    pending_actions = []
    for i, ln in enumerate(lines, 1):
        s = ln.rstrip("\n")
        m = SCENE.match(s)
        if m:
            ep = int(m.group(1))
            cur_ep = ep
            if ep not in ep_first_header:
                ep_first_header[ep] = m.group(3)
            time_raw, venues = parse_header(m.group(3))
            ep_venues.setdefault(ep, set()).update(venues)
            for v in venues:
                venue_first_last.setdefault(v, []).append(ep)
            if JUMP_RE.search(time_raw):
                jump_hits.append((i, ep, time_raw))
            continue
        if s.lower().startswith("characters:") and cur_ep is not None:
            roster = s.split(":", 1)[1]
            roster = re.sub(r"[(\[·].*?[)\]]?(?=,|$)", " ", roster)  # 괄호/부가 설명 대충 제거
            for token in re.split(r"[,/]| and ", roster):
                name = token.strip().split("(")[0].strip()
                m2 = re.match(r"([A-Z][A-Za-z'’.\-]+(?:\s+[A-Z][A-Za-z'’.\-]+)?)", name)
                if m2:
                    ep_roster.setdefault(cur_ep, set()).add(m2.group(1).split()[0])
            continue
        if ACTION.match(s) and cur_ep is not None:
            pending_actions.append(s)
            pending_actions = pending_actions[-2:]
        if HARDCUT.match(s) and cur_ep is not None:
            ep_last_action_before_cut[cur_ep] = list(pending_actions)
            pending_actions = []

    eps_sorted = sorted(ep_venues.keys())
    if not eps_sorted:
        print("NO SCENE HEADERS FOUND — check ## EPn - S#n format"); return

    # --- CHECK 1: single-use venues (grace zones: setup EP1-2 + epilogue last-2 EPs) ---
    max_ep = eps_sorted[-1]
    setup_eps = set(e for e in eps_sorted[:2])
    epilogue_eps = set(e for e in eps_sorted if e >= max_ep - 1)
    single_use_all = {v: eps[0] for v, eps in venue_first_last.items() if len(set(eps)) == 1}
    single_use_grace = {v: e for v, e in single_use_all.items() if e in setup_eps or e in epilogue_eps}
    single_use = {v: e for v, e in single_use_all.items() if v not in single_use_grace}

    # --- CHECK 2: time-jump budget ---
    jump_count = len(jump_hits)

    # --- CHECK 3: home-base drift ---
    venue_ep_count = {v: len(set(eps)) for v, eps in venue_first_last.items()}
    top_venues = sorted(venue_ep_count, key=lambda v: -venue_ep_count[v])[:2]
    drift_blocks = []
    for start in range(0, len(eps_sorted), homebase_window):
        block = eps_sorted[start:start + homebase_window]
        if len(block) < homebase_window:
            continue  # partial trailing block, skip
        block_venues = set()
        for ep in block:
            block_venues |= ep_venues[ep]
        if not (block_venues & set(top_venues)):
            drift_blocks.append((block[0], block[-1], sorted(block_venues)))

    # --- CHECK 4: repeated closing device ---
    closer_eps = []
    for ep, acts in ep_last_action_before_cut.items():
        joined = " ".join(acts).lower()
        if any(k in joined for k in closer_kw):
            closer_eps.append(ep)

    # longest consecutive run of closer_eps
    closer_runs = []
    run = []
    for ep in sorted(closer_eps):
        if run and ep == run[-1] + 1:
            run.append(ep)
        else:
            if len(run) >= 3: closer_runs.append(tuple(run))
            run = [ep]
    if len(run) >= 3: closer_runs.append(tuple(run))
    eff_closer_rate_cap = closer_rate_cap if closer_rate_cap > 0 else max(3, round(len(eps_sorted) * 0.15))
    closer_rate_flag = len(closer_eps) > eff_closer_rate_cap

    # --- CHECK 5: EP-boundary continuation (§C-2 — 다음 화 오프닝 = 직전 상태 그대로) ---
    # 연속(Continuous) 오프닝이 아닌 EP가 5화+ 연달아 이어지면 "닫힌 EP" 의심 구간.
    cont_eps, noncont_eps = [], []
    for ep in eps_sorted[1:]:
        hdr = ep_first_header.get(ep, "")
        (cont_eps if re.search(r"\bContinuous\b", hdr, re.I) else noncont_eps).append(ep)
    noncont_streaks = []
    run = []
    for ep in eps_sorted[1:]:
        if ep in noncont_eps:
            if run and ep == run[-1] + 1:
                run.append(ep)
            else:
                if len(run) >= 5: noncont_streaks.append(tuple(run))
                run = [ep]
        else:
            if len(run) >= 5: noncont_streaks.append(tuple(run))
            run = []
    if len(run) >= 5: noncont_streaks.append(tuple(run))

    # --- CHECK 6: protagonist presence (§C-3 인물 운용 — 라이터스룸 §11) ---
    name_counts = Counter()
    for ep, names in ep_roster.items():
        for nm in names:
            name_counts[nm] += 1
    protagonist = name_counts.most_common(1)[0][0] if name_counts else None
    missing_eps = [ep for ep in eps_sorted if protagonist and protagonist not in ep_roster.get(ep, set())]
    missing_streaks = []
    run = []
    for ep in missing_eps:
        if run and ep == run[-1] + 1:
            run.append(ep)
        else:
            if len(run) >= 2: missing_streaks.append(tuple(run))
            run = [ep]
    if len(run) >= 2: missing_streaks.append(tuple(run))

    P = print
    P("=" * 60); P(f"pacing_lint :: {path}"); P("=" * 60)

    P("\n[1] SINGLE-USE VENUES (§C-3 단발 공간 — mid-run cap=" + str(single_use_cap)
      + f" · grace zone = setup EP{sorted(setup_eps)} + epilogue EP{sorted(epilogue_eps)})")
    P(f"  mid-run count: {len(single_use)}  cap: {single_use_cap}  => {'PASS' if len(single_use) <= single_use_cap else 'FLAG'}")
    for v, ep in sorted(single_use.items(), key=lambda kv: kv[1]):
        P(f"  EP{ep}: {v}")
    if single_use_grace:
        P(f"  (grace {len(single_use_grace)}건 — 카운트 제외·참고만)")
        for v, ep in sorted(single_use_grace.items(), key=lambda kv: kv[1]):
            P(f"   EP{ep}: {v}")

    P("\n[2] TIME-JUMP BUDGET (§C-2 — 50화 기준 3~5회, cap=" + str(jump_cap) + ")")
    P(f"  count: {jump_count}  cap: {jump_cap}  => {'PASS' if jump_count <= jump_cap else 'FLAG'}")
    for i, ep, t in jump_hits:
        P(f"  L{i} EP{ep}: \"{t}\"")

    P(f"\n[3] HOME-BASE DRIFT (연속 {homebase_window}화 블록 중 top-2 공간 {top_venues} 0회 등장)")
    P(f"  drifting blocks: {len(drift_blocks)}  => {'PASS' if not drift_blocks else 'FLAG'}")
    for s, e, vs in drift_blocks:
        P(f"  EP{s}-EP{e}: {vs}")

    P(f"\n[4] REPEATED CLOSING DEVICE (키워드: {closer_kw})")
    P(f"  화 수: {len(closer_eps)}  cap: {eff_closer_rate_cap} (~15% of {len(eps_sorted)}화)  {sorted(closer_eps)}")
    P(f"  연속 3화+ 런: {len(closer_runs)}")
    for run in closer_runs:
        P(f"  EP{run[0]}-EP{run[-1]} ({len(run)}화 연속)")
    P(f"  => {'PASS' if not closer_runs and not closer_rate_flag else 'FLAG'}")

    P(f"\n[5] EP-BOUNDARY CONTINUATION (§C-2 — 다음 화 = 직전 상태 그대로가 기본값)")
    total_bd = len(eps_sorted) - 1
    P(f"  Continuous 오프닝: {len(cont_eps)}/{total_bd} ({round(100*len(cont_eps)/max(1,total_bd))}%)  {cont_eps}")
    P(f"  비연속 5화+ 스트릭: {len(noncont_streaks)}  => {'PASS' if not noncont_streaks else 'FLAG (닫힌 EP병 의심 구간 — 화 경계가 매번 시간/장소 리셋)'}")
    for st in noncont_streaks:
        P(f"  EP{st[0]}-EP{st[-1]} ({len(st)}화 연속 리셋 오프닝)")

    P(f"\n[6] PROTAGONIST PRESENCE (§C-3 인물 운용 — 주인공 = 로스터 최빈 인물 추정: {protagonist})")
    P(f"  부재 EP: {len(missing_eps)}/{len(eps_sorted)}  {missing_eps}")
    P(f"  2화+ 연속 부재: {len(missing_streaks)}  => {'PASS' if not missing_streaks else 'FLAG (주인공 스토리 이탈 구간)'}")
    for st in missing_streaks:
        P(f"  EP{st[0]}-EP{st[-1]}")

    P("\n[VENUE REUSE TABLE]")
    for v in sorted(venue_ep_count, key=lambda v: -venue_ep_count[v]):
        eps_list = sorted(set(venue_first_last[v]))
        P(f"  {venue_ep_count[v]:>2}x  {v}  {eps_list}")

    P("\n[SUMMARY]")
    all_pass = (len(single_use) <= single_use_cap and jump_count <= jump_cap
                and not drift_blocks and not closer_runs and not closer_rate_flag
                and not noncont_streaks and not missing_streaks)
    P(f"  single-use<=cap:{len(single_use) <= single_use_cap}  jump<=cap:{jump_count <= jump_cap}  "
      f"no-drift-blocks:{not drift_blocks}  closer-ok:{not closer_runs and not closer_rate_flag}  "
      f"no-reset-streaks:{not noncont_streaks}  protagonist-ok:{not missing_streaks}")
    P(f"  => 구조 게이트 {'PASS' if all_pass else 'FLAG (Track A 쇼러너 판정 — 예외 사유 없으면 재분절 검토)'}")

if __name__ == "__main__":
    main()
