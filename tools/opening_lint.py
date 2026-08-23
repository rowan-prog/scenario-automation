"""
opening_lint.py — 회차 오프닝 게이트 기계 검사
LLM 판단 0. 회차별 개별 판정만 낸다. 스트릭 유예 없음 — 한 화 한 화가 따로 팔린다.

배경 (2026-08-23 — TITAN BORN / The Lost Wolfless Mate IG 실측 x 원문 대본 대조):
같은 작품 안에서 회차별 조회가 4.7배(LWM 10.1만~47.3만) / 19배(TITAN 4.1만~76.4만)
갈렸다. 각 화의 첫 컷을 조회 순위와 대조한 결과:
  - A/B/C에 걸린 화가 상위 3위에 든 적 = 두 작품 통틀어 0건
  - LWM: 최하위 3화(10.1/10.1/10.7만) 전부 FLAG · 최상위 3화(47.3/44.9/42.8만) 전부 pass
  - TITAN(EP1-8 · 8/22 사용자 재수집): 1·2·3위 EP6(76.4만)/EP8(15.1만)/EP2(8.6만)
    전부 pass · 꼴찌 EP1(4.1만) FLAG · 6위 EP4(6.8만) FLAG
통과가 히트를 보장하지는 않는다(pass인데 하위인 화 있음). 필요조건이다 —
이 게이트는 "터뜨려라"가 아니라 "죽이지 마라"만 센다.

  A. 무인 / 주인공 부재
     첫 컷에 주인공이 없다. 단 그 화가 앞 화와 물리적으로 연속이면(헤더 CONTINUOUS
     또는 직전 화와 같은 공간) 면제 — 주인공은 이미 프레임 안에 서 있다.
     실측: LWM EP4 INSERT 여관 외경(10.1만·최저) · EP9 거실+빌런 소개(10.7만)
           TITAN EP1 全景 산정상(4.1만·8화 중 꼴찌) · EP4 신상→관중석 전경(6.8만)
  B. 리셋 오프닝
     첫 컷이 기상·도착·이동이다(가해 동작 없이). 앞 화를 끊고 무대를 다시 깐다.
     실측: LWM EP2 "눈을 뜬다"(20.1만) · EP6 "아침 햇살, 깬다"(21.0만) = 중위 주저앉음
  C. 사후 정적
     첫 컷에 가해 동작이 하나도 없고 정적 동사만 있다(간호·정리·응시·대기).
     실측: LWM EP8 "린 부인 상처를 지혈한다"(10.1만·최저)

  통과형 = 첫 컷이 "앞 화가 끊긴 그 동작의 다음 프레임"
     LWM EP3 반지를 집어 코에 댄다(47.3만 1위) · EP5 젖은 구두에서 틸트업(44.9만 2위)
     EP11 현관에서 거실로 끌려 들어온다(42.8만 3위) · TITAN EP6 창이 가슴에(76.4만 1위)

주의 1 — 워밍업 '길이'는 변수가 아니다. LWM EP1은 첫 대사까지 무성 컷 9개인데 4위,
        EP8은 1개인데 최저다. 세는 것은 컷 수가 아니라 첫 컷의 내용이다.
주의 2 — FLAG = 자동 실패가 아니라 쇼러너 판정 의무 항목. 단 1화 FLAG는 예외 없다
        (TITAN EP1 = 全景으로 열고 8화 중 꼴찌 · LWM EP1 = 빈 지하실 2컷으로 열고
         1위를 EP3에 내줬다. 1화 첫 컷 = S0 최고 가중치).

usage: python tools/opening_lint.py <script.md|.txt> [--protagonist NAME] [--window 3] [--quiet]
       지원 회차 헤더 = EP01 / 제1화 / 1화 / 第1集 / 第一集   (지문 = 행 첫머리 △)
"""
import sys, io, re
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

CN_NUM = "一二三四五六七八九十百零两"
EP_PATS = [
    re.compile(r"^\s*EP\s*0*(\d+)\b"),
    re.compile(r"^\s*#+\s*EP\s*0*(\d+)\b"),
    re.compile(r"^\s*제\s*0*(\d+)\s*화\b"),
    re.compile(r"^\s*0*(\d+)\s*화\s*$"),
    re.compile(r"^\s*第\s*0*(\d+)\s*集\s*$"),
    re.compile(r"^\s*第\s*([" + CN_NUM + r"]+)\s*集\s*$"),
]


def cn2int(s):
    if s.isdigit():
        return int(s)
    d = {c: i for i, c in enumerate("零一二三四五六七八九", 0)}
    d["两"] = 2
    if s == "十":
        return 10
    if "十" in s:
        a, _, b = s.partition("十")
        return (d.get(a, 1) if a else 1) * 10 + (d.get(b, 0) if b else 0)
    return sum(d.get(c, 0) for c in s) if s else 0


def ep_num(line):
    for p in EP_PATS:
        m = p.match(line)
        if m:
            try:
                return cn2int(m.group(1))
            except Exception:
                return None
    return None


DELTA = re.compile(r"^\s*[△▲]")
CAST = re.compile(r"(?:CAST|出场人物|등장인물|CHARACTERS)\s*[:：]\s*(.+)", re.I)
SPEAKER = re.compile(r"^\s*([^\s△▲\[\]:：][^:：\[\]]{0,38}?)\s*[:：]\s*")
SCENE_HD = re.compile(r"^\s*\d+[-–]\d+\s")
NOISE = re.compile(r"^\s*(\[|CAMERA|SFX|INSERT|CUT|FADE|END|Hard Cut|BGM)", re.I)

ESTABLISH = re.compile(
    r"\b(INSERT|ESTABLISHING|AERIAL|DRONE|SKYLINE|WIDE SHOT)\b"
    r"|全景|远景|航拍|空镜"
    r"|외경|전경|풍경|인서트", re.I)

RESET = re.compile(
    r"\b(wakes?|awakens?|opens? (?:her|his|their) eyes|gets? out of bed|arrives?|pulls? up|"
    r"walks? in(?:to)?|enters?|steps? (?:in|out)|morning light|the next (?:day|morning))\b"
    r"|睁开眼|醒来|走进|走入|来到|抵达|下车|清晨|次日"
    r"|눈을 뜨|잠에서|일어난다|들어선다|도착한", re.I)

FORCE = re.compile(
    r"\b(grabs?|grips?|drags?|dragging|shoves?|throws?|slams?|hurls?|kicks?|punches?|strikes?|hits?|"
    r"chokes?|choking|pins?|points?|aims?|rips?|tears?|yanks?|forces?|crushes?|smashes?|swings?|"
    r"lunges?|charges?|stabs?|slaps?|whips?|bursts? in|kneels? on|steps? on|blocks?|catches?|"
    r"snatch\w*|pushes?|pulls?|breaks?|shatters?|wrenches?|jerks?|crouches?)\b"
    r"|抓住|掐住|拽|拖|扑向|砸|踹|踢|打飞|刺|贯穿|挥|甩"
    r"|夺过|按住|撞|劈|捏起|冲向|钉|拔出|摔|架住|扇|掳"
    r"|붙잡|움켰|끌어|끌고|밀치|던지|내리친|겨눈|겨누"
    r"|찌르|짓밟|후려|잡아채|뿌리치|틀어막|박아|찍어", re.I)

STATIC = re.compile(
    r"\b(presses a towel|bandag\w+|tends?|nurses?|wipes?|cleans?|folds?|sits? (?:on|down|by)|"
    r"stands? (?:frozen|still|there)|watches?|stares? (?:at|into)|looks? (?:at|out|down)|"
    r"lies? (?:on|in)|sleeps?|waits?|remembers?|thinks?)\b"
    r"|包扎|擦拭|守着|坐在|站着|望着|看着|躺在|等待|回忆"
    r"|지혈|닦아|앉아|서 있|바라본|지켜본|누워|기다린", re.I)


META_NAME = re.compile(r"^(Characters?|Cast|Note|EP\d|S#|Title|Logline|Setting|출연|등장인물|人物)", re.I)


def strip_tone(name):
    return re.sub(r"[（(].*?[)）]", "", name).strip()


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(1)
    path = a[0]
    window = int(a[a.index("--window") + 1]) if "--window" in a else 3
    forced = a[a.index("--protagonist") + 1] if "--protagonist" in a else None
    quiet = "--quiet" in a
    lines = open(path, encoding="utf-8", errors="ignore").read().replace("\r\n", "\n").split("\n")

    eps, ep_hdr, cur = {}, {}, None
    for ln in lines:
        raw = ln.replace("\\", "")            # 이스케이프된 마크다운(\-\-) 정리
        n = ep_num(raw.strip().lstrip("#").strip())
        if n is not None:
            if n not in eps:
                eps[n] = []
                ep_hdr[n] = raw
            cur = n
            continue
        if cur is not None:
            eps[cur].append(raw)
    if not eps:
        print("회차 헤더를 못 찾았다 (EP01 / 제1화 / 1화 / 第1集 형식 지원)")
        sys.exit(2)

    spk = Counter()
    for body in eps.values():
        for ln in body:
            if DELTA.match(ln) or NOISE.match(ln) or SCENE_HD.match(ln):
                continue
            m = SPEAKER.match(ln)
            if m:
                nm = strip_tone(m.group(1))
                if 0 < len(nm) <= 20 and not META_NAME.match(nm):
                    spk[nm] += 1
    protagonist = forced or (spk.most_common(1)[0][0] if spk else None)
    roster = [n for n, c in spk.items() if c >= 2]

    print("=" * 66)
    print("opening_lint :: " + path)
    print("=" * 66)
    print("  회차 %d개 · 주인공(최빈 화자) = %s · 판정창 = 첫 %d컷\n" % (len(eps), protagonist, window))

    rows, flagged = [], 0
    prev_venue = None
    for n in sorted(eps):
        body = [l for l in eps[n] if l.strip()]
        hdr = ep_hdr.get(n, "")
        for l in body[:3]:
            if SCENE_HD.match(l) or re.search(r"(INT\.|EXT\.|INT ?/|EXT ?/|日 ?内|日 ?外|夜 ?内|夜 ?外)", l):
                hdr = hdr + " " + l
                break
        vsrc = re.split(r"(?:CAST|등장인물|出场人物)\s*[:：]", hdr, 1)[0]
        vsrc = re.sub(r"[·・]?\s*Continuous", "", vsrc, flags=re.I)
        venue = re.sub(r"[^A-Za-z一-鿿가-힣]+", "", vsrc)[-30:]
        deltas = [l for l in body if DELTA.match(l)][:window]
        cut1 = deltas[0] if deltas else ""

        # 연속성: 헤더 CONTINUOUS 마커 또는 직전 화와 같은 공간
        cont = bool(re.search(r"CONTINUOUS|연속", hdr, re.I))
        if not cont and prev_venue and venue and venue == prev_venue:
            cont = True
        prev_venue = venue or prev_venue

        c1 = cut1.lower()
        prot_l = (protagonist or "").lower()
        has_prot_cut1 = bool(prot_l and prot_l in c1)
        present = {nm for nm in roster if nm and nm.lower() in c1}

        f = []
        if not has_prot_cut1 and not cont:
            f.append("A무인/주인공부재")
        if RESET.search(cut1) and not FORCE.search(cut1):
            f.append("B리셋")
        if STATIC.search(cut1) and not FORCE.search(cut1):
            f.append("C사후정적")
        if f:
            flagged += 1
        rows.append((n, f, len(present), has_prot_cut1, cont, cut1[:80]))

    for n, f, np_, hp, cont, first in rows:
        if quiet and not f:
            continue
        mark = "FLAG " + "+".join(f) if f else "pass"
        print("  EP%-3d [%-26s] 주인공%s 연속%s  %s" % (n, mark, "O" if hp else "X", "O" if cont else "X", first))

    verdict = "PASS" if flagged == 0 else "FLAG (해당 화 오프닝 재설계 — 유예 없음)"
    print("\n[SUMMARY]  FLAG %d/%d화  => %s" % (flagged, len(eps), verdict))
    print("  판정 = 첫 컷이 '앞 화가 끊긴 그 동작의 다음 프레임'인가. 아니면 그 화는 하위권으로 간다.")


if __name__ == "__main__":
    main()
