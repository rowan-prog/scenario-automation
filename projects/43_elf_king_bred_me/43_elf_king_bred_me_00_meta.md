# 43_elf_king_bred_me — meta

- 원작: DramaWave 《Elf King Bred Me, Now He Hunts ME》(51화 · 사용자: DramaWave 일간 3위). 역대본 = `C:\Users\Rowan\scenario-automation\projects\43_elf_king_bred_me\reference\Elf King Bred Me, Now He Hunts ME.역대본.md`(2026-10-12 Downloads에서 복사) · 1~12화 축약본 `reference\elf_1_5.txt` `elf_6_12.txt`(긴 지문 줄 제거). 화자 라벨 흔들림 심함(인간여자·여자 = 여주 / 할머니·마가렛·모후 = 왕의 어머니).
- 원작 캐논(메인 정독 1~12화): 인간 노예 + 미약 취한 엘프왕 하룻밤 → 왕 흠모 귀족녀가 수명 100년 바쳐 예언 조작 → "다시 눈에 띄면 재로" 추방 → 10개월 뒤 숲에서 알로 출산(100년 만의 엘프 아기) → 혼혈 힘 폭주·봉인·기한 → 2년 뒤 복귀(오크 대사제 찾기) → 대비가 손주 그리워 차린 보육원에 친손주 맡김 · 칙령 "후계자 낳는 여자 = 왕비" → 츤데레 왕(하루 50번 묻기·몰래 길 일러 주기) · "남자 보러 온 건 맞는데 당신 아님" → 방의 아기 "설마?" → 젖·"보육원 아이" → 왕비 간택 무도회·아기 "아빠".
- 2026-10-12 러프 2안(무료 9화 · 원작 1~12): A = `43_elf_king_bred_me_p0_rough_A.md` **The Elf King Made Me Hatch My Own Stolen Egg**(그레이스·루카스·캐롤라인·마사·노아 · 한끗 = 귀족녀가 알을 훔쳐 왕비 · 알은 엄마 손에서만 금빛 · 알 품는 하녀 · 위협 = 덩굴로 숨통) / B = `_p0_rough_B.md` **I Hid His Heir, Then Entered the Elf King's Bride Trials**(해나·가브리엘·사브리나·이디스·핀·브렌다·거스 · 한끗 = 아들 숨긴 채 왕비 간택 참가 · 세계수 관문 · 핀 덩굴 무늬 · 위협 = 태워 죽인다).
- 원작 대사 근접 줄 메인 워싱(A 18곳·B 15곳 — 깨진 창문·50번 묻기·내 손주였으면·사람 잘못 보셨어요·이 손/이 다리·2년 후회 등) · name_leak PASS · logline_lint FAIL 0. 대비 노트 = 각 `_twist.md`.
## 2026-10-12 손보기 2차 (사용자: "재밌게·후킹·AI 문체 아니게" 점검 → "손봐. 정합성 오류(주체·객체 혼동·심각한 모순)까지")
- 편마다 opus 손보기 1기(AI 문체 걷기 · 말버릇 상한 · 정합성 장부) → sonnet 독립 정합성 검수 → 메인이 원문 확인 후 진짜만 반영 → plain-reader 2차 → opus 콜드리드(1화·마지막 무료 화) → 콜드리드 지적 문장 수정. 말버릇(천자당): 그순간·그때 0~0.7 · 것이다 0 · 모른다 0~1.0(모범 0.8/0.8/0.4).
- ⚠️ 작업 사고: PowerShell 단일 쌍 배열이 글자 단위로 풀려 5파일 글자 치환 → git 자동 커밋(2980dbf·dee9e0c)에서 복원 후 정확 일치 스크립트로 재적용. 이후 일괄 치환은 Python 정확 일치(횟수 1 확인)만.
- 묶음 = `C:\Users\Rowan\scenario-automation\projects\리메이크 러프 기획안 8종_v2.docx`(v1 보존).## 2026-10-13 top3 정돈 — B2 (사용자: 8종 v2 "장황·이해 안 감·제목/동사/설정 비직관·재미없음 → 원작 쉽게 레퍼런스 삼은 top3만 정돈")
- 산출 = `C:\Users\Rowan\scenario-automation\projects\43_elf_king_bred_me\43_elf_king_bred_me_p0_rough_B2.md` · **Secret Son at the Elf King's Bride Contest** · 노트 `_B2_twist.md` · 묶음 = `projects\리메이크 러프 기획안 top3.docx`. B·A 보존.
- 원칙 = 원작 1~12 흐름 그대로 + 한끗 하나(아들 살릴 수액 = 간택 마지막 관문까지 간 여자만 → 아들 숨긴 채 후보로). 관문 4 → 3(뿌리 꽃 · 우는 아기 · 무도회) · 묘목 관문·거스·브렌다·고양이족 이름 삭제.
- 작성 유닛이 원작 대사를 다시 옮긴 5줄(손주였으면·남자 보러 온 건 맞아요·2년 후회·이 손 기억·처음이에요) 메인 워싱. 5화 「살려야 할 남자」 뒤에 "가브리엘은 그 남자가 두 살배기 자기 아들인 줄 모른다" 추가.
- 게이트 = 화당 272~360자(B 370~704) · logline_lint PASS 3 · name_leak PASS · plain-reader 진짜 4건 수정.

## 2026-10-13 B3 뱀파이어판 (사용자: "Secret Son at the Elf King's Bride Contest 이게 원작이 엘프였으니 다른 걸로 바꾸고 … 더 디벨롭해. 타이틀도 후킹·내용 예상·매력·직관·쉽게")
- 산출 = `C:\Users\Rowan\scenario-automation\projects\43_elf_king_bred_me\43_elf_king_bred_me_p0_rough_B3.md` · **The Bride Hiding the Vampire King's Son** · 노트 `_B3_twist.md` · 묶음 = `projects\리메이크 러프 기획안 top3_v2.docx`. B2 보존.
- 세계 = 엘프 → 뱀파이어. 서브 레퍼런스 = 사내 히트작 「Owned by the Vampire King」(우선 8종)에서 두 가지만: 피를 바치는 인간 노예 · 왕을 닮은 금빛 눈(원작의 '왕가 정통 표시'로 쓰면 보육원에서 핀을 돌본 대비가 바로 알아야 해서 닮음으로만).
- 치환 = 미약 → 왕의 피 잔에 탄 약 · 세계수 예언 → 신전 예언(인간 여자가 왕의 피를 마시고 뱀파이어가 되려 한다) · 알 출산 삭제 · 덩굴 → 검은 핏줄(심장에 닿으면 죽음 · 막을 건 왕의 피뿐) · 나무 정령 → 숲속 늙은 산파 · 세계수 수액 → 왕의 피 한 잔 · 뿌리 흰 꽃 관문 → 왕가의 피로 만든 붉은 돌 · 우는 엘프 아기 → 이가 나서 무는 뱀파이어 아기.
- 디벨롭 = 거울(왕의 피를 노린 여자로 쫓겨난 해나가 이번엔 정말 왕의 피를 받으러 옴 — 아들 때문에) · 주인 행세(쫓아낸 노예라도 아직 자기 거) · 6화 목덜미 피 냄새에 송곳니. 메인 정합 수정 = 4화 손목 잡기 복원(5화 "손목을 놓지 않고"와 연결) · "도망친 노예" → "쫓아낸 노예".
- 게이트 = 화당 256~389자(평균 315) · logline_lint PASS 3 · name_leak PASS(원작 + 서브 레퍼런스 둘 다 · --allow Secret) · 작업어 0.
