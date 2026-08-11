---
name: pitch-pass-fail-inference
description: 11개 피칭덱 (10 통과 + 1 비통과) 비교 분석 — 통과작 공통 패턴 vs 비통과작 함정. phase_2 피칭덱 작성 시 자가 검수 baseline.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2d65e927-1cd5-4df0-bd23-1493c3adfb18
---

> **사용자 직접 제공 (2026-05-19).** 통과 10개 + 비통과 1개 = 직접 비교 가능한 매우 드문 학습 데이터.
> 비통과작 = US/AI *Sealed Bride: First Seal* (Han Choi). 같은 CM이 통과시킨 *Beast Lord's Rejected Bride*와 차이 분석으로 인사이트 추출.

## 룰

**phase_2 피칭덱 작성·검토 시:** `config/pitch_references/INDEX.md` 자동 참조 + 본 메모리의 8 통과 패턴 + 7 회피 항목 자가 검수 강제.

**Why:** 사용자가 "AI는 허구한날 피칭덱이 떨어지는데, 사용자 작성 11개 중 10개 통과" 명시. 통과작과 비통과작의 차이 패턴을 학습하지 않으면 동일 함정 반복.

**How to apply:** 피칭덱 1차 안 작성 직후 + 사용자 검토 전, 본 8 통과 패턴과 7 회피 항목으로 자가 점검. 어긋난 부분 사전 정정.

---

## 1. 통과작 공통 패턴 (10개)

### P1. 검증된 IP·플랫폼 성과 수치를 피칭사유에 명시
- 01 Lost Boy: Netshort *The wolfless carpenter rules the world* 등 4 레퍼런스
- 03 Vampire Brother: ReelShort *My Secret Lover is His Brother* + *Vampire Prince's Bride 73.4M / Kissed by Claw and Fang 78.0M*
- 04 Sister Picked Male Lead: 원작 웹툰 **1,854만 / 웹소설 2,270만 / 평점 9.9**
- 05 Villain Daughter-In-Law: 원작 웹툰 **480만 / 웹소설 1800만 / 평점 9.9**
- 06 Dear Nemesis: 원작 **35.2M view**
- 07 Teach Me Desire: 원작 **10.6M view**
- 08 Beast Lord: *Claimed by Alpha I Hate* **125M+ 뷰** + 표 형식 비교
- 10 White Wolf Queen: RS *Rejected Luna* / DB *Watch Out, I'm The Lady Boss* / 중국 *용감한 배신*

→ **숫자 없는 "비슷한 작품" 언급 X / 검증 작품 + 정량 성과 동반.**

### P2. AI 변별력을 구체 비주얼 요소로 명시
- 01 Lost Boy: 마법·군대·전쟁·크리처
- 03 Vampire Brother: 고딕 성·혈월
- 08 Beast Lord: 늑대 변신(full shift, half shift) / Blood Moon / Mate Mark VFX / 흡혈귀 송곳니·발톱 / Feral wolf 상태 / 중세 황무지 / 명명일 무도회

→ **"AI 강점" 추상 언급 X / 일반 실사로 못 만드는 구체 비주얼 1-7개 나열.**

### P3. 시대극·판타지 변환 (현대 검증 IP의 AIGC 강화)
- 03 Vampire Brother: My Secret Lover is His Brother (현대 상류층) → 뱀파이어 귀족 사회
- 08 Beast Lord: Claimed by Alpha I Hate (현대 고등학교) → 중세 무어랜드 왕국 + 일곱 늑대 귀족 가문
- 05 Villain Daughter-In-Law: 천재 아기 (한국 시장 검증) → 중세 판타지 회귀

→ **현대 배경 검증 IP를 AIGC 강점 살리는 판타지 시대극으로 변환 = 시청자 익숙함 + AI 신선함 동시 확보.**

### P4. 1화 강한 후킹 + EP1-2 즉시 굴욕·각성·이해 가능
- 01 Lost Boy: 1화 즉시 마법 평가 실패·꼴찌·웃음거리 (장르 약속 즉시)
- 08 Beast Lord: EP1 즉시 공개 굴욕·진흙·약혼자 배신 시작 (1초 감정 이입)
- 10 White Wolf Queen: EP1 즉시 남편 배신 + "더 이상 숨지 않겠다"
- 11 Fight for Love: EP1 즉시 비밀 연인 + 챔피언 도전 + 빌런 등장

→ **EP1에 mythology 설명·계보·세계관 설치 0건. 즉시 굴욕·각성·이해 가능한 상황.**

### P5. 정보량 절제 (EP1-7 1-2개 새 정보)
- 04 Sister Picked Male Lead: 16살 빙의 + 낮밤 인격 분리 = 2개 (다른 모든 mythology는 후행)
- 05 Villain Daughter-In-Law: 회귀 + 보석 페어리 = 2개
- 08 Beast Lord: 늑대 사회 + Rejected Mate = 2개 (Hybrid·Vampire 봉인은 6화 이후 점진 공개)

→ **회차당 mythology 1개 / 7화까지 누적 2-3개 한도.**

### P6. 페이월 = 구체 행동 직전 컷
- 03 Vampire Brother EP11 (페이월): 두 형제 송곳니가 양쪽 목덜미에 닿기 직전 암전
- 08 Beast Lord EP9 (페이월 #1): "내 짝(Mate)" 선언 직전 컷
- 10 White Wolf Queen EP9: White Wolf 각성 직후 (다음 미카 처벌 예측)
- 11 Fight for Love EP6 가능 페이월: "넌 이미 내게 죽은 사람이야" → 재회 진전 예측

→ **"무슨 일이 일어날지 명확한" 행동 직전 컷. 사건이 이미 진행 중인 페이월 X.**

### P7. 여주 능동성 + 남주 욕망 매력 분리
- 05 Villain Daughter-In-Law: 회귀 후 적극적으로 베르슈타인 가문 도피처 선택·경매 능력 사용
- 08 Beast Lord: 짝 거절 후 6달 도망 + 활 훈련 + 능동 복귀
- 10 White Wolf Queen: "더 이상 숨지 않겠다" 명확 will + Lycan King 동맹 선택
- 06 Dear Nemesis: "감당할 능력도 없는데 바라기만 하는 건 욕심이다 / 네, 알아요. 저 욕심부리고 있는 거예요"

→ **여주 = 끌려다님 X. 자기 욕망·선택 명확. 남주 = 분리된 매력 (위험·아름다움·권력) 명시.**

### P8. 트리트먼트 대사 = 행동 생성형
- 01 Lost Boy: "그 낙인을 가진 자를 30년 만에 보는구나" + "다음 주 탈락 심사에서 네 이름을 올리겠다"
- 03 Vampire Brother: "난 절대 너를 선택하지 않아. 너도 나를 선택하지 마라" + "형을 선택하고 빨리 사라져"
- 08 Beast Lord: "Touch her again, and I'll break it" / "내 짝(Mate)" / "I reject you as my mate"
- 10 White Wolf Queen: "당신은 이딴 곳에 묻힐 존재가 아니다" / "내 파트너가 되어. 당신을 버린 놈이 뭘 잃었는지 직접 보여주자"

→ **시적·문어체·연극톤 0건. 모든 대사가 다음 행동·관계 변화·압력 생성.**

---

## 2. 비통과작 함정 (Sealed Bride 분석)

### F1. 정보량 폭격 (가장 큰 원인)
EP1-7에 이해해야 할 mythology:
- 일곱 봉인 / 1024년 중세 성 / 1547년 베니스 / 1820년 빈 / 1923년 파리 (다중 전생)
- 천사장 / 타락천사 / 6쌍 vs 4쌍 날개 / 666 표식 / Eliana 전생
- The Beast (Ashley) / The Dragon (친아버지) / 휴거 / 황금 갑옷
- = 매 화 새로운 mythology 설정 폭격

→ **EP1-7에서 시청자가 학습해야 할 정보 1-2개로 줄였어야.**

### F2. 종교 IP 직접 차용
- 666·휴거·일곱 봉인 = 성경 요한계시록 직접 차용
- Twilight·Lucifer는 종교 톤 회피로 성공. 이 작품은 직접 차용
- "Universal IP, 성경 요한계시록 기반" 명시 = 북미 시청자 거부감 위험

→ **종교 모티프는 mythology 톤으로 변환하되 직접 어휘는 회피.**

### F3. 시장성 근거 잘못 매핑
- 시장성 근거가 "Bible Influencer AI"·"The Chosen"·"Angel Studios"
- 이건 종교 시청자 시장. paid vertical supernatural romance 시청자와 다름
- Twilight·Lucifer 팬덤 = 종교 회피 톤. 이 작품은 정반대

→ **시장성 = 같은 카테고리·같은 톤의 paid vertical 검증 IP만.**

### F4. 트리트먼트 시적·문어체·연극톤 누적
- "Hello, my bride. Did you miss me?"
- "A thousand years he's been hiding you from me"
- "I've died for you eleven times in eleven lifetimes"
- "Find me again in a thousand years"

→ **AI 집필 가이드 2.2 위반. 행동을 만들지 않는 명문장. 캐릭터 voice 부재. 작가 자아실현 톤.**

### F5. 페이월 = 사건 진행 중 (예측 약함)
- EP7 페이월: "둘이 함께 추락하기 시작한다" = 이미 일어난 사건
- 다음 화에 보고 싶은 구체 행동 없음

→ **"무슨 일이 일어날지" 명확한 행동 직전 컷이어야.**

### F6. 여주 능동성 부재
- "평범한 카페 알바생" → 7화 내내 두 남자 사이에서 끌려다님
- 자기 욕망·선택·will 부재
- 비교: Beast Lord 세라피나 = 짝 거절 후 6달 도망 + 능동 복귀

→ **여주 = will 명시 필수. 끌려다님 X.**

### F7. 9:16 세로형 부적합 스케일
- "도시 전체 정전" / "휴거 도시 와이드샷" / "50km 재화" / "별이 되어 사라짐"
- paid vertical = 친근한 감정 거래·접촉·공개 장면 보상
- 우주적 스케일 = 시청자 감정 이입 어려움

→ **세로형 화면에서 친근하게 보일 스케일 우선. 우주·도시 와이드샷은 1-2 비트.**

---

## 3. 자가 검수 8 질문 (피칭덱 작성 직후 강제)

1. **검증 IP·플랫폼 성과 수치 동반?** (예: "RS 누적 X뷰", "원작 웹툰 Y만 / 평점 Z")
2. **AI 변별력 = 일반 실사 못 만드는 구체 비주얼 1-7개 나열?**
3. **EP1-7에 새로 이해해야 할 mythology 1-3개 한도?**
4. **EP1에 mythology 설명 0건 + 즉시 굴욕·각성·이해 상황?**
5. **페이월 = "무슨 일 일어날지" 명확한 행동 직전 컷?**
6. **여주 will·욕망·선택 명확 (끌려다님 X)?**
7. **모든 트리트먼트 대사 = 행동 생성형 (시적·연극톤 0건)?**
8. **시장성 근거 = 같은 카테고리·같은 톤 paid vertical만 (다른 시장 매핑 X)?**

→ 1개라도 NO = 재작성.

---

## 4. 동일 CM 비교 (가장 강력한 인사이트)

같은 CM Han Choi:
- ✅ Beast Lord's Rejected Bride (Werewolf Romance 시대극) — 통과
- ❌ Sealed Bride: First Seal (Supernatural Romance 종말론) — 실패

→ CM 역량 문제 X / **작품 설계 자체 문제.** 8 통과 패턴과 7 함정의 차이가 통과/실패를 결정.

상세 인사이트는 `config/pitch_references/09_sealed_bride_first_seal_US_FAIL.md` 끝 "비통과 추정 원인" 섹션 참조.

관련: [[pitch-master]] / [[banned-expressions]] / [[directness-master]] / [[paid-vertical-master]]
