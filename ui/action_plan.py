import streamlit as st


def render_action_plan_module():
    st.markdown(
        """
        <div class="action-plan-placeholder">
            <span class="action-plan-kicker">ACTION PLAN</span>
            <h3>แผนปฏิบัติการ</h3>
            <p>พื้นที่สำหรับลงรายละเอียดแผนการทำงาน ขั้นตอนการยิงแอด ครีเอทีฟที่ต้องใช้ Timeline และ Checklist เพิ่มเติม</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
