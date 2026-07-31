# -*- coding: utf-8 -*-
"""_build_feedback*.py 안의 표 행 단락번호를 초고 실제 번호로 자동 교정."""
import io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = r"C:\Users\Rowan\scenario-automation\projects\16_moses" + "\\"
draft = {}
for ln in open(BASE + '_draft_paras.txt', encoding='utf-8'):
    if '\t' not in ln:
        continue
    n, t = ln.rstrip('\n').split('\t', 1)
    draft[int(n)] = t


def norm(s):
    return re.sub(r'[\s△…·\.\,!\?\'"\-—/()~]+', '', s)


ROW = re.compile(r"\['(\d+)((?:[~·]\d+)*)((?: 뒤 삽입)?)', '((?:[^'\\]|\\.)*)'")

APPLY = '--apply' in sys.argv
for fn in ['_build_feedback.py', '_build_feedback2.py']:
    src = open(BASE + fn, encoding='utf-8').read()
    out_lines = []
    for line in src.split('\n'):
        m = ROW.search(line)
        if not m:
            out_lines.append(line)
            continue
        n, extra, ins, old = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        if ins or old in ('—', '') or '삭제' in old:
            out_lines.append(line)
            continue
        # 가장 긴 연속 조각으로 탐색
        frags = [f for f in re.split(r'…|/', old) if len(norm(f)) >= 8]
        if not frags:
            out_lines.append(line)
            continue
        probe = norm(max(frags, key=lambda f: len(norm(f))))[:24]
        if n in draft and probe in norm(draft[n]):
            out_lines.append(line)
            continue
        hit = [k for k in draft if probe in norm(draft[k])]
        if len(hit) == 1 and hit[0] != n:
            k = hit[0]
            shift = k - n
            new_first = str(k)
            new_extra = ''.join(
                (c if not c.isdigit() else '') for c in '')  # rebuilt below
            if extra:
                parts = re.findall(r'[~·](\d+)', extra)
                seps = re.findall(r'[~·]', extra)
                new_extra = ''.join(s + str(int(p) + shift) for s, p in zip(seps, parts))
            print(f'  {fn}: {n}{extra} → {new_first}{new_extra}   {old[:55]}')
            line = line.replace(f"['{n}{extra}{ins}',", f"['{new_first}{new_extra}{ins}',", 1)
        elif not hit:
            print(f'  ! {fn}: {n} 초고에서 못 찾음 — 수동확인   {old[:55]}')
        out_lines.append(line)
    if APPLY:
        open(BASE + fn, 'w', encoding='utf-8').write('\n'.join(out_lines))
print('APPLIED' if APPLY else 'DRY RUN (--apply 로 반영)')
