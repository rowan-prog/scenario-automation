# -*- coding: utf-8 -*-
"""45 피칭덱(61 양식) md → docx + 캐릭터 디자인 이미지.

서식 상수·헬퍼 = tools/build_pitch_page.py 의 Doc 그대로(새 서식 발명 안 함).
이미지 = images/*_doc.jpg (각 히로인 그림 = 왼쪽 하객 눈 / 오른쪽 라이언 눈).
사용: py -3 _build_pitch_page_docx.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, os.path.abspath(TOOLS))
from build_pitch_page import Doc, BLACK, GREY, ACC  # noqa: E402
from docx.shared import Cm, Pt  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402

MD = os.path.join(HERE, '45_horror_game_hottie_02_pitch_page.md')
OUT = os.path.join(HERE, 'Kiss the Monster Bride or Die_피칭덱.docx')
IMG = os.path.join(HERE, 'images')

SECTIONS = ['타이틀', '담당 CM', '기본 정보', '해당 IP 피칭 사유 (Core Expectation)',
            '주요 인물 소개', '줄거리', '트리트먼트 (1화~Paywall 화)']

HALF = ' — 왼쪽 하객 눈 / 오른쪽 라이언 눈'
CHAR_IMAGES = {
    '라이언': [('00_ryan_character_sheet_doc.jpg', '라이언 캐릭터 시트')],
    '아이비': [('01_ivy_wedding_chapel_doc.jpg', '아이비 · 본식 웨딩드레스 (무료 1~8화)' + HALF),
              ('02_ivy_reception_roulette_doc.jpg', '아이비 · 피로연 검은 코르셋 드레스 (유료 룰렛 시험)' + HALF)],
    '매디슨': [('07_madison_ring_girl_doc.jpg', '매디슨 · 링걸 (유료 격투장)' + HALF),
              ('08_madison_lifeguard_pool_doc.jpg', '매디슨 · 라이프가드 (유료 수영장)' + HALF)],
    '몰리': [('03_zombie_maid_dinner_doc.jpg', '몰리 · 메이드복 (1화 만찬)' + HALF),
            ('04_zombie_nurse_infirmary_doc.jpg', '몰리 · 간호사복 (유료 의무실)' + HALF)],
    '루비': [('05_wolf_cat_waitress_dinner_doc.jpg', '루비 · 고양이 귀 웨이트리스 (1~2화 만찬)' + HALF),
            ('06_wolf_bunny_bouquet_doc.jpg', '루비 · 바니걸 (유료 구간)' + HALF)],
}
GROUP = [('09_group_guests_view_doc.jpg', '히로인 넷 · 하객 눈'),
         ('10_group_ryan_view_doc.jpg', '히로인 넷 · 라이언 눈 (같은 순간 · 같은 옷 · 같은 포즈)')]

CHAR_HEAD = re.compile(r'^(\S+(?: \S+)?) \((남|여)\s*/\s*[^)]*\)\s*·\s*.+$')
EP_HEAD = re.compile(r'^EP\s?\d{1,2}$')
AD_CAP = re.compile(r'^\[스크린샷: 광고 (\d) · (.+)\]$')
SHOT_TABLE = re.compile(r'^\[스크린샷 표: (.+) \| (.+)\]$')
# 랭킹 스크린샷 = DataEye 위챗 기사 원본 차트(상단 크롭). 칸 = (파일, 캡션). 날짜 = 발표일 · 집계일은 차트 统计时间 그대로.
SHOT_CELLS = {
    '10/9 기준': [('rank_1009_drama.jpg', 'DataEye 해외 숏드라마 일간 · 10/9 발표(집계 10/8) · 1위'),
                ('rank_1009_ai.jpg', 'DataEye 해외 AI 드라마 일간 · 10/9 발표(집계 10/8) · 1위')],
    '10/13 기준': [('rank_1013_ai.jpg', 'DataEye 해외 AI 드라마 일간 · 10/13 발표(집계 10/12) · 1위 · Top 6 중 4편(1·3·5·6위)이 이 작품(원판 + 다른 언어 판 3편)')],
}
ATTACH = re.compile(r'^\[첨부: [^\]]+\.mp4\]$')
IMAGE_SLOT = re.compile(r'^\[(키아트|스크린샷|이미지|캡처)')
BLOCK = re.compile(r'^\[[^\]]+\]$')
BOLD_LEAD = re.compile(r'^(레퍼런스 광고 \d+|무료 회차: .+|무료 회차 이후|[①②] .+)$')


def picture(doc, fname, caption, width=None, height=None):
    path = os.path.join(IMG, fname)
    assert os.path.exists(path), path
    p = doc.para(space_before=4, space_after=1)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    if height:
        r.add_picture(path, height=height)
    else:
        r.add_picture(path, width=width or Cm(15.5))
    c = doc.para(space_after=8)
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.run(c, caption, size=9, color=GREY)


def shot_table(doc, heads):
    """[스크린샷 표: A | B] → 2칸 표. 칸마다 날짜 머리 + 원본 차트 이미지 + 캡션."""
    t = doc.d.add_table(rows=2, cols=len(heads))
    t.style = 'Table Grid'
    n = 0
    for j, h in enumerate(heads):
        assert h in SHOT_CELLS, ('스크린샷 표 칸에 넣을 이미지 없음', h)
        hc = t.cell(0, j)
        hp = hc.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.run(hp, h, size=10, bold=True, color=BLACK)
        hp.paragraph_format.keep_with_next = True
        cell = t.cell(1, j)
        first = True
        for fname, cap in SHOT_CELLS[h]:
            path = os.path.join(IMG, fname)
            assert os.path.exists(path), path
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(path, width=Cm(7.6))
            cp = cell.add_paragraph()
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            doc.run(cp, cap, size=8.5, color=GREY)
            n += 1
    # 표가 쪽 사이에서 잘리지 않게(이미지 칸이 두 쪽에 걸쳐 반쪽만 보이는 것 방지)
    for row in t.rows:
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement('w:cantSplit'))
    doc.para(space_after=6)
    return n


def main():
    lines = open(MD, encoding='utf-8').read().splitlines()
    assert '**' not in '\n'.join(lines), 'md 안에 ** 있음'
    doc = Doc()
    section = None
    used = set()
    group_done = False
    n_img = 0
    for i, raw in enumerate(lines):
        t = raw.rstrip()
        s = t.strip()
        if not s:
            continue
        nxt = next((x.strip() for x in lines[i + 1:] if x.strip()), '')
        if i == 0 or (section is None and re.match(r'^N\. \[S급 AI\]', s)):
            p = doc.para(space_after=10)
            doc.run(p, s, size=16, bold=True, color=BLACK)
            continue
        if s in SECTIONS:
            section = s
            doc.section(s)
            if s == '주요 인물 소개' and not group_done:
                for f, cap in GROUP:
                    picture(doc, f, cap)
                    n_img += 1
                group_done = True
            continue
        m = AD_CAP.match(s)
        if m:
            picture(doc, 'ref_ad%s_capture.jpg' % m.group(1), '레퍼런스 광고 %s · %s' % m.groups(), height=Cm(9.0))
            n_img += 1
            continue
        m = SHOT_TABLE.match(s)
        if m:
            n_img += shot_table(doc, [m.group(1).strip(), m.group(2).strip()])
            continue
        # 이미지 자리가 글자로 남으면 안 됨(사용자 2026-11-03) — 못 채운 자리는 빌드 실패
        assert not IMAGE_SLOT.match(s), ('이미지 없이 자리 표시만 남음', i + 1, s)
        if ATTACH.match(s):
            doc.body(s, color=GREY, size=10)
            continue
        if BLOCK.match(s):
            doc.subhead(s)
            continue
        if section == '주요 인물 소개':
            m = CHAR_HEAD.match(s)
            if m:
                p = doc.para(space_before=12, space_after=3, keep=True)
                doc.run(p, s, size=11.5, bold=True, color=ACC)
                key = next((k for k in CHAR_IMAGES if s.startswith(k)), None)
                if key and key not in used:
                    for f, cap in CHAR_IMAGES[key]:
                        if f.startswith('00_'):
                            picture(doc, f, cap, height=Cm(11.0))
                        else:
                            picture(doc, f, cap)
                        n_img += 1
                    used.add(key)
                continue
        if section and section.startswith('트리트먼트') and EP_HEAD.match(s):
            p = doc.para(space_before=10, space_after=3, keep=True)
            doc.run(p, s, size=11, bold=True, color=ACC)
            continue
        if section == '해당 IP 피칭 사유 (Core Expectation)':
            if BOLD_LEAD.match(s) or nxt.startswith('레퍼런스:') or s.endswith('★★'):
                p = doc.para(space_before=6, space_after=2, keep=True)
                doc.run(p, s, size=11, bold=True, color=BLACK)
                continue
        if s.startswith('엔딩 훅'):
            p = doc.para(space_after=6)
            doc.run(p, '엔딩 훅 ', bold=True, color=ACC)
            doc.run(p, s[len('엔딩 훅'):].lstrip(' :'))
            continue
        indent = 0
        if s.startswith('- '):
            indent = 10
        elif t.startswith('  '):
            indent = 18
        doc.body(s, indent=indent, space_after=4)
    missing = [k for k in CHAR_IMAGES if k not in used]
    doc.save(OUT)
    print('saved', OUT)
    print('images', n_img, 'missing chars', missing)


if __name__ == '__main__':
    main()
