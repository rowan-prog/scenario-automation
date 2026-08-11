---
name: persona-system-v2-2026-05-19
description: 페르소나 시스템 v2 재설계 (2026-05-19). 메타 페르소나 00 신설·09 처방 권한·v3 baseline 통합·silo 차단 폐기. 모든 검토 단계 강제 적용.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2d65e927-1cd5-4df0-bd23-1493c3adfb18
---

> **2026-05-19 시스템 재설계.** OFFERING이 풀 페르소나 검토 통과 후에도 결함 투성이였던 근본 원인 = 페르소나 silo·09 처방 차단·메타 결함 책임자 X. 본 시스템 v2에서 해소.

## 룰

**모든 phase_5 페르소나 검토 진행 시 본 시스템 v2 절대 적용.**

**Why:** 9 페르소나 각자 영역만 보는 silo 구조 → 작품 전체 장르 정체성·후반 paid 동력 같은 메타 결함 = 어느 한 페르소나도 책임 X. OFFERING 풀 페르소나 검토 (Round 1·Round 2) 모두 통과한 후에도 사용자가 "결함 투성이" 평가 = 시스템 구조 결함.

**How to apply:** 페르소나 검토 trigger 시 본 시스템 v2 강제. 옛 9 페르소나 호출 폐기 → 10 페르소나 (00 + 01-07 + 09) + silo 차단 룰.

---

## 1. 페르소나 구조 v2 (10 페르소나)

| 페르소나 | 영역 | 권한 |
|---|---|---|
| **00** | **Genre Identity (메타)** | **청사진 환류 권한·09 진단 직접 수용·다른 페르소나 "유지" 무력화** |
| 01 | Intimacy / Sexual Scene | 정사·신체 비트 |
| 02 | AIGC Production | 양식·VFX·블로킹 |
| 03 | Continuity / Logic | 공간·시간·인과 |
| 04 | English Dialogue / Voice | 대사·시적 톤 |
| 05 | Commerciality / Marketing | 페이월·결제 트리거 |
| 06 | Visual Appeal / Character Lock | 비주얼 락·어셋 |
| 07 | Genre Pleasure | 장르 쾌감 (메타 결함의 부분 영역) |
| 09 | Female Viewer Diagnostic | **시청자 진단 — 처방 권한은 00이 수용** |

→ 페르소나 08 (남성 시청자) = 남성향 작품 한정 (동일 처방 룰).

---

## 2. silo 차단 룰 (절대)

### 2.1 페르소나 09 처방 강제 trigger
**옛 룰:** 09 = 진단 한정·처방 권한 X.
**v2 룰:** 09 시청자 발견 이탈 코드 (F-A ~ F-L) = **페르소나 00이 직접 처방으로 변환**. 다른 페르소나가 안 받아도 무력화 못함.

예 (OFFERING 실제):
- 09 Round 1 발견: "F-C Vael 변질·F-L 보호 친밀 약화 EP31+"
- 옛 시스템: 처방 페르소나 안 받음 → 무시 → LOCK 통과
- v2: 페르소나 00이 직접 수용 → "후반 정치물 변질·청사진 환류 trigger" 처방 → BLUEPRINT RETURN

### 2.2 메타 결함 발견 시 다른 페르소나 "유지" 무력화
- 페르소나 00이 "장르 정체성 변질" 또는 "후반 paid 동력 약화" 발견 시
- 다른 페르소나의 "검토했으나 유지" 판정 = 자동 무력화
- 메타 결함 = 부분 결함의 패치로 해결 불가

### 2.3 청사진 거슬러 올라가는 권한
- 본문 결함이 청사진 단계 결함에서 비롯 시 → 청사진 환류 강제 trigger
- 페르소나 00 verdict = "GENRE WARNING·BLUEPRINT RETURN" 또는 "GENRE FAIL·FULL REWRITE"
- 이 경우 본문 패치로 LOCK 불가. **청사진 재설계 후 새 본문 작성** 강제.

### 2.4 검증 작품 직접 비교 강제
- 모든 페르소나가 검토 시 같은 장르 검증 작품 1편 이상 본문 직접 정독
- 메모리 인사이트만 X / `config/vertical_drama_hit_scripts/`·`config/hit_library/` 직접 참조
- "메모리 본문 인용했음" = 통과 사유 아님

---

## 3. v3 진단 baseline 통합 (모든 페르소나 강제)

**모든 페르소나 검토 진입 시 v3 진단 baseline 정독 강제 (다크 로맨타지·werewolf·vampire·dragon romance 작품 한정):**

- `feedback_dark_romantasy_paid_vertical_v3_diagnosis.md` (절대)
- 페르소나가 자기 영역 검토 시에도 v3 진단 baseline에 따라 평가
- 예: 페르소나 05 페이월 검토 시에도 "후반 정치 vs mate·heir 확정" 기준 적용

---

## 4. 검토 진행 순서 v2

### 옛 순서 (silo):
1. 9 페르소나 병렬 검토
2. 종합 = MEMORY.md 안내·처방 페르소나가 수용 여부 결정
3. 4-Gate 양식·정합성 평가
4. LOCK

### v2 순서 (silo 차단):
1. **페르소나 00 사전 스캔 (메타 결함 의심 10+)** — 청사진 단계 + 본문 큰 그림 + 검증 작품 비교
2. **페르소나 01-07 + 09 병렬 검토** (자기 영역)
3. **페르소나 00 종합 + 09 진단 처방 변환**
4. **페르소나 00 verdict 결정:**
   - GENRE OK·LOCK
   - GENRE OK·PATCH THEN LOCK
   - GENRE WARNING·BLUEPRINT RETURN (청사진 환류)
   - GENRE FAIL·FULL REWRITE
5. 1·2 verdict → 본문 패치 후 5-Gate (Genre Identity Gate 포함)
6. 3·4 verdict → 청사진 재설계 또는 전면 재작성

---

## 5. 페르소나 정의 파일 갱신 룰

`config/personas/` 9 파일 (01-07·08·09) 본문 정정 = 큰 작업. 본 메모리 v2가 **상위 룰**로 작동. 페르소나 정의와 본 메모리 충돌 시 **본 메모리 우선**.

- 페르소나 00 정의 = `config/personas/persona_00_genre_identity_auditor.md` (2026-05-19 신규)
- 페르소나 01-09 정의 = 옛 파일 유지 / 본 메모리 v2 강제 적용

---

## 6. 5번째 Gate — Genre Identity Gate (4-Gate → 5-Gate)

phase_7 4-Gate 평가에 5번째 Gate 추가:

| Gate | 영역 | 책임 |
|---|---|---|
| 1 | Structure | phase_7 |
| 2 | Narrative | phase_7 |
| 3 | Script | phase_7 |
| 4 | Production | phase_7 |
| **5** | **Genre Identity** | **페르소나 00** |

5-Gate 미통과 시 LOCK 불가. 청사진 환류 또는 본문 전면 재작성.

---

## 7. 자가 검수 (검토 진행 시 강제)

1. 페르소나 00 사전 스캔 진행했는가?
2. 09 진단 → 00 처방 변환 강제 적용했는가?
3. v3 진단 baseline 정독했는가?
4. 검증 작품 본문 직접 정독했는가? (메모리만 X)
5. 페르소나 00 verdict 받았는가?
6. 5-Gate 모두 통과했는가?

→ 1개라도 NO = LOCK 불가.

관련: [[dark-romantasy-paid-vertical-v3-diagnosis]] / [[demon-lord-failure-postmortem]] / [[review-master]] / [[4gate-persona-validation]] / [[hit-library-v2-2026-05-19]] / [[hit-scripts-folder-priority]]
