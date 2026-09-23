# -*- coding: utf-8 -*-
"""CD1 v4 in-place: B34·B17·C17 줄글 → 짧은 줄 (2026-09-23 사용자: 길고 장황하면 마케터가 안 읽는다)."""
import openpyxl
P = r"C:/Users/Rowan/scenario-automation/projects/16_moses/내 남편은 거지 모세_CD1 셀링 포인트_v4.xlsx"
SET = {
    "B34": "\n".join([
        "① 동생이 등을 떠밀어, 언니의 화관이 거지 음유시인 손에 떨어진다.",
        "② 지참금 망신을 당하는 혼례 날, 하늘에서 \"내 신부를 맞으러 왔다\".",
        "③ 그 거지가 빛의 신 아폴론이라는 걸 가족들이 먼저 알고 바닥에 엎드린다.",
        "④ 아내만 모른다. 시어머니 여신의 시험을 다 견딘 뒤에야 안다(44화).",
        "⑤ 언니를 해치려던 동생은 용암 감옥에 사슬로 묶인다(46화).",
        "각색: 화관은 비둘기로, 아폴론은 모세로, 신의 힘은 열 가지 재앙과 바다 가르기로 바꿨다. 모세·출애굽·열 가지 재앙은 서구권 시청자가 이미 아는 이야기다.",
    ]),
    "B17": "\n".join([
        "· 굴욕 바로 뒤에 되갚는 장면이 붙어 있다: 발 씻기 뒤 이 떼 / 라반 구타 뒤 우박 / 낙인 직전 모래폭풍 / 18화 델릴라·파라오 얼굴을 불길 앞으로.",
        "· 바다 가르기 두 번: 7화(지참금 망신 직후), 46~47화(백성이 건너는 장면).",
        "· 델릴라가 무너지는 장면 세 번: 34·35·49화.",
        "· 개구리·이 장면은 웃기게 쓰여 있다.",
    ]),
    "C17": "\n".join([
        "· Every humiliation is followed right away by payback: lice after the foot-washing / hail after Laban is beaten / a sandstorm right before the brand lands / EP18 Delilah and Pharaoh's faces dragged to the fire.",
        "· The sea parts twice: EP7 (right after the dowry humiliation) and EP46-47 (the people cross).",
        "· Delilah falls three times: EP34, EP35, EP49.",
        "· The frogs and lice scenes are written for laughs.",
    ]),
}
wb = openpyxl.load_workbook(P); ws = wb.worksheets[1]
for c, v in SET.items(): ws[c].value = v
wb.save(P); print("ok")
