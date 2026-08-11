---
name: token-diet-70-percent
description: 🚨🚨🚨 최상위 룰 (2026-05-27 사용자 명시). 토큰 소모 70% 컷·최종고까지 종래의 30% 토큰만. Background agent·multi-pass rewrite·persona 검토·report 폐기·direct Bash 우선·prompt 압축. 모든 작품·모든 phase 적용.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 822d9a9c-17d7-46a8-b0d9-5716ec65a086
---

# 🚨🚨🚨 토큰 다이어트 — 70% 컷·종래의 30% 모드

## 사용자 명시 (2026-05-27)

> *"너의 토큰 소모량이 60% 이상 줄여야함. 아니. 내가 봤을 땐 70% 이상 줄여야함. 즉 최종고 확정까지 걸리는 토큰량을 종래의 30% 수준으로 떨궈야함."*

## Why

SHE STOLE MY FACE 50 EP · phase_4-7 · 라운드 1-3 = 토큰 폭탄. 매 라운드:
- Background agent 6-10개 동시 launch (각 자기 context 잡아먹음·메모리 정독·히트작 정독·EP read·rewrite·report)
- 페르소나 검토 3개 (각 50 EP scan)
- Sweep agent 추가
- Final-consolidator 추가

→ 사용자 평가가 가장 정확하고 빠른데 *agent 위임으로 시간·토큰 5-10배*.

## 7 룰 (즉시 적용·모든 작업)

### 룰 1. Background agent 최소화
- agent 호출 = 마지막 수단
- 메인 context에서 직접 처리 우선 (Bash·Edit·grep·sed)
- agent 호출 시 = 단 1개·필요 시만

### 룰 2. 메모리 새 파일 폭증 금지
- 새 인사이트 = 기존 메모리에 짧게 추가
- 새 메모리 파일 = 사용자 명시 + 영구 가치 있을 때만
- always-load 메모리 = 9-10개 max (현재 13개)·중복 통합

### 룰 3. 페르소나 검토 폐기 (대부분)
- 페르소나 04·09·Three-Gate 등 50 EP 전수 scan = 토큰 폭탄
- 사용자가 직접 평가 = 가장 정확·빠름
- 페르소나 검토 = phase_5 최종 1회 미만·아예 X 권장

### 룰 4. Multi-pass rewrite 폐기
- "1차 rewrite → 검토 → 패치 → 재작업 → 통합" = 4-5단계 토큰 곱셈
- 1번에 완성도 75% 목표·사용자 평가·필요한 부분만 surgical patch

### 룰 5. Agent report 폐기
- agent에 "report under 300 words" 요구 = 길게 정리·토큰 낭비
- 결과 파일 경로 + 0-1줄 요약만

### 룰 6. Direct Bash·grep·sed·awk 우선
- 1순위: Bash one-liner (5-10배 효율)
- 2순위: Edit tool (surgical)
- 3순위: agent (마지막 수단)
- 검증·통합·치환 = Bash 직접

### 룰 7. Prompt 압축
- agent prompt 길이 = 1000자 max
- 메모리 인용 = 경로만·"읽어라" 없이
- spec table 1개로 압축

## 적용 매트릭스

| 작업 | 종래 (X) | 다이어트 (O) |
|---|---|---|
| 50 EP 집필 | 6 batch 병렬 agent | 사용자 spec → 1 agent·1 pass |
| 검토 | 3 페르소나 + Three-Gate | 사용자 직접 평가 |
| 패치 | 4 batch 병렬 agent | grep + Edit 직접·agent 1개 |
| 통합 | final-consolidator agent | Bash concat + grep verify |
| 메타 갱신 | agent 위임 | 직접 Edit |
| 메모리 갱신 | 새 파일 생성 | 기존 파일에 짧게 추가 |

## 자가 점검 (매 작업 시작 시)

1. 이 작업이 agent 필요한가? 아니면 Bash·Edit으로 직접 가능? → 직접
2. agent 호출 시 — 정말 1개만? Multi-batch 필요한가? → 1개로 통합
3. agent prompt 1000자 초과? → 압축
4. 페르소나 검토 부르는가? → 사용자 평가로 대체
5. 새 메모리 만드는가? → 기존에 추가 가능?
6. Report 요구하는가? → 결과 경로 + 한 줄
7. multi-pass 계획? → 1 pass + surgical patch만

## SHE STOLE 라운드 비교 (학습)

### 종래 (라운드 1+2+3):
- Phase 4: 6 batch + 3 batch 재시도 + 5 batch 완전 재작업 = **14 agent**
- Phase 5: 3 페르소나 = **3 agent**
- Phase 6: 4 batch 패치 = **4 agent**
- Continuity sweep: 2 agent
- v2 sweep: 1 agent
- Final consolidator: 2 agent (v1 + v2 + v3)
- **총 26 agent calls**

### 다이어트 모드 (목표):
- Phase 4: 사용자 spec → 1 agent → 50 EP 본문 1 pass
- Phase 5: 사용자 직접 평가 (1 round)
- Phase 6: 발견 issue → 직접 Bash·Edit (agent 0)
- Final: 직접 Bash concat (agent 0)
- **총 1-2 agent calls** = 토큰 70-90% 컷

## 연관

`[[vertical-structure-hit-script-lesson]]` (vertical 구조 학습) · `[[no-theater-tone]]` (7 차원) · `[[no-ai-korean-jargon]]` (한국어 jargon 금지·최상위 룰)
