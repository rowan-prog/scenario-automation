# -*- coding: utf-8 -*-
"""프로젝트 폴더 정리. 루트 = 작가 전달 3종 + meta + README, 나머지는 분류 폴더로."""
import io, os, sys, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

B = r"C:\Users\Rowan\scenario-automation\projects\16_moses"
os.chdir(B)

DIRS = {
    '01_원본': '원작 대본 · 작가 초고 · 사용자 코멘트본 · 외부 피드백',
    '02_기획': 'phase_p 기획 산출물 · 트리트먼트 원본 md',
    '03_작업파일': '추출 텍스트 · 검토 에이전트용 덤프',
    '04_스크립트': '문서 빌더 · 검증 도구',
    '05_구버전': '폐기된 이전 판본',
}
for d in DIRS:
    os.makedirs(d, exist_ok=True)

KEEP_ROOT = {
    '내 남편은 거지 모세_각색 가이드_v14.docx',
    '내 남편은 거지 모세_1-21화 수정 지시서_v3.docx',
    '내 남편은 거지 모세_회차 트리트먼트_1-50화_v4.docx',
    '16_moses_00_meta.md', 'README.md', '_organize.py',
}

MAP = {
    '01_원본': [
        '거지남편아폴론_양식조정본.docx', '(완)역대본_거지남편아폴론_01-48화.docx',
        '_writer_draft_ep1-21.docx', '_user_commented_v2.docx',
        '_user_commented_ep1-21.docx', '_codex_feedback.docx', '_codex_feedback.txt',
        '_user_comments_v2.txt', 'I Chose a Slave, But He Parts the Sea.docx',
        '16_moses_source_apollo.md',
    ],
    '02_기획': [
        '16_moses_p0_source.md', '16_moses_p1_proposal_spec.txt',
        '16_moses_p1_treatment_full_v2.md', '16_moses_p1_treatment_full.md',
        '16_moses_p1_treatment_ep1-21_v2.md', '16_moses_adaptation_guide.md',
    ],
    '03_작업파일': [
        '_draft_paras.txt', '_orig_paras.txt', '_docx_dump.txt',
        '_export_feedback_v1.txt', '_export_guide_v14.txt', '_export_guide_v13.txt',
        '_export_guide_v12.txt', '_export_guide_v11.txt',
        '_writer_draft_ep1-7.txt', '_v7_comments_dump.txt',
    ],
    '04_스크립트': [
        '_build_guide_v14.py', '_build_feedback.py', '_build_feedback2.py',
        '_build_feedback3.py', '_build_treatment_v2.py',
        '_verify_rows.py', '_xcheck.py', '_xcheck2.py', '_xcheck3.py',
        '_guide_factcheck.py', '_gap_audit.py', '_count_rows.py',
        '_export_txt.py', '_extract_docx.py', '_gate_check.py', '_add_comments.py',
    ],
}

moved, busy = 0, []
for dst, files in MAP.items():
    for f in files:
        if os.path.isfile(f):
            try:
                shutil.move(f, os.path.join(dst, f)); moved += 1
            except Exception as e:
                busy.append(f)

# 남은 것 = 구버전으로
for f in sorted(os.listdir('.')):
    if not os.path.isfile(f) or f in KEEP_ROOT or f.startswith('~$'):
        continue
    try:
        shutil.move(f, os.path.join('05_구버전', f)); moved += 1
    except Exception:
        busy.append(f)

# 스크립트가 어디서 실행돼도 루트를 보게
CH = "import os as _os; _os.chdir(r'%s')\n" % B
for f in sorted(os.listdir('04_스크립트')):
    if not f.endswith('.py'):
        continue
    p = os.path.join('04_스크립트', f)
    s = open(p, encoding='utf-8').read()
    if '_os.chdir' in s:
        continue
    lines = s.split('\n')
    i = 1 if lines and lines[0].startswith('# -*-') else 0
    lines.insert(i, CH.rstrip())
    open(p, 'w', encoding='utf-8').write('\n'.join(lines))

# 스크립트 안의 상대 경로를 03_작업파일 기준으로
FIX = [("'_draft_paras.txt'", r"'03_작업파일/_draft_paras.txt'"),
       ("'_orig_paras.txt'", r"'03_작업파일/_orig_paras.txt'"),
       ("+ '_draft_paras.txt'", r"+ '03_작업파일/_draft_paras.txt'"),
       ("+ '_orig_paras.txt'", r"+ '03_작업파일/_orig_paras.txt'"),
       ("'16_moses_p1_treatment_full_v2.md'", r"'02_기획/16_moses_p1_treatment_full_v2.md'"),
       ("+ '16_moses_p1_treatment_full_v2.md'", r"+ '02_기획/16_moses_p1_treatment_full_v2.md'"),
       ("'_export_feedback_v1.txt'", r"'03_작업파일/_export_feedback_v1.txt'"),
       ("'_export_guide_v14.txt'", r"'03_작업파일/_export_guide_v14.txt'"),
       ("B + '_export", r"B + '03_작업파일/_export"),
       ("B + '_draft", r"B + '03_작업파일/_draft"),
       ("B + '_orig", r"B + '03_작업파일/_orig"),
       ("SRC = r\"C:\\Users\\Rowan\\scenario-automation\\projects\\16_moses\\16_moses_p1_treatment_full_v2.md\"",
        "SRC = r\"C:\\Users\\Rowan\\scenario-automation\\projects\\16_moses\\02_기획\\16_moses_p1_treatment_full_v2.md\""),
       ]
for f in sorted(os.listdir('04_스크립트')):
    if not f.endswith('.py'):
        continue
    p = os.path.join('04_스크립트', f)
    s = open(p, encoding='utf-8').read()
    for a, b in FIX:
        s = s.replace(a, b)
    s = s.replace(r"03_작업파일/03_작업파일/", "03_작업파일/")
    open(p, 'w', encoding='utf-8').write(s)

print('옮긴 파일', moved)
print('잠겨서 못 옮김:', busy if busy else '없음')
for d in sorted(DIRS):
    print(f'  {d}/  {len(os.listdir(d))}개')
