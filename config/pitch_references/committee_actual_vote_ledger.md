# 위원 실제 투표 ledger — REAL VOTES ONLY

> **본 파일 = *실제 피칭 결과*만. 가상 투표·예측 모델·일반 조언 *절대 포함 금지*.**
>
> 위원 가상 투표 (SPECULATIVE) 모델은 별도: `config/evaluators.md` (Section 17 v2 모델·`config/pitch_references/MASTER_DATASET.md` Section D)
>
> **혼동 방지 핵심:** "위원이 이렇게 *볼 것*"이 *실제 결과*처럼 인용되면 안 된다.

---

## 데이터 출처 (모두 사용자 직접 제공·실측)

### 2026-05-12 회차 (8 작품)

| 작품 | A | B | C | D | E | F | G | Yes | 결과 |
|---|---|---|---|---|---|---|---|---|---|
| OFFERING | Y | Y | Y | Y | Y | Y | Y | 7/7 | PASS 만장일치 |
| Wolfless Mate | Y | — | Y | Y | Y | Y | Y | 6/6 | PASS 만장일치 (B 미답) |
| Hero Beneath | Y | Y | Y | Y | Y | N | Y | 6/7 | PASS |
| First Love | Y | — | Y | Y | — | Y | Y | 5/5 | PASS 만장일치 (B·E 미답) |
| TITAN BORN | N | N | Y | N | Y | Y | Y | 4/7 | PASS |
| SHE STOLE | N | Y | Y | N | Y | N | Y | 4/7 | PASS |
| HEIR | N | — | Y | N | N | N | N | 1/6 | FAIL (폐기) |
| MY MAP | N | N | N | N | N | N | N | 0/7 | FAIL (폐기) |

### 2026-05-21 회차 (6 작품)

| 작품 | A | B | C | D | E | F | G | Yes | 결과 | CM |
|---|---|---|---|---|---|---|---|---|---|---|
| Back to You: Titanic | Y | Y | Y | Y | — | Y | Y | 6/6 | PASS (E 미답) | Bonnie |
| Ashborn: Academy | Y | Y | Y | Y | Y | Y | Y | 7/7 | PASS 만장일치 | Lily |
| Olympus | N | N | Y | N | Y | Y | Y | 4/7 | PASS (A·B·D 거부) | Rowan |
| Demon Lord | N | N | Y | N | N | Y | N | 2/7 | FAIL | Rowan |
| Knight | Y | N | N | N | N | N | N | 1/7 | FAIL | Emika |
| Elf King | N | N | N | Y | N | N | N | 1/7 | FAIL | Rowan |

→ **총 14 작품·98 cells (일부 미답).** 이 데이터만 *실제*.

---

## 실제 verbatim 코멘트 (저장 위치)

각 작품의 위원별 실제 코멘트는 다음 위치:

### 2026-05-12 (verbatim 4 작품만 있음)
- OFFERING: `projects/02_the_offering/02_the_offering_03_pitch_outcome.md`
- TITAN: `projects/01_titan_born/01_titan_born_03_pitch_outcome.md`
- SHE STOLE: `projects/06_she_stole_my_face/06_she_stole_my_face_03_pitch_outcome.md`
- HEIR: `projects/_X_04_heiress_clause/04_heiress_clause_03_pitch_outcome.md`
- Wolfless·Hero·First·MY MAP: **verbatim 없음** (verdict only)

### 2026-05-21 (verbatim 6 작품 모두 있음)
- `config/pitch_references/2026_05_21/RESULTS.md` (전체 종합)
- 작품별 raw 피칭덱·verbatim: `config/pitch_references/2026_05_21/01_*.md` ~ `06_*.md`

---

## 사용 룰 (이 ledger만)

### 작품 작업 시 사용 방법:
1. **실제 피칭 받은 작품이면:** 본 ledger에서 작품 행 확인 + 작품 outcome 파일에서 verbatim 정독
2. **반영할 피드백 식별:** verbatim에서 작품 *본질*에 관한 비판만 채택
3. **반영 금지 피드백 식별:** 다른 작품 비판이나 일반 조언은 무시
4. **프로젝트 `00_STATUS.md`에 기록:**
   - "실제 위원 verdict 및 verbatim 인용"
   - "반영 결정된 피드백"
   - "반영 금지 피드백 + 사유"

### 작품 작업 시 *하지 말 것*:
- ❌ "위원 A가 *이렇게 볼 것이다*"라고 실제 결과처럼 말하기 → 그것은 가상 투표·`config/evaluators.md`·`MASTER_DATASET.md` 영역
- ❌ 피칭덱 본문에 위원 라벨 ("위원 A 요구") 또는 수정 이력 포함
- ❌ 옛 작품의 위원 코멘트를 *새 작품*에 *룰*처럼 일반화

---

## 가상 투표 (SPECULATIVE) 분리 명시

가상 투표 결과는 *반드시* 다음 라벨을 사용:

> **[SPECULATIVE — 가상 투표·실제 결과 아님]**
> 신뢰구간 ±20% (sample size 14 작품).
> CM/Presentation 효과 예측 불가.

→ 라벨 없이 가상 투표 인용 = 위반.

---

## 새 회차 데이터 입수 시

1. 본 ledger에 새 row 추가 (작품·위원별 verdict)
2. 작품별 outcome 파일에 verbatim 보존
3. `config/pitch_references/MASTER_DATASET.md` Section A·B 갱신
4. `config/evaluators.md` Section 17 v2 모델의 *베이스라인*만 재계산 (verbatim 패턴 일반화는 신중)
5. 본 ledger 마지막 갱신일 갱신

마지막 갱신: 2026-05-21
