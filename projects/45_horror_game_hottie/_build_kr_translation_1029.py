# -*- coding: utf-8 -*-
"""Kiss the Monster Bride or Die 작가 무료회차 초고(10.29 수정고 · 1~8화) 한국어 번역본 -> 하우스 양식 docx."""
import os, re, sys
sys.path.insert(0, r'C:\Users\Rowan\scenario-automation\tools')
from house_script_docx import build

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'Kiss the Monster Bride or Die_작가 무료회차 수정고(1029·1-8화)_한국어 번역본.docx')
TITLE = 'Kiss the Monster Bride or Die(괴물 신부에게 키스하거나, 죽거나) — 작가 무료회차 수정고(10.29) · 1~8화 · 한국어 번역본'
PAYWALL_EP = 8

# 말풍선 — {중문 원고 줄 번호(1부터): [문단...]}  원고 오류는 번역에서 고치지 않고 여기에만 단다.
C = {
    51: ['[인물 묘사] 몰리는 좀비 들러리인데 벨이 「狼爪」(늑대 발톱)에 나타나요. 늑대 발톱은 늑대인간 루비예요. 번역은 원고대로 옮겼어요.',
         '[고칠 줄] △莫莉抬手，黄铜铃铛出现在手中，歪头一笑。'],
    219: ['[설정] 거울에서 나온 여자를 「魅魔」(서큐버스)로 이름 붙였어요. 기획안에서 서큐버스는 매디슨이 유료에서 되는 모습이라, 여기서 서큐버스가 먼저 나오면 겹쳐요. 4-1 인물 줄도 같이 바꿔야 해요.',
          '[고칠 줄] △特殊视角。镜中女鬼坐在邻座宾客怀中搂着他脖子，薄纱下的身材曼妙，赤足在椅背后纠缠。 (220줄 「魅魔」, 181줄 인물 줄 「魅魔」도 「镜中女鬼」로)'],
    229: ['[인물 줄] 234줄에서 사회자가 말하는데 5-1 인물 줄에 「司仪」가 없어요.',
          '[고칠 줄] 角色：莱恩，艾薇，司仪，莫莉，露比，邻座宾客，年轻男宾客，女友，宾客若干'],
    271: ['[인물 줄] 매디슨이 274줄에서 뛰어나가고 275줄에서 말하는데 6-1 인물 줄에 없어요.',
          '[고칠 줄] 角色：莱恩，艾薇，司仪，麦迪逊，年轻男宾客，女友，倒霉宾客，众宾客'],
    367: ['[연결] 1화에서 몰리가 하객들 앞에서 「你愿意成为今天的新郎吗？」라고 묻고, 아이비도 「今晚我会在你们之中选择一位幸运儿，成为我的……」라고 해서 신랑이 아직 없다는 걸 하객들이 다 들었어요. 그런데 이 줄은 신랑이 따로 있는 것처럼 말해요.',
          '[고칠 줄] 宾客B（低声）：疯了吧？给这种怪物当新郎，跟送死有什么区别？'],
}

cn = open(os.path.join(HERE, '45_horror_game_hottie_writer_free_v2_cn.txt'), encoding='utf-8').read().split('\n')
kr = {}
for ln in open(os.path.join(HERE, '45_horror_game_hottie_writer_free_v2_kr.txt'), encoding='utf-8').read().split('\n'):
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
        assert re.match(r'^[^:]{1,16}: ', k), (n, k)
        items.append(('dlg', c, k))
    line2item[n] = len(items) - 1

comments = {line2item[n]: v for n, v in C.items()}
assert len(comments) == len(C)
cnt = build(items, OUT, comments=comments, title=TITLE)
print('items', len(items), 'comments', cnt, OUT)
