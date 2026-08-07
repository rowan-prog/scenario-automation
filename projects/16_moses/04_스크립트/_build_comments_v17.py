# -*- coding: utf-8 -*-
"""작가 3차 회수본(1~30화)에 검수 코멘트 주입 → _1-30화_검수코멘트_v17.docx
   v16 대비: 총평은 대본 전체 단위 얘기만. 라인 코멘트는 전부 '무엇을 어떻게'.
   오류·오탈자·치환 = 지시만(사유 0). 우리가 방향을 바꾸는 것만 사유 한 줄.
"""
import io, os, re, sys, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC = r"C:\Users\Rowan\Downloads\I Chose a Slave, But He Parts the Sea_내 남편은 거지 모세_대본1-30.docx"
OUT = r"C:\Users\Rowan\scenario-automation\projects\16_moses\내 남편은 거지 모세_1-30화_검수코멘트_v17.docx"
AUTHOR, INITIALS, DATE = 'Rowan Lee', 'RL', '2026-08-06T00:00:00Z'
WT = r'<w:t(?:\s[^>]*)?>(.*?)</w:t>'

SUMMARY = (
 "1~21화는 지난 코멘트가 절반쯤 안 들어왔습니다. 8~10화·14화·17~18화·21화는 손이 안 간 것 같아 그 자리에 다시 달았습니다.\n"
 "\n"
 "이번 원고에서 문장이 여섯 군데 잘렸습니다(1·5·7·8·15·25화). 일괄 치환하시다 빠진 것 같습니다. "
 "\"대왕비\"는 지금 대본 전체에 1화 델릴라 대사 한 곳만 남았습니다."
)

C = [
("제1화\n", SUMMARY),

# ── 1화 ──
("그녀의 가슴을 관통해",
 "아래 두 곳도 등으로.\n"
 "\"가슴에서 피를 흘린 채\" → \"등에서 피를 흘린 채\"\n"
 "\"다말의 가슴에 박힌 단검\" → \"다말의 등에 박힌 단검\""),

("로 책봉하노라",
 "\"이 왕국의 로\" → \"이 왕국의 대왕비로\""),

("△ 델릴라가\n",
 "잘렸습니다. → △ 델릴라가 계속 미친듯 웃고 있다."),

("지옥의 불길 속으로",
 "\"지옥의 불길\" → \"저승의 불길\""),

# ── 2~3화 ──
("△ 비둘기는 부드럽게 노예들이 있는 구역으로 날아간다",
 "이 지문을 \"△ 비둘기가 날아올라 광장을 한 바퀴 돈다.\"로 바꾸고 2화를 여기서 끊어주세요. 노예 구역으로 날아가는 건 3화 첫 컷입니다.\n"
 "\n"
 "지금은 3화 첫 컷(군중이 팔 뻗는)이 되감기가 됩니다."),

("하지만 신의 대언자로서 선사받은 이 지팡이를",
 "이 대사를 통째로 교체.\n"
 "모세: 나도 쉬는 새를 괴롭히고 싶진 않아. 하지만 이건 내 지팡이다.\n"
 "\n"
 "정체를 숨기는 중인데 제 입으로 대언자라고 해서요."),

# ── 5화 ──
("계략을 꾸미기 바쁜데",
 "뒷문장이 날아갔습니다.\n"
 "→ 모세VO: 이 땅의 거짓된 신들은 권세를 차지하기 위해 서로 계략을 꾸미기 바쁜데... 이 여인의 영혼만은 새벽빛처럼 밝고 맑구나."),

# ── 7화 ──
("△ 라반은 급히 몸을 숙여 떠받들 듯이\n",
 "잘렸습니다. 뒷부분 채워주세요."),

# ── 8화 ──
("마차에서 화관을 쓴 대머리 대신관이 내린다",
 "\"화관을 쓴\" → \"흰 관을 쓴\""),

("내가 왕국의 가 되는 날",
 "\"왕국의 가 되는 날\" → \"왕국의 대왕비가 되는 날\""),

# ── 9화 ──
("저 펜던트는 주군께서 가장 아끼시는 성물이잖아",
 "\"가장 아끼시는 성물이잖아\" → \"태어날 때부터 지녀오신 물건이잖아\""),

("우리 인연의 증표로 간직할게요",
 "이 대사를 통째로 교체.\n"
 "다말: 이걸 저한테요? 평생 몸에 지니셨던 거잖아요. 무슨 일이 있어도 제가 지킬게요.\n"
 "\n"
 "\"당신의 과거를 맡기신 거군요\"가 소리로 들으면 안 잡혀서요."),

# ── 10화 ──
("다말: 모세, 저들은 누구예요?",
 "이 대사를 교체.\n"
 "다말: 방금… 대언자라고 했어요. 당신을 그렇게 불렀어요.\n"
 "\n"
 "앞 화 끝에서 장로들이 다말 앞에서 \"대언자시여!\" 했는데 못 들은 것처럼 넘어가서요."),

("성소에 혼란이 일고 있습니다",
 "이 대사를 교체.\n"
 "장로1: 주군, 성소로 돌아오셔야 합니다. 주군 없이는 아무것도 정하지 못하고 다들 기다리고만 있습니다.\n"
 "\n"
 "\"혼란이 일고 있다\"로는 무슨 일인지 안 들려서요."),

("너희는 성소의 보물고로 가라",
 "\"성소의 보물고로 가라. 그곳에서 가장 귀한 성물들을 골라\" → \"성소에서 가장 귀한 것들을 골라\""),

# ── 13화 ──
("지금 당장 주군께 알려야 해",
 "이 대사 뒤에 두 컷 추가.\n"
 "△ 성소. 말하던 모세가 문득 멈추고 왕도 쪽을 돌아본다.\n"
 "모세: …다말.\n"
 "\n"
 "11~14화 네 화 연속 모세가 화면에 없어서, 다말 당하는 것만 네 화가 됩니다."),

# ── 14화 ──
("그 사람의 가문에서 대대로 내려온 펜던트라고",
 "\"그 사람의 가문에서 대대로 내려온 펜던트라고\" → \"그 사람이 태어날 때부터 지녀온 물건이야\""),

# ── 15화 ──
("#2. 성소 / 같은 시각",
 "\"#2. 성소 / 같은 시각\" → \"#2. 왕도 밖 광야, 성소 / 같은 시각\""),

("지금 당장 왕도로 !",
 "\"왕도로 !\" → \"왕도로 간다!\""),

# ── 17화 ──
("누가 내 아내를 이렇게 만들었지?",
 "델릴라 자백(\"…어리석을 줄은 몰랐거든\") 뒤에 두 줄 추가.\n"
 "다말: …그리고 저 사람이, 제 턱을 잡았어요.\n"
 "△ 모세의 시선이 천천히 파라오에게로 옮겨간다.\n"
 "\n"
 "11화에서 파라오가 다말의 턱을 잡은 값을 아무도 안 받아서요."),

("엄정한 법정에 세워 그 죄를 심판할 것이다",
 "\"엄정한 법정에 세워 그 죄를 심판할 것이다\" → \"내 앞에 끌어내 그 죄를 물을 것이다\""),

# ── 18화 ──
("얼굴만은 안 돼요",
 "이 대사 뒤에 한 컷 추가.\n"
 "△ 델릴라의 뺨이 불길에 닿는다. 비명과 함께 볼에 붉은 자국이 길게 남는다.\n"
 "\n"
 "얼굴만은 안 된다고 비는데 얼굴에 아무 일도 안 일어나서 이 대사가 헛돕니다."),

# ── 21화 ──
("나를 지켜주는 황금 펜던트는 지금 다말에게 있다",
 "이 대사를 한 줄로 교체.\n"
 "모세: 그래. 나는 사람이다.\n"
 "\n"
 "펜던트에 힘이 있으면 다말이 목숨 걸고 되찾은 이유가 물건값이 됩니다."),

("△ 왕도를 가로지르는 큰 강이 상류부터 핏빛으로 물들기 시작한다",
 "이 지문 삭제. 군중 대사는 유지.\n"
 "\n"
 "다음 화 첫 대사가 \"핏물이 솟는 건 우물뿐이오!\"라 정면으로 부딪힙니다."),

# ── 22화 ──
("급하게 왕도를 수색했으나",
 "이 대사 뒤에 한 줄 추가.\n"
 "라반: 다말은? 그년도 같이 사라진 것이냐?\n"
 "\n"
 "어제 실려 나간 딸인데 이 화에서 아무도 안 찾습니다."),

# ── 23화 ──
("△ 화려하고 넓은 침전",
 "\"△ 화려하고 넓은 침전.\" → \"△ 좁고 단단한 돌방. 두꺼운 천이 창을 가리고 있다.\"\n"
 "아래 \"부드러운 침대\" → \"낮은 나무 침상\"\n"
 "\n"
 "성소는 왕도 어느 가문도 못 당하지만 화려하진 않은 은신처로 잡아뒀습니다. 지난번에 저희가 \"초라하게 그리지 말아주세요\"라고만 적어서 생긴 일입니다."),

("사제1: 저자는 라반 가문에서 소란을 일으키고",
 "\"사제1\" → \"신관1\"\n"
 "이 화 등장인물 줄, 24화 등장인물 줄과 지문까지 네 군데."),

("네 오만함을 꺾을 벌이 수백 가지가 넘는다",
 "다음 모세 대사(\"내 사람들을 자유롭게 하라\") 앞에 한 줄 추가.\n"
 "모세: 하나만 해라. 시간 없다.\n"
 "\n"
 "모세가 정색하고 받으면 파라오와 같은 급이 됩니다. 상대 안 하는 쪽이 세 보입니다."),

("이것은 부탁이 아니다",
 "\"모세: 오해가 있는 것 같군. 이것은 부탁이 아니다.\" → \"모세: 묻는 게 아니라고 했다.\""),

# ── 24화 ──
("델릴라의 침소를 더럽힌 것도 네 술수겠지",
 "다음 모세 대사 \"정말로 약속하는 것이냐?\"를 교체.\n"
 "모세: 내가 벌인 일이 아니다. 네가 벌인 일이다.\n"
 "\n"
 "모세가 파라오 말을 믿었다가 뒤통수를 맞으면 순진한 사람이 됩니다."),

("△ 지팡이에서 황금빛 빛과 함께 모래 바람이 분다",
 "이 지문부터 \"모세가 바람을 다시 가라 앉히며\"까지를 아래로 교체.\n"
 "모세: 그래라.\n"
 "△ 모세가 돌아선다.\n"
 "△ 개구리는 저절로 걷힌다.\n"
 "\n"
 "다음 파라오 대사(\"순진한 것…\")는 그대로 둡니다. 모세가 안 놀라면 속은 사람은 파라오가 됩니다. 지팡이가 빛나는 컷은 힘이 지팡이에 있는 것처럼 보여서 뺍니다."),

("감독관: 여기서는 당신이 누구의 아내인지",
 "\"감독관\" → \"감독\"\n"
 "이 화 네 군데, 25화 두 군데."),

# ── 25화 ──
("성소 사람들도 나를 알아봐",
 "\"나를 알아봐  거야\" → \"나를 알아봐 줄 거야\""),

# ── 26화 ──
("△ 다말이 물독 마당을 향해 걸음을 옮긴다",
 "다말이 여기서 나갔는데 다음 씬에 다시 봉사관에 서 있습니다.\n"
 "\"#2. 성소 봉사관 / 낮\" → \"#2. 성소, 물독 마당 / 낮\""),

# ── 27화 ──
("모래바람이 불고 모세가 나타난다",
 "\"모래바람이 불고 모세가 나타난다\" → \"모세가 걸어 들어온다\"\n"
 "29화 \"모세가 등을 돌리고 사라진다\" → \"모세가 걸어 나간다\""),

("#2. 왕국 / 낮",
 "\"#2. 왕국 / 낮\" → \"#2. 왕궁, 파라오의 앞 / 낮\"\n"
 "28화 두 곳, 29화 두 곳 씬 헤더의 \"왕국\"도 \"왕궁\"으로."),

("왕궁 밖으로 한 발짝도 나가지 못하게 하라",
 "28화 첫 장면의 무릎 꿇리는 대목을 이 뒤로 옮겨 이 화 클리프로.\n"
 "△ 하녀들이 다말의 어깨를 눌러 무릎 꿇린다.\n"
 "델릴라: 언니, 여기선 이게 예법이야.\n"
 "28화 델릴라 대사 중 \"언니는 모르겠지만, 왕궁에는 각자의 위치에 맞는 예법이라는 게 있어…\"는 삭제.\n"
 "\n"
 "지금 클리프가 병사에게 내리는 명령이라 다음 화를 눌러야 할 이유가 약합니다."),

# ── 28화 ──
("#1. 왕국의 지하 감옥 / 밤",
 "\"#1. 왕국의 지하 감옥 / 밤\" → \"#1. 왕궁, 다말이 갇힌 방 / 밤\"\n"
 "29화 \"#2. 왕국의 지하 감옥\"도 같이. 본문의 \"지하 감옥\"·\"무거운 철문\"도 방으로.\n"
 "\n"
 "다말은 죄수가 아니라 남편을 불러들이려고 잡아둔 볼모라 왕궁 안에 둡니다. 두 화 연속 어두운 감옥이면 화면도 답답해집니다."),

("△ 흙먼지는 서서히 이로 변한다",
 "이 지문을 두 컷으로.\n"
 "△ 왕궁 마당에 흙먼지가 인다.\n"
 "△ 델릴라의 옷 속으로 이가 파고든다.\n"
 "\n"
 "흙이 벌레로 변하는 과정은 AI 영상으로 안 나옵니다."),

# ── 29화 ──
("왕국에 벌레가 들끓고 있어",
 "이 대사를 교체.\n"
 "하녀1: 왕궁이 난리야. 그런데 성 밖은 멀쩡하대. 이상하지 않아?\n"
 "다음 하녀2 대사는 유지.\n"
 "\n"
 "재앙이 나라 전체로 번지는 건 36화부터입니다. 여기서 전국이 되면 남은 재앙들이 갈 데가 없어집니다."),

("모세가 남자의 얼굴로 변신해 정체를 숨긴 것이다",
 "변신을 빼고 모세 그대로 들어오게.\n"
 "아래 \"손바닥으로 얼굴을 훔치자, 원래 얼굴이 나온다\" 컷도 삭제.\n"
 "모세 대사 \"저는 그대의 남편을 대신해 이곳에 왔습니다\" → \"데리러 왔다.\"\n"
 "\n"
 "모세는 사람이라 얼굴을 못 바꿉니다. 남편이 아내에게 남인 척 접근하는 그림이라 다말 쪽 감정도 상합니다."),

("그대의 뜻이 그렇다면 존중하겠소",
 "이 화 모세 대사가 \"그대…하겠소\" 하오체입니다. 23·27화처럼 \"너\"에 반말로."),

# ── 30화 ──
("밤하늘에 먹구름이 몰려온다",
 "\"밤하늘에\" → \"하늘에\". 씬 헤더가 \"낮\"입니다."),

("분명 저 여자가 꾸민 짓이야",
 "이 대사를 교체.\n"
 "델릴라: 하필 왜 나만! 왜 나만 이런 꼴을 당하는 거냐고!\n"
 "위 군중2 대사 \"마치 신께서 다말의 편에 서신 것처럼 보이는구나\"도 \"저 노예의 신인가?\"로.\n"
 "\n"
 "다말과 재앙을 연결 짓는 건 33화에 델릴라가 처음 알아채는 대목이라 여기선 아직 몰라야 합니다."),

("근위대장의 머리를 때린다",
 "이 지문 뒤에 한 컷 추가.\n"
 "△ 바로 옆에 선 하인의 머리 위엔 한 알도 떨어지지 않는다."),

("내 손에 피를 묻혀서라도",
 "오탈자 — 걱정마(4화), 눈을 크게 뜬다..(13화), 사과 말아요(23화), 가야해요(27화), 이중 공백(5·19·20·22·25·28화)."),
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

assert not re.search(r'<w:ins\b|<w:del\b', doc), '변경 이력이 남아 있음'
assert 'word/comments.xml' not in names and 'commentReference' not in doc, '기존 코멘트 있음'
print('원본 확인: 변경 이력 0 · 기존 코멘트 0')

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

ct = ct.replace('</Types>',
                '<Override PartName="/word/comments.xml" ContentType="application/vnd.'
                'openxmlformats-officedocument.wordprocessingml.comments+xml"/></Types>')
rels = rels.replace('</Relationships>',
                    '<Relationship Id="rIdComments1" Type="http://schemas.openxmlformats.org/'
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

zz = zipfile.ZipFile(OUT)
d2 = zz.read('word/document.xml').decode('utf-8')
p2 = [m.span() for m in re.finditer(r'<w:p[ >].*?</w:p>|<w:p/>', d2, re.S)]
assert ''.join(texts) == ''.join(''.join(re.findall(WT, d2[a:b], re.S)) for a, b in p2), '본문 변경됨'
assert len(re.findall(r'<w:comment ', zz.read('word/comments.xml').decode('utf-8'))) == len(bodies)
import xml.etree.ElementTree as ET
ET.fromstring(zz.read('word/comments.xml')); ET.fromstring(zz.read('word/document.xml'))
print(f'코멘트 {len(bodies)}개 · 본문 무변경 · 단락 {len(p2)} · XML ok')
print('WROTE', OUT)
