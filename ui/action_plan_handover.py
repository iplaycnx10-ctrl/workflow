import streamlit as st


def render_handover_benefit_card():
    st.markdown(
        """
        <div class="handover-card">
            <span class="action-kicker">HANDOVER BENEFIT</span>
            <h4>ทีมที่เข้าใจ Event และ Performance Ads สามารถต่อยอดระบบได้</h4>
            <p>
                เมื่อวาง LDP, Pixel, GA4 และ Event Structure ให้เป็นระบบกลางไว้แล้ว
                ทีมที่มีพื้นฐานด้าน Tracking และการบริหารแคมเปญบน Meta สามารถเข้ามาอ่านสัญญาณจากข้อมูลเดิมได้ง่ายขึ้น
                ทำให้การทำงานไม่ต้องเริ่มจากการเดาใหม่ทั้งหมด ลดความเสี่ยงจากการพึ่งคนทำงานคนเดียว
                และช่วยให้การปรับแคมเปญในอนาคตมีฐานข้อมูลรองรับมากกว่าเดิม
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
