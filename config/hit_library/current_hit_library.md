# 현재 기준 히트 라이브러리 — 단일 진실

> **이 파일이 *현재 활성* 히트 라이브러리를 지정한다. 다른 옛 파일은 archive 취급.**

---

## 현재 활성 (2026-06-05 updated)

**파일:** `vertical_hit_library_2026-06-05_updated.xlsx`

**상태:** 활성. 모든 작품 reference 시 본 파일만 사용.

**6/5 갱신 내용 (시트 `08_0605_UPDATE_LOG` 단일 진실):**
- Final library rows **349** (Base 212 + merged 8 + supplement 67 + 6/5 추가). A_Core(근거 ≥85) 147행.
- `01_FINAL_LIBRARY` L0325-L0348 = NetShort 현재 페이지(all-plots/hotseries) 타이틀 24행 APPEND / L0349 = Fruit Love Island(AIGC social-native 벤치마크·paid 앱 히트 아님).
- `03_AIGC_TRACKER` +11행(NetShort VFX/AIGC 후보 + Direct AI 벤치마크) / `04_TROPE_INDEX` 6/5 delta 4행(레거시 카운트 보존·delta만 추가) / `05_SOURCE_REGISTER` +6 / `06_WEB_CHECK_NOTES` +6.
- **판정 원칙:** 공개근거 기반 큐레이션 → 강제 삭제 X·Base 유지+병합/추가/약한 슬롯 교체후보 표기. 기획 참조 시 title보다 `desire_engine`·`conversion_engine`·`aigc_leverage` 우선.
- **신호 한계:** current-page 신호만 — 앱 내 paid 랭킹/광고비는 별도 검증 후 ranking claim.

**시장 인사이트 보조:** `market_insights_2026-05-16.md` (데이터 한계 명시·과잉 일반화 금지)

---

## 옛 라이브러리 (작업 금지)

| 파일 | 상태 |
|---|---|
| `_archived_vertical_hit_library_2026-05-15.xlsx` | Archive — *재참조 금지* |
| `_archived_vertical_hit_library_2026-05-19_corrected_v2.xlsx` | Archive (2026-06-08) — 06-05 updated가 Base 포함 superset이라 대체. *재참조 금지* |

---

## 사용 룰 (라이브러리는 단일 도구가 아니라 6 카테고리 분리 도구)

새 작품 진입 시 히트 라이브러리에서 다음 6 카테고리를 *별도로* 참조:

### 1. 제목 (title)
유사 장르·욕망축의 히트작 제목 5-10개. *제목 패턴* (3-7 단어·동사형·욕망축 명시) 분석.

### 2. 트로프 결합 (trope combo)
유사 작품의 검증된 *트로프 결합* (예: Werewolf + Rejected mate + Hybrid + Forbidden) 3-5건. 시청자 검증 트로프 우선.

### 3. 욕망축 (desire axis)
타깃 시청자가 *결제하는* 핵심 욕망축 (status / vengeance / mate-bond / 보호 / breeding 등). 5-7개 모드 중 작품 매칭.

### 4. 페이월 (paywall design)
첫 paywall (EP6-8 or EP8-9) 패턴: 미완료 cliffhanger·declaration 직전·물리 행동 직전. 유사 작품 5건 비교.

### 5. 첫 유료 보상 (first paid payoff)
EP9 or 첫 paid scene에서 발화/사건. 유사 작품 5건의 *첫 유료 폭발 비트* 분석.

### 6. 반복 보상 루프 (reward loop)
시리즈 전체 반복되는 결제 동력 (3-5 비트 패턴). 출산·재회·status 상승·복수 완성 등.

→ **작품 진입 시 6 카테고리 각각 별도 reference 작성 의무**. 한 작품에 6 reference card.

---

## evidence_score / reaction_signal / performance_signal 사용 룰

- **evidence_score:** 매출 검증 신호 (high·medium·low). *결제 도파민 강도* 추정. *매출 자체 X*.
- **reaction_signal:** 시청자 댓글·SNS 반응 수치. *재생산 가능성* 추정.
- **performance_signal:** 플랫폼 순위·노출 수치. *현재 시장 인기*.

→ 셋 모두 *추정 신호*. *매출 검증*으로 쓰지 말 것. *Market_insights*의 한계 (데이터 부정확·시점 불명·일부 추정) 함께 인지.

---

## 작품별 reference memo 의무

새 작품 phase_1 진입 시 다음 파일 작성:

```
projects/[작품]/[작품]_07_hit_library_references.md
```

내용:
- 6 카테고리별 매칭 row 3-5개씩
- 사용 기능 (제목 / 트로프 / 욕망축 / 페이월 / 첫 유료 / 반복 루프)
- 본 작품에 어떻게 변환할지

→ phase_1 청사진 작성 시 이 파일이 *근거*. 청사진 본문에 reference 인용 X (작품 본문 외부 노이즈 제거).

---

## 새 라이브러리 갱신 시

매번 새 corrected 또는 updated 라이브러리가 들어오면:

1. 본 파일 *즉시* 갱신 (현재 활성 파일명 변경)
2. 이전 파일을 `_archived_*`로 rename
3. `00_START_HERE.md` 갱신
4. 모든 옛 reference memo 검토 (재참조 필요 시 갱신)

마지막 갱신: 2026-06-08 (06-05 updated 라이브러리 활성화 + 05-19 corrected_v2 archive)
