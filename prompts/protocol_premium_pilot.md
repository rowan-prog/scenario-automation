# Premium Pilot Protocol v5.2

**상태:** Production-ready. **무료회차 EP1-8 작업 시 필수 호출** — phase_4·5·6·7을 통째로 대체하는 orchestration spec. 유료회차 EP9-50은 Step 20-22 운영 (phase_4~7은 그대로 사용 + protocol 가이드 적용).

**라우팅:** phase_4·5·6·7 prompts 모두 본 protocol로 자동 분기 룰 등재 (호출 키워드 매칭 시 본 protocol로 진입).

**모델:** Claude Opus 4.7
**Effort:** max (단일 effort 통일)

---

## 0. 목표·기준·소스 정책

### 0-1. 목표
북미 타깃에게 팔리는 무료회차 (EP1-8) 완성본 + 유료회차 (EP9-50) 통제 base 확립.

### 0-2. 기준

**Red gates (통과 필수, 1-5 절대 척도 기준 ≥4):**
- Native English
- Continuity

**상업성 5축 (가중 우선·최대화):**
- Viewer Pull
- Paywall Force
- Character Desire
- Romance Heat
- Native English

**그 외 4축:**
- Visual Specificity
- Pace / Hook Density
- Genre Pleasure
- Continuity

최종 품질 = "정합성 있는 글"이 아니라 **"북미 타깃이 계속 보고 결제할 글"**.

### 0-3. 소스 정책

**허용 소스:**
- 청사진 (`projects/[작품]/[작품]_03_blueprint_full.md`)
- 비주얼 락 (`projects/[작품]/[작품]_04_visual_lock.md`)
- 레퍼런스 floor (`config/reference_scripts/` — 기능 추출만, 문장·구조 복제 금지)
- **Working material** = 현재 protocol run 안에서 생성된 seed / rewrite / matrix / treasure / brief / bible / gate report

**금지 소스:**
- **이전 protocol 실행 결과물 (version_A / B / C 등)** — blind contamination 방지
- 외부 AI 출력물 (워싱 안 된 상태)

### 0-4. Artifact Tree

```
projects/[작품]/premium_pilot/
  01_reference_floor.md
  02_seeds/
    draft_a_visual.md
    draft_b_voice.md
    draft_c_paywall.md
    draft_d_heat.md
    floor_check.md
  03_table_read.md
  04_matrix.md
  05_scene_winner_map.md
  06_quoted_treasure.md       ← Raw / Approved 분리
  07_voice_anchor.md
  08_merge_brief.md
  09_cut_list.md
  10_rewrite/
    ep01.md ... ep08.md
  11_scoped_english_pass.md
  12_scoped_heat_pass.md
  13_blind_duel/
    ep01.md ... ep08.md
  14_hybrid_finalization/
    ep01.md ... ep08.md
    treasure_v2.md
  15_persona_adversarial_review.md
  16_gap_regen/
    [scene_id].md
  17_final_gate.md
  18_pilot_bible.md
  19_cold_read.md             ← EP9 full + EP20 outline
  20_amendments/
    [amendment_id].md
  22_coherence_gate/
    ep09.md, ep10.md, ...     ← 3-layer (Polish / Spot Check / Heavy)
```

각 Step은 이전 Step artifact를 read + 자기 결과를 고정 artifact로 write. 세션 끊겨도 재진입 가능.

---

# I. Pilot Protocol (무료회차 EP1-8)

## Step 1. Reference Floor Definition

**입력:** 청사진 / 비주얼 락 / 레퍼런스 (Demon Lord·LOCKED OUT 등)

**처리:** 작품 장르·타깃·포맷에 부합하는 **기능 floor만** 명시.

**추출 대상 = 기능 (모방 X):**
- 첫 10초에 어떤 압박이 걸리는가 (압박 종류·강도·방식)
- 정보 비대칭이 어떻게 생기는가 (누가 무엇을 알고 누가 모르는가)
- paywall 직전 어떤 미완성을 남기는가 (회수 차단 방식)
- 감정 압박 강도 (캐릭터 처지 변화 패턴)
- 장면 밀도 (회차당 비트 수·전환 빈도)
- intimacy heat (해당 시 — 단계·강도 패턴)

**금지:**
- 레퍼런스 작품의 실제 문장·대사 인용 floor 박기 X
- 고유 장면 구조 (특정 장소·소품·인물 배치) 복제 X
- 설정 (캐릭터 이름·세계관 요소) 차용 X

레퍼런스는 **"이런 기능이 floor 수준이다"**를 가리키는 용도. 모방용 X.

**출력:** `01_reference_floor.md` (기능 항목별 floor 명시)

## Step 2. Diverse Seed Pool 생성 + Floor 검사

**입력:** `01_reference_floor.md` / 청사진 / 비주얼 락

**처리:** EP1-8 fresh draft × N=4

| Draft | 강조 |
|---|---|
| A | visual brutality, first-frame hook, close-up impact |
| B | native English voice, dialogue economy, performable lines |
| C | paywall force, information asymmetry, EP-end hook |
| D | romance heat, desire escalation, physical tension |

동일 prompt 반복 금지. 각 draft는 후보 원고가 아니라 **강점 채굴용 시드**.

생성 후 floor 검사 — 미달 draft는 약점 가시화 후 재생성. **모든 draft floor 통과까지 Step 3 진입 금지.**

**출력:** `02_seeds/draft_a.md` ... `draft_d.md` + `02_seeds/floor_check.md`

## Step 3. Draft-Level English Table Read

**입력:** Step 2 산출 4 drafts

**처리:** 각 draft에 영어 자연스러움 검사:
- 번역체 제거
- 과도하게 완전한 문장 제거
- 설명 대사 제거
- 캐릭터별 말투 분리
- 배우가 입으로 말 가능한 리듬 확인
- **Anti-AI dialect:** em-dash 남용·반복적 대구·"It wasn't X, it was Y" 패턴·과잉 poetic phrasing·과도한 parallel structure

**판정:**
- Native English 통과 draft → 전체 winner 후보 + Approved Treasure 출처 자격
- Native English 미달 draft → scene 기능·visual 재료로만 제한 사용, **verbatim 보존 불가**

**출력:** `03_table_read.md` (draft별 통과/미달 + Approved 자격 표시)

## Step 4. Multi-Axis Matrix

**입력:** Step 2 drafts + Step 3 판정

**처리:** 축별 전문 페르소나가 독립 채점

| 축 | 페르소나 |
|---|---|
| Viewer Pull | 09 |
| Paywall Force | 05 |
| **Native English** | **04 + 고정 framing prompt (아래)** |
| Romance Heat | 01 |
| Character Desire | 01 + 04 |
| Visual Specificity | 06 |
| Pace / Hook Density | 02 |
| Genre Pleasure | 07 |
| Continuity | 03 |

**Native English 축 고정 framing prompt:**

```
역할: native US/Canada dialogue editor
기준: mobile short-form drama (ReelShort·NetShort·DreameShort·MoboReels 등)
우선순위: performability > grammar

즉시 감점:
- translation smell
- AI dialect (em-dash 남용 / "It wasn't X, it was Y" 반복 /
  과잉 parallel structure / 과도한 poetic phrasing)
- stiff fantasy English (mock-archaic, "thee/thou", medieval pastiche)
- 책 narration tone (배우가 입으로 못 내는 문어체)

판단 기준: "북미 배우가 실제로 입에서 낼 수 있는 라인인가?"
문법 정확성보다 spoken naturalness 우선.
```

이 framing 안 박으면 "문법적으로 맞지만 안 팔리는 영어"가 통과됨.

**채점 규칙:**
- Draft 순서 무작위화
- 절대 척도 1-5
- Draft 간 상대 비교 금지
- Continuity / Native English = red gate (≥4 통과)
- 상업성 5축 가중 우선

**출력:** `04_matrix.md` (draft × 축 매트릭스 + 가중 합산)

## Step 5. Scene Winner Map

**입력:** Step 4 매트릭스 + Step 2 drafts

**처리:** EP별·scene slot별 winner 지정. 기록:
- winner draft
- 선택 이유
- scene 기능
- 가져올 visual / dialogue / hook / intimacy beat
- 버릴 요소
- 다른 draft에서 보강할 재료

**출력:** `05_scene_winner_map.md`

## Step 6. Quoted Treasure (Raw / Approved 분리)

**입력:** Step 5 + Step 2 drafts + **Step 3 Native English 판정**

**처리:** 2-layer 분리 보존.

### Raw Treasure
모든 draft의 강한 기능 보유 line·비트:
- 강한 대사 (기능 우수)
- 강한 [Visual] · [Camera]
- EP-end hook line
- intimacy / desire beat
- 캐릭터 시그니처 반응

### Approved Treasure (verbatim 보존 허용)
Raw Treasure 중 **Native English 통과 draft 출신만**. Step 3 미달 draft의 line은 Approved 제외.

### 사용 룰
- **Approved Treasure** → Step 10 Rewrite에서 verbatim 보존 강제
- **Raw Treasure (영어 미달 출신)** → 기능만 보존. 같은 기능을 영어 통과 voice로 **재작성**

분리 안 하면 영어 미달 draft의 번역체가 최종본에 verbatim 침투.

**출력:** `06_quoted_treasure.md` (Raw / Approved 분리 섹션 + 출처 draft 기록)

## Step 7. Voice Anchor

**입력:** Step 4 / 5 / Step 2 drafts

**처리:** 캐릭터별 voice 출처 고정

**예시 형식:**
```
Piper: Draft B baseline + Draft D intimacy register
Ronan: Draft B baseline + Draft C threat cadence
Antagonist: Draft C pressure logic + Draft A visual menace
```

핵심 voice rule 3-5개를 캐릭터별 명시 (어휘·cadence·반응 패턴).

**Voice Anchor 없이 Step 10 Rewrite 금지.**

**출력:** `07_voice_anchor.md`

## Step 8. Merge Brief

**입력:** Step 5 / 6 / 7

**처리:** EP1-8 재집필용 설계도

포함:
- EP별 scene spine
- Scene Winner Map (`see Step 5`)
- **Approved Treasure** (`see Step 6` — verbatim 보존 강제 항목)
- **Voice Anchor: see Step 7** (핵심 voice rule 3-5개 짧게 복사)
- paywall promise
- 정보 공개 순서
- 캐릭터 감정 상태
- heat ladder
- hook ladder
- continuity locks

**출력:** `08_merge_brief.md`

## Step 9. Cut List Pass

**입력:** Step 8 Brief

**처리:** 강화 전 삭제·응축 우선. 삭제 후보:
- 기능 반복 비트
- 너무 명확한 foreshadowing
- 유료회차로 넘겨야 할 약속의 조기 해결
- 런타임만 차지하는 감정 설명
- 이미 보여준 관계 변화를 다시 설명하는 장면

Brief 업데이트 (삭제 결정 반영).

**출력:** `09_cut_list.md` + Brief 업데이트

## Step 10. Single-Author Rewrite

**입력:** Step 8 Brief (Step 9 업데이트 포함) + Step 6 Approved Treasure + Step 7 Voice Anchor

**처리:** EP1-8 전체를 한 작가가 새로 집필:
- 조립 티 제거
- voice 통일 (Step 7 anchor 엄수)
- 영어 리듬 통일
- scene 간 온도 정렬
- **Approved Treasure는 verbatim 보존**
- **Raw Treasure (영어 미달 출신)은 기능만 — 영어 통과 voice로 재작성**
- 북미 숏폼 드라마처럼 바로 재생되는 장면화

**출력:** `10_rewrite/ep01.md` ... `ep08.md`

## Step 11. Scoped English Pass

**입력:** Step 10 rewrite

**처리:** 전체 갈아엎기 금지. 문제 line·문제 scene만 **최소 수정**.

검사:
- native English (Step 4 framing prompt 동일 기준)
- performable dialogue
- translation smell
- AI dialect
- 캐릭터별 말투 붕괴
- paywall 직전 punch 약화

**변경 범위 명시 (track changes 식).**

**출력:** `11_scoped_english_pass.md` (변경 라인 목록 + 수정본)

## Step 12. Scoped Heat / Intimacy Pass

**입력:** Step 11 rewrite + Step 6 Raw Treasure (Draft D 라인 — 기능 참조)

**처리:** 결함 scene만 보강. 전체 편집 금지.

필수 회복:
- 물리적 순서
- 주도권 이동
- 상대 반응
- close-up shot
- consent가 행동/대사로 보임
- 장면 끝에서 욕망/권력/관계 변화 발생

**출력:** `12_scoped_heat_pass.md`

## Step 13. EP-Level Blind Duel

**입력:** Step 12 rewrite + Step 2 best seed draft per EP (Matrix 기준 EP별 가중 합산 1위 seed)

**처리:** EP별 blind 비교

**판정 기준:**
- Step 4 동일 축 사용
- 상업성 5축 가중 우선
- Continuity / Native English red gate 통과 필수
- EP 단위 승자 결정

**Rewrite 자동 승리 금지.**

**출력:** `13_blind_duel/ep01.md` ... `ep08.md` (per-EP 점수표 + 승자)

## Step 14. Hybrid Finalization

**입력:** Step 13 duel 결과

**Tie-breaker:** Step 13 가중 합산 차이 **< 0.3 = rewrite 유지** (voice 통일성 우선). seed는 명확 우열 시만 spine 승격.

**Seed 승리 EP 처리:**
- seed EP를 spine 지정
- rewrite의 그 EP에서 강한 line은 **Quoted Treasure v2** (Approved 자격 재검증 후)로 회수
- 해당 EP만 single-author pass로 재집필
- voice anchor = seed voice 기준 재고정

**Rewrite 승리 EP 처리:** 그대로 유지.

**출력:** `14_hybrid_finalization/ep01.md` ... `ep08.md` (final EP 본문) + `14_hybrid_finalization/treasure_v2.md`

## Step 15. Persona Review + Meta-Adversarial Review

### A. 9 페르소나 검토 — 미세 결함 hunting

표준 phase_5 검토 (페르소나 01-07 + 시청자 페르소나 작품 타깃에 맞게).

### B. Adversarial — 구조 결함 hunting

**운영 룰:**
- **별도 새 Claude 세션** (기존 persona 결과 미참조)
- 미세 문장 결함 금지 — 구조 결함만
- 프롬프트 고정: `"당신은 구조 결함 hunter다. 미세 문장 결함은 무시한다."`

**Adversarial 범위:**
- EP 순서 오류
- reveal 위치 오류
- hook 반복
- 굴욕 / reveal / 구원 패턴 반복
- agency arc 붕괴
- escalation curve 붕괴
- 장르 일관성 표류
- 무료 → 유료 결제 동력 부족
- 무료회차 약속 과다 (유료 회수 부담)

**출력:** `15_persona_adversarial_review.md`

## Step 16. Gap-Targeted Regen

**입력:** Step 15 결함 보고

**처리:** 결함 부분만 재생성.

**규칙: 단일 scene 고립 생성 금지.** 항상 컨텍스트로 포함:
- 이전 scene
- 문제 scene
- 다음 scene
- 해당 EP hook 목적
- 캐릭터 현재 상태
- 무료회차 전체 paywall promise
- voice anchor
- Approved Treasure 보호 목록

**출력:** `16_gap_regen/[scene_id].md` + EP 본문 업데이트

## Step 17. Final Pilot Gate

**통과 조건:**

| 항목 | 기준 |
|---|---|
| Viewer Pull | ≥ 4 |
| Paywall Force | ≥ 4 |
| Native English (red gate) | ≥ 4 |
| Character Desire | ≥ 4 |
| Romance Heat | ≥ 4 |
| Continuity (red gate) | **Persona 03 ≥ 4 + critical 결함 0건** |
| EP8 → EP9 결제 동력 | 명확 |
| Undocumented Yellow | 0건 (Documented Yellow 허용) |

**Critical continuity 정의:**
- 회차 간 정보 모순
- 캐릭터 정체성 / 동기 모순
- 핵심 소품 / 증거 위치 모순
- 약속한 hook의 회수 불능
- EP8 → EP9 연결 붕괴

**Minor continuity 정책:**
- 1-3건 허용, **단 문서화 필수** (의도적 보존인지·후속 회수 예정인지)
- **Unexplained minor 누적 시 red 승격**

**Yellow 0 강제 금지.** 의도된 Yellow는 사유 명시 후 보존.

**출력:** `17_final_gate.md`

### Step 17 통과 직후 자동 — FINAL_FREE.md 통합 (필수)

Final Pilot Gate 통과 시 즉시 `projects/[작품]/07_final/[작품]_FINAL_FREE.md` 자동 생성:

- 입력: `14_hybrid_finalization/ep01.md ~ ep08.md`
- 처리: `Get-ScriptBody` (post-script 제외) + EP 간 separator `---` + UTF-8 no BOM
- 검증: Korean=0 / Hard Cut=8 / 헤더 9 / 씬 = 청사진 명시 수 / 4 블록 일관성 (`feedback_final_consolidation_three_files.md`)
- 실패 시: 🔴 즉시 원본 수정 후 재생성

본 통합은 유료회차 진입 전 필수 단계. 무료 작품 완결 표지.

## Step 18. Pilot Bible 생성

**입력:** Step 14 최종본 + Step 6 / 7 + Step 17

**처리:** 무료회차 최종본에서 유료회차 통제용 bible 추출.

**필수 항목 (12):**
1. **Voice Book** — 캐릭터별 어휘·cadence·반응 패턴
2. **Character Desire Map**
3. **Continuity Bible** — 정보·소품·관계 상태
4. **Heat Ladder** — EP1-8 + EP9 이후 예상 진행 단계
5. **Paywall Ledger**
6. **Hook Library** — EP-end hook 정리
7. **EP1-8 End Promise Log** — verbatim
8. **EP8 → EP9 Bridge** — 다층 약속 (단기 / 장기 / sensual / power)
9. **Native English Style Rules** (Step 4 framing prompt 흡수)
10. **Forbidden Translation-Smell List**
11. **Best Scene Floor** — EP1-8에서 추출된 강도 기준
12. **Cut List Memory** — 왜 잘랐는지 (유료에서 재도입 금지 목록)

**출력:** `18_pilot_bible.md`

## Step 19. Bible Cold Read 검증 (2-tier)

**입력:** Step 18 Bible (단독)

### A. EP9 Full Cold Draft (필수)
무료 본문을 가린 **별도 세션**이 Bible만 보고 EP9 cold full draft 작성. Step 4 매트릭스 적용.

### B. EP20 Midpoint Cold Outline (필수 보강)
같은 cold session이 EP20 cold **outline**만 작성 (full draft 아님 — outline으로 충분).

**평가 항목:**
- Bible의 Heat Ladder가 EP20까지 유효한가
- Character Desire Map이 EP20에서도 일관된가
- Paywall Ledger가 중반에서 동력 유지하는가
- Voice Book이 EP20 캐릭터 진화 단계에서 적용 가능한가

**왜 EP20인가:** Bible이 EP9는 받지만 EP15+에서 무너지는 패턴이 실제 리스크. Midpoint(EP20)는 Bible의 50화 전체 지구력 시험.

### 판정
- EP9 cold draft + EP20 cold outline **둘 다 통과** → Bible OK
- 둘 중 하나라도 미달 → Bible 보완 후 재검증

**Pilot Bible 검증 없이 유료회차 진입 금지.**

**출력:** `19_cold_read.md` (EP9 cold draft + EP20 cold outline + 매트릭스 평가 + Bible 보완점)

---

# II. Paid Episodes Protocol (EP9-50)

## Step 20. Paid 회차 집필 운영

**입력:** 청사진 + Step 14 무료 최종본 + Step 18 Bible (Step 19 검증 통과)

**기본 밴드 (U-자형 — risk 우선 / 전파 영향 큰 양쪽 끝에 자원 집중):**

| 밴드 | EP | N (draft 수) | 이유 |
|---|---|---|---|
| **Conversion bridge** | **EP9-10** | **N=4** | 무료→유료 paywall test. EP9 실패 = paid 진입 X = 전 paid 무효. 단일 EP 최고 stake. |
| Bible anchored | EP11-25 | N=2 | Pilot Bible 갓 만든 직후 — 강한 anchor. drift 적음. |
| Drift territory | EP26-46 | N=3 | Bible Amendment 누적·voice drift·heat ladder 변형 시작. 다중 후보 가치 ↑. |
| **Finale arc** | **EP47-50** | **N=4** | 작품 마무리. 컨버전스 다양·결함 시 회수 불가. closure 최대 안전 마진. |

**Draft 강조 (N=2 기준):**
- Draft A: plot / paywall / continuity
- Draft B: voice / English / desire / heat

**N=3+ 추가 강조:**
- Draft C: visual / intimacy
- Draft D (N=4 시): heat / intimacy 별도 트랙

**대형 회차 트리거 (밴드 default에 +1, 단 N=4가 상한):**
- first major intimacy payoff
- betrayal
- midpoint reversal
- identity reveal
- major sacrifice
- finale opening
- final paywall turn

**적용 예:**
- EP9·EP10 = N=4 (밴드 default, 이미 최대)
- EP15 first major intimacy payoff = N=2 → N=3
- EP35 betrayal = N=3 → N=4
- EP47 finale opening = N=4 (이미 최대 유지)

### Native English Polish (필수, 모든 paid EP)

N=2/3/4 draft → 선정본 → **lightweight Native English polish** 적용 후 최종본 확정.

- Polish 기준: **Bible의 Native English Style Rules + Forbidden Translation-Smell List**
- 변경 범위 명시 (Scoped Pass 식, track changes)
- Polish는 결함 탐지가 아니라 **마감 품질 보장**

**출력:** EP별 draft + 선정본 + polish 적용본 (구조는 무료와 동일하되 축소).

## Step 21. Bible Amendment 서브프로토콜

**입력:** Paid 진행 중 발생한 새 요소 (새 캐릭터·새 heat rung·새 paywall 패턴)

**처리:**
- 대형 회차 트리거 발생 시 Bible Amendment 작성 가능
- Amendment는 별도 섹션 기록
- 원본 Bible 원칙과 충돌 검사
- **Amendment > 3건 누적 시 Pilot Bible v2 재발행** (전체 일관성 재검증)

**출력:** `20_amendments/[amendment_id].md` (또는 v2 발행 시 `18_pilot_bible_v2.md`)

## Step 22. Free-Paid Coherence Gate (3-Layer, 전부 자동)

**3 Layer 모두 자동.** 사용자 트리거 X — 각 paid EP 완성 시 자동 실행.

| Layer | 범위 | 트리거 |
|---|---|---|
| **Polish** | Native English lightweight 수정 (Bible Style Rules 적용) | 모든 paid EP 완성 시 **자동** |
| **Spot Check** | translation-smell regex / anti-AI dialect / voice fingerprint (Bible Voice Book 키 어휘·cadence) / paywall promise drift / character desire drift | 모든 paid EP 완성 시 **자동** |
| **Heavy Gate** | Full English Table Read + 9 페르소나 + coherence 항목 | **자동** — 아래 조건 매칭 시 |

**차이:**
- **Polish** = 마감 품질 (결함 없어도 모든 EP에 적용)
- **Spot Check** = 결함 탐지 (Flag 시 Heavy Gate 자동 트리거)
- **Heavy Gate** = 블록 단위 종합 검수

### Heavy Gate 자동 트리거 조건

다음 중 하나 매칭 시 즉시 자동 실행 (사용자 호출 불필요):

**A. 지정 EP 도달:**

| EP | 이유 |
|---|---|
| **EP9 (mandatory)** | 무료 결제 약속의 즉시 회수 검증. EP9 무너지면 결제 약속 즉시 파탄. |
| EP10 | Bridge stabilization |
| EP15 / 20 / 30 / 40 | 블록 heavy |
| EP47-50 | Finale arc heavy (전 화수 자동) |

**B. Spot Check Flag 발생:** 어느 paid EP든 spot check가 flag → 즉시 Heavy Gate로 승격.

**C. Bible Amendment 발행 직후:** Step 21에서 새 amendment 등재 시 다음 EP는 자동 Heavy Gate (Amendment ripple 검증).

**D. 사용자 명시 요청:** 위 자동 조건 외에도 사용자가 특정 EP heavy 요청 시 추가.

### Heavy Gate 검사 항목 (자동 실행 시)
- EP8 약속 회수 정합 (특히 EP9)
- 무료 voice ↔ 유료 voice 일치
- 캐릭터 욕망 drift 없음
- heat escalation 점프 없음
- paywall promise 회수·갱신 흐름
- 영어 톤 후반 번역체 무너짐 없음
- Continuity: 일반 회차 Persona 03 ≥ 3 / 대형 회차 ≥ 4

### 자동 실행 흐름

```
paid EP 완성
  → Polish 자동 (라이트)
  → Spot Check 자동 (regex/fingerprint)
       ├─ Pass: 다음 EP로
       └─ Flag: Heavy Gate 자동 승격
  → EP 번호가 지정 EP (EP9·10·15·20·30·40·47-50)면 Heavy Gate 자동 실행
  → Bible Amendment 직후 EP면 Heavy Gate 자동 실행
```

**출력:** `22_coherence_gate/[ep].md` (3-layer 결과 분리 기록)

## Step 23. 작품 완결 — FINAL_PAID + FINAL 통합 (자동, 필수)

모든 유료 EP (EP9-50) 완성 + Step 22 Coherence Gate 통과 시 즉시 자동 실행:

**처리:**
- `[작품]_FINAL_PAID.md` 생성 (EP9-50 통합) — `paid/ep09.md ~ ep50.md`에서 추출
- `[작품]_FINAL.md` 생성 (전체 EP1-50 통합) — `10_rewrite/ep01.md ~ ep08.md` + `paid/ep09.md ~ ep50.md`
- 모두 `projects/[작품]/07_final/` 디렉토리에 저장
- UTF-8 no BOM / EP 간 separator `\r\n\r\n---\r\n\r\n` / post-script 섹션 제외

**검증 필수 (자동):**
- Korean character count = 0 (EP body)
- Hard Cut count = **EP 수 - 1** (마지막 EP 자연 엔딩 — FREE 8 / PAID 41 / FULL 49). 상세: `feedback_final_episode_natural_ending.md`
- Work header count = EP 수 + 1
- 4 블록 일관성 (Visual = scene count / Camera·DIALOGUE·FX = scene + end image)
- Separator 일관

**실패 시 (🔴):** 원본 EP 수정 후 재생성. 검증 통과까지 작품 미완결 처리.

**메타 갱신:** `[작품]_00_meta.md`에 "완결 ✅" + 최종고 위치 + 검증 결과 기록.

**상세 룰:** 메모리 `feedback_final_consolidation_three_files.md`.

→ 본 단계 통과 = 작품 모든 회차 최종고 완성. 이후 phase_8 (한국어 줄거리 요약 1,500자) 진입.

---

# III. 통합 운영 요약

### Effort·모델

| 항목 | 값 |
|---|---|
| 모델 | Claude Opus 4.7 |
| Effort | max (단일 effort 통일) |
| 핵심 단계 (Step 4·8·10·13·15·17·18·19) | max × 2 권장 |
| 그 외 단계 | max × 1 |

### 무료 vs 유료 강도

| 항목 | 무료 (Premium Pilot) | 유료 (Bible-controlled) |
|---|---|---|
| N (draft 수) | 4 | **U-자형: 2-4** (EP9-10 N=4 / EP11-25 N=2 / EP26-46 N=3 / EP47-50 N=4) + 대형 회차 +1 |
| Protocol 단계 | Step 1-19 전체 | Step 20-22 |
| Native English Polish | Step 11 Scoped Pass | **모든 EP 필수 (Step 20)** |
| Gate 강도 | Final Pilot Gate (≥4) | **3-layer 전부 자동** (Polish / Spot / Heavy) |
| Heavy Gate 트리거 | — | 자동 (지정 EP / Spot Flag / Amendment 직후) |
| Continuity 기준 | Persona 03 ≥ 4 | 일반 ≥ 3 / 대형 ≥ 4 |
| 검토 페르소나 | 9 + Adversarial | 표준 + automated spot |

### 최종 기준

- **정합성은 floor** (red gate)
- **Native English는 판매 gate** (red gate, framing prompt 고정)
- **Viewer Pull과 Paywall Force가 중심** (최대화 대상)
- **무료회차는 거의 무제한으로 엄격**
- **유료회차는 Pilot Bible로 통제 + U-자형 N + 자동 3-layer gate**
- **모든 paid EP는 Native English polish 필수** (spot check와 분리)
- **Heavy Gate는 자동 트리거** (수동 호출 X)

---

# IV. 변경 이력

## v5.1 → v5.2 (2026-05-13)

| # | 섹션 | 변경 | 이유 |
|---|---|---|---|
| 1 | Step 20 Band | **Escalating N (2→3→4) → U-자형 N (4→2→3→4)** — EP9-10·EP47-50 양쪽 끝 N=4 / EP11-25 N=2 / EP26-46 N=3 | EP9는 단일 EP 최고 stake (paywall conversion test). 전파 영향 큰 양쪽 끝에 자원 집중 (risk 우선 모델) |
| 2 | Step 22 Heavy Gate | **수동 → 자동 트리거** — 지정 EP 도달 / Spot Check Flag / Bible Amendment 직후 자동 실행 | 사용자 트리거 의존 시 누락 위험. 시스템이 알아서 처리 |
| 3 | Step 22 추가 | Bible Amendment 직후 EP = 자동 Heavy Gate (ripple 검증) | Amendment가 다음 EP에 미치는 영향 자동 감지 |

## v5 → v5.1

| # | 섹션 | 변경 | 방지하는 리스크 |
|---|---|---|---|
| 1 | Step 1 | Reference Floor를 "기능 추출"로 한정. 문장·구조·설정 복제 금지 명시. | 모방 (Demon Lord 라인·구조 직접 차용) |
| 2 | Step 4 | Native English 축에 **고정 framing prompt** (native US/Canada dialogue editor / mobile short-form drama / performability > grammar / AI dialect·stiff fantasy English 즉시 감점). | "문법은 맞지만 안 팔리는 영어" 통과 |
| 3 | Step 6 | Quoted Treasure를 **Raw / Approved 2-layer 분리**. Approved = Native English 통과 draft 출신만 verbatim 보존. Raw = 기능만. | 번역체가 verbatim으로 최종본 침투 |
| 4 | Step 19 | Cold Read 2-tier: **EP9 full cold draft + EP20 midpoint cold outline**. Bible의 50화 전체 지구력 시험. | Bible이 EP9는 받지만 EP15+에서 무너지는 패턴 |
| 5 | Step 20 + Step 22 | **3-layer 분리**: Polish (모든 EP, 마감 품질) / Spot Check (자동, 결함 탐지) / Heavy Gate (블록 단위). | 후반 영어 무너짐 (spot check만으로는 마감 품질 안 잡힘) |
