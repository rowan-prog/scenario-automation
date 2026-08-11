---
name: 시나리오 영어 일원화 (필수)
description: EP 본문은 영어 일원화 — 한국어 메타·footer·로그 절대 금지. 4-Gate Production이 한국어 검출 시 자동 fail
type: feedback
originSessionId: 764e3acd-d10a-4307-82be-cb216d64afc2
---
# 규칙

EP 파일과 통합 최종고는 **영어로만 기록**. 한국어 메타·footer·로그·비주얼 락 메모는 모두 영어로 변환 또는 제거.

## 적용 범위
- EP 파일(`projects/[작품]/05_episodes/*.md`): 첫 헤더(`# WORK — EPNN: TITLE`) + S#1 ~ Hard Cut 본문만. 헤더 메타(`**Function:**`, `**Information:**`, `**Cut:**`, `**Power Stage:**`, `**Look variants used:**`)·footer(`**Episode Update:**`, `**Series Update:**`, `**Hard Lock principle preserved:**`) 모두 금지.
- 통합 최종고(`projects/[작품]/07_final/[작품]_FINAL.md`): 한국어 0건.
- 비주얼 락 정보가 본문에 들어가는 경우 모두 영어 (캐릭터 첫 등장 시 [Visual] 안에서 영어로 묘사).

## Why
사용자 시나리오 표준 위반 사례 발생 (2026-05-08): 01·02 최종고에 한국어 메타·footer·환류 노트가 잔존했고, 4-Gate Production 검수가 이를 잡지 못함. 시청자가 보는 시나리오는 영어 일원화 필수 — 작가 노트는 별도 파일로 분리.

## How to apply
- **집필 시 (phase_4):** EP 첫 헤더 + S#1 ~ Hard Cut 본문만 작성. 작가 노트·메타 작성 금지.
- **검토 시 (phase_5):** 페르소나 02(AIGC Production Director)·06(Visual Lock Auditor)이 한국어 검출을 자동 🟡 trigger로 등재.
- **4-Gate (phase_7):** Production Gate에 한국어 검출 검증 추가 — `\p{IsHangulSyllables}` 또는 `[ㄱ-ㆎ]` 매칭 시 즉시 fail. 통과 조건: 0건.
- **통합 후 검증 (phase_7):** 통합 MD 생성 직후 한국어 0건·EP 헤더 50개·4-블록 카운트 일치 검증.

## 검증 명령 (PowerShell)
```powershell
Get-ChildItem "projects\<work>\05_episodes\*_ep*.md","projects\<work>\07_final\*_FINAL.md" |
  Select-String -Pattern '\p{IsHangulSyllables}' -Encoding UTF8
```
결과 0건이어야 통과.

## 작가 노트가 필요한 경우
EP별 작가 메모·환류 로그·검토 노트는 별도 파일로 분리:
- 환류 로그 → 청사진(`[작품]_03_blueprint_full.md` 또는 `_04_blueprint_full.md`) 끝에 영어 또는 한국어 자유.
- 검토 노트 → `06_reviews/round[N]/round[N]_summary.md` 한국어 자유.
- 메타 진행 상황 → `[작품]_00_meta.md` 한국어 자유.

EP 본문만이 영어 일원화 대상.
