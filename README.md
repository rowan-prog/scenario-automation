# Scenario Automation

AIGC 숏폼 시나리오 제작 워크플로우 자동화 작업 공간.
공통 설정·기준·prompt를 모아두고, 작품은 `projects/` 아래에 개별 폴더(`넘버_타이틀` 형식)로 관리한다.

**최종 목표:** 4-Gate (Structure / Narrative / Script / Production) 통과한 완성된 스크립트.

---

## 폴더 구조

```
scenario-automation/
├── README.md                    이 파일
├── config/                      공통 기준·자료 (모든 작품 공유)
│   ├── production_guide.md      마스터 가이드 v2 — 모든 원칙·기준
│   ├── evaluators.md            피칭 평가위원 7인 분석
│   ├── visual_lock_template.md  캐릭터 비주얼 락 템플릿
│   ├── meta_template.md         작품 진행 메타 템플릿
│   ├── personas/                검토 페르소나 7인
│   └── reference_scripts/       참고 스크립트·청사진·피칭덱
├── prompts/                     단계별 prompt (워크플로우 순)
│   ├── phase_1_rough_blueprint.md
│   ├── phase_2_pitch_deck.md
│   ├── phase_3_full_blueprint.md
│   ├── phase_4_episode_writing.md
│   ├── phase_5_persona_review.md
│   ├── phase_6_revision.md
│   ├── phase_7_final_gate.md
│   ├── phase_a_1_adaptation_blueprint.md   (부가 트랙 A — 각색)
│   ├── phase_a_2_adaptation_script.md
│   └── phase_b_external_script_intake.md (부가 트랙 B — 외부 대본)
└── projects/                    각 작품 폴더
    ├── 01_titan_born/
    │   ├── 01_titan_born_00_meta.md           작품 진행 메타
    │   ├── 01_titan_born_01_blueprint_rough.md
    │   ├── 01_titan_born_02_pitch_deck.md
    │   ├── 01_titan_born_03_pitch_outcome.md  (사용자 작성 — 피칭 결과)
    │   ├── 01_titan_born_04_blueprint_full.md
    │   ├── 05_episodes/         초안 + 패치 라운드 (파일은 01_titan_born_ep01.md 등)
    │   ├── 06_reviews/          검토·패치·게이트 보고서 (파일도 prefix)
    │   └── 07_final/            4-Gate 통과한 최종고만 (파일도 prefix)
    ├── 02_the_offering/
    └── 03_black_core/
```

**파일명 규칙:**

모든 작품 파일은 `[작품 폴더명]_` prefix로 시작한다 — 파일 자체로 어느 작품의 어느 단계인지 식별 가능.

형식: `[작품명]_[단계 번호]_[단계 이름].md`

예: `02_the_offering_01_blueprint_rough.md` (작품명 + 단계번호 + 단계이름)

**번호 의미:**
- 폴더 번호 (`projects/01_titan_born/` 의 `01`) — **작품 생성 순서** (식별자)
- 파일 prefix (`01_titan_born_...md` 의 `01_titan_born_`) — **파일 자기 식별용 작품 ID** (폴더명과 동일)
- 파일 단계 번호 (`_00_`, `_01_`, `_02_` 등) — **워크플로우 단계 순서**

하위 폴더(`05_episodes/`, `06_reviews/`, `07_final/`)는 prefix 없음 — 모든 작품 공통 표준 폴더.

---

## 세 가지 트랙

### 메인 트랙 — 신규 작품 (아이디어 → 최종고)

```
phase_1 (러프 청사진)
  → phase_2 (피칭덱)
    → 03_pitch_outcome.md (사용자 작성)
      → phase_3 (완성 청사진)
        → phase_4 (에피소드 집필)
          → phase_5 (페르소나 검토)
            ↔ phase_6 (패치)  [라운드 5회 한계]
              → phase_7 (최종고 게이트 4-Gate)
                → 07_final/ep[N].md ✅
```

### 부가 트랙 A — 원작 각색

```
phase_a_1 (각색 방향 청사진)
  → phase_a_2 (각색 스크립트 집필)
    → phase_5 / phase_6 / phase_7 (메인 트랙 검토·패치·게이트 루프 진입)
```

각색 강도: **충실 / 현대화 / 재해석** (Soft Lock — 작품 자율).

### 부가 트랙 B — 외부 AIGC 대본 검토→수정 반복

```
phase_b (외부 대본 등재 + 1차 게이트 평가)
  → 결론 분기:
    A. 패치 가능 → phase_5 → phase_6 → phase_7
    B. 구조 재설계 필요 → phase_3 (청사진 작업으로 전환)
    C. 폐기 권장 → 작업 중단
```

청사진 부재 시 phase_5·phase_7은 **대본 내적 정합성**으로 판정 (Hard Lock 영역만).

---

## 빠른 시작

### 신규 작품 시작
1. `projects/[다음 번호]_[작품 슬러그]/` 폴더 생성 (예: `04_new_work`)
2. `phase_1` prompt 호출 → 러프 청사진 작성 + `00_meta.md` 자동 생성
3. 이후 워크플로우 순서대로 진행

### 원작 각색 시작
1. `projects/[다음 번호]_[작품 슬러그]/` 폴더 생성
2. 원작 자료 준비 (전문 또는 핵심 챕터)
3. `phase_a_1` prompt 호출 → 각색 청사진 + `00_meta.md`
4. 이후 `phase_a_2` → 메인 트랙 검토 루프

### 외부 대본 검토 시작
1. `projects/[다음 번호]_[작품 슬러그]/` 폴더 생성
2. 외부 대본 텍스트 준비
3. `phase_b` prompt 호출 → 대본 등재 + 1차 게이트 + `00_meta.md`
4. 결론 (A/B/C)에 따라 분기

---

## 핵심 원칙

모든 작업의 출발점은 **`config/production_guide.md` Section 3 (핵심 제작 원칙)**.
의문이 생기면 **Section 24 (최종 핵심 규칙)** 으로 돌아간다.

특히 중요한 메타 원칙:
- **Section 0-3 (락/열어둠)** — Hard Lock vs Soft Lock 구분. 작품 자율 영역을 강제 표준화하지 않는다.
- **Section 9-1 (선언형 대사 5조건)** — 시점·구간으로 일률 잠금하지 않는다. 5조건으로 판정.
- **Section 11 (재밌겠다 식별 1차)** — "내가 보지 않더라도 뭐가 재밌는지는 알겠다"가 떠올라야.

---

## 라이선스 / 권한

내부 작업 도구. 외부 공개 전 권한 확인 필요.
