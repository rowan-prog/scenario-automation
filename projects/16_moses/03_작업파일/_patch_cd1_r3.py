# -*- coding: utf-8 -*-
"""2026-09-23 r3 — 회차별 사실 대조 유닛(6기) 확정 불일치 반영. 실행 1회.
builder(_build_cd1_spec.py)와 카드 JSON(scratchpad cards_*.json) 중 문구가 있는 쪽을 교체."""
import io, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(HERE, "_build_cd1_spec.py")
s = io.open(p, encoding="utf-8").read()
if "r3 패치 적용됨" in s:
    raise SystemExit("already patched")
SP = r"C:/Users/Rowan/AppData/Local/Temp/claude/C--Users-Rowan/248b6693-79b5-4723-8457-6ea04d637ba9/scratchpad"
CARDS = {f: io.open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(SP, "cards_*.json"))}

def rep(old, new):
    global s
    if s.count(old) >= 1:
        s = s.replace(old, new, 1); return
    for f, t in CARDS.items():
        if t.count(old) >= 1:
            CARDS[f] = t.replace(old, new, 1); return
    raise AssertionError(old[:70])

# EP40 G 장면 순서
rep(r'''40: "모세가 다말의 손바닥 상처를 어루만지자 상처가 낫는다. 다말이 달려가 안기고 두 사람이 입을 맞춘다."''',
    r'''40: "다말이 달려가 안기고, 모세가 다말의 손바닥 상처를 어루만지자 상처가 낫는다. 두 사람이 입을 맞춘다."''')
# EP28 H 무릎 꿇림 주체 (카드 JSON)
rep('델릴라가 지하 감옥에 갇힌 다말을 찾아와 조롱하며 발을 씻기라 명령하고, 다말은 아버지를 살리기 위해 무릎 꿇고 델릴라의 발을 씻긴다.',
    '델릴라가 지하 감옥에 갇힌 다말을 찾아와 조롱하고, 하녀들이 다말을 무릎 꿇리자 다말은 아버지를 살리기 위해 델릴라의 발을 씻긴다.')
# EP29 H (카드 JSON)
rep('모세는 말없이 돌아서 사라졌다가,', '모세는 그대의 뜻을 존중하겠다며 돌아서 사라졌다가,')
# EP30 H 근위대장 (builder TREAT_FIX)
rep('    30: "왕궁 병사들이 광장에서 라반을 무릎 꿇리고 때리자', '    30: "광장에서 근위대장이 쇠사슬에 묶인 라반을 무릎 꿇리고 때리자')
# EP44 H 멱살 단수 (카드 JSON)
rep('붉은 바다 앞에 갇힌 백성들은 모세의 멱살을 잡고 원망을 쏟아내고, 다말이 나서서 사람들을 진정시킨다.',
    '붉은 바다 앞에 갇힌 백성 하나가 모세의 멱살을 잡고 원망을 쏟아내자, 다말이 나서서 사람들을 진정시킨다.')
# EP49 MKT 행 순서 (builder)
rep(r'''다말이 델릴라의 손목에서 대왕비의 팔찌를 빼내 웅덩이에 던진다. \"Give it back! That's the Great Royal Wife's bracelet!\" 다말이 귓가에 말한다.''',
    r'''다말이 델릴라의 손목에서 대왕비의 팔찌를 빼낸다. \"Give it back! That's the Great Royal Wife's bracelet!\" 다말이 팔찌를 웅덩이에 던지고 귓가에 말한다.''')
rep(r'''Tamar rips the Great Royal Wife's bracelet off her wrist and throws it into a puddle. \"Give it back! That's the Great Royal Wife's bracelet!\" Tamar bends to her ear:''',
    r'''Tamar rips the Great Royal Wife's bracelet off her wrist. \"Give it back! That's the Great Royal Wife's bracelet!\" Tamar throws it into a puddle and bends to her ear:''')
rep("塔玛从她手腕上扯下大王妃手镯扔进水洼。“还给我！那是大王妃的手镯！”塔玛俯身在她耳边说：",
    "塔玛从她手腕上扯下大王妃手镯。“还给我！那是大王妃的手镯！”塔玛把手镯扔进水洼，俯身在她耳边说：")
# 개요·인물 (builder)
rep('그리고 그때마다 왕궁에 재앙이 떨어진다. 이 작품에서 팔리는 그림은', '그리고 그 뒤에 왕궁에 재앙이 떨어진다. 이 작품에서 팔리는 그림은')
rep('And every time, a plague hits the palace. Every sellable image', 'And after each one, a plague hits the palace. Every sellable image')
rep('而每一次，灾祸都会降临王宫。本作所有能卖的画面', '而在那之后，灾祸便降临王宫。本作所有能卖的画面')
rep('다말이 다칠 때마다 재앙을 내려 갚고, 아내에게는', '다말이 괴롭힘을 당하면 재앙을 내려 갚고, 아내에게는')
rep('Every time Tamar is hurt he answers with a plague, and he only', 'When Tamar is hurt he answers with a plague, and he only')
rep('塔玛每受一次伤，他就降下灾祸偿还；', '塔玛受到欺凌，他便降下灾祸偿还；')
rep('그 밖의 키스는 23·40·50화.', '그 밖의 키스는 10화(이마)·23·40·50화.')
rep('Other kisses in EP23, EP40 and EP50.', 'Other kisses in EP10 (forehead), EP23, EP40 and EP50.')
rep('비둘기가 노예 구역으로 날아가자 다말을 쓸모없는 것이라 부르고, 혼인하는 순간 가문과 남남이라고 선언한다(EP5).',
    '비둘기가 노예 구역으로 날아가자(EP2) 다말을 쓸모없는 것이라 부르고(EP4), 혼인하는 순간 가문과 남남이라고 선언한다(EP5).')
rep("When the dove flies to the slaves' quarter he calls Tamar useless and declares her nothing to the family the moment she marries (EP5).",
    "When the dove flies to the slaves' quarter (EP2) he calls Tamar useless (EP4) and declares her nothing to the family the moment she marries (EP5).")
rep('鸽子飞向奴隶区后他骂塔玛没用，宣布她一旦成婚就与家族再无关系（第5集）。',
    '鸽子飞向奴隶区后（第2集）他骂塔玛没用（第4集），宣布她一旦成婚就与家族再无关系（第5集）。')
rep('전생에 다말을 왕비로 두고도 버린 남편이고, 이번 생에서는', '전생에 다말의 남편이었고, 이번 생에서는')
rep("In Tamar's last life he was the husband who made her queen and still threw her away; this time", "In Tamar's last life he was her husband; this time")
rep('前世他立塔玛为王妃却仍将她抛弃，这一世', '前世他是塔玛的丈夫，这一世')
# EP15 H 시늉 (카드 JSON)
rep('다말은 델릴라가 진짜로 펜던트를 불에 던지려 하자 걷겠다고 답한다.', '다말은 델릴라가 펜던트를 불에 던지는 시늉을 하자 걷겠다고 답한다.')
# EP16 MKT 행 상태 (builder)
rep('펜던트를 되찾으려 피투성이 손으로 바닥을 기는 다말의 턱을 델릴라가 잡고,', '피투성이 손으로 바닥을 기어 펜던트를 되찾은 다말의 턱을 델릴라가 잡고,')
rep("Tamar crawls across the floor with bloodied hands to get her pendant back. Delilah grabs her jaw", "Tamar crawls across the floor with bloodied hands and gets her pendant back. Delilah grabs her jaw")
rep('塔玛用血淋淋的双手在地上爬着去捡回吊坠，德莉拉掐住她的下巴', '塔玛用血淋淋的双手爬过地面捡回吊坠，德莉拉掐住她的下巴')
# EP17 H 순서·귀속 (카드 JSON)
rep('다말이 화상 입은 발을 보이며 정신을 잃으려 하자 모세는 누가 아내를 이렇게 만들었냐며 살기를 드러내고,', '다말이 정신을 잃으려 하자 모세가 화상 입은 발을 발견하고, 누가 아내를 이렇게 만들었냐며 살기를 드러내고,')
# EP18 G/H/B 순서 (builder)
rep(r'''18: "병사들이 델릴라와 파라오의 얼굴을 불길 앞으로 밀어 넣는다. \"Spare me! Anything but my face! Please, I'll do whatever you say!\"",''',
    r'''18: "병사들이 델릴라와 파라오를 불길 앞으로 끌고 간다. \"Spare me! Anything but my face! Please, I'll do whatever you say!\" 병사들이 두 사람의 얼굴을 불길 가까이로 밀어 넣는다.",''')
rep('병사들이 델릴라와 파라오의 얼굴을 불길 가까이로 밀어 넣자 델릴라는 얼굴만은 안 된다며 애원하고 파라오도 필사적으로 몸부림친다.',
    '델릴라와 파라오가 불길 앞으로 끌려가 얼굴만은 안 된다며 애원하고 몸부림치자, 병사들이 두 사람의 얼굴을 불길 가까이로 밀어 넣는다.')
rep(r'''병사들이 델릴라와 파라오의 얼굴을 다말이 걸었던 불길 앞으로 밀어 넣는다. 델릴라가 비명을 지른다. \"Spare me! Anything but my face! Please, I'll do whatever you say!\"",''',
    r'''병사들이 델릴라와 파라오를 다말이 걸었던 불길 앞으로 끌고 간다. 델릴라가 비명을 지른다. \"Spare me! Anything but my face! Please, I'll do whatever you say!\" 병사들이 두 사람의 얼굴을 불길 가까이로 밀어 넣는다.",''')
rep(r'''The soldiers shove Delilah's and Pharaoh's faces toward the same flames Tamar walked through. Delilah screams, \"Spare me! Anything but my face! Please, I'll do whatever you say!\"",''',
    r'''The soldiers drag Delilah and Pharaoh to the same flames Tamar walked through. Delilah screams, \"Spare me! Anything but my face! Please, I'll do whatever you say!\" Then the soldiers shove both faces toward the fire.",''')
rep('士兵把德莉拉和法老的脸推向塔玛走过的那条火路。德莉拉尖叫：“饶了我！别毁我的脸！求你，你说什么我都照做！”',
    '士兵把德莉拉和法老拖到塔玛走过的那条火路前。德莉拉尖叫：“饶了我！别毁我的脸！求你，你说什么我都照做！”随后士兵把两人的脸推向火焰。')

s = s.replace("TREAT_FIX = {  # 2026-09-23 패치 적용됨", "TREAT_FIX = {  # 2026-09-23 패치 적용됨 · r3 패치 적용됨", 1)
io.open(p, "w", encoding="utf-8").write(s)
for f, t in CARDS.items():
    io.open(f, "w", encoding="utf-8").write(t)
    io.open(os.path.join(HERE, os.path.basename(f)), "w", encoding="utf-8").write(t)
print("r3 patched")
