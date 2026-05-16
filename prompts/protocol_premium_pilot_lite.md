# Premium Pilot Protocol Lite v1 (2026-05-16)

**상태:** Production. 옛 `protocol_premium_pilot.md` (19 step) 대체. 무료회차 EP1-8 작업 시 본 prompt 사용.

**근거:** 옛 19-step protocol은 시간·토큰 5-10배 소모하나 결과는 protocol 없던 시절과 유의미한 차이 없음. 매출 영향 거의 0인 7 step (2·3·4·5·6·13·14·19) 폐기. 19 → 7 step (63% 단축).

**모델:** Claude Opus 4.7 / Effort: max

---

## 라우팅

phase_4·5·6·7 prompt에서 무료회차 EP1-8 호출 시 본 prompt로 자동 분기 (기존 protocol 라우팅 룰 그대로 — 본 prompt가 옛 protocol 대체).

---

## 0. 목표·소스

**목표:** 북미 paid vertical 시청자가 결제로 전환되는 무료회차 EP1-8 (75-80분 무료 분량) + Pilot Bible.

**허용 소스:**
- 청사진 `projects/[작품]/[작품]_04_blueprint_full.md` (절대 락)
- 비주얼 락 `projects/[작품]/[작품]_04_visual_lock.md`
- 본 protocol run 안에서 생성된 artifact

**금지 소스:**
- 이전 protocol 실행 결과물 (옛 premium_pilot/·premium_pilot_v2/·version_b/c/d/e — fresh 재작성 시)
- 외부 AI 출력물 (워싱 안 된 상태)

---

## Artifact Tree

```
projects/[작품]/premium_pilot_lite/
  01_reference_floor.md
  02_voice_anchor_merge_brief.md
  03_rewrite/
    ep01.md ... ep08.md
  04_scoped_pass.md
  05_persona_adversarial.md
  06_gap_regen_final_gate.md
  07_pilot_bible.md
```

---

## Step 1. Reference Floor Lite

**5 항목만:**
1. 첫 10초 압박 종류·강도·방식
2. 정보 비대칭 (누가 무엇을 알고 누가 모르는가)
3. 페이월 직전 미완성 (회수 차단 방식)
4. 감정 압박 강도 (캐릭터 처지 변화 패턴)
5. Intimacy heat 단계·강도 (다크 로맨타지·high-heat 작품에서)

**금지:** 시드 풀 X. 4 draft 비교 X. 매트릭스 X. floor는 기능 명시만.

**산출:** `01_reference_floor.md`

---

## Step 2. Voice Anchor + Merge Brief 통합

### Voice Anchor

- 주요 캐릭터별 voice rule (cadence·금지 어휘·typical line shape)
- alpha possessive stylized cadence (다크 로맨타지 등 stylized 허용 작품)
- Native English 강제 (작품·캐릭터·세계관 fit 시 stylized OK)

### Merge Brief (EP1-8 spine)

- EP별 핵심 비트·핵심 scene·핵심 dialogue (한 줄 finishing 대사)
- Sensual 8 질문 매핑 (다크 로맨타지·high-heat 시)
- 결제 엔진 매핑 (`feedback_v3_17_payment_engines.md`)
- 무료 EP1-8 분량: 2-2.5분/EP (다크 로맨타지) / 2-3분/EP (남성향 액션)
- 청사진 화별 락 그대로 적용

**산출:** `02_voice_anchor_merge_brief.md`

---

## Step 3. Single-Author Rewrite EP1-8 (핵심)

**가장 중요한 단계 — 실제 집필.** N=1 직접 집필 (4 draft 시드 X).

### 🔥🔥 필수 정독 매출 baseline (2026-05-15·16)

집필 진입 전 정독:
- `feedback_paid_vertical_viewer_psychology.md` (사적 즐김·부끄러운 욕망+해소)
- `feedback_paid_vertical_6_conversion_patterns.md` (메인 1-2 + 보조 1-2 매핑 강제)
- `feedback_female_buy_engine_relational.md` (A/B 엔진) — 여성향
- `feedback_male_target_alpha_taboo_patterns.md` (알파 환상·회피 4) — 남성향
- `feedback_50_episode_serial_engines.md` (7 룰)
- `feedback_character_situation_appeal.md` (3축)
- `feedback_female_lead_agency_balance.md` — 여성향
- `feedback_reference_market_verification.md`

### 양식 v2 강제

```
EP[N] — [TITLE]

S#[번호] — [LOCATION / TIME or CONTINUOUS]

[VISUAL / ACTION]
(상황·동작·블로킹·시각 정보 통합. 스토리상 중요한 사운드 비트.)

[KEY CAMERA]
(스토리·상업 엔진 중요 컷만 — 2-5 cuts. 선택.)

[DIALOGUE]
CHARACTER: line (3-10 단어 이하)

[GRAPHIC / UI]    ← 필요 씬만
[END HOOK]        ← 회차 마지막 씬만
```

### 룰
- 청사진 절대 락 (인물·관계·페이월·화별 락)
- 비주얼 락 어셋 식별 (첫 의상·변경·재착용 시 묘사)
- 9:16 세로형 적합
- 매 EP 1+ 결제 엔진 작동
- 무료회차 압도적 중요 — 분량 압축 X / 깊은 비트·페이월 압력 누적
- EP8 페이월 = 붕괴 직전
- 수위 = 결제 엔진 (sensual 장면 8 질문 통과)
- mid-EP `Hard Cut` 마커 / 마지막 EP는 자연 엔딩 X (무료회차 마지막 EP8은 Hard Cut)

**산출:** `03_rewrite/ep01.md` ~ `ep08.md`

---

## Step 4. Scoped English + Heat Pass 통합

매 EP 통합 패스:

### English Pass
- 번역체 제거·과도 완전 문장 제거·설명 대사 제거
- Anti-AI dialect 제거 (em-dash 남용·"It wasn't X it was Y"·과잉 parallel structure·poetic phrasing)
- 캐릭터별 voice 일관

### Heat Pass (다크 로맨타지·high-heat 작품 한정)
- Sensual 8 질문 자가 검수 (모두 통과)
- mutual claim·금기 결속·소유감 적극
- 라인 레벨 디테일 (혀 얽힘·잇자국·머리채·옷 안)
- "절제" 표현 X

**산출:** `04_scoped_pass.md` (EP별 변경 내역 + 통과 verdict)

---

## Step 5. Persona Adversarial Review (핵심 5)

**페르소나 9 → 5로 축소.** 핵심 5만:

| 페르소나 | 영역 |
|---|---|
| **01 Intimacy** | sensual 8 질문·heat 단계·mutual claim |
| **02 AIGC Production** | 양식 v2·비주얼 락 어셋·EP 본문 영어 일원화 |
| **05 Commerciality** | 페이월·결제 엔진·광고 컷·고통-보상 장부 |
| **07 Genre Pleasure** | 장르 약속·캐릭터 매력·안전 밋밋 회피 |
| **09 Female Viewer** (or 08 Male) | 시청자 이탈 코드·작품 타깃 정렬 |

각 페르소나 verdict 4단계 + 등급 + 원문 FIND 인용 + 14 failure codes 자동 스캔.

**병렬 권장:** `persona-reviewer` subagent 5개 병렬 호출 → 메인 컨텍스트 절감.

**산출:** `05_persona_adversarial.md` (5 페르소나 verdict 통합)

---

## Step 6. Gap Regen + Final Pilot Gate

### Gap Regen
- Step 5에서 발견된 🔴/🟡 항목 EP별 패치 (최소 수정 단위)
- 청사진 환류 (더 강한 요소 발견 시)

### Final Pilot Gate

다음 항목 모두 통과 시 무료회차 LOCK:

| 항목 | 기준 |
|---|---|
| v3 12 HARD RULE | 1건이라도 fail = 4-Gate 진입 불가 |
| v3 14 Failure Codes | 검출 0건 |
| 양식 v2 일관성 | [VISUAL/ACTION] = scene count / 무료 EP8 = Hard Cut |
| 청사진 정합 | 인물·관계·페이월·화별 락 일관 |
| 비주얼 락 정합 | 어셋 식별 (첫·변경·재착용) 명시 |
| Korean 0건 | EP 본문 한국어 0건 |
| 분량 | EP1-8 합 16-24분 (무료회차 압도적) |

**산출:** `06_gap_regen_final_gate.md` (패치 내역 + Gate verdict)

---

## Step 7. Pilot Bible Lite

**1 페이지 (이전 protocol Bible의 1/5 분량):**

- 캐릭터 (3-5 주요): 한 줄 정체성 + 핵심 voice + 핵심 비주얼
- 관계 (1-3 핵심): 관계 변화 사이클 한 줄
- 세계관 (5 항목): 공간·권력·시스템·금기·페이월 구조
- 페이월: EP8 trigger + 유료 EP9 첫 보상 1줄
- 결제 엔진: 메인 1-3 + 보조 2-3 (v3 17)
- Voice 룰: 캐릭터별 cadence 1줄
- 시각 캐논: 핵심 색·소재·실루엣 1줄

**산출:** `07_pilot_bible.md`

---

## 무료 통합 최종고

Step 7 통과 직후 자동:
- `final-consolidator` subagent 호출
- `premium_pilot_lite/03_rewrite/ep01.md ~ ep08.md` → `07_final/[작품]_FINAL_FREE.md` 통합
- 검증: Korean 0건 / Hard Cut = 7 (EP1-7 mid + EP8 hard) / 양식 v2 일관성

---

## 옛 19-step Protocol과의 차이

| 항목 | 옛 19-step | Lite 7-step |
|---|---|---|
| Step 수 | 19 | 7 |
| 평균 시간 | 7-10h | 1.5-2h |
| 평균 토큰 | 200-300K | 30-50K |
| N (seed pool) | 4 (32 EP draft) | 1 (직접 집필) |
| 페르소나 검토 | 9 (Adversarial) | 5 (핵심) |
| Matrix·Scene Winner Map·Quoted Treasure·Blind Duel·Hybrid·Cold Read | O | 폐기 |
| 결과 (매출 영향) | Baseline | Baseline (동등 또는 ↑) |

## 핵심 한 줄

> **N=1 직접 집필 + 핵심 5 페르소나 검토. 옛 protocol 시간 70% 절감, 결과 동등 또는 우수.**
