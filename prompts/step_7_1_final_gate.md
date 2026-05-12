# Step 7-1 — 최종고 게이트 평가 프롬프트

## 역할
패치 라운드를 거친 에피소드 스크립트가 최종고로 확정 가능한지를 production_guide Section 23의 4-Gate (Structure / Narrative / Script / Production) 로 평가한다.

모두 통과 → `07_final/[작품명]_ep[N].md`에 최종고 복사 + `[작품명]_00_meta.md` 업데이트.
일부 미통과 → 미통과 게이트별 결함 보고 + 다음 행동 권장 (재검토 / 재패치 / 청사진 재작업).

## 실행 전 읽어야 할 파일
- config/production_guide.md
  - Section 0-3 (락/열어둠 — Soft Lock 영역은 미통과 사유로 쓰지 않음)
  - **Section 23 전체** (Structure / Narrative / Script / Production Gate — 4-Gate 체크리스트)
  - Section 22 (재검토 원칙 — 무한 수정 회피)
  - Section 24 (최종 핵심 규칙 — 한 줄 요약)
- 정합성 기준 청사진 (트랙별 분기):
  - 메인 트랙: `projects/[작품명]/[작품명]_04_blueprint_full.md`
  - 부가 A 트랙: `projects/[작품명]/[작품명]_01_adaptation_blueprint.md`
  - 부가 B 트랙: 청사진 부재 — 대본 자체가 정합성 기준 (대본 내적으로 평가)
- 최종 검토 대상 스크립트: `projects/[작품명]/05_episodes/[작품명]_ep[번호]_r[N].md` (마지막 라운드)
- 최신 검토 보고서: `projects/[작품명]/06_reviews/round[N]/` (최종 라운드의 페르소나 검토 결과)
- `projects/[작품명]/[작품명]_00_meta.md` (트랙·라운드 카운트 확인)

## 필수 입력값
- 평가 대상 에피소드 번호
- 최종 라운드 번호 (라운드 N — 가장 마지막에 패치된 라운드)

## 4-Gate 진입 조건 (필수)

다음 조건 모두 충족 시에만 4-Gate 진입:
1. step_5_1 최신 라운드의 모든 페르소나 verdict가 **"통과"** 또는 **"조건부 통과"**.
2. "패치 필수" 또는 "재설계" verdict 잔존 시 **즉시 step_6_1 패치 → step_5_1 재검토(전수검사)** 강제. 4-Gate 불가.
3. **각 페르소나가 검토 시 의심 지점 5+건 사전 스캔 + "검토했으나 유지" 1-3건 + 모든 등급 판정에 원문 FIND 인용을 동반**했는지 확인 (step_5_1 공격적 검증 프로토콜 충족). 이 형식이 아닌 검토 보고서는 검토 강도 미달 — 재검토 강제.
4. **각 페르소나의 LOCK / PATCH THEN LOCK / HOLD 최종 verdict 동반.**
   - LOCK = 최종고 즉시 확정 가능
   - PATCH THEN LOCK = 명시 패치 후 최종고 확정
   - HOLD = 패치만으로 부족 — 재설계 필요
   하나라도 HOLD면 4-Gate 진입 불가.

조건부 통과 페르소나의 🟢 항목은 4-Gate 통과 후 별도 결정 (제작 단계 권고).

## 공격성·증거 요구·통과 기준 (필수)

페르소나 구성은 충분하지만 검토 모드의 공격성·증거 요구·통과 기준이 약하면 통과가 너무 쉬워진다. 4-Gate 평가는 다음 기조로 진행한다.

### 1. 칭찬 목적 아님
4-Gate는 "잘 만들어졌다 인정"이 아니라 **"제작·서비스·결제·시청자 반응에 실제 손해가 될 문제를 마지막에 한 번 더 잡는 게이트"**다. 통과는 결과지 목적이 아니다.

### 2. 모든 통과 판정도 근거 강제
"Structure 통과", "Production 통과" 같은 판정은 **반드시 원문 인용 또는 검증 명령 결과를 동반**한다. "Hard Lock 모두 충족"이 아니라 "EP8 페이월 — `'You don't command me anymore.'` 발화 + 함대 섬멸 + 계급장 강탈 + 다음 좌표 4요소 모두 본문에서 확인" 형식.

### 3. 의심 지점 사전 스캔 (4-Gate 단위)
각 Gate 진입 전 **그 Gate에서 깨질 수 있는 5+ 의심 지점을 먼저 스캔**. 검증 후 통과/패치 판정.

### 4. 추상 평가·전체 재작성 제안 금지
- "전체적으로 작동" 류 추상 평가 금지.
- 4-Gate 단계에서 "대본 재작성" 제안 금지 (재설계는 step_5_1·step_6_1 단계).

### 5. 시청자 페르소나 진단의 단독 통과 차단
시청자 페르소나(08/09)의 "작동" 판정만으로 Gate 통과 불가. **05·07·04 중 최소 2명이 같은 부분에 대해 원문 근거로 재판정**한 결과를 4-Gate 보고서에 동반.

## 출력 — 두 산출물

### 1. 최종고 게이트 평가 보고서

경로: `projects/[작품명]/06_reviews/[작품명]_final_gate_ep[번호].md`

작성 형식 (마크다운):

```markdown
# 최종고 게이트 평가 — [작품명] EP[번호]

## 평가 대상
- 스크립트: `projects/[작품명]/05_episodes/[작품명]_ep[번호]_r[N].md` (Round [N])
- 트랙: 메인 / 부가 A / 부가 B
- 정합성 기준: 04_blueprint_full.md / 01_adaptation_blueprint.md / 대본 내적

## 4-Gate 결과 (Section 23)

### Structure Gate (23-1)
- [ ] 시청자 결핍이 초반에 선명한가?
- [ ] 욕망이 한 줄로 고정되는가?
- [ ] 무료 구간이 하나의 보상으로 수렴하는가?
- [ ] 페이월 직전 절단이 강한가?
- [ ] 유료 초반에 약속한 보상을 회수하는가?

**판정:** 통과 / 미통과
**미통과 항목:** [있다면 어느 항목·왜]

### Narrative Gate (23-2)
- [ ] 캐릭터 캐논이 흔들리지 않는가? (트랙 B는 대본 내적 일관성으로 판정)
- [ ] 관계 원리가 유지되는가?
- [ ] 세계 규칙이 일관되는가?
- [ ] 정보 공개 순서가 설계되어 있는가?
- [ ] 큰 reveal의 어휘가 작은 reveal에서 소모되지 않았는가?
- [ ] 캐릭터가 알 수 없는 정보를 말하지 않는가?

**판정:** 통과 / 미통과
**미통과 항목:** [있다면 어느 항목·왜]

### Script Gate (23-3)
- [ ] 대사가 기능만 수행하지 않는가?
- [ ] 캐릭터가 살아 있게 반응하는가?
- [ ] 주제 설명 대사가 아닌가?
- [ ] Visual 지문은 물리적인가?
- [ ] AIGC가 만들 수 있는가?
- [ ] 장면 끝에 관계 / 정보 / 주도권 / 감정 / 상황 중 하나가 갱신되는가?

**판정:** 통과 / 미통과
**미통과 항목:** [있다면 어느 항목·왜]

### Production Gate (23-4)
- [ ] 공간 동선이 이해되는가?
- [ ] 아이템 위치가 이어지는가?
- [ ] 캐릭터 외형 락이 유지되는가?
- [ ] 권한 / 시스템 / UI 정보가 충돌하지 않는가?
- [ ] 섹슈얼 포인트가 장면 기능과 연결되는가?
- [ ] 페티시 과잉으로 일반 타깃을 좁히지 않는가?
- [ ] 연출 변경이 정보 전달 기능을 훼손하지 않는가?

**판정:** 통과 / 미통과
**미통과 항목:** [있다면 어느 항목·왜]

## 종합 판정

- [ ] **모두 통과** → 최종고 확정. `07_final/[작품명]_ep[번호].md`에 복사.
- [ ] **일부 미통과** → 다음 행동 권장:
  - **단순 미세 조정 가능 (1~2건):** step_6_1 추가 패치 라운드 (라운드 한계 내일 때)
  - **정합성·구조 결함:** step_5_1 페르소나 재검토 (해당 페르소나만 재호출)
  - **상위 결함 (캐논·세계 규칙·페이월 약속 위반):** step_3_1 / step_a_1 청사진 재작업
  - **무한 수정 위험 (라운드 5 도달 + 유사 결함 반복):** 사람 판단 — Soft Lock 영역으로 분류 후 통과 인정 또는 작업 보류

## 최종 권장
[1~2문장 — 다음 행동 + 이유]
```

### 2. (통과 시) 최종고 복사

경로: `projects/[작품명]/07_final/[작품명]_ep[번호].md`

마지막 라운드 스크립트(`05_episodes/ep[번호]_r[N].md`)를 그대로 복사.
파일 헤더에 다음 메타 한 줄 추가:

```
<!-- 최종고: [작품명] EP[번호] · Round [N] · 4-Gate 통과 [날짜] -->
```

## 작성 원칙

### Hard Lock 위반만 미통과 사유 (Section 0-3)

평가는 **4-Gate 항목**에 집중. 4-Gate는 모두 Hard Lock 영역.
Soft Lock 영역(톤·대사 방식·인티머시 강도·캐릭터 매력의 강약 등)은 미통과 사유로 쓰지 않는다.

"이 톤이 더 다크해야 한다 / 이 인티머시가 더 강해야 한다 / 이 캐릭터가 더 매력적이어야 한다" 같은 지적은 미통과가 아니다 — 작품 자율 영역.

### 트랙별 정합성 기준

- **메인 트랙:** 04_blueprint_full.md의 캐릭터 캐논·세계 규칙·정보 설계와 비교.
- **부가 A 트랙:** 01_adaptation_blueprint.md의 각색 방향 + 캐논과 비교. 원작 충실성은 청사진 강도(충실/현대화/재해석)에 따라.
- **부가 B 트랙:** 청사진 부재 → **대본 내적 정합성**으로 판정. 같은 캐릭터·세계 규칙이 대본 안에서 일관되는지.

### 라운드 5 도달 + 유사 결함 반복 → 사람 판단

라운드 5까지 패치를 거쳤는데도 같은 결함이 미통과로 남는다면:
- 결함이 정말 Hard Lock 위반인지 재확인
- 또는 Soft Lock 영역을 강제로 표준화하려 했는지 의심
- 사람 판단으로 "이 결함은 작품 자율 영역으로 분류" 결정 시 통과 인정 가능

이때 통과로 인정되면 그 결정 근거를 보고서 "최종 권장" 섹션에 명시.

## 저장 위치
- 평가 보고서: `projects/[작품명]/06_reviews/[작품명]_final_gate_ep[번호].md`
- 통과 시 최종고: `projects/[작품명]/07_final/[작품명]_ep[번호].md`

## 실행 순서
1. config/production_guide.md Section 23 4-Gate를 내면화한다.
2. 트랙·정합성 기준을 확인한다 ([작품명]_00_meta.md 참조).
3. 마지막 라운드 스크립트와 최신 검토 보고서를 읽는다.
4. 4-Gate 체크리스트를 항목별로 점검한다 (각 항목 통과/미통과 표기).
5. 종합 판정 — 모두 통과 / 일부 미통과 결정.
6. 평가 보고서를 `06_reviews/final_gate_ep[번호].md`에 저장한다.
7. 모두 통과 시 — **단일 통합 MD 생성 + 검증**(아래 섹션 참조). EP별 분리 X.
8. `[작품명]_00_meta.md`를 업데이트한다 (4-Gate 통과 표 갱신, 통과 시 최종고 위치 기록).
9. 종료 안내:
   - 모두 통과: `✅ [작품명] 50화 최종고 확정 — projects/[작품명]/07_final/[작품명]_FINAL.md`
   - 일부 미통과: `🟡 [작품명] 게이트 미통과 — 미통과 게이트: [목록]`
   - 권장: `[step_6_1 패치 / step_5_1 재검토 / step_3_1 청사진 재작업 / 사람 판단]`

## 최종고 = 단일 통합 MD + 검증 (필수)

최종고는 **화별 분리 X — 모든 화 순서대로 통합한 단일 MD 1개**를 생성한다.

### 통합 형식
- 경로: `projects/[작품명]/07_final/[작품명]_FINAL.md`
- 구조: 작품 정보 헤더 → EP1 본문 + `---` → ... → EP50 본문 + `---` → 시리즈 푸터.
- 각 EP는 cleanup된 형태(첫 헤더 + S#1 ~ Hard Cut)만 포함.

### 통합 명령 (PowerShell, 권장)
```powershell
$work = "<work_slug>"; $title = "<work title>"
$outPath = "projects\$work\07_final\${work}_FINAL.md"
$epDir = "projects\$work\05_episodes"
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# $title — FINAL CUT"); [void]$sb.AppendLine(""); [void]$sb.AppendLine("---"); [void]$sb.AppendLine("")
for ($i = 1; $i -le 50; $i++) {
  $padded = "{0:D2}" -f $i; $epPath = "$epDir\${work}_ep${padded}.md"
  if (Test-Path $epPath) {
    [void]$sb.AppendLine((Get-Content $epPath -Raw -Encoding UTF8).TrimEnd())
    [void]$sb.AppendLine(""); [void]$sb.AppendLine("---"); [void]$sb.AppendLine("")
  }
}
Set-Content -Path $outPath -Value $sb.ToString() -Encoding UTF8 -NoNewline
```

### 검증 (필수)
통합 MD 생성 직후 다음을 모두 검증. 이상 시 즉시 재생성·재검증.

| 항목 | 기준 |
|---|---|
| EP 헤더 개수 | 50 (`^# .* — EP\d+:`) |
| EP 헤더 순서 | EP1 → EP50 |
| `[Visual]`·`[Camera]`·`[DIALOGUE]`·`[FX]` 블록 | 각 카운트 일치 (50 × 4씬 + 페이월 보정) |
| `[End Image]` | 50 |
| `Hard Cut` | 50 |
| **한국어 검출** | **0** (`\p{IsHangulSyllables}` 또는 `[ㄱ-ㆎ]`) |

### 검증 명령 (PowerShell, 권장)
```powershell
$path = "projects\<work>\07_final\<work>_FINAL.md"
$lines = Get-Content $path -Encoding UTF8
$ep = ($lines | Where-Object { $_ -match '^# .* — EP\d+:' }).Count
$v = ($lines | Where-Object { $_ -match '^\[Visual\]' }).Count
$c = ($lines | Where-Object { $_ -match '^\[Camera\]' }).Count
$d = ($lines | Where-Object { $_ -match '^\[DIALOGUE\]' }).Count
$f = ($lines | Where-Object { $_ -match '^\[FX\]' }).Count
$ei = ($lines | Where-Object { $_ -match '^\[End Image\]' }).Count
$hc = ($lines | Where-Object { $_ -match 'Hard Cut' }).Count
$ko = 0; foreach ($l in $lines) { if ($l -match '\p{IsHangulSyllables}' -or $l -match '[ㄱ-ㆎ]') { $ko++ } }
"EP=$ep V=$v C=$c D=$d F=$f EndImg=$ei HardCut=$hc Korean=$ko"
```

**한국어 1건이라도 검출 시 Production Gate 즉시 fail — step_6_1 패치 후 step_7_1 재진행.** 한국어가 잡히지 못하고 통합된 사례 있음(2026-05-08); 이 검증은 4-Gate 평가의 일부.
