# -*- coding: utf-8 -*-
"""46 B 이집트 각색 대본: 05_episodes 4개 md → 합본 md + 하우스 양식 docx (영어 줄 밑 한국어 줄).
  py -3 -X utf8 _build_B_script.py [--check-only]
요소 = 영어 줄 1 + 한국어 줄 1, 요소 사이 빈 줄 1. 종류는 영어 줄 모양으로 가른다.
검사: 요소 줄 수 · 영어 줄 한글 0 · 한국어 줄 한글 있음 · 영어 지문 대명사 · 화 번호 1~30 · 씬 번호 · 페이월 표기.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
EP_DIR = os.path.join(HERE, '05_episodes')
PARTS = ['EP01-10', 'EP11-18', 'EP19-25', 'EP26-30']
TITLE = 'Get Three Wives With System Power in Ancient Egypt'
OUT_DIR = os.path.join(HERE, '07_final')
OUT_MD = os.path.join(OUT_DIR, TITLE + '_FINAL_v1_EN&KO.md')
OUT_DOCX = os.path.join(OUT_DIR, TITLE + '_FINAL_v1_EN&KO.docx')

HANGUL = re.compile(r'[가-힣]')
EP_RE = re.compile(r'^EP\.(\d{2})( \(PAYWALL\))?$')
KR_EP_RE = re.compile(r'^(\d{1,2})화( \(페이월\))?$')
SC_RE = re.compile(r'^S#(\d{1,2})-(\d{1,2})\. ')
DLG_RE = re.compile(r"^[A-Z][A-Z0-9 .'’&\-]*( \((?:V\.O\.|O\.S\.)\))?: ")
MARK_RE = re.compile(r'^(\[[A-Z ]+\]|\(SFX\)|FLASH TO WHITE|CUT TO|SMASH CUT|FADE (IN|OUT)|BACK TO)')
PRON = re.compile(r"\b(he|she|they|him|them|her|his|their|hers|theirs|himself|herself|themselves)\b", re.I)


def kind_of(en):
    if EP_RE.match(en):
        return 'ep'
    if SC_RE.match(en):
        return 'scene'
    if en.startswith('Cast:'):
        return 'cast'
    if MARK_RE.match(en):
        return 'mark'
    if DLG_RE.match(en):
        return 'dlg'
    return 'action'


def load():
    items, errs = [], []
    for part in PARTS:
        p = os.path.join(EP_DIR, '46_viking_three_wives_B_%s.md' % part)
        if not os.path.exists(p):
            errs.append('없음: ' + p)
            continue
        text = io.open(p, encoding='utf-8').read().replace('\r\n', '\n').strip('\n')
        for bi, block in enumerate(re.split(r'\n\s*\n', text)):
            lines = [l.rstrip() for l in block.split('\n') if l.strip()]
            if len(lines) != 2:
                errs.append('%s 블록 %d: %d줄 → %r' % (part, bi + 1, len(lines), lines[:3]))
                continue
            en, kr = lines
            items.append((kind_of(en), en, kr, part))
    return items, errs


def check(items):
    errs, warns = [], []
    ep, sc, eps = 0, 0, []
    for i, (k, en, kr, part) in enumerate(items):
        if HANGUL.search(en):
            errs.append('영어 줄에 한글: ' + en[:80])
        if k not in ('ep', 'scene') and not HANGUL.search(kr):
            warns.append('한국어 줄에 한글 없음: %s | %s' % (en[:50], kr[:50]))
        if k == 'ep':
            m, mk = EP_RE.match(en), KR_EP_RE.match(kr)
            n = int(m.group(1))
            if not mk or int(mk.group(1)) != n:
                errs.append('화 제목 한영 불일치: %s / %s' % (en, kr))
            if bool(m.group(2)) != (n == 10) or (mk and bool(mk.group(2)) != (n == 10)):
                errs.append('페이월 표기 자리 틀림: %s / %s' % (en, kr))
            if n != ep + 1:
                errs.append('화 번호 순서: %d 다음에 %d' % (ep, n))
            ep, sc = n, 0
            eps.append(n)
        elif k == 'scene':
            m = SC_RE.match(en)
            a, b = int(m.group(1)), int(m.group(2))
            if a != ep:
                errs.append('EP%d 안에 씬 %d-%d' % (ep, a, b))
            if b != sc + 1:
                errs.append('EP%d 씬 번호 건너뜀/역순: %d 다음 %d' % (ep, sc, b))
            if not kr.startswith('S#%d-%d. ' % (a, b)):
                errs.append('씬 헤더 한영 번호 불일치: %s / %s' % (en, kr))
            sc = b
        elif k == 'action':
            for w in PRON.findall(en):
                (errs if w.lower() in ('he', 'she', 'they', 'him', 'them', 'himself', 'herself', 'themselves') else warns).append(
                    'EP%d 지문 대명사 %s: %s' % (ep, w, en[:110]))
        elif k == 'dlg':
            if not re.match(r'^[^:]{1,25}: ', kr):
                warns.append('한국어 대사 줄 모양: ' + kr[:60])
    if eps != list(range(1, 31)):
        errs.append('화 목록이 1~30이 아님: %s' % eps)
    return errs, warns


def main():
    items, errs = load()
    e2, warns = check(items)
    errs += e2
    for w in warns:
        print('△', w)
    for e in errs:
        print('✗', e)
    print('요소 %d · 오류 %d · 확인 %d' % (len(items), len(errs), len(warns)))
    if '--check-only' in sys.argv or errs:
        return 1 if errs else 0
    os.makedirs(OUT_DIR, exist_ok=True)
    with io.open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write('# %s\n# 시스템 파워로 아내만 셋 in 고대 이집트\n\n' % TITLE)
        f.write('\n\n'.join('%s\n%s' % (en, kr) for _, en, kr, _ in items) + '\n')
    from house_script_docx import build
    build([(k, en, kr) for k, en, kr, _ in items], OUT_DOCX,
          title='%s / 시스템 파워로 아내만 셋 in 고대 이집트' % TITLE)
    print(OUT_MD)
    print(OUT_DOCX)
    return 0


if __name__ == '__main__':
    sys.exit(main())
