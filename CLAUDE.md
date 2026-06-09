# 시나리오 자동화

AIGC 숏폼 vertical drama 시나리오 제작. 최종 산출 = `projects/[작품]/07_final/[작품]_FINAL_v{N}.md`.

---

## 어디서 무엇 찾는지 (이 파일은 인덱스만)

| 필요 | 위치 |
|---|---|
| Hard rule 12개 | `config/hard_rules.md` (1페이지·매 phase 진입 시 정독) |
| Phase별 prompt | `prompts/phase_*.md` (단계 진입 시) |
| 작품 진행 메타 | `projects/[작품]/[작품]_00_meta.md` |
| 검증 히트작 raw 대본 | `config/vertical_drama_hit_scripts/` (집필 시 매칭 작품 3-5 EP raw 강제 정독) |
| 히트작 분석 | `config/vertical_drama_hit_scripts_analysis/` |
| 페르소나 | `config/personas/` (검토 시점만) |
| 평가위원 | `config/evaluators.md` (피칭 시점만) |
| 타깃 자료 | `config/target_research/[성별]_target_research.md` · 권역 인사이트 = `es/jp_region_insights_2026-06.md` |
| 비주얼 락 템플릿 | `config/visual_lock_template.md` |
| Reference 인덱스 | `config/reference_scripts/INDEX.md` |
| 시스템 baseline 메모리 | `memory/` (always-load 3개만·MEMORY.md 참조) |
| 상태·정합성 도구 | `prompts/status.md` · `prompts/audit.md` |
| 검수 agent 7종 + 운용 룰 | `~/.claude/agents/` (정의) · **`config/agent_operating_rules.md` (운용 단일 진실)** (LOCK 전 최소 = voice_lint + fresh-eyes-auditor + cold-read 3회 수렴) |
| 최종고 검수 흐름 | **`config/final_review_flow.md`** (10+3패스·단일/sub-agent 모드 기준·쇼러너 merge·**절대 규칙: 천박함 ≠ 싸구려**) |
| 핸드오프 템플릿 | `config/production_handoff_template.md` (titan v169 양식·영어·LOCK 후 환류 시) |
| 마케팅 셀링포인트 템플릿 | `config/mkt_selling_points_template.md` (BUMP 엑셀 양식·전회차 트리트먼트+MKT IDEA·LOCK 후 마무리 산출물) |

> **master_guide_v3.md (5816줄) = 시스템 백과·집필 컨텍스트 진입 금지.** Hard rule 12개는 `config/hard_rules.md`에 추출됨.

---

## 워크플로우

```
phase_0 (아이디어) → phase_1 (러프 청사진) → phase_2 (피칭) → 피칭 결과
  → phase_3 (완성 청사진 + visual lock) → phase_4 (Conversion Runway 집필)
  → phase_5 (페르소나 검토) → phase_6 (패치) → phase_7 (최종고)

부가 트랙: phase_a (각색) / phase_b (외부 대본) / phase_c (외부 피드백)
```

---

## 작품 파일 명명 규칙 (필수)

`projects/[NN]_[slug]/[NN]_[slug]_[단계번호]_[단계명].md`
- 폴더 prefix = 폴더명 동일
- 하위 폴더 (`05_episodes/`·`06_reviews/`·`07_final/`) 안 파일도 prefix 적용
- 폐기 폴더 = `_X_NN_slug` prefix (자동 차단)

---

## 현재 작품 (2026-05-21)

| 폴더 | 작품 | 현재본 (정본) | 단계 |
|---|---|---|---|
| `_X_01_titan_born` | TITAN BORN | (외부 진행) | **🚫 폐기 — 외부 별도 진행 (2026-06-02)·작업 금지** |
| `_X_02_the_offering` | THE OFFERING: Claimed by the Dragon Lord | **🎬 `07_final/02_the_offering_FINAL_v68_dialogue_surgery.md`** | **🚫 폐기 — 외부 별도 진행 (2026-06-02)·작업 금지.** v68 = 대사·VO surgery 최종본(5217 lines·Korean 0·EP 50/50·sex scene 7건 보존). 상세 이력 = `02_the_offering_00_meta.md`(CLAUDE.md 원문 이관 포함). |
| `03_most_wanted_ship` | I BOUGHT THE GALAXY'S MOST WANTED SHIP | (07_final 확인 필요) | phase_2 완료 |
| `_X_04_heiress_clause` | I AM THE HEIR | — | 폐기 |
| `06_she_stole_my_face` | SHE STOLE MY FACE | **🟡🎬 `07_final/06_she_stole_my_face_FINAL_v48.md`** (2026-06-09 · **LOCK-ready · 사용자 교차검수 대기**) | **현행 정본 = v48 = AIGC △ 프롬프트-제작양식 전면 변환. 풀 파이프라인(기계게이트+적대 Track B+cold-read Track A) 전부 통과 = LOCK-ready. 단 *진짜 LOCK = 사용자 교차검수 후 확정*(자가판정 단독 LOCK 금지 — [[claude-voice-bias-vertical-failure]]). Track A 패치 5개(EP9/30/31/35/48)는 신규 작성분이라 교차검수 필수.** v47(구 [KEY CAMERA]/[VO] 블록양식)→v48 = 매 컷 1프롬프트 △ 양식(EP-S#·Characters·△ atomic·고유명·[END HOOK]→훅컷·메타0). **LOCK 파이프라인(`config/lock_pipeline_standard.md` 단일 진실):** ①Phase 2A 기계게이트 PASS(50EP·씬87·HC49·END HOOK49·Korean0·action-pronoun0·포맷클린·분모 대사393/VO31/△542) ②Track B 적대 에러게이트(10 에이전트·분모 제시·76 flags)→쇼러너 merge: HARD 11(Continuous 텔레포트·LIVE 시간모순·EP20 중복아이디어·"he"=Ethan 모호·aisle 방향·상처 lip↔hairline·EP41 INTERCUT 누락·"Tonight"↔주간) + FIX 11(내면-대체 지문·posed VO·recap) + WATCH 14 수정 = **진성오류 0** ③Track A cold-read 3회+페르소나(engine_intact=True·"PATCH THEN LOCK"·전원 EP8 결제 YES)→수렴 약점 패치: EP9 첫유료=헌터각성·EP30 공회전→Lena 능동 reporter 크랙(남는 승리)·EP31 reshape(잠입 반복→의심이 Mara에게·staircase)·EP35 gloat중복 제거→공개 TV 함정·EP48 트리거 막장 taunt화 ④델타 적대검수→reporter 스레드 정합(EP9 hands lie→10 계획→30 전달→35 공개 결실)·확인 cold-read(EP9 7·EP30 7·EP35 8·남는 승리 확인) ⑤voice_lint: METAPHOR2(씬타이틀+엔진모티프 "wearing my mother"·≤baseline3)·MICRO_ACTING0·Korean0·"I love you"2·97,018 chars(AIGC 제작양식이라 대사 70-80k spec 미적용). 엔진 = impostor-believed 막장(시청자 EP01부터 전모·세상 EP48까지 가짜 믿음·진실=증거X Mara 자백·악역 천박/뻔뻔/멍청). 50EP·페이월 EP8·HC49·END HOOK49(EP50 자연 END). 핵심 메모리 = [[vertical-revenge-impostor-believed-engine]]·[[easy-dopamine-over-logic]]·[[emotion-to-action-aigc-writing]]·[[aigc-prompt-script-writing]]. **이전 양식(v30→v47) 이력·수술 상세 = `06_she_stole_my_face_00_meta.md`. 잔존 WATCH(~40 intended-design: 흉터 tell·pendant 소유·Lena 불신=엔진) = LOCK 비차단·문서화.** |
| `_X_08_reborn_at_ten` | REBORN AT TEN | — | 폐기 |

새 작품 번호 = **09**.

> **현재본 단일 진실:** 각 작품의 `07_final/[작품]_FINAL_v{최신N}.md`. 메타 파일·CLAUDE.md 모순 시 → *파일 시스템 우선*. 메타 즉시 갱신.

> **메모리 위치 주의:** workspace 안에 `memory/` 폴더 *없음*. 실제 위치 = `C:/Users/Rowan/.claude/projects/C--Users-Rowan-scenario-automation/memory/`. `memory/feedback_*.md` 참조 = 그 위치를 의미.

---

## 룰

1. **묻지 말고 자율 진행.** 비가역 (캐논 변경·작품 이름 변경·대량 삭제·Hard Lock 변경)만 사전 확인.
2. **검증 보고서·테이블·자가 검수 풀이 = 본문 외 작성 금지.** 메타 분량 = 본문 톤 침투의 근본 원인.
3. **집필 컨텍스트 = raw drama prose 우선.** 매 phase_4 진입 시 매칭 히트작 3-5 EP + 이전 EP 3개 raw 정독 강제.
4. **EP 본문 = 영어 100% (한국어 0건).** EP 외 메타·footer·로그도 영어 권장.
5. **사용자 질문 시 PushNotification** (200자 이내·결정/입력값/블로커).

---

## 모델·세션

Opus / High effort. 시작 시 `/model` 확인. 본문 영어·대화 한국어.
