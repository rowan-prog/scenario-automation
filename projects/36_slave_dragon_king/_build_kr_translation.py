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
}

# 메인 워싱 — {원문 줄 번호(1부터): [그 줄 뒤에 덧붙일 한국어 줄, ...]}
PATCH_AFTER = {
    'v1': {},
    'v2': {
        # (2026-10-14 철회) 002-1 끝 "짐승 용이 쇠사슬을 물어 끊는다" 1줄 추가 — 사용자: 짐승 용이 낑낑대며 엎드리고
        # 씬·에피가 바뀌면 시청자가 바로 메우는 논리라 불필요, 호흡만 끊음 → 작가 원고 그대로.
    },
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
        f.write(f'# 《{TITLE_KR}》 {c["sub"]}\n\n원본 = `{c["src"]}`\n\n---\n\n')
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

    first_ep = True
    for k in lines:
        s_ = k.strip()
        if not s_:
            continue
        if IS_EP.match(s_):
            if not first_ep or ver == 'v2':
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
    out = os.path.join(HERE, c['docx'])
    d.save(out)
    print('OK', out, '/ 줄', len([l for l in lines if l.strip()]))


if __name__ == '__main__':
    for v in (sys.argv[1:] or ['v1', 'v2']):
        build(v)
