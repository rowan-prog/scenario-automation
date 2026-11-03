# -*- coding: utf-8 -*-
"""Kiss the Monster Bride or Die 작가 무료회차 수정고(10.29 · 1~8화) 한국어 번역 워싱본 -> 하우스 양식 docx + md.
원료 = 45_horror_game_hottie_writer_free_v2_kr_washed.txt (원래 번역본에 워싱 85줄 적용). 말풍선 없음(원고 오류 9줄은 번역에서 고침)."""
import os, re, sys
sys.path.insert(0, r'C:\Users\Rowan\scenario-automation\tools')
from house_script_docx import build

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = 'Kiss the Monster Bride or Die_작가 무료회차 수정고(1029·1-8화)_한국어 번역_워싱본'
OUT = os.path.join(HERE, BASE + '.docx')
MD = os.path.join(HERE, BASE + '.md')
TITLE = 'Kiss the Monster Bride or Die(괴물 신부에게 키스하거나, 죽거나) — 작가 무료회차 수정고(10.29) · 1~8화 · 한국어 번역 워싱본'
PAYWALL_EP = 8

cn = open(os.path.join(HERE, '45_horror_game_hottie_writer_free_v2_cn.txt'), encoding='utf-8').read().split('\n')
kr = {}
for ln in open(os.path.join(HERE, '45_horror_game_hottie_writer_free_v2_kr_washed.txt'), encoding='utf-8').read().split('\n'):
    if ln.strip():
        n, t = ln.split('\t', 1)
        kr[int(n)] = t.strip()
src = [n for n, c in enumerate(cn, 1) if c.strip()]
assert sorted(kr) == src, (set(src) ^ set(kr))

items = []
for n in src:
    c, k = cn[n - 1].strip(), kr[n]
    if m := re.match(r'^第(\d+)集$', c):
        ep = int(m.group(1))
        if ep == PAYWALL_EP:
            c = f'第{ep}集（付费卡点）'
            assert k == f'{ep}화 (페이월)', k
        else:
            assert k == f'{ep}화', k
        items.append(('ep', c, k))
    elif m := re.match(r'^(\d+-\d+)/(.*?)/(.*?)/(.*)$', c):
        assert k.startswith(f'S#{m.group(1)}. '), k
        items.append(('scene', f'S#{m.group(1)}. {m.group(2)} / {m.group(3)} / {m.group(4)}', k))
    elif c.startswith('角色：'):
        assert k.startswith('인물: '), k
        items.append(('cast', c, k))
    elif c.startswith('【'):
        items.append(('mark', c, k))
    elif c.startswith('△'):
        assert ': ' not in k[:12], (n, k)
        items.append(('action', c, k))
    else:
        assert re.match(r'^[^：]{1,12}[：]', c), (n, c)
        assert re.match(r'^[^:]{1,16}: ', k), (n, k)
        items.append(('dlg', c, k))

cnt = build(items, OUT, comments={}, title=TITLE)

# md (별표 없이 — 복사해도 기호가 안 딸려 오게)
out = [f'# {TITLE}', '']
for kind, c, k in items:
    if kind == 'ep':
        out += ['', f'## {k}', '']
    elif kind == 'scene':
        out += [f'### {k}', '']
    else:
        out += [k, '']
open(MD, 'w', encoding='utf-8', newline='\n').write('\n'.join(out).rstrip() + '\n')
print('items', len(items), OUT, MD)
