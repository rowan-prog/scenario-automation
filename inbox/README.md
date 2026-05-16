# inbox/

사용자가 외부 자료를 일시적으로 보관하는 자유 저장소.

## 용도
- 외부 문서·자료를 작업공간에 빠르게 임시 등재 (붙여넣기·다른 경로 첨부 어려운 경우)
- 사용자가 명시적으로 경로를 지시할 때만 AI가 읽음
- **자동 로딩 없음 — 시스템 자료와 완전 분리**

## 사용 흐름
1. 사용자: 자료를 `inbox/` 안에 놓음 (자유 파일명)
2. 사용자: AI에게 "inbox/[파일명] 읽고 ~ 해줘" 식으로 지시
3. AI: 해당 파일만 읽고 작업 수행
4. 인사이트가 지속 참조 필요한 경우: AI가 시스템 내 적절한 위치에 정리 저장 (`config/`, 메모리, 작품 폴더 등)
5. 사용자: inbox/ 안의 원본은 언제든 자유 삭제

## AI 규율
- ❌ **자동 로드 금지** — 사용자 명시 지시 없이 inbox/ 안의 파일을 읽거나 참조 X
- ❌ inbox/ 안의 파일을 시스템 룰·메모리·작품 근거로 직접 인용 X (워싱 → 정식 위치 등재 거쳐야 함)
- ❌ inbox/ 안의 파일을 status.md·audit.md 점검 대상에 포함 X
- ✅ 사용자 지시 시 해당 파일만 정독
- ✅ 인사이트 추출 시 검증 후 적절한 시스템 위치에 정리 저장
- ✅ inbox/ 안의 파일은 사용자 자유 삭제

## 폴더 분리 원칙
inbox/ 는 시스템 자료(`config/`, `prompts/`, `projects/`, `memory/`)와 완전히 격리. inbox/ 안에서 일어나는 모든 일은 inbox/ 안에 머무름 — 단, 사용자 명시 지시로 인사이트가 시스템에 정리될 때만 외부에 흔적이 남음.

## 본 README
이 README도 사용자 판단으로 언제든 삭제 가능. 단, AI가 향후 세션에서 inbox 용도를 잊지 않도록 보존 권장.

---

## 처리된 자료 (2026-05-15)

| inbox 파일 | 시스템 이관 위치 | 처리 |
|---|---|---|
| `AIGC_Paid_Vertical_Integrated_Master_Guide_20260515_v3.md` | `config/master_guide_v3.md` | ✅ 이관 + 최상위 권한 등재 (메모리 `feedback_v3_master_guide_supremacy.md`) |
| `vertical_hit_library_final_validated_2026-05-15_final.xlsx` | `config/hit_library/vertical_hit_library_2026-05-15.xlsx` | ✅ 이관 (288작 + 76 후보 + 43 AIGC tracker + 81 tropes) |
| `피칭덱 문체용 레퍼런스.txt` | `config/pitch_style_reference.txt` | ✅ 이관 + 메모리 `feedback_pitch_style_master_v2.md` 추출 |

inbox 본 파일은 사용자가 언제든 삭제 가능. 시스템 내 사본·인사이트는 보존.
