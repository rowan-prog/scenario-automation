---
name: lock-fix-volume-writing-diagnostic
description: LOCK 단계 수정량 = 집필 품질의 진단지표. 논리오류 수십 건이 LOCK에서 나오고 수정이 새 seam을 낳으면(whack-a-mole) = 검수 꼬리가 아니라 집필 자체의 오류. 근본 = 집필 시 continuity state-ledger 부재. 고침은 upstream(집필 시 ledger) + holistic(상호연결은 piecemeal 금지).
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2232c2a-2d77-4cdb-97dc-f680b25e871b
---

# LOCK 수정량 = 집필 품질 진단지표 (2026-06-10 사용자 명시·SHE STOLE v49)

**사용자 지적:** "LOCK을 위해 수정이 이렇게 많이 된다면 집필 자체의 오류 아닌가." → **정확.**

## 진단
- **잘 쓴 대본 → LOCK 검수는 *확인*(0-2건). 내 대본 → LOCK이 *발견*(65건).** 그 격차 = 집필 실패의 증거. 검수 long-tail로 둘러대지 마라.
- **근본 원인 = 집필 시 continuity *state-ledger* 부재.** 나는 프로스는 유창하나 50화 상호연결 *상태*를 추적하며 쓰지 않는다: ①타임라인(언제/몇시간 경과) ②knowledge-order(누가 언제 무엇을 아는가·증거 출처) ③위치/공간(누가 어디·이동) ④소품/상처(언제 생겨 언제 회수) ⑤인물 현장유무(char list ↔ 실제 등장) ⑥세계룰(예: flagged-face=즉시 퇴장·impostor 통과). → seam이 *집필 단계에서* 박힘. (claude-voice-bias의 논리版: 문체는 좋으나 상태추적 0.)
- **piecemeal LOCK 패칭 = whack-a-mole.** 상호연결 대본은 한 곳 수정이 다른 비트를 깬다(SHE STOLE v49: EP1·EP9·EP15·EP37·EP47에서 *내 수정이 새 seam 생성*). C-logic HARD가 6→1→1→5→3로 *진동*(0 수렴 X) = 신선한 적대패스가 deep-tail + 내 새 seam을 매번 ~3-5건 새로 발견. 토큰 폭발의 정체.

## 처방 (upstream + holistic)
1. **집필 시 canon state-ledger를 쓰면서 유지.** EP 쓸 때마다 위 6축 갱신·다음 비트는 직전 상태 대조 후. LOCK은 *확인*만 하게.
2. **수정은 holistic.** 상호연결 seam은 *전체 ledger를 펴 놓고 한꺼번에* 고친다(한 비트 고치면 연결 비트 동시 점검). piecemeal 금지.
3. **LOCK 수정량을 메트릭으로 본다.** LOCK에서 논리 HARD가 다수 = "더 패치"가 아니라 "집필/구조 재점검" 신호. 자가검수 단일 진실 = `config/lock_pipeline_standard.md` + [[lock-exhaustive-line-audit]].
4. **토큰:** LOCK 단계 적대감사 반복은 비싸고 asymptotic(deep-tail). 싸고 효과적 = 집필 시 ledger + 1회 holistic ledger 패스. 무한 재감사 루프 금지.

## How to apply
- 새 작품/대수술: 집필 *전* canon-ledger 골격 잡고 EP마다 갱신.
- 기존 대본 LOCK 전: 1회 holistic continuity-ledger 패스(전 상태 한 번에 구축→모든 contradiction 동시 enumerate→holistic 수정) → 그 다음 LOCK은 확인.
- LOCK 적대감사가 논리 HARD 다수 반환 = 집필 빚 신호. piecemeal 추가패치 말고 ledger로.

관련: [[claude-voice-bias-vertical-failure]](문체 편향의 논리版) · [[lock-exhaustive-line-audit]](per-line 동작정합) · [[emotion-to-action-aigc-writing]] · lock-pipeline=`config/lock_pipeline_standard.md`.
