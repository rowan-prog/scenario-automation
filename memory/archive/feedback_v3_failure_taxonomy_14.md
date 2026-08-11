---
name: v3-14-f-a-f-n
description: paid vertical 매출 fail 14 패턴. 페르소나 검토 자동 trigger codes. 1건 검출 = 즉시 🔴.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 462b4a02-4290-4164-a105-ac1f2ff0ecca
---

# v3 23 핵심 실패 유형 14종 — Trigger Codes

`config/master_guide_v3.md` PART 11 23장 발췌. 페르소나 검토 자동 trigger codes.

## 14 Failure Codes (F-A ~ F-N)

| Code | 실패 유형 | 책임 페르소나 | 자동 등급 |
|---|---|---|---|
| **F-A** | 가치 간극 없음 (실제 가치 ≈ 거짓 판결 = 작은 차이) | 03·07 | 🔴 |
| **F-B** | 대체자 약함 (위협감 X·매력 X) | 02·07 | 🔴 |
| **F-C** | 공동체 오판 약함 (대표 인물 부재·군중 부재) | 02·07 | 🟡 |
| **F-D** | 관객이 진실 모름 (관객 우월 인식 부재) | 03 | 🔴 |
| **F-E** | 무료 보상 빨리 (페이월 전 보상 완결) | 05 | 🔴 |
| **F-F** | 고통만 반복 (보상 단계 설계 부재) | 05·07 | 🟡 |
| **F-G** | 후회 쉬움 (후회남이 빠르게 용서받음) | 01·07 | 🟡 |
| **F-H** | 남성향 무력감 김 (EP1-2 1층 보상 미달) | 08 | 🔴 |
| **F-I** | 소재 공식 복제 (기능 슬롯 없이 표면만) | 07·05 | 🟡 |
| **F-J** | 공개 무대 없음 (사적 화해만) | 02·07 | 🟡 |
| **F-K** | 비주얼만 강함 (감정 장부 부재) | 06·05 | 🟡 |
| **F-L** | 약속 무료에 X (제목·광고 약속 미실행) | 02·05 | 🔴 |
| **F-M** | 세계관 복잡 (EP1-2 진입 압력 큼) | 02·03 | 🟡 |
| **F-N** | 미감 약함 (AIGC 비주얼 강점 안 활용) | 06·02 | 🟡 |

## 자동 Trigger 룰

phase_5 검토 진입 시 페르소나가 14 codes 자동 스캔:

- 각 코드별 검출 자가 답
- 검출 시 코드 + EP/S#/원문 FIND 인용 + 등급
- 0 검출 시 검토 강도 약함 의심 (메모리 `feedback_review_master.md`)

## 시청자 페르소나 이탈 코드와의 관계

- **F-A ~ F-N** = 제작 페르소나 (01-07) 자동 trigger
- **M-A ~ M-J** = 시청자 페르소나 08 (남성) 진단
- **F-A ~ F-L** = 시청자 페르소나 09 (여성) 진단 (별도 — 본 메모리의 F 코드와 다름)

⚠️ Naming 충돌 주의 — F-A는 두 개:
- v3 14 failure (본 메모리, 제작 페르소나)
- viewer persona 09 이탈 코드 (별도)

호출 시 명시: "v3 F-A" vs "viewer F-A".

## 검토 보고 양식

```
### v3 14 Failure 자동 스캔 (페르소나 NN 검토 — 보조)

| Code | 검출 | EP | S# | 원문 FIND | 등급 |
|---|---|---|---|---|---|
| v3 F-A | ✅ | EP3 | S#2 | `Just another worthless porter.` | 🔴 |
| v3 F-E | ⚠ | EP7 | S#5 | 페이월 직전 KAEL 완전 인정 | 🔴 |
| v3 F-H | (남성향이 아니라 N/A) | - | - | - | - |
```

## How to apply

- **phase_5 검토 진입 시 자동:** 페르소나가 자기 영역 코드 우선 스캔
- **protocol_premium_pilot Step 15 (Persona Adversarial)** 진입 시 자동 적용
- **검토 강도 = strict** 일 때 14 코드 모두 자가 답 강제

## 핵심 한 줄

> **14 failure codes = paid vertical 매출 fail 패턴. 페르소나 검토 자동 trigger. 검출 = 즉시 🔴/🟡.**
