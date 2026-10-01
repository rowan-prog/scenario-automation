# 러닝타임 추정 (2026-10-01)
# 한국어 대사 음절 -> GOMS 한영 대본 비율(약 2.03음절 = 영어 1단어)로 영어 단어 환산
# -> 실제 제작작 분/단어 적용 (Billion 61분/4,622 · 매치플레이 100분/7,380 · One Night 74분/4,948)
import re, docx
# --- calibrate on GOMS KO/EN pairs
GOMS = r'C:\Users\Rowan\Documents\Codex\scenario-automation-codex\projects\23_get_off_my_ship\23_get_off_my_ship_SCRIPT_KO_EN_EP01-50_TRIM8271_v006.docx'
g = '\n'.join(p.text for p in docx.Document(GOMS).paragraphs).split('\n')
ko_syl=0; en_w=0; pairs=0
for i in range(len(g)-1):
    a=g[i]; b=g[i+1]
    m=re.match(r'^([^△:：]{1,25}?)(\s*\([^)]*\))?\s*[:：]\s*(.+)$',a)
    if m and m.group(1).strip() not in ('인물',) and re.search(r'[가-힣]',m.group(1)) and re.match(r'^[A-Z][A-Z .\'\-()]+[:：]',b):
        kt=re.sub(r'\([^)]*\)','',m.group(3)); kt=re.sub(r'【[^】]*】','',kt)
        et=b.split(':',1)[1] if ':' in b else b.split('：',1)[1]
        et=re.sub(r'\([^)]*\)','',et); et=re.sub(r'【[^】]*】','',et)
        ko_syl+=len(re.findall(r'[가-힣]',kt)); en_w+=len(re.findall(r"[A-Za-z0-9']+",et)); pairs+=1
print('GOMS pairs',pairs,'ko_syl',ko_syl,'en_words',en_w,'syl/word',round(ko_syl/en_w,3))
r=ko_syl/en_w
# --- measure Kim script
t=open(r'C:\Users\Rowan\scenario-automation\projects\37_masked_duke\37_masked_duke_writer_script_v1.md',encoding='utf-8').read().split('\n')
ep=None; data={}
spk=None
for line in t:
    m=re.match(r'^<(\d+)화>',line.strip())
    if m: ep=int(m.group(1)); data[ep]={'syl':0,'turns':0,'act':0}; spk=None; continue
    if ep is None: continue
    if not line.strip(): spk=None; continue
    m=re.match(r'^([^\t]{1,14})\t+(.*)$',line)
    if m and not line.startswith('\t'):
        name=m.group(1).strip()
        if name in ('E',) : spk=None; continue
        spk=name; data[ep]['turns']+=1; txt=m.group(2)
    elif line.startswith('\t') and spk:
        txt=line
    else:
        spk=None
        if not re.match(r'^(S#|#\d|CUT TO|\[|다시 현재|\d+화 엔딩)',line.strip()): data[ep]['act']+=1
        continue
    txt=re.sub(r'\([^)]*\)','',txt)
    data[ep]['syl']+=len(re.findall(r'[가-힣]',txt))
tot_s=sum(d['syl'] for d in data.values()); tot_t=sum(d['turns'] for d in data.values()); tot_a=sum(d['act'] for d in data.values())
print('eps',len(data),'ko_syl',tot_s,'turns',tot_t,'action lines',tot_a)
ew=tot_s/r
print('est EN words',round(ew),'words/turn',round(ew/tot_t,1))
for spw,lab in ((0.792,'Billion'),(0.813,'Matchplay'),(0.897,'OneNight')):
    print(lab,'rate ->',round(ew*spw/60,1),'min')
for spt,lab in ((61*60/539,'Billion'),(74*60/479,'OneNight')):
    print(lab,'turn-rate ->',round(tot_t*spt/60,1),'min')
free=[data[i] for i in range(1,11)]
fs=sum(d['syl'] for d in free); ft=sum(d['turns'] for d in free)
print('free1-10 syl',fs,'turns',ft,'EN',round(fs/r),'min@0.85',round(fs/r*0.85/60,1))
for i in sorted(data):
    d=data[i]; print(i,d['syl'],d['turns'],d['act'],round(d['syl']/r*0.85,0),'s', sep='\t')
