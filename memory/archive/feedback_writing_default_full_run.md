---
name: 2026-05-17
description: phase_3 청사진 완성 후 무료 EP1-8 자동 진행 OK. **유료 EP9-50은 사용자 명시 지시 시에만 진행** (자율 진행 X).
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 462b4a02-4290-4164-a105-ac1f2ff0ecca
---

# 집필 진행 룰 (2026-05-17 정정 — 사용자 명시)

## 핵심 (사용자 명시 2026-05-17)

> **"유료회차는 내가 지시하기 전에 하지마라."**

옛 룰 ("phase_3 이후 자동 50화") **정정 폐기.**

## 새 룰

### 무료 EP1-8 — 자동 진행 OK
- phase_3 청사진 완성 후 자동 진행
- protocol_premium_pilot_lite 또는 phase_4 사이클
- 사용자 명시 지시 없어도 무료 완성까지 진행 가능

### 유료 EP9-50 — 사용자 명시 지시 시에만
- **자율 진행 X**
- 무료 완성 후 → 사용자 결정 대기
- 사용자가 "유료 진행" 명시 시에만 phase_4 EP9 진입
- 임의 진입 X / 청사진에 50화 락 있어도 임의 집필 X

## 진행 흐름

```
phase_3 청사진 (50화 락) → 
무료 EP1-8 자동 (protocol_premium_pilot_lite) → 
FINAL_FREE 완성 → 
🚨 사용자 결정 대기 (정지) → 
사용자 "유료 진행" 명시 시 → 
유료 EP9-50 phase_4·5·6·7 사이클
```

## Why

사용자 명시:
- 무료 = 검증·반복 patch가 잦음 (G v2·v3·v4·v5 등 사례)
- 유료 = 무료 patch 완성·시스템 baseline 안정·사용자 평가 후 진행이 효율
- 자율 유료 진행 = 옛 baseline 잘못 적용 시 매출 박살 위험
- 무료 완성 후 사용자가 평가·baseline 조정 후 유료 진입이 최적

## How to apply

- **무료 EP1-8 완료 시 = 정지 + 사용자 보고 + 결정 대기**
- 다음 옵션 제시:
  - 무료 patch (사용자 평가 후)
  - 유료 EP9-50 진행 (사용자 명시 시)
  - 다른 작품 / 시스템 갱신 / 청사진 환류
- 사용자 명시 없으면 유료 진행 X

## 기존 메모리 정합

- `feedback_no_ask_autonomous.md` (자율 진행 룰) — 본 메모리 우선 (유료는 예외)
- `feedback_episode_split_and_runtime.md` (50화 고정·무료 1-8화) — 정합
- `feedback_writing_default_full_run.md` (구버전 룰) → **본 메모리로 대체**

## 핵심 한 줄

> **무료 EP1-8 자동 진행 OK. 유료 EP9-50 = 사용자 명시 지시 시에만. 자율 진입 X.**
