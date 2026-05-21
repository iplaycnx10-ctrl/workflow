import streamlit as st


def render_risk_fix_summary():
    st.markdown(
        """
        <div class="risk-fix-wrap">
            <div class="risk-fix-card risk-card">
                <span class="risk-fix-kicker">IF NOT FIXED</span>
                <h4>หากไม่แก้ระบบ Signal</h4>
                <p>
                    ระบบจะยังต้องวัดดวงกับ <b>CI + Offer</b> ว่าจะดึงคนที่มีกำลังซื้อเข้ามาถูกกลุ่มหรือไม่
                    แนวโน้มคือแคมเปญจะเสี่ยงกับเรื่อง <b>ราคาและกำลังซื้อ</b> เป็นหลัก ถ้าคนที่ชอบ Creative
                    ไม่พร้อมจ่าย Admin ก็จะปิดการขายยาก และบัญชีอาจจำพฤติกรรม Lead คุณภาพต่ำซ้ำไปเรื่อย ๆ
                </p>
            </div>
            <div class="risk-fix-card manual-card">
                <span class="risk-fix-kicker">SHORT-TERM FIX</span>
                <h4>แก้เบื้องต้นด้วย Manual Ads</h4>
                <p>
                    ระยะสั้นสามารถลองยิงแอดแบบ <b>Manual</b> และระบุกลุ่ม Interest เอง เพื่อคุมคุณภาพกลุ่มเป้าหมายมากขึ้น
                    แต่ยังมีความเสี่ยงที่ค่าโฆษณาจะแพง เพราะบัญชีอาจยังจำพฤติกรรมเดิมจากกลุ่มที่ชอบดูวิดีโอหรือทักง่ายอยู่
                </p>
            </div>
            <div class="risk-fix-card system-card">
                <span class="risk-fix-kicker">SYSTEM FIX</span>
                <h4>ปูฐานใหม่ด้วย LDP + Pixel + CAPI</h4>
                <p>
                    ควรเปลี่ยนเว็บเพจให้รองรับ <b>Meta Pixel</b> และผูก <b>CAPI</b> เพื่อส่งสัญญาณจากฝั่ง Server กลับเข้า Meta
                    ลดปัญหาข้อมูลหายจากข้อจำกัด Privacy / Cookie / iOS และช่วยให้ระบบเรียนรู้ว่าใครเห็นราคา กด LINE
                    รับ Offer และมี Intent ซื้อจริงได้ชัดขึ้น
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
