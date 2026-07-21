# 수술 계획서 v3 — 대사 직설 레지스터 전면 재작성 (2026-07-15)

## 발단
사용자 콜드리드 판정(2026-07-15): 전 대사 코퍼스 레지스터 불합격(완곡·암시·재치 대구·압축 은유·큐의존). EP1~13 LOCK 해제. 기준 = `10_writing_standard.md` §D-2-1 (이 판정으로 신설).

## 범위·순서
1. **EP1~3 교정 배치 (이 문서·집행됨):** script-surgeon(opus) 제안 39줄 심문 → 16줄 교체 + 쇼러너 부분수용 2건(#7·#34 워딩 조정) + 연속성 1건(#9 "for a year"→"for three years" — #2·#23 결혼 3년과 정렬). 제1부 훅 = 유지 라인만 인용 → 동기화 불요.
2. **사용자 콜드리드 도장** (v3 EP1~3) → 톤 확정.
3. **EP4~50 fan-out** (확정 톤·§D-2-1·병렬 opus 배치) — 도장 전 착수 금지.
4. **KR 참고본 동기화** — 전 회차 완료 후 일괄(중간 동기화 = 재작업).

## 보존
전개·비트·씬·△·[END HOOK]·Hard Cut·화자 태그 전부 불변. 대사 텍스트+톤 큐만. 수위 = 상향만 허용.

## 버전
`FINAL_v3.md` 분기 (v2 불변). 적용 = python exact-match·건수 검증.

## 게이트
구패턴 잔존 grep 0 · EP/END HOOK/Hard Cut 카운트 불변 · esl_hardwords 비퇴행 · 교체 18건 = 18건 검증.

## 확정 바닥 레지스터 (사용자 2026-07-15)
= **천박 슬랭.** 빌런/이브 = crude 직설(`Get me my wife on tape, screwing another woman.`), 클레어 = 순진-강단 유지. 전 라인 = 나열 0·은유 0·짧은 SVO·쉬운 단어·행위 한 번만 평문. 앵커 = `claude_localiation/projects/the-offering-the-dragon-lord`·`find-the-crown` 완성 대사본.

## v3 1차(에피그램) 폐기 → 바닥 재작성
1차 script-surgeon 16건 = 사용자 재기각(`kissing her, touching her, fucking her` 나열=tricolon tic·`furniture` 은유·`I don't bite` 관용구·무거운 구문 ESL 실패). 표준 §D-2-1 예문 자체가 병이었음 → 수정. EP1~3 = 메인 직접 바닥 재작성 9건 적용(오프너 = 사용자 선택 verbatim + 녹취 콜백 2 동기화).

## 미해결 안건 (fan-out 시)
- **`furniture` 모티프 체인 4건**(EP-후반 L1031/1836/2254/2360 = 리처드 라벨 → 클레어 되치기 "the furniture held the deed"). 라벨 되치기 자산이나 사용자가 단어 기각 → **전 체인 교체 라벨 선정 필요**(fan-out 때 사용자 확인).

## 소스 V2 재앵커 (2026-07-15)
원작 소스 리빌드본(`_source_v2_frame_accurate/` R01 46초) 등재. 사용자 지시 = 참조해 각색 완성·러프 결함(19초 무드컷) 비계승·대사없는 구간 ≤5초·무드로 끌지 마라. **오프닝을 소스식 콜드오픈으로 재앵커**(사용자 승인): EP1 = 유혹 콜드오픈(S#1)→굴욕(S#2)→함정 리빌+훅(S#3). 소스 대사 척추 GL 계승(`I'm married`/`Doesn't that make it more fun?`/`Do you know who my husband is?`). 엔진 보존(정보 비대칭 = 모니터 인터컷·이브 언더커버·클레어 함정 모름). EP1 훅 라인 원본 유지(제1부 요약 정합).

## △ 규율 (사용자 교정)
△ = one-shot(1컷)·롱테이크면 공간 넘어도 1컷. 못 찍는 내면서술 외화: `before she catches herself`(×2)·`instead of pulling free`·`instead of sending`·`neither closing the gap`·`smile falters then smooths`·`into the touch` = 전부 보이는 동작으로. voice_lint 미검출 = 룰/린트 보강 안건.

## 타격감 기준 (사용자 격노 교정)
모욕/대사 판정 = F-2-2 타격감("실제 인간이 아프냐·시청자가 움찔하냐"), 미감/단어 아님. furniture = "가구? 어쩌라고" = 안 꽂힘 → 전 체인 교체(구체·개인·상황). [[dialogue-direct-register-wit-ration]].

## AI 완결·축자 편향 (2026-07-15 사용자 — Find My Crown 이중역 실측)
전문번역가·원어민 = 더 완전·축자·설명적 DOCX판 버리고 더 벼려진 Pasted판 선호. AI는 반대 = 내 완결/축자/설명 선호가 오답 신호. 교정 = 설명골조 삭제·급소어 문두·최상급/개인/즉물·화자레지스터 보존·화행하되 서술마라·긍정직결·파편. 본문 = §D-2-2. [[dialogue-direct-register-wit-ration]].

## 상태
- [x] 확정 바닥 레지스터 + 소스 V2 등재 + △ 규율 + 타격감 기준 + AI완결편향 렌즈(§D-2-2)
- [x] **무료런 EP1~8 디벨롭 완료** → v3:
  - EP1~3 = 소스 콜드오픈 재구성(유혹→굴욕→함정리빌+훅)·△ 외화·타격감·바닥 재작성
  - EP4~8 = de-tic(`No camera reaches`·`mouth says/hands`·`Only me`·`first person` 토씨중복·성애씬 △런)·△ 외화(jaw)·구체화
  - crisp-up(§D-2-2): 설명골조/헤지/대구 제거(EP1 리처드·EP7 클레어·EP8 페이월 훅)
  - 게이트: 무료런 tic 0·△ 내면서술 0·EP130/훅49/하드컷49 불변·esl 85.2%
- [x] **무료런 KR 참고본** → `07_final/12_hired_to_ruin_me_FINAL_v3_KR_ep1-8.md` (자연스러운 구어·직역X·씬23/하드컷8/엔드훅8·영어누출0). 기존 v2 KR은 옛 내용(furniture·리처드 서재 오프닝)이라 무료런은 이 v3 KR이 정본.
- [ ] **사용자 무료런(EP1~8) 콜드리드 도장** ← 현재
- [ ] EP9~50 fan-out (§D-2-2 렌즈+furniture 라벨 교체+잔여 jaw tic L975/L2100+소스 라운드 반영)
- [ ] KR 동기화 (EP9~50 = fan-out 후 일괄)
