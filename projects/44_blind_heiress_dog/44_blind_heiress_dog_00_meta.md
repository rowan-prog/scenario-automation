# 44_blind_heiress_dog — meta

- 원작: NetShort 《Don't Let The Blind Heiress's Dog Die》(40화 · 사용자: NetShort 랭킹 2위). 역대본 = `C:\Users\Rowan\scenario-automation\projects\44_blind_heiress_dog\reference\Don't Let The Blind Heiress's Dog Die.역대본.md`(2026-10-12 Downloads에서 복사) · 1~12화 축약본 `reference\dog_1_5.txt` `dog_6_12.txt`. 화자 라벨 흔들림 심함(Victim/Blind/Injured Woman = 여주 · Villain/Antagonist/Blonde/Carter Woman·Vance = 정부 · 6화 Max = 개).
- 원작 캐논(메인 정독 1~12화): 시각장애 상속녀가 결혼 3주년 서프라이즈로 공항 VIP 라운지 → 남편 정부·혼외 아들이 남편이 준 안내견을 레이저·커피·몽둥이 → "내 남편이 누군지 알아"(= 그녀 남편) · 블랙카드 글자 더듬기 → 상속녀라 밝혀도 "진짜 상속녀는 전용기에 경호원" → 남편 상장·50억 딜에 그녀 서명 필요 → 개가 차에 깔려 죽음 "못 봐서 아깝다" → 엔진·카트 → 비서실장이 시립병원에 가둠 → 병원 산소 끊기 → "리엄은 이미 결혼했어, 나랑" · 오빠·아버지 위성 추적.
- 2026-10-12 러프 2안(무료 9화 · 원작 1~12): A = `44_blind_heiress_dog_p0_rough_A.md` **The Blind Heiress Sees Everything**(오드리 웰스·마크 포스터·티파니·타일러·베어·닉·월터·딘 · 현대 뉴욕 유지 · 한끗 = 몰래 각막 수술, 처음 본 게 남편과 정부의 키스 · 계속 못 보는 척 · 일주일 안 머리 충격 = 영구 실명) / B = `_p0_rough_B.md` **The Blind Princess's Wolf Is a King**(아멜리아·사이먼 공작·모니카·토비·로건·윌리엄 왕 · 판타지 항구 왕국 · 한끗 = 안내 늑대가 저주받은 늑대 왕, 자정마다 사람으로 침대 곁을 지켰지만 그녀만 모름 · 9화 눈물에 사람으로 일어섬).
- 원작 대사 근접 줄 메인 워싱(A 15곳·B 7곳) · name_leak PASS(--allow Blind,Dog) · logline_lint PASS. 대비 노트 = 각 `_twist.md`.
## 2026-10-12 손보기 2차 (사용자: "재밌게·후킹·AI 문체 아니게" 점검 → "손봐. 정합성 오류(주체·객체 혼동·심각한 모순)까지")
- 편마다 opus 손보기 1기(AI 문체 걷기 · 말버릇 상한 · 정합성 장부) → sonnet 독립 정합성 검수 → 메인이 원문 확인 후 진짜만 반영 → plain-reader 2차 → opus 콜드리드(1화·마지막 무료 화) → 콜드리드 지적 문장 수정. 말버릇(천자당): 그순간·그때 0~0.7 · 것이다 0 · 모른다 0~1.0(모범 0.8/0.8/0.4).
- ⚠️ 작업 사고: PowerShell 단일 쌍 배열이 글자 단위로 풀려 5파일 글자 치환 → git 자동 커밋(2980dbf·dee9e0c)에서 복원 후 정확 일치 스크립트로 재적용. 이후 일괄 치환은 Python 정확 일치(횟수 1 확인)만.
- 묶음 = `C:\Users\Rowan\scenario-automation\projects\리메이크 러프 기획안 8종_v2.docx`(v1 보존).## 2026-10-13 top3 정돈 — A2 (사용자: 8종 v2 "장황·이해 안 감·제목/동사/설정 비직관·재미없음 → 원작 쉽게 레퍼런스 삼은 top3만 정돈")
- 산출 = `C:\Users\Rowan\scenario-automation\projects\44_blind_heiress_dog\44_blind_heiress_dog_p0_rough_A2.md` · **The Blind Heiress Sees Everything** · 노트 `_A2_twist.md` · 묶음 = `projects\리메이크 러프 기획안 top3.docx`. A·B 보존.
- 원칙 = 원작 1~12 흐름 그대로(현대 뉴욕 유지) + 한끗 하나(몰래 눈 수술 · 계속 못 보는 척). "일주일 안 머리 충격 = 영구 실명" 규칙·머리 감싸기·화재경보·헬기·렌치·배수로·반지 두 개·닉/월터/딘 이름 삭제. 원작 「못 봐서 아깝다」 = 오드리는 다 봤다(한끗이 살리는 순간).
- 원작 근접 줄 워싱(밥 흘린다·아이 싫다·가죽 북·500만 달러) · 「마크 포스터. 내 남편 이름이야」 화자 혼동·「약속이 쓰러져 있다」 비유 수정.
- 게이트 = 화당 297~379자(A 447~676) · logline_lint WARN(트롭 어휘 0 · 모델 Last Day도 같음) · name_leak PASS(--allow Blind,Dog) · plain-reader 진짜 8건 수정.

## 2026-10-14 러프 통과 → 작가(한국인) proposal + 원작 정식대본_KR
- 사용자: A2 러프 통과 · 작가용 proposal = 무료 트리트먼트·로그라인·타깃·목표·레퍼런스 변형 방향(스트릭트 말고 러프) + 메인/서브 레퍼런스(플랫폼+제목) · 메인 역대본 워싱(화자·장면 · 지문은 연결만 · 진짜 대본처럼) · 중국어 불필요.
- 서브 레퍼런스 = **FlexTV <Dangerous Blind Wife>**(2024.10 · 앞 못 보던 작가가 우연히 시력을 되찾고 숨긴 채 바람난 남편에게 복수) — top3 docx '참고한 히트작'에 있던 것. 메인 = NetShort <Don't Let The Blind Heiress's Dog Die>(40화).
- proposal = `44_blind_heiress_dog_writer_proposal.md` → `The Blind Heiress Sees Everything_작가 proposal.docx` (비글루 양식 아님 · 기본 정보 + 로그라인 + 목표 + 바꿔 봤으면 하는 것 7 + 무료 1~9화 트리트먼트 A2 글자 그대로). 원작 인물 이름은 역할로만(name_leak PASS).
- 원작 정식대본 = `reference/Don't Let The Blind Heiress's Dog Die.원작 정식대본_KR.md/.docx` (sonnet 9기 · 40화 115씬 · 원작 이름 그대로 · episode_number_check 오류 0). 메인 수정 2: 1화 S#5 차에서 내리는 흰 코트 여자 = 소피아(「오늘은 꼭 당신 이혼시키고 말 거야」 VO) · 8화 끝 「멈춰! 그 여자한테서 손 떼!」 = 라이언 OS(소피아가 돌아봄 · 9화 라이언 등장).
- 원작 13~40 흐름(유닛 보고): 13~17 병원 지하 고문·리엄이 아내일까 봐 병원행 · 18~19 리엄이 아내인 걸 알고도 도둑으로 몰아 보호소에 버림 · 20~22 헨리가 클라라 구출, 가스실 맥스 구출 · 23~26 상장식장(건물 = 싱클레어 소유) 정체 공개·지하실 감금 대가·위임장 위조 폭로 · 27~32 녹음 공개·자산 동결·체포(메이슨은 리엄 아들 아님 폭로) · 33~36 재판(소피아·라이언 종신 · 리엄 30년) · 37~40 면회 거절·소피아 교도소 폭행·메이슨 후견인·보호소 개관.
- 같은 날 2차(사용자: "너무 디테일하게 지시하지마" · "로그라인·트리트먼트 AI티만 빼" · "고수위 방향 넣어" · "~해주세요 문체 금지, 건조하게 명사형 불렛"): 변형 방향 7항 → 목표 2 + 바꾼 것 4 불렛 · `## 수위` 5불렛(고수위 가능·광고에 쓸 수 있게 / 노출 줄이기·암시 우회·장소 바꾸기 / 암시 단계 편집점 / 진입 직전 후킹 컷 / 광고 안 쓸 고수위 = 후반 보상) · 근거 = `Downloads\[UA+저수위+소재]+콘텐츠팀+제작+요청+가이드+(메타·틱톡+통합).doc`. 로그라인·트리트먼트 = opus 1기 AI 티 스윕(해설 "모른다" 4→2 · 복붙 꾸밈말 · 사물 주어 · 하늘길) + 메인 3곳(5화 마크 모름을 사건 문장 안으로 · 6화 베어 쓰러짐 중복 · 9화 의사 문장). 「」 대사·사건·화 경계 불변. 로그라인 152자 · name_leak PASS · plain-reader 진짜 3건 수정.
