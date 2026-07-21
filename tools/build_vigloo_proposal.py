# -*- coding: utf-8 -*-
"""Vigloo(플랫폼) 기획안 docx 빌더 — spec 텍스트 → 템플릿 구조 docx (phase_p)

사용: python tools/build_vigloo_proposal.py <spec.txt> <out.docx>

spec 형식 (UTF-8):
  #DOCTITLE <문서 최상단 타이틀>            (선택, 1회)
  #SECTION <섹션 헤더>                      (2열 병합·회색 음영·볼드. '|' = 셀 내 줄바꿈)
  #ROW <좌측 레이블>                        ('|' = 줄바꿈)
  <우측 내용 줄들...>                        (다음 #ROW/#SECTION 전까지 전부 내용)

예:
  #DOCTITLE Vigloo AI Drama Proposal_MY TITLE
  #SECTION 프로젝트 기본 정보    项目基本信息
  #ROW 타이틀|标题 (Title)
  한국어 / 韩语: ...
  영어 / 英语: ...
  중국어 / 中文: ...
  #ROW 담당자|负责人
  Rowan
"""
import sys
from docx import Document
from docx.shared import Pt, Cm
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def build(spec_path, out_path):
    lines = open(spec_path, encoding='utf-8').read().split('\n')
    title = None
    items = []  # ['section', text] | ['row', label, [content lines]]
    cur = None
    for ln in lines:
        if ln.startswith('#DOCTITLE '):
            title = ln[len('#DOCTITLE '):].strip()
            cur = None
        elif ln.startswith('#SECTION '):
            items.append(['section', ln[len('#SECTION '):].strip()])
            cur = None
        elif ln.startswith('#ROW '):
            cur = ['row', ln[len('#ROW '):].strip(), []]
            items.append(cur)
        elif cur is not None:
            cur[2].append(ln)

    doc = Document()
    st = doc.styles['Normal']
    st.font.name = 'Malgun Gothic'
    st.font.size = Pt(10)
    rpr = st.element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    rf.set(qn('w:eastAsia'), 'Malgun Gothic')

    if title:
        tp = doc.add_paragraph()
        tr = tp.add_run(title)
        tr.bold = True
        tr.font.size = Pt(14)

    table = doc.add_table(rows=0, cols=2)
    table.style = 'Table Grid'
    table.autofit = False

    def shade(cell, color='D9D9D9'):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:fill'), color)
        tcPr.append(shd)

    def set_text(cell, text, bold=False):
        cell.text = ''
        first = True
        for line in text.split('\n'):
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            r = p.add_run(line)
            r.bold = bold

    for it in items:
        if it[0] == 'section':
            row = table.add_row()
            c = row.cells[0].merge(row.cells[1])
            set_text(c, it[1].replace('|', '\n'), bold=True)
            shade(c)
        else:
            content = '\n'.join(it[2]).strip('\n')
            row = table.add_row()
            row.cells[0].width = Cm(4)
            row.cells[1].width = Cm(12.5)
            set_text(row.cells[0], it[1].replace('|', '\n'), bold=True)
            set_text(row.cells[1], content)

    doc.save(out_path)
    print('SAVED rows=%d -> %s' % (len(table.rows), out_path))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    build(sys.argv[1], sys.argv[2])
