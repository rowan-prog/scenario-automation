# -*- coding: utf-8 -*-
"""작가 대본 한국어 번역본 빌더 (md + docx) — 36 노예라 불린 용의 공주.

입력 = 줄 대 줄 번역 본문(`_kr_body.txt`) + 중문 추출본(`_cn.txt`) — 줄 수가 같아야 한다.
번역 후 메인 워싱(연결 오류 보정)은 PATCH_AFTER 로만 넣는다(원문 줄 대응을 깨지 않게 '뒤에 덧붙이는 줄').
서식 = projects/17_son_of_the_lamp/_build_kr_v3.py 승계(맑은 고딕 · 색 상수 동일).

사용: python _build_kr_translation.py v1|v2
"""
import os
import re
import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
TITLE_KR = '노예라 불린 용의 공주'
TITLE_EN = 'THE DRAGON PRINCESS THEY CALLED A SLAVE'

CFG = {
    'v1': dict(
        cn='36_slave_dragon_king_writer_free_v1_cn.txt',
        kr='36_slave_dragon_king_writer_free_v1_kr_body.txt',
        md='36_slave_dragon_king_writer_free_v1_kr.md',
        docx=f'{TITLE_KR}_작가 대본 1차(1-4화)_한국어 번역본.docx',
        sub='작가 대본 1차  ·  1~4화  ·  한국어 번역본',
        src='THE DRAGON PRINCESS THEY CALLED A SLAVE.docx (중문 · 1~4화)',
    ),
    'v2': dict(
        cn='36_slave_dragon_king_writer_free_v2_cn.txt',
        kr='36_slave_dragon_king_writer_free_v2_kr_body.txt',
        md='36_slave_dragon_king_writer_free_v2_kr.md',
        docx=f'{TITLE_KR}_작가 대본 2.0(1-8화)_한국어 번역본.docx',
        sub='작가 대본 2.0  ·  인물 설정 · 회차 개요 · 1~8화  ·  한국어 번역본',
        src='THE DRAGON PRINCESS THEY CALLED A SLAVE（2.0）.docx (중문 · 인물 설정 + 회차 개요 + 1~8화)',
    ),
    'v3': dict(
        cn='36_slave_dragon_king_writer_free_v3_cn.txt',
        kr='36_slave_dragon_king_writer_free_v3_kr_body.txt',
        md='36_slave_dragon_king_writer_free_v3_kr.md',
        docx=f'{TITLE_KR}_작가 무료회차 최종고(1-9화)_한국어 번역본.docx',
        sub='작가 무료회차 최종고 (10.22)  ·  인물 설정 · 1~9화  ·  한국어 번역본 (검토용 러프)',
        src='THE DRAGON PRINCESS THEY CALLED A SLAVE（10.22）.docx (중문 · 인물 설정 + 1~9화)',
        notes=[
            '원고의 여왕 이름 奥蕾莉亚(오렐리아)는 원작 여왕 이름이라 번역본에서는 엘레노어로 옮겼다. 작가 원고에는 아직 그대로 남아 있다.',
            '인물 설정은 원고 그대로 옮겼다. 원고 설정에는 "이십 년"·"북부 용족"·웨슬리가 남아 있지만, 본문은 18년 뒤이고 웨슬리가 나오지 않는다.',
            '泥种은 "천것", 贱人은 "천한 년"으로 옮겼다. 2.0과 원문이 같은 줄은 2.0 번역을 그대로 쓰고, 바뀐 줄만 새로 옮긴 검토용 러프 번역이다.',
        ],
    ),
    'v4': dict(
        cn='36_slave_dragon_king_writer_free_v4_cn.txt',
        kr='36_slave_dragon_king_writer_free_v4_kr_body.txt',
        md='36_slave_dragon_king_writer_free_v4_kr.md',
        docx=f'{TITLE_KR}_작가 무료회차 수정고(10.27·1-9화)_한국어 번역본.docx',
        sub='작가 무료회차 수정고 (10.27)  ·  인물 설정 · 1~9화  ·  한국어 번역본',
        src='THE DRAGON PRINCESS THEY CALLED A SLAVE（10.27）.docx (중문 · 인물 설정 + 1~9화)',
        notes=[
            '원고의 줄을 하나도 빼거나 고치지 않고 옮겼다. 원고에 있는 오류·오타(빠진 말, 화자 없는 대사, 인물 줄 누락 등)도 번역에 그대로 남겼고, 그 자리마다 말풍선으로 어디가 왜 틀렸는지와 고칠 줄을 달았다.',
            '여왕 이름 埃莉诺는 엘레노어로 옮겼다. 인물 설정의 영문 표기 Aurelia는 원고 그대로 두었다(말풍선 참고).',
            '泥种은 "천것", 贱人은 "천한 년", 贱种은 "천한 것"으로 옮겼다. 10.22 원고와 같은 줄은 10.22 번역을 그대로 썼다.',
        ],
    ),
}

# 한국어 번역본 말풍선 — {원문 줄 번호(1부터): [문단, ...]}. 원고 오류를 번역에 남긴 자리에 단다.
KR_COMMENTS = {
    'v4': {
        18: ['[오타] 사라 칸 "长达多年年" — 年이 겹쳤다.', '[고칠 줄] 通过长达多年的虐待和洗脑'],
        24: ['[인물 설정 ↔ 본문] 도미닉 칸 "在大街上掌掴艾薇"(큰길에서 아이비 뺨을 때린다) — 10.27 본문에는 이 장면이 없다. 10.22 원고 6화에 있던 뺨 때리기가 이번에 빠지면서 설정만 남았다. 지금 큰길(4~6화)에서 도미닉은 칼만 휘두르고, 뺨은 8화 연회장에서 바네사가 때린다.',
             '[고칠 줄] 他可以毫无王室风度地当街对艾薇拔剑相向'],
        27: ['[인물 설정 ↔ 본문] 세바스찬 칸 "在街头和宴会上……总是作为最坚硬的阻碍站出来" — 6화 큰길에서 에드워드가 도미닉을 막을 때 세바스찬은 대사도 동작도 없다. 막아서는 건 9화 연회뿐이다. 10.22 원고 6화의 세바스찬 대사("护卫！把这贱人给我按住！")가 빠지면서 생긴 어긋남이다.',
             '[고칠 줄] 在宴会上，当爱德华因为潜意识的血脉感应想要干预对艾薇的惩罚时……'],
        30: ['[합의 미반영] 중문 이름은 埃莉诺로 바뀌었는데 괄호 영문은 Aurelia(원작 여왕 이름) 그대로다. 지난번 요청은 엘레노어(Eleanor)였다. 영문 대본을 이 칸을 보고 쓰면 원작 이름이 다시 들어간다.',
             '[고칠 줄] 埃莉诺（Eleanor）——伟大的白龙女王', '번역은 원고대로 Aurelia를 남겼다.'],
        32: ['[오타] 여는 따옴표 “만 있고 닫는 따옴표가 없다. 번역도 그대로 남겼다.',
             '[고칠 줄] 따옴표를 지우거나 “王者的血脉从不低头”로 감싼다.'],
        38: ['[오타 · 지난번 요청 미반영] "朝着喷出" — 무엇을 향하는지가 빠졌다. 번역은 빈칸 ( )으로 남겼다.', '[고칠 줄] 黑色龙息即将朝着莎拉喷出！'],
        67: ['[인물 줄] 001-3 인물 줄에 세 왕자가 없다. 세 왕자는 이 씬에서 용으로 내려와 사람으로 변하고 맹세까지 한다.', '[고칠 줄] 人物：莎拉、婴儿艾薇、婴儿凡妮莎、爱德华、塞巴斯蒂安、多米尼克'],
        94: ['[그림 보강] 아기 아이비 이마의 "白龙印记"(흰 용 문양)가 사라지는 컷인데, 앞에서 문양이 생기거나 보이는 컷이 없다. 지문대로 찍으면 없던 문양이 사라지는 그림이 된다.',
             '[고칠 줄] 1화 001-1 엘레노어의 입맞춤 지문 끝에 "特，艾薇额头浮现出白龙印记。" 한 줄.'],
        145: ['[인물 줄] 003-1 인물 줄의 侍女(시녀)는 본문에 한 번도 안 나온다.', '[고칠 줄] 侍女 삭제'],
        173: ['[확인] 씬 헤더는 "王室养龙场/日/外"(실외)인데 흰 용이 "撞破养龙场顶棚"(지붕을 뚫고) 나간다. 2화에서 사육장은 대문을 잠그는 울타리 우리로 나온다.',
              '[고칠 줄] 지붕 있는 건물이면 헤더를 内로, 울타리 우리면 "撞破养龙场围栏"으로.'],
        177: ['[인물 줄] 004-1 인물 줄에 에드워드가 있는데 4화에는 나오지 않는다. 세 왕자는 5화 "人群分开。爱德华、塞巴斯蒂安和多米尼克大步走来。"에서 처음 온다. 이 줄대로 찍으면 4화 행렬 장면에 에드워드가 들어간다.',
              '[고칠 줄] 爱德华 삭제'],
        197: ['[오타] "听的清清楚楚" → "听得清清楚楚"'],
        214: ['[오타] "你是在怪我嘛" → "你是在怪我吗"'],
        229: ['[오타] "配剑" → "佩剑"(바로 다음 6화 첫 줄은 佩剑). 230줄도 같다.'],
        233: ['[인물 줄] 006-1 인물 줄에 마부(车夫)가 없다. 이 씬 끝에서 "车夫挥动缰绳"으로 마부가 행렬을 출발시킨다.', '[고칠 줄] 人物 줄에 车夫 추가'],
        239: ['[표기 오류] 바네사 대사가 화자 이름 없이 지문 기호(△) 줄에 들어가 있고, 그 앞 지문 줄에는 △가 없다. 대사만 뽑으면 이 대사가 지문으로 빠진다. 번역도 원고 모양 그대로 남겼다.',
              '[고칠 줄] 두 줄을 하나로: 凡妮莎（冷笑）：祈福？就凭你？一个满身龙粪味的泥种也配！你的出现，只能是对我宴会的亵渎！'],
        261: ['[연결 오류] 에드워드 속마음 "看到她流血"(저 애가 피 흘리는 걸 보니) — 6화 지문 어디에도 아이비의 피가 없다. 10.22 원고에선 이 앞에서 도미닉이 뺨을 때려 "嘴角瞬间溢出鲜血"였는데, 이번에 뺨 때리기가 칼 피하기로 바뀌면서 피가 빠지고 속마음만 남았다.',
              '[고칠 줄] 236줄 끝에 덧붙임: △重剑劈在地上，艾薇闷哼一声被剑气震飞，重重地摔在地上，嘴角渗出血丝。'],
        271: ['[연결 오류 · 지난번 지적 미반영] 흰 용이 사라진다. 5화 끝에서 푸른 칼날을 맞고 길 위에 쓰러진 흰 용("白龙发出凄厉哀鸣，身躯轰然倒地")이 바로 이어지는 6화에 한 번도 안 나오고, 마지막 컷은 아이비가 "独自"(혼자) 서 있다. 지문대로 찍으면 쓰러진 용이 길에서 없어진다. 7화부터 아이비는 용 없이 연회장에 있다.',
              '[고칠 줄] 艾薇守在倒地的白龙身旁，看着远去的车队。(용이 어떻게 되는지는 검토 보고서 대본 검토 1번 참고)'],
        277: ['[인물 줄] 007-1 인물 줄의 贵族少女(귀족 아가씨)는 7화에 나오지 않는다.', '[고칠 줄] 贵族少女 삭제'],
        301: ['[인물 줄] 008-1 인물 줄에 에드워드가 없다. 본문 "凡妮莎余光瞥见不远处的爱德华正皱着眉头看向这边"에서 화면에 잡힌다(9화에서 바로 끼어드는 근거이기도 하다).', '[고칠 줄] 人物 줄에 爱德华 추가'],
        302: ['[오타] "宴会区长桌上，长桌上摆满" — 长桌上이 겹쳤다.', '[고칠 줄] 宴会区长桌上摆满精致甜点和水果。'],
        348: ['[오타 · 지난번 요청 미반영] "到底是这么了" → "到底是怎么了"'],
    },
}

# 메인 워싱 — {원문 줄 번호(1부터): [그 줄 뒤에 덧붙일 한국어 줄, ...]}
PATCH_AFTER = {
    'v1': {},
    'v2': {
        # (2026-10-14 철회) 002-1 끝 "짐승 용이 쇠사슬을 물어 끊는다" 1줄 추가 — 사용자: 짐승 용이 낑낑대며 엎드리고
        # 씬·에피가 바뀌면 시청자가 바로 메우는 논리라 불필요, 호흡만 끊음 → 작가 원고 그대로.
    },
    'v3': {},
    'v4': {},
}

BLACK = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x86, 0x86, 0x86)
ACC = RGBColor(0x8A, 0x5A, 0x10)
STAGE = RGBColor(0x44, 0x44, 0x44)
LINE = RGBColor(0xD8, 0xCB, 0xB0)
MD = re.compile(r'(\*\*[^*]+\*\*)')
IS_EP = re.compile(r'^#\s*제\s*\d+\s*화\s*$')
IS_SCENE = re.compile(r'^###\s*\d{1,3}-\d')
IS_OUTLINE_EP = re.compile(r'^###\s*\d+\s*화\s*$')
IS_CAST = re.compile(r'^인물\s*[:：]')
SECTION_HEADS = ('인물 설정', '악역', '핵심 배경 인물', '회차 개요')


def load(ver):
    c = CFG[ver]
    cn = open(os.path.join(HERE, c['cn']), encoding='utf-8').read().split('\n')
    kr = open(os.path.join(HERE, c['kr']), encoding='utf-8').read().split('\n')
    while cn and not cn[-1].strip():
        cn.pop()
    while kr and not kr[-1].strip():
        kr.pop()
    if len(cn) != len(kr):
        sys.exit(f'줄 수 불일치: 중문 {len(cn)} / 한국어 {len(kr)}')
    for i, (a, b) in enumerate(zip(cn, kr), 1):
        if bool(a.strip()) != bool(b.strip()):
            sys.exit(f'{i}번 줄 빈 줄 대응 깨짐: 중문 "{a[:30]}" / 한국어 "{b[:30]}"')
    out = []
    for i, line in enumerate(kr, 1):
        out.append(line)
        out.extend(PATCH_AFTER[ver].get(i, []))
    return out


def build(ver):
    c = CFG[ver]
    lines = load(ver)

    # md
    with open(os.path.join(HERE, c['md']), 'w', encoding='utf-8') as f:
        f.write(f'# 《{TITLE_KR}》 {c["sub"]}\n\n원본 = `{c["src"]}`\n\n')
        for n in c.get('notes', []):
            f.write(f'- {n}\n')
        f.write('\n---\n\n')
        f.write('\n'.join(lines) + '\n')

    d = docx.Document()
    s = d.sections[0]
    s.left_margin = s.right_margin = Cm(2.3)
    s.top_margin = s.bottom_margin = Cm(1.9)

    def para(after=0, before=0, keep=False, indent=0, spacing=1.32):
        p = d.add_paragraph()
        pf = p.paragraph_format
        pf.space_after, pf.space_before, pf.line_spacing, pf.keep_with_next = Pt(after), Pt(before), spacing, keep
        if indent:
            pf.left_indent = Pt(indent)
        return p

    def run(p, text, *, size=11, color=BLACK, bold=False):
        r = p.add_run(text)
        r.font.size, r.font.color.rgb, r.bold, r.font.name = Pt(size), color, bold, '맑은 고딕'
        r._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
        return r

    def mdline(p, text, size, color):
        for seg in MD.split(text):
            if seg:
                b = seg.startswith('**')
                run(p, seg[2:-2] if b else seg, size=size, color=(ACC if b else color), bold=b)

    t = para(after=3)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t, TITLE_KR, size=19, bold=True)
    t2 = para(after=3)
    t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t2, TITLE_EN, size=11, color=ACC)
    t3 = para(after=14)
    t3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t3, c['sub'], size=10, color=GREY)
    for n in c.get('notes', []):
        run(para(after=3, indent=8), '· ' + n, size=9.5, color=GREY)

    first_ep = True
    kr_cm = KR_COMMENTS.get(ver, {})
    anchors = {}
    for li, k in enumerate(lines, 1):
        s_ = k.strip()
        if not s_:
            continue
        n_before = len(d.paragraphs)
        _anchor_line = li
        if IS_EP.match(s_):
            if not first_ep or ver in ('v2', 'v3', 'v4'):
                d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            first_ep = False
            h = para(after=3, before=6, keep=True)
            run(h, s_.lstrip('# ').strip(), size=17, bold=True)
            run(para(after=10), '─' * 44, size=8, color=LINE)
        elif IS_SCENE.match(s_):
            run(para(before=15, after=2, keep=True), s_.lstrip('# ').strip(), size=12.5, bold=True, color=ACC)
        elif IS_OUTLINE_EP.match(s_):
            run(para(before=10, after=2, keep=True), s_.lstrip('# ').strip(), size=11.5, bold=True, color=ACC)
        elif s_ in SECTION_HEADS or s_.lstrip('# ').strip() in SECTION_HEADS:
            run(para(before=16, after=6, keep=True), s_.lstrip('# ').strip(), size=14, bold=True)
        elif IS_CAST.match(s_):
            run(para(after=9, keep=True), s_, size=9.5, color=GREY)
        elif s_.startswith('【') and len(s_) < 20:
            run(para(before=6, after=4), s_, size=10, color=GREY, bold=True)
        elif s_.startswith('△'):
            mdline(para(after=5), s_, 10.5, STAGE)
        elif s_.startswith('**'):
            mdline(para(after=7, before=5), s_, 11.5, BLACK)
        else:
            # 인물 설정·개요 산문 / 인물 제목 줄
            is_head = bool(re.match(r'^[가-힣A-Za-z· ]{2,20}\s*[(（][A-Za-z ]+[)）]', s_)) or s_.startswith('**')
            mdline(para(after=4, before=(8 if is_head else 0)), s_, (11.5 if is_head else 10.5),
                   (ACC if is_head else BLACK))
        if kr_cm:
            runs = [r for p_ in d.paragraphs[n_before:] for r in p_.runs if r.text.strip()]
            if runs:
                anchors[_anchor_line] = runs
    for ln, paras in kr_cm.items():
        if ln not in anchors:
            sys.exit(f'말풍선 줄 {ln} 이 본문에 없음')
        cm = d.add_comment([anchors[ln][0], anchors[ln][-1]], text=paras[0], author='검토', initials='검')
        for t_ in paras[1:]:
            cm.add_paragraph(t_)
    out = os.path.join(HERE, c['docx'])
    d.save(out)
    print('OK', out, '/ 줄', len([l for l in lines if l.strip()]), '/ 말풍선', len(kr_cm))


# ---------------------------------------------------------------------------
# 한중 대조본 (윗줄 한국어 · 아랫줄 중국어 원문) + 고칠 곳 Word 코멘트
# 서식 = projects/17_son_of_the_lamp/_build_bilingual.py 승계. 코멘트 키 = 원문 줄 번호(1부터).
# 코멘트 문단 = [문제] / [근거] / [수정] — 근거는 원고 줄·합의 문서로만 댄다.
# ---------------------------------------------------------------------------
RED = RGBColor(0xC0, 0x1E, 0x1E)
LEAK = re.compile(r'(奥蕾莉亚|Aurelia)')

BI = {
    'v3': dict(
        docx=f'{TITLE_KR}_작가 무료회차 최종고(1-9화)_한중 대조본.docx',
        sub='작가 무료회차 최종고 (10.22)  ·  인물 설정 · 1~9화  ·  한중 대조본 (검토용)',
        guide='윗줄 = 한국어 번역(검토용 러프) · 아랫줄 = 중국어 원문(작가 원고 그대로) · 말풍선 = 고쳐야 할 곳',
        notes=[
            '원문의 빨간 글자는 원작 여왕 이름이 그대로 남은 곳이다(32곳). 원문은 손대지 않았고, 번역은 엘레노어로 옮겼다.',
            '泥种은 "천것", 贱人은 "천한 년"으로 옮겼다. 2.0과 원문이 같은 줄은 2.0 번역을 그대로 썼다.',
            '근거로 든 "작가 전달 문서"는 10-14에 작가에게 보낸 「1~8화 검토와 이후 방향」, "미팅록"은 작가와의 화상 미팅 정리다.',
        ],
        # {시작 줄: (끝 줄, [문단, ...])}
        comments={
            30: (30, [
                '[문제] 여왕 이름(빨간 글자)이 원작 여왕 이름 그대로다. 원문 32곳 전부 해당한다.',
                '[근거] 원작 레퍼런스 역대본의 여왕 이름과 같다(이 줄의 영어 표기까지 같음). 작가 전달 문서 첫 항목 "여왕 이름이 원작 여왕 이름과 같습니다. 엘레노어(Eleanor)로 바꿔 주세요."가 반영되지 않았다.',
                '[수정] 원작과 다른 이름으로 32곳 모두 교체(예: 埃莉诺 Eleanor).',
            ]),
            5: (5, [
                '[문제] 인물 설정의 "二十年"이 본문과 다르다(사라 칸 "长达二十年"도 같음).',
                '[근거] 본문 2화 첫 자막 "【字幕：十八年后】", 2화 에드워드 "迎来十八岁的成年礼".',
                '[수정] 二十年 → 十八年.',
            ]),
            14: (14, [
                '[문제] 바네사 칸에 웨슬리(伟斯利)가 "약혼자"로 남아 있다.',
                '[근거] 미팅록 2 "서브 남주(남주 2) 캐릭터 삭제". 본문 1~9화에도 웨슬리는 안 나온다.',
                '[수정] 在察觉到未婚夫伟斯利对艾薇的异常关注后 → 在察觉到大哥爱德华对艾薇的异常关注后',
            ]),
            25: (25, [
                '[문제] 세바스찬 칸에 웨슬리(伟斯利)와 "北部龙族"가 남아 있다.',
                '[근거] 미팅록 2 웨슬리 삭제. 왕실은 남부 용족이다(아이비 칸 "南部龙族真正的未来继承人"). 본문 9화에서 세바스찬이 막아서는 사람은 에드워드다.',
                '[수정] 예: 极其维护王室的颜面与凡妮莎的尊严。在爱德华想替艾薇解围时，他强硬阻拦。',
            ]),
            38: (38, [
                '[문제] "朝着喷出"에 무엇을 향하는지가 빠졌다(오타).',
                '[수정] 朝着喷出 → 朝着莎拉喷出',
            ]),
            71: (71, [
                '[문제] 반지를 가리키는데 "她"를 썼다(오타).',
                '[수정] 谁能拥有她 → 谁能拥有它',
            ]),
            89: (89, ['[문제] "与与" 중복(오타).', '[수정] 阴谋与与暗箭 → 阴谋与暗箭']),
            150: (154, [
                '[문제] 이 플래시백에서 바네사는 자기가 가짜인 걸 이미 알고 사라와 짜고 있다("哥哥们一定会怀疑我的身份" / "只要三位王子认定你是他们的妹妹").',
                '[근거] 합의 설정은 "바네사는 처음엔 자기가 가짜인 줄 모른다"이다(작가 전달 문서 인물 항목 "바네사: 처음엔 자기가 가짜인 줄 몰랐습니다"). 2.0 원고도 4화에서 반지가 빛나자 "龙戒……有反应了？！" 하고 놀라기만 했다.',
                '[수정] 【闪回】부터 【闪回结束】까지 다섯 줄 삭제. 다음 줄 "△凡妮莎猛地回神，脸色苍白地看向爱德华三人。" → "△凡妮莎脸色苍白地看向爱德华三人。"',
            ]),
            158: (158, ['[문제] "哪"는 "那"의 오타.', '[수정] 都是哪该死的叛军 → 都是那该死的叛军']),
            178: (178, [
                '[확인] 씬 헤더는 "王室养龙场/日/外"(실외)인데 흰 용이 "撞破养龙场顶棚"(지붕을 뚫고) 나간다.',
                '[수정] 지붕이 있는 사육장 안이면 헤더를 內로, 실외면 "冲破围栏"처럼 맞춰 주기.',
            ]),
            204: (204, [
                '[문제] 반지가 빛나자 바네사가 "저 애야…… 사육장의 그 노예!"라고 바로 알아본다. 진짜 공주가 사육장에 있다는 걸 미리 안다는 뜻이다.',
                '[근거] 합의 설정 "바네사는 처음엔 자기가 가짜인 줄 모른다"(작가 전달 문서 인물 항목).',
                '[수정] 该死！龙戒共鸣了！是她......是那个养龙场的低贱奴隶！ → 该死！龙戒怎么会对一个奴隶有反应？！',
                '(5화 "我绝不能让人发现龙戒的异样，她今天必须死在这里！"는 의심받을까 봐 죽이려는 걸로 읽혀 그대로 둬도 된다.)',
            ]),
            226: (226, [
                '[확인] 푸른 마법 칼날을 누가 쐈는지 화면에 없다. 바로 뒤에 세 왕자가 등장해 그중 하나로 짐작만 된다.',
                '[수정] 예: 쏜 왕자의 손을 한 컷(△塞巴斯蒂安抬手，一道蓝色魔法光刃……). 누가 쏘느냐가 오빠 셋의 성격 차이를 보여 주는 자리이기도 하다.',
            ]),
            242: (242, ['[문제] "浑奴隶" 어색(오타로 보임).', '[수정] 一个浑奴隶 → 一个低贱的奴隶']),
            273: (273, ['[문제] "脏手" 앞 동사가 빠져 문장이 안 된다.', '[수정] 为了这种低贱的泥种脏手 → 为了这种低贱的泥种弄脏手']),
            277: (277, [
                '[문제] 흰 용이 사라졌다. 5화에서 칼날을 맞고 쓰러진 흰 용이 같은 큰길·같은 시간으로 이어지는 6화에 다시 나오지 않고, 끝 장면에서 아이비가 "홀로" 길 한가운데 서 있다.',
                '[근거] 5화 "白龙发出凄厉哀鸣，身躯轰然倒地" → "艾薇正心疼地抚摸着受伤的白龙". 6화에 흰 용이 떠나는 줄이 없다.',
                '[수정] 艾薇独自站在道路中央，看着远去的车队 → 艾薇守在倒地的白龙身旁，看着远去的车队',
            ]),
            289: (289, [
                '[문제] "娇羞"(수줍게) 때문에 바네사가 에드워드를 연인처럼 보는 장면으로 읽힌다.',
                '[근거] 여기는 에드워드 시선이 아이비에게 가는 걸 바네사가 알아채는 자리다. 가족애 이상의 감정을 품는 오빠는 따로 있다(미팅록 3). 에드워드에게 이 반응을 주면 나중에 그 오빠가 나올 때 헷갈린다.',
                '[수정] 凡妮莎娇羞地看向走在最前方的爱德华 → 凡妮莎甜甜地看向走在最前方的爱德华',
            ]),
            295: (295, [
                '[문제] 바네사의 "오빠!"가 VO(속마음)인데 에드워드가 바로 "미안, 바네사"라고 대답한다. 속마음을 들은 셈이다.',
                '[근거] 이 원고에서 VO = 속마음, OS = 화면 밖 목소리다(아이비·바네사·에드워드 VO 모두 속마음).',
                '[수정] 凡妮莎VO：哥哥！ → 凡妮莎（轻声）：哥哥！',
            ]),
            301: (301, [
                '[문제] ① "引起了大哥的疑心"(큰오빠가 의심하게 만들어)은 숨길 게 있는 사람의 말이라, 바네사가 자기가 가짜인 걸 아는 걸로 읽힌다. ② "爱德华是我的！"는 289줄 "娇羞"와 같이 연인처럼 읽힌다.',
                '[근거] 합의 설정 "바네사는 처음엔 자기가 가짜인 줄 모른다"(작가 전달 문서). 가족애 이상의 감정을 품는 오빠는 따로 있다(미팅록 3).',
                '[수정] 居然还引起了大哥的疑心！ → 居然还勾走了大哥的目光！ / 爱德华是我的！ → 삭제 또는 哥哥们是我的！(바로 뒤 "他们三个人所有的宠爱都只能是我的"가 같은 뜻)',
            ]),
            349: (349, [
                '[문제] 에드워드가 등장하는 줄 없이 현장에 있다.',
                '[근거] 7화 끝 "爱德华收回目光，重新走上高台"(단상으로 돌아감) → 8화 인물 줄에 에드워드 없음 → 9화에서는 세바스찬이 한 걸음 옆으로 나서 막을 만큼 가까이 있다. 2.0에서 이 장면의 웨슬리 줄("大步走来")을 에드워드로 바꾸면서 등장 줄이 빠졌다.',
                '[수정] 이 줄 앞에 △爱德华从高台上快步走来。 추가.',
            ]),
            350: (350, [
                '[문제] 18년을 금이야 옥이야 키운 동생이 시킨 일을, 그날 아침 그 동생 행렬을 습격했다는 노예 때문에 대놓고 막는다. 이유가 "왕실 체면" 하나라 설득력이 약하다. 세바스찬도 "你之前也不这样"이라고 할 만큼 갑작스럽다.',
                '[근거] 2.0에서 이 장면은 바네사와 정이 없는 웨슬리가 했다. 에드워드로 옮기면서 이유를 안 붙였다. 5~7화의 에드워드는 끌림을 스스로 누르거나(6화 "我真是昏了头") 바네사를 위한 말로 둘러댄다(6화 "王者的心，要装得下所有子民"). 9화만 그 선을 넘는다.',
                '[수정] 겉으로 대는 이유를 바네사를 위한 것으로, 진짜 이유는 속마음으로: 够了，多米尼克！今天是凡妮莎的成年礼，满场贵族都看着。你想让全王国说，新女王在自己的庆典上逼人吃垃圾吗？ + 바로 뒤 爱德华VO：……可我为什么，就是看不得她跪在那里？',
            ]),
            352: (352, ['[문제] "这么了"는 "怎么了"의 오타.', '[수정] 到底是这么了？ → 到底是怎么了？']),
            355: (355, [
                '[문제] 바네사가 에드워드의 "熟悉感"(익숙함)을 안다. 이 느낌은 에드워드 속마음에만 나왔다(5화 VO "和母亲年轻时一模一样", 7화 VO "那种牵绊感"). 7화에서 에드워드는 "연회 준비 보고 있었다"고 둘러댔다.',
                '[수정] 就为了那可笑的熟悉感，他连我的委屈都不顾了？！ → 说什么为了我……他从刚才开始，眼睛就一直在那个奴隶身上！ (7화에서 바네사가 에드워드 시선을 본 것과 이어진다. 350줄 수정과 짝.)',
            ]),
        },
    ),
}


def build_bi(ver):
    c, b = CFG[ver], BI[ver]
    cn = open(os.path.join(HERE, c['cn']), encoding='utf-8').read().split('\n')
    kr = open(os.path.join(HERE, c['kr']), encoding='utf-8').read().split('\n')
    while cn and not cn[-1].strip():
        cn.pop()
    while kr and not kr[-1].strip():
        kr.pop()
    if len(cn) != len(kr):
        sys.exit(f'줄 수 불일치: 중문 {len(cn)} / 한국어 {len(kr)}')
    if PATCH_AFTER[ver]:
        sys.exit('대조본은 원문 줄 대응만 쓴다 — PATCH_AFTER 가 있는 판은 따로 처리')

    d = docx.Document()
    s = d.sections[0]
    s.left_margin = s.right_margin = Cm(2.0)
    s.top_margin = s.bottom_margin = Cm(1.8)

    def para(after=0, before=0, keep=False, indent=0):
        p = d.add_paragraph()
        pf = p.paragraph_format
        pf.space_after, pf.space_before, pf.line_spacing, pf.keep_with_next = Pt(after), Pt(before), 1.18, keep
        if indent:
            pf.left_indent = Pt(indent)
        return p

    def run(p, text, *, cnfont=False, size=11, color=BLACK, bold=False):
        r = p.add_run(text)
        name = '微软雅黑' if cnfont else '맑은 고딕'
        r.font.size, r.font.color.rgb, r.bold, r.font.name = Pt(size), color, bold, name
        r._element.rPr.rFonts.set(qn('w:eastAsia'), name)
        return r

    def kr_runs(p, text, size=11, color=BLACK, bold_all=False):
        out = []
        for seg in MD.split(text):
            if seg:
                bb = seg.startswith('**')
                out.append(run(p, seg[2:-2] if bb else seg, size=size, color=(ACC if bb and not bold_all else color),
                               bold=bb or bold_all))
        return out

    def cn_runs(p, text, size=9.5, color=GREY, bold=False):
        out = []
        for seg in LEAK.split(text):
            if seg:
                hit = bool(LEAK.fullmatch(seg))
                out.append(run(p, seg, cnfont=True, size=size, color=(RED if hit else color), bold=(hit or bold)))
        return out

    t = para(after=3)
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t, TITLE_KR, size=19, bold=True)
    t2 = para(after=3)
    t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t2, TITLE_EN, size=11, color=ACC)
    t3 = para(after=3)
    t3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t3, b['sub'], size=10, color=GREY)
    t4 = para(after=14)
    t4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(t4, b['guide'], size=9, color=GREY)
    for n in b['notes']:
        run(para(after=3, indent=8), '· ' + n, size=9.5, color=GREY)

    # 줄 번호(1부터) → 그 줄에서 만든 run 목록
    anchors = {}
    first_ep, n_in_scene = True, 0
    for i, (k, c_) in enumerate(zip(kr, cn), 1):
        ks, cs = k.strip(), c_.strip()
        if not ks:
            continue
        rs = []
        if IS_EP.match(ks):
            d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
            first_ep = False
            h = para(after=3, before=6, keep=True)
            rs += [run(h, ks.lstrip('# ').strip(), size=16, bold=True)]
            rs += cn_runs(h, '   ' + cs, size=11)
            run(para(after=10), '─' * 44, size=8, color=LINE)
            n_in_scene = 0
        elif IS_SCENE.match(ks):
            h = para(before=14, after=1, keep=True)
            rs += [run(h, ks.lstrip('# ').strip(), size=12.5, bold=True, color=ACC)]
            rs += cn_runs(para(after=6, keep=True), cs, size=10)
            n_in_scene = 0
        elif IS_CAST.match(ks):
            p = para(after=1, keep=True)
            rs += [run(p, ks, size=9.5, color=GREY)]
            rs += cn_runs(para(after=9, keep=True), cs, size=9)
        elif first_ep and (ks in SECTION_HEADS or ks.lstrip('# ').strip() in SECTION_HEADS):
            h = para(before=14, after=6, keep=True)
            rs += [run(h, ks.lstrip('# ').strip(), size=14, bold=True)]
            rs += cn_runs(h, '   ' + cs, size=10)
        elif first_ep and ks.startswith('【'):
            h = para(before=8, after=4, keep=True)
            rs += [run(h, ks, size=10, color=GREY, bold=True)]
            rs += cn_runs(h, '   ' + cs, size=9.5)
        elif first_ep and re.match(r'^[가-힣A-Za-z· ]{2,20}\s*[(（][A-Za-z ]+[)）]', ks):
            h = para(before=10, after=1, keep=True)
            rs += kr_runs(h, ks, size=11.5, color=ACC, bold_all=True)
            rs += cn_runs(para(after=6, keep=True), cs, size=10)
        elif first_ep:
            p = para(after=1, keep=True)
            rs += kr_runs(p, ks, size=10.5)
            rs += cn_runs(para(after=7), cs)
        elif ks.startswith('【') and len(ks) < 20:
            p = para(before=6, after=1, keep=True)
            rs += [run(p, ks, size=10, color=GREY, bold=True)]
            rs += cn_runs(para(after=6), cs, size=9.5, bold=True)
        else:
            n_in_scene += 1
            p = para(after=1, keep=True)
            run(p, '%02d  ' % n_in_scene, size=8, color=IDX)
            rs += kr_runs(p, ks, size=(10.5 if ks.startswith('△') else 11), color=(STAGE if ks.startswith('△') else BLACK))
            rs += cn_runs(para(after=9, indent=20), cs)
        anchors[i] = rs

    for start, (end, paras) in b['comments'].items():
        if start not in anchors or end not in anchors:
            sys.exit(f'코멘트 줄 {start}-{end} 이 본문에 없음')
        cm = d.add_comment([anchors[start][0], anchors[end][-1]], text=paras[0], author='검토', initials='검')
        for t_ in paras[1:]:
            cm.add_paragraph(t_)

    out = os.path.join(HERE, b['docx'])
    d.save(out)
    print('OK', out, '/ 줄', len(anchors), '/ 코멘트', len(b['comments']))


IDX = RGBColor(0xB0, 0xB0, 0xB0)

if __name__ == '__main__':
    for v in (sys.argv[1:] or ['v1', 'v2']):
        if v.startswith('bi:'):
            build_bi(v[3:])
        else:
            build(v)
