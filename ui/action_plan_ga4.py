import streamlit as st


def render_ga4_plan_tab():
    st.markdown(
        """
        <div class="action-module ga4-module">
            <span class="action-kicker">STEP 03 · GA4 ANALYTICS</span>
            <h3>เชื่อม GA4 เพื่อวิเคราะห์พฤติกรรมเชิงลึก</h3>
            <p class="action-lead">
                GA4 ช่วยดูจุด Drop-off และ Behavior ของลูกค้าในหน้าเว็บ เพื่อเอากลับไปปรับ Creative, Offer และ Funnel ให้แม่นขึ้น
            </p>
            <ul class="action-list">
                <li>ดูว่าคนออกจากหน้าไหนมากที่สุด</li>
                <li>วัดเวลาที่อยู่ในหน้า</li>
                <li>ดู Scroll Depth และปุ่มที่ถูกกด</li>
                <li>วิเคราะห์ว่า Offer ไหนทำให้คนไปต่อ</li>
                <li>เปรียบเทียบคุณภาพ Traffic จากแต่ละ Campaign</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
