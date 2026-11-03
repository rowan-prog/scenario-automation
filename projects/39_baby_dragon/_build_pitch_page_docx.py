# -*- coding: utf-8 -*-
"""39 피칭덱(61 양식) md → docx, 광고 핵심 장면 캡처 이미지를 문서 안에 넣음.
서식 = tools/build_pitch_page.py 의 Doc 그대로(45 빌더와 같은 규칙).
사용: py -3 _build_pitch_page_docx.py
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', 'tools')))
from build_pitch_page import Doc, BLACK, GREY, ACC  # noqa: E402
from docx.shared import Cm  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402

MD = os.path.join(HERE, '39_baby_dragon_02_pitch_page.md')
OUT = os.path.join(HERE, "The Vampire King's Human Nanny_피칭덱_v2.docx")
SECTIONS = ['타이틀', '담당 CM', '기본 정보', '해당 IP 피칭 사유 (Core Expectation)',
            '주요 인물 소개', '줄거리', '트리트먼트 (1화~Paywall 화)']
CHAR_HEAD = re.compile(r'^\S+(?: \S+)? \((남|여)(?:\s*/\s*[^)]*)?\)\s*·\s*.+$')
EP_HEAD = re.compile(r'^EP\s?\d{1,2}$')
IMG_LINE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)$')
PLACEHOLDER = re.compile(r'^-?\s*\[(키아트|스크린샷|첨부)[^\]]*\]$')
BLOCK = re.compile(r'^\[[^\]]+\]$')
BOLD_LEAD = re.compile(r'^(레퍼런스 광고 \d+|무료 회차: .+|무료 회차 이후|[①②] .+|시그니처 소품|.+ \(\d+화 · \d+화\)|.+ \((유료 구간|\d+화)\)( ★★)?)$')


def picture(doc, path, caption, height=Cm(9.0)):
    assert os.path.exists(path), path
    p = doc.para(space_before=4, space_after=1)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, height=height)
    c = doc.para(space_after=8)
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.run(c, caption, size=9, color=GREY)


def main():
    lines = open(MD, encoding='utf-8').read().splitlines()
    assert '**' not in '\n'.join(lines), 'md 안에 ** 있음'
    doc = Doc(); section = None; n_img = 0
    for i, raw in enumerate(lines):
        t = raw.rstrip(); s = t.strip()
        if not s:
            continue
        nxt = next((x.strip() for x in lines[i + 1:] if x.strip()), '')
        if i == 0:
            p = doc.para(space_after=10); doc.run(p, s, size=16, bold=True, color=BLACK); continue
        if s in SECTIONS:
            section = s; doc.section(s); continue
        m = IMG_LINE.match(s)
        if m:
            picture(doc, os.path.join(HERE, m.group(2)), m.group(1)); n_img += 1; continue
        if PLACEHOLDER.match(s):
            doc.body(s.lstrip('- '), color=GREY, size=10); continue
        if BLOCK.match(s):
            doc.subhead(s); continue
        if section == '주요 인물 소개' and CHAR_HEAD.match(s):
            p = doc.para(space_before=12, space_after=3, keep=True)
            doc.run(p, s, size=11.5, bold=True, color=ACC); continue
        if section and section.startswith('트리트먼트') and EP_HEAD.match(s):
            p = doc.para(space_before=10, space_after=3, keep=True)
            doc.run(p, s, size=11, bold=True, color=ACC); continue
        if section == '해당 IP 피칭 사유 (Core Expectation)':
            if BOLD_LEAD.match(s) or nxt.startswith('레퍼런스:'):
                p = doc.para(space_before=6, space_after=2, keep=True)
                doc.run(p, s, size=11, bold=True, color=BLACK); continue
        if s.startswith('엔딩 훅'):
            p = doc.para(space_after=6)
            doc.run(p, '엔딩 훅 ', bold=True, color=ACC)
            doc.run(p, s[len('엔딩 훅'):].lstrip(' :')); continue
        indent = 10 if s.startswith('- ') else (18 if t.startswith('  ') else 0)
        doc.body(s, indent=indent, space_after=4)
    doc.save(OUT)
    print('saved', OUT); print('images', n_img)


if __name__ == '__main__':
    main()
