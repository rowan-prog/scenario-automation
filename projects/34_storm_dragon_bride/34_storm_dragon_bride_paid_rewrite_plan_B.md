# B안 계획 — 9~53화 "원작 영어와 글자 그대로 같은 대사"만 살짝 (2026-09-22 · v32 기준 · 승인 대기 · 대본 미수정)

## 목표
유료 9~53화에서 원작 영어와 글자까지 같은 대사를 0으로. 뼈대·비유·비트·톤은 그대로 두고 **어순·어휘·문장 나누기 수준**만 바꾼다. 1~8화(계획 G)처럼 공격 각도를 바꾸는 작업이 아니다.

## 대상 (기계 집계 · 목록 = `34_storm_dragon_bride_paid_identical_list.md`)
- 9~53화 대사 397줄 중 원작 영어와 유사도 0.85 이상 = **220줄**
- 제외 ① 보호선 10줄(시그니처·회수선 verbatim 쌍) ② 3단어 이하 기능어 53줄("Stop." "My Lord." "Ophelia!" 류 — 바꾸면 억지)
- **실제 작업 = 157줄** · 화당 1~7줄(평균 3.5)

## 보호선 (절대 불변)
30화 `It won't hurt anymore. I'm carrying it now.` · 36화 `Kneel? Fine. But I won't forget a single face.` · 21화 `If you want revenge, then use me...` / `Just stay by my side. Forever.` · 35화 `Are you insane?! You bound your own life to the poison that's killing me...` · 39화 `So what? It was my choice!` · 42화 치유의 샘 전 구간(`I'm about to snap` · `I love you, Ophelia.` / `Say it again. In my ear this time.`) · 45화 고백 3연 + `I promised I'd protect you.` · 49화 `Stop dying for me, Dorian. Live with me instead!` / `Blood is the only way this ends!` / `That's your law. Not ours.` · 52화 `Then I'll love a dragon.` · 53화 `This time, together.` · 골든 아일스 약속 3회(27·48·50화) + 53화 회수 · 회수선 verbatim 쌍(35↔37화 `As long as you're still breathing…` · 43↔48화 `use it…`/`kill you` · 27↔53화 `bring me here`) · Codex 검토가 "유지"로 못 박은 19·24·28·36·38·42·49·50화 8줄 · 9화는 비트·주도권 불변(영어 어순만).

## 방법 (1~8화와 같은 파이프라인)
1. **재작성** — script-surgeon(opus) 3기 병렬: 9~23화 / 24~38화 / 39~53화. 입력 = 해당 구간 대상 줄(현재 CN/KO/EN + 원작 EN). 지시 = 뜻·비트·화자 톤 불변, 원작 영어와 문장 구조가 달라질 것, 단어만 바꿔 치환한 티 금지, 짧고 직설, 순화 금지, 한·중은 새 영어와 같은 뜻으로(대부분 한·중은 원작 뜻이라 안 바뀜 — 바뀌는 경우만 명시).
2. **메인 판정** — 줄마다 ① 원작보다 약해졌나 ② 어색한 영어인가 ③ 앞뒤 응수가 끊기나 ④ 같은 화 안 반복 → 기각·수정.
3. **사전 맥락 검사** — fresh-eyes(opus) 1기: 새 줄을 그 자리에 넣고 무맥락·의미 오류·캐릭터·개연성·반복.
4. **사용자 승인** — 표(현재 EN → 새 EN, 한·중 바뀌면 같이) 제시 → 승인분만.
5. **반영** — v34(1~8화 v33 뒤) 한 번에. 줄 수·손실 0·교체 후 존재·name_leak 게이트.
6. **사후 검사** — sonnet 클래스 스윕(세 언어 뜻 일치·회수선 verbatim 쌍 재확인).

## 예산·시간
surgeon 3기 + fresh-eyes 1기 + 스윕 1기 = 5기 · 약 60~80만 토큰 · 1~2시간. 1~8화 라운드(62줄)에서 메인이 20줄 이상 손봤으니 157줄이면 40~50줄은 메인 판정에서 걸러질 것으로 봄.

## 산출
- `34_storm_dragon_bride_paid_rewrite_table.md` — 승인용 표(구간별)
- `07_final/…_FINAL_v34_CN&KO&EN.docx/.md` — 반영본
- `34_storm_dragon_bride_v34_changes.md` — 전후 대조

## 순서
① 1~8화 계획 G → v33 반영(승인 시) → ② B안 1단계 착수(3기 병렬) → ③ 표 제시 → ④ 승인 → v34.
