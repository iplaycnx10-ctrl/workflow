import streamlit as st


def render_dropoff_plan_tab():
    st.markdown(
        """
        <div class="action-module dropoff-module">
            <span class="action-kicker">STEP 04 · DROP-OFF ANALYSIS</span>
            <h3>วิเคราะห์จุดหลุดเพื่อปรับโฆษณา</h3>
            <p class="action-lead">
                เมื่อมี Pixel + GA4 ทีมจะเริ่มรู้ว่าคนหลุดตรงไหน แล้วเอากลับไปแก้ Hook, Offer, ราคา และ CTA ได้แม่นขึ้น
            </p>
            <div class="dropoff-flow">
                <div class="dropoff-node">เข้าเว็บเยอะ</div>
                <div class="dropoff-arrow">→</div>
                <div class="dropoff-node">ไม่กด LINE</div>
                <div class="dropoff-arrow">→</div>
                <div class="dropoff-node">อาจติด Offer / Trust / ราคา</div>
                <div class="dropoff-arrow">→</div>
                <div class="dropoff-node">นำข้อมูลไปปรับ Creative</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
