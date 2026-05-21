import streamlit as st


def render_case_plan_tab():
    st.markdown(
        """
        <div class="action-module case-module">
            <span class="action-kicker">STEP 05 · CASE STUDY</span>
            <h3>Case Start ที่ทำเสร็จได้ภายใน 1 วัน</h3>
            <p class="action-lead">
                เป้าหมายของเคสแรกไม่ใช่ยอดพุ่งทันที แต่คือพิสูจน์ว่าระบบเริ่มเก็บ Signal ได้จริง
            </p>
            <div class="timeline-card">
                <div><b>Day 1:</b> สร้าง/ปรับ LDP</div>
                <div><b>Day 1:</b> ติด Pixel + GA4</div>
                <div><b>Day 1:</b> ตั้ง Event พื้นฐาน</div>
                <div><b>Day 1:</b> ยิง Traffic Test เข้าเว็บ</div>
                <div><b>Day 1:</b> เริ่มเก็บข้อมูล Behavior ชุดแรก</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
