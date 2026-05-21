# Hard Rules — 1 Page (절대 12)

> 모든 phase 진입 시 본 파일 정독. master_guide_v3 (5816줄) 대신 본 1페이지가 hard rule의 단일 출처.

---

## 본문 양식 v3 (2026-05-19 후반 — 영상 리듬 확장)

1. **EP 양식 v3 블록 10개:**
   - **장면 블록 5개 (기존):** `[VISUAL/ACTION]` · `[KEY CAMERA]` · `[DIALOGUE]` · `[GRAPHIC/UI]` · `[END HOOK]`
   - **영상 리듬 블록 5개 (신설):**
     - `[MONTAGE]` — 시간 압축·여러 짧은 컷·1 비트당 1줄 (예: "Vael locks the same door at dawn. / Belly grows under silk. / Kiran reports from the same threshold. / Ridge eyes open then close. / Vael's hand on her belly more careful each night.")
     - `[VO]` — Isolde / Vael / Kiran 등 화자 명시·감정·시간 압축용·EP당 1-2문장 이하 (예: `ISOLDE (V.O.): The keep did not get smaller. He made the world stop at the door.`). 설명·문학체 금지.
     - `[FLASHBACK]` — 1-2초 insert·대사 재생 금지 또는 한 단어만·감각 회수용 (예: `EP01 chain on her wrist — 1 second cut.`)
     - `[INSERT/CUTAWAY]` — Object·Body·Detail close-up·1초 (예: `Wet pebble on bench. / Mireille pendant catching firelight. / Iron link in cradle corner.`)
     - `[INTERCUT]` — 두 공간 동시 진행·cross-cut 표기 (예: `INTERCUT — corridor: Kiran's men at the door. Chamber: Vael's hand on her belly.`)

2. **회차 수 가변 + Hard Cut = EP수-1.** 마지막 EP = 자연 엔딩 (`Fade Out.` / `End.` / 없음). mid-EP `Hard Cut` 마지막 EP에 두면 즉시 fail.
3. **9:16 default.** 16:9는 명시적 사유 필요.
4. **EP body Korean character 0건.** `\p{IsHangulSyllables}` 매칭 = 즉시 fail.

## 화면 리듬 (가장 비싼 룰·반드시 준수)

5. **EP당 영상 리듬 블록 ≥1개 필수.** `[VISUAL/ACTION]` 정면 대화만 = 화면 선형화. 매 EP MONTAGE / VO / FLASHBACK / INSERT / INTERCUT 중 1개+ 삽입. 후반부 (반복 위험) EP = 2개+.
6. **부위 순회형 tracking 금지 (Female gaze 룰).** "thigh → ribs → throat → collarbone" 순회 = male gaze. 대신 Vael 통제 상실·forearm weight·Isolde agency·breath·firelight·sheet·hand·choice 우선. 부위 자체 줄임 X / **시선 우선화.** 상세: `feedback_female_gaze_camera_polish.md`.
7. **Master + Platform-safe 이원화.** 초고수위 씬 = master version (`07_final/[작품]_FINAL_v{N}.md`) 보존·platform-safe = 별도 파일 (`07_final/[작품]_FINAL_v{N}_platform_safe.md`) 카메라·문장 우회 본문. 상세: `feedback_master_platform_safe_dual_version.md`.
8. **Spoken English 원어민 polish.** 5단어 default·자연 spoken English 우선. 5단어 이하 강제 = "원시인 영어"·"코미디" 위험 (`If she cost me you.` 류 문법 오류·`Her no holds. Her names cost hands.` 류 부자연 압축). 자연 spoken 위해 5-10 단어 허용·핵심 결정 발화만 1-3 단어.

## 집필 컨텍스트

9. **매 phase_4 진입 시 매칭 히트작 raw 대본 3-5 EP + 이전 EP 3개 raw 정독.** 옛 "첫 1-2 씬만 Read" 룰 = 폐기. 메타 baseline = 매 phase 진입 시 always-load 3개만 (MEMORY.md). 나머지 = 호출 트리거. **검증 보고서·테이블·자가 검수 풀이 = 본문 외 작성 금지.**

## 작품·폴더·파일

10. **작품 폴더 prefix 명명** (`projects/02_the_offering/02_the_offering_04_blueprint.md`). 폐기 = `_X_NN_slug` (자동 차단). **최종고 1종 + V 번호 명명** (`07_final/[작품]_FINAL_v{N}.md`). 옛 정본 = `07_final/_archive_versions/`.

## 검토 / 환류

11. **검토 채택 필터 2단계:** 필터 1 (무조건 채택) = 공간/시간/소품/인과/정합성/언어 일원화 위반·**부위 순회 tracking·시선 위반·영상 리듬 블록 부재** 추가. 필터 2 (거부) = 작품 핵심 쾌감 약화·캐릭터 매력 약화·Soft Lock 강제 표준화.
12. **청사진 ↔ 본문 환류.** 본문이 더 강하면 청사진 부분 업데이트 (Hard Lock = 사용자 승인). 환류 시 청사진 말미 1줄 로그.

---

## 자료 출처 (필요 시만 정독)

| 자료 | 위치 | 진입 시점 |
|---|---|---|
| Conversion Runway 7 단계 | `prompts/phase_4_episode_writing.md` | phase_4 진입 |
| 영상 리듬 baseline | `memory/feedback_screen_rhythm_v3_blocks.md` | 집필 진입 |
| Female gaze baseline | `memory/feedback_female_gaze_camera_polish.md` | 다크 로맨스 집필 진입 |
| Master + platform-safe | `memory/feedback_master_platform_safe_dual_version.md` | 초고수위 작품 |
| Spoken English | `memory/feedback_spoken_english_native_polish.md` | 영어 대본 집필 |
| 페르소나 9개 | `config/personas/` | 검토 시점만 |
| 평가위원 7인 | `config/evaluators.md` | 피칭 시점만 |
| 타깃 자료 | `config/target_research/[성별]_target_research.md` | phase_0-5 진입 |
| 히트작 분석 | `config/vertical_drama_hit_scripts_analysis/` | 청사진·집필 진입 |
| 히트작 raw 대본 | `config/vertical_drama_hit_scripts/` | 집필 시 (룰 #9) |
| Reference INDEX | `config/reference_scripts/INDEX.md` | phase_3/4 진입 |

---

## 자동 차단 (실행 X)

- 폐기 프로젝트 (`_X_*`) 호출 → 폐기 알림 + 작업 거부
- 본문 한국어 → 즉시 정정
- 영상 리듬 블록 0개 EP → 작업 중단·MONTAGE/VO/FLASHBACK/INSERT 1개+ 추가
- 부위 순회 tracking (thigh → ribs → throat 순서 묘사) → 시선 우선화 정정
- 검증 보고서·테이블·자가 검수 풀이 = 작성 거부
- **🚨 Vertical 자체 룰 — 행정/법/정치/외교 절대 금지** (성별·신분·장르 무관). charter·treasury·hearing·decree·외교 협상·exile (formal)·policy·writes letter·brand mark·council vote·sentence 등. 어떤 캐릭터도 (왕·여왕·주인공·악역) 행정 행위 X. Vertical ≠ HBO 변호사 드라마. 사용자 명시 지시 없으면 *즉시 personal violence + visceral claim 비트로 reframe*. 상세: `memory/feedback_vertical_no_admin_power.md`.

---

## 한 줄

> **장면 5블록 + 영상 리듬 5블록 = v3. 매 EP 영상 리듬 1개+. Female gaze 시선 우선. Master + platform-safe 이원화. Spoken English 자연 5-10단어.**
