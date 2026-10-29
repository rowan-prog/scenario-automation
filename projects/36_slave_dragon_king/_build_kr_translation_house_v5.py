# -*- coding: utf-8 -*-
"""노예라 불린 용의 공주 10.29 수정고(인물 설정 + 1~8화) 한국어 번역본 -> 하우스 양식 docx.

입력 = 36_slave_dragon_king_writer_free_v5_cn.txt / _v5_kr_body.txt (줄 대 줄).
무료 1~8화(피칭 페이지 기준) -> 8화 제목에 페이월 표기.
"""
import os, re, sys
sys.path.insert(0, r'C:\Users\Rowan\scenario-automation\tools')
from house_script_docx import build

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '노예라 불린 용의 공주_작가 무료회차 수정고(10.29·1-8화)_한국어 번역본.docx')
TITLE = '노예라 불린 용의 공주 — 작가 무료회차 수정고(10.29) · 인물 설정 + 1~8화 · 한국어 번역본'
LAST_FREE = 8

# 말풍선 — {중문 원고 줄 번호(1부터): [문단...]}
C = {
    22: ['[인물 설정] 웨슬리가 3·6·7·8화에 나오는데 인물 설정에 칸이 없어요.', '[고칠 것] (웨슬리를 살리면) 조연에 웨슬리 칸 추가'],
    29: ['[인물 설정과 본문] 「毫不留情地扇艾薇巴掌」 — 본문에서 도미닉은 칼을 휘두르고(4·5화) 걷어차고 누르기만 해요(8화). 뺨은 7화에 바네사가 때려요. (10월 28일에 말씀드린 곳)',
         '[고칠 줄] 他会毫不留情地拔剑，要一寸寸敲碎艾薇的骨头'],
    58: ['[대사 줄 표기] 말투 지시 「（轻声呢喃）」가 쌍점 뒤에 있어서, 대사만 뽑으면 지시가 대사로 읽혀요. (10월 28일에 말씀드린 곳)', '[고칠 줄] 埃莉诺（轻声呢喃）：原谅我，宝贝。'],
    70: ['[인물 줄] 세 왕자가 이 씬에서 용으로 내려와 맹세까지 하는데 인물 줄에 없어요. (10월 28일에 말씀드린 곳 · 씬 번호만 001-3 → 001-2)',
         '[고칠 줄] 人物：莎拉、婴儿艾薇、婴儿凡妮莎、爱德华、塞巴斯蒂安、多米尼克'],
    94: ['[오타] 「紧紧的捂着」는 地가 맞아요. (10월 28일에 말씀드린 곳)', '[고칠 줄] 莎拉紧紧地捂着艾薇的嘴'],
    100: ['[인물 줄] 아룡이 울타리를 부수고 달려들어 엎드리는데 인물 줄에 없어요. 1화에 黑龙若干을 넣으신 것과 같은 방식이에요.', '[고칠 것] 人物 줄에 亚龙 추가'],
    120: ['[앞뒤 안 맞음] 쇠사슬은 발목에만 채웠는데(「扣住艾薇脚踝」) 여기선 「周身铁链」(온몸의 쇠사슬)이 끊어져요. 번역도 원고대로 남겼어요.', '[고칠 줄] △艾薇脚踝上的铁链崩断，亚龙动作僵住惊恐呜咽，朝艾薇俯首趴下。'],
    151: ['[중복] 바로 위 바네사 대사 앞의 지문과 같은 줄이 한 번 더 들어갔어요.', '[고칠 것] 이 줄 삭제'],
    164: ['[인물 줄] 에드워드는 3화에 나오지 않아요. 세 왕자는 4화 「爱德华、塞巴斯蒂安和多米尼克大步走来」에서 처음 와요. 반대로 행렬을 끄는 짐승 용은 나오는데 없어요.',
          '[고칠 것] 爱德华 삭제, 亚龙兽 추가'],
    180: ['[인물 줄] 짐승 용들이 급히 멈춰 아이비 앞에 엎드리는데 인물 줄에 없어요.', '[고칠 것] 人物 줄에 亚龙兽 추가'],
    198: ['[오타 확인] 아이비가 말한 건 「没有权利」(권리)인데 여기는 「权力」(권력)예요. 일부러 말을 비튼 게 아니면 오타예요. 번역도 원고대로 남겼어요.', '[고칠 줄] 凡妮莎（怒极反笑）：你跟我谈权利？'],
    243: ['[씬 머리] 정원인데 「内」(실내)이고, 시간·실내외 순서도 다른 씬(「日/外」)과 반대예요. 번역도 원고대로 남겼어요.', '[고칠 줄] 005-2王宫花园/日/外'],
    244: ['[인물 줄·대사] 맞는 사람은 「侍从」(시종)인데 엘레노어 대사는 「拒绝倾听她的真相」(그녀의 진실)이에요. 영어로 옮기면 남자 시종을 두고 her truth가 돼요.', '[고칠 것] 인물 줄과 지문의 侍从 → 侍女'],
    274: ['[오타] 공주와 어울린다는 사람은 웨슬리인데 「她」로 적혀서, 엘레노어 여왕이 공주와 어울린다는 말이 돼요. 번역도 원고대로 남겼어요.', '[고칠 줄] 平民B（仰慕）：他和埃莉诺女王一样伟大！只有他才配得上凡妮莎公主！'],
    283: ['[중복] 「长桌旁」와 「站在餐桌旁」이 겹쳤어요.', '[고칠 줄] △镜头推近。长桌旁，艾薇正站着，看着桌上的精美食物，眼神新奇。'],
    297: ['[인물 줄] 씬 끝 「凡妮莎余光瞥见不远处的爱德华和韦斯利正看向这边」에서 에드워드가 화면에 잡히는데 인물 줄에 없어요.', '[고칠 것] 人物 줄에 爱德华 추가'],
    319: ['[대사 줄 표기] 화자 이름이 두 번 들어갔어요. 번역도 원고대로 남겼어요.', '[고칠 줄] 凡妮莎：哥哥！又是这个泥种！她潜伏进了宴会，现在居然还敢偷窃！她根本就是来捣乱的！'],
}

cn = open(os.path.join(HERE, '36_slave_dragon_king_writer_free_v5_cn.txt'), encoding='utf-8').read().split('\n')
kr = open(os.path.join(HERE, '36_slave_dragon_king_writer_free_v5_kr_body.txt'), encoding='utf-8').read().split('\n')
while cn and not cn[-1].strip(): cn.pop()
while kr and not kr[-1].strip(): kr.pop()
assert len(cn) == len(kr), (len(cn), len(kr))
for a, b in zip(cn, kr):
    assert bool(a.strip()) == bool(b.strip())

DLG = re.compile(r'^\*\*(.+?)\*\*(?:\((.*?)\))?:\s*(.*)$')
items, line2item = [], {}
first_ep = next(i for i, c in enumerate(cn) if re.match(r'^第\d+集$', c.strip()))
for n, (c, k) in enumerate(zip(cn, kr), 1):
    if not c.strip():
        continue
    c, k = c.strip(), k.strip()
    if n - 1 < first_ep:
        kind = 'head' if (n == 1 or c.startswith('【') or c == '灵魂线索人物') else 'text'
        items.append((kind, c, k.replace('**', '')))
    elif re.match(r'^第(\d+)集$', c):
        m = re.match(r'^# 제(\d+)화$', k); assert m, k
        ep = int(m.group(1))
        if ep == LAST_FREE:
            items.append(('ep', f'{c}（付费卡点）', f'{ep}화 (페이월)'))
        else:
            items.append(('ep', c, f'{ep}화'))
    elif re.match(r'^\d{3}-\d', c):
        m1 = re.match(r'^(\d{3}-\d)\s*(.*?)\s*/\s*(.*?)\s*/\s*(.*)$', c)
        m2 = re.match(r'^### (\d{3}-\d)\s+(.*?)\s*/\s*(.*?)\s*/\s*(.*)$', k); assert m1 and m2, (c, k)
        items.append(('scene', f'S#{m1.group(1)}. {m1.group(2)} / {m1.group(3)} / {m1.group(4)}',
                      f'S#{m2.group(1)}. {m2.group(2)} / {m2.group(3)} / {m2.group(4)}'))
    elif c.startswith('人物：'):
        items.append(('cast', c, k))
    elif c.startswith('【'):
        items.append(('mark', c, k))
    elif k.startswith('**'):
        m = DLG.match(k); assert m, k
        name, par, text = m.groups()
        suffix, direction = '', ''
        if par:
            toks = [t.strip() for t in par.split(',', 1)]
            if toks[0] in ('VO', 'OS'):
                suffix, direction = f'({toks[0]})', (toks[1] if len(toks) > 1 else '')
            else:
                direction = par
        kr_line = f'{name}{suffix}: ' + (f'({direction}) ' if direction else '') + text
        items.append(('dlg', c, kr_line.replace('**', '')))
    else:
        items.append(('action', c, re.sub(r'^△ ', '', k).replace('**', '')))
    line2item[n] = len(items) - 1

comments = {line2item[n]: v for n, v in C.items()}
assert len(comments) == len(C)
cnt = build(items, OUT, comments=comments, title=TITLE)
print('items', len(items), 'comments', cnt, OUT)
