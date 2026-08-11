---
name: agent-roster-orchestration
description: 검수 agent 7종 로스터 + 운용 8룰 (fresh-context 병렬·가드레일 의무·검수자는 보고만·교체는 천박한 쪽·구조 먼저·cold-read 다회 수렴·token-diet 정합·점수 해석). 2026-06-05 SHE STOLE v30→v41 + OFFERING v52→v68 학습 종합.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 71ca6a78-0b75-451b-9f8b-a515434062ed
---

# Agent 로스터 + 운용 룰 (2026-06-05 정착)

> **⚠️ 운용 단일 진실 = workspace `config/agent_operating_rules.md` (2026-06-05 이관).** 모순 시 그쪽 우선. 이 메모리 = 학습 배경(어떤 실패에서 나왔는지) 보존용.

3주간(SHE STOLE v30→v41·OFFERING v52→v68·외부 대본 검수) 검증된 작업방식을 agent로 정식화. 정의 위치 = `C:/Users/Rowan/.claude/agents/`.

## 로스터 — 어느 시점에 무엇

| Agent | 시점 | 역할 |
|---|---|---|
| **fresh-eyes-auditor** | **LOCK 전 의무**·대수술/재분절/이식 후 | 전수 정합성 감사 (셋업-회수선·지식상태·시간클럭·수술잔재·단역 EP 일관) |
| **funnel-cold-reader** | 페이월/무료부 수술 전후·LOCK 전 | NA 신규 시청자 구간 채점 + 이탈/결제 판정. **독립 3회+ 수렴 의무** |
| **native-ear-reviewer** | phase_4/6 후·LOCK 직전 | voice_lint 기계 1차 + 인간귀 2차 (번역투·문학톤·0.1초 테스트) |
| **persona-reviewer** | LOCK 전 구조 패널 (3-4인 병렬) | 페르소나 시점 구조/엔진 판정 먼저·line 나중. 9인 정기 라운드 폐기 |
| **external-intake-evaluator** | phase_b/c 외부 자료 | fresh 평가 + **막장-필터** (논리닫기/증거살리기/세련교체형 기각 권고) |
| **evaluator-panel** | phase_2 피칭 | 위원 7인 가상투표 (MASTER_DATASET + v2 확률 모델) |
| **final-consolidator** | 통합·일괄 변환 후 | 기계 게이트 (HC·END HOOK·카메라 샷 보존·word-diff·헤더 메타 0·voice_lint) |

## 운용 8룰

1. **fresh-context 병렬·사전 결론 비공유.** 검수자에게 내 진단/수정 내역을 결론 형태로 주지 않는다 (오염). 수술 *위치*만 알리는 건 OK.
2. **가드레일 의무.** 모든 검수 prompt에 장르 엔진 요약 + 의도된-설계 목록 + (native-ear엔) 시그니처 보존 목록 포함 — 거짓양성이 메인 대조 비용을 잡아먹는다.
3. **검수자는 보고만.** 수정 권한 X. 메인이 전 지적을 **원문과 1:1 대조 후 진성만 집행** (v41: 외부+내부 지적 ~40건 중 진성 21건만 집행).
4. **교체 방향 = 더 천박/직설/쉬운 쪽으로만.** 검수발 교체가 세련 방향이면 역방향 (웨이브→커튼 사건·[[claude-voice-bias-vertical-failure]]).
5. **구조/엔진 렌즈 먼저, line-level 나중.** line 지적 쌓고 #1 구조 결함 놓친 실패 2회 (v34·v37).
6. **cold-read 1회 점수는 노이즈.** 독립 3회+ 수렴으로만 의사결정. 낮은 구간은 "수술 가능" vs "엔진 고정 비용" 분리 판정 (EP9-12 6점 = 비용 판정 사례).
7. **token-diet 정합.** 검수단 투입 = LOCK 전·대수술 후·사용자 명시 시만. 평시 = voice_lint(0.5초·LLM 0) + 직접 한 줄 수술. 비싼 멀티패스가 퀄을 사주지 않는다.
8. **점수 해석 = 돈 변수.** 움직이는 건 점수가 아니라 이탈 화수(=인당 구매화수). "어디까지 보고 끄는가" > "몇 점인가".

**Why:** 자가검수는 같은 사각을 반복한다(자기 목소리·자기 수정이 만든 모순을 못 봄). 검증된 해법 = 기계(싸게) → fresh 외부 눈(병렬) → 메인 원문 대조(진성 선별) → 막장-필터(방향 통제)의 4단 파이프라인.

**How to apply:** LOCK 선언 전 최소 = voice_lint + fresh-eyes-auditor 1회 + cold-read 3회 수렴. 대수술 후 = +final-consolidator 게이트. 외부 피드백 도착 = external-intake-evaluator 막장-필터 먼저.

Link: [[fresh-eyes-full-inspection-method]] [[voice-lint-gate-pass]] [[claude-voice-bias-vertical-failure]] [[easy-dopamine-over-logic]] [[token-diet-70-percent]] [[bulk-script-verify-strict]]
