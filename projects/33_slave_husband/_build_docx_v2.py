# -*- coding: utf-8 -*-
"""v2 T1 페이지 + 대본 전체 피드백 -> docx 2종 (작가 발송용)"""
import re
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

def build(src, out):
    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "맑은 고딕"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "맑은 고딕")
    def add(text, bold=False, size=None, space=4):
        p = doc.add_paragraph(); r = p.add_run(text); r.bold = bold
        if size: r.font.size = Pt(size)
        p.paragraph_format.space_after = Pt(space); return p
    for raw in open(src, encoding="utf-8").read().splitlines():
        line = raw.rstrip()
        if not line.strip(): continue
        if line.startswith("# "):  add(line[2:].strip(), bold=True, size=16, space=10); continue
        if line.startswith("## "): add(line[3:].strip(), bold=True, size=13, space=8); continue
        if line.startswith("### "):add(line[4:].strip(), bold=True, size=16, space=10); continue
        if re.match(r"^EP\d+$", line.strip()): add(line.strip(), bold=True, size=11, space=2); continue
        m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", line)
        if m:
            p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4)
            r = p.add_run(m.group(1)); r.bold = True
            if m.group(2): p.add_run("  " + re.sub(r"\*\*(.+?)\*\*", r"\1", m.group(2)))
            continue
        add(re.sub(r"\*\*(.+?)\*\*", r"\1", line.strip()))
    doc.save(out); print("saved", out)

build("33_slave_husband_p0_rough_v3.md", "밤마다 나를 탐하는 노예 남편_로그라인·무료회차 트리트먼트_v3.docx")
build("33_slave_husband_writer_feedback_v1.md", "밤마다 나를 탐하는 노예 남편_대본 전체 피드백_v1.docx")
