import streamlit as st


def render_ldp_plan_tab():
    st.markdown(
        """
        <div class="action-module ldp-module">
            <span class="action-kicker">STEP 01 · LDP FOUNDATION</span>
            <h3>ปรับ LDP ให้เป็นหน้ากรอง Intent ก่อนเข้า LINE</h3>
            <p class="action-lead">
                เปลี่ยนเส้นทางจากยิงแอดเข้าแชทตรง เป็นยิงเข้า Landing Page ก่อน เพื่อให้ลูกค้าเห็นข้อมูลสำคัญครบก่อนตัดสินใจกด LINE หรือสแกน QR
            </p>
            <div class="action-flow-row">
                <div class="action-flow-card"><b>Meta Ads</b><br><span>ยิง Traffic เข้า LDP</span></div>
                <div class="action-flow-arrow">→</div>
                <div class="action-flow-card"><b>LDP</b><br><span>ราคา / Offer / รีวิว / FAQ</span></div>
                <div class="action-flow-arrow">→</div>
                <div class="action-flow-card"><b>LINE CTA</b><br><span>กด LINE หรือสแกน QR</span></div>
            </div>
            <p>
                LDP จะทำหน้าที่เป็นด่านกรองลูกค้าเบื้องต้น คนที่อ่านข้อมูลแล้วค่อยกด LINE จะมี Intent สูงกว่าคนที่ทักจากแอดเพราะเห็นครีเอทีฟเฉย ๆ
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
