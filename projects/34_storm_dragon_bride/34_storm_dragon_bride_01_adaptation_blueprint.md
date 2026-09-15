# 34 · I Bought the Dragon Lord for One Night — 각색 청사진 (2026-09-15)

## 1. 원작
- `config/vertical_drama_hit_scripts/One Night with the Dragon Lord_FINAL_CN&EN.docx` (53화 완본 · CN 지문 + EN 대사(중문 병기)) — 사내 히트작. 사본 = `reference/`.
- 형식 = 원작과 동일(CN 지문 · EN 대사 · 중문 병기). 중국 제작이라 지문은 중국어 그대로 간다.

## 2. 모드 = ① verbatim 계승 + 껍데기 교체
- 구조·비트 순서·클리프 자리·대사 턴·화 길이 = 원작 53화 1:1. 무료 1~8화. 사건 추가 0·삭제 0.
- 손대는 것 = 이름·지명·용어·용의 색/원소·공간 묘사 한 줄씩·어색한 영어 대사(최소 수정).
- 수위 = 원작 그대로(올리지도 내리지도 않음).

## 3. 치환표

| 원작 | 우리 | CN |
|---|---|---|
| Isolde 伊索尔德 | **Nora** | 诺拉 |
| Vael 维尔 | **Damon** | 达蒙 |
| Hadren 哈德伦 | **Garrick** | 加里克 |
| Chloe 克洛伊 (妹妹/表妹 혼용) | **Vivian** (계모 쪽 여동생 = 왕의 친딸) | 薇薇安 · 继妹 |
| Elara 艾拉拉 | **Sabrina** | 萨布丽娜 |
| King Aldric 阿尔德里克 | **King Edmund** | 埃德蒙 |
| 母亲 · 侍卫 · 死士 · 长老甲/乙 · 医师 · 将领 | 그대로(무명 역할) | — |
| 人类王国 | **Ravenmoor** | 鸦泽王国 |
| Dragon Castle 龙堡 / 黑色城堡 | **Stormhold** (북해 절벽 위의 성) | 风暴堡 |
| 酒馆 | 항구 여관 | 港口客栈 |
| 黑石林 | **Wailing Wood** | 哀嚎林 |
| 雪山峭壁 / 避风山洞 | 바닷가 눈 절벽 / 해안 동굴 | 海崖 / 海崖洞穴 |
| Southern Islands 南方群岛 | **Golden Isles** | 金屿群岛 |
| Bloodline Stone 血脉石 | **Oathstone** | 誓约石 |
| Royal Blood-Poison | **Royal Venom** | 毒 (원작 그대로) |
| Primal Fire 初火 | **First Spark** | 初雷 |
| Black Sun 黑日 | 그대로 (왕의 저주 = 검정) | 黑日 |
| 黑龙 / 黑龙大军 | Storm Dragon / 风暴龙军 | 风暴巨龙 |
| 黑红色龙火 · 黑火 · 黑炎 · 龙火 | 남빛 번개불 (storm-fire) | 靛蓝雷火 · 雷焰 |
| 黑鳞 · 黑色龙鳞 · 漆黑龙鳞 | 은청색 비늘 | 银鳞 · 银蓝龙鳞 |
| 暗金色竖瞳 · 猩红竖瞳(저주) | 그대로 | — |
| 黑红色毒纹 · 咒纹 · 黑日의 黑芒 | 그대로 (검정·붉음 = 왕의 것) | — |

색 규칙 = 파랑·은색은 데이먼 자신의 힘, 검정·검붉음은 왕의 저주와 독. 원작에선 둘 다 검붉어서 구분이 없었다.

## 4. 이름 기준 (사용자 2026-09-15)
**영어권 이름만**(북유럽·이탈리아풍 "판타지 이름" 금지 — 2026-09-15 사용자 교정, 1차 Astrid/Soren/Bianca/Ingrid/Magnus 반려) · AI가 이름으로 읽음 · 읽는 법이 하나뿐(Nora·Damon·Garrick·Vivian·Sabrina·Edmund 전부 통과) · 원작 이름 잔존 0 (`tools/name_leak_check.py` PASS 필수).

## 5. 작업 방식 (토큰 최소)
1. 기계 치환(python) — 이름·지명·용어·색. 지문 본문은 손 안 댐.
2. opus 2기 — EN 대사 482줄 중 어색한 줄만 old/new 쌍으로(≤30%) · 급소 대사 verbatim.
3. sonnet 1기 — 바닷가 절벽 세계에 맞게 지문 20줄 내외 한 구절씩.
4. 게이트 — name_leak_check PASS · 잔재 grep 0 · 53화 · 대사 줄 수 482 유지 · 한국어 0.
