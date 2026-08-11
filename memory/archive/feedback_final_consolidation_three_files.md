---
name: deprecated-2026-05-17-by-final-md-only
description: ⛔ 폐기 (2026-05-17 체질 개선 v3). 옛 3종 최종고 (FINAL_FREE·FINAL_PAID·FINAL). 대체 = FINAL.md 1종.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 868e03f4-e9d0-41c4-ac4d-5b5b74c6d554
  deprecated: true
  deprecated_by: feedback_unified_writing_flow.md
---

# ⛔ 폐기 — 3종 최종고 통합 룰

> **2026-05-17 체질 개선 v3 폐기.** 새 룰: **최종고 1종 (FINAL.md만)** — 무료/유료 분리 폐기 정합.
>
> **대체 시스템:** `feedback_unified_writing_flow.md` (FINAL.md 1종) + `feedback_conversion_runway_writing.md` (Conversion Runway 집필).
>
> 본 메모리 = 역사 기록·삭제 X / 단 룰로 사용 X.

---

## (옛 내용 — 참고용·실행 X)

작품의 **모든 회차 (무료 + 유료) 집필·검토·패치·4-Gate 완료** 시점에 **반드시** 다음 3종 최종고 통합 + 검증 자동 진행. 어떤 프로젝트에도 예외 X.

**Why:** 사용자 명시 (2026-05-13) — "항상, 반드시. 전체 회차 최종고가 나오면, 이 프로세스 진행해야한다. 어떤 프로젝트". 화별 분리된 파일 50개 통합 부담을 사용자가 지지 않도록 시스템이 자동 제공.

**How to apply:**

## 1. 트리거

다음 조건 모두 충족 시 자동 진행:
- 모든 회차 (free + paid) EP 파일 작성 완료
- 모든 회차 phase_5 (검토) + phase_6 (패치) + phase_7 (4-Gate) 통과
- 또는 protocol_premium_pilot.md run 완료 (premium 작품)

## 2. 산출 파일 (07_final/)

```
projects/[작품명]/07_final/
  [작품명]_FINAL_FREE.md       (무료 회차 통합 — 보통 EP1-8)
  [작품명]_FINAL_PAID.md       (유료 회차 통합 — 보통 EP9-50)
  [작품명]_FINAL.md            (전체 회차 통합 — EP1-50)
  [작품명]_FINAL_synopsis_kr.md (한국어 1,500자 요약 — phase_8 산출)
```

## 3. 통합 처리 룰

### 헤더
각 FINAL 파일 상단에 작품 헤더 + 메타:
```
# [작품명] — FINAL_FREE/PAID/FULL (EP범위)

Format: [AIGC Live-action·Animation / 9:16·16:9]
Target: [타깃 정보]
Generated: [날짜] via [phase_7 or protocol_premium_pilot v5.x]

---
```

### EP 본문 추출
각 EP 파일에서:
- 첫 `# [작품명] — EPxx: Title` 헤더부터
- 마지막 `Hard Cut` 마커까지 (EP-end marker)
- 검토·패치 노트·Heavy Gate·Bible Amendment 등 **post-script 섹션 제외**

**Post-script 제외 패턴 (정규식):**
```
(?ms)\r?\n---\s*\r?\n\r?\n#{1,3}\s*EP\d+
```
이 패턴 매칭 위치 이전까지 본문으로 채택.

### Separator
EP 간 separator: `\r\n\r\n---\r\n\r\n` (공백 줄 + `---` + 공백 줄).

### 인코딩
UTF-8 without BOM. `[System.Text.UTF8Encoding]::new($false)` 사용.

## 4. 검증 (자동, 통합 직후 필수)

**필수 통과 항목:**

| 항목 | 기준 | 실패 시 |
|---|---|---|
| Korean character count | EP body에 0건 (`\p{IsHangulSyllables}` 매칭 0) | 🔴 원본 EP 수정 후 재생성 |
| Work header count | EP 수 + 1 (master + 각 EP) | 🔴 누락·중복 확인 |
| S# scene count | 청사진 명시 씬 수와 일치 | 🟡 차이 발견 보고 |
| Hard Cut count (strict `^Hard Cut\s*$`) | EP 수와 일치 (1 per EP) | 🔴 mid-EP Hard Cut 제거 / 누락 보강 |
| 4 블록 일관성 | Visual = scene count / Camera·DIALOGUE·FX = scene count + end image 수 | 🟡 블록 누락 확인 |
| Separator (`---`) | EP 간 일관 | 🟡 일관성 보강 |
| File size | 합리적 범위 | 🟡 너무 작거나 큼 확인 |

## 5. 실행 방식

**phase_7_final_gate.md** 또는 **protocol_premium_pilot.md Step 17** 통과 직후 자동 진행:

```powershell
# 의사 코드 (PowerShell .NET I/O 사용 — UTF-8 no BOM)
function Get-ScriptBody($path) {
    $content = [System.IO.File]::ReadAllText($path)
    $rx = [regex]"(?ms)\r?\n---\s*\r?\n\r?\n#{1,3}\s*EP\d+"
    $m = $rx.Match($content)
    if ($m.Success) { return $content.Substring(0, $m.Index).TrimEnd() }
    return $content.TrimEnd()
}

# 무료 + 유료 EP body 추출
$free_content = (1..[무료마지막] | ForEach-Object { Get-ScriptBody "[free path]/ep$($_.ToString('00')).md" })
$paid_content = ([무료마지막+1]..[전체화수] | ForEach-Object { Get-ScriptBody "[paid path]/ep$($_.ToString('00')).md" })

# 3종 헤더 추가 후 통합
[System.IO.File]::WriteAllText("[07_final]/FINAL_FREE.md", $free_header + ($free_content -join $sep), $utf8NoBom)
[System.IO.File]::WriteAllText("[07_final]/FINAL_PAID.md", $paid_header + ($paid_content -join $sep), $utf8NoBom)
[System.IO.File]::WriteAllText("[07_final]/FINAL.md", $full_header + (($free_content + $paid_content) -join $sep), $utf8NoBom)

# 검증 — Korean 0건·Hard Cut = EP 수·블록 일관성
```

## 6. 메타 갱신

3종 FINAL 생성 후 작품 메타 (`[작품]_00_meta.md`) 갱신:
- 작품 상태: "**완결 ✅**"
- 최종고 위치: `07_final/FINAL.md` (전체) / FINAL_FREE.md (무료) / FINAL_PAID.md (유료)
- 검증 결과: Korean=0 / 헤더 수 / 씬 수 / Hard Cut 수 / 블록 일관성 모두 통과

## 7. 예외 / 변형

- **무료-only 작품 (희귀):** FINAL_FREE.md + FINAL.md만 (FINAL_PAID 생략)
- **무료/유료 분할 시점 다른 작품:** 작품 메타의 "무료회차 수" 기준 분할
- **시즌 분할 작품:** 시즌별 FINAL_FREE / FINAL_PAID 또는 시즌별 FINAL 추가 생성 가능
- **premium_pilot run 작품:** protocol Step 17 Final Pilot Gate 통과 후 자동 / `premium_pilot/10_rewrite/` + `premium_pilot/paid/`에서 추출

## 8. 관련 룰

- 단일 통합 MD 룰: `feedback_round_independence_and_final_format.md`
- 한국어 영어 일원화: `feedback_script_english_only.md`
- 메타 신뢰성: `feedback_meta_trust_and_verify.md`
- phase_8 한국어 요약: `phase_8_synopsis_summary.md` (별도 phase)

## 핵심 한 줄 결론

> **작품 완결 = 07_final/에 FINAL_FREE.md + FINAL_PAID.md + FINAL.md 3종 통합 + 자동 검증. 모든 프로젝트 예외 X.**
