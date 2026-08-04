# -*- coding: utf-8 -*-
"""작가 회수본(2차)에 검수 코멘트 주입 → _1-21화_검수코멘트_v15.docx
   - 회수본에 남아 있던 지난 라운드 코멘트 54개는 전부 제거하고 새 것만 넣는다.
   - 앵커는 단락 번호가 아니라 본문 고유 문구로 잡는다(초고가 바뀌어도 안 어긋나게).
"""
import io, os, re, sys, shutil, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC = r"C:\Users\Rowan\Downloads\I Chose a Slave, But He Parts the Sea_내 남편은 거지 모세_대본 (2).docx"
OUT = r"C:\Users\Rowan\scenario-automation\projects\16_moses\내 남편은 거지 모세_1-21화_검수코멘트_v15.docx"
AUTHOR, INITIALS, DATE = 'Rowan Lee', 'RL', '2026-08-03T00:00:00Z'
WT = r'<w:t(?:\s[^>]*)?>(.*?)</w:t>'

# (앵커 문구, 코멘트)
C = [
# ── 1화 ──
("사제: 신들의 뜻에 따라, 파라오의 아내 다말은",
 "\"사제\"를 \"신관\"으로 부탁 드립니다. 1화와 12화에 열다섯 군데입니다."),

("어서 신관을 데려와",
 "\"신관의\"로요. 의원 대신 쓰기로 한 말이라 \"의\"가 있어야 의사가 됩니다."),

("누군가 뒤에서 단검으로 그녀의 가슴을 깊숙이 찌른다",
 "등으로 바꿔주세요. 뒤에서 찌르는데 가슴이면 그림이 안 나와서요.\n"
 "아래 \"가슴에서 피를 흘린 채\", \"가슴에 박힌 단검\"도 같이요."),

("네페라에게는 황금 새장을, 다말에게는 나무 상자를 준다",
 "네페라가 아니라 델릴라입니다.\n"
 "그리고 여기서 나눠주면 다음 줄에서 다말이 황금 새장에 손을 뻗을 수가 없어요.\n"
 "△ 라반이 두 딸 앞에 황금 새장과 나무 상자를 내려놓는다."),

("스스로 지옥의 불길 속으로 걸어 들어갔을 뿐이야",
 "지옥 → 저승."),

# ── 2~3화 ──
("△ 비둘기는 부드럽게 노예들이 있는 구역으로 날아간다",
 "클리프는 비둘기가 날아올라 광장 한 바퀴 도는 데까지만.\n"
 "여기서 노예 구역에 닿으면 3화 첫 컷(군중이 팔 뻗고 비둘기가 피해 다니는)이 되감기가 됩니다. 라반 대사는 그대로 두세요."),

("하지만 신의 대언자로서 선사받은 이 지팡이를",
 "정체를 숨기는 중인데 제 입으로 대언자라고 합니다.\n"
 "모세: 나도 쉬는 새를 괴롭히고 싶진 않아. 하지만 이건 내 지팡이다."),

("언니의 신성한 연꽃을 받아 든 자가 누구인지",
 "연꽃이 남았습니다. \"언니의 새를 받아 든 자가\"로요."),

# ── 6화 ──
("△ 모세가 처음으로 희미하게 웃는다",
 "4화에 두 번, 이 화 앞에도 한 번 웃습니다. \"처음으로\"만 빼주세요."),

# ── 8화 ──
("마차에서 화관을 쓴 백발의 대신관이 내린다",
 "화관이 남았습니다. \"흰 관을 쓴\" 정도로요."),

# ── 9화 ──
("저 펜던트는 주군께서 가장 아끼시는 성물이잖아",
 "\"성물\" → \"태어날 때부터 지녀오신 물건\".\n"
 "\"인간 여인과\" → \"저 여인과\". 모세가 사람이 아닌 게 되어서요."),

("우리 인연의 증표로 간직할게요",
 "\"당신의 과거를 맡기신 거군요\"가 소리로 들으면 안 잡힙니다.\n"
 "다말: 이걸 저한테요? 평생 몸에 지니셨던 거잖아요. 무슨 일이 있어도 제가 지킬게요."),

# ── 10화 ──
("다말: 모세, 저들은 누구예요?",
 "앞 화 끝에서 장로들이 다말 앞에서 \"대언자시여!\" 했는데, 못 들은 것처럼 넘어갑니다.\n"
 "다말: 방금… 대언자라고 했어요. 당신을 그렇게 불렀어요."),

("주군께서 자리를 비우신 사이 성소에 혼란이 일고 있습니다",
 "\"혼란이 일고 있다\"로는 무슨 일인지 안 들려서요.\n"
 "장로1: 주군, 성소로 돌아오셔야 합니다. 주군 없이는 아무것도 정하지 못하고 다들 기다리고만 있습니다.\n"
 "\n"
 "그리고 성소는 초라하게 그리지 말아주세요. 왕도가 이름도 모르는데 왕도의 어느 가문도 못 당하는 곳입니다. 15화에 컷 적어뒀습니다."),

# ── 12화 ──
("△ 잠시 후, 정체를 알 수 없는 수행원들이 거대한 보물 상자들을 들고",
 "상자 뚜껑에 문양이 새겨진 컷 하나만 넣어주세요. 다음 화에서 라반이 펜던트를 알아보는 근거입니다."),

("사제: 성소에서 보내온 신성한 선물입니다",
 "여기 \"사제\"도 \"신관\"으로요. 금화 받는 장면은 그대로 두셔도 됩니다."),

("네페라: 분명 착오가 있을 겁니다. 모든 왕국민이",
 "네페라가 성소를 떠받들면 김이 빠집니다. 이 사람들은 끝까지 모세를 거지로 알아야 해서요.\n"
 "네페라: 성소? 그게 어디 붙은 데랍니까? 저런 아이한테 이런 걸 보낼 데가 어디 있다고!"),

# ── 13화 ──
("성소에서 보았던 성물에 새겨진 것과 같은 문양이",
 "라반은 성소에 가본 적이 없습니다. 예물 상자가 아직 마당에 있으니 그걸로요.\n"
 "라반: 저 문양은… 저 상자들에 새겨진 것과 같지 않으냐?\n"
 "△ 카메라가 마당에 쌓인 예물 상자로 옮겨간다. 뚜껑마다 같은 문양이 새겨져 있다.\n"
 "\n"
 "다음 화 델릴라도 같이 —\n"
 "델릴라: 어디서 훔친 게 뻔하죠. 그 상자들하고 무슨 상관이에요."),

("아론: 저들이 다말 님을 짓밟고 있어! 지금 당장 주군께 알려야 해",
 "11·12·13·14화 네 화 연속으로 모세가 화면에 없습니다. 다말 당하는 것만 네 화라 보기가 괴로워요.\n"
 "이 뒤에 인서트 두 컷만 —\n"
 "△ 성소. 말하던 모세가 문득 멈추고 왕도 쪽을 돌아본다.\n"
 "모세: …다말."),

# ── 14화 ──
("그 사람의 가문에서 대대로 내려온 성물이야",
 "\"태어날 때부터 지녀온 물건이야\"로요. 아래 라반의 \"신의 성물\"도 같이요."),

# ── 15화 ──
("세는 처음으로 내 영혼을 바라봐준 사람이야",
 "\"모세는\"이 잘렸습니다."),

("#2. 성소 / 같은 시각",
 "씬 헤더에 위치만 넣어주세요 → #2. 왕도 밖 광야, 성소 / 같은 시각"),

# ── 17화 ──
("모세: …누가 내 아내를 이렇게 만들었지?",
 "11화에서 파라오가 다말의 턱을 잡았는데 그 값을 아무도 안 받습니다.\n"
 "델릴라 자백 뒤에 한 줄만 —\n"
 "다말: …그리고 저 사람이, 제 턱을 잡았어요.\n"
 "△ 모세의 시선이 천천히 파라오에게로 옮겨간다."),

("엄정한 법정에 세워 그 죄를 심판할 것이다",
 "\"법정\" → \"내 앞에 끌어내 그 죄를 물을 것이다\" 정도로요."),

# ── 18화 ──
("△ 성소의 병사들이 델릴라와 파라오, 라반과 네페라를 타오르는 장작길 앞으로 끌고 간다",
 "다말은 불길을 끝까지 건넜는데 델릴라는 근위대가 오면서 그냥 풀려납니다. 자국 하나만 남겨주세요.\n"
 "△ 델릴라의 뺨이 불길에 닿는다. 비명과 함께 볼에 붉은 자국이 길게 남는다."),

# ── 20화 ──
("그러나 병사들은 겁먹어 시선을 피할 뿐 따라가지 않는다",
 "여기 한 줄만 얹어주세요.\n"
 "파라오: 쫓아가란 말이다!\n"
 "△ 아무도 대답하지 않는다."),

# ── 21화 ──
("모세: 나를 지켜주는 황금 펜던트는 지금 다말에게 있다",
 "이 대사만 빼주세요. 펜던트에 힘이 있으면 다말이 목숨 걸고 되찾은 이유가 물건값이 됩니다.\n"
 "\"그래. 나는 사람이다.\" 한 줄이면 됩니다."),

("△ 왕도를 가로지르는 큰 강이 상류부터 핏빛으로 물들기 시작한다",
 "이 지문만 빼주세요. 군중 대사는 그대로 둡니다.\n"
 "22화가 \"라반의 저택 우물과 델릴라 손에 닿은 물만\"으로 시작해서요."),

("△ 라반 저택의 우물이란 우물이 전부 피로 넘친다",
 "오탈자만 모았습니다 — 든실루엣 / 날린다.. (1화), 나역시 (3화), 걱정마 (4화), 대신관는 (8화), 띠을 (10화), "
 "돌아가실 어머니께 (11화), 이중 공백 세 곳 (5·19·20화)."),
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
doc = z.read('word/document.xml').decode('utf-8')
com = z.read('word/comments.xml').decode('utf-8')

# ── 0. 사용자 변경 이력 수락 (삽입 확정 · 삭제 반영) ────────
ins_n, del_n = len(re.findall(r'<w:ins\b', doc)), len(re.findall(r'<w:del\b', doc))
doc = re.sub(r'<w:del\b[^>]*/>', '', doc)
doc = re.sub(r'<w:del\b[^>]*>.*?</w:del>', '', doc, flags=re.S)
doc = re.sub(r'<w:ins\b[^>]*/>', '', doc)
doc = re.sub(r'</?w:ins\b[^>]*>', '', doc)
assert not re.search(r'<w:ins\b|<w:del\b|<w:delText', doc), '변경 이력 잔재'
print(f'변경 이력 수락: 삽입 {ins_n} · 삭제 {del_n}')

# ── 1. 지난 라운드 코멘트 전부 제거 ─────────────────────────
before = len(re.findall(r'<w:comment ', com))
doc = re.sub(r'<w:commentRangeStart[^>]*/>', '', doc)
doc = re.sub(r'<w:commentRangeEnd[^>]*/>', '', doc)
doc = re.sub(r'<w:r\b(?:(?!</w:r>).)*?<w:commentReference[^>]*/>(?:(?!</w:r>).)*?</w:r>', '', doc, flags=re.S)
com = re.sub(r'<w:comment .*</w:comment>', '', com, flags=re.S)
assert not re.search(r'commentRangeStart|commentReference', doc), '구 코멘트 잔재'
print(f'구 코멘트 제거: {before}개')

# ── 2. 앵커 찾기 ──────────────────────────────────────────
spans = [m.span() for m in re.finditer(r'<w:p[ >].*?</w:p>|<w:p/>', doc, re.S)]
texts = []
for a, b in spans:
    t = ''.join(re.findall(WT, doc[a:b], re.S))
    texts.append(t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
                  .replace('&quot;', '"').replace('&apos;', "'"))

edits, bodies, cid = [], [], 0
for anchor, text in C:
    key = anchor.rstrip('\n')
    hits = [i for i, t in enumerate(texts)
            if (key in t) and (not anchor.endswith('\n') or t.strip() == key.strip())]
    assert len(hits) == 1, f'앵커 {len(hits)}건: {anchor[:35]}'
    i = hits[0]
    a, b = spans[i]
    p = doc[a:b]
    m = re.search(r'<w:r[ >]', p)
    assert m, f'run 없음: {anchor[:35]}'
    st = f'<w:commentRangeStart w:id="{cid}"/>'
    en = (f'<w:commentRangeEnd w:id="{cid}"/><w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>'
          f'<w:commentReference w:id="{cid}"/></w:r>')
    newp = p[:m.start()] + st + p[m.start():]
    newp = newp[:newp.rindex('</w:p>')] + en + '</w:p>'
    edits.append((a, b, newp))
    bodies.append(body_xml(cid, text))
    cid += 1

for a, b, newp in sorted(edits, key=lambda x: -x[0]):
    doc = doc[:a] + newp + doc[b:]
com = com.replace('</w:comments>', ''.join(bodies) + '</w:comments>')

# ── 3. 저장 ──────────────────────────────────────────────
shutil.copyfile(SRC, OUT)
tmp = OUT + '.tmp'
zin, zout = zipfile.ZipFile(OUT), zipfile.ZipFile(OUT + '.tmp', 'w', zipfile.ZIP_DEFLATED)
for it in zin.infolist():
    d = zin.read(it.filename)
    if it.filename == 'word/document.xml':
        d = doc.encode('utf-8')
    elif it.filename == 'word/comments.xml':
        d = com.encode('utf-8')
    zout.writestr(it, d)
zout.close(); zin.close()
os.replace(tmp, OUT)
print(f'코멘트 {len(bodies)}개 주입')
print('WROTE', OUT)
