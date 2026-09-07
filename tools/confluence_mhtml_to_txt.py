#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""confluence_mhtml_to_txt.py — Confluence「Word로 내보내기」(.doc = MHTML) → 코퍼스용 txt.

사내 「신규 작품 제작 결정 미팅」 문서를 Confluence에서 .doc로 내보내면 실체는 MIME multipart(HTML 1파트 + 이미지)다.
이 스크립트는 그 HTML 파트를 꺼내 표·불릿·헤더를 남긴 평문으로 바꾼다. 출력 형식은
config/pitch_page_corpus/deck_2026-08-*.txt 와 같다(엔트리 헤더 `N. 제목` + `[TABLE]`…`[/TABLE]` · 셀 구분 ` | ` · 불릿 `- `).
tools/pitch_page_lint.py --stats 의 ENTRY_RE 가 그 형식을 읽는다.

사용:
  python tools/confluence_mhtml_to_txt.py "<내보낸 .doc>" config/pitch_page_corpus/deck_YYYY-MM-DD.txt
  (두 번째 인자를 생략하면 같은 이름 .txt 를 입력 파일 옆에 쓴다)

주의: 이미지 안 글자는 못 꺼낸다 — `[IMG 파일명]` 자리표시만 남긴다. 표 안 텍스트박스는 Confluence HTML엔 그대로 있어
docx 변환과 달리 유실되지 않는다(메모리 [[docx-conversion-drops-table-textbox-text]]는 docx 얘기).
"""
import email
import re
import sys
from email import policy
from html.parser import HTMLParser


class _P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.buf = []
        self.skip = 0
        self.list_depth = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.buf.append("\n\n")
        elif tag in ("p", "div", "tr", "br"):
            self.buf.append("\n")
        elif tag in ("td", "th"):
            self.buf.append(" | ")
        elif tag == "li":
            self.buf.append("\n" + "  " * (self.list_depth - 1) + "- ")
        elif tag in ("ul", "ol"):
            self.list_depth += 1
        elif tag == "table":
            self.buf.append("\n[TABLE]\n")
        elif tag == "img":
            self.buf.append(f"[IMG {d.get('alt', '') or d.get('src', '')[:40]}]")
        elif tag == "a" and d.get("href"):
            self.buf.append(f"[A href={d['href']}]")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag in ("ul", "ol"):
            self.list_depth -= 1
        if tag == "table":
            self.buf.append("\n[/TABLE]\n")
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.buf.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


def convert(src_path):
    with open(src_path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)
    html_parts = [p.get_content() for p in msg.walk() if p.get_content_type() == "text/html"]
    if not html_parts:
        raise SystemExit("text/html 파트가 없다 — Confluence .doc(MHTML) 내보내기 파일이 맞나?")
    p = _P()
    p.feed(html_parts[0])
    txt = "".join(p.buf)
    txt = re.sub(r"[ \t\u00a0]+", " ", txt)
    txt = re.sub(r"^\s+-\s*$", "- ", txt, flags=re.M)      # 빈 불릿 마커 줄 통일
    txt = re.sub(r"\n\s*\n\s*\n+", "\n\n", txt)
    return txt


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"\.doc$", "", src) + ".txt"
    txt = convert(src)
    with open(out, "w", encoding="utf-8") as f:
        f.write(txt)
    n_entries = len(re.findall(r"(?:^|\n)\d+\.\s*.+?\s*\n+\[TABLE\]", txt))
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"{out}  —  {len(txt)}자 · 엔트리 {n_entries}개")


if __name__ == "__main__":
    main()
