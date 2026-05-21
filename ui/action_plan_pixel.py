import streamlit as st


def render_pixel_plan_tab():
    st.markdown(
        """
        <div class="action-module pixel-module">
            <span class="action-kicker">STEP 02 · PIXEL SIGNAL</span>
            <h3>ติด Meta Pixel เพื่อเก็บพฤติกรรมที่ใช้ยิงแอดต่อได้</h3>
            <p class="action-lead">
                Pixel ทำให้บัญชีเห็นพฤติกรรมหลังคลิก ไม่ใช่เห็นแค่คนดูวิดีโอหรือคนทักง่าย ช่วยแยกคนสนใจจริงออกจาก Viewer ทั่วไป
            </p>
            <div class="action-grid-2">
                <div class="action-mini-card"><b>ViewContent</b><br><span>รู้ว่าใครเข้า LDP และดูข้อมูลสินค้า</span></div>
                <div class="action-mini-card"><b>Offer / Price Intent</b><br><span>รู้ว่าใครเห็นราคา หรือสนใจโปรจริง</span></div>
                <div class="action-mini-card"><b>Click LINE / QR</b><br><span>รู้ว่าใครตั้งใจไปต่อเข้า LINE OA</span></div>
                <div class="action-mini-card"><b>Retarget Pool</b><br><span>เอา Signal ไปทำรีมาร์เก็ตติ้งต่อได้</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
