#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
continuity_lint.py — AIGC △ 대본 결정론 정합성 보조 (LOCK 파이프라인 Phase 2A/2B용)
LLM 판단 0. 숫자 + 라인번호만 낸다. "괜찮다" 금지 — 분모/카운트로 증명.

검사:
  - 구조 카운트 (EP / S# / Characters / [END HOOK] / Hard Cut. / have sex / Jump cut / On-screen text)
  - per-line 분모 (Dialogue / VO / △ action 라인 수)
  - 한국어 잔존 (라인 flag)
  - action-line 대명사 (△가 대명사로 시작 = HARD / △ 내 대명사 총량 = INFO)
  - 소품/상태 thread (shirt·dress·cloak·pendant·scar·mark·door·window·knife·blood… 라인 나열 → on/off 충돌 육안)
  - END HOOK 아래 △ 개수
  - 포맷 비준수 라인 (정체불명 = 메타/깨짐 후보)
  - scene별 Characters 누락
  - 금지/회귀 문구 (인자로 추가 가능)

usage: python tools/continuity_lint.py <script.md> [--banned "phrase1;phrase2"]
"""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()

KOREAN = re.compile(r"[가-힣㄰-㆏]")
SCENE  = re.compile(r"^##\s*EP\s*(\d+)\s*-\s*S#\s*(\d+)", re.I)
EPNUM  = re.compile(r"EP\s*(\d+)", re.I)
DIA    = re.compile(r"^[A-Z][A-Z0-9'’.\- ]*(\([^)]*\))?:\s")   # NAME (cue): ...
PRON   = re.compile(r"\b(he|she|his|her|him|hers|they|them|their)\b", re.I)
PRON_START = re.compile(r"^△\s*(\[[^\]]*\]\s*)?(He|She|His|Her|Him|They|Their)\b")
NAME   = re.compile(r"\b([A-Z][a-z]+)\b")  # crude proper-name (capitalized word)

PROPS = ["shirt","dress","cloak","gown","robe","coat","pendant","necklace","scar",
         "mark","ring","knife","blade","syringe","needle","mask","cap","IV","blood",
         "door","window","gate","phone","veil","scale","scales","wrist"]

FORMAT_OK = [
    re.compile(r"^\s*$"),
    re.compile(r"^---\s*$"),
    re.compile(r"^#"),                       # title / EP / scene headers
    re.compile(r"^Characters:", re.I),
    re.compile(r"^△"),
    re.compile(r"^On-screen text", re.I),
    re.compile(r"^\[END HOOK\]"),
    re.compile(r"^Hard Cut\.?"),
    re.compile(r"^>"),                       # subtitle alt
    re.compile(r"^END\.?\s*$"),              # EP50 natural END
    DIA,
]

def is_format_ok(line):
    return any(p.match(line) for p in FORMAT_OK)

def main():
    path = sys.argv[1]
    banned = []
    if "--banned" in sys.argv:
        banned = [b.strip() for b in sys.argv[sys.argv.index("--banned")+1].split(";") if b.strip()]
    lines = load(path)

    eps, scenes, scene_has_chars = set(), [], []
    end_hook_idx, hardcut, havesex, jumpcut, onscreen = [], 0, 0, 0, 0
    dia_lines, vo_lines, tri_lines = [], [], []
    korean, pron_hard, pron_info = [], [], []
    nonformat = []
    prop_hits = {p: [] for p in PROPS}
    cur_scene = None
    scene_chars_seen = {}

    for i, ln in enumerate(lines, 1):
        s = ln.rstrip("\n")
        m = SCENE.match(s)
        if m:
            eps.add(int(m.group(1))); scenes.append((i, s))
            cur_scene = i; scene_chars_seen[cur_scene] = False
            continue
        if s.lower().startswith("characters:"):
            if cur_scene: scene_chars_seen[cur_scene] = True
            continue
        if s.startswith("△"):
            tri_lines.append(i)
            if PRON_START.match(s): pron_hard.append((i, s))
            for pm in PRON.finditer(s): pron_info.append((i, pm.group(0)))
            low = s.lower()
            if "have sex" in low: havesex += 1
            if "jump cut" in low: jumpcut += 1
            for p in PROPS:
                if re.search(r"\b"+re.escape(p)+r"\b", s, re.I): prop_hits[p].append(i)
        if s.startswith("[END HOOK]"): end_hook_idx.append(i)
        if re.match(r"^Hard Cut\.?", s): hardcut += 1
        if re.match(r"^On-screen text", s, re.I): onscreen += 1
        if DIA.match(s):
            if re.search(r"\(\s*V\.?O\.?", s, re.I): vo_lines.append(i)
            else: dia_lines.append(i)
        if KOREAN.search(s): korean.append((i, s.strip()[:60]))
        if not is_format_ok(s): nonformat.append((i, s.strip()[:70]))
        for b in banned:
            if b.lower() in s.lower(): nonformat.append((i, f"[BANNED:{b}] "+s.strip()[:60]))

    # END HOOK 아래 △ 개수
    hook_struct = []
    for hi in end_hook_idx:
        cnt = 0
        for j in range(hi, len(lines)):   # hi=1-based; lines[hi]=line hi+1 (첫 줄 after [END HOOK])
            t = lines[j].strip()
            if t.startswith("△") or DIA.match(t) or re.match(r"^On-screen", t, re.I): cnt += 1
            elif SCENE.match(t) or re.match(r"^Hard Cut", t) or t == "---": break
        hook_struct.append((hi, cnt))

    P = print
    P("="*60); P(f"continuity_lint :: {path}"); P("="*60)
    P("\n[STRUCTURE]")
    P(f"  EP: {len(eps)}  {sorted(eps)}")
    P(f"  Scenes (S#): {len(scenes)}")
    miss = [s for s in scenes if not scene_chars_seen.get(s[0])]
    P(f"  Characters: 누락 scene: {len(miss)}" + ("" if not miss else f"  -> {[m[0] for m in miss]}"))
    P(f"  [END HOOK]: {len(end_hook_idx)}   Hard Cut.: {hardcut}   On-screen text: {onscreen}")
    P(f"  have sex: {havesex}   Jump cut: {jumpcut}")
    P("\n[PER-LINE 분모]")
    P(f"  Dialogue: {len(dia_lines)}   VO: {len(vo_lines)}   △ action: {len(tri_lines)}")
    P("\n[KOREAN 잔존]: " + str(len(korean)))
    for i,t in korean[:20]: P(f"  L{i}: {t}")
    P("\n[ACTION-LINE 대명사]")
    P(f"  HARD (△가 대명사로 시작): {len(pron_hard)}")
    for i,t in pron_hard[:30]: P(f"  L{i}: {t[:75]}")
    P(f"  INFO (△ 내 대명사 총 occurrence): {len(pron_info)}  (이름 뒤 대명사는 OK·같은성별 다수 씬만 주의)")
    P("\n[END HOOK 아래 △ 개수]")
    for hi,c in hook_struct: P(f"  L{hi}: {c}개" + ("  <- 0! 확인" if c==0 else ""))
    P("\n[소품/상태 thread] (on→off 충돌 육안 추적)")
    for p,hits in prop_hits.items():
        if hits: P(f"  {p}: {hits}")
    P("\n[포맷 비준수/금지문구 라인]: " + str(len(nonformat)))
    for i,t in nonformat[:30]: P(f"  L{i}: {t}")

    P("\n[SUMMARY]")
    hard0 = (len(korean)==0 and len(pron_hard)==0 and len(nonformat)==0
             and not miss and all(c>=1 for _,c in hook_struct))
    P(f"  korean=0:{len(korean)==0}  action-pronoun-hard=0:{len(pron_hard)==0}  "
      f"format-clean:{len(nonformat)==0}  chars-complete:{not miss}  "
      f"endhook-shots>=1:{all(c>=1 for _,c in hook_struct) if hook_struct else 'n/a'}")
    P(f"  => 기계 게이트 {'PASS' if hard0 else 'FAIL (위 항목 수술)'}")

if __name__ == "__main__":
    main()
