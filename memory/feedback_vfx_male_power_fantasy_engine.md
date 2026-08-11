---
name: vfx-male-power-fantasy-engine
description: VFX 남성향 파워판타지(신화·이세계 액션) 집필+검토 엔진 — 분량기준 정정·combat-read 데코보코·god-reveal·지문 경제·결제 배치. TITAN BORN(외부 Codex) v138→v148 5라운드 검토 학습.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 36a0c44d-d6c5-4478-aedf-6a8829c892b1
---

워크스페이스 첫 남성향 작품(TITAN BORN: 노예가 된 제우스의 아들·매 EP VFX spectacle·여신 4인 합류) 외부 검토 5라운드에서 추출. **여성향 dark romance / impostor 복수물 baseline과 엔진이 다름** — 남성향·VFX·액션 작품 진입 시 이 파일을 [[vertical-revenge-impostor-believed-engine]] 대신/병행 로드.

## 0. 🚨 분량·지문 기준 정정 (사용자가 직접 교정·가장 중요)

**`50화 ~70-80k자` 기준을 VFX 액션 대본에 raw char count로 적용하지 마라 = 카테고리 오류.**
- 그 기준은 **대사 주도 한국 여성향 vertical 히트작**(추락한 K-pop 등)에서 나온 *드라마 분량* 기준. 측정 대상 = 대사 + 핵심 동작.
- VFX 남성향 대본은 [KEY CAMERA] 샷리스트 + [VISUAL/ACTION] VFX 콘티 = **제작 스펙이 분량의 절반**. 이건 시청자가 보는/듣는 드라마가 아니라 **런타임 0초인 지시문**.
- 화면 런타임은 대사+액션 비트가 정함, **KEY CAMERA 불릿 개수가 아님.** 147k자라도 대사가 짧고 즉발적이면 화수 길이는 vertical에 맞음.
- **"강한 지문은 VFX 남성향에 필수"**(사용자 명시). 글자수로 깎으라는 건 자기모순.
- **개선 비트(god-reveal·凸·전술 VO) 추가로 분량 증가 = 부채 아님 = 대본이 좋아진 것.** "매 버전 +되니 감산 필요" 프레이밍 금지.

**Why:** 기준을 기계적으로 숫자에 갖다 대면 장르·포맷이 다른 작업을 오판함. 메트릭이 *같은 것을 재는지* 먼저 물어라.
**How to apply:** VFX/액션 대본 분량 지적 전 자문 — "이 글자수가 화면 런타임을 늘리나, 아니면 지시문이 부풀린 건가?" 후자면 분량 지적 자체를 폐기. 유일한 정당한 좁은 질문 = *한 샷에 동시 물리 이벤트 5-7개가 AIGC에서 뭉개지나*(분량 X·샷 명료성 O). 파이프라인이 소화하면 그냥 둔다.

## 1. Combat-read 데코보코 (남성향 핵심 엔진)

주인공은 **안 지지만, 경합·힘겨루기조차 없으면 안 됨.** 중간보스가 한방에 나가떨어지면 장르가 죽음.
- **모든 신/보스가 원샷 금지.** 최소 1-2 보스(특히 최강 가문)는 *한 번 붙잡고/휘청시키고/진짜 후퇴 강요* 후 쓰러져야. 3비트 凸 모델: 1타 실패("The palm does not break")→붙잡혀 으스러짐→2타 균열→3타 관통.
- 저항이 **물량/소모전(군대·재열상)에만** 쏠리면 안 됨 — *힘을 맞받는* 비트(적이 Kael만큼 세게 침)도 필요. 안 그러면 "신을 꺾었다" 체감 0.
- **down-beat 클리프행어**(진짜 "졌나?") 1-2개로 스테이크 리셋. (TITAN: EP49 whiteout "White thunder swallows Kael whole.")
- **boss-read 전술 VO** = 각 보스 공략 로직을 짧게 가독화("He pulls when I resist. So I stop resisting"·"The throne feeds him. Hit both"). 시적 X·정보형 O. [[real-human-speech-01s-test]] VO룰 준수.
- 최종 킬은 기계적 X — **감정 스파이크(모친/이름) + 주제 이미지(노예흉터 발화) 위에** 얹어라.

## 1.5 🚨 마크/트라우마-심볼 = 무기·마법시스템 아님 (12라운드 검토에서 놓친 핵심·자기교정)

알파메일 물리 카타르시스 = **"네가 찍은 노예 낙인 따위, 내 주먹 앞엔 의미 없다."** 그런데 그 노예 낙인이 후반으로 갈수록 *빔 쏘는 무기·버프/디버프·"누가 누구 마크를 덮어씌우나" 주술전*으로 변질되면 = **두통·쾌감 사망.**
- **마크/흉터 = 상징·증거·분노스위치 + 흑금 발광 VFX**(크레이토스 문신·둠 표식). **무기 X.**
- **전투 주체 = 주먹/힘/불.** 마크가 `fires a beam / cuts / tears through` 하면 안 됨 → **Kael의 주먹이** 부순다. 마크는 *달아오를(glow/burn)* 뿐. (= rename이 아니라 *주체 재귀속*이 진짜 작업.)
- **용어 1개로 통일(slave mark).** brand/seal/divine scar/dead brand로 쪼개지 마라. `slave mark→divine scar` 개명도 금지(power-up 획득처럼 읽힘) — 계속 slave mark로 두고 빛만. 적 무기도 "brand" X → `lightning chain / lightning spear`(물리어).
- 관객이 따라갈 건 마크 시스템 X → **"Zeus가 아들 안 죽이고 노예화 → Eryx 실행 → Kael이 힘으로 갚음"** 한 줄.
- **🚨 자기교정:** §1의 "보스전을 *가독적·전술적*으로"(boss-read VO)가 오히려 *마법 퍼즐 전투*로 밀 수 있음 — **가독성 ≠ 물리성.** 색문법 추적가능 ≠ 기믹 아님. **전투는 diff가 아니라 통째로** "물리→마법 드리프트" 점검. (TITAN v152: divine scar가 빔 쏘고 dead-brand 덮어씌우기를 12라운드 검토 내내 놓침 — 오히려 凸 개선이라 칭찬했음.)

## 2. 신/보스 비주얼 = 풀 god-reveal 머니샷 (VFX 핵심)

- 각 신은 **물리 본체 + 차원 스케일**의 awe-reveal 1컷을 가져야. "실루엣/보이스"만으로 때우면 그 신과 *싸운다* 체감 안 남. (TITAN 초기 실패: Hera·Aphrodite가 실루엣뿐 → 풀 god-form으로 교정: "vast, crowned, white-gold hair…beautiful enough to make the gate go still" / "larger than the shrine, mirrors blooming like wings".)
- 색문법 일관 = 강점(주인공/각 가문 고유색). 유지하라.

## 3. 지문 = "대본"이지 콘티+프롬프트+작가해설 아님

- **촬영 불가한 내부의도/의미주석 금지**(AIGC 렌더 불가): "respect enters underneath it"·"first time he protected her in public"·"Zeus wants witnesses when Kael breaks" → 가시 행동으로 외화 or 삭제.
- **샷당 지배 동작 1 + 반응 1.** 동시 물리 7개 stack = 생성기 mush + 머니샷 매장.
- 단 **지문 강도 자체는 유지**(VFX 장르). 트림 ≠ 약화.
- [VISUAL/ACTION]과 [KEY CAMERA] 중복은 *명료성* 관점에서만 보고, 분량 관점으론 보지 마라(0번 항목).

## 4. 결제 구조 배치 (paid vertical)

- **빌런 처단을 paywall 직후로 hold** = 결제 즉시 보상(TITAN: EP8 Deimos 격파→EP9 처형). 우수 설계.
- **첫 유료 구간(paywall 직후)에 최반복 arc 두지 마라** — 신규 결제자 이탈 지점. (TITAN 약점: EP10-14 볼트 5화 반복이 첫 유료 구간.)
- **최고 자산(god-reveal·실체 보스전)을 paywall 한참 뒤에 묻지 마라.** 전환·초반 유지에 당겨라.
- 결제 임계 화수별 훅 강도 + 그 사이 유지력을 따로 점검(EP8 전환 / EP9-12 유지 / EP13 추가전환 / EP14 만족).

## 5. 첫컷 15초 락인 타이밍

- 파워-reveal "WHOA" 머니샷은 **첫 ~10초 안에** 떠야(모바일 썸스톱). 논리 수정이 머니샷을 밀면(예: 칼 "이미 낙하"→"걸려있다 떨어짐") 창 가장자리로 감 — *논리 vs 즉시성* 트레이드오프 주시. 밀리면 1초 flash-forward 1컷 고려.

## 6. 타이틀=엔진=결말 1단어 루프 + 박탈 미러 회수 (2026-06-12 — LOCKED OUT 57화 reference 실증)

- **타이틀 동사 = 쾌감 엔진 = 결말을 한 단어가 짊어진다.** LOCKED OUT: EP1 빌런이 "Locked out of your own grave" 선언(제목을 악역 입으로) → 매 화 하나씩 탈환 → EP56 주인공이 가해자에게 "Locked out." 되돌려줌. 남성향 청사진 진입 시 검토 항목: *제목이 동사형 엔진인가, 그게 1화에 선언되고 결말에 회수되는가.* (여성판 = SHE STOLE의 stole→stolen back과 동형.)
- **박탈 humiliation = 결말에서 동일 앵글(MATCHING ANGLE)로 물리 회수.** EP1 진흙에 처박힌 그 자세·그 자리 그대로 EP56에 가해자를 처박음. "처음 당한 그 자리/그 자세 그대로 되갚기" = paid 남성향 최강 체감 승리. (SHE STOLE v53도 동일 채택: 마라를 레나가 끌려나간 그 오버플로 게이트로 퇴장.)
- **🚨 회수 목표 소진 타이밍 가드레일 (LOCKED OUT 최대 결함):** 핵심 회수 목표(코어 3종)를 EP13에 다 소진 → 남은 ~22화가 "길 막힘→뚫음" 변별 약한 반복 = 후반 동력 공백·페이월 후반 이탈. **코어 목표 소진 = 전체의 80% 이후로 배치.** 중반에 비우면 "새 규칙이 아니라 새 장소일 뿐" 피로가 옴.
- **사이다 형태 3종 고착 경고:** "적 비웃음→한 방→smile dying" 패턴이 7+회 동형이면 30화 후 결과를 미리 앎 = 손맛 마모. 보상 형태도 데코보코(§1) 필요 — 즉살/굴종/힘겨루기 변주.

---

연결: [[easy-dopamine-over-logic]](쉬운 도파민·논리는 한 줄) · [[no-theater-tone]](연극톤 금지) · [[bulk-script-verify-strict]](일괄 개명 후 speaker-label/헤더 ALL CAPS 규약 grep 검증) · 프리미스 재설정 시 = 해당 스레드 전 씬 전파(TITAN: Hades 적→조력 재설정에 EP22 미동기화 모순 발생).
