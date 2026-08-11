---
name: voice-lint-gate-pass
description: 문학톤 기계 탐지 도구(voice_lint.py) + 대사/VO 북미 구어 게이트 패스 워크플로우 (2026-05-29 사용자 명시)
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2d145cfe-e9c6-438b-bd5e-5d876492e4d8
---

규칙을 아무리 가르쳐도 모델은 집필 중 문학톤으로 샌다. 그 글을 같은 모델이 검수하면 못 잡는다(자기 목소리라 안 이상함). 비싼 짓(에이전트 패널·멀티패스 재집필·페르소나 검토·대형 리포트)은 퀄을 안 사준다 = "오래 한 거나 빨리 한 거나 차이 없음". **해결 = 기계로 싸게 1차 거름 + 사람이 짚으면 즉시 한 줄 수술.**

**도구:** `tools/voice_lint.py` (LLM 0·0.5초). 매 FINAL LOCK·phase_4·6 직전 강제 실행:
`python tools/voice_lint.py <file> [--ep 9-50] [--full] [--cat ANAPHORA,METAPHOR]`
탐지: ANAPHORA(토막 나열 `X. Y. Z.`·dialogue/VO만 HIGH·stage-direction 비주얼 반복은 제외)·METAPHOR(은유로 사건 때우기 `wear like a costume`)·NEG_PIVOT·EM_DASH(≥2/line)·TRICOLON·BRITISH·BREATH·KOREAN. 트리거 명령 `보이스린트 [작품] [v]`.

**수술 우선순위 P0:** ①토막 나열 제거(`My face. My home.`→한 문장) ②은유 제거 ③**번역투→북미 실제 구어**(한국어식 추상명사 직역 금지·`my life/my name/my mother` 반복 감정문 줄이기·`She married my life`→`She married Ethan in my name`·쉬운 동사 take/wear/sleep/lie/call/kick out/film/cry). 기준 = "멋있는 영어"가 아니라 **북미 여자가 분노해서 실제로 뱉을 짧고 쉽고 구체적인 영어**.

**연극톤 자동폐기(추가):** 캐릭터 펀치 3연(`She doesn't need X / Y / Z`)·prosecutor식 죄목 나열·prepared cool line·tiki-taka 핑퐁·관객 향한 방백·writerly 복수 선언. **단 예외=diegetic:** villain이 TV 카메라 앞에서 *연기하는* anaphora·무덤 앞 감정 반복(`It's me, Mom. It's really me.`)·패닉 절규 run-on은 정상(진짜 그 상황의 진짜 사람).

**원칙:** 구조 LOCK ≠ 대사 LOCK. 구조 통과본도 대사·VO 게이트 패스 별도 전수 필요(안 하면 90점대 못 감). 재집필·리포트·멀티에이전트 X·Edit 직접 수술만. SHE STOLE v31→v32 학습(ANAPHORA 14→7→3·METAPHOR 18→1). Link [[no-theater-tone]] [[real-human-speech-01s-test]] [[token-diet-70-percent]] [[vertical-structure-hit-script-lesson]] [[bulk-script-verify-strict]].
