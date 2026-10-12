# 44_blind_heiress_dog — meta

- 원작: NetShort 《Don't Let The Blind Heiress's Dog Die》(40화 · 사용자: NetShort 랭킹 2위). 역대본 = `C:\Users\Rowan\scenario-automation\projects\44_blind_heiress_dog\reference\Don't Let The Blind Heiress's Dog Die.역대본.md`(2026-10-12 Downloads에서 복사) · 1~12화 축약본 `reference\dog_1_5.txt` `dog_6_12.txt`. 화자 라벨 흔들림 심함(Victim/Blind/Injured Woman = 여주 · Villain/Antagonist/Blonde/Carter Woman·Vance = 정부 · 6화 Max = 개).
- 원작 캐논(메인 정독 1~12화): 시각장애 상속녀가 결혼 3주년 서프라이즈로 공항 VIP 라운지 → 남편 정부·혼외 아들이 남편이 준 안내견을 레이저·커피·몽둥이 → "내 남편이 누군지 알아"(= 그녀 남편) · 블랙카드 글자 더듬기 → 상속녀라 밝혀도 "진짜 상속녀는 전용기에 경호원" → 남편 상장·50억 딜에 그녀 서명 필요 → 개가 차에 깔려 죽음 "못 봐서 아깝다" → 엔진·카트 → 비서실장이 시립병원에 가둠 → 병원 산소 끊기 → "리엄은 이미 결혼했어, 나랑" · 오빠·아버지 위성 추적.
- 2026-10-12 러프 2안(무료 9화 · 원작 1~12): A = `44_blind_heiress_dog_p0_rough_A.md` **The Blind Heiress Sees Everything**(오드리 웰스·마크 포스터·티파니·타일러·베어·닉·월터·딘 · 현대 뉴욕 유지 · 한끗 = 몰래 각막 수술, 처음 본 게 남편과 정부의 키스 · 계속 못 보는 척 · 일주일 안 머리 충격 = 영구 실명) / B = `_p0_rough_B.md` **The Blind Princess's Wolf Is a King**(아멜리아·사이먼 공작·모니카·토비·로건·윌리엄 왕 · 판타지 항구 왕국 · 한끗 = 안내 늑대가 저주받은 늑대 왕, 자정마다 사람으로 침대 곁을 지켰지만 그녀만 모름 · 9화 눈물에 사람으로 일어섬).
- 원작 대사 근접 줄 메인 워싱(A 15곳·B 7곳) · name_leak PASS(--allow Blind,Dog) · logline_lint PASS. 대비 노트 = 각 `_twist.md`.
## 2026-10-12 손보기 2차 (사용자: "재밌게·후킹·AI 문체 아니게" 점검 → "손봐. 정합성 오류(주체·객체 혼동·심각한 모순)까지")
- 편마다 opus 손보기 1기(AI 문체 걷기 · 말버릇 상한 · 정합성 장부) → sonnet 독립 정합성 검수 → 메인이 원문 확인 후 진짜만 반영 → plain-reader 2차 → opus 콜드리드(1화·마지막 무료 화) → 콜드리드 지적 문장 수정. 말버릇(천자당): 그순간·그때 0~0.7 · 것이다 0 · 모른다 0~1.0(모범 0.8/0.8/0.4).
- ⚠️ 작업 사고: PowerShell 단일 쌍 배열이 글자 단위로 풀려 5파일 글자 치환 → git 자동 커밋(2980dbf·dee9e0c)에서 복원 후 정확 일치 스크립트로 재적용. 이후 일괄 치환은 Python 정확 일치(횟수 1 확인)만.
- 묶음 = `C:\Users\Rowan\scenario-automation\projects\리메이크 러프 기획안 8종_v2.docx`(v1 보존).