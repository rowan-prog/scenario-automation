# Step 0-1 — 아이디어 제출 프롬프트

## 역할
신규 작품의 **아이디어 4-8개를 생성·제출**한다. 이 단계는 청사진 초안(phase_1)을 작성하기 위한 **선행 단계**다. 사용자가 아이디어를 1개 선택하거나, AI가 자율 선택 후 보고. 선택된 아이디어가 phase_1의 input이 된다.

반드시 한국어로 작성한다.

## 워크플로우 위치

```
phase_0 (아이디어 제출 + 선택)
  → phase_1 (러프 청사진)
    → phase_2 (피칭덱)
      → phase_3 (완성 청사진)
        → phase_4 (스크립트 집필)
          → phase_5 (검토) ↔ phase_6 (패치)
            → phase_7 (최종고)
```

## 핵심 원칙 — 타깃 맞춤 (필수)

아이디어 단계부터 **타깃 맞춤**이 시작된다. 이후 청사진 초안·피칭덱·청사진 완성·스크립트 집필 모든 단계가 동일 타깃에 정렬되어야 한다. 아이디어가 타깃과 어긋나면 이후 단계에서 수정해도 작품 정체성이 흔들린다.

**타깃 정의 = 북미 남성 시청자 OR 북미 여성 시청자 (혼합·전연령 작품 X — 한쪽 선명).**

타깃 맞춤 = 다음 5개 차원이 모두 정렬:
1. **구조 설계** (보상 루프·페이월·결제 트리거)
2. **소재** (장르·트로프·카테고리)
3. **미감** (톤·분위기·세계관)
4. **비주얼** (AIGC 포맷·9:16 vs 16:9·색감·캐릭터 비주얼)
5. **결제 동기** (다음 화를 누르게 만드는 것)

## 실행 전 읽어야 할 파일

### 공통 (모든 작품)
- `config/production_guide.md` Section 0-3, 5, 5-5, 11
- `config/reference_scripts/INDEX.md` (reference 자료 매칭)
- 메모리: `feedback_target_alignment_all_steps.md` (타깃 맞춤 강제), `feedback_character_name_diversity.md` (이름 충돌), `feedback_core_tropes.md` (검증 트로프), `feedback_2026_market_research_insights.md` (시장 리서치)

### 남성향 작품 진입 시 (필수 — 단계 한정 Section만 정독)
- **문서:** `config/target_research/male_target_research.md`
  - **이 단계 필요 Section: 1-5 (결론·4축·16 카테고리), 15 (5 최적 조합), 31 (12 후킹 소재 매트릭스), 38 (플랫폼 신호 요약)**
  - 다른 Section은 후속 phase에서 정독
- **플랫폼 신호:** `config/target_research/platform_recent/2026-05-12_paid_vertical_signals.md` (해당 성향 작품 매트릭스만)
- 메모리: `feedback_male_target_research_data.md` / `feedback_male_target_immediate_gratification.md` / `feedback_paid_vertical_platform_signals.md` / `feedback_space_adventure_niche_opportunity.md` (해당 시)
- 페르소나: `config/personas/persona_08_male_viewer_diagnostic.md`

### 여성향 작품 진입 시 (필수 — 단계 한정 Section만 정독)
- **문서:** `config/target_research/female_target_research.md`
  - **이 단계 필요 Section: 1-4 (결론·시장 전제·9 핵심 보상·16 카테고리), 18 (10 기획 조합), 24 (플랫폼 신호 요약)**
- **플랫폼 신호:** `config/target_research/platform_recent/2026-05-12_paid_vertical_signals.md` (해당 성향만)
- 메모리: `feedback_female_target_research_data.md` / `feedback_female_target_romance.md` / `feedback_paid_vertical_platform_signals.md`
- 페르소나: `config/personas/persona_09_female_viewer_diagnostic.md`

### 공통 룰 메모리 (필수)
- `feedback_target_data_dual_use.md` (검증+집필+피칭 근거 활용)
- `feedback_hook_vs_payment_engine.md` (후킹 vs 결제 엔진 분리)
- `feedback_aigc_format_selection.md` (AIGC 포맷 선택)
- `feedback_target_alignment_all_steps.md` (5차원 정렬)

## 필수 입력값

사용자에게 다음 항목 확인. 빠진 항목 있으면 먼저 묻는다.

- **타깃 국가** (북미 / 일본 / 한국 / 글로벌)
- **타깃 성별** (남성향 / 여성향)
- **타깃 나이** (예: 25-45세 / 35-54세)
- **선호 카테고리·장르 방향** (열려 있는 카테고리·반드시 피할 카테고리)
- **플랫폼** (페이드 버티컬 / TVOD / OTT)
- **포맷** (AIGC Live-action vs Animation 3D / 2.5D / 2D + 세로형 9:16 vs 가로형 16:9)
- **총화수·편당 길이** (50화 50화 / 90초-3분 표준)
- **무료-유료 구조** (무료 EP1-8 / 유료 EP9+)
- **제한 수위** (다크 로맨타지 고수위 / 일반 / 안전 톤)
- **참고 작품·톤** (선택)
- **사용자 아이디어** (있으면 1차 input. 없으면 AI가 자유 생성)
- **개수** (생성 아이디어 개수 — default: 5개)
- **선택 방식** (사용자 선택 / AI 자율 선택)

## 출력 구조 — 아이디어 4-8개

각 아이디어는 **한 단락**으로 구성. 다음 6개 항목 모두 포함:

### [아이디어 N] 제목 가제 (영어 + 한국어 두 줄)

1. **로그라인 (2-3문장, 한국어)**
   - 누가 무엇을 빼앗기는가
   - 어디서 어떻게 뒤집는가
   - 더 큰 갈등 남김 (페이월 시그널)
   - **광고 카피라이팅 톤** — 첫 줄 즉시 멈춤·마지막 줄 페이월 시그널

2. **카테고리·트로프**
   - 남성향: 16 카테고리 중 1-2개 매칭 (예: System Action Fantasy + Soft Harem) / 5대 엔진 중 어떤 게 작동하는지
   - 여성향: Tier 1-3 트로프 매트릭스 중 1-3개 (예: Alpha CEO + Marriage of Convenience + Secret Baby)

3. **결제 트리거 1-2개**
   - 무료 구간 마지막에 무엇이 안 끝나는가
   - 유료 구간에 남는 것 (굴욕·폭로·역전·소유·정복·공개 선언)

4. **타깃 정렬 5차원 자가 점검**
   - 구조 설계 (보상 루프) — 한 줄
   - 소재 (장르·트로프) — 한 줄
   - 미감 (톤·세계관) — 한 줄
   - 비주얼 (AIGC 포맷) — 한 줄
   - 결제 동기 — 한 줄

5. **변별력 (참고작 대비 차별 한 줄)**

6. **위험 신호 (자가 진단)**
   - 작품 간 이름 충돌 가능성
   - 카테고리 단일축 위험 (남성향: 능동성·결제 엔진 / 여성향: 사적 친밀로만 끝남)
   - 미시 정합성 우려 (시스템·메커닉)
   - **유사 아이디어 작품 진행 중인가 (충돌 회피)**

## 작성 원칙

### A. 카테고리 다양화 (필수)
**4-8개 아이디어를 동일 카테고리로 채우지 말 것.** 사용자가 다양한 옵션을 비교 가능하도록 카테고리 분산:

**남성향 5개 아이디어 예시 분산:**
- 1개: System Action Fantasy (LitRPG계열)
- 1개: Survival Base-building (포스트아포칼립스)
- 1개: Operator Thriller (밀리터리·전직 요원)
- 1개: Power Academy / Ranking League (학원·랭킹전)
- 1개: Soft Harem Adventure (HaremLit 톤)

**여성향 5개 아이디어 예시 분산:**
- 1개: Modern Mafia / Alpha CEO (할리퀸 Presents 톤)
- 1개: Marriage of Convenience / Flash Marriage
- 1개: Secret Baby / Hidden Pregnancy
- 1개: Dark Romantasy (Dragon Mate / Shifter)
- 1개: 외도 복수 / 후회남

### B. 타깃 자료 기반 (필수)
각 아이디어는 **`feedback_male_target_research_data.md` 또는 `feedback_female_target_research_data.md` 자료에 직접 매칭**.

남성향:
- 보상 루프 본질 7개 중 최소 3개 포함 (강해진다·해금된다·장비가 좋아진다·거점이 커진다·판을 읽는다·강자가 인정한다·여자가 붙는다)
- 매 3-5화마다 무엇을 얻는가 답 가능

여성향:
- Tier 1 트로프 1-2개 + Tier 2-3 트로프 1-2개
- 공개 지위 회복 + 거리 변화 + 남주 비언어 발화 + 여주 능동성 자가 검증 통과

### C. 작품 간 이름·트로프 충돌 회피 (필수)
- 기존 진행 작품 (`projects/` 폴더)의 인물 이름·트로프 핵심·세계관과 충돌하는지 사전 검사
- 충돌 시 신규 아이디어 측 양보 (이름·세계관 변경)
- 메모리 `feedback_character_name_diversity.md` 참조

### D. 광고 카피라이팅 톤 (로그라인)
- 첫 줄 = "어 이거 뭐야" 즉시 멈춤
- 마지막 줄 = 페이월 시그널 ("그 단어는 ~에 끊긴다" 진행형)
- 평어체·명사형 둘 다 OK

### E. "그래서 뭐?" 사전 차단
각 아이디어에 다음 질문 자가 답:
- 시청자가 EP1 보고 "다음 화 누르고 싶은가?"
- EP8 페이월 비트가 "지금 결제해야 한다" 강도인가?
- 무료 구간이 첫 증거만 주고 더 큰 보상은 남겼는가?

## 선택 방식

### 옵션 1: 사용자 선택
- 4-8개 아이디어 제출 후 사용자에게 번호 + 이유 요청
- 사용자가 선택 후 phase_1 진입

### 옵션 2: AI 자율 선택
- 사용자가 "알아서 선택"이라고 명시한 경우
- AI가 5차원 자가 점검 + 결제 트리거 강도 + 위원 4표 가능성 + 시장성을 종합 평가 후 1개 선택
- 선택 이유 보고

### 옵션 3: 하이브리드 (권장)
- AI가 4-8개 제출 + 추천 1개 명시 (`(추천)` 태그)
- 사용자가 추천 받든지 다른 것 선택하든지 결정

## 저장 위치

선택된 아이디어가 결정되면:

1. **작품 슬러그 결정** — 선택된 아이디어 제목 기반 (예: TITAN BORN → `titan_born`, THE OFFERING → `the_offering`)
2. **작품 번호 결정** — `projects/` 폴더 다음 번호 (예: `01_`, `02_` 다음이면 `03_`)
3. **작품 폴더 생성** — `projects/[NN]_[슬러그]/` (CLAUDE.md 폴더 경로 규율 준수 — scenario-automation/projects/ 직속)
4. **저장:**
   - `projects/[NN]_[슬러그]/[NN]_[슬러그]_00_idea_pool.md` — 선택된 아이디어 + 후보 아이디어 모두 기록
   - `projects/[NN]_[슬러그]/[NN]_[슬러그]_00_meta.md` — 메타 파일 생성 (선택 아이디어 기준 초기 정보)

## 실행 순서

1. **필수 입력값 전체 확보 확인** — 빠진 항목 있으면 먼저 묻는다.
2. **타깃별 자료 정독** — 남성향이면 `feedback_male_target_research_data.md`, 여성향이면 `feedback_female_target_research_data.md`.
3. **기존 작품 충돌 검사** — `projects/` 폴더 메타·인물 이름·세계관 확인.
4. **아이디어 N개 생성** — 카테고리 분산 + 타깃 자료 기반 + 광고 카피라이팅 로그라인 + 5차원 자가 점검.
5. **위험 신호 자가 진단** — 각 아이디어마다 점검.
6. **사용자 선택 요청 OR AI 자율 선택** — 입력값에 따라.
7. **선택 후 작품 폴더 생성** — slug 결정 + 번호 결정 + 폴더 생성.
8. **저장** — `00_idea_pool.md` (전체 아이디어) + `00_meta.md` (초기 메타).
9. **종료 안내 (3줄):**
   - `✅ projects/[NN]_[슬러그]/[NN]_[슬러그]_00_idea_pool.md — [아이디어 N개 / 선택: 아이디어 N]`
   - `✅ projects/[NN]_[슬러그]/[NN]_[슬러그]_00_meta.md — 초기 메타`
   - `다음: 청사진 초안(phase_1)으로 진행할까요?`

## 출력 양식 예시 (참고)

```markdown
# [작품 슬러그] — 아이디어 풀 (phase_0)

## 입력 정보
- 타깃: [북미 / 남성향 / 25-40세]
- 플랫폼: [페이드 버티컬 / ReelShort 류]
- 포맷: [AIGC Live-action / 세로형 9:16]
- 총화수: [50화 / 무료 1-8 / 유료 9+]
- 톤·수위: [성인 톤 / 폭력·섹슈얼 강·강]

---

## [아이디어 1] BLOOD CROWN: The Slave Who Bought His Owner / 피의 왕관: 노예가 주인을 사들이다

**로그라인:**
검투장 노예가 첫 경기에서 황제의 친아들을 베어 죽인다.
관중 5만이 그의 이름을 외치는 동안, 그는 황제의 비밀 통장을 손에 쥐고 있다.
"내일은 황실 금고를 사겠다" — 그 선언은 다음 경기 직전에 끊긴다.

**카테고리·트로프:**
Combat Sports / Pro Wrestling Ranking Spectacle + Soft Harem Adventure. 5대 엔진 중 Status Reversal + Ownership + Competence Porn 작동.

**결제 트리거:**
- 무료 EP8 절단: 황제의 친딸이 검투장에 노예 신분으로 끌려옴 — 주인공 손에 자기 신분증명서가 있음.
- 유료 잠금: 노예 신분 폭로·황제 직접 굴복·하렘 형성.

**타깃 정렬 5차원:**
- 구조: 매 회차 랭킹 1단계 상승 + 새 적·새 동료
- 소재: Combat ranking + 노예 신분 상승 + 비밀 통장
- 미감: 콜로세움 검투·황궁·암시장·도시 권력
- 비주얼: 가로형 16:9 (스케일 보상) — 단 페이드 적합도 평가 필요
- 결제 동기: 다음 경기 + 다음 신분 폭로

**변별력:**
일반 검투장물은 노예가 자유를 얻는 게 보상이지만, 이 작품은 노예가 주인을 사들이는 것이 보상.

**위험 신호:**
- 16:9 가로형 — 페이드 버티컬 표준 9:16과 미스매치 위험 (포맷 재검토 필요)
- 카테고리 (Combat ranking + Harem) 결합으로 단일축 위험 X

---

[아이디어 2~5 동일 양식 반복]

---

## 추천 (AI 1차 선택)
**아이디어 N — [제목]** 추천. 이유: [한 줄].

## 사용자 결정
[ ] 아이디어 1 선택
[ ] 아이디어 2 선택
[ ] 아이디어 3 선택
[ ] 아이디어 4 선택
[ ] 아이디어 5 선택
[ ] 알아서 선택 (AI 자율)
```
