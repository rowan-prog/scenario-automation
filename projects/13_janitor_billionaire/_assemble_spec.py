# -*- coding: utf-8 -*-
"""fields(KR+CN) + body_kr + body_cn + p0_rough 트리트먼트 -> Vigloo spec.txt 조립"""
import re, io, os

D = os.path.dirname(os.path.abspath(__file__))
R = lambda n: open(os.path.join(D, n), encoding='utf-8').read()

fields = R('13_janitor_billionaire_p1_fields_kr_cn.txt')
kr     = R('13_janitor_billionaire_p1_body_kr.md')
cn     = R('13_janitor_billionaire_p1_body_cn.md')
rough  = R('13_janitor_billionaire_p0_rough.md')


def section(txt, head, nexts):
    """'# head' 다음부터 다음 '# ' 헤더 전까지"""
    m = re.search(r'^#\s*' + re.escape(head) + r'\s*$', txt, re.M)
    if not m:
        raise SystemExit('섹션 없음: ' + head)
    start = m.end()
    end = len(txt)
    for n in nexts:
        m2 = re.search(r'^#\s*' + re.escape(n) + r'\s*$', txt, re.M)
        if m2 and m2.start() > start:
            end = min(end, m2.start())
    return txt[start:end].strip()


# ---- 줄거리 ----
syn_kr = section(kr, '줄거리', ['캐릭터 소개', '금기 사항'])
syn_cn = section(cn, '줄거리 中文', ['캐릭터 中文', '금기 中文', '트리트먼트 中文'])

# ---- 캐릭터: 3줄 블록 5개 ----
def chars(block):
    blocks = [b.strip() for b in re.split(r'\n\s*\n', block) if b.strip()]
    return blocks

ch_kr = chars(section(kr, '캐릭터 소개', ['금기 사항']))
ch_cn = chars(section(cn, '캐릭터 中文', ['금기 中文', '트리트먼트 中文']))
assert len(ch_kr) == 5 and len(ch_cn) == 5, (len(ch_kr), len(ch_cn))

# ---- 금기 ----
ban_kr = section(kr, '금기 사항', [])
ban_cn = section(cn, '금기 中文', ['트리트먼트 中文'])

# ---- 트리트먼트 ----
body = rough.split('**무료회차 줄거리**')[1].split('**레퍼런스 작품**')[0]
eps_kr = re.split(r'\n\s*EP0(\d)\s*\n', body)
kr_eps = {}
for i in range(1, len(eps_kr), 2):
    kr_eps[int(eps_kr[i])] = eps_kr[i + 1].strip()

tcn = R('13_janitor_billionaire_p1_treatment_cn.md')
parts = re.split(r'\n\s*第(\d)集\s*\n', '\n' + tcn)
cn_eps = {}
for i in range(1, len(parts), 2):
    cn_eps[int(parts[i])] = parts[i + 1].strip()
assert sorted(kr_eps) == list(range(1, 10)), sorted(kr_eps)
assert sorted(cn_eps) == list(range(1, 10)), sorted(cn_eps)

treat = []
for n in range(1, 10):
    treat += ['%d화' % n, kr_eps[n], '', '第%d集' % n, cn_eps[n]]
    if n != 9:
        treat.append('')

# ---- 조립 ----
out = []
for bad in ('레이싱', '리프트', '드라이빙 코치', '폐엔진오일', '키링', '1일 이용권', '휠을'):
    for name, t in (('kr', kr), ('cn', cn), ('rough', rough)):
        if bad in t:
            raise SystemExit('구무대 잔재 [%s] in %s' % (bad, name))

out.append('#TEMPLATE ' + os.path.join(D, '_template_krcn_41rows.docx'))
out.append(fields.strip())

def block(idx, lines):
    out.append('#FILL %d' % idx)
    out.extend(lines)

block(12, [syn_kr, '', syn_cn])
for idx, k, c in zip([15, 16, 18, 19, 20], ch_kr, ch_cn):
    block(idx, k.split('\n') + [''] + c.split('\n'))
block(28, ban_kr.split('\n') + [''] + ban_cn.split('\n'))
block(30, treat)

open(os.path.join(D, '13_janitor_billionaire_p1_proposal_spec_kr_cn.txt'), 'w',
     encoding='utf-8').write('\n'.join(out) + '\n')
print('spec OK | 줄거리 KR', len(syn_kr), 'CN', len(syn_cn),
      '| 캐릭터 5+5 | 트리트먼트 9+9')
