# -*- coding: utf-8 -*-
"""사용자 코멘트 docx에서 [단락 텍스트]와 [기존 코멘트+앵커]를 뽑는다."""
import io, os, re, sys, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC = r"C:\Users\Rowan\Downloads\I Chose a Slave, But He Parts the Sea_내 남편은 거지 모세_대본.docx"
OUT = r"C:\Users\Rowan\scenario-automation\projects\16_moses\03_작업파일"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

z = zipfile.ZipFile(SRC)
print('파일 목록:', [n for n in z.namelist() if 'comment' in n or n.endswith('document.xml')])

doc = z.read('word/document.xml').decode('utf-8')

# 단락 분해
paras = re.findall(r'<w:p[ >].*?</w:p>|<w:p/>', doc, re.S)
texts = []
for p in paras:
    t = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S))
    t = (t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
          .replace('&quot;', '"').replace('&apos;', "'"))
    texts.append(t)
print('단락 수:', len(texts))

with open(os.path.join(OUT, '_userdoc_paras.txt'), 'w', encoding='utf-8') as f:
    for i, t in enumerate(texts):
        f.write(f'{i}\t{t}\n')

# 코멘트 본문
cm = {}
if 'word/comments.xml' in z.namelist():
    c = z.read('word/comments.xml').decode('utf-8')
    for m in re.finditer(r'<w:comment [^>]*w:id="(\d+)"[^>]*>(.*?)</w:comment>', c, re.S):
        cid, body = m.group(1), m.group(2)
        t = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', body, re.S))
        au = re.search(r'w:author="([^"]*)"', m.group(0))
        cm[cid] = (au.group(1) if au else '', t)

# 코멘트가 걸린 단락 번호
anchor = {}
for i, p in enumerate(paras):
    for cid in re.findall(r'<w:commentRangeStart w:id="(\d+)"', p):
        anchor.setdefault(cid, i)
    for cid in re.findall(r'<w:commentReference w:id="(\d+)"', p):
        anchor.setdefault(cid, i)

print('코멘트 수:', len(cm))
with open(os.path.join(OUT, '_userdoc_comments.txt'), 'w', encoding='utf-8') as f:
    for cid in sorted(cm, key=lambda x: int(x)):
        i = anchor.get(cid, -1)
        f.write(f'--- id={cid} 단락={i} 작성자={cm[cid][0]}\n')
        f.write(f'[본문] {texts[i] if i >= 0 else ""}\n')
        f.write(f'[코멘트] {cm[cid][1]}\n\n')
print('WROTE _userdoc_paras.txt / _userdoc_comments.txt')
