# Phase 7 — 최종고 게이트 (보호 단계)

> **v4 (2026-06-05 전면 재작성):** 페르소나 verdict 진입 게이팅·5-Gate 페르소나 00·Gate↔페르소나 매핑·FULL REWRITE 라우팅·버전 없는 FINAL.md·EP별 07_final 복사 = 전부 폐기. 운용 단일 진실 = `config/agent_operating_rules.md` · **검수 절차 단일 진실 = `config/final_review_flow.md` (같은 날 신설 — 10+3패스·모드 선택·쇼러너 merge).**

## 역할 — 이 단계의 정의 (최상위)

**최종고/LOCK = 오류 조정과 엔진 보호 단계다. 재미는 이미 만들어져 있어야 한다.**
- 여기서 "재미있게 만들자" = 이미 늦은 것 (쾌감은 phase_0-6의 중심).
- 동시에 다림질(세련화·표준화) 금지 — **이미 재미있는 원고가 무너지지 않게 잠그는 단계.**
- 잡는 것: 논리·정합성·동선·지식/정보 순서·보이스 일관·포맷·금칙어·잔존 오류.
- 안 하는 것: 새 비트 추가·톤 개선·문장 다듬기·구조 변경.

## 진입 조건 (운용 룰 §4 LOCK 전 최소셋)

1. **voice_lint** 통과 (작품 baseline 이내)
2. **fresh-eyes-auditor** 전수 정합성 감사 1회 (CRITICAL/HIGH 0 또는 전부 처리됨)
3. **funnel-cold-reader** 독립 3회 수렴 (engine brief §4 게이트 기준 충족)
4. 사용자 LOCK 신호 (검토 결과 보고 후)

— self "clean" 단독 신뢰 금지. 1-3 미충족 시 진입 불가 → 해당 검수부터.

## 4-Gate 체크 (production_guide Section 23 — 쇼러너 직접)

각 Gate 진입 전 그 Gate에서 깨질 수 있는 의심 지점 5+건 먼저 스캔. **모든 통과 판정도 원문 인용 또는 검증 명령 결과 동반** ("Hard Lock 충족"이 아니라 "EP8 페이월 — `인용` + 4요소 본문 확인" 형식). 추상 평가 금지.

- **Structure (23-1):** 결핍 선명·욕망 한 줄·무료 수렴·페이월 절단·유료 초반 보상 회수.
- **Narrative (23-2):** 캐논·관계 원리·세계 규칙·정보 공개 순서·reveal 어휘 미소모·인물이 알 수 없는 정보 발화 0.
- **Script (23-3):** 기능-only 대사 X·살아있는 반응·물리적 지문·AIGC 구현 가능·씬 끝 갱신.
- **Production (23-4):** 동선·아이템 위치·외형 락·UI 정보·섹슈얼 포인트 기능 연결·페티시 과잉 X.

**Soft Lock 영역(톤·대사 방식·인티머시 강도·캐릭터 매력 강약)은 미통과 사유가 아니다** — "더 다크해야/더 매력적이어야" 류 지적은 작품 자율.

### 트랙별 정합성 기준

- 메인: `04_blueprint_full.md` / 부가 A: `01_adaptation_blueprint.md` / 부가 B: 청사진 부재 → 대본 내적 일관성.

## 미통과 처리 (페르소나 매핑 폐기 — 쇼러너 판정)

1. **기계 검출 (한국어·헤더 메타·footer·EP 누락/중복·블록 카운트)** → 판단 영역 X·즉시 수정.
2. **Soft Lock 영역 지적** → 즉시 reject.
3. **그 외** → 쇼러너가 운용 룰 §6 (필터 0 엔진 선판정 → 채택/거부)으로 판정 → phase_6 외과 수술 → **delta 재검수** (전량 재라운드 X) → 본 게이트 재진입.
4. 판단 충돌·구조 결함 → 사용자 결정 (PushNotification).

우선순위 최상위: **작품 쾌감·캐릭터 매력·production_guide > 체크리스트.** 체크리스트가 쾌감과 충돌하면 쾌감을 보존하는 방식으로만 수정 (한 줄/한 행동).

## 통합·기계 검증 (final-consolidator agent 위임 권장 — 1벌)

- **산출 = `projects/[작품]/07_final/[작품]_FINAL_v{N}.md` 단일 파일** (버전 필수·기존 정본 덮어쓰기 금지 = version-anchor). EP별 분리 X·FREE/PAID 분리는 요청 시만.
- 파일 = 타이틀 + 본문만 (헤더 spec·버전 노트·작업 과정 금지 — [[script-file-zero-meta]]).

| 게이트 | 기준 | 실패 |
|---|---|---|
| 한국어 (EP 본문) | 0건 (`\p{IsHangulSyllables}`·`[ㄱ-ㆎ]`) | 🔴 즉시 — 원본 수정 후 재생성 |
| EP 헤더 수·순서 | = EP 수·EP1→끝 | 🔴 |
| Hard Cut | = EP 수 - 1 (+ 마지막 EP 자연 END 1) | 🔴 |
| [END HOOK] | = EP 수 | 🔴 |
| 헤더 메타 | 0 | 🔴 |
| 블록 양식 (v3) | [VISUAL/ACTION]·[DIALOGUE]·[KEY CAMERA] 등 일관 | 🟡 |
| char count | 작품 spec 범위 (default 70-80k) — 실측 보고 | 🟡 |
| voice_lint | baseline 이내 | 🟡 |
| 깨진 패턴 grep | 빈 블록·중복 헤더·고아 태그·이중 separator 0 | 🔴 |

🔴 발견 → 원인 EP 수정 → 재생성 → 재검증. 모든 작품(메인/부가A/부가B) 동일 적용.

## 통과 후 (LOCK)

1. `[작품]_00_meta.md` 갱신 (정본 경로·게이트 실측치·LOCK 일자).
2. CLAUDE.md 작품 행 = 현재 상태 + 포인터만 갱신 (이력 누적 금지).
3. **docs 환류 1회** (핸드오프 = `config/production_handoff_template.md` 양식·비주얼락·청사진 — 대본 실측 라인 검증 동반). LOCK 전 환류 금지 (운용 룰 §7).
4. **마케팅 셀링포인트 작성** (`config/mkt_selling_points_template.md` → `08_ad_creative/[작품]_mkt_selling_points_v{N}.md`) — 전회차 트리트먼트·✭ 키워드·MKT IDEA 5종. **작품의 진짜 마무리 산출물 (2026-06-05 사용자 명시).** 대본 수정 0.
5. 종료 안내 3줄: `✅ [작품] FINAL_v{N} LOCK — 경로` / `게이트: 전부 통과 (실측치)` / `다음: docs 환류·마케팅 셀링포인트 완료·대기`.
