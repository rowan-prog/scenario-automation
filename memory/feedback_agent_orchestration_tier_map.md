---
name: agent-orchestration-tier-map
description: "에이전트 오케스트레이션 원칙 — 모델 티어는 '중요도' 아닌 '업무 성격'이 정한다·naive-proxy는 작은 모델이 더 정확·AIGC 생성기 프록시 상설·직교 병렬 sweep·집필 write-time 지원 3종. 룰 본문 = workspace 2문서."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 036bc9d4-42bb-43b9-a9b2-cb938e41066a
---

2026-07-02 사용자 지시(에이전트 전개 필요·토큰효율·단일패스 누락·모델별 적합업무·독립 2에이전트 다시각)로 오케스트레이션 재설계. **룰 본문은 workspace에 산다** — `config/20_review_standard.md` §7(3-tier 맵·직교 sweep·토큰회계) + `config/10_writing_standard.md` §A-1(집필지원 W1-W3). 이 메모리 = 배경·원칙 요약.

**대원칙: 티어는 '중요도'가 아니라 '업무 성격'이 정한다.**
- **OPUS** = 단발 정밀도가 품질을 좌우하는 *발견/하드블록/판정* (fresh-eyes 발견·native 정밀귀·external 막장필터·evaluator).
- **SONNET** = 반복 수렴(노이즈 흡수) + 중난도 추출/합성 (cold-read×3·페르소나 패널·크래프트 추출·아크 옵션 패널·통합).
- **HAIKU** 🆕 = 기계 + **naive-proxy**. 핵심 통찰: **뇌오프 시청자·flat-TTS 낭독기·무맥락 이미지 생성기는 작은 모델이 *더 정확한 계측기*다** — 이 역할은 "덜 이해하는 것"이 본질이고, 똑똑한 모델은 "네가 의도한 걸 알아채 줘서" 실제 소비자가 안 해주는 보정을 해버림 = 프록시 오염. 똑똑함이 여기선 버그.
- **MAIN(Fable) = 아키텍트 (2026-07-03 사용자 재정의 — 구 "집필=메인 직접" 룰 폐기):** 구조·규칙·워크플로우 설계 + 역할/모델 분배 + 최종 판정(머지·진성 선별·LOCK)만. **프로스 실무 직접 수행 금지**("아키텍트가 벽돌 나르지 마라"). 집필·수술 실무 = opus — 단 지시서에 논문병 가드레일(감정 중심 명시·히트작 raw/hit_dna 앵커·원작 직역 대비·정리병 금지) 의무 동봉, 산출은 쇼러너 판정 후 채택.
- 발견(discovery) 역할엔 haiku/sonnet 금지(naive-proxy는 단일 클래스 신고지 발견 아님). 비용 감각(메인 Fable): opus 38%·sonnet 23%·haiku ~7%.

**Why:** 영상=AIGC·음성=AIGC·인간=기초편집뿐이라, 생성기(TTS/이미지툴)와 뇌오프 모바일 시청자를 *그 관점 그대로* 흉내 내는 프록시가 검수의 핵심인데 그걸 큰 모델로 돌리면 오염되고 비싸다. 또 "히트작 쓰기가 약하다"의 진짜 병목 = 집필이 메인 단독이라 write-time 레버리지 0이었던 것.

**How to apply:**
- 신규 에이전트 2종(전부 haiku·보고전용): **aigc-draw-auditor**(무맥락 △ 단독 drawability — 상태태그 누락·대명사·2동작·추상) + **tts-literal-ear**(무톤 대사 낭독 — 톤/반어 의존 신고). 이중 귀 = 정밀귀(native-ear opus) + 리터럴귀(tts-literal-ear haiku).
- **단일패스 누락 = 재라운드 금지(asymptotic) → 직교 병렬 sweep**: 각 렌즈가 서로 블라인드로 *다른 오류 클래스만* 사냥(겹침0 = 토큰당 캐치 최대). belt는 호출수 아닌 tier-weighted 비용으로 잰다(≈1.8 Fable-pass).
- **다시각 = 독립 N개 × *다른 프레이밍*** (같은 프롬프트 재실행 아님): 이중 귀·아크 옵션 패널(연료축별)·cold-read(페르소나별).
- **집필지원 3종(프로스는 위임 0)**: W1 크래프트-차지 프리브리프(sonnet 추출) / W2 아크-비트 옵션 패널(sonnet ×2-3 독립) / W3 인라인 히트게이트(haiku 뇌오프·5화 배치마다 — LOCK 전에 히트약점 조기 포착).
- Agent 호출 시 `model` 파라미터 항상 명시.

검증 참고작(둘 다 글로벌 AIGC 히트) = `Bussy and the Beast`(다중상태 태그·SFX대문자·TTS안전 실증) + `약자의 가면 강자의 힘`(안믿기는 주인공·경멸라벨어 합창·제3자 사이다 실증). 히트-크래프트 룰은 10_writing §B/§D-0-1/§D-5-1에 편입.

관련: [[token-diet-70-percent]] [[agent-roster-orchestration]] [[claude-voice-bias-vertical-failure]] [[vertical-revenge-impostor-believed-engine]] [[lock-class-sweep-not-oneoff]]
