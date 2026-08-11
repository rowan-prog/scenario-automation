---
name: master-platform-safe-dual-version
description: "초고수위 다크 로맨스 작품 = master version + platform-safe production version 이원화 강제. master = high-heat 보존·platform-safe = 카메라·문장 우회 본문. 둘 다 동시 보관. 2026-05-19 V16 통합 피드백."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2d65e927-1cd5-4df0-bd23-1493c3adfb18
---

> **근본 진단:** 초고수위 다크 로맨스 작품 = 한 파일에서 master·platform 둘 다 달성 불가 시 = 이원화. 단일본으로도 production-ready 달성 가능 시 (platform-safe 기반 + agency 보강) = 사용자 결정 = 단일본 OK.

## 룰

**초고수위 작품 = master + platform-safe 두 파일 운용 옵션 (사용자 결정).** 단일본 채택 시 = platform-safe 기반 + agency·tension 보강 = production-ready·OSMU 필요 시 master 별도 복원 archive에서 가능.

### 작품별 결정 가이드

| 시나리오 | 권장 |
|---|---|
| 웹소설 + 영상 동시 OSMU | 이원화 (master 웹소설용·safe 영상용) |
| 영상만 (paid vertical) | 단일본 (platform-safe 기반 + agency·tension 보강) |
| AIGC 어셋 생성 only | 단일본 (safe 기반) |
| 사용자 미결정 | 이원화 default·archive에서 옵션 유지 |

### 파일 구조

```
07_final/
├── [작품]_FINAL_v{N}.md                  ← master version (high-heat 보존)
├── [작품]_FINAL_v{N}_platform_safe.md    ← platform-safe (카메라·문장 우회)
└── _archive_versions/
```

## Master version (high-heat)

**기능:** 작품 정체성·다크 로맨스 농도 유지. 사용 = 개발·청사진 환류·내부 검수·메타 baseline.

**보존:**
- 명시적 신체 결합 함의
- 부위 직접 묘사 (단 시선 우선·female gaze 룰)
- 통제·소유 표지 강화
- 감각 3축 (촉각·숨소리·피부)
- 광기 보존 (Vael full red eyes·shaking·burn the world)
- Mark 위치 명시

## Platform-safe version (production)

**기능:** 영상화·플랫폼 송출용. 카메라·문장 우회로 신체 직접 묘사 줄임. 함의 유지·표현 우회.

**우회 룰:**

| 위험 | 우회 |
|---|---|
| "He settles between her thighs" | "He lowers himself over her on his forearms" |
| "He pushes inside her slow" | "His weight settles. Her breath catches three times." |
| "When he moves slow first, then not slow" | "The firelight on his shoulder. The black sheet pulling tight at her hip. Her hairline darkens with sweat." |
| Body mechanics 진행 묘사 | Cutaway → breath / sheet / firelight / scale / hand / mark |
| Inner thigh / under breast close-up | Palm cover / aftermath / Vael reaction |
| Postpartum mark | 회복 후로 이동·Isolde 주도일 때만 |
| 신체 부위 부위 순회 tracking | Vael 통제 상실·Isolde agency 우선 |

**유지 (platform에서도):**
- Vael의 통제 상실 (scales·breath·shaking)
- Isolde agency ("I'm on top"·"I waited")
- Mark 결과 (palm cover·aftermath)
- 결합 함의 (직접 묘사 X / 강한 implication)
- 광기 보존 (sound design·firelight·shadow)

## 작업 방식

### 1차: Master 작성 (초고수위 보존)
청사진→집필 단계에서 master로만 작성. 다크 로맨스 정체성 우선.

### 2차: Platform-safe 변환
master 완성 후 별도 파일 생성. 초고수위 씬 (EP03·EP10·EP21·EP43·EP46·bath 씬 등) = 우회 본문으로 정정. 다른 EP = master 그대로 carry.

### 변환 자동 검수
- 본문 직접 body mechanics 0건 확인
- "settles between thighs"·"pushes inside"·"moves slow then not slow" 등 0건
- Cutaway·firelight·breath 표현 ≥1건 (각 초고수위 씬)
- Vael 통제·Isolde agency 비트 보존 확인

## 한 작품 운용 예시 (OFFERING)

| 파일 | 사용처 |
|---|---|
| `02_the_offering_FINAL_v17.md` (master) | 내부 baseline·다음 작품 학습·전체 정체성 |
| `02_the_offering_FINAL_v17_platform_safe.md` (production) | 영상화·플랫폼 송출·prompt engineering 입력 |

## 자가 검수 (초고수위 작품)

1. **Master + platform-safe 두 파일 모두 존재하는가?**
2. **Master version에 초고수위 씬 명시 4-6개 있는가?**
3. **Platform-safe version에 body mechanics 직접 묘사 0건인가?**
4. **두 version 모두에 Vael 통제 상실·Isolde agency 보존되어 있는가?**
5. **메타 (`[작품]_00_meta.md`)에 두 version 명시되어 있는가?**

→ 1개라도 NO = 작업 미완.

## 옛 시스템 룰과 정합

- `feedback_dark_romance_high_explicit_4_prescriptions.md` (4 처방·초고수위 강화) — master version 적용.
- `feedback_female_gaze_camera_polish.md` (시선 교정) — 두 version 모두 적용.
- `config/hard_rules.md` 룰 7 (이원화 명시).

## 절대 한 줄

> **초고수위 작품 = master + platform-safe 이원화. master 보존·platform 우회. 둘 다 동시.**

관련: [[dark-romance-high-explicit-4-prescriptions]] / [[female-gaze-camera-polish]] / [[screen-rhythm-v3-blocks]]
