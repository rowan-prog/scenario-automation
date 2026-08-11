---
name: lock-exhaustive-line-audit
description: 최종 LOCK 검수 필수 방식 — spoken-english(시적/연극적/소설적 대사 금지)는 모든 대사를 한 줄씩 enumerate-then-verdict 전수(샘플링 금지·누락 0). 동작 정합성은 모든 동작을 직전 동작과 대조(앞동작 모순 허다). 집필+검수 양쪽.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2232c2a-2d77-4cdb-97dc-f680b25e871b
---

# 최종 LOCK 검수 — 전수(per-line) 방식 필수

**룰 (2026-06-08 사용자 명시·LOCK 한정·집필+검수 양쪽).** 최종 LOCK 검수에서 두 축은 **반드시 전수(exhaustive)**다. "읽다가 눈에 띈 것만 flag" = 라인 누락의 원인 = 금지.

## 1. Spoken-English 전수 (per-line)
**vertical spoken-english 여부(= 시적 대사 금지·연극적 금지·소설 서술체 금지)는 단 한 개의 대사도 놓치지 않고 검사.**
- 방법 = **enumerate-then-verdict.** 먼저 모든 [DIALOGUE] 라인 + 모든 VO/NA를 *전부 열거*(grep로 완전 목록 추출 → 빠진 줄 0 보장) → 그 목록을 **한 줄 한 줄 PASS / FLAG** 판정.
- FLAG 기준: 시적/은유 · 연극톤 · 소설 서술체 · 낭송 cadence(tri-colon/anaphora/mirror) · 번역투 · 톤 의존 의미([[ai-dub-tone-independent-dialogue]]) · 미세표정 의존 지문.
- 시그니처/엔진 모티프(제목 conceit 등)는 보존하되 *표기*는 한다(누락이 아니라 의도 보존임을 명시).
- 기계 1차 = `tools/voice_lint.py --full`(전 카테고리). 단 패턴 미탐지분(예: 맥락상 소설체)은 per-line 인간 패스가 메운다 — 기계만으로 끝내지 않는다.

## 2. 동작(지문) 정합성 전수 (action-to-action)
**지문/동작이 *앞 동작과 모순*되는 경우가 허다하다.** 씬 순서대로 **모든 [VISUAL/ACTION]·[KEY CAMERA] 비트를 하나씩 추적하며 직전 상태와 대조**한다.
- 추적 항목: 위치(누가 어디)·자세·소품 위치/소유·부상·인물 지식(누가 무엇을 아는가)·시선·시간/연속 태그(Continuous인데 두 장소 동시?).
- 동작 A→B로 넘어갈 때마다 "B가 A와 모순 아닌가" 1줄 점검.
- **실제 적발 사례(v46까지 잔존):** EP07 "머리채 잡기 삭제했는데 'releases the hair' 잔존" / EP02 S#3 "Continuous"인데 Mara가 세단 안 + 연단 생중계 동시.

## 3. 집필에서도 동일
- 집필 시 다음 동작을 쓰기 전에 직전 동작/상태를 확인(앞동작 모순 차단).
- 집필 시 매 대사를 vertical spoken으로(시적/연극/소설체 금지) — 검수에서 잡기 전에 쓸 때 거른다.

**Why:** AI 영상+AI 더빙 제작. 시적/연극/소설체 대사는 더빙·세로 단컷에서 죽고, 동작 모순은 AI 영상이 그대로 렌더해 결함이 박제된다. LOCK은 마지막 방어선이라 한 줄·한 동작도 못 놓친다.

**적용 범위:** **LOCK 직전(또는 "철저 검토" 명시)에만** 이 전수 방식. 일상 incremental "검토"는 diff 경량(`config/final_review_flow.md` 검수 강도). 즉 *무겁게 자주*가 아니라 *LOCK에 한 번 완전하게*.

## 관련
- [[ai-dub-tone-independent-dialogue]] · [[no-theater-tone]] · [[real-human-speech-01s-test]] · [[claude-voice-bias-vertical-failure]]
- 절차 단일 진실 = `config/final_review_flow.md` 패스 2(동작 정합성 전수)·패스 7(spoken-english per-line).
