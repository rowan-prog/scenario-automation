# 시나리오 자동화 (Scenario Automation)

AIGC 숏폼 vertical drama 시나리오 제작 워크플로우. **Claude Code에서 그대로 돌아가는 완성된 작업 시스템**이다.

아이디어 → 러프 기획 → 피칭 → 청사진 → 집필 → 검수 → LOCK 까지 단계별 절차와 판정 기준이 문서·에이전트·기계 검사 도구로 고정돼 있다. 각색(원작 치환), 외부 대본 검수, 플랫폼 제출용 기획안 트랙도 포함.

실제로 이 시스템이 뽑아낸 것 → [`CASE_STUDIES.md`](CASE_STUDIES.md)

---

## 5분 설치

**필요한 것:** [Claude Code](https://claude.com/claude-code) · Python 3.9+ · (docx 산출물을 쓸 거면) `pip install python-docx`

```powershell
# Windows PowerShell
cd <이 폴더>
.\install.ps1
```

```bash
# macOS / Linux
cd <이 폴더>
bash install.sh
```

설치 스크립트가 하는 일은 하나뿐이다 — **메모리 185개를 Claude Code가 읽는 위치로 복사**. 나머지(룰 문서·에이전트·프롬프트·도구)는 이 폴더 안에 있어서 복사가 필요 없다.

설치 후 확인:

```bash
python verify.py
```

그다음 이 폴더에서 `claude` 를 실행하면 끝이다. `CLAUDE.md`가 자동으로 읽히고, `.claude/agents/` 의 서브 에이전트 14종이 자동 인식된다.

---

## 첫 작업 시작하기

Claude Code를 띄우고 그냥 한국어로 말하면 된다. 예:

- `새 작품 하나 시작하자. 소재는 ○○○ 이고 남성향 글로벌 타깃.`
- `이 원작 대본 각색하고 싶어. 파일 여기 있어: <경로>`
- `외부에서 받은 대본인데 검수해줘.`
- `플랫폼 제출용 기획안 만들어야 해.`

에이전트가 `CLAUDE.md`의 **작업 라우팅 표**를 보고 알아서 해당 절차 문서로 진입한다. 어느 phase인지 사용자가 지정할 필요는 없다.

---

## 무엇이 들어 있나

```
├── CLAUDE.md              ★ 진입점. Claude Code가 자동으로 읽는다. 작업 라우팅 표가 심장
├── CASE_STUDIES.md          이 시스템이 실제로 만든 것 + 실패에서 나온 룰
├── SETUP.md                 설치 상세·검증·문제 해결·재배포
├── install.ps1 / install.sh 메모리 설치
├── verify.py                설치 검증
│
├── .claude/agents/          서브 에이전트 14종 (검수·수술·발상·프록시)
├── memory/                  학습 메모리 185개 — 설치 스크립트가 여기서 복사해 간다
│
├── config/                  룰과 자산
│   ├── 00_vertical_dna.md       근본 원리 (8대 매체 조건)
│   ├── 10_writing_standard.md   집필 표준
│   ├── 20_review_standard.md    검수·LOCK 표준
│   ├── 30_writer_feedback_standard.md  외부 작가 대본 코멘트 표준
│   ├── vertical_drama_hit_scripts/          히트작 역대본 원본 ※
│   ├── vertical_drama_hit_scripts_analysis/ 히트작 분석·강의록
│   ├── personas/ · evaluators.md            검토 페르소나 10 · 피칭 위원 7
│   ├── pitch_references/ · target_research/ 피칭 실적 데이터 · 권역별 리서치
│   └── *_template.md                        각종 템플릿
│
├── prompts/                 단계별 절차 15종 (phase 0~7 · a · b · c · p)
├── tools/                   기계 검사·빌더 8종
└── projects/                작품 폴더가 여기 생긴다 (비어 있음)
```

※ `config/vertical_drama_hit_scripts/` 는 **외부 저작물**이다. 사내 참고 목적으로만 쓰고, 외부 재배포·공개 저장소 업로드 금지. 이 폴더 없이도 시스템은 동작한다(분석본·craftcard가 대체) — 다만 집필 품질 기준이 눈에 띄게 내려간다.

---

## 이 시스템의 작동 방식 한 장 요약

1. **모든 판정은 문서에 있다.** 감으로 판정하지 않는다. 판정 기준이 문서에 없으면 그건 문서 개정 안건이지 즉흥 판단 대상이 아니다.
2. **생산자와 판정자를 분리한다.** 메인 세션은 대본 본문을 직접 쓰지 않는다 — 별도 에이전트에 위임하고, 메인은 채택 여부만 판정한다.
3. **기계로 잡을 수 있는 건 기계가 잡는다.** 대사 톤·정합·페이싱·인물별 레지스터는 파이썬 스크립트가 먼저 훑는다.
4. **최종 도장은 사람이 찍는다.** LOCK 후보까지가 시스템의 몫이고, 확정은 사용자 콜드리드 뒤에 이뤄진다.
5. **반려당한 이유는 반드시 메모리가 된다.** 이게 이 패키지의 실제 자산이다.

---

## 라이선스

내부 작업 도구. 히트작 역대본·리서치 자료·피칭 데이터는 외부 공개 금지.
