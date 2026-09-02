#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
logline_lint.py — 한국어 로그라인 기계 게이트 (규격 = config/50_logline_standard.md §3 · 모델 = config/50_t1_page_exemplars.md · 코퍼스(--stats 참고용) = config/50_logline_corpus.md)

사용:
  python tools/logline_lint.py --stats                      # 코퍼스 실측(자수·문장수·물음표·대시·인명) 출력
  python tools/logline_lint.py --text "로그라인 한 줄"        # 후보 1개 판정
  python tools/logline_lint.py --file cands.txt              # 줄마다 후보 1개(빈 줄·# 주석 무시)
  python tools/logline_lint.py --file cands.md --md          # "번호. 후보 — 근거" 형식(agent 출력)에서 후보만 추출

판정 = PASS / WARN / FAIL. FAIL = 규격 밖(자수·문장수·물음표·금지어). WARN = 쇼러너 판정 의무(관계·트롭·주어·인명·라벨).
이 도구는 '세는 것'만 센다. 되감기(원관념 해독) 판정은 plain-reader(haiku)가, 7요소 판정은 logline-auditor(sonnet)가 한다.
"""
import argparse, io, os, re, statistics, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "..", "config", "50_logline_corpus.md")

# ── 규격 상수 (2026-09-02 정정 — 모델 = config/50_t1_page_exemplars.md T1 페이지 3편 실측 124·135·173자) ──
# 2026-08-27의 95자 상한은 슬롯 헤더 "70 words"를 자수로 오독 + 카탈로그 코퍼스(다른 회사 소개문·중앙값 55)를
# 길이 모델로 삼은 것 → 승인된 세 편이 전부 FAIL했다. 코퍼스 실측은 --stats 참고용으로만 남긴다.
MAX_CHARS_SPACED = 185     # 공백 포함 자수 FAIL 상한 (모델 최대 173)
WARN_CHARS_SPACED = 100    # 이 아래는 WARN — 요소가 빠졌을 가능성 (모델 최소 124)
MIN_CHARS_SPACED = 60      # FAIL 하한
MAX_SENTENCES = 3          # A 아크형 1문장 / B 오해형 3문장 · 4문장 = 줄거리
MAX_QMARK = 0              # 모델 3편 물음표·느낌표 0
MAX_NAMES = 3              # B 오해형은 관계 골격이라 3까지(엠마·애덤·벤) · A형은 0

# 금지어: 우리 반려 실물에서 나온 것 + 코퍼스 0회 어휘. (코퍼스에 있는 '운명·진실·비밀·욕망' 등은 금지 아님)
BANNED = [
    "사수", "매장하", "정조준", "각성 사이다", "사이다극", "기득권", "안목", "왕조", "증명하", "관념",
    "서사", "구조", "엔진", "컨테이너", "비트", "훅", "쾌감", "레지스터", "트롭", "클리프",
    "페이오프", "판돈", "락인", "결제", "무료런", "유료", "장편", "숏폼",
]
# 라벨어: 사건 대신 라벨을 붙인 신호 → WARN (사건으로 바꿔 쓸 것)
LABELS = ["리벤지극", "사이다", "권선징악", "복수극", "로맨스극", "판타지극", "파워판타지", "성장극", "각성극", "히든 아이덴티티"]

# 관계 명사(코퍼스 실측 빈출) — 하나도 없으면 WARN(관계가 안 보임)
RELATION = [
    "남편", "아내", "전남편", "전 남편", "전처", "전남친", "전 남자 친구", "전 남자친구", "남친", "남자친구", "여자친구", "약혼자", "약혼남", "약혼녀",
    "삼촌", "의붓", "계부", "계모", "시어머니", "시아버지", "장모", "사위", "며느리", "자매", "언니", "동생", "여동생", "형", "오빠", "쌍둥이",
    "아들", "딸", "아빠", "아버지", "엄마", "어머니", "부모", "할머니", "가족", "혈육",
    "상사", "부하", "동료", "라이벌", "숙적", "적", "절친", "친구", "스승", "교수", "학생", "보디가드", "집사", "하녀", "하인", "시녀", "청소부",
    "CEO", "회장", "억만장자", "재벌", "상속녀", "상속자", "후계자", "대통령", "왕", "왕자", "공주", "여왕", "황제", "제독", "장군", "기사",
    "마피아", "보스", "두목", "알파", "루나", "오메가", "늑대인간", "뱀파이어", "마녀", "마왕", "괴물", "용", "드래곤", "신", "저승사자", "유령",
    "신부", "신랑", "커플", "연인", "정부", "애인", "불륜", "싱글맘", "대리모", "대리 신부", "펫", "주인", "형사", "용의자", "변호사", "의사", "기자",
]
# 트롭 라벨(코퍼스 실측) — 하나도 없으면 WARN(핵심 트롭이 안 보임)
TROPE = [
    "위장 결혼", "계약 결혼", "계약결혼", "가짜 약혼", "가짜 신부", "정략결혼", "비밀 결혼", "대리 신부", "하룻밤", "동침", "회귀", "다시 태어나",
    "환생", "타임리프", "시간을 되돌리", "잠입", "정체를 숨긴", "신분을 숨기", "정체", "비밀", "복수", "배신", "불륜", "외도", "이혼",
    "억만장자", "재벌", "마피아", "늑대인간", "뱀파이어", "알파", "루나", "저주", "운명의 짝", "제물", "팔린", "팔려", "빼앗", "되찾", "집착",
    "금지된", "금기", "유혹", "목줄", "노예", "거지", "사기꾼", "누명", "감옥", "옥살이", "암살", "죽음", "죽고", "죽을", "살아남", "살리", "살려", "각성", "능력", "보인다", "보이는", "보이기", "보인 뒤", "보였다", "수명", "마지막 날", "남편이 된", "남편이라",
]
CONNECTIVE_SPLIT = re.compile(r"(?<=[.!?…])\s+|(?<=[.!?])(?=[가-힣A-Za-z\"'「])")
NAME_RE = re.compile(r"[가-힣]{2,4}(?=[은는이가을를의와과도만에게]|\s|[,.!?]|$)")


def split_sentences(t: str):
    t = t.strip()
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+|(?<=[.!?])(?=[^\s.!?])", t) if p.strip()]
    # 말줄임표·대시로 끝나는 조각은 문장으로 세지 않음
    return [p for p in parts if re.search(r"[가-힣A-Za-z0-9]", p)]


def count_names(t: str):
    """외래 인명 추정: 코퍼스 빈출 인명 패턴(2~4음절 + 조사)에서 일반명사 제외. 근사치·WARN 용도만."""
    cands = set()
    for m in re.finditer(r"([가-힣]{2,4})(?:는|은|가|이|를|을|와|과|의|에게|도)\b", t):
        w = m.group(1)
        if w in COMMON:
            continue
        # 인명 휴리스틱: 받침 없는 외래어 음절 비중·흔한 인명 종결
        if re.search(r"(아|라|나|리|이|야|린|나|엘|안|스|드|크|트|디|비|미|시|지|피|니|카|타|파|사|하|마|바|자|다|가|우|주|누|루|무|부|수|투|후|쿠|푸|츠|즈|가|나|다|라|마|바|사|아|자|차|카|타|파|하)$", w):
            cands.add(w)
    return sorted(cands)


COMMON = set("""병원비 보이 숫자 집안 눈 값 수명 좌판 은화 동전 병상 수표 서류 도장 잔치 계단 복도 마스크 산소마스크 전처 배달부 여회장 애인 병원장 새 남자 그날 그날밤 하루 오늘 며칠 그때 그해
남편 아내 여자 남자 사랑 배신 복수 비밀 정체 운명 진실 결혼 이혼 인생 세계 가족 자신 그녀 그들 우리 이야기 사람 자리 그날 그날밤 이번 과거 현재 미래 상대 상사 동료 라이벌
회장 억만장자 재벌 마피아 두목 보스 알파 루나 왕자 공주 여왕 황제 제독 장군 기사 신부 신랑 하녀 하인 시녀 집사 청소부 의사 변호사 형사 기자 교수 학생 소녀 소년 상속녀 상속자 후계자 대통령 스타 톱스타
아들 딸 엄마 아빠 어머니 아버지 언니 동생 여동생 오빠 삼촌 절친 친구 자매 쌍둥이 부모 할머니 시어머니 장모 사위 계부 의붓오빠 의붓아들 의붓언니
저택 호텔 병원 학교 회사 요트 배 섬 바다 숲 벙커 감옥 왕좌 왕관 목줄 유산 제국 도시 시카고 서울 파리 호주 뉴욕 카리브해 이태원
로맨스 스캔들 게임 미션 데이트 연애 결말 시작 선택 결정 위기 위험 유혹 집착 열정 욕망 진심 마음 기억 능력 저주 각인 표식 치료제 제물 경매장 하룻밤 사실 경우 순간 이유 대가 상황 관계 문제 모든 하나
""".split())


def check(text: str):
    t = " ".join(text.split())
    sents = split_sentences(t)
    n_sp = len(t)
    n_nosp = len(t.replace(" ", ""))
    q = t.count("?") + t.count("？")
    dash = t.count("—") + t.count(" - ")
    names = count_names(t)
    fails, warns = [], []
    if n_sp > MAX_CHARS_SPACED:
        fails.append(f"자수 {n_sp} > {MAX_CHARS_SPACED} (모델 3편 124·135·173) — 줄거리다. A형 = 처지·능력·핵심 사건·도달점 4~5절만")
    if n_sp < MIN_CHARS_SPACED:
        fails.append(f"자수 {n_sp} < {MIN_CHARS_SPACED} — 관계·사건·도달점 중 뭔가 빠졌다")
    elif n_sp < WARN_CHARS_SPACED:
        warns.append(f"자수 {n_sp} < {WARN_CHARS_SPACED} (모델 최소 124) — A형이면 최종 도달점(결국 …하는 이야기)이 있는지, B형이면 세 문장인지 확인")
    if len(sents) == 2:
        warns.append("2문장 — 정본 2형 어느 쪽도 아니다(A 아크형 1문장 / B 오해형 3문장). 주어가 바뀌지 않는지 확인")
    if t.count("!") + t.count("！") > 0:
        warns.append("느낌표 — 모델 3편은 0")
    if len(sents) > MAX_SENTENCES:
        fails.append(f"문장 {len(sents)}개 > {MAX_SENTENCES} — 줄거리 요약이다")
    if q > MAX_QMARK:
        fails.append(f"물음표 {q}개 > {MAX_QMARK}")
    hit = [b for b in BANNED if b in t]
    if hit:
        fails.append("금지어(내부 작업어·은유 동사·반려 실물): " + ", ".join(hit))
    lab = [l for l in LABELS if l in t]
    if lab:
        warns.append("장르 라벨어 — 라벨 대신 그 사건을 써라: " + ", ".join(lab))
    if not any(r in t for r in RELATION):
        warns.append("관계 명사 0 — 누구와 누구 사이 이야기인지 안 보인다 (남편/전남친의 삼촌/의붓언니의 약혼자…)")
    if not any(k in t for k in TROPE):
        warns.append("트롭 어휘 0 — 핵심 트롭(위장 결혼·회귀·하룻밤·정체·복수…)이 이름으로 안 박혀 있다")
    if len(names) > MAX_NAMES:
        warns.append(f"인명 {len(names)}개({', '.join(names)}) > {MAX_NAMES} — 역할명으로 바꿔라 (전처·회장·배달부)")
    # 주어 휴리스틱: 각 문장에 주격/주제 조사 또는 명사구 종결이 있는가
    for s in sents:
        if not re.search(r"[가-힣A-Za-z)\]」』\"']([은는이가]|께서)\s|[가-힣]\.$|[가-힣A-Za-z]+[.!?]$", s) and not re.search(r"[은는이가]\s", s):
            warns.append(f"주어가 안 보이는 문장: 「{s[:40]}…」 — 누가 하는지 명사로 박아라")
    verdict = "FAIL" if fails else ("WARN" if warns else "PASS")
    return {"text": t, "chars": n_sp, "chars_nospace": n_nosp, "sentences": len(sents), "qmark": q, "dash": dash,
            "names": names, "fails": fails, "warns": warns, "verdict": verdict}


def load_corpus():
    rows = []
    with open(CORPUS, encoding="utf-8") as f:
        in_a = False
        for line in f:
            if line.startswith("## A."):
                in_a = True; continue
            if line.startswith("## B."):
                break
            if in_a and line.startswith("|") and not line.startswith("|---") and not line.startswith("| #"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 3 and cells[2]:
                    rows.append((cells[1], cells[2]))
    return rows


def stats():
    rows = load_corpus()
    ch = [len(l) for _, l in rows]
    chn = [len(l.replace(" ", "")) for _, l in rows]
    se = [len(split_sentences(l)) for _, l in rows]
    qm = sum(1 for _, l in rows if "?" in l)
    da = sum(1 for _, l in rows if "—" in l)
    ex = sum(1 for _, l in rows if "!" in l)
    nm = [len(count_names(l)) for _, l in rows]
    rel = sum(1 for _, l in rows if any(r in l for r in RELATION))
    trp = sum(1 for _, l in rows if any(k in l for k in TROPE))
    def pct(a, p):
        a = sorted(a); return a[min(len(a) - 1, int(round(p * (len(a) - 1))))]
    print(f"코퍼스 로그라인 수: {len(rows)}")
    print(f"자수(공백 포함): 최소 {min(ch)} · 중앙값 {statistics.median(ch):.0f} · 평균 {statistics.mean(ch):.1f} · p90 {pct(ch,0.9)} · 최대 {max(ch)}")
    print(f"자수(공백 제외): 중앙값 {statistics.median(chn):.0f} · p90 {pct(chn,0.9)} · 최대 {max(chn)}")
    from collections import Counter
    c = Counter(se)
    print("문장 수 분포: " + " · ".join(f"{k}문장 {v}건({v/len(rows):.0%})" for k, v in sorted(c.items())))
    print(f"물음표 포함: {qm}건({qm/len(rows):.0%}) · 대시(—) 반전: {da}건({da/len(rows):.0%}) · 느낌표: {ex}건({ex/len(rows):.0%})")
    cn = Counter(nm)
    print("인명 수 분포(추정): " + " · ".join(f"{k}명 {v}건" for k, v in sorted(cn.items())))
    print(f"관계 명사 포함: {rel}건({rel/len(rows):.0%}) · 트롭 어휘 포함: {trp}건({trp/len(rows):.0%})")
    print("\n자수 상위 5 (상한 참고):")
    for t, l in sorted(rows, key=lambda r: -len(r[1]))[:5]:
        print(f"  {len(l):>3}자 | {t} | {l}")
    print("\n자수 하위 5 (하한 참고):")
    for t, l in sorted(rows, key=lambda r: len(r[1]))[:5]:
        print(f"  {len(l):>3}자 | {t} | {l}")


def extract_md(path, drop_reason=False):
    """'번호. 후보' 줄만 뽑는다. drop_reason=True(agent 원출력 '번호. 후보 — 근거')면 마지막 ' — ' 뒤를 버린다.
    기본값은 자르지 않는다 — P3 골격(대시 반전)이 후보 본문에 ' — '를 품기 때문."""
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^\s*\d+[.)]\s*(.+?)\s*$", line.strip())
            if not m:
                continue
            t = m.group(1)
            if drop_reason and " — " in t:
                t = t.rsplit(" — ", 1)[0]
            out.append(t.strip().strip('"“”'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--text")
    ap.add_argument("--file")
    ap.add_argument("--md", action="store_true", help="'번호. 후보' 줄만 추출 (라운드 파일)")
    ap.add_argument("--md-reasons", action="store_true", help="agent 원출력 '번호. 후보 — 근거'에서 근거를 떼고 추출")
    a = ap.parse_args()
    if a.stats:
        stats(); return
    cands = []
    if a.text:
        cands = [a.text]
    elif a.file:
        if a.md or a.md_reasons:
            cands = extract_md(a.file, drop_reason=a.md_reasons)
        else:
            with open(a.file, encoding="utf-8") as f:
                cands = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    if not cands:
        ap.print_help(); return
    tot = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for i, c in enumerate(cands, 1):
        r = check(c)
        tot[r["verdict"]] += 1
        print(f"[{i}] {r['verdict']} · {r['chars']}자/{r['sentences']}문장/?{r['qmark']}/인명{len(r['names'])}")
        print(f"    {r['text']}")
        for f_ in r["fails"]:
            print(f"    ✗ {f_}")
        for w in r["warns"]:
            print(f"    △ {w}")
    print(f"\n합계: PASS {tot['PASS']} · WARN {tot['WARN']} · FAIL {tot['FAIL']}  (규격: {MIN_CHARS_SPACED}~{MAX_CHARS_SPACED}자·목표 110~175 · A형 1문장/B형 3문장 · 물음표·느낌표 0 · 금지어 0 · 모델 = config/50_t1_page_exemplars.md)")


if __name__ == "__main__":
    main()
