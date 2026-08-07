# projects/

작품 폴더가 생기는 곳. 지금은 비어 있다.

## 명명 규칙 (필수)

```
projects/[NN]_[slug]/[NN]_[slug]_[단계번호]_[단계명].md
```

- 폴더 번호 `NN` = 작품 생성 순서. 두 자리.
- 폴더 안의 모든 파일은 **폴더명과 같은 prefix**로 시작한다 — 파일만 봐도 어느 작품의 어느 단계인지 식별된다.
- 하위 폴더 `05_episodes/` · `06_reviews/` · `07_final/` 는 prefix 없이 공통 이름을 쓴다. 그 **안의 파일**은 prefix를 붙인다.
- 폐기한 작품은 폴더명 앞에 `_X_` 를 붙인다 (`_X_03_something`). 에이전트가 자동으로 작업 대상에서 제외한다.

예시:

```
projects/01_my_work/
├── 01_my_work_00_meta.md              작품 진행 메타 (이력 단일 진실)
├── 01_my_work_01_blueprint_rough.md   러프 청사진
├── 01_my_work_02_pitch_deck.md        피칭덱
├── 01_my_work_04_blueprint_full.md    완성 청사진
├── 05_episodes/                       회차 초안
├── 06_reviews/                        검토·패치 보고서
└── 07_final/
    └── 01_my_work_FINAL_v3.md         ★ 정본은 여기 한 개만
```

## 두 가지 원칙

1. **정본은 항상 `07_final/[작품]_FINAL_v{최신N}.md` 한 개.** 옛 버전은 `07_final/_archive_versions/` 로 즉시 옮긴다.
2. **메이저 수정 전에는 `v{N+1}` 로 복사한 뒤 고친다.** 원본을 직접 고치지 않는다.

작품을 새로 시작할 때 폴더를 직접 만들 필요는 없다 — Claude Code에 그냥 "새 작품 시작하자"고 말하면 절차대로 만들어준다.
