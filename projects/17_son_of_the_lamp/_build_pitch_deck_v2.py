# -*- coding: utf-8 -*-
"""피칭 페이지 — 주요 인물 소개 / 줄거리 / 초반 회차 트리트먼트 빌더.

이 파일이 텍스트 정본. 실행하면 docx + md 두 벌을 같은 내용으로 뽑는다.
v3 (2026-08-12): 사용자 지시 — 이 3개 항목만 산출(타이틀·기본정보·피칭 사유는 사용자 작성분 사용).
                 구구절절 삭제 · 비유 표현 제거(손/판을 뒤집는다/왕의 손에 남긴다) · 설명체 → 짧은 문장.
"""
import os
import docx
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DOCX = os.path.join(HERE, '거지 알라딘과 요술램프_피칭페이지_v4.docx')
OUT_MD = os.path.join(HERE, '17_son_of_the_lamp_02_pitch_deck_v4.md')

BLACK = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x7A, 0x7A, 0x7A)
ACC = RGBColor(0x8A, 0x5A, 0x10)
LINE = RGBColor(0xC9, 0xB8, 0x92)

d = docx.Document()
sec = d.sections[0]
sec.left_margin = sec.right_margin = Cm(2.2)
sec.top_margin = sec.bottom_margin = Cm(1.9)

PLAIN = []


def para(space_after=0, space_before=0, keep=False, indent=0, spacing=1.30):
    p = d.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    pf.line_spacing = spacing
    pf.keep_with_next = keep
    if indent:
        pf.left_indent = Pt(indent)
    PLAIN.append('')
    return p


def run(p, text, *, size=11, color=BLACK, bold=False, plain=True):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.bold = bold
    r.font.name = '맑은 고딕'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), '맑은 고딕')
    if plain:
        PLAIN[-1] += text
    return r


def section(title, en=None):
    p = para(space_before=18, space_after=7, keep=True)
    run(p, title, size=13, bold=True, color=ACC)
    if en:
        run(p, '  ' + en, size=9.5, color=GREY)


def body(text, space_after=6, indent=0):
    p = para(space_after=space_after, indent=indent)
    run(p, text)


def person(name, desc):
    p = para(space_before=10, space_after=3, keep=True)
    run(p, name, size=11, bold=True, color=ACC)
    body(desc, space_after=0)


# ── 표지 ─────────────────────────────────────────────
t = para(space_after=3)
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(t, '거지 알라딘과 요술램프', size=20, bold=True)

t2 = para(space_after=4)
t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(t2, 'Beggar Aladdin and the Almighty Lamp', size=12, color=ACC)

t3 = para(space_after=6)
t3.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(t3, '주요 인물 소개  ·  줄거리  ·  초반 회차 트리트먼트', size=9.5, color=GREY)

t4 = para(space_after=4)
t4.alignment = WD_ALIGN_PARAGRAPH.CENTER
run(t4, '─' * 20, size=8, color=LINE, plain=False)

# ── 인물 ─────────────────────────────────────────────
section('주요 인물 소개')

person('알라딘 (Aladdin, 남 / 외견 20대)  ·  남자주인공',
       '정령들의 왕. 전쟁도 정복도 매번 똑같아서 지겨워 왕좌를 버리고, 군단은 놋쇠 램프에 봉인해 허리에 '
       '차고 인간 세상으로 내려왔다. 세계 최강인데 밥벌이를 못 해 접시 27장 깨고 잘린다. 월급 200금화짜리 '
       '공주 호위 공고를 보고 "공주를 지키는 건 양심 있는 자의 의무지"라며 지원한다.')
body('몰래는 다 처리한다. 자객이 던진 단검은 손가락 한 번에 궤도가 꺾이고, 자객은 램프 속으로 빨려 '
     '들어간다. 대신 대놓고 나서는 건 명령이 있어야 한다. 눈앞에서 공주가 협박당해도 "아직 명령을 안 '
     '내렸잖아. 절차를 존중해라"면서 사과만 씹는다. 공주가 "가서 저것들 다 죽여버려!"라고 소리쳐야 '
     '"절차가 맞았군요. 업무 시작." 그리고 고위 마법사 둘이 뺨 한 대씩에 날아간다.', space_after=0)

person('소라야 (Soraya, 여)  ·  여자주인공',
       '카마르(Qamar) 왕국의 공주. 술탄이 쓰러진 뒤 왕좌를 노리는 총독 마리크와 혼자 싸운다. "내가 살아 '
       '있는 한 카마르는 썩은 피가 넘볼 수 없다"고 면전에 대고 쏘아붙인다.')
body('약에 취해 끌려가던 밤 웬 거지가 구해줬고, 다음 날 아침 그 거지에게 금화를 던지며 "어젯밤 일은 '
     '없었던 걸로 해. 한마디라도 흘리면 죽인다"고 못 박는다. 그런데 그놈이 자기 호위로 들어온다. 자객이 '
     '사라질 때마다 저놈인가 싶다가도, 사과나 씹고 있는 얼굴을 보면 아니라고 결론 낸다.', space_after=0)

person('지니 (Genie, 남)  ·  램프의 정령',
       '램프에 봉인된 시종장. 부르지도 않았는데 튀어나와 거지꼴 주인을 "전하"라고 불러서 매번 정체를 '
       '날려먹을 뻔한다. "인간 세계에선 그 호칭 금지. 끄덕이면 예스, 흔들면 노!"라는 규칙이 생긴 뒤로는 '
       '할 말이 있어도 고개만 흔든다. 주인이 씹는 흑빵을 보고는 "이건 저녁이 아니라 건축 자재입니다!"라며 '
       '통곡한다.')

person('마리크 (Malik, 남)  ·  메인 빌런',
       '공주의 외척이자 총독. 술탄이 쓰러지자 나라를 대신 굴리면서 공주를 귀족 할리드와 결혼시켜 치우려 '
       '한다. 보낸 자객이 사라지면 고위 마법사를, 그것도 안 되면 현상수배된 찬탈자를 부른다. "암영을 '
       '지웠다면 최소 대마법사급… 술탄, 아직 뒷수가 남아 있었군." 매일 공주 옆에 서 있는 그 호위는 '
       '끝까지 눈에 안 들어온다.')

person('할리드 (Khalid, 남)  ·  귀족 공자 / 연적',
       '마리크가 미는 공주의 약혼자. 고위 마법사 둘을 개인 호위로 끌고 다닌다. 공주 침전 문을 부수고 '
       '들어와 "무릎 꿇고 내 장화를 핥으면 다리 하나만 부러뜨려주지"라고 지껄이다가, 이름도 모르는 '
       '호위에게 뺨 한 대 맞고 붉은 속바지 차림으로 문밖으로 날아간다.')

person('바스마 (Basma, 여)  ·  공주의 시녀',
       '호위 선발 담당 시녀. 전 종목 0점 받은 알라딘을 "그래도 공주님이 악몽은 안 꾸시겠네"라며 얼굴만 '
       '보고 뽑았다. 사고가 터질 때마다 몸으로 공주를 막아선다.')

person('레이븐 (Raven, 남)  ·  찬탈자',
       '여러 왕국이 현상금을 건 찬탈자. 창백한 얼굴 전체에 뒤틀린 검은 룬이 새겨져 있다. 마리크가 '
       '마지막으로 부른 인물이고, 7화 마지막 컷에 걸어 들어오며 말한다. "안녕들 하신가. 누가 자잘한 '
       '장애물을 좀 치워달라던데."')

# ── 줄거리 ───────────────────────────────────────────
section('줄거리')
body('진의 왕 알라딘은 무적이 지겨워 왕좌를 버린다. 군단은 램프에 봉인했고, 인간 세상에서 원하는 건 '
     '월급과 조용한 삶뿐이다. 접시나 깨고 쫓겨나던 어느 밤, 뒷골목에서 끌려가던 공주 소라야를 구한다. '
     '다음 날 월급 200금화에 혹해 하필 그 공주의 호위로 들어간다.')
body('총독 마리크는 공주를 귀족과 결혼시켜 치우고, 그게 안 되면 자객을 보내 왕좌를 가져가려 한다. '
     '알라딘은 날아드는 단검을 손가락으로 꺾고, 자객을 램프에 삼키고, 고위 마법사들을 뺨 한 대씩으로 '
     '눕힌다. 왕국은 "술탄이 숨겨둔 대마법사"를 찾아 술렁이지만, 그가 진의 왕이라는 건 관객만 안다.')
body('마리크가 찬탈자 레이븐을 불러들이고, 소라야는 그날 밤 자기를 구한 게 매일 옆에서 사과나 씹던 그 '
     '호위였다는 걸 알게 된다. 정체를 드러낸 알라딘이 마리크와 레이븐을 무너뜨리고 술탄이 보는 앞에서 '
     '공주의 손을 잡는다. 사막 저편엔 그가 비워둔 진의 왕좌가 그대로 남아 있다.')

# ── 트리트먼트 ───────────────────────────────────────
section('초반 회차 트리트먼트', '1화~무료 마지막 화')
p = para(space_after=9)
run(p, '무료회차 대본 1-7화 첨부', size=10, color=GREY)

TREATMENT = [
    ('1화',
     '진의 왕 알라딘이 손가락 하나로 적 대군을 통째로 지운다. "무적이란 건 가장 지루한 저주였군." '
     '군단을 램프에 봉인하고 내려간 인간 세상, 그날 밤 폐가에서 돌덩이 같은 흑빵을 씹는다.',
     '골목에서 비명. 약을 먹인 공주를 마차로 끌고 가려던 폭도들 앞에 반쪽 흑빵을 든 거지 청년이 선다.'),
    ('2화',
     '금빛 몇 줄기에 폭도 전원이 벽에 처박힌다. 다음 날 아침 마차 안, 얼굴이 붉어진 소라야가 금화 '
     '주머니를 던진다. "어젯밤 일은 없었던 걸로 해. 한마디라도 흘리면 죽인다."',
     '광장 게시판 [공주 전속 호위 고액 모집]. "안 가!" 돌아서던 알라딘이 "월급이 200금화입니다" '
     '한마디에 게시물을 뜯어낸다. "공주를 지키는 건 양심 있는 자의 의무지."'),
    ('3화',
     '전 종목 0점을 받은 알라딘이 얼굴 하나로 뽑힌다. 침전에서 재회한 소라야 앞에 허리를 90도로 '
     '꺾는다. "사람을 잘못 보셨습니다. 여신 같은 여자는 본 적도 없습니다."',
     '"전하, 이 방에 쥐가 들었습니다." 구석의 그림자가 찢어지고 단검이 소라야의 등으로 날아간다.'),
    ('4화',
     '손가락 한 번에 단검 궤도가 꺾이고, 도망치던 자객은 램프에 통째로 삼켜진다. "방금… 네가 한 '
     '거야?" "제가요? 저 방금 오줌 쌀 뻔했는데요."',
     '마리크의 밀실, 푸른 촛불이 꺼진다. "암영을 지웠다면 최소 대마법사급… 이제 할리드 그 멍청이를 '
     '써야겠어."'),
    ('5화',
     '침전 문이 부서지며 할리드가 고위 마법사 둘을 끌고 들어온다. "네 호위 중에 내 손에서 한 수라도 '
     '버티는 놈이 있으면 돌아가주지."',
     '사과 씹는 소리가 침전에 크게 울린다. 기둥에 기대 구경하던 호위를 발견한 소라야가 손가락으로 '
     '그를 가리킨다. "너! 알라딘, 이 개자식! 가서 저것들 다 죽여버려!"'),
    ('6화',
     '"저요?" "그래, 너!" "절차가 맞았군요. 업무 시작." 알라딘이 공주 앞을 막아선다. "쫓아내면 '
     '됩니까, 기절시킬까요, 아니면 앞으로 문만 봐도 무서워지게 만들까요?"',
     '두 마법사가 동시에 주문을 시작하고 발밑에서 검은 법진이 타오른다.'),
    ('7화',
     '불뱀이 침전을 채우는 순간 알라딘이 사라진다. 짝—! 뺨 네 번에 마법사와 호위 전원이 벽에 '
     '처박히고, 허리띠가 끊긴 할리드가 붉은 속바지 차림으로 문밖으로 날아간다. "꺼져."',
     '마리크의 저택. 뺨이 부어터진 할리드 앞으로 검은 룬을 새긴 찬탈자 레이븐이 걸어 들어온다. '
     '"안녕들 하신가. 누가 자잘한 장애물을 좀 치워달라던데."'),
]

for ep, line, cliff in TREATMENT:
    h = para(space_before=10, space_after=3, keep=True)
    run(h, ep, size=11, bold=True, color=ACC)
    body(line, space_after=3)
    p = para(space_after=0)
    run(p, '클리프  ', size=10.5, bold=True, color=GREY)
    run(p, cliff, size=10.5)

d.save(OUT_DOCX)

# 같은 내용의 텍스트본 (docx와 절대 어긋나지 않게 같은 버퍼에서 뽑는다)
lines, blank = [], False
for x in PLAIN:
    x = x.replace('\t', ' ').strip()
    if not x:
        blank = True
        continue
    if lines and blank:
        lines.append('')
    lines.append(x)
    blank = False
with open(OUT_MD, 'w', encoding='utf-8') as f:
    f.write('# 거지 알라딘과 요술램프 — 인물 / 줄거리 / 트리트먼트\n\n'
            '> `_build_pitch_deck_v2.py` 자동 생성물. 직접 고치지 말 것 — 빌더를 고치고 다시 실행.\n\n')
    f.write('\n'.join(lines) + '\n')

print('OK docx', OUT_DOCX)
print('OK md  ', OUT_MD)
print('paragraphs', len(lines))
