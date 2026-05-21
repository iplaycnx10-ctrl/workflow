import html

import streamlit as st


FOUNDATION_FIX_PIPE = [
    {
        "title": "Meta Ads",
        "body": "ยิงแอดเข้า LDP ก่อน ไม่ยิงเข้าแชทตรง ๆ เพื่อให้ระบบเริ่มเห็นพฤติกรรมก่อนเข้า LINE",
    },
    {
        "title": "LDP + Pixel",
        "body": "หน้า LDP มี Pixel คอยเก็บสัญญาณว่าใครคลิกเข้ามา อ่านข้อมูล เห็นราคา และสนใจ Offer จริง",
    },
    {
        "title": "QR / LINE CTA",
        "body": "ให้ลูกค้าสแกน QR หรือกดปุ่ม LINE จาก LDP หลังจากอ่านข้อมูลแล้ว เพื่อคัดคนที่มี Intent มากกว่าแค่ดูวิดีโอ",
    },
    {
        "title": "LINE OA",
        "body": "คนที่เข้า LINE จะเป็นกลุ่มที่ผ่านการอ่าน Offer มาแล้ว ทำให้แชทมีคุณภาพกว่า Lead ที่ทักจากแอดโดยตรง",
    },
    {
        "title": "Admin Close",
        "body": "Admin ปิดการขายต่อจาก Lead ที่ถูกกรองมาแล้ว และสามารถใช้ข้อมูลจาก LDP ช่วยอ่านคุณภาพลูกค้าได้ง่ายขึ้น",
    },
]


def render_foundation_fix_pipe(items=FOUNDATION_FIX_PIPE):
    st.markdown(
        '<div class="foundation-section-title">แนวทางแก้ไขเบื้องต้น: ปูฐานใหม่</div>'
        '<p class="foundation-section-desc">วางระบบใหม่ให้แอดส่งคนเข้า LDP ก่อน เพื่อให้ Pixel เก็บสัญญาณและใช้ LDP เป็นตัวกรอง Intent ก่อนส่งเข้า LINE OA</p>',
        unsafe_allow_html=True,
    )

    columns = st.columns([1, 0.06, 1, 0.06, 1, 0.06, 1, 0.06, 1])
    step_columns = [columns[0], columns[2], columns[4], columns[6], columns[8]]
    arrow_columns = [columns[1], columns[3], columns[5], columns[7]]

    for column, item in zip(step_columns, items):
        title = html.escape(item["title"])
        body = html.escape(item["body"])
        with column:
            st.markdown(
                f'<div class="foundation-step"><h4>{title}</h4><p>{body}</p></div>',
                unsafe_allow_html=True,
            )

    for column in arrow_columns:
        with column:
            st.markdown('<div class="foundation-arrow">→</div>', unsafe_allow_html=True)
