import streamlit as st


def render_ldp_plan_tab():
    st.markdown(
        """
        <style>
        .ldp-board{background:radial-gradient(circle at top left,#dbeafe 0,transparent 34%),radial-gradient(circle at bottom right,#dcfce7 0,transparent 30%),linear-gradient(135deg,#ffffff,#f8fafc);border:1px solid #e2e8f0;border-radius:30px;padding:28px;margin-top:18px;box-shadow:0 20px 52px rgba(15,23,42,.07)}
        .ldp-kicker{display:inline-flex;width:fit-content;padding:7px 12px;border-radius:999px;background:#dbeafe;color:#1d4ed8;border:1px solid #bfdbfe;font-size:12px;font-weight:900;letter-spacing:.06em;margin-bottom:12px}
        .ldp-title{font-size:34px;line-height:1.18;letter-spacing:-.045em;color:#0f172a;font-weight:950;margin:0 0 10px}.ldp-lead{font-size:15px;line-height:1.85;color:#475569;max-width:980px;margin:0 0 22px}
        .ldp-flow{display:grid;grid-template-columns:1fr 56px 1fr 56px 1fr;gap:12px;align-items:stretch;margin:22px 0}.ldp-card{background:rgba(255,255,255,.82);border:1px solid #dbeafe;border-radius:22px;padding:20px;min-height:150px;box-shadow:0 14px 34px rgba(15,23,42,.055)}.ldp-card-icon{font-size:30px;margin-bottom:8px}.ldp-card h4{font-size:19px;color:#0f172a;margin:0 0 8px;letter-spacing:-.02em}.ldp-card p{font-size:13.5px;color:#475569;line-height:1.65;margin:0}.ldp-arrow{display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:34px;font-weight:950}
        .ldp-note{background:linear-gradient(90deg,#eff6ff,#f0fdf4);border:1px solid #bfdbfe;border-radius:22px;padding:18px 20px;margin-top:18px}.ldp-note h4{font-size:18px;color:#0f172a;margin:0 0 6px}.ldp-note p{font-size:14px;color:#475569;line-height:1.75;margin:0}
        @media(max-width:900px){.ldp-flow{grid-template-columns:1fr}.ldp-arrow{min-height:24px;transform:rotate(90deg)}}
        </style>
        <div class="ldp-board">
            <div class="ldp-kicker">STEP 01 · LDP FOUNDATION</div>
            <div class="ldp-title">ปรับ LDP ให้เป็นหน้ากรอง Intent ก่อนเข้า LINE</div>
            <p class="ldp-lead">
                เปลี่ยนเส้นทางจากยิงแอดเข้าแชทตรง เป็นยิงเข้า Landing Page ก่อน เพื่อให้ลูกค้าเห็นราคา Offer รีวิว FAQ และเหตุผลที่ควรซื้อให้ครบก่อนกด LINE หรือสแกน QR
            </p>
            <div class="ldp-flow">
                <div class="ldp-card">
                    <div class="ldp-card-icon">📣</div>
                    <h4>Meta Ads</h4>
                    <p>ยิง Traffic เข้า LDP เพื่อให้ระบบเริ่มเห็นพฤติกรรมหลังคลิก ไม่ใช่เห็นแค่คนดูวิดีโอหรือคนทักง่าย</p>
                </div>
                <div class="ldp-arrow">→</div>
                <div class="ldp-card">
                    <div class="ldp-card-icon">🧾</div>
                    <h4>LDP + ข้อมูลขาย</h4>
                    <p>รวมราคา Offer รีวิว FAQ วิธีใช้ และ Trust proof เพื่อคัดคนที่สนใจจริงก่อนเข้า LINE</p>
                </div>
                <div class="ldp-arrow">→</div>
                <div class="ldp-card">
                    <div class="ldp-card-icon">💬</div>
                    <h4>LINE CTA / QR</h4>
                    <p>คนที่อ่านข้อมูลแล้วกด LINE หรือสแกน QR จะมี Intent สูงกว่าคนที่ทักจากแอดเพราะเห็น Creative เฉย ๆ</p>
                </div>
            </div>
            <div class="ldp-note">
                <h4>บทบาทของ LDP</h4>
                <p>LDP คือด่านกรองลูกค้าเบื้องต้นและเป็นจุดเริ่มเก็บ Signal ให้ระบบรู้ว่าใครสนใจจริง เห็นราคาแล้วไปต่อ และพร้อมเข้าสู่บทสนทนากับ Admin มากกว่าเดิม</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
