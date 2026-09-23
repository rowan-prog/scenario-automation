# -*- coding: utf-8 -*-
"""2026-09-23 외부 대조(1~50화) 반영 패치 — _build_cd1_spec.py 문자열 교체. 실행 1회."""
import io, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_build_cd1_spec.py")
s = io.open(p, encoding="utf-8").read()
if "2026-09-23 패치 적용됨" in s:
    raise SystemExit("already patched")

def rep(old, new):
    global s
    assert s.count(old) >= 1, old[:60]
    s = s.replace(old, new, 1)

# ---- keywords / scene
rep('4: ["파혼거절", "가문의절"]', '4: ["혼인수락선언", "가족경악"]')
rep('47: "갈라진 바다 사이 마른 길로 백성들이 걸어 들어간다. 마지막 수레가 지나자 왕실 전차들이 바다 밑바닥으로 쏟아져 들어온다."',
    '47: "갈라진 바다 사이 마른 길로 백성들이 걸어 들어간다. 마지막 수레가 바닷길에 들어서자 모래기둥이 사라지고 왕실 전차들이 뒤따라 쏟아져 들어온다."')

# ---- treatments
add = '''    1: "대왕비 책봉식에서 두루마리를 받아 든 다말의 등에 델릴라가 단검을 박아 넣는다. 델릴라는 3년 전 같은 날 새 날리기 의식에서 자신은 거지와 엮였는데 다말만 파라오를 얻었다며 울부짖고, 불기둥이 델릴라까지 집어삼켜 두 사람이 나란히 숨을 거둔다. 다말이 3년 전 새 날리기 의식 날 아침으로 돌아와 눈을 뜨고, 델릴라가 먼저 황금 새장의 매를 잡아 파라오에게 날려 보내는 것을 보며 델릴라도 같은 날로 돌아왔음을 알아챈다. 매가 파라오의 어깨에 앉고 가족들이 환호한다.",
    14: "델릴라가 펜던트를 돌려주는 조건으로 다말에게 가문 이름을 영원히 버리라고 요구하고, 라반은 지금부터 자기 딸은 델릴라 하나뿐이라고 선언한다. 다말이 신목 앞에서 가문과의 인연을 끊겠다고 맹세하지만 델릴라는 약속을 어기고 떠나는 자가 치러야 할 법도가 남았다고 말한다. 델릴라가 하인들에게 제단의 기름 먹인 장작을 가져오라 명령한다.",
    24: "델릴라가 화려한 장신구에 취해 웃다가, 장신구인 줄 알고 집어 든 것이 개구리라는 것을 알고 비명을 지르며 침상 위로 올라간다. 파라오는 개구리를 없애주면 노예를 풀어주겠다 약속하지만, 모세가 재앙을 거두자마자 약속을 깬다. 다말은 성소 봉사관에서 일을 시작하지만 하녀 우두머리 케네트가 그녀 발치에 더러운 빨랫감을 내던지며 텃세를 부린다.",
    30: "왕궁 병사들이 광장에서 라반을 무릎 꿇리고 때리자 다말이 몸부림치며 막아서지만, 파라오는 침묵하면 아비를 버리는 것이라 다그친다. 다말이 굴복하지 않겠다 외치자 하늘에서 거대한 우박이 쏟아지고, 라반을 때린 근위대장과 다말을 조롱한 델릴라만 정확히 맞아 쓰러진다. 군중이 신이 다말의 편이라 웅성거리자 파라오는 다말을 다시 지하 감옥에 가두라 명하고, 네페라가 다말에게 복수를 다짐한다.",
    31: "병사들이 다말을 지하 감옥으로 끌고 가던 중, 네페라가 가로막고 다말의 뺨을 때린다. 다말이 발의 상처 때문에 계단에서 굴러떨어져 이마가 찢어지고, 네페라는 치료를 막으며 다시는 나타나지 말라고 말한다. 새벽, 라반의 저택 외양간에서 가축들이 전부 다말과 같은 자리에 상처를 입은 채 죽어 있다. 네페라는 우연이라 되뇌며 두려움에 떤다.",
    35: "해가 사라지자 신관들이 태양신에게 불을 올리지만 신성한 불마저 꺼지고, 파라오의 얼굴에 처음으로 두려움이 스친다. 대왕비 자리에서 쫓겨난 델릴라는 거지 행색으로 거리를 헤매다 백성에게 침 뱉음을 당하고 절규한다. 어둠 속에서 다말은 손끝에 닿은 온기를 모세의 신이라 착각하고 남편을 지켜 달라 기도하며 눈물짓는다. 그 손이 다말의 손을 단단히 감싸는 순간, 파라오가 다말의 어깨를 잡아채 지하 감옥으로 끌고 간다.",
    40: "감독관 미리암이 다말에게 펜던트를 돌려주며 왕국의 학살령 때 갓난 동생을 갈대 바구니에 띄워 보낸 이야기를 들려주고, 다말은 그 아이가 모세이며 지하 감옥에서 느낀 온기의 주인도 모세였음을 알게 된다. 멀리서 모세가 다말을 부르고, 다말이 달려가 안기자 모세가 손바닥의 상처를 어루만져 낫게 하고 두 사람이 조심스럽게 키스한다. 그 시각 텅 빈 왕궁에서는 거지꼴이 된 델릴라가 파라오 앞에 무릎 꿇고, 왕의 권위에 도전한 자들에게 대가를 치르게 하라고 부추긴다.",
    41: "백성들이 사막을 행렬 지어 걷는 가운데, 다말은 대리석이 쏟아지던 날 자신들을 구한 바람을 떠올리며 그것이 신의 힘이었음을 깨닫는다. 밤이 되자 모래기둥이 사라지고 거대한 불기둥이 솟아올라 백성들의 길을 밝히고, 다말과 모세는 서로에게 기대어 그 광경을 지켜본다. 텅 빈 왕도에서 델릴라는 노예들이 왕의 재산을 통째로 훔쳐 달아났다며 파라오를 부추기고, 파라오는 왕국에 남은 마지막 군마를 전차에 매어 추격을 명령한다.",
    47: "갈라진 바다 사이로 길이 드러나고, 백성들은 놀라움과 기쁨 속에 마른땅을 밟으며 건너기 시작한다. 모세는 행렬의 맨 뒤를 지키며 모두가 지나갈 때까지 물벽을 지킨다. 마지막 짐수레가 바닷길에 들어서고 모세가 뒤따르자 모래기둥이 사라지고, 왕실 전차들이 마른 바다 밑바닥으로 쫓아 들어온다. 파라오는 한 사람도 놓치지 말라고 병사들에게 명령한다.",
'''
rep("TREAT_FIX = {\n", "TREAT_FIX = {  # 2026-09-23 패치 적용됨\n" + add)
rep('    2: "다말이 황금 새장에 손을 뻗자 델릴라가 가로막고 이번 생의 파라오는 자신이 갖겠다며 매를 낚아채 파라오에게 날린다. 매가 파라오의 어깨에 앉자 가족들은 델릴라의 혼사를 축하하며 다말을 비웃는다. 델릴라는 공사장 노예 무리 속에서 돌을 깨는 모세를 발견하고 낯빛이 굳는다. 다말이 아무도 없는 구역을 향해 비둘기를 날리자, 비둘기가 황금빛 모래에 싸여 노예 구역으로 날아간다.",',
    '    2: "가족들이 델릴라의 혼사를 축하하며 다말을 비웃는 사이, 델릴라는 공사장 노예 무리 속에서 돌을 깨는 모세를 발견하고 낯빛이 굳는다. 네페라는 다말에게도 파라오 가문에 걸맞은 배필을 고르라고 다그치고, 델릴라는 언니의 비둘기가 대단한 분에게 닿을 거라며 비꼰다. 다말이 아무도 없는 구역을 향해 비둘기를 날리자, 비둘기가 황금빛 모래에 싸여 노예 구역으로 날아간다. 라반이 머리카락을 쥐어 잡고 그쪽은 노예들이 일하는 곳이라고 소리친다.",')
rep('가족들 앞에서 다말이 신의 뜻이 아니라 자신의 선택이라며 파혼을 거절한다.',
    '가족들 앞에서 다말이 신의 뜻이 두려워서가 아니라 자신이 이 남자를 골랐다며 혼인을 받아들인다.')
rep('    42: "델릴라는 도망친 백성들이 왕국의 재산까지 가져갔다며 파라오를 부추기고, 파라오는 마지막 남은 군마와 전차를 끌어내 추격을 명령한다. 사막을 걷던 모세와 다말은',
    '    42: "파라오와 델릴라가 탄 왕실 전차들이 왕궁 문을 열고 사막으로 쏟아져 나온다. 사막을 걷던 모세와 다말은')

# ---- overview
rep('나를 때린 손, 나를 무릎 꿇린 발마다 개구리와 이와 우박이 정확히 그 사람에게만 떨어지는 것.',
    '나를 때린 손, 나를 무릎 꿇린 발에 개구리와 이와 우박이 되돌아오는 것.')
rep('Frogs, lice and hail landing on exactly the hand that hit you and the foot that made you kneel, and no one else.',
    'Frogs, lice and hail coming back down on the hand that hit you and the foot that made you kneel.')
rep('바다 가르기는 7화와 47화 두 번 있고, 7화 쪽은 지참금 굴욕 바로 뒤에 붙어 있다.',
    '바다 가르기는 7화, 그리고 46~47화의 바다 가르기와 도하까지 두 번 있고, 7화 쪽은 지참금 굴욕 바로 뒤에 붙어 있다.')
rep('The sea parts twice, in EP7 and EP47, and the EP7 one sits right after the dowry humiliation.',
    'The sea parts twice, in EP7 and again in EP46-47 with the crossing, and the EP7 one sits right after the dowry humiliation.')
rep(' NetShort <Swapped to a Beggar But He is Apollo> 시청층과 같은 자리.', '')
rep(" Same seat as NetShort's <Swapped to a Beggar But He is Apollo>.", '')
rep('NetShort <Swapped to a Beggar But He is Apollo>(48화)의 플롯 구조를 그대로 두고 모세와 출애굽 세계로 옮긴 각색. 대본은 한국어와 영어 병기. 노출과 정사는',
    'NetShort <Swapped to a Beggar But He is Apollo>(48화)를 모세와 출애굽 세계로 옮긴 각색. 노출과 정사는')
rep("An adaptation that keeps the plot of NetShort's <Swapped to a Beggar But He is Apollo> (48 EP) and moves it into a Moses / Exodus world. Script is bilingual KR/EN. One bedroom scene",
    "An adaptation of NetShort's <Swapped to a Beggar But He is Apollo> (48 EP) moved into a Moses / Exodus world. One bedroom scene")

# ---- cast
rep('남편의 정체를 모르는 채 뺨을 맞고, 맨발로 불 위를 걷고, 동생의 발을 씻기고, 목에 칼이 닿는 자리에서도 남편을 부르지 않는다. 그리고 그때마다 왕궁에 재앙이 떨어진다. 이 작품에서 팔리는 그림은 전부 이 인물이 당하는 자리와 그 뒤에 오는 되갚음에서 나온다.',
    '뺨을 맞고, 맨발로 불 위를 걷고, 동생의 발을 씻기고, 목에 칼이 닿는 자리에서도 남편을 부르지 않는다. 그리고 그때마다 왕궁에 재앙이 떨어진다. 이 작품에서 팔리는 그림은 전부 이 인물에게서 나온다.')
rep("Not knowing who he is, she gets slapped, walks barefoot over fire, washes her sister's feet and takes a blade to her throat without ever calling for him. And every time, a plague hits the palace. Every sellable image in this title comes from what is done to her and what comes back for it.",
    "She gets slapped, walks barefoot over fire, washes her sister's feet and takes a blade to her throat without ever calling for him. And every time, a plague hits the palace. Every sellable image in this title comes from her.")
rep("她不知道丈夫的真实身份，被打耳光、赤脚走火路、给妹妹洗脚、被刀抵住喉咙，也从不呼喊丈夫。而每一次，灾祸都会降临王宫。本作所有能卖的画面，全部来自她所受的屈辱和随之而来的偿还。",
    "她被打耳光、赤脚走火路、给妹妹洗脚、被刀抵住喉咙，也从不呼喊丈夫。而每一次，灾祸都会降临王宫。本作所有能卖的画面，全部来自这个人物。")
rep('다말이 날린 비둘기가 그의 지팡이에 앉는다. 혼례 날 지팡이를 들어 붉은 바다를 가르고(EP7), 다말이 낙인을 찍히기 직전 모래폭풍을 타고 나타나며(EP16), 다말을 괴롭힌 자들의 얼굴을 불 앞으로 밀어 넣는다(EP18). 다말이 다칠 때마다 우물이 피로 변하고, 개구리와 이와 우박이 떨어지고, 사흘 동안 해가 사라진다. 아내에게는 대언자라는 사실을 23화에서야 말한다. 마지막에 바다를 갈라 백성을 건너게 하고, 왕의 군대 위로 바다를 닫는다.',
    '다말이 날린 비둘기가 그의 지팡이에 앉는다. 다말이 다칠 때마다 재앙을 내려 갚고, 아내에게는 대언자라는 사실을 23화에서야 말한다. 혼례 날 붉은 바다를 갈라 다말을 데려가고(EP7), 마지막에 다시 바다를 갈라 백성을 건너게 한 뒤 왕의 군대 위로 바다를 닫는다(EP47~49).')
rep("Tamar's dove lands on his staff. On the wedding day he raises that staff and parts the Crimson Sea (EP7), rides a sandstorm in the instant before Tamar's face is branded (EP16), and has the faces of the people who hurt her shoved toward the fire (EP18). Each time Tamar is hurt, wells turn to blood, frogs, lice and hail fall, and the sun goes out for three days. He only tells his wife what he is in EP23. In the end he parts the sea for his people and closes it over the king's army.",
    "Tamar's dove lands on his staff. Every time Tamar is hurt he answers with a plague, and he only tells his wife what he is in EP23. On the wedding day he parts the Crimson Sea to take her home (EP7), and in the end he parts it again for his people and closes it over the king's army (EP47-49).")
rep("塔玛放出的鸽子落在了他的手杖上。婚礼当天他举杖分开红海（第7集），在塔玛即将被烙印的瞬间乘沙暴现身（第16集），把伤害她的人的脸推向火焰（第18集）。塔玛每受一次伤，井水就变血，青蛙、虱子、冰雹接连落下，太阳三天消失。他直到第23集才告诉妻子自己是谁。最后他分开大海让百姓渡过，再让海水合拢吞没王军。",
    "塔玛放出的鸽子落在了他的手杖上。塔玛每受一次伤，他就降下灾祸偿还；直到第23集才告诉妻子自己是谁。婚礼当天他分开红海带走塔玛（第7集），最后再次分开大海让百姓渡过，再让海水合拢吞没王军（第47~49集）。")
rep('다말의 어깨에 손톱을 박아 넣고(EP3), 펜던트를 미끼로 맨발로 불 위를 걷게 하고(EP15), 달군 낙인을 얼굴에 대고(EP16), 기절한 언니의 심장에 검을 내리찍고(EP21), 감옥에서 무릎 꿇려 발을 씻기고(EP28), 거울 조각을 목에 댄다(EP33). 그때마다 개구리와 이가 몸에 들러붙고 우박에 맞는다. EP34에서 파라오가 다말에게 대왕비 관을 내밀자 근위병에게 끌려 나가고, EP35에서 거지꼴로 거리를 헤매다 침 뱉음을 당한다. EP49에서 바다에 휩쓸린 뒤 진흙 속에서 다말의 발치까지 기어오고, 다말이 그 손목의 대왕비 팔찌를 빼내 웅덩이에 던진다. 죽지 못하고 살아서 대가를 치른다.',
    '펜던트를 미끼로 언니를 맨발로 불 위를 걷게 하고 달군 낙인을 얼굴에 대며(EP15~16), 감옥에서 무릎 꿇려 발을 씻긴다(EP28). 그때마다 개구리와 이가 몸에 들러붙고 우박에 맞는다. EP34에서 파라오가 다말에게 대왕비 관을 내밀자 근위병에게 끌려 나가고, EP49에서 바다에 휩쓸린 뒤 진흙 속에서 다말의 발치까지 기어오지만 다말이 그 손목의 대왕비 팔찌를 빼내 웅덩이에 던진다. 죽지 못하고 살아서 대가를 치른다.')
rep("She digs her nails into Tamar's shoulder (EP3), uses the pendant to make her walk barefoot over fire (EP15), holds a red-hot brand to her face (EP16), drives a sword at her unconscious sister's heart (EP21), makes her kneel and wash her feet in the dungeon (EP28) and presses a shard of mirror to her throat (EP33). Each time, frogs and lice crawl over her and hail hits her. In EP34 Pharaoh offers the crown to Tamar and the guards drag Delilah out; in EP35 she wanders the streets in rags and gets spat on. In EP49, washed up by the sea,",
    "She uses the pendant to make her sister walk barefoot over fire and holds a red-hot brand to her face (EP15-16), then makes her kneel and wash her feet in the dungeon (EP28). Each time, frogs and lice crawl over her and hail hits her. In EP34 Pharaoh offers the crown to Tamar and the guards drag Delilah out; in EP49, washed up by the sea,")
rep("她把指甲掐进塔玛的肩膀（第3集），用吊坠逼她赤脚走火路（第15集），把烧红的烙铁按向她的脸（第16集），朝昏迷的姐姐心口挥剑（第21集），在地牢里逼她跪下洗脚（第28集），用镜子碎片抵住她的喉咙（第33集）。每一次，青蛙和虱子都爬满她的身体，冰雹砸中她。第34集法老把大王妃的王冠递给塔玛，她被卫兵拖出王宫；第35集她衣衫褴褛流落街头被人吐口水。第49集",
    "她用吊坠逼姐姐赤脚走火路、把烧红的烙铁按向她的脸（第15~16集），又在地牢里逼她跪下洗脚（第28集）。每一次，青蛙和虱子都爬满她的身体，冰雹砸中她。第34集法老把大王妃的王冠递给塔玛，她被卫兵拖出王宫；第49集")
rep('다말의 턱을 잡아 올려 수작을 걸고(EP11), 낙인을 찍으라고 부추기고(EP16), 노예 해방을 약속하고는 개구리가 사라지자마자 말을 바꾼다(EP24). 라반을 광장에서 무릎 꿇려 때리게 하고(EP30), 다말과 라반의 처형을 명한다(EP36).',
    '다말의 얼굴에 낙인을 찍으라고 부추기고(EP16), 노예 해방을 약속하고는 개구리가 사라지자마자 말을 바꾸며, 다말과 라반의 처형을 명한다(EP36).')
rep("He lifts Tamar's chin and makes a pass at her (EP11), eggs on the branding (EP16), promises to free the slaves and breaks his word the moment the frogs are gone (EP24). He has Laban beaten on his knees in the square (EP30) and orders Tamar and Laban executed (EP36).",
    "He eggs on the branding of Tamar's face (EP16), promises to free the slaves and breaks his word the moment the frogs are gone, and orders Tamar and Laban executed (EP36).")
rep("他抬起塔玛的下巴调戏她（第11集），怂恿烙刑（第16集），答应释放奴隶却在青蛙一消失就翻脸（第24集）。他让拉班在广场上跪着挨打（第30集），下令处死塔玛和拉班（第36集）。",
    "他怂恿给塔玛的脸烙印（第16集），答应释放奴隶却在青蛙一消失就翻脸，又下令处死塔玛和拉班（第36集）。")
rep('"kr": "모세의 친누이. 성소의 감독관으로 위장해 모세를 돕는다.', '"kr": "모세의 친누이이자 성소의 감독관.')
rep("Moses' elder sister, posing as an overseer at the Sanctuary.", "Moses' elder sister and an overseer at the Sanctuary.")
rep("摩西的亲姐姐，伪装成圣所的监工协助摩西。", "摩西的亲姐姐，也是圣所的监工。")

# ---- reference
rep('"scenes": "새를 날려 배필을 정하는 의식에서 언니가 거지를 뽑는 자리(EP2~3). 혼례 날 지참금으로 망신을 당하던 신부 앞에 거지 신랑이 기적을 부리며 나타나는 자리(EP7). 아내는 남편의 정체를 모르는 채 굴욕을 당하고, 그때마다 남편의 힘이 상대에게 떨어지는 되갚음 루프. 같이 회귀한 동생이 끝까지 언니를 밟으려다 무너지는 자매 구도. 이 뼈대를 그대로 두고 아폴론을 예언자 모세로, 신의 권능을 열 가지 재앙과 바다 가르기로 바꿨다.",',
    '"scenes": "화관을 던져 배필을 정하는 의식에서 언니가 거지를 얻는 자리. 혼례 날 지참금으로 망신을 당하던 신부 앞에 거지 신랑 아폴론이 신의 권능을 드러내며 나타나는 자리. 아내는 남편의 정체를 모르는 채 굴욕을 당하고, 그때마다 남편의 힘이 상대에게 떨어지는 되갚음 루프. 같이 회귀한 동생이 끝까지 언니를 밟으려다 무너지는 자매 구도. 이 뼈대를 그대로 두고 화관을 비둘기로, 아폴론을 예언자 모세로, 신의 권능을 재앙과 바다 가르기로 바꿨다.",')
rep('"ad": "미확인. 원작 광고 소재는 Meta 광고 라이브러리에서 NetShort 계정으로 검색 가능.",', '"ad": "미확인.",')

# ---- MKT
rep('"axis": "여주를 건드린 그 사람에게만 재앙이 떨어진다 - 굴욕·되갚음"', '"axis": "여주를 건드린 자에게 재앙이 돌아온다 - 굴욕·되갚음"')
rep('모세는 맨 뒤에서 물벽을 지킨다. 마지막 짐수레가 지나자 모래기둥이 사라지고, 파라오의 전차들이 바다 밑바닥으로 쏟아져 들어온다.',
    '모세는 맨 뒤에서 물벽을 지킨다. 마지막 짐수레가 바닷길에 들어서고 모세가 뒤따르자 모래기둥이 사라지고, 파라오의 전차들이 바다 밑바닥으로 쫓아 들어온다.')
rep("The moment the last cart is through, the pillar of sand vanishes and Pharaoh's chariots pour down onto the seabed after them.",
    "As the last cart enters the road and Moses follows, the pillar of sand vanishes and Pharaoh's chariots pour down onto the seabed after them.")
rep("最后一辆货车刚过，沙柱消失，法老的战车倾泻而下冲进海底。",
    "最后一辆货车驶入海路、摩西跟上的那一刻，沙柱消失，法老的战车紧追着冲进海底。")

# ---- reuse fake: 3인칭 나레이션 추가 (컷1~3)
rep('\\n △ 파라오와 라반, 귀족들이 다말을 보며 웃는다."', '\\n △ 파라오와 라반, 귀족들이 다말을 보며 웃는다.\\n 나레이션VO: 혼례 날, 그녀가 고른 거지 남편은 오지 않았다."')
rep('\\n △ Pharaoh, Laban and the nobles laugh at Tamar."', '\\n △ Pharaoh, Laban and the nobles laugh at Tamar.\\n VO (Narrator): On her wedding day, the beggar she chose never came."')
rep('\\n △ 法老、拉班和贵族们看着塔玛大笑。"', '\\n △ 法老、拉班和贵族们看着塔玛大笑。\\n 旁白VO：婚礼当天，她选的乞丐丈夫没有来。"')
rep('불꽃이 발을 휘감고 얼굴이 고통으로 일그러진다."', '불꽃이 발을 휘감고 얼굴이 고통으로 일그러진다.\\n 나레이션VO: 버림받은 여자는 동생 앞에서 불 위를 걸었다."')
rep('Fire wraps around her feet and her face twists in agony."', 'Fire wraps around her feet and her face twists in agony.\\n VO (Narrator): The abandoned wife walked through fire in front of her sister."')
rep('火舌缠住她的脚，脸因剧痛而扭曲。"', '火舌缠住她的脚，脸因剧痛而扭曲。\\n 旁白VO：被抛弃的女人在妹妹面前走过了火路。"')
rep('I suppose that\'s what a beggar\'s wife does!\\""', 'I suppose that\'s what a beggar\'s wife does!\\"\\n 나레이션VO: 그리고 감옥에서, 동생의 발을 씻겼다."')
rep('MAID 1: \\"You look so used to this! I suppose that\'s what a beggar\'s wife does!\\""', 'MAID 1: \\"You look so used to this! I suppose that\'s what a beggar\'s wife does!\\"\\n VO (Narrator): And in the dungeon, she washed her sister\'s feet."')
rep('侍女1：“看你多熟练！乞丐老婆就是干这个的吧！”"', '侍女1：“看你多熟练！乞丐老婆就是干这个的吧！”\\n 旁白VO：然后在地牢里，她给妹妹洗了脚。"')

io.open(p, "w", encoding="utf-8").write(s)
print("patched")
