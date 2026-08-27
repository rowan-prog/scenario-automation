# 워크플로우 지도 (2026-08-27 개선 설계 · Fable 1회성)

> **한 장 요약.** 무엇을 하든 ① 해당 권역의 **작성 skill**로 들어가 지침을 읽고 ② 산출은 **생성 유닛 ≠ 되감기 유닛 ≠ 판정 유닛**으로 나눠 만들고 ③ 나가기 전에 **검수 skill**을 통과한다. 메인(쇼러너)은 설계·문답·지시서·머지·판정만 — 프로즈를 직접 쓰지 않는다. 작업 모델 = opus/sonnet/haiku만.

## 0. 이 설계가 고친 것 (사용자 2026-08-27)

| 지적 | 뿌리 | 착지 |
|---|---|---|
| 로그라인을 하도 못 쓴다 → 실물 179건 제공 | 내가 실물 규격을 한 번도 안 봤다(13번 길이 4문장 = 로그라인 아님) | `50_logline_standard.md` + `50_logline_corpus.md` + `logline_lint.py` + `/logline` |
| 우회·암시 문장이 룰을 고쳐도 안 없어진다 | 판정을 쓴 내가 했다 — 맥락을 아는 나는 통과시킨다 | **독자 3종 게이트** = `plain-reader`(haiku·low) 재진술 `못 함` 0 → `/plain-gate` · CLAUDE.md 룰 7 |
| 라우팅이 흐리다 · 단일 agent로 돈다 | 절차가 문서에만 있고 호출 단위가 없었다 | **skill 10종**(작성 4 · 로그라인 1 · 검수 5) · CLAUDE.md 룰 8 (workflow fan-out은 예산 개정으로 폐기) |
| 지침대로 됐는지 검수가 없다 | 기획안·각색·검수 리포트가 무검수로 나갔다 | **검수의 검수** = `proposal-spec-auditor` · `adaptation-fidelity-auditor` · `review-auditor` → `20_review` §1④ |
| 모델·effort | fable 예외가 살아 있었다 | opus/sonnet/haiku만 · effort = 창의 low / 논리 high / 뇌오프 low / 집필 medium — agent 21종 `effort:` 핀 |
| 로그라인은 러프 기획안 안의 것이다 | "슬롯용 짧은 것 / 기획안용 긴 것" 갈래를 내가 만들었다 | 갈래 삭제 · 4문장 문단 폐기 · `/logline` = `/rough-proposal` 2단계 |
| 엔진을 내가 요약하면 장르가 바뀐다 | 29 시운전: "전처 리벤지"로 적자 판정 21건이 틀어짐 | 0단계 엔진 한 줄 = **사용자 문장** · 없으면 묻고 진입 |

## 0-1. 예산 — 절차 크기는 산출물 크기에 비례한다 (🚨 2026-08-27 사용자: "러프 기획안은 A4 1장짜리 산출물이다. 1/10로 줄여도 모자라다")

29번 v6 실측 = A4 한 장에 subagent 12기 · 약 110만 토큰 · 45분. 뿌리 = 절차가 산출물 크기와 무관하게 풀 벨트(3프레이밍 fan-out·후보 36·sonnet 판정·45항 체크리스트 2회)를 돌게 설계돼 있었다. **아래 상한은 하드다 — 넘기면 멈추고 사용자에게 보고.**

| 산출물 | 크기 | agent 상한 | 토큰 상한 | 시간 | 절차 |
|---|---|---|---|---|---|
| 로그라인 단독 | 한 문장 | **2** (opus 생성 1 · haiku 되감기 1) | 40k | **2분** | 후보 10 · lint · haiku · 메인 선별. sonnet 판정 유닛 금지 |
| **러프 기획안** | **A4 1장** | **2** (opus 작성 1 · haiku 되감기 1) | **80k** | **3분** (사용자: "5분도 길다") | opus 1기가 통째로 씀(규칙은 지시서 인라인 · 파일 정독 = p0·원안만) → lint·grep → haiku → 메인 10항 직접 대조 |
| 플랫폼 기획안 | docx 10필드 | 6 | 300k | 15분 | phase_p 유닛표 + `/proposal-review`(45항 전수·opus 3축) |
| 작가 발송본(기획안·트리트먼트·가이드) | 문서 | +2 | +150k | +10분 | `/proposal-review` + `/review-audit` — 외부로 나가는 것만 |
| 회차 집필 배치(3~5화) | 대본 | 5 | 300k | 15분 | opus 프로즈 1 + haiku 3 + 기계 |
| 각색 배치 | 대본 | 5 | 300k | 15분 | `/adapt` |
| 풀 LOCK | 50화 | §7 belt | 토큰 회계 §1 | — | `/script-review lock` |

**원칙:** ①A4 한 장은 메인이 직접 본다 — 체크리스트 유닛을 부르지 않는다 ②작성 유닛은 산출물당 1기 — 로그라인·셀링·트리트먼트를 따로 fan-out하면 각자 표준·코퍼스를 재정독한다(5기 × 80k) ③후보는 10개면 충분 — 36개를 만들고 130k로 판정하는 건 낭비지 품질이 아니다 ④재라운드 자동 트리거 금지 — 문장 단위 수정 ⑤**agent에 파일 정독을 시키지 않는다 — 규칙은 지시서 안에 인라인**(표준 5개 읽는 데 2~3분이 나간다 · agent가 여는 파일 = p0·원안·원작 해당 EP뿐) ⑥라운드 파일·판정표 생성 금지(러프) — meta 5줄 ⑦시간의 기준 = opus가 A4 한 장 쓰는 데 1분·haiku가 읽는 데 30초 — 그 이상은 절차가 만든 시간이다.

## 1. 권역 × 절차 (작성 → 검수 한 쌍)

| 권역 | 작성 skill | 유닛(모델·effort) | 게이트 | 검수 skill |
|---|---|---|---|---|
| 러프 기획안 (A4 1장) | `/rough-proposal <원안>` — **agent ≤2 · ≤80k · ≤3분** | **opus 1기가 통째로**(로그라인 후보 3 + 셀링 5~6 + 무료 8화 · 파일 직접 저장) · haiku 되감기 1 | `logline_lint` · 작업어·구설정 grep · 메인 10항 직접 대조 | (러프는 `/proposal-review` 안 태움 — 플랫폼·발송본 전용) |
| 플랫폼 기획안 | `/platform-proposal <p0>` | 안목 opus(high) · 훅·아크 opus(medium) · 트리트먼트 sonnet(low) · 시놉·캐릭터 sonnet · 메타 haiku | 기계 게이트 ①~⑩ | `/plain-gate` → `/proposal-review` → 빌드 |
| 각색 대본 | `/adapt <원작> <①\|②> [EP]` | 프로즈 opus(medium·원작 직역 나란히) · 잔재/골격 consistency-sweeper(sonnet·high) · 이중 귀 tts-literal-ear(haiku)+native-ear(opus·high) | `10_writing` §A-2 배치 게이트 | `/adaptation-review` → `/script-review light` |
| 회차 집필 | `/write-episodes <작품> <EP>` | 프로즈 opus(medium) · haiku 3종(low) · 통합 final-consolidator(sonnet) | 배치 기계 게이트 7종 | `/script-review` |
| 대본 검수 | — | `20_review` §7 belt (모드별) | Track B | `/script-review <대본> [light\|lock\|external\|writer]` → 외부 발송이면 `/review-audit` |
| 로그라인 단독(반려 후 재라운드) | `/logline <작품>` — **agent ≤2 · ≤40k · ≤2분** | copy-candidate-generator(opus·low) 1기 후보 10 → `logline_lint` → plain-reader(haiku) → 메인 3 선별 | 자수·문장·금지어 | (sonnet 판정 유닛·workflow fan-out 폐기) |
| 모든 한국어 산출물 | — | plain-reader(haiku·low) | 재진술 `못 함` 0 | `/plain-gate <파일>` |
| 검수물(리포트·코멘트·반박서) | — | review-auditor(opus·high · 리포트 안 쓴 인스턴스) | 지적별 7항 | `/review-audit <리포트> <원문>` |

## 2. 유닛 21종 — 성격별 (`~/.claude/agents/` · frontmatter `model:`+`effort:`)

- **생성(창의 · low):** copy-candidate-generator(opus) · idea-diverger(opus)
- **되감기·뇌오프 프록시(low · 덜 이해할수록 정확):** plain-reader(haiku) · tts-literal-ear(haiku) · aigc-draw-auditor(haiku) · funnel-cold-reader(sonnet) · persona-reviewer(sonnet) · branch-playtest-reader(opus)
- **판정·대조(논리 · high):** logline-auditor(sonnet) · proposal-spec-auditor(sonnet) · adaptation-fidelity-auditor(sonnet) · review-auditor(opus) · consistency-sweeper(sonnet) · fresh-eyes-auditor(opus) · native-ear-reviewer(opus) · evaluator-panel(opus) · external-intake-evaluator(opus) · worldtree-graph-auditor(sonnet)
- **집필·추출·통합(medium):** script-surgeon(opus) · mkt-selling-point-extractor(sonnet) · final-consolidator(sonnet)

## 3. 위치

- 라우팅 표·룰 7·8 = `CLAUDE.md` · 절차 = `.claude/skills/<name>/SKILL.md` 10종 · **예산 상한 = §0-1**
- 표준 = `config/00_vertical_dna.md`(원리) · `10_writing_standard.md`(집필 · §D-2-1 ⑧ 독자 3종 게이트) · `20_review_standard.md`(검수 · §1③ 기획 문서 · **§1④ 검수의 검수** · §7 effort) · `30_writer_feedback_standard.md` · `40_selling_point_standard.md` · **`50_logline_standard.md` + `50_logline_corpus.md`**
- 기계 = `tools/logline_lint.py`(신설) + 기존 lint 7종 · 메모리 = [[logline-catalog-slot-corpus]] [[three-readers-rewind-zero-gate]]

## 4. 운용 원칙 세 줄

1. **이 룰을 누가 재는가?** 내가 재면 안 지켜진다. 게이트(기계·다른 유닛) 없는 룰은 소원이다.
2. **엔진·규격은 사용자 문장과 실물에서.** 내가 요약·발명하면 장르가 바뀐다.
3. **작성과 검수는 한 쌍.** 어느 권역이든 검수 skill을 안 거친 산출은 안 나간다.
