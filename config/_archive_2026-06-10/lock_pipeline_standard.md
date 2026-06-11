# LOCK 파이프라인 표준 (단일 진실 · 2026-06-09 확정)

> AIGC 세로드라마 작품을 집필/변환 → LOCK까지 가는 표준 과정. `agent_operating_rules.md`(권한)·`final_review_flow.md`(검수 절차)와 한 쌍 — 본 문서가 LOCK 전체 파이프라인의 진실.

## 대원칙
- **오류 ≠ 재미. 트랙 2개 분리.**
  - **Track A = 재미/엔진** — 쇼러너가 판단. 수용/기각 가능.
  - **Track B = 오류 게이트** — 쇼러너 권한 밖. 숫자/레저/전수 기반. FLAG 있으면 LOCK 불가.
- 재미 좋아도 오류 통과 X. 쇼러너 마음에 들어도 포맷/정합/지문/대사 오류 통과 X.
- **"AI들이 괜찮다" 답변 금지.** 반드시 `분모 + 라인번호 + 판정 + 0 카운트`로 증명.
- **LOCK = 감상이 아니라 카운트.** Track B가 0이 아니면 LOCK 아님.

---

## ⚖️ 검수 강도 = 2 모드 (언제 무엇을 돌리나 · 2026-06-09)

**아래 Phase 2~9 풀 파이프라인(전수·적대·풀 패널)은 *최종 LOCK 단계용*이다. 매 수정마다 돌리면 토큰/시간 낭비.** 상황별로 무게를 바꾼다:

**① 경량 모드 (기본값) — 집필·재집필·가필·incremental 수정·"어떻지?/검토" 일상 점검**
- *바뀐 diff + 그 파급(연결된 setup/payoff·thread) + 기계 게이트(2A · voice_lint · continuity_lint)* 만.
- per-line 전수(2B·2C) · State Ledger 전수(2D) · 적대 다회(2E) · 풀 페르소나 패널 · cold-read 3회 = **안 돌린다.** 필요하면 fresh-eyes 1개를 *바뀐 구간 한정*으로만.
- **단, 집필 단계 자체가 1차 방어선** — 쓰면서 룰 적용(직전 동작 확인·대명사·일기 VO 회피·1컷 지문) = 하류 오류 예방. + voice_lint + 5렌즈 self-check.

**② 풀 LOCK 모드 (무거움) — 최종 LOCK 직전 / "철저 검토·매출 고점·광고소재력·외부 완성 대본" 명시 / 새 정본 *첫* 풀검수 / 큰 리라이트 후 첫 게이트**
- 아래 Phase 2A~2E 전수 + Track A 전체 + 쇼러너 merge + 수정·재게이트 루프 → LOCK Certificate.

**전환 판단:** 변경 작고 최근 풀검수 통과 = ①경량 / LOCK·대수술·외부 완성본 = ②풀. (LOCK 루프 *내부*의 Delta Re-Gate(Phase 6)는 이미 경량 — 수술 EP × 렌즈만.)

---

## Phase 0 — Source / Engine / Ledger Seed
- 기준본 확인: 정본 대본·청사진·비주얼락·핸드오프·프로젝트 writing lock (파일시스템 우선).
- **핵심 쾌감 엔진 1문단 고정** (예: SHE STOLE = 여성향 신분/얼굴 강탈 복수·도둑이 끝까지 진짜로 믿겨야 억울함이 산다·진실은 Mara 자백으로·펜던트/흉터는 *주인공 물증+Mara tell*이지 reveal 트리거 아님).
- **의도된 예외/저점(엔진 고정비용) 목록** 작성 → 모든 검수 프롬프트에 복붙(없으면 의도 설계를 결함으로 오인).
- **🚫 절대규칙: 천박함 ≠ 싸구려.** 막장 직설/저속 빌런/과잉 = 자산. 검수가 "싸구려/품위"로 깎으면 즉시 기각. 교체는 항상 더 천박/직설 쪽.
- **State Ledger 씨앗**: 추적 대상 전부 + 초기 상태 — 인물 위치·의상·소품·상처/흉터/낙인·문/창/패널·무기·지식 상태·시간/연속 태그·sex 체위/의상/신체위치·작품별 특수 금지/주의.

## Phase 1 — 5화 배치 집필/변환
- 직전 5화 강제 정독 → 다음 5화 집필/변환 → 인라인 QA → **멈추지 않고 마지막화까지** (5화 검수 = 인라인 QA지 승인 체크포인트 아님).
- 대사/묘사 최대 보존. 단 수정: 시적/일기 VO · 소설/연극 spoken · 물리를 *대체*하는 내면 지문(단 *동작의 감정 결*은 필수 유지) · 불명확 주체 · AIGC 오독 대명사 · 행동/공간/소품 상태 오류.
- 평시 검수 = voice_lint + 직접 한 줄 수술 + 5렌즈 self-check(구조/payoff·spoken·drawability·광고·writer). **풀 에이전트 패널 X(LOCK 때만).**

---

# Track B — 오류 게이트 (쇼러너 불가침)

## Phase 2A — Deterministic Mechanical Gate (LLM 판단 0)
숫자/grep로만. 항목: EP수 · S#수 · Characters수 · `[END HOOK]`수 · `Hard Cut.`수(=EP-1) · `have sex` 수/위치 · 깨진문자 `??` 0 · 한국어 잔존 0 · 금지/회귀 문구 0 · action-line 대명사 · 고아 태그 0 · 이중 separator 0 · END HOOK 아래 △ 1개 · 미허용 블록 태그 0 · char count 스펙내 · **프로젝트 금지어/주의어** · **작품별 금지 강조(예: `scale/scales`)** · `voice_lint.py --full`(METAPHOR/ANAPHORA/TRICOLON/MICRO_ACTING/KOREAN…) · `continuity_lint.py`. → 출력 = 숫자. 통과 = 전항 0/스펙내.

## Phase 2B — Per-Line Exhaustive Gate (가장 중요)
grep으로 **모든 Dialogue + 모든 VO + 모든 △** 번호 매겨 완전 추출(분모 확보) → 표 판정: `line# | text | PASS/FLAG | 사유 | 교체방향`.
- **Dialogue**: spoken English인가 · 인물 보이스 맞는가 · 연극/소설/묵독 문장 아닌가 · **AI더빙 톤-독립**(flat TTS로 한 의미 수렴? 반어/이중의미/의미심장/withheld = FLAG).
- **VO/Dialogue 판정 = *방식* 표준화 (예문 블랙리스트 금지·2026-06-09 교정).** **어떤 문장도 영구 GOOD/BAD 아님** (`The first night I chose`도 `This is crazy. But I'm not stopping`도 맥락 의존) — 5기준으로 판정: ①그 순간 사람 속마음/실제 발화처럼 들리는가 ②화면과 즉시 붙는가(없이도 이해되되 붙으면 더 셈) ③일기/테마/작가요약처럼 *안* 들리는가 ④`X. But Y.`·`I don't know X. I know Y.` 대구가 *자동으로 폼 잡는 독백*으로 안 들리는가 — **대구 = *주의 트리거*지 자동탈락 X**(맥락에서 폼이면 FLAG·날것이면 PASS) ⑤flat TTS로 읽어도 의미 즉시 박히는가(반어/이중의미/withheld = FLAG). (`Don't you dare`·`Look at me`도 *예문*이라 통과가 아니라 기준 통과라 통과.)
- **△ (감정 = 장면 구조에서·2026-06-09 최종 확정)**: 지문은 감정을 *설명하지 않는다.* **깨끗한 동작 + 그 동작이 만든 반응**만 쓴다. 감정은 여기서 옴 → ①직전 대사/상황 ②인물의 실제 행동(중립 축 — ①③④가 의미를 입힘) ③주변 인물의 반응 ④그 반응이 만든 위험/권력/긴장. **동작 줄에 감정 주입 ❌**(전부 작가의 의미 덧칠·대본 지문으로 별로): `for the first time`·`instead of looking away`·`angry now`·`jaw tight, eyes wet`·`steps into her space`. ✅ 원본형: `Isolde steps toward Adeline.` / `The guard moves.` / `Aldric lifts one hand.` / `The guard stops.` — 감정어 없이 *반응*이 그 다가감을 세게 만든다. **컷이 밍밍하면 지문에 감정 형용사 바르지 말고 *대사·상황·반응*을 고친다.** (반응할 인물 없는 솔로 비트면 ③ 빠지고 ①②④ + VO가 운반 — 반응은 4소스 중 하나지 필수 아님.) ECU 얼굴 insert만 물리 얼굴동작이 본체(`wrong answer` 류 판단어 금지).
- **분모 의무**: `312/312 checked` 식. 분모 없는 "문제 없음" = 무효·재실행.

## Phase 2C — State Ledger Continuity Gate (제일 큰 사고 차단)
**모든 △를 순서대로 밟으며** Ledger 갱신 + 직전 상태와 대조: 누가 어디 · 옷 입음/벗음/어디(몸·바닥·침대) · 눈 뜸/감음 · 문/창 열림/닫힘 · 손 위치 · 칼/편지/낙인/상처 위치 · 누가 뭘 아는가 · 직전컷↔다음컷 물리 연결.
- 오류 유형: 물리 불가능 · 앞 동작 충돌 · 소품 순간이동 · 옷 on/off 충돌 · 눈 순서 오류 · 문 상태 오류 · 주체/대상 불명확 · 정보 선후 오류 · 동기 붕괴.
- 출력 = 씬별 Ledger 표 + 충돌 `라인A ↔ 라인B` + 유형 + 수정방향. **"AI 보기엔 괜찮음" 금지 — 레저 기준 충돌 여부만.**

## Phase 2D — Adversarial Error Pass ("AI 괜찮다" 구조적 차단)
검수 프롬프트 강제: ❌"정합성 괜찮아?" → ✅**"오류 최소 1개 있다고 가정하고 찾아라 · 불확실하면 PASS 아닌 FLAG · 분모 없이 CLEAN이면 무효."**
- 렌즈: continuity · AIGC drawability · spoken English · production format · sex motion/body logic.
- **독립 다회(fresh context) — 1회 "이슈없음" = CLEAN 아님. 전원이 못 찾고 + 분모 검사 있어야 CLEAN.** (3 AI가 다 "괜찮다"던 실패 모드를 구조로 거부.)
- 판정자: continuity_logic_auditor · aigc_production_director (+ fresh-eyes-auditor).

---

# Track A — 재미/엔진 (쇼러너 중심·but 오류 못 덮음)

## Phase 3 — Genre / Pleasure / Commercial
- 장르 쾌감 · 초반 락인(EP01 15초/EP01-03) · 무료회차 결제유도 · 첫 유료 보상 · 모욕/핍박 강도(비트 4+·폭행 성별룰) · 여주 감정반응(쿨찐 X) · 남주 알파 매력 · 섹스 여성향 high-heat 보상/female gaze · 캐릭터 미감/체격차 · 광고 4~10분 조립 mini-arc packet.
- **cold-read 1회=노이즈 → 독립 3회 수렴(funnel-cold-reader).** 저점은 "수술 가능" vs "엔진 고정비용" 분리.
- **set-piece 장르 캘리브**: 로맨스에 보스전 결말 요구 금지 — set-piece = 공개모욕/신분반전/claim/intimacy payoff/라이벌 몰락.
- 판정자: genre_pleasure · female_viewer_diagnostic · intimacy_auditor · commerciality_marketing · persona-reviewer. **지적은 쇼러너 수용/기각 가능·단 Track B 못 덮음.**

## Phase 4 — Showrunner Merge
모든 의견 병합 → 분류: HARD ERROR · FIX REQUIRED · MED/WATCH · NO FIX · REJECT.
- 집행 렌즈 순서: **엔진 충돌 먼저 · line 마지막.** 교체는 더 천박/직설 쪽.
- 쇼러너 권한: 장르 쾌감 판단 · 과잉 세련화 방지 · 외부 AI 틀린 피드백 기각 · 통합.
- 쇼러너 금지: 기계/물리/연속성/spoken/AIGC 오류 무시. **Track B FLAG = 자동 FIX REQUIRED.**
- **🔑 쇼러너 증명 의무**: Track B를 "오류 아님"으로 기각하려면 5조 중 하나로 *증명*: ①앞뒤 지문으로 물리 가능 ②인물 지식 선후 맞음 ③AIGC 컷 생성 가능 ④spoken English로 실제 들림 ⑤장르 허용·제작 오독無. 증명 못 하면 수정. **"재밌으니까" = Track B 기각 사유 불가.**

## Phase 5 — Fix Pass
순서: ①Track B HARD ERROR ②Track B FIX REQUIRED ③spoken/VO hard failure ④AIGC drawability hard failure ⑤Track A 수용분 ⑥MED/WATCH 중 효율 좋은 것. 최소 범위 수정.
- **수정 thread map**(고친 줄만 X): 옷 수정 → 씬 전체 옷 상태 / 문·창 → 공간 동선 / 대사 → 캐릭터 보이스+앞뒤 감정 / sex motion → 체위·손·다리·시선·의상. + 앞뒤 10~20줄·해당 EP 전체·관련 이전/이후 EP thread.

## Phase 6 — Delta Re-Gate
수정 기준 재실행: 기계 게이트 *전체*(싸니까 매번) · per-line은 수정 EP 중심 · State Ledger는 수정 씬 + 연결 씬 · 필요시 관련 이전/이후 EP(예: EP46 reveal 수정 → EP1·9·25·45 재확인). **새 오류 생기면 Phase 5로.**

## Phase 7 — Full LOCK Gate (Certificate)
**Track B (전부 0·분모 증명):** mechanical 0 · format 0 · forbidden phrase 0 · broken char 0 · Korean 0 · action pronoun 0 · END HOOK multi-shot 0 · per-line Dialogue FLAG 0 · per-line VO FLAG 0 · per-line △ drawability FLAG 0 · State Ledger contradiction 0 · continuity_lint 0 · voice_lint 0(또는 baseline 예외 명시).
**Track A:** 핵심 쾌감 훼손 0 · 초반/무료/유료보상 기능 통과 · 광고 packet 존재 · 장르/타깃 매칭 · cold-read 3회 안정.
**둘 다 동시 만족할 때만 LOCK.** LOCK Certificate = 위 전항 카운트 + MED/WATCH 잔존 내역·왜 LOCK 차단 아닌지.

**🚨 루프 종료(수렴) 기준 — 주관적 스타일 렌즈는 0으로 수렴 안 한다 (2026-06-09 학습):** 대명사-뻣뻣함·감정라벨 지문·미세 VO톤 같은 *주관적 스타일* 렌즈는 *무한 long-tail* — 매 패스마다 동급 nitpick을 새로 생성한다(SHE STOLE: 1회차 78→2회차 71, HARD만 1→0). 끝까지 0으로 쫓으면 = **대본을 밋밋하게 다림질(과교정·claude-voice-bias 역방향).** 따라서 **루프 종료 = ①HARD/에러 0(이건 진짜 수렴·반드시) + ②엔진 무손상 + ③기계게이트 PASS + ④스타일은 *진성 substantive 처리 + diminishing returns 도달*.** "스타일 nitpick 0"은 LOCK 기준이 아니다. 잔존 스타일 long-tail = 문서화·비차단.

---

## 도구 (결정론 — 유일 100% 신뢰층)
- `tools/voice_lint.py` — 문학톤/미세표정/한국어 기계 탐지.
- **`tools/continuity_lint.py` (빌드 필요)** — action-line 대명사 · 의상/소품 on/off 토글 · `shirt/dress/cloak/window/door/knife/wrist/mark` 상태어 추적 · END HOOK 아래 △ 개수 · sex marker 위치 · 금지/회귀 문구 · project-specific forbidden emphasis · 같은 씬 내 상태 충돌 후보. (완전 자동 무결은 아니나 "기초 오류 조용히 통과"를 크게 줄임.)

## 역할 권한
| 역할 | 권한 | 하드블록? |
|---|---|---|
| showrunner | 재미·장르·쾌감·최종 병합 | Track A만. 오류엔 veto 無(증명 의무) |
| final-consolidator | 숫자/포맷/기계 게이트 | ✅ 쇼러너보다 하드 |
| continuity_logic_auditor | 정합/논리/레저 | ✅ 물리/논리 사유 없이 기각 불가 |
| aigc_production_director | drawability/제작성 | ✅ AIGC 생성 불가 = 하드 차단 |
| english_dialogue_voice_auditor / native-ear | spoken/VO | ✅ spoken failure = 하드 차단 |
| genre_pleasure / female_viewer / intimacy / commerciality | 재미/매출/감정 | Track A (진단·쇼러너 수용/기각) |

## 운영 원칙
- "괜찮다" 금지 — "몇 줄 중 몇 줄 검사·몇 개 FLAG"만 인정.
- 쇼러너 = 재미의 최종 결정자 / 오류 게이트 = 쇼러너보다 위.
- LOCK은 카운트. Track B ≠ 0 → LOCK 아님.
