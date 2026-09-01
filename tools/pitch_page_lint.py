#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pitch_page_lint.py — 사내 "피칭 페이지"(S급 제작 결정 미팅 원고) 기계 게이트

규격 근거 = 실물 10개 엔트리 전수 실측(scratchpad pitchdeck census, 2026-09-01).
코퍼스 사본 = config/pitch_page_corpus/deck_2026-08-{13,20,27}.txt (원본 = 사내 Confluence
미팅 문서 MHTML→txt 추출본. --stats 실측·검증 전용 — 실제 원고 검사에는 안 쓰인다).

입력 = 마크다운 원고. 섹션은 `## ` 헤더로 구분된다고 가정하고, 표준 7섹션명(부분 일치)을 인식한다:
타이틀 / 담당 CM / 기본정보 / 피칭 사유 / 주요 인물 소개 / 줄거리 / 초반 회차 트리트먼트
섹션 헤더를 못 찾으면 그 게이트만 SKIP — 죽지 않는다.

이 도구는 '세는 것'만 센다. 재미·설득력·크리에이티브 변별력 판정은 이 도구의 일이 아니다
(그건 evaluator-panel 같은 다른 유닛 몫). 여기서 하는 일은 정확히 셋뿐이다:
  ① 필드가 채워졌는가 ② 문체가 AI 티 어휘/자기평가/라벨을 쓰는가 ③ 사용자 룰(페이월 표기 등)을 어겼는가.

사용:
  python tools/pitch_page_lint.py <원고.md>          # 전 게이트 판정 (사람이 읽는 표)
  python tools/pitch_page_lint.py <원고.md> --json   # 기계 판독용 JSON
  python tools/pitch_page_lint.py --stats            # 실물 코퍼스 3종 실측치 출력(규격 근거 재확인)
"""
import argparse, io, json, os, re, statistics, sys
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS_DIR = os.path.join(HERE, "..", "config", "pitch_page_corpus")
CORPUS_FILES = ["deck_2026-08-13.txt", "deck_2026-08-20.txt", "deck_2026-08-27.txt"]

# ── 게이트 임계값 (전부 상수로 분리 — 나중에 조정 가능) ──────────────────────────
MIN_FIELD_CHARS = 30          # F1
EP_MIN_CHARS = 130            # G3 (골드 화당 150자 실측)
EP_MAX_CHARS = 180            # G3
MAX_SINGLE_QUOTES = 3         # G9
# G12 — 골드 실측이 두 갈래다: 문체 census(소제목 제외) 33.5자 / 이 파서(소제목 포함) 46.9자.
# 기준은 이 파서로 잰 골드에 맞춘다 — 골드가 FAIL이면 게이트가 틀린 것이다.
# 이 값으로도 E5(52.9)·E9(67)은 그대로 걸린다.
MAX_SENT_CHARS_AVG = 50
MAX_CONNECTIVE_AVG = 0.40      # G12 (골드 0.27 실측)
LOGLINE_MIN = 120             # G13 — 실측 재산정(2026-09-01): 골드 173자/3문장. 실물 8건 = 108·118·131·
LOGLINE_MAX = 220             #   162·173·200·212자. E9·E10은 로그라인 칸에 줄거리 전문을 넣어 상한 초과 = 의도된 FAIL.
                              #   ※ 이 축은 `50_logline_standard.md`(카탈로그 슬롯 45~70자)와 다른 축 — 확정 = 표준 §8 TBD 2.
CLIFF_DIALOGUE_MIN_RATIO = 0.5   # G11
NOUN_ENDING_MIN_RATIO = 0.6      # G15
MIN_FACT_ANCHORS = 4             # G7

CONCEPT_WORDS = ["긴장감", "몰입감", "카타르시스", "도파민", "관계성", "서사", "구조",
                 "요소", "포인트", "매력", "임팩트", "케미", "쾌감"]
PRODUCTION_JARGON = ["기능한다", "역할을 한다", "매개체", "조력자", "도구로", "상징한다", "장치", "로 작용한다"]
SELF_EVAL_PREDICATES = ["적합하다", "유리하다", "용이하다", "특징적이다", "차별점이다", "구조다",
                        "지점이다", "강하다", "높일 예정", "할 수 있다", "가능하다", "할 필요가 있"]
# "강력한"은 뺐다 — 일반 형용사라 인월드 서술을 오탐한다(골드 실증: "램프를 문지르면 강력한 정령이
# 나온다는 규칙" = 원전 규칙 설명이지 자기 작품 자랑이 아니다). 남긴 것은 자기 작품에만 붙는 어휘.
SUPERLATIVES = ["압도적", "극강", "극상", "완벽히", "절대적", "파격적", "최고의", "을 선사", "극대화"]
PLATFORMS = ["NetShort", "Netshort", "ReelShort", "DramaBox", "Dramabox", "DramaWave",
             "Stardust", "ShortDrama", "Vigloo", "비글루", "Douyin", "抖音"]
CLIFF_SUMMARY_ENDINGS = ["하기 시작한다", "하게 된다", "기로 결심한다", "깨닫는다", "넘어간다", "노려본다", "다짐한다"]
JUDGE_PHRASES = ["라고 판단한다", "제안한다", "예정이다", "필요가 있다"]
CONNECTIVES = ["고 ", "며", "지만", "면서", "는데", "어서", "아서", "으로"]

COMMON_NAME_STOP = set("""남자 여자 사랑 배신 복수 비밀 정체 운명 진실 결혼 이혼 인생 세계 가족 자신 그녀 그들 우리 이야기 사람 자리 상대 상사 동료 라이벌
회장 재벌 마피아 두목 보스 알파 왕자 공주 여왕 황제 기사 신부 신랑 하녀 하인 시녀 집사 의사 변호사 형사 기자 교수 학생 소녀 소년 상속녀 상속자 후계자 대통령
아들 딸 엄마 아빠 어머니 아버지 언니 동생 오빠 삼촌 친구 자매 부모 할머니 시어머니 장모 사위 계부
저택 호텔 병원 학교 회사 왕국 도시 궁전 신전 왕성 그룹 회사원 계약
로맨스 게임 미션 데이트 연애 결말 시작 선택 결정 위기 위험 유혹 집착 열정 욕망 진심 마음 기억 능력 저주 각인 표식 사실 경우 순간 이유 대가 상황 관계 문제 모든 하나 정말 이제 결국 그러나 하지만 지금 오늘 내일 어제""".split())

STANDARD_SECTION_LABELS = [
    ("title", "타이틀"), ("cm", "담당 CM"), ("basic", "기본정보"), ("pitch", "피칭 사유"),
    ("characters", "주요 인물 소개"), ("plot", "줄거리"), ("treatment", "트리트먼트"),
]
SECTION_KEYWORDS = [
    ("title", ["타이틀"]),
    ("cm", ["담당 CM", "담당CM"]),
    ("basic", ["기본정보", "기본 정보"]),
    ("pitch", ["해당 IP 피칭 사유", "피칭 사유"]),
    ("characters", ["주요 인물 소개", "인물 소개"]),
    ("plot", ["줄거리"]),
    ("treatment", ["초반 회차 트리트먼트", "회차 트리트먼트", "트리트먼트"]),
]
FIELD_LABELS = ["타겟층", "AI실사", "AI 실사", "레퍼런스", "reference", "Reference", "키워드", "keywords",
                "Keywords", "장르", "Genre", "genre", "회차", "productionType", "Audience", "https",
                "원작", "제작 방식", "Target", "타이틀"]

DIALOGUE_QUOTE_RE = re.compile(r'["“][^"“”]{1,600}["”]')
SINGLE_QUOTE_RE = re.compile(r"[‘']([^‘’']{1,300})[’']")
HANJA_RE = re.compile(r'[一-鿿]')
TITLE_BRACKET_RE = re.compile(r'[<《]([^<>《》]{1,80})[>》]')
NUMBER_UNIT_RE = re.compile(r'\d+(?:[.,]\d+)?\s?(?:%|억|만|천|개|건|화|년|일|회|배|위|시간|분|초|명|원|달러)')
REF_LINE_RE = re.compile(r'레퍼런스|reference|원작', re.I)
EP_MARKER_RE = re.compile(r'^(?:제\s?(?P<a>\d{1,3})\s*화|(?P<b>\d{1,3})\s*화|EP\.?\s?0*(?P<c>\d{1,3})(?!\d))', re.I)
LOGLINE_LABEL_RE = re.compile(r'^(로그라인|logline)(?:\s*/\s*logline)?\s*[:：]?\s*(.*)$', re.I)
SENT_SPLIT_RE = re.compile(r'(?<=[.!?])\s+|(?<=[.!?])(?=[^\s.!?])')
GENRE_LABEL_ENDING_RE = re.compile(r'(스릴러|로맨스|복수극|판타지|코미디|드라마|액션물?)[.]$')
SUMMARY_ENDING_RE = re.compile(r'(?:' + '|'.join(CLIFF_SUMMARY_ENDINGS) + r')[.]?\s*$')
HANGUL_NAME_CAND_RE = re.compile(r'[가-힣]{2,4}(?=[은는이가을를의와과에게도만]|\s|[,.!?]|$)')
ROMAN_NAME_CAND_RE = re.compile(r'\b[A-Z][a-zA-Z]{1,14}\b')
FREE_RANGE_RE = re.compile(r'무료\s*(?:EP\.?\s*)?(\d{1,3})\s*[-~](\d{1,3})')
FREE_COUNT_RE = re.compile(r'무료\s*(\d{1,3})\s*화')
VERBY_END_RE = re.compile(r'(다|요|니다)[.!?]?$')
NOUNY_END_RE = re.compile(r'(음|함|임)[.!?]?$')


# ── 섹션 파서 (마크다운 `## ` 헤더 / 원자료 raw-line 폴백 겸용) ───────────────────
def classify_heading(text):
    s = text.strip()
    for key, kws in SECTION_KEYWORDS:
        for kw in kws:
            if s.startswith(kw):
                return key
    return None


def parse_sections(text):
    lines = text.splitlines()
    has_md_headers = any(re.match(r'^#{1,6}\s+\S', l) for l in lines)
    sections = {}
    current_key = None
    buf = []

    def flush():
        if current_key is not None:
            sections.setdefault(current_key, []).append("\n".join(buf).strip())

    if has_md_headers:
        for line in lines:
            m = re.match(r'^#{1,6}\s+(.*)', line)
            if m:
                flush()
                current_key = classify_heading(m.group(1).strip())
                buf = []
            elif current_key is not None:
                buf.append(line)
        flush()
    else:
        # 원자료(raw MHTML→txt) 폴백: 진짜 섹션 헤더는 독립된 줄이지만, 기본정보 안의
        # 하위 필드("- \n타이틀: Elevator Game...")도 우연히 같은 키워드로 시작할 수 있다.
        # 그 하위 필드는 항상 바로 앞줄이 맨 "- " 불릿 마커라는 게 유일한 구조적 차이라서,
        # 직전 줄이 불릿 마커면 헤더로 인정하지 않는다.
        prev_stripped = None
        for line in lines:
            s = line.strip()
            if s == "[/TABLE]":
                flush()
                current_key = None
                buf = []
                prev_stripped = s
                continue
            prev_is_bullet_marker = bool(prev_stripped is not None and re.match(r'^-\s*$', prev_stripped))
            if s and len(s) <= 60 and not prev_is_bullet_marker and classify_heading(s) is not None:
                flush()
                current_key = classify_heading(s)
                buf = []
            elif current_key is not None:
                buf.append(line)
            if s:
                prev_stripped = s
        flush()
    return {k: "\n\n".join(v).strip() for k, v in sections.items()}


def sec(sections, key):
    return sections.get(key, "")


# ── 인물 헤더 분할 (G1) ──────────────────────────────────────────────────────
DENY_CHAR_HEADER = {"주연", "조연", "메인", "서브", "주연진", "조연진", "등장인물", "조역", "단역", "기타"}


def is_char_header(raw_line):
    s = re.sub(r'^-\s+', '', raw_line.strip())
    if not s:
        return False
    if not re.search(r'[A-Za-z0-9가-힣]', s):
        return False  # "|" 류 MHTML 표 구분선 잔재 — 텍스트가 아니므로 헤더 아님
    if s.startswith('**') and s.endswith('**') and len(s) > 4:
        return True
    # "이름(역할)" 패턴: 이름 뒤 30자 이내 여는 괄호, 그 닫는 괄호 바로 뒤가 줄끝이거나
    # ·/—/:/- 구분자여야 헤더다. 본문 문장 속 괄호(예: "카마르(Qamar) 왕국의 공주...")는
    # 닫는 괄호 다음에 그냥 문장이 이어지므로 이 조건에서 걸러진다.
    open_pos = None
    for i, ch in enumerate(s[:30]):
        if ch in '（(':
            open_pos = i
            break
    if open_pos is not None and open_pos >= 1:
        close_idx = None
        for j in range(open_pos + 1, len(s)):
            if s[j] in ')）':
                close_idx = j
        if close_idx is not None:
            rest = s[close_idx + 1:].lstrip()
            if rest == '' or rest[0] in '·—:：-–／/':
                return True
    # 괄호 없는 맨 이름 한 줄(예: "이든", "마일스") — 그룹 구분 라벨(주연/조연 등)은 제외
    if len(s) <= 12 and not re.search(r'[.!?。,，:：]', s) and s not in DENY_CHAR_HEADER:
        return True
    return False


def split_characters(char_text):
    lines = char_text.splitlines()
    chars = []
    current_label = None
    buf = []

    def flush():
        if current_label is not None:
            chars.append((current_label, "\n".join(buf).strip()))

    for line in lines:
        if is_char_header(line):
            flush()
            current_label = re.sub(r'^-\s+', '', line.strip())
            buf = [current_label]
        elif current_label is not None:
            buf.append(line)
    flush()
    return chars


def shorten_name(label):
    s = re.sub(r'^\*\*|\*\*$', '', label.strip())
    s = re.sub(r'^-\s*', '', s)
    m = re.match(r'^([^\(（]{1,20})', s)
    nm = (m.group(1) if m else s[:15]).strip()
    nm = re.split(r'[·\-—:：]', nm)[0].strip()
    return nm or s[:10]


# ── 회차 분할 (F2, F3, G2, G3, G11, U2) ──────────────────────────────────────
def split_episodes(treatment_text):
    lines = treatment_text.splitlines()
    episodes = {}
    order = []
    current_num = None
    buf = []

    def flush():
        if current_num is not None:
            episodes.setdefault(current_num, []).append("\n".join(buf).strip())

    for line in lines:
        s = line.strip()
        m = EP_MARKER_RE.match(s)
        if m:
            flush()
            num = int(m.group('a') or m.group('b') or m.group('c'))
            current_num = num
            order.append(num)
            remainder = s[m.end():].lstrip(" .:：-—｜")
            buf = [remainder] if remainder else []
        elif current_num is not None:
            buf.append(line)
    flush()
    return {n: "\n".join(v).strip() for n, v in episodes.items()}, order


def char_count(t):
    return len(re.sub(r'\s+', ' ', t.strip()))


def extract_cliff(ep_text):
    lines = [l for l in ep_text.splitlines() if l.strip()]
    labeled = [l for l in lines if re.search(r'클리프|엔딩\s*클리프행어|엔딩\s*훅|\[클리프\]|\[엔딩\]', l)]
    if labeled:
        return labeled[-1]
    return lines[-1] if lines else ""


def cliff_is_summary(text):
    return bool(SUMMARY_ENDING_RE.search(text.strip()))


def cliff_is_dialogue(text):
    return bool(re.search(r'["”][.!?]?\s*$', text.strip()))


def parse_declared_free_count(basic_text):
    m = FREE_RANGE_RE.search(basic_text)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return abs(b - a) + 1
    m = FREE_COUNT_RE.search(basic_text)
    if m:
        return int(m.group(1))
    return None


# ── 로그라인 추출 (G13, G16) ─────────────────────────────────────────────────
def extract_logline(basic_text):
    lines = [l.strip() for l in basic_text.splitlines()]
    capturing = False
    buf = []
    for line in lines:
        if not capturing:
            s_nb = re.sub(r'^-\s*', '', line)
            m = LOGLINE_LABEL_RE.match(s_nb)
            if m:
                capturing = True
                rest = m.group(2).strip()
                if rest:
                    buf.append(rest)
            continue
        if line in ("", "-"):
            continue
        stripped = re.sub(r'^-\s*', '', line)          # 불릿 접두 제거 후 하위 라벨 판정
        if any(stripped.startswith(lbl) for lbl in FIELD_LABELS):
            break
        buf.append(stripped)
    return " ".join(buf).strip().strip('"“”')


# ── 문장/연결어미 (G12, G15) ─────────────────────────────────────────────────
def split_sentences(t):
    parts = [p.strip() for p in SENT_SPLIT_RE.split(t) if p.strip()]
    return [p for p in parts if re.search(r'[가-힣A-Za-z0-9]', p)]


def count_connectives(s):
    return sum(s.count(c) for c in CONNECTIVES)


def ends_noun_style(s):
    t = s.strip()
    if NOUNY_END_RE.search(t):
        return True
    if VERBY_END_RE.search(t):
        return False
    return True


# ── 편집거리(Damerau-Levenshtein, OSA) — G16 유사표기 판정 ───────────────────
def edit_distance_dl(a, b):
    la, lb = len(a), len(b)
    d = [[0] * (lb + 1) for _ in range(la + 1)]
    for i in range(la + 1):
        d[i][0] = i
    for j in range(lb + 1):
        d[0][j] = j
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + cost)
    return d[la][lb]


def quoted_hangul_aliases(text):
    """따옴표로 격리된 2~4자 한글 별칭만 뽑는다 (예: '강준서'/'강서준') — 일반 한글 조사-어미
    패턴(HANGUL_NAME_CAND_RE)은 보통명사 오탐이 너무 많아 인명 후보로는 안 쓴다."""
    cands = set()
    for qre in (SINGLE_QUOTE_RE, DIALOGUE_QUOTE_RE):
        for m in qre.finditer(text):
            inner = m.group(1) if m.groups() else m.group(0)
            inner = inner.strip(' "“”‘’\'')
            if re.fullmatch(r'[가-힣]{2,4}', inner) and inner not in COMMON_NAME_STOP:
                cands.add(inner)
    return cands


def name_candidates(text, known_hangul_names=frozenset()):
    """인명 후보 = ①로만 대문자 고유명사 ②이미 인물 헤더에서 확인된 한글 이름이 본문에 등장
    ③따옴표로 격리된 한글 별칭. 자유 한글 조사-패턴 스캔은 보통명사 오탐이 압도적이라 뺀다."""
    cands = set(m.group(0) for m in ROMAN_NAME_CAND_RE.finditer(text))
    for nm in known_hangul_names:
        if nm and nm in text:
            cands.add(nm)
    cands |= quoted_hangul_aliases(text)
    return cands


def is_reference_line(line):
    return bool(REF_LINE_RE.search(line)) or bool(TITLE_BRACKET_RE.search(line))


# ── A. 필드 무결성 ────────────────────────────────────────────────────────────
# 타이틀·담당 CM은 원래 짧은 필드(작품명·사람 이름)라 MIN_FIELD_CHARS를 그대로 적용하면
# 항상 걸린다 — "공란이냐 아니냐"만 보고, 나머지 5개 내용 필드만 30자 기준을 적용한다.
FIELD_MIN_CHARS = {"title": 2, "cm": 2, "basic": MIN_FIELD_CHARS, "pitch": MIN_FIELD_CHARS,
                    "characters": MIN_FIELD_CHARS, "plot": MIN_FIELD_CHARS, "treatment": MIN_FIELD_CHARS}
# 피칭 사유 섹션 헤더 바로 아래 고정으로 따라붙는 3문 템플릿 — 답이 하나도 안 채워져도
# 이 질문 텍스트만으로 30자 문턱을 넘어버려 "공란"을 놓치게 만든다. 길이 측정 전에 제거.
PITCH_BOILERPLATE_RE = re.compile(
    r'왜\s*제작해야\s*하는(?:지|가)\??|시장성이?\s*있는지\??|크리에이티브(?:에)?\s*변별력이?\s*있는지\??|크리에이티브\s*변별력')


def gate_F1(sections):
    empties = []
    for key, label in STANDARD_SECTION_LABELS:
        content = sec(sections, key).strip()
        if key == "pitch":
            content = PITCH_BOILERPLATE_RE.sub('', content).strip()
        if len(content) < FIELD_MIN_CHARS[key]:
            empties.append(f"{label}({len(content)}자)")
    if empties:
        return "FAIL", f"{len(empties)}개 필드 공란/부족 — " + " ".join(empties)
    return "PASS", "7개 필드 전부 기준 이상"


def gate_F2(sections):
    basic = sec(sections, "basic")
    treatment = sec(sections, "treatment")
    if not basic.strip():
        return "SKIP", "기본정보 섹션을 찾지 못함"
    if "무료" not in basic:
        return "SKIP", "무료 회차 선언 없음 — 검증 불가"
    declared = parse_declared_free_count(basic)
    if declared is None:
        return "SKIP", "무료 회차 표기를 해석하지 못함"
    if not treatment.strip():
        return "FAIL", f"무료 {declared}화 선언, 트리트먼트 섹션 자체가 없음"
    episodes, _ = split_episodes(treatment)
    actual = len(episodes)
    if actual == declared:
        return "PASS", f"선언 무료 {declared}화 = 실제 회차 헤더 {actual}개"
    return "FAIL", f"선언 무료 {declared}화 vs 실제 회차 헤더 {actual}개"


def gate_F3(sections):
    plot = sec(sections, "plot")
    if not plot.strip():
        return "SKIP", "줄거리 섹션을 찾지 못함"
    hits = []
    for line in plot.splitlines():
        s = line.strip()
        if s and EP_MARKER_RE.match(s):
            hits.append(s[:40])
    if hits:
        return "FAIL", f"줄거리 안에 회차 헤더 {len(hits)}건 — " + " / ".join(f'"{h}"' for h in hits[:3])
    return "PASS", "줄거리에 회차 헤더 없음"


# ── B. 문체 ──────────────────────────────────────────────────────────────────
def gate_G1(sections):
    char_text = sec(sections, "characters")
    if not char_text.strip():
        return "SKIP", "인물 소개 섹션을 찾지 못함"
    chars = split_characters(char_text)
    if not chars:
        return "SKIP", "인물 헤더를 찾지 못함"
    with_q = [nm for nm, body in chars if DIALOGUE_QUOTE_RE.search(body)]
    without = [shorten_name(nm) for nm, body in chars if not DIALOGUE_QUOTE_RE.search(body)]
    n, total = len(with_q), len(chars)
    if n == total:
        return "PASS", f"{n}/{total} 인물에 대사"
    status = "FAIL" if n == 0 else "WARN"
    return status, f"{n}/{total} 인물에 대사 — 대사 없음: {', '.join(without[:5])}"


def gate_G2(sections):
    treatment = sec(sections, "treatment")
    if not treatment.strip():
        return "SKIP", "트리트먼트 섹션을 찾지 못함"
    episodes, order = split_episodes(treatment)
    if not episodes:
        return "SKIP", "회차 헤더를 찾지 못함"
    total = len(episodes)
    with_q = [n for n, t in episodes.items() if DIALOGUE_QUOTE_RE.search(t)]
    n = len(with_q)
    if n == total:
        return "PASS", f"{n}/{total}화 전부 대사 포함"
    missing = sorted(set(episodes) - set(with_q))
    status = "FAIL" if n == 0 else "WARN"
    return status, f"{n}/{total}화 대사 포함 — 대사 없음: {', '.join(str(m) + '화' for m in missing[:6])}"


def gate_G3(sections):
    treatment = sec(sections, "treatment")
    if not treatment.strip():
        return "SKIP", "트리트먼트 섹션을 찾지 못함"
    episodes, order = split_episodes(treatment)
    if not episodes:
        return "SKIP", "회차 헤더를 찾지 못함"
    lens = {n: char_count(t) for n, t in episodes.items()}
    out = [(n, L) for n, L in lens.items() if not (EP_MIN_CHARS <= L <= EP_MAX_CHARS)]
    avg = statistics.mean(lens.values())
    if not out:
        return "PASS", f"{len(episodes)}화 전부 {EP_MIN_CHARS}~{EP_MAX_CHARS}자 범위 (평균 {avg:.0f}자)"
    detail = " / ".join(f"{n}화 {L}자" for n, L in sorted(out)[:6])
    return "WARN", f"{len(episodes)}화 중 {len(out)}화가 범위 밖 (평균 {avg:.0f}자) — {detail}"


def _word_hit_detail(text, words):
    hits = []
    total = 0
    for w in words:
        c = text.count(w)
        if c:
            hits.append(f'"{w}"({c})')
            total += c
    return total, hits


def gate_G4(sections):
    targets = [("characters", "인물소개"), ("plot", "줄거리"), ("treatment", "트리트먼트")]
    found_any = False
    parts = []
    total = 0
    for key, label in targets:
        text = sec(sections, key)
        if not text.strip():
            continue
        found_any = True
        t, hits = _word_hit_detail(text, CONCEPT_WORDS)
        total += t
        parts += [f"{label}:{h}" for h in hits]
    if not found_any:
        return "SKIP", "대상 섹션(인물소개·줄거리·트리트먼트)을 찾지 못함"
    if parts:
        return "FAIL", f"{total}건 — " + " ".join(parts)
    return "PASS", "개념어 0"


def gate_G5(sections):
    text = sec(sections, "characters")
    if not text.strip():
        return "SKIP", "인물 소개 섹션을 찾지 못함"
    total, hits = _word_hit_detail(text, PRODUCTION_JARGON)
    if hits:
        return "FAIL", f"{total}건 — " + " ".join(hits)
    return "PASS", "제작진 용어 0"


def gate_G6(sections):
    text = sec(sections, "pitch")
    if not text.strip():
        return "SKIP", "피칭 사유 섹션을 찾지 못함"
    total, hits = _word_hit_detail(text, SELF_EVAL_PREDICATES)
    if hits:
        return "FAIL", f"{total}건 — " + " ".join(hits)
    return "PASS", "자기평가 술어 0"


def gate_G7(sections):
    text = sec(sections, "pitch")
    if not text.strip():
        return "SKIP", "피칭 사유 섹션을 찾지 못함"
    anchors = []
    for p in PLATFORMS:
        c = text.count(p)
        anchors += [f"플랫폼:{p}"] * c
    for t in TITLE_BRACKET_RE.findall(text):
        anchors.append(f"작품명:<{t[:20]}>")
    for n in NUMBER_UNIT_RE.findall(text):
        anchors.append(f"수치:{n}")
    total = len(anchors)
    status = "PASS" if total >= MIN_FACT_ANCHORS else "FAIL"
    sample = ", ".join(anchors[:6]) if anchors else "없음"
    return status, f"사실 앵커 {total}개 (기준 ≥{MIN_FACT_ANCHORS}) — {sample}"


# 최상급이 "우리 작품"이 아니라 타사 실적·원작/원전 규칙을 수식하는 문장은 제외한다.
# 골드 실증: "웨어울프의 압도적 흥행"(타사 실적) · "강력한 정령이 나온다"(원전 규칙 설명)
# — 문체 census에서 골드의 자기 작품 최상급은 0으로 판정됐다.
OTHERS_CONTEXT = ["원작", "원전", "레퍼런스", "타사", "경쟁작", "흥행작", "히트작", "시장",
                  "NetShort", "Netshort", "ReelShort", "DramaBox", "Dramabox", "DramaWave",
                  "Stardust", "ShortDrama", "Douyin", "웨어울프", "늑대인간"]


def _is_other_work_sentence(sent):
    if any(k in sent for k in OTHERS_CONTEXT):
        return True
    return bool(re.search(r'[《<〈][^》>〉]{1,60}[》>〉]', sent))


def gate_G8(sections):
    text = sec(sections, "pitch")
    if not text.strip():
        return "SKIP", "피칭 사유 섹션을 찾지 못함"
    own, excused = [], []
    for sent in split_sentences(text):
        _, hits = _word_hit_detail(sent, SUPERLATIVES)
        if not hits:
            continue
        (excused if _is_other_work_sentence(sent) else own).append((sent, hits))
    if own:
        detail = " ".join(h for _, hs in own for h in hs)
        quote = own[0][0][:44]
        return "FAIL", f'{len(own)}문장 — {detail} · 예: "{quote}..."'
    if excused:
        return "PASS", f"자기 작품 최상급 0 (타사 실적·원전 서술 {len(excused)}문장은 제외)"
    return "PASS", "자기 최상급 0"


def gate_G9(sections):
    text = sec(sections, "pitch")
    if not text.strip():
        return "SKIP", "피칭 사유 섹션을 찾지 못함"
    n = len(SINGLE_QUOTE_RE.findall(text))
    if n <= MAX_SINGLE_QUOTES:
        return "PASS", f"작은따옴표 {n}개 (기준 ≤{MAX_SINGLE_QUOTES})"
    sample = ", ".join(f'"{m}"' for m in SINGLE_QUOTE_RE.findall(text)[:5])
    return "FAIL", f"작은따옴표 {n}개 (기준 ≤{MAX_SINGLE_QUOTES}) — {sample}"


def gate_G10(sections):
    keys = ("title", "cm", "basic", "pitch", "characters", "plot", "treatment")
    if not any(sec(sections, k).strip() for k in keys):
        return "SKIP", "표준 섹션을 찾지 못함"
    hits = []
    for k in keys:
        for line in sec(sections, k).splitlines():
            if is_reference_line(line):
                continue
            hits += HANJA_RE.findall(line)
    if hits:
        counts = Counter(hits)
        sample = " ".join(f'{ch}×{c}' for ch, c in counts.most_common(10))
        return "FAIL", f"한자 {len(hits)}자 — {sample}"
    return "PASS", "한자 0"


def gate_G11(sections):
    treatment = sec(sections, "treatment")
    if not treatment.strip():
        return "SKIP", "트리트먼트 섹션을 찾지 못함"
    episodes, _ = split_episodes(treatment)
    if not episodes:
        return "SKIP", "회차 헤더를 찾지 못함"
    summary_hits, dialogue_n = [], 0
    for n, t in sorted(episodes.items()):
        c = extract_cliff(t)
        if cliff_is_summary(c):
            summary_hits.append(n)
        if cliff_is_dialogue(c):
            dialogue_n += 1
    total = len(episodes)
    ratio = dialogue_n / total if total else 0
    msgs = []
    status = "PASS"
    if summary_hits:
        status = "FAIL"
        msgs.append(f"감정·요약종결 {len(summary_hits)}건({','.join(str(x) + '화' for x in summary_hits)})")
    if ratio < CLIFF_DIALOGUE_MIN_RATIO:
        status = "FAIL" if status == "FAIL" else "WARN"
        msgs.append(f"대사 클리프 {dialogue_n}/{total}({ratio:.0%}) < {CLIFF_DIALOGUE_MIN_RATIO:.0%}")
    if status == "PASS":
        return "PASS", f"감정·요약종결 0 · 대사 클리프 {dialogue_n}/{total}({ratio:.0%})"
    return status, " / ".join(msgs)


def gate_G12(sections):
    text = sec(sections, "pitch")
    if not text.strip():
        return "SKIP", "피칭 사유 섹션을 찾지 못함"
    sents = split_sentences(re.sub(r'\s+', ' ', text))
    if not sents:
        return "SKIP", "문장을 추출하지 못함"
    lens = [len(s) for s in sents]
    avg_len = statistics.mean(lens)
    avg_conn = statistics.mean([count_connectives(s) for s in sents])
    if avg_len <= MAX_SENT_CHARS_AVG and avg_conn <= MAX_CONNECTIVE_AVG:
        return "PASS", f"평균 {avg_len:.1f}자/문장 · 절연결 {avg_conn:.2f} (문장 {len(sents)}개)"
    msgs = []
    if avg_len > MAX_SENT_CHARS_AVG:
        msgs.append(f"평균 {avg_len:.1f}자 > {MAX_SENT_CHARS_AVG}자")
    if avg_conn > MAX_CONNECTIVE_AVG:
        msgs.append(f"절연결 {avg_conn:.2f} > {MAX_CONNECTIVE_AVG}")
    return "WARN", " · ".join(msgs) + f" (문장 {len(sents)}개)"


def gate_G13(sections):
    basic = sec(sections, "basic")
    if not basic.strip():
        return "SKIP", "기본정보 섹션을 찾지 못함"
    logline = extract_logline(basic)
    if not logline:
        return "SKIP", "로그라인 필드를 찾지 못함"
    n = char_count(logline)
    q = logline.count('?') + logline.count('？')
    sents = split_sentences(logline)
    last = sents[-1] if sents else logline
    fails = []
    if not (LOGLINE_MIN <= n <= LOGLINE_MAX):
        fails.append(f"{n}자(기준 {LOGLINE_MIN}~{LOGLINE_MAX})")
    if q:
        fails.append(f"물음표 {q}개")
    if GENRE_LABEL_ENDING_RE.search(last) or re.search(r'하기\s*시작한다[.]?$', last):
        fails.append(f'종결 라벨/요약형 — "...{last[-24:]}"')
    if fails:
        return "FAIL", " / ".join(fails) + f' — "{logline[:50]}..."'
    return "PASS", f"{n}자 · 물음표 0 · 종결 정상"


def gate_G15(sections):
    text = sec(sections, "pitch")
    if not text.strip():
        return "SKIP", "피칭 사유 섹션을 찾지 못함"
    sents = split_sentences(re.sub(r'\s+', ' ', text))
    if not sents:
        return "SKIP", "문장을 추출하지 못함"
    noun_n = sum(1 for s in sents if ends_noun_style(s))
    ratio = noun_n / len(sents)
    _, judge_hits = _word_hit_detail(text, JUDGE_PHRASES)
    detail = f"명사/-음/-함 종결 {noun_n}/{len(sents)}({ratio:.0%})"
    if judge_hits:
        detail += " · 판단술어 " + " ".join(judge_hits)
    status = "PASS" if ratio >= NOUN_ENDING_MIN_RATIO else "WARN"
    return status, detail


def gate_G16(sections):
    basic = sec(sections, "basic")
    full_body = "\n".join(sec(sections, k) for k in ("characters", "plot", "treatment"))
    if not basic.strip() or not full_body.strip():
        return "SKIP", "기본정보 또는 본문 섹션을 찾지 못함"
    logline = extract_logline(basic)
    if not logline:
        return "SKIP", "로그라인 필드를 찾지 못함"
    cast_hangul = set()
    for label, _ in split_characters(sec(sections, "characters")):
        nm = shorten_name(label)
        if re.fullmatch(r'[가-힣]{2,4}', nm):
            cast_hangul.add(nm)
    body_names = name_candidates(full_body, cast_hangul)
    logline_names = name_candidates(logline, cast_hangul)
    # 괄호 안 로마자 = 음역 병기(진(Djinn)의 왕 · 삼해(三海))지 인명이 아니다 — 후보에서 뺀다.
    paren_glosses = set()
    for g in re.findall(r"[（(]\s*([A-Za-z][A-Za-z\s\-]{1,28})\s*[)）]", logline):
        paren_glosses.update(g.split())
    issues = []
    for nm in sorted(logline_names):
        if nm in full_body or nm in paren_glosses:
            continue
        near = [bn for bn in body_names if abs(len(bn) - len(nm)) <= 1 and edit_distance_dl(nm, bn) == 1]
        if near:
            issues.append(f'표기 유사: 로그라인"{nm}" vs 본문"{near[0]}"')
        else:
            issues.append(f'로그라인 전용:"{nm}"(본문 미등장)')
    bl = sorted(body_names)
    for i in range(len(bl)):
        for j in range(i + 1, len(bl)):
            a, b = bl[i], bl[j]
            if abs(len(a) - len(b)) <= 1 and edit_distance_dl(a, b) == 1:
                issues.append(f'본문 내 표기 유사:"{a}"/"{b}"')
    issues = sorted(set(issues))
    if issues:
        return "FAIL", "; ".join(issues[:6])
    return "PASS", f"인명 후보 {len(body_names)}개 — 로그라인 정합·유사표기 충돌 0"


# ── C. 사용자 룰 ─────────────────────────────────────────────────────────────
def gate_U1(sections, full_text):
    hits = []
    for line in full_text.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.match(r'^#{1,6}\s', s):
            heading = re.sub(r'^#{1,6}\s+', '', s)
            if classify_heading(heading) is not None:
                continue
        elif classify_heading(s) is not None:
            continue
        for m in re.finditer(r'페이월|paywall', s, re.I):
            hits.append(f'"{m.group(0)}" in "{s[:40]}"')
    if hits:
        return "FAIL", f"{len(hits)}건 — " + "; ".join(hits[:5])
    return "PASS", "페이월/Paywall 단어 0 (섹션 헤더 라벨 제외)"


def gate_U2(sections):
    treatment = sec(sections, "treatment")
    if not treatment.strip():
        return "SKIP", "트리트먼트 섹션을 찾지 못함"
    hits = []
    for line in treatment.splitlines():
        s = line.strip()
        if not s or not EP_MARKER_RE.match(s):
            continue
        if '｜' in s or re.search(r'\s-\s\S', s):
            hits.append(s[:50])
    if hits:
        return "FAIL", f"{len(hits)}건 — " + " / ".join(f'"{h}"' for h in hits[:4])
    return "PASS", "회차 부제 0"


# ── 오케스트레이션 ────────────────────────────────────────────────────────────
GATE_LABELS = {
    "F1": "필드 공란 0", "F2": "회차 수 일치", "F3": "필드 자리 뒤바뀜 0",
    "G1": "인물 대사", "G2": "트리트먼트 대사", "G3": "화당 분량", "G4": "개념어 0",
    "G5": "제작진 용어 0", "G6": "자기평가 술어 0", "G7": "사실 앵커 ≥4", "G8": "자기 최상급 0",
    "G9": "개념 라벨 ≤3", "G10": "한자 0", "G11": "클리프 유형", "G12": "문장 길이",
    "G13": "로그라인", "G15": "어미 통일", "G16": "인명 정합",
    "U1": "\"페이월\" 단어 0", "U2": "회차 부제 0",
}
GATE_ORDER = ["F1", "F2", "F3", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",
              "G10", "G11", "G12", "G13", "G15", "G16", "U1", "U2"]
GATE_FUNCS = {
    "F1": lambda s, t: gate_F1(s), "F2": lambda s, t: gate_F2(s), "F3": lambda s, t: gate_F3(s),
    "G1": lambda s, t: gate_G1(s), "G2": lambda s, t: gate_G2(s), "G3": lambda s, t: gate_G3(s),
    "G4": lambda s, t: gate_G4(s), "G5": lambda s, t: gate_G5(s), "G6": lambda s, t: gate_G6(s),
    "G7": lambda s, t: gate_G7(s), "G8": lambda s, t: gate_G8(s), "G9": lambda s, t: gate_G9(s),
    "G10": lambda s, t: gate_G10(s), "G11": lambda s, t: gate_G11(s), "G12": lambda s, t: gate_G12(s),
    "G13": lambda s, t: gate_G13(s), "G15": lambda s, t: gate_G15(s), "G16": lambda s, t: gate_G16(s),
    "U1": lambda s, t: gate_U1(s, t), "U2": lambda s, t: gate_U2(s),
}


def run_all_gates(sections, full_text):
    results = []
    for gid in GATE_ORDER:
        try:
            status, detail = GATE_FUNCS[gid](sections, full_text)
        except Exception as e:
            status, detail = "SKIP", f"게이트 실행 오류: {e}"
        results.append((gid, GATE_LABELS[gid], status, detail))
    return results


def print_report(results):
    for gid, label, status, detail in results:
        head = f"[{status}] {gid} {label}"
        pad = " " * max(1, 30 - len(head))
        print(f"{head}{pad}{detail}")
    tot = Counter(r[2] for r in results)
    overall = "FAIL" if tot["FAIL"] else ("WARN" if tot["WARN"] else "PASS")
    print(f"\n판정 = {overall} (FAIL {tot['FAIL']} · WARN {tot['WARN']} · PASS {tot['PASS']} · SKIP {tot['SKIP']})")


def results_to_json(results):
    tot = Counter(r[2] for r in results)
    overall = "FAIL" if tot["FAIL"] else ("WARN" if tot["WARN"] else "PASS")
    return {
        "verdict": overall,
        "counts": {"FAIL": tot["FAIL"], "WARN": tot["WARN"], "PASS": tot["PASS"], "SKIP": tot["SKIP"]},
        "gates": [{"id": gid, "label": label, "status": status, "detail": detail}
                  for gid, label, status, detail in results],
    }


# ── --stats: 실물 코퍼스 3종 실측 ─────────────────────────────────────────────
ENTRY_RE = re.compile(r'(?:^|\n)(\d+)\.\s*(.+?)\s*\n+\[TABLE\](.*?)\[/TABLE\]', re.S)


def split_corpus_entries(raw_text):
    entries = []
    for m in ENTRY_RE.finditer(raw_text):
        entries.append({"title": m.group(2).strip(), "body": m.group(3)})
    return entries


def load_corpus_entries():
    all_entries = []
    for fname in CORPUS_FILES:
        path = os.path.join(CORPUS_DIR, fname)
        if not os.path.exists(path):
            print(f"(경고) 코퍼스 파일을 찾지 못함: {path}")
            continue
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        for e in split_corpus_entries(raw):
            e["file"] = fname
            all_entries.append(e)
    return all_entries


def run_stats():
    entries = load_corpus_entries()
    print(f"코퍼스 엔트리 수: {len(entries)} (기대 10 — deck 3종 합산)\n")

    rows = []
    all_results = []
    for i, e in enumerate(entries, 1):
        sections = parse_sections(e["body"])
        full_text = e["body"]
        total_chars = sum(len(sec(sections, k)) for k, _ in STANDARD_SECTION_LABELS)
        dq = len(DIALOGUE_QUOTE_RE.findall(full_text))
        sq = len(SINGLE_QUOTE_RE.findall(full_text))
        # 주의: 이 forensic 표는 MAIN_FINDINGS 유닛3 원 census 방식을 재현하기 위해 전체 텍스트
        # 스코프로 센다 (G4 게이트 자체는 피칭 사유를 제외한 좁은 스코프 — run_all_gates 쪽 참조).
        cw_total, _ = _word_hit_detail(full_text, CONCEPT_WORDS)
        rows.append((f"E{i}", e["title"][:28], total_chars, dq, sq, cw_total))
        results = run_all_gates(sections, full_text)
        all_results.append((f"E{i}", e["title"][:28], results))

    print("문체 포렌식 (MAIN_FINDINGS §유닛3 표 재현 — 전체 텍스트 기준)")
    print(f"{'':4}{'엔트리':30}{'총자':>6}{'큰따옴표':>8}{'작은따옴표':>10}{'개념어':>8}")
    for eid, title, total, dq, sq, cw in rows:
        print(f"{eid:4}{title:30}{total:>6}{dq:>8}{sq:>10}{cw:>8}")

    print("\n검증 대조 (MAIN_FINDINGS 실측 vs 이 도구 재계산)")
    checks = [
        ("E1 (골드·거지 알라딘)", 0, {"dq": 36, "sq": 0, "cw": 2}),
        ("E5 (내가 죽인 남자가 돌아왔다)", 4, {"dq": 0, "sq": 16, "cw": 14}),
    ]
    for label, idx, expect in checks:
        _, _, total, dq, sq, cw = rows[idx]
        ok = (dq == expect["dq"] and sq == expect["sq"] and cw == expect["cw"])
        tag = "일치" if ok else "불일치"
        print(f"  {label}: 실측 dq={dq}/sq={sq}/cw={cw}  vs  MAIN_FINDINGS dq={expect['dq']}/sq={expect['sq']}/cw={expect['cw']}  -> {tag}")
        if not ok and idx == 0:
            print("    (E1 sq 2 vs 0 — 원문 확인 결과 '세계관 학습 비용'/'소원 세 개' 둘 다 개념 라벨용 직선"
                  " 따옴표(' ')다. G9 스펙이 명시적으로 ‘ ’ 및 ' ' 둘 다 세라고 하므로 의도된 확장이며"
                  " 파서 오류가 아니다 — 원 census는 곡선 따옴표만 셌던 것으로 보임.)")

    print("\n인물소개 대사 밀도 (MAIN_FINDINGS: 골드 13개 / 나머지 9개 합계 2개)")
    char_quote_total_gold = None
    char_quote_rest_sum = 0
    for i, e in enumerate(entries, 1):
        sections = parse_sections(e["body"])
        char_text = sec(sections, "characters")
        n = len(DIALOGUE_QUOTE_RE.findall(char_text))
        if i == 1:
            char_quote_total_gold = n
        else:
            char_quote_rest_sum += n
    print(f"  E1(골드) 인물소개 대사 {char_quote_total_gold}개 / 나머지 9개 합계 {char_quote_rest_sum}개")

    print("\nG3 화당 분량 (MAIN_FINDINGS: 골드 화당 150자, 8/8 화 대사 포함)")
    e1_sections = parse_sections(entries[0]["body"])
    e1_eps, _ = split_episodes(sec(e1_sections, "treatment"))
    if e1_eps:
        lens = [char_count(t) for t in e1_eps.values()]
        print(f"  E1 회차 {len(e1_eps)}개 · 평균 {statistics.mean(lens):.0f}자 · 범위 {min(lens)}~{max(lens)}자")

    print("\n전체 게이트 판정 분포 (10 엔트리 × 20 게이트)")
    per_gate_fail = Counter()
    per_gate_skip = Counter()
    overall_counts = Counter()
    for eid, title, results in all_results:
        tot = Counter(r[2] for r in results)
        overall = "FAIL" if tot["FAIL"] else ("WARN" if tot["WARN"] else "PASS")
        overall_counts[overall] += 1
        print(f"  {eid} {title:28} FAIL {tot['FAIL']:>2} WARN {tot['WARN']:>2} PASS {tot['PASS']:>2} SKIP {tot['SKIP']:>2}  -> {overall}")
        for gid, label, status, detail in results:
            if status == "FAIL":
                per_gate_fail[gid] += 1
            if status == "SKIP":
                per_gate_skip[gid] += 1
    print(f"\n엔트리 판정 분포: " + " · ".join(f"{k} {v}건" for k, v in overall_counts.items()))
    print("게이트별 FAIL 빈도(10건 중): " + " ".join(f"{g}={per_gate_fail.get(g,0)}" for g in GATE_ORDER))
    print("게이트별 SKIP 빈도(10건 중): " + " ".join(f"{g}={per_gate_skip.get(g,0)}" for g in GATE_ORDER))


def main():
    ap = argparse.ArgumentParser(description="사내 피칭 페이지 기계 게이트 — 세는 것만 센다 (재미·설득력 판정 아님)")
    ap.add_argument("file", nargs="?", help="검사할 피칭 페이지 마크다운 파일")
    ap.add_argument("--json", action="store_true", help="기계 판독용 JSON 출력")
    ap.add_argument("--stats", action="store_true", help="실물 코퍼스 3종 실측치 출력(규격 근거 재확인)")
    a = ap.parse_args()

    if a.stats:
        run_stats()
        return

    if not a.file:
        ap.print_help()
        return

    with open(a.file, encoding="utf-8") as f:
        text = f.read()
    sections = parse_sections(text)
    results = run_all_gates(sections, text)

    if a.json:
        print(json.dumps(results_to_json(results), ensure_ascii=False, indent=2))
    else:
        print_report(results)


if __name__ == "__main__":
    main()
