# -*- coding: utf-8 -*-
"""작가 3차 회수본(1~30화)에 검수 코멘트 주입 → _1-30화_검수코멘트_v16.docx
   - 원본에 comments.xml이 없어서 새로 만들고 Content_Types/rels도 함께 등록한다.
   - 앵커는 단락 번호가 아니라 본문 고유 문구.
"""
import io, os, re, sys, shutil, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC = r"C:\Users\Rowan\Downloads\I Chose a Slave, But He Parts the Sea_내 남편은 거지 모세_대본1-30.docx"
OUT = r"C:\Users\Rowan\scenario-automation\projects\16_moses\내 남편은 거지 모세_1-30화_검수코멘트_v16.docx"
AUTHOR, INITIALS, DATE = 'Rowan Lee', 'RL', '2026-08-06T00:00:00Z'
WT = r'<w:t(?:\s[^>]*)?>(.*?)</w:t>'

SUMMARY = (
 "22~30화 트리트먼트 골격 정확히 따라와 주셨습니다. 25~26화 케네트 대목 — 펜던트를 뺏고, 그날 밤 그 손에 종기가 돋고, "
 "무릎 꿇은 사람을 다말이 약초로 치료해주는 흐름 — 은 이 작품이 22화부터 하려던 걸 그대로 보여줍니다. 손대지 마세요.\n"
 "\n"
 "두 가지만 부탁드립니다.\n"
 "\n"
 "하나. 1~21화 지난 코멘트가 절반쯤 안 들어왔습니다. 특히 8~10화, 14화, 17~18화, 21화는 통째로 손이 안 간 것 같아 다시 앵커 달았습니다.\n"
 "\n"
 "둘. 이번 원고에서 문장이 일곱 군데 잘렸습니다. 일괄 치환하시다 빠진 것 같습니다 — 1화 \"이 왕국의 로 책봉하노라\"(대왕비), "
 "1화 \"△ 델릴라가\", 5화 \"바쁜데... .\", 7화 \"떠받들 듯이\", 8화 \"왕국의 가 되는 날\"(대왕비), 15화 \"왕도로 !\"(간다), "
 "25화 \"알아봐  거야\"(알아봐 줄). 각 자리에 코멘트 달아뒀습니다. \"대왕비\"는 지금 대본 전체에 1화 델릴라 대사 한 곳만 남았습니다."
)

# (앵커 문구, 코멘트)  — 앵커가 \n 로 끝나면 그 단락 전체와 정확히 일치해야 함
C = [
# ── 총평 ──
("제1화\n", SUMMARY),

# ── 1화 ──
("그녀의 가슴을 관통해",
 "뒤에서 찔러 앞으로 나오게 고쳐주신 건 좋은데, 아래에서 델릴라가 다말 앞에 서 있는 채로 \"가슴에 박힌 단검\"을 뽑습니다.\n"
 "등에 박힌 걸 뽑는 걸로요."),

("로 책봉하노라",
 "\"대왕비\"가 통째로 빠졌습니다 → 이 왕국의 대왕비로 책봉하노라."),

("△ 델릴라가\n",
 "문장이 잘렸습니다. 원래 \"계속 미친듯 웃고 있다\"였습니다."),

("지옥의 불길 속으로",
 "지옥 → 저승."),

# ── 2~3화 ──
("△ 비둘기는 부드럽게 노예들이 있는 구역으로 날아간다",
 "클리프는 비둘기가 날아올라 광장 한 바퀴 도는 데까지만.\n"
 "여기서 노예 구역에 닿으면 3화 첫 컷(군중이 팔 뻗고 비둘기가 피해 다니는)이 되감기가 됩니다."),

("하지만 신의 대언자로서 선사받은 이 지팡이를",
 "정체를 숨기는 중인데 제 입으로 대언자라고 합니다.\n"
 "모세: 나도 쉬는 새를 괴롭히고 싶진 않아. 하지만 이건 내 지팡이다."),

# ── 5화 ──
("계략을 꾸미기 바쁜데",
 "뒷문장이 통째로 날아갔습니다. 원래 \"이 여인의 영혼만은 새벽빛처럼 밝고 맑구나\"였습니다."),

# ── 7화 ──
("△ 라반은 급히 몸을 숙여 떠받들 듯이\n",
 "문장이 잘렸습니다."),

# ── 8화 ──
("마차에서 화관을 쓴 대머리 대신관이 내린다",
 "화관이 남았습니다. \"흰 관을 쓴\" 정도로요."),

("내가 왕국의 가 되는 날",
 "여기도 \"대왕비\"가 빠졌습니다."),

# ── 9화 ──
("저 펜던트는 주군께서 가장 아끼시는 성물이잖아",
 "\"성물\" → \"태어날 때부터 지녀오신 물건\"으로요."),

("우리 인연의 증표로 간직할게요",
 "\"당신의 과거를 맡기신 거군요\"가 소리로 들으면 안 잡힙니다.\n"
 "다말: 이걸 저한테요? 평생 몸에 지니셨던 거잖아요. 무슨 일이 있어도 제가 지킬게요."),

# ── 10화 ──
("다말: 모세, 저들은 누구예요?",
 "앞 화 끝에서 장로들이 다말 앞에서 \"대언자시여!\" 했는데, 못 들은 것처럼 넘어갑니다.\n"
 "다말: 방금… 대언자라고 했어요. 당신을 그렇게 불렀어요."),

("성소에 혼란이 일고 있습니다",
 "\"혼란이 일고 있다\"로는 무슨 일인지 안 들려서요.\n"
 "장로1: 주군, 성소로 돌아오셔야 합니다. 주군 없이는 아무것도 정하지 못하고 다들 기다리고만 있습니다."),

("너희는 성소의 보물고로 가라",
 "성소는 보물창고가 아니라 검소한 은신처입니다.\n"
 "모세: 성소에서 가장 귀한 것들을 골라 라반의 저택으로 가져가라.\n"
 "\"성물들\"도 같이 빼주세요."),

# ── 13화 ──
("지금 당장 주군께 알려야 해",
 "11·12·13·14화 네 화 연속으로 모세가 화면에 없습니다. 다말 당하는 것만 네 화라 보기가 괴로워요.\n"
 "이 뒤에 두 컷만 —\n"
 "△ 성소. 말하던 모세가 문득 멈추고 왕도 쪽을 돌아본다.\n"
 "모세: …다말."),

# ── 14화 ──
("그 사람의 가문에서 대대로 내려온 펜던트라고",
 "\"태어날 때부터 지녀온 물건이야\"로요."),

# ── 15화 ──
("#2. 성소 / 같은 시각",
 "씬 헤더에 위치만 넣어주세요 → #2. 왕도 밖 광야, 성소 / 같은 시각"),

("지금 당장 왕도로 !",
 "\"간다\"가 잘렸습니다."),

# ── 17화 ──
("누가 내 아내를 이렇게 만들었지?",
 "11화에서 파라오가 다말의 턱을 잡았는데 그 값을 아무도 안 받습니다.\n"
 "델릴라 자백 뒤에 한 줄만 —\n"
 "다말: …그리고 저 사람이, 제 턱을 잡았어요.\n"
 "△ 모세의 시선이 천천히 파라오에게로 옮겨간다."),

("엄정한 법정에 세워 그 죄를 심판할 것이다",
 "\"법정\" → \"내 앞에 끌어내 그 죄를 물을 것이다\" 정도로요."),

# ── 18화 ──
("얼굴만은 안 돼요",
 "얼굴만은 안 된다고 비는데 얼굴에 아무 일도 안 일어나서 이 대사가 헛돕니다. 자국 하나만 —\n"
 "△ 델릴라의 뺨이 불길에 닿는다. 비명과 함께 볼에 붉은 자국이 길게 남는다."),

# ── 21화 ──
("나를 지켜주는 황금 펜던트는 지금 다말에게 있다",
 "이 대사만 빼주세요. 펜던트에 힘이 있으면 다말이 목숨 걸고 되찾은 이유가 물건값이 됩니다.\n"
 "\"그래. 나는 사람이다.\" 한 줄이면 됩니다."),

("△ 왕도를 가로지르는 큰 강이 상류부터 핏빛으로 물들기 시작한다",
 "이 지문만 빼주세요. 군중 대사는 그대로 둡니다.\n"
 "바로 다음 화 첫 대사가 \"핏물이 솟는 건 우물뿐이오!\"라 정면으로 부딪힙니다."),

# ── 22화 ──
("급하게 왕도를 수색했으나",
 "이 화에 다말이 한 번도 언급이 안 됩니다. 어제 실려 나간 딸인데 라반도 네페라도 안 찾아서요.\n"
 "라반: 다말은? 그년도 같이 사라진 것이냐?"),

# ── 23화 ──
("△ 화려하고 넓은 침전",
 "성소는 검소한 은신처로 잡아뒀습니다. 지난번에 저희가 \"성소를 초라하게 그리지 말아주세요\"라고만 적어서 생긴 일이라 죄송합니다.\n"
 "화려한 쪽이 아니라 단단하고 조용한 쪽으로요 — 돌벽, 두꺼운 천, 약 냄새."),

("사제1: 저자는 라반 가문에서 소란을 일으키고",
 "\"사제\" → \"신관\"으로요. 등장인물 줄에도 있고, 다음 화에도 두 군데 있습니다."),

("네 오만함을 꺾을 벌이 수백 가지가 넘는다",
 "모세가 받아치는 톤을 조금 낮춰주세요. 화를 내면 파라오와 같은 급이 됩니다.\n"
 "모세: 하나만 해라. 시간 없다."),

("이것은 부탁이 아니다",
 "짧게 —\n"
 "모세: 묻는 게 아니라고 했다."),

# ── 24화 ──
("델릴라의 침소를 더럽힌 것도 네 술수겠지",
 "여기가 제일 중요합니다. 지금은 모세가 파라오 말을 믿고 재앙을 거뒀다가 뒤통수를 맞아서, 시청자 눈에 모세가 순진한 사람이 됩니다.\n"
 "모세: 내가 벌인 일이 아니다. 네가 벌인 일이다."),

("△ 지팡이에서 황금빛 빛과 함께 모래 바람이 분다",
 "모세가 거두는 게 아니라 저절로 걷히는 걸로 바꿔주세요. 지팡이 컷도 빼주시고요 — 지팡이에 힘이 있는 것처럼 보여서요.\n"
 "모세: 그래라.\n"
 "△ 모세가 돌아선다.\n"
 "△ 개구리는 저절로 걷힌다.\n"
 "\n"
 "그다음 파라오가 비웃는 대사는 그대로 두세요. 모세가 안 놀라면 속은 사람은 파라오가 됩니다."),

("감독관: 여기서는 당신이 누구의 아내인지",
 "이 인물 표기가 24·25화는 \"감독관\", 26화는 \"감독\"입니다. \"감독\"으로 통일해주세요."),

# ── 25화 ──
("성소 사람들도 나를 알아봐",
 "\"줄\"이 빠졌습니다 → 나를 알아봐 줄 거야."),

# ── 26화 ──
("△ 다말이 물독 마당을 향해 걸음을 옮긴다",
 "바로 다음 씬에서 다말이 다시 봉사관에 서 있습니다. 사자가 오는 씬을 물독 마당으로 옮겨주세요."),

# ── 27화 ──
("모래바람이 불고 모세가 나타난다",
 "모세는 걸어서 오고 걸어서 갑니다. 순간이동은 안 하는 인물이라서요.\n"
 "29화 \"모세가 등을 돌리고 사라진다\"도 같이요."),

("#2. 왕국 / 낮",
 "왕궁으로요. 28화 두 곳, 29화 두 곳 씬 헤더에도 \"왕국\"이 들어가 있습니다."),

("왕궁 밖으로 한 발짝도 나가지 못하게 하라",
 "이 화 클리프가 약합니다. 다음 화 첫머리의 무릎 꿇리는 장면을 여기로 당겨주세요.\n"
 "델릴라: 언니, 여기선 이게 예법이야.\n"
 "\n"
 "28화 델릴라 대사 중 \"왕궁에는 각자의 위치에 맞는 예법이라는 게 있어…\" 부분은 이 한 줄로 줄이시면 됩니다."),

# ── 28화 ──
("#1. 왕국의 지하 감옥 / 밤",
 "다말은 죄수가 아니라 볼모라 왕궁 안에 두는 게 맞습니다. 28·29화 지하 감옥을 왕궁 안 빈 방으로 바꿔주세요.\n"
 "두 화 연속 어두운 감옥이면 화면도 답답해집니다."),

("△ 흙먼지는 서서히 이로 변한다",
 "흙이 벌레로 변하는 과정은 AI로 안 나옵니다. 두 컷으로 끊어주세요 —\n"
 "△ 왕궁 마당에 흙먼지가 인다.\n"
 "△ 델릴라의 옷 속으로 이가 파고든다."),

# ── 29화 ──
("왕국에 벌레가 들끓고 있어",
 "재앙은 아직 왕궁 안에서만 일어납니다. 나라 전체로 번지는 건 36화부터라, 여기서 나라 전체가 되면 남은 재앙들이 갈 데가 없어집니다.\n"
 "하녀1: 왕궁이 난리야. 그런데 성 밖은 멀쩡하대. 이상하지 않아?"),

("모세가 남자의 얼굴로 변신해 정체를 숨긴 것이다",
 "변신은 빼주세요. 모세는 사람이라 얼굴을 못 바꿉니다. 그리고 남편이 아내에게 남인 척하고 접근하는 그림이라 다말 쪽 감정도 상합니다.\n"
 "변장 없이 그냥 모세로 들어가고, 다말이 안 가겠다고 하는 걸로요.\n"
 "아래 \"손바닥으로 얼굴을 훔치자 원래 얼굴이 나온다\" 컷도 같이 빼주세요."),

("그대의 뜻이 그렇다면 존중하겠소",
 "모세가 다말을 부르는 말이 당신·너·그대로 섞여 있고, 이 화만 \"…하겠소\"입니다.\n"
 "23·27화처럼 통일해주세요."),

# ── 30화 ──
("밤하늘에 먹구름이 몰려온다",
 "씬 헤더가 \"왕도 광장 / 낮\"인데 밤하늘입니다."),

("분명 저 여자가 꾸민 짓이야",
 "델릴라가 다말과 재앙을 연결 짓는 건 33화에 터뜨릴 카드입니다. 여기선 아직 몰라야 해서요.\n"
 "델릴라: 하필 왜 나만! 왜 나만 이런 꼴을 당하는 거냐고!\n"
 "\n"
 "위 군중2의 \"마치 신께서 다말의 편에 서신 것처럼\"도 \"저 노예의 신인가?\" 정도로요."),

("근위대장의 머리를 때린다",
 "좋습니다. 옆에 안 맞는 사람 하나만 붙여주세요.\n"
 "△ 바로 옆에 선 하인의 머리 위엔 한 알도 떨어지지 않는다."),

("내 손에 피를 묻혀서라도",
 "오탈자만 모았습니다 — 걱정마 (4화), 사과 말아요 (23화), 가야해요 (27화), 눈을 크게 뜬다.. (13화), "
 "이중 공백 (5·19·20·22·25·28화)."),
]


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def body_xml(cid, text):
    runs = []
    for j, line in enumerate(text.split('\n')):
        br = '<w:br/>' if j else ''
        runs.append(f'<w:r><w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>{br}'
                    f'<w:t xml:space="preserve">{esc(line)}</w:t></w:r>')
    return (f'<w:comment w:id="{cid}" w:author="{AUTHOR}" w:initials="{INITIALS}" '
            f'w:date="{DATE}"><w:p><w:pPr><w:pStyle w:val="CommentText"/></w:pPr>'
            + ''.join(runs) + '</w:p></w:comment>')


z = zipfile.ZipFile(SRC)
names = z.namelist()
doc = z.read('word/document.xml').decode('utf-8')
ct = z.read('[Content_Types].xml').decode('utf-8')
rels = z.read('word/_rels/document.xml.rels').decode('utf-8')

# 원본 무결성 확인 — 변경 이력·기존 코멘트 없음
assert not re.search(r'<w:ins\b|<w:del\b', doc), '변경 이력이 남아 있음 — 수락 후 진행할 것'
assert 'word/comments.xml' not in names and 'commentReference' not in doc, '기존 코멘트 있음'
print('원본 확인: 변경 이력 0 · 기존 코멘트 0')

# ── 앵커 찾기 ──
spans = [m.span() for m in re.finditer(r'<w:p[ >].*?</w:p>|<w:p/>', doc, re.S)]
texts = []
for a, b in spans:
    t = ''.join(re.findall(WT, doc[a:b], re.S))
    texts.append(t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                  .replace('&quot;', '"').replace('&apos;', "'"))

edits, bodies, cid, bad = [], [], 0, []
for anchor, text in C:
    key = anchor.rstrip('\n')
    hits = [i for i, t in enumerate(texts)
            if (key in t) and (not anchor.endswith('\n') or t.strip() == key.strip())]
    if len(hits) != 1:
        bad.append((anchor[:45], len(hits)))
        continue
    i = hits[0]
    a, b = spans[i]
    p = doc[a:b]
    m = re.search(r'<w:r[ >]', p)
    if not m:
        bad.append((anchor[:45], 'run 없음'))
        continue
    st = f'<w:commentRangeStart w:id="{cid}"/>'
    en = (f'<w:commentRangeEnd w:id="{cid}"/><w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>'
          f'<w:commentReference w:id="{cid}"/></w:r>')
    newp = p[:m.start()] + st + p[m.start():]
    newp = newp[:newp.rindex('</w:p>')] + en + '</w:p>'
    edits.append((a, b, newp))
    bodies.append(body_xml(cid, text))
    cid += 1

if bad:
    print('=== 앵커 실패 ===')
    for k, n in bad:
        print('  ', n, '|', k)
    sys.exit(1)

for a, b, newp in sorted(edits, key=lambda x: -x[0]):
    doc = doc[:a] + newp + doc[b:]

NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"')
com = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       f'<w:comments {NS}>' + ''.join(bodies) + '</w:comments>')

# Content_Types · rels 등록
assert 'comments+xml' not in ct
ct = ct.replace('</Types>',
                '<Override PartName="/word/comments.xml" ContentType="application/vnd.'
                'openxmlformats-officedocument.wordprocessingml.comments+xml"/></Types>')
rid = 'rIdComments1'
assert rid not in rels
rels = rels.replace('</Relationships>',
                    f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/'
                    'officeDocument/2006/relationships/comments" Target="comments.xml"/></Relationships>')

tmp = OUT + '.tmp'
zout = zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED)
for it in z.infolist():
    d = z.read(it.filename)
    if it.filename == 'word/document.xml':
        d = doc.encode('utf-8')
    elif it.filename == '[Content_Types].xml':
        d = ct.encode('utf-8')
    elif it.filename == 'word/_rels/document.xml.rels':
        d = rels.encode('utf-8')
    zout.writestr(it, d)
zout.writestr('word/comments.xml', com.encode('utf-8'))
zout.close(); z.close()
os.replace(tmp, OUT)

# ── 검증: 본문 텍스트 무변경 ──
zz = zipfile.ZipFile(OUT)
d2 = zz.read('word/document.xml').decode('utf-8')
t_old = ''.join(texts)
p2 = [m.span() for m in re.finditer(r'<w:p[ >].*?</w:p>|<w:p/>', d2, re.S)]
t_new = ''.join(''.join(re.findall(WT, d2[a:b], re.S)) for a, b in p2)
assert t_old == t_new, '본문이 변경됨'
assert len(re.findall(r'<w:comment ', zz.read('word/comments.xml').decode('utf-8'))) == len(bodies)
print(f'코멘트 {len(bodies)}개 주입 · 본문 무변경 확인 · 단락 {len(p2)}')
print('WROTE', OUT)
