---
name: flashback-source-ep-tag
description: 모든 flashback 컷에 source EP·씬 번호 명시 강제. AIGC production·storyboard 팀이 같은 shot 재사용·스타일 매칭할 anchor 필요.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37994db2-a795-4d48-9fe7-5e1a796a2110
---

# Flashback Source EP Tagging — 모든 회상 컷에 출처 표기

**룰:** 대본 안의 모든 flashback (회상·과거 재현) 컷에는 출처 EP·씬 번호 또는 시간 anchor를 반드시 표기한다.

**Why:** 사용자 명시 (2026-05-28). Vertical drama AIGC production = 같은 shot 재활용·스타일·미술·캐스팅 매칭 필수. Source EP 안 적힌 flashback = production 팀이 "처음 보는 장면인가? 이전 EP를 다시 찍는 건가?" 혼란. 시청자도 "내가 본 적 있는 장면인가" 빠르게 파악해야 결제·시청유지.

**How to apply:** 매 phase_4 (집필)·phase_6 (패치)·LOCK 직전 → grep으로 `[FLASHBACK|FLASH BACK|FLASH-BACK|회상`  모든 등장 위치 sweep → 출처 anchor 없으면 즉시 추가.

---

## 표기 format (3 유형)

### ① Replay — 이전 EP에서 본 장면 재방송
```
[FLASHBACK — EP01 S#3 (mirror reveal)]
```
- 시청자가 "아 그 장면" 즉시 인식
- AIGC: 같은 shot·같은 frame·같은 actor 재활용

### ② Same-EP callback — 같은 EP 안 앞부분 장면 재출현
```
[FLASHBACK — within EP05 S#2 (rooftop kiss)]
```
- 보통 한 EP 안에서 motif 강화·context shift용

### ③ Pre-series memory — 처음 보여지는 과거 backstory
```
[FLASHBACK — pre-series · Lena age 9 · ~20 yrs ago · first appearance]
```
- "first appearance" 명시 = production·시청자 "새로 찍는 shot"임을 알림
- 인물·나이·시간 거리 (years ago) 포함 → 미술·캐스팅 anchor

---

## 추가 권장 (선택)

**Length 표기:** flashback 길이가 다양하면 (motif 1-2초 vs. 완전 짧은 씬 30초) 함께 표기.
```
[FLASHBACK — EP01 S#3 · 2-sec motif]
[FLASHBACK — pre-series · Lena age 9 · ~20 yrs ago · 30-sec scene]
```

**Lens·Filter anchor:** Production note 차원에서 톤 (`desaturated`·`warm grain`·`B&W`) 명시.

---

## 금기

1. **출처 없는 [FLASHBACK] 사용 금지** — 무조건 anchor 필요
2. **[INSERT]와 혼동 X** — 사진·편지·CCTV 라이브 피드는 [INSERT]·flashback 아님. 진짜 시간 이동만 [FLASHBACK]
3. **시청자 혼란 = 매출 직격** — "이거 처음 보는 거야? 본 거야?" 0.1초 안에 안 잡히면 fail

---

## 적용 사례 (2026-05-28)

SHE STOLE MY FACE v26 → v27 — EP19 line 1928 [FLASHBACK] 블록:
- Before: `[FLASHBACK]`
- After: `[FLASHBACK — pre-series · Lena age 9 · ~20 yrs ago · first appearance]`

이 작품은 flashback 사용 minimal (1건). THE OFFERING v68 = 0건. 향후 사용 시 즉시 룰 강제.

---

## 관련 메모리

- [[no-theater-tone]] — 비선형 연출 필수 (flashback·VO·몽타주 매 EP ≥1)
- [[vertical-structure-hit-script-lesson]] — flashback = 1-2초 motif 또는 30초 완전 짧은 씬 (씬마다 5 기능 혼합 X)
- [[real-human-speech-01s-test]] — 시청자 0.1초 perception (혼란 = 결제 살해)
