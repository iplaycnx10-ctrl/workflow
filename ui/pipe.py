import html

import streamlit as st


ANDROMEDA_SIGNAL_PIPE = [
    {
        "title": "หลังใช้ Advantage+",
        "body": "ระบบเริ่มพึ่ง AI Optimization มากขึ้น แต่ Signal หลังบ้านยังไม่พร้อม ยอดเลยตก",
    },
    {
        "title": "Creative + Offer ต้องตอบโจทย์",
        "body": "เลยต้องไปพึ่ง Creative อย่างเดียว แล้ววัดเอาว่าราคาจะโดนกลุ่มลูกค้าไหม ปรากฏว่ากลุ่มลูกค้าที่ชอบ Creative กำลังซื้อไม่มี เลยปิดยาก",
    },
    {
        "title": "Pixel / Event ต้องส่งสัญญาณ",
        "body": "ระบบต้องรู้ว่าใครเห็นราคา กด LINE รับราคา และซื้อจริง แต่ตอนนี้ไม่ได้มีสัญญาณแยกให้ว่าลูกค้าไหนดีหรือไม่ดี",
    },
    {
        "title": "AI หา Buyer Pattern",
        "body": "เมื่อ Signal ดีขึ้น Retarget / Lookalike / Scale จะเริ่มแม่นขึ้น แต่ตอนนี้กลายเป็น AI หาแค่คนชอบดูวิดีโอมาให้มากกว่า",
    },
]


def render_pipe_steps(items=ANDROMEDA_SIGNAL_PIPE):
    columns = st.columns([1, 0.07, 1, 0.07, 1, 0.07, 1])
    step_columns = [columns[0], columns[2], columns[4], columns[6]]
    arrow_columns = [columns[1], columns[3], columns[5]]

    for column, item in zip(step_columns, items):
        title = html.escape(item["title"])
        body = html.escape(item["body"])
        with column:
            st.markdown(
                f'<div class="minimal-step"><h4>{title}</h4><p>{body}</p></div>',
                unsafe_allow_html=True,
            )

    for column in arrow_columns:
        with column:
            st.markdown('<div class="minimal-arrow">→</div>', unsafe_allow_html=True)
