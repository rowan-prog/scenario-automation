# -*- coding: utf-8 -*-
"""원작 정식 대본(한국어 md) → 하우스 양식 docx (한 언어).
  py -3 -X utf8 tools/formal_kr_to_house_docx.py <정식대본_KR.md> <out.docx>
md 양식 = `## EP1 - S#1  밤 / 안 / 장소 · 덧붙임` · `등장인물:` · `△ 지문` · `이름: 대사` · `이름 VO:` · `이름(OS):` · `자막:` · `△ 시스템 패널 — 「…」`
docx = 화 제목 `N화` · 씬 헤더 `S#N-n. 장소 / 실내 / 밤` · `인물:` · 지문(△ 뺌) · 대사 `이름: (지시) 대사` 파랑 굵게 · 속마음 `이름 (속마음):` · 화면 밖 `이름 (소리):` · 자막·상태창 = 표시 줄(파랑 굵게)
검사: 화 번호 1부터 빈틈 없이 · 씬 번호 화마다 1부터.
"""
import io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from house_script_docx import build  # noqa: E402

SC = re.compile(r'^## EP(\d+) - S#(\d+)\s+(.*)$')
DLG = re.compile(r'^([^\s:△>#][^:]{0,30}?)\s*(VO|\(OS\))?\s*:\s*(.*)$')
INOUT = {'안': '실내', '밖': '실외', '안·밖': '실내·실외', '밖·안': '실외·실내'}


def scene_head(ep, n, rest):
    parts = [p.strip() for p in rest.split('/')]
    if len(parts) >= 3:
        time, io_, place = parts[0], parts[1], ' / '.join(parts[2:])
        return 'S#%d-%d. %s / %s / %s' % (ep, n, place, INOUT.get(io_, io_), time)
    return 'S#%d-%d. %s' % (ep, n, rest)


def convert(md):
    items, errs = [], []
    title = None
    ep_prev, sc_prev = 0, 0
    for raw in io.open(md, encoding='utf-8').read().split('\n'):
        s = raw.strip()
        if not s:
            continue
        if s.startswith('# '):
            title = s[2:]
            continue
        if s.startswith('>'):
            items.append(('text', s.lstrip('> '), ''))
            continue
        m = SC.match(s)
        if m:
            ep, n = int(m.group(1)), int(m.group(2))
            if ep != ep_prev:
                if ep != ep_prev + 1:
                    errs.append('화 번호 %d 다음에 %d' % (ep_prev, ep))
                items.append(('ep', '%d화' % ep, ''))
                ep_prev, sc_prev = ep, 0
            if n != sc_prev + 1:
                errs.append('%d화 씬 %d 다음에 %d' % (ep, sc_prev, n))
            sc_prev = n
            items.append(('scene', scene_head(ep, n, m.group(3)), ''))
            continue
        if s.startswith('등장인물:'):
            items.append(('cast', '인물:' + s[len('등장인물:'):], ''))
            continue
        if s.startswith('자막:'):
            items.append(('mark', '[자막] ' + s[3:].strip(), ''))
            continue
        if s.startswith('△'):
            body = s.lstrip('△').strip()
            pm = re.match(r'^시스템 패널\s*[—–-]\s*(.*)$', body)
            if pm:
                items.append(('mark', '[상태창] ' + pm.group(1).strip().strip('「」'), ''))
            else:
                items.append(('action', body, ''))
            continue
        d = DLG.match(s)
        if d:
            name, tag, line = d.group(1).strip(), d.group(2), d.group(3).strip()
            if tag == 'VO':
                name += ' (속마음)'
            elif tag == '(OS)':
                name += ' (소리)'
            items.append(('dlg', '%s: %s' % (name, line), ''))
            continue
        items.append(('action', s, ''))
    return title, items, errs


def main():
    md, out = sys.argv[1], sys.argv[2]
    title, items, errs = convert(md)
    for e in errs:
        print('✗', e)
    if errs:
        return 1
    build(items, out, title=title)
    print('화 %d · 씬 %d · 요소 %d → %s' % (sum(k == 'ep' for k, _, _ in items),
                                        sum(k == 'scene' for k, _, _ in items), len(items), out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
