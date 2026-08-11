---
name: aigc-prompt-script-writing
description: AIGC EP 대본(=AI 영상 생성 프롬프트 문서) 집필 표준 — △1컷1프롬프트·인물 1회명시+대명사·기능적 화면압력 지문·순간감정 대사·근거 있는 동작동사·깔끔 장르 씬타이틀·자연 영어. 전 작품 적용.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2232c2a-2d77-4cdb-97dc-f680b25e871b
---

# AIGC 프롬프트 대본 집필 표준 (전 작품)

**대전제:** AIGC EP 대본 = *읽는 소설*이 아니라 **AI 영상 생성 + AI 더빙용 제작 스펙**. 작가(인간 감독)가 읽을 땐 콘티처럼 텐션이 살고, `△` 한 줄을 영상 툴(Kling/Gen-3/Runway)에 복붙하면 물리 오류 없이 1컷이 뽑혀야 한다. THE OFFERING EP01 v1→v10 + 외부 AI v001→v013 상호 흡수로 수렴(2026-06-08).

## 🆕 집필 프로세스 — 5화 배치 + 읽고-쓰기 (고정·2026-06-08 사용자)
- **5화 단위로 집필.** `[1-5 집필] → (1-5 정독) → [6-10 집필] → (6-10 정독) → [11-15] → …` **EP50까지** 이 사이클 고정.
- "50화 전부 써"라는 지시여도 *한 번에 쏟지 말고* 이 5화 배치 과정으로 끝까지 간다.
- **다음 배치 쓰기 전 직전 5화 정독 필수** — 연속성·캐릭터 voice·setup→payoff·중복(반복 venue/gloat 등) 추적. (기존 "이전 EP 3개 raw 정독"의 배치판 상위 규칙.)
- **각 배치 드래프트 = 이해되는 완성형이어야 한다.** rough/난해한 초벌·"무슨 말인지 모를" 드래프트 금지. 배치라도 품질 바 유지.

## 형식
- 씬헤더 `## N-n  시간 / 안·밖 / 장소. (깔끔 장르 타이틀)` → `Characters:` 로스터 → `△` 비트 → `이름 (톤): 대사` → `On-screen text:` → `Hard Cut.`
- **△ 하나 = 1샷 = 복붙 가능한 1프롬프트.** 동작 과다(=1컷 초과) 금지. 단 *한 인물의 연결된 짧은 동작*은 한 △에 묶어도 됨(로봇 체크리스트 X).
- **🚨 내 고질(반복): 2컷을 한 △에 욱여넣고 "lean"이라 방어.** `Vael presses her to the wall. She fists his collar.` = *두 인물·두 샷* → **2개 △로 쪼개라.** AIGC는 △1개→영상1생성이라 욱여넣으면 한 클립에 두 동작=환각/품질저하. **매 △ 사이 빈 줄로 격리**(각 △ = 독립 복붙 블록). 짧게 압축한 "대본"이 아니라 *샷리스트*다. (외부 final_line_audit 169줄 > 내 클럼프 125줄 — 길어도 atomic이 정답.)
- **대본 파일 = 타이틀 + 본문만.** 메타·작업로그·버전노트·날짜·흡수내역 절대 금지(보고는 채팅으로만). [[script-file-zero-meta]]

## 대명사 (AIGC 환각 방어)
- **△마다 각 인물을 1회 명시 + 그 △ 안 재참조는 대명사.** 컷이 모델에 독립 입력돼 앞 문맥이 없으니, 한 △ 안에 antecedent가 없으면 얼굴 융합·손꼬임 환각.
- 같은 성별 2명+ 동석 = 그 성별 전부 고유명. 1남1녀면 명시 후 대명사 OK.
- ❌ 이름 도배(`Isolde lifts Isolde's eyes`·`behind Vael`) = v008 로봇병. ✅ `Isolde lifts her eyes`.

## 지문 (기능적 화면압력, 소설·로봇 양 끝 금지)
- 모든 줄 = "프레임에 뭐가 있나 / 무슨 일이 일어나나" + 카메라/조명/SFX 화면압력.
- ❌ 소설 장식("water snakes down the glass"·"hair fanned"·"knuckles white"·"forgotten cup")·내면 해설("wrong"·"she wants this")·메타("so she doesn't notice"·"audience sees"). ❌ 제네릭("his large body is above her"). ❌ 로봇 단동작 나열.
- **🆕 동작동사 = 근거(주체+경로/앵커) 필수.** 막연 비교급 금지 — `scales lift higher`(뭐보다? 떠오름?) ❌ → `scales rise along his wrist, beside her face`(몸 위 경로 + 위치 분리) ✅. *소품의 변화*와 *부위의 위치*를 한 막연 동사로 뭉치지 말 것. AI 렌더+독자 둘 다 "뭐가·어디 따라·어디 옆으로" 명확해야.

## 대사 / VO
- **순간 감정 = 그 순간 사람이 실제로 내뱉는 말.** ❌ 일기/소설 요약(`I chose him. Nobody made me.`=의미 정리문). ✅ `Don't you dare.`·`Look at me.`(지금 일어나는 일에 대한 즉발).
- **🚨 일기 검출 텔(기계적·반복 실패 차단): *관찰→반전/결심/요약* 대구 골격 = 자동 일기 = 탈락.** `X. But Y.`(`This is crazy. But I'm not stopping.`) · `I don't know X. I know Y.`(`I don't know his name. I know I don't want him to stop.`) · `I chose X. Nobody Y.`(`I chose him. Nobody made me.`) — 전부 같은 골격(자기 상황 논평+결심). **사람은 그 순간 그렇게 정돈된 관찰+결론을 안 한다.** AI가 'composed 산문'을 "괜찮음/살짝 싸구려"로 통과시키는 편향이 근원 → *내용*이 아니라 *구조(대구/반전/요약)*로 잡아라. 캐릭터 대사 느낌(raw 발화/명령/충동) O / 일기·산문 O인 척 X.
- 강한 *능동 대사* > 설명형 VO. VO는 엔진이라 **삭제 X**·단 자연·순간만(시적/대구/완성문=작가 침입). [[real-human-speech-01s-test]] [[ai-dub-tone-independent-dialogue]]
- 톤-독립 단일 의미(AI 더빙은 반어/이중의미 못 살림).

## 🆕 씬 타이틀 register
- 깔끔 + 장르 register. ❌ 임상/문서 라벨(`Actual Sex Scene` = 정본 느낌 죽임). ❌ 시적-모호. ✅ `The Heat`·`The Sex`(장소 앵커 `Bed`가 의미 고정). 타이틀은 본문보다 *톤 풍미*를 줄 순 있으나 단일 의미 유지.

## 🆕 자연 영어
- 단일 의미 native idiom. `one month away`(미래 거리·명확) ✅ / `one month off`(취소·휴무 뜻 겹침) ❌. stage-direction·on-screen-text의 캐주얼-모호 관용구 점검.

## 섹스 / 비주얼 / 미스터리
- 수위는 장르 자산(유지). 단 *무성 안무 몽타주*(=porn) 금지 — 풀 유지하되 *순간 감정 대사*를 중간에 박아 드라마로. [[t4-sex-scene-standard]]
- 남주 얼굴/몸 = 비주얼 보상(보여줘라). 관객용 미스터리는 *인물 인지(망각 주문 등)*로, 카메라로 관객에게 숨기거나 placeholder(HIM) 금지.

## 메타-교훈 (제일 중요)
**내 버전을 반사 방어하지 마라.** 차이는 *사안별 메리트*로 판단 — ①원어민 자연성 ②동작 물리 근거 ③AIGC 복붙 적합 ④장르 register. 외부/타 AI가 이 축에서 옳으면 내가 틀린 것 — 흡수하라(`one month away`를 내가 놓친 사례). 내 기본 편향 = 내 것/문학 방어. [[claude-voice-bias-vertical-failure]] [[easy-dopamine-over-logic]]
