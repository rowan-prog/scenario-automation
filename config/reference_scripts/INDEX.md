# Reference Scripts — INDEX

이 폴더는 청사진·집필·피칭덱 작성 시 **포맷·밀도·톤 참조용 자료**의 통합 인덱스다. 각 phase 프롬프트는 이 INDEX를 통해 적합한 reference를 자동 선택한다.

## 자동 발견 원칙 (필수)

phase_3·phase_4·phase_a_1·phase_a_2·phase_b 진입 시:
1. 본 INDEX를 먼저 읽는다.
2. 작품 메타(타깃·포맷·장르·언어)와 **카테고리**가 일치하는 reference를 자동 선택해 정독.
3. 일치하는 reference가 여러 개면 모두 정독 후 가장 가까운 사례를 우선 적용.
4. 사용자가 새 reference 파일을 폴더에 추가하면 **본 INDEX에도 한 줄 등재**한다 — 등재되지 않은 파일은 자동 발견되지 않는다.

## Reference 카테고리

각 reference는 다음 카테고리 중 하나 이상에 속한다:
- **script_format** — 스크립트 포맷·씬 밀도·대사 cadence 참조 (phase_4·phase_a_2 진입 시 정독)
- **blueprint_density** — 청사진의 비주얼 락·캐릭터 캐논·세계 규칙 밀도 참조 (phase_3 진입 시 정독)
- **pitchdeck_format** — 피칭덱 포맷·강점 어휘 참조 (phase_2 진입 시 정독)
- **evaluation_case_study** — 기존 작품을 시스템 룰(3층 보상·Mode A/B/C·욕망 강화 방식 등)에 매핑한 case study. phase_3 청사진 작성 시 자기 작품과 비교 참조
- **title_patterns** — vertical drama 타이틀 패턴 (phase_1·phase_2 시 정독)
- **adaptation_source** — 부가 트랙 A 각색 원작 (phase_a_1·phase_a_2 진입 시 정독)

## 등재된 Reference

| 파일 | 카테고리 | 타깃 | 포맷 | 장르 | 언어 | 비고 |
|---|---|---|---|---|---|---|
| `script_locked_out.md` | script_format | 북미 남성향 23-44 | AIGC 3D 애니 (semi-realistic) | SF 포스트아포칼립스 / Power fantasy / 하렘 | 영어 | LOCKED OUT 58화 풀 스크립트. 4씬/회차 표준, 4 블록(Visual·Camera·Dialogue·FX) 강제, 짧은 단언형 대사. **남성향 기본 포맷 표준.** |
| `script_Demon_Lord's_Marked_Bride.md` | script_format | (작품별 메타 확인) | AIGC 실사 | 다크 로맨타지 | 한국어 | 한국어 포맷 참조용. 한국어 작업 시. 파일명에 curly apostrophe (`'`) 사용 — 정확 매칭 필요. |
| `script_genius_baby_original.md` | adaptation_source, script_format | 한국 일반 시청자 (각색 원작) | 한국어 실사 일반 대본 | 회귀 / 천재아동 복수극 / 가족 복수 / 모던 | 한국어 | 70화 한국어 원작 시나리오. 08_reborn_at_ten 각색 base. phase_a_1·phase_a_2 진입 시 정독. **이 원작 = 한국 시청자 톤** — 북미 각색 시 사건 뼈대만 차용, 톤·대사 처음부터 영어 재구성 (`feedback_north_american_judgment_baseline.md`). |
| `blueprint_locked_out.md` | blueprint_density | 북미 남성향 | AIGC 3D 애니 | SF Power fantasy | 영어 | 청사진의 시스템 락(Entry Code Chip / Commander Authority / Core Unlock Sequence 등) 밀도 참조. 시스템 메커니즘이 풍부한 작품의 청사진 밀도 기준. |
| `locked_out_evaluation.md` | evaluation_case_study | 북미 남성향 | AIGC 3D 애니 | SF Power fantasy / 하렘 | 한국어 | LOCKED OUT을 시스템 룰(3층 보상·Mode A/B/C·욕망 강화 방식·결제 트리거)에 매핑한 case study. phase_3 청사진 작성 시 자기 작품의 보상·모드 매핑을 검증할 때 비교 참조. 남성향 무쌍·즉시 충족·승리 확장 정답 패턴 사례. |
| `pitchdeck_examples.md` | pitchdeck_format | 다양 | 다양 | 다양 | 영어 | 피칭덱 포맷·강점 어휘 사례. phase_2 진입 시 정독. |
| `title_patterns.md` | title_patterns | 북미 vertical drama | 다양 | 다양 | 영어 | Vertical drama 시장 타이틀 7대 패턴 + 시장 예시 200+ + 짓는 프로세스 5단계 + 거절 어휘. phase_1 작품명 결정·phase_2 통 타이틀 작성 시 정독. |

## 자동 선택 규칙

step 진입 시 작품 메타와 위 표를 매칭:

### phase_3 (완성 청사진) — blueprint_density 카테고리만
- 모든 작품: `blueprint_locked_out.md` 정독 (청사진 밀도 기준).
- 추가 reference가 등재되면 — 작품 카테고리 일치 시 함께 정독.

### phase_4 (에피소드 집필) — script_format 카테고리
- **남성향 + 영어**: `script_locked_out.md` 우선 정독.
- **여성향 + 영어**: 현재 등재된 영어 여성향 reference 없음. 사용자 추가 권장. 임시로 `script_locked_out.md` 4 블록 포맷만 차용 (대사 cadence·씬 비트 패턴은 여성향에 맞춰 자체 재해석).
- **한국어 작업**: `script_Demon_Lord's_Marked_Bride.md` 정독.
- **AIGC 애니 vs 실사**: 둘 다 동일한 4 블록 포맷 적용 — reference 부족 시 LOCKED OUT 차용.

### phase_a_1 / phase_a_2 (각색) — adaptation_source 카테고리
- 작품별 원작 파일 정독 (예: 08_reborn_at_ten → `script_genius_baby_original.md`).
- 원작 톤·대사가 비영어권일 경우 사건 뼈대만 차용, 톤·대사는 처음부터 타깃 언어로 재구성.

### phase_2 (피칭덱) — pitchdeck_format
- **모든 작품 정독:** `pitchdeck_examples.md` (기존 사례·강점 어휘).
- 메모리 룰 같이 적용: `feedback_pitch_master.md` (통합 마스터) / `feedback_evaluator_master.md` / `feedback_directness_master.md` / `feedback_banned_expressions.md` / `feedback_female_target_romance.md` / `feedback_character_name_diversity.md` / `feedback_pitch_male_target_education.md` (남성향).

### phase_a_1 / phase_a_2 (각색)
- phase_3·phase_4과 동일 규칙 적용.

### phase_b (외부 대본)
- 청사진 부재 — reference는 작품 카테고리 일치 시 정독 (대본 내적 정합성 비교 기준).

## 누락된 카테고리 — 추가 권장 Reference

현재 시스템은 다음 카테고리의 reference가 부족하다. 사용자가 추가 시 본 INDEX에 등재 필요:

- **여성향 + 영어 + AIGC 실사 / Romantasy**: ACOTAR / Fourth Wing 류 페이지 단위 톤 참조. 02_the_offering 류 작품에 직접 적용 가능.
- **남성향 + 영어 + AIGC 애니 (anime-style)**: Solo Leveling / Overlord 류 일본 seinen 영어 더빙 cadence 참조. 03_black_core 류 작품에 직접 적용 가능.
- **각색 작품 reference**: 원작 → 각색 변환 사례.
- **부가 트랙 B 외부 대본 reference**: 외부 대본 등재·평가 사례.

## 새 Reference 추가 — AI 자동 등재 방식 (필수)

사용자는 본 INDEX를 직접 편집하지 않는다. 다음 흐름:

1. **사용자**: 새 reference 파일을 `config/reference_scripts/` 폴더에 추가 (또는 외부에서 내용 제공).
2. **AI**: 자동으로 다음 처리:
   - 파일 정독.
   - 카테고리 판정 (script_format / blueprint_density / pitchdeck_format).
   - 타깃·포맷·장르·언어·비고 추출.
   - 본 INDEX의 "등재된 Reference" 표에 한 줄 자동 추가.
   - 사용자에게 한 줄 확인 보고 (예: "✅ `script_xxx.md` 등재 — 카테고리 script_format, 타깃 북미 여성향 영어").
3. **이후**: phase 진입 시 자동 발견 (INDEX 등재됨).

**사용자 트리거 패턴:**
- 사용자가 새 파일을 폴더에 추가하고 알려주거나, 다음 phase 진입 시 폴더에 새 파일이 있으면 AI가 자동 발견 → 등재 → 보고.
- 외부에서 reference 내용 제공 시 AI가 적절한 파일명으로 저장 후 등재.

**금지:** 사용자에게 INDEX를 직접 편집하라고 요청하지 않음. AI가 maintain.
