# -*- coding: utf-8 -*-
"""The Weakest Man in Rome Took Three Wives 작가 무료회차 초고(10.29 · 1~10화) 한국어 번역본 -> 하우스 양식 docx."""
import os, re, sys
sys.path.insert(0, r'C:\Users\Rowan\scenario-automation\tools')
from house_script_docx import build

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'The Weakest Man in Rome Took Three Wives_작가 무료회차 초고(1029·1-10화)_한국어 번역본.docx')
TITLE = 'The Weakest Man in Rome Took Three Wives(로마 최약체가 아내를 셋 얻었다) — 작가 무료회차 초고(10.29) · 1~10화 · 한국어 번역본'
PAYWALL_EP = 10

# 말풍선 — {중문 원고 줄 번호(1부터): [문단...]}  원고 오류는 번역에서 고치지 않고 여기에만 단다.
C = {
    4: ['[오타] 「石塌」는 「石榻」예요. 131줄·137줄도 같아요(130줄은 「石榻」로 맞게 썼어요).',
        '[고칠 줄] △埃里克斜靠在宽大的石榻上，… (131줄 「扑到石榻上」 · 137줄 「摸着石榻上的干草」)'],
    26: ['[자막 표기] 힐다·비비안은 【字幕：…】인데 엘라만 「字幕：」가 빠졌어요.',
         '[고칠 줄] 艾拉【字幕：Ella/Slave/奴隶】满脸惊恐，缩着肩膀瑟瑟发抖。'],
    200: ['[화면 글자] 호감도 창의 이름이 32~140줄은 영어(Hilda·Ella·Vivian)인데 148줄·200줄부터는 중국어(艾拉·薇薇安·希尔达)예요. 화면에 그대로 나가는 글자라 하나로 맞춰야 해요.',
          '[고칠 줄] 光幕变化【Ella好感度：30】。 (148·210·213·250·255·263·311·333줄도 영어 이름으로)'],
    323: ['[연결] 8화에서 목에 입을 맞춘 건 엘라고(301·302줄 「吻在了他的脖子上」), 에릭은 엘라의 가슴께에만 입을 맞췄어요(310줄). 그런데 여기선 엘라 목에 키스 자국이 클로즈업으로 나와요.',
          '[고칠 줄] 310줄 △埃里克坐起身抱住了艾拉，在她的脖颈和胸前未被衣物覆盖的皮肤上胡乱吻着。'],
    373: ['[오타] 「装模做样」는 「装模作样」예요.',
          '[고칠 줄] 达蒙（沉声）：装模作样！'],
}

cn = open(os.path.join(HERE, '46_viking_three_wives_A_writer_free_v1_cn.txt'), encoding='utf-8').read().split('\n')
kr = {}
for ln in open(os.path.join(HERE, '46_viking_three_wives_A_writer_free_v1_kr.txt'), encoding='utf-8').read().split('\n'):
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
    elif m := re.match(r'^(\d+-\d+)\s+(.+?)\s+(日|夜)\s+(内|外)$', c):
        assert k.startswith(f'S#{m.group(1)}. '), k
        items.append(('scene', f'S#{m.group(1)}. {m.group(2)} / {m.group(3)} / {m.group(4)}', k))
    elif c.startswith('人物：'):
        assert k.startswith('인물: '), k
        items.append(('cast', c, k))
    elif c.startswith('△'):
        assert not re.match(r'^[가-힣A-Z0-9 ]{1,12}(\(VO\))?: ', k), (n, k)
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
