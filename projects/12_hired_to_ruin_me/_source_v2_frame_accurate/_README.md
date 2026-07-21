# 원작 소스 V2 (프레임 정확 리빌드) — 각색 레퍼런스

**원작 = The CEO's Tempting Secretary** (dailymotion xacqflm · 1h42m · 영어 자막 번인). 이 폴더 = 원작 영상에서 **프레임 단위로 재추출한 프로덕션 컷 대본**의 사본(레퍼런스 전용·수정 금지).

## 왜 V2인가 (2026-07-15 사용자 지시로 등재)
- 우리 각색(FINAL_v1~v3)이 기반했던 **옛 66씬 단일 마스터 = 폐기됨**(소스 파이프라인이 speaker swap·STT 깨짐·**△를 one-shot이 아닌 generic action paragraph로 취급**한 결함으로 rejected — `_SOURCE_STATUS.md` §Rebuild V2).
- 새 소스 = scene-change 후보 2,044개 → 검증된 순서 shot index → **컷당 shot cue 1개 + △ 1개**. 프레임 타임스탬프 drift 0.
- **현재 R01(00:00~00:46.555)만 존재.** 나머지 ~1h41m은 아직 재추출 중(status "Next action: Continue cut verification and English drafting after R01"). 라운드 도착 시마다 이 폴더에 추가.

## 러프임 (반드시 인지 — 사용자 강조)
완벽 구현 아님. 명백한 결함 예: **S#001 = 19초·8샷 전부 대사 0 (샤워 무드컷)** = 무드로 끄는 구간. 우리 각색에 **베끼면 안 됨**.

## 각색 크래프트 룰 (이 소스 적용 시 · 사용자 2026-07-15)
- **대사 없는 구간 5초 초과 금지.** 무드/분위기로 끌지 마라. 초고수위 씬만 약간 초과 허용(그래도 최소).
- 소스 실제 대사 = 직설 레지스터 앵커(`Are you drunk?`·`Do you know who my wife is?`). GL 치환해 계승.
- **△ = one-shot 규율** — 소스 V2의 리빌드 사유 그 자체. 우리 각색 △도 동일 규율로(못 찍는 지문 외화).

## GL 매핑 (blueprint §3-1)
| 원작 | 본작 |
|---|---|
| Elric (표적·기혼·유혹당함) | **Claire** |
| Elia (고용된 유혹자·에스코트) | **Eve** |
| Cyrene (바람난 계략 배우자) | **Richard** |
| Neil (내연) | **Vanessa** |

R01 씬 = Elia가 Elric 유혹 → Elric 거절("I'm married. Do you know who my wife is?"). GL = **Eve가 Claire 유혹 → Claire 거절.** 아이러니 = Eve는 Claire의 남편(Richard)이 보낸 걸 안다.
