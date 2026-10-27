# -*- coding: utf-8 -*-
"""검토 보고서 md → docx (맑은 고딕). 지원: # / ## / ### 제목, 문단, '- ' 목록, '| ' 표, **굵게**.

사용: py -3 _build_review_docx.py <보고서.md> <보고서.docx>
"""
import re
import sys

import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BLACK = RGBColor(0x1A, 0x1A, 0x1A)
ACC = RGBColor(0x8A, 0x5A, 0x10)
GREY = RGBColor(0x60, 0x60, 0x60)
BOLD = re.compile(r'(\*\*[^*]+\*\*)')
FONT = '맑은 고딕'


def set_font(r, size, color=BLACK, bold=False):
    r.font.size, r.font.color.rgb, r.bold, r.font.name = Pt(size), color, bold, FONT
    r._element.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), FONT)


def runs(p, text, size=10.5, color=BLACK, bold_all=False):
    for seg in BOLD.split(text):
        if not seg:
            continue
        b = seg.startswith('**') and seg.endswith('**')
        set_font(p.add_run(seg[2:-2] if b else seg), size, color, bold_all or b)


def shade(cell, hex_):
    tcPr = cell._element.get_or_add_tcPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear')
    sh.set(qn('w:color'), 'auto')
    sh.set(qn('w:fill'), hex_)
    tcPr.append(sh)


def build(md, out):
    lines = open(md, encoding='utf-8').read().split('\n')
    d = docx.Document()
    s = d.sections[0]
    s.left_margin = s.right_margin = Cm(2.2)
    s.top_margin = s.bottom_margin = Cm(1.9)

    def para(before=0, after=4, indent=0):
        p = d.add_paragraph()
        pf = p.paragraph_format
        pf.space_before, pf.space_after, pf.line_spacing = Pt(before), Pt(after), 1.3
        if indent:
            pf.left_indent = Pt(indent)
        return p

    i = 0
    first_h1 = True
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'-+', c) for c in cells):
                    rows.append(cells)
                i += 1
            t = d.add_table(rows=len(rows), cols=len(rows[0]))
            t.style = 'Table Grid'
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for r_i, row in enumerate(rows):
                for c_i, val in enumerate(row):
                    cell = t.cell(r_i, c_i)
                    cell.paragraphs[0].paragraph_format.space_after = Pt(1)
                    runs(cell.paragraphs[0], val, size=9.5, bold_all=(r_i == 0))
                    if r_i == 0:
                        shade(cell, 'EFE6D2')
            para(after=4)
            continue
        if ln.startswith('# '):
            p = para(before=(0 if first_h1 else 16), after=6)
            runs(p, ln[2:], size=(16 if first_h1 else 14.5), bold_all=True)
            first_h1 = False
        elif ln.startswith('## '):
            runs(para(before=14, after=4), ln[3:], size=12.5, color=ACC, bold_all=True)
        elif ln.startswith('### '):
            runs(para(before=10, after=3), ln[4:], size=11, bold_all=True)
        elif ln.startswith('- '):
            p = para(after=3, indent=12)
            p.paragraph_format.first_line_indent = Pt(-9)
            runs(p, '· ' + ln[2:], size=10.5)
        elif re.match(r'^\d+\. ', ln):
            p = para(after=3, indent=12)
            p.paragraph_format.first_line_indent = Pt(-12)
            runs(p, ln, size=10.5)
        else:
            runs(para(after=5), ln, size=10.5)
        i += 1
    d.save(out)
    print('OK', out)


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
