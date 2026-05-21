import streamlit as st


def render_stability_plan_tab():
    st.markdown(
        """
        <div class="action-module stability-module">
            <span class="action-kicker">STEP 06 · LONG TERM STABILITY</span>
            <h3>ระบบอาจไม่ดันยอดทันที แต่จะเสถียรมากขึ้นระยะยาว</h3>
            <p class="action-lead">
                การวางระบบก่อน คือการสอนให้บัญชีเข้าใจว่าใครคือ Buyer จริง ไม่ใช่แค่ Viewer หรือคนทักง่าย
            </p>
            <div class="stability-grid">
                <div class="stability-box">ระบบเริ่มจำพฤติกรรมคนซื้อ</div>
                <div class="stability-box">Retarget แม่นขึ้น</div>
                <div class="stability-box">Scale ได้เสถียรกว่าเดิม</div>
                <div class="stability-box">ลดปัญหา Lead ไม่มีคุณภาพ</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
