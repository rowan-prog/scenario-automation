# -*- coding: utf-8 -*-
"""v1/v2 비교 번역본 docx 빌더. 입력 = _merge2_cn.txt(CN 합본) + _merge_kr.txt/_merge2_newlines_kr.txt(KR 줄 사전)."""
import re, sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NOTES = {
1:("초음파 앞에 차별 몽타주 3컷 + 「오메가」 VO를 넣고, 초음파 위 VO는 삭제","v1","첫 컷(임신·세쌍둥이)이 뒤로 밀린다. 오메가는 오메가버스 단어라 다른 장르로 읽힌다. VO는 원작처럼 아예 빼는 게 제일 낫다."),
2:("「세쌍둥이 다 늑대 피가 뚜렷하다」 추가","v2","6화 클레어 「울프리스는 못 낳는다」와 맞물리는 정체 단서."),
3:("신분 설명을 속말로 옮기고, 입으로는 「그레이슨 님」 존칭","v2","신분 차가 말투에 실린다."),
4:("속말 「알파 후계자」→「귀하신 순혈」, 지문 한 줄 추가(「米兰」 오타)","무방","v2 쓰면 오타만 고친다."),
5:("(6과 한 묶음) 「그레이슨, 내가 도울게」 두 줄을 안아 올리기 앞으로 이동","v2","밀라가 먼저 응하고 그다음 안는 순서."),
6:("(5와 한 묶음)","v2",""),
7:("셔츠 찢기→손목 누르기. 끝 대사 「걱정 마. 다 들어갈 거야」→「겁내지 마, 베이비」","v1","원작 1화 끝 대사 그대로였고 광고컷 문장. v2는 어느 작품에나 있는 말."),
8:("「약 기운 탓」 삭제","무방",""),
9:("월터가 먼저 묻고 밀라가 잡아떼는 순서로 재배치. 「돈이 늑대한테서 온 걸 알면 미친다」 삭제","v2","흐름이 자연스럽다. 지운 정보는 3화 첫 줄(월터 발작)이 대신한다."),
10:("「설마 그 집 놈이냐」→「늑대 이빨 자국이냐」","v2","v1은 월터가 어느 집인지 알 길이 없는 말. v2가 원작 2화 「설마 엘프 놈은 아니겠지」 자리."),
11:("「혼혈이라도」→「늑대 피가 흐르니」","v2","미세. 다이애나가 밀라를 챙기는 결."),
12:("「천한」 첨가, 문장이 길어짐","v1","짧은 쪽."),
13:("「오늘 밤 제대로 망가뜨려 주마」 삭제, 욕으로 끝냄","v1","원작 4화 끝 대사 그대로였다. \"지금 저지른다\"가 빠져 절단면이 없어졌다."),
14:("「내 여자다 → 기어 나가」를 「꺼져 → 내 여자다」로","v1","원작 순서. 무릎 꿇는 이유가 먼저, 굴욕(기어 나가)이 마지막."),
15:("지문 한 줄 추가","무방",""),
16:("「겁내지 마」 첨가","무방","v2 써도 된다."),
17:("순서 바꾸고 「할아버지 수술비가 급했다」 삭제","v1","그 한마디가 바로 뒤 60만 제안의 방아쇠."),
18:("「할게요」 첨가 + 감정 지시 (추적 표시 없이 바꿈)","무방","v2 써도 된다."),
19:("「올라타. 네가 직접 해」→「와서 네 의무를 이행해」","v1","원작 5화 끝 대사 그대로. 5화 첫 대사 「나더러 하라며?」가 받을 말이 없어진다."),
20:("「50만」→「60만」 숫자 수정(추적 표시 없음) + 「이리 와, 붙어」→「날 즐겁게 해 봐」","숫자 v2 · 대사 v1","v1의 50만은 오류."),
21:("「안 돼! 너무 깊어」 추가(추적 표시 없음)","무방","5-1을 줄이겠다면서 자극 줄은 늘렸다."),
22:("「내 무릎에서 네가 움직이는 걸 가까이서 보겠다」→「자기, 참 엄살이네」","v1","4화 끝 「네가 직접 해」와 이어지는 줄이 끊긴다."),
23:("「이 남자한테 두근대는 내가 싫다」→「날 아끼는 건가?」","v1","저항하면서 넘어가는 문장이 그냥 묻는 문장이 됐다(원작 「우린 사는 세계가 달라」 결)."),
24:("「차가워!」 첨가, VO→OS","무방",""),
25:("「날 보호하려고?」→「차가운 거래를 위해 보호하다니」","v1","뜻이 흐리다."),
26:("「참지 마. 소리 내. 아프면 말해. 안 아프게 할게」 삭제","v1","밀라가 흔들리는 근거 줄(원작 7화 「괜찮아, 그만하자」). 5-1을 줄이려면 핸들·클랙션 동작 비트를 빼야지 이 줄이 아니다."),
27:("VO→OS 표기, 클레어 감정 지시","표기만",""),
28:("VO→OS 표기","표기만",""),
29:("월터 「그 돈 덕에 수술이 됐다」→「수술이 잘됐으니」 (추적 표시 없음)","v2","월터는 돈 출처를 모르는 게 3화 설정. v1은 모순."),
30:("「내가 준 돈이면 이 거리를 사고도 남는데 왜 신 과일이나 줍냐」 삭제 (추적 표시 없음)","v1","원작 8화 「돈이 생겼을 텐데 왜 산딸기를」 그대로인 줄. 살린다."),
31:("「설마 임신?」 앞에 「신 과일 주워 먹는 걸 보니」 붙임","무방","30을 살리면 v1."),
32:("맥박 짚고 놀라는 지문 → 배를 노려보는 지문 (추적 표시 없음)","무방","어느 쪽이든 「설마 임신했냐?」에서 끊고 이 지문은 7화 첫 줄로."),
33:("목 만지기, 월터가 목을 보는 지문 추가 (추적 표시 없음)","무방",""),
34:("VO→OS 표기","표기만",""),
35:("「내 집이 더 안전해, 의사도 있어」 삭제 (추적 표시 없음)","v1","그레이슨이 임신을 의심한다는 걸 보여주는 유일한 줄."),
36:("「순혈 알파와 울프리스의 아이」→「울프리스의 아이」 + 오타 수정","v2","v1은 밀라가 다이애나 앞에서 애아빠가 순혈 알파라고 말해 아들을 거의 지목한다."),
37:("「순혈 늑대 중에 어떻게」→「요즘 세상에 어떻게」","v2","36과 짝."),
}

def load_map():
    m={}
    for cn,kr in [("_merge_cn.txt","_merge_kr.txt"),("_merge2_newlines_cn.txt","_merge2_newlines_kr.txt")]:
        a=open(cn,encoding="utf-8").read().split("\n"); b=open(kr,encoding="utf-8").read().split("\n")
        while a and not a[-1].strip(): a.pop()
        while b and not b[-1].strip(): b.pop()
        assert len(a)==len(b),(cn,len(a),len(b))
        for x,y in zip(a,b): m.setdefault(x.strip(),y.strip())
    return m

def shade(cell,hex_):
    tcPr=cell._tc.get_or_add_tcPr(); s=OxmlElement('w:shd'); s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),hex_); tcPr.append(s)

def para(doc,text,bold=False,size=10.5,color=None,italic=False,indent=0):
    p=doc.add_paragraph(); r=p.add_run(text); r.bold=bold; r.italic=italic; r.font.size=Pt(size)
    if color: r.font.color.rgb=RGBColor.from_string(color)
    p.paragraph_format.space_after=Pt(2); p.paragraph_format.left_indent=Cm(indent); return p

def build(out):
    m=load_map(); L=open("_merge2_cn.txt",encoding="utf-8").read().split("\n")
    doc=Document(); st=doc.styles['Normal']; st.font.name='맑은 고딕'; st.element.rPr.rFonts.set(qn('w:eastAsia'),'맑은 고딕'); st.font.size=Pt(10.5)
    for s in doc.sections: s.left_margin=s.right_margin=Cm(1.5); s.top_margin=s.bottom_margin=Cm(1.5)
    para(doc,"늑대 후계자의 세쌍둥이를 임신했다 — 작가 무료 1~8화 v1 / v2 비교 번역본",True,15)
    para(doc,"읽는 법: 두 판이 같은 줄은 그냥 대본으로 흐른다. 다른 자리는 회색 번호 「차이 N」 아래 왼쪽 = v1(초고), 오른쪽 = v2(수정본). 그 밑 한 줄 = v2가 무엇을 바꿨나 / 어느 쪽을 쓰나 / 이유. 「추적 표시 없음」 = 작가가 변경 이력 없이 고친 자리(v2 파일만 보면 안 보임). 판정 요약 = 맨 뒤.",False,9.5,"555555")
    i=0
    while i<len(L):
        s=L[i].strip()
        if s.startswith("◆ 차이"):
            n=int(s.split()[-1]); j=i+1; a=[];b=[];cur=None
            while not L[j].startswith("◆끝"):
                t=L[j].strip()
                if t=="【v1】": cur=a
                elif t=="【v2】": cur=b
                else: cur.append(t)
                j+=1
            what,pick,why=NOTES[n]
            p=para(doc,f"차이 {n}",True,10,"FFFFFF"); p.paragraph_format.space_before=Pt(6)
            pPr=p._p.get_or_add_pPr(); sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:fill'),'666666'); pPr.append(sh)
            tb=doc.add_table(rows=2,cols=2); tb.style='Table Grid'
            h=tb.rows[0].cells; h[0].text="v1 (초고)"; h[1].text="v2 (수정본)"
            for c in h: c.paragraphs[0].runs[0].bold=True; c.paragraphs[0].runs[0].font.size=Pt(9.5)
            shade(h[0],"E8EEF7"); shade(h[1],"FBEBDD")
            for c,lines in zip(tb.rows[1].cells,(a,b)):
                c.text=""; first=True
                for ln in lines:
                    kr=m.get(ln,"(없음)" if ln=="(없음)" else "[미번역] "+ln)
                    pp=c.paragraphs[0] if first else c.add_paragraph(); first=False
                    r=pp.add_run(kr); r.font.size=Pt(10)
                    if ln.startswith("△"): r.font.color.rgb=RGBColor.from_string("666666")
                    pp.paragraph_format.space_after=Pt(2)
            shade(tb.rows[1].cells[0],"F3F6FB"); shade(tb.rows[1].cells[1],"FDF6EF")
            col={"v1":"1F4E9A","v2":"B4551A","무방":"555555","표기만":"555555"}.get(pick,"1F4E9A")
            p=doc.add_paragraph(); r=p.add_run("v2가 바꾼 것: "); r.bold=True; r.font.size=Pt(9.5)
            r=p.add_run(what+"   "); r.font.size=Pt(9.5)
            r=p.add_run(f"→ {pick}"); r.bold=True; r.font.size=Pt(9.5); r.font.color.rgb=RGBColor.from_string(col)
            if why: r=p.add_run("  "+why); r.font.size=Pt(9.5); r.font.color.rgb=RGBColor.from_string("444444")
            p.paragraph_format.space_after=Pt(8)
            i=j+1; continue
        if re.match(r'^(第\d+集|\d+화)',s):
            para(doc,m.get(s,s),True,13).paragraph_format.space_before=Pt(14)
        elif re.match(r'^\d+-\d+',s):
            para(doc,m.get(s,s),True,11,"333333").paragraph_format.space_before=Pt(8)
        elif s.startswith("△"):
            para(doc,m.get(s,"[미번역] "+s),False,10,"666666")
        elif s:
            para(doc,m.get(s,"[미번역] "+s))
        i+=1
    para(doc,"판정 요약",True,13).paragraph_format.space_before=Pt(16)
    v2=[k for k,v in NOTES.items() if v[1]=="v2"]; v1=[k for k,v in NOTES.items() if v[1]=="v1"]
    para(doc,f"v2 채택 ({len(v2)}곳): 차이 "+", ".join(map(str,v2))+" + 차이 20의 숫자 수정. 전부 논리·설정 오류를 잡은 자리다.")
    para(doc,f"v1 유지 ({len(v1)}곳): 차이 "+", ".join(map(str,v1))+" + 차이 20의 대사. 원작 대사 그대로였던 끝 대사(1·3·4화)와 정사 자리의 감정 근거 줄을 v2가 순한 말로 바꾸거나 지운 자리다.")
    para(doc,"나머지는 무방·표기만. 최종본 = v1 본문에 위 v2 채택분만 얹는다. 그래서 \"v1+v2\"다 — v2를 통째로 받으면 v1 유지 자리의 손실까지 같이 받는다.")
    doc.save(out); print("saved",out)

if __name__=="__main__":
    build(sys.argv[1] if len(sys.argv)>1 else "늑대 후계자의 세쌍둥이를 임신했다_작가 무료 1-8화_v1·v2 비교 번역본.docx")
