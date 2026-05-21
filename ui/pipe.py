import html

import streamlit as st


ANDROMEDA_SIGNAL_PIPE = [
    {
        "title": "หลังใช้ Advantage+ (อันโดเมด้า)",
        "body": "ยอดลดลง เพราะ AI หาคนชอบดูวิดีโอที่กำลังซื้อไม่มีมาให้มากกว่า",
    },
    {
        "title": "ต้องพึ่ง OFFER อย่างเดียว",
        "body": "ปรากฏว่ากลุ่มที่ได้กำลังซื้อไม่มี เลยกลายเป็น Lead ไม่มีคุณภาพ",
    },
    {
        "title": "Pixel / Event ต้องส่งสัญญาณ",
        "body": "Pixel ที่ติดมากับ 3rd Party ไม่ได้ทำงาน ไม่ได้ช่วยบัญชีในการหาลูกค้าหรือคัดลูกค้า",
    },
    {
        "title": "AI หา Viewer กำลังซื้อน้อยมาให้",
        "body": "Admin เลยปิดการขายยาก",
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
