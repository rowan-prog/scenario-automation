---
name: per-episode-runtime-gate
description: "NA paid vertical 제출 스펙 = 각 화 최소 1분. LOCK 전 전 회차 러닝타임 추정 필수. 짧은 화는 패딩 말고 응징/회수 dessert로 확장. 추정식 cuts*3.24 + 대사words*0.54 (사용자 추정 캘리브레이션)."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4aaa6296-8e27-427d-9e4e-a2b06585d6ce
---

사용자 제정(2026-06-16 · SHE STOLE MY FACE v60 LOCK 직전). **기계 게이트(한국어0·Hard Cut·END HOOK·PAYWALL·NAME·연속성)는 다 통과해도 LOCK 아님 — 플랫폼 제출 스펙 "각 화 최소 1분"을 따로 검증해야 한다.** 이번에 이 클래스를 놓쳐서 사용자가 잡음(감사 에이전트도 안 잡음 — 콘텐츠 결함이 아니라 *스펙*이라).

**LOCK 게이트에 추가:**
1. **전 회차 러닝타임 추정** = `est_sec ≈ (△컷 수)*3.24 + (대사 단어 수)*0.54`. 사용자 회차별 추정치(EP43≈72s·EP49≈37s 등)에 최소제곱 피팅한 계수. 회당 **≥60s**(여유 ≥65s 목표).
2. AIGC라 지문 한 줄이 컷 하나로 늘 수는 있지만, **컷 수 적고 대사 짧은 화는 자동생성 시 30~45s로 떨어짐** → 위험.
3. **위험 구간 = 결말 직후 후일담/응징 정리 회차**(클라이맥스 폭로 뒤 감정 정리라 일부러 짧게 치게 됨). 결말 폭로 구간 자체는 보통 충분히 김.

**짧은 화 수정법 = 패딩 금지·"응징/회수 dessert"로 확장** (사용자 핵심): 후반 짧은 화는 *장르 보상*을 넣어 늘린다 — 악역 완전 몰락 savored(맨목·"nobody's coming"·고립), 주인공 복원/환영 귀가, **초반 굴욕/대사의 역전 콜백**(예: "wake up with nothing" → 악역이 그렇게 됨; 끌려나갔던 로비 → 환영받으며 입장). 이건 vertical 관객이 *원하는* 도파민이지 억지 분량이 아니다. ([[vertical-repetition-emotional-not-procedural]] 연장 — 후일담의 "맞는 반복"=응징 만끽.)

**경계:** 구조 압축으로 화를 *분할*해 50화 맞추면(클리프행어 split) 분할된 화가 1분 미만으로 떨어질 위험 큼 → 분할 직후 러닝타임 재검 필수.

관련: [[lock-fix-volume-writing-diagnostic]] [[claude-voice-bias-vertical-failure]] [[vertical-repetition-emotional-not-procedural]] [[paywall-declaration-timing]]
