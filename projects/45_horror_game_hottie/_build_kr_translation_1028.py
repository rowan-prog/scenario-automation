# -*- coding: utf-8 -*-
"""Kiss the Monster Bride or Die 작가 무료회차 초고(10.28 · 1~8화) 한국어 번역본 -> 하우스 양식 docx."""
import os, re, sys
sys.path.insert(0, r'C:\Users\Rowan\scenario-automation\tools')
from house_script_docx import build

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'Kiss the Monster Bride or Die_작가 무료회차 초고(1028·1-8화)_한국어 번역본.docx')
TITLE = 'Kiss the Monster Bride or Die(괴물 신부에게 키스하거나, 죽거나) — 작가 무료회차 초고(10.28) · 1~8화 · 한국어 번역본'
PAYWALL_EP = 8

# 말풍선 — {중문 원고 줄 번호(1부터): [문단...]}  원고 오류는 번역에서 고치지 않고 여기에만 단다.
C = {
    4: ['[인물 줄] 22줄에서 말하고 24줄에서 죽는 중년 남자 하객이 1-1 인물 줄에 없어요. 그리고 인물 줄은 「司仪」인데 본문은 「荷官司仪」예요.',
        '[고칠 줄] 角色：莱恩，艾薇，荷官司仪，中年男宾客，宾客若干'],
    29: ['[오타] 「外头」(바깥)는 「歪头」(고개를 갸웃)로 보여요. 번역은 歪头로 옮겼어요.',
         '[고칠 줄] △荷官司仪歪头，没有嘴唇的牙齿颤动。'],
    54: ['[화자 표기] 같은 인물인데 이 대사만 「司仪」예요. 나머지 대사는 전부 「荷官司仪」라서 대사만 뽑으면 두 사람으로 갈려요. 바로 위 53줄 지문도 「司仪」예요.',
         '[고칠 줄] 荷官司仪：为什么你还不动嘴？你想……浪费食物？'],
    158: ['[인물 줄] 매디슨이 170줄에서 입을 막고 171줄에서 말하는데 4-1 인물 줄에 없어요.',
          '[고칠 줄] 角色：莱恩，艾薇，荷官司仪，麦迪逊，邻座宾客，宾客若干'],
    176: ['[소품] 이 줄만 「吊带袜」(가터 스타킹)예요. 152·160·166·169·172줄은 전부 「吊袜带」(가터)라서 들어 올리는 소품이 달라져요. 번역은 원고대로 옮겼어요.',
          '[고칠 줄] △莱恩高高举起吊袜带。'],
    177: ['[오타] 「祝福一种方式」에 的가 빠졌어요.',
          '[고칠 줄] 莱恩：婚礼前把新娘的贴身之物分给宾客，本就是祝福的一种方式。'],
    204: ['[화자 표기] 인물 줄은 「年轻男」「年轻女」인데, 본문 화자는 「年轻男」(223줄)·「年轻男宾客」(229·231줄)·「女友」(227·232줄)로 섞여 있고 6-1 인물 줄은 「年轻男宾客」「女友」예요. 대사만 뽑으면 한 사람이 두 사람으로 갈려요.',
          '[고칠 줄] 角色：莱恩，艾薇，莫莉，露比，邻座宾客，年轻男宾客，女友，宾客若干 / 223줄 年轻男宾客：我拿到了，捧花是我的！'],
    280: ['[인물 줄] 299줄 회상(몰리가 몰래 장미를 가져다줌)은 5화에 없던 장면이라 새로 찍어야 하는데, 7-1 인물 줄에 몰리가 없어요.',
          '[고칠 줄] 角色：莱恩，艾薇，莫莉（闪回），麦迪逊，红发男宾客，邻座宾客，众宾客'],
    299: ['[오타] 장미는 「一只」가 아니라 「一枝」(또는 一朵)예요.',
          '[고칠 줄] △莱恩自信一笑，闪回之前莫莉偷偷为他拿来一枝玫瑰的画面。'],
    339: ['[오타] 「后补」는 「候补」예요. 330줄은 「新郎候选人」이에요.',
          '[고칠 줄] 艾薇：既然是我的新郎候补，那理当佩戴同样的配饰。'],
}

cn = open(os.path.join(HERE, '45_horror_game_hottie_writer_free_v1_cn.txt'), encoding='utf-8').read().split('\n')
kr = {}
for ln in open(os.path.join(HERE, '45_horror_game_hottie_writer_free_v1_kr.txt'), encoding='utf-8').read().split('\n'):
    if ln.strip():
        n, t = ln.split('\t', 1)
        kr[int(n)] = t.strip()
src = [n for n, c in enumerate(cn, 1) if c.strip()]
assert sorted(kr) == src, (set(src) ^ set(kr))

items, line2item = [], {}
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
        assert re.match(r'^[^:]{1,14}: ', k), (n, k)
        items.append(('dlg', c, k))
    line2item[n] = len(items) - 1

comments = {line2item[n]: v for n, v in C.items()}
assert len(comments) == len(C)
cnt = build(items, OUT, comments=comments, title=TITLE)
print('items', len(items), 'comments', cnt, OUT)
