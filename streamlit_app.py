import streamlit as st

# =========================================================
# 00_APP_CONFIG_MODULE
# =========================================================
st.set_page_config(
    page_title="ลูกอมบุหรี่ | Work Flow Board",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def render_theme():
    st.markdown(
        """
        <style>
        :root {
            --bg: #fbfbfe;
            --card: #ffffff;
            --ink: #1f2937;
            --muted: #6b7280;
            --line: #edf0f7;
            --blue: #dbeafe;
            --blue-text: #1d4ed8;
            --lavender: #ede9fe;
            --lavender-text: #6d28d9;
            --mint: #dcfce7;
            --mint-text: #15803d;
            --pink: #fce7f3;
            --pink-text: #be185d;
            --amber: #fef3c7;
            --amber-text: #b45309;
        }
        .stApp { background: radial-gradient(circle at top left, #fdf2f8 0, transparent 28%), radial-gradient(circle at top right, #dbeafe 0, transparent 26%), var(--bg); color: var(--ink); }
        [data-testid="stSidebar"] { display: none; }
        .main .block-container { padding-top: 2.2rem; max-width: 1280px; }
        .module-wrap { background: rgba(255,255,255,0.48); border: 1px solid rgba(237,240,247,0.95); border-radius: 30px; padding: 22px 22px 26px; margin: 28px 0; box-shadow: 0 18px 48px rgba(31,41,55,0.035); }
        .module-head { display:flex; align-items:center; justify-content:space-between; gap:16px; margin-bottom: 16px; }
        .module-title { font-size: 14px; font-weight: 850; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin: 0; }
        .module-desc { color: var(--muted); font-size: 13px; line-height:1.55; margin: 4px 0 0; }
        .hero, .card, .mini-card, .persona-card, .test-card, .insight-card, .ci-card, .traffic-card, .pipe-card, .flow-node, .merge-node, .budget-card { background: rgba(255,255,255,0.9); border: 1px solid var(--line); box-shadow: 0 12px 36px rgba(31,41,55,0.045); }
        .hero { border-radius: 28px; padding: 28px 30px; margin-bottom: 20px; }
        .eyebrow { display: inline-flex; padding: 7px 12px; border-radius: 999px; background: #f8fafc; border: 1px solid var(--line); color: var(--muted); font-size: 13px; margin-bottom: 12px; }
        .title { font-size: 38px; font-weight: 850; letter-spacing: -0.04em; margin: 0; color: var(--ink); }
        .subtitle { color: var(--muted); font-size: 16px; margin-top: 8px; line-height: 1.7; }
        .flow-line { height: 3px; border-radius: 99px; background: linear-gradient(90deg, #bfdbfe, #ddd6fe, #bbf7d0); margin: 12px 0 20px 0; }
        .card { border-radius: 24px; padding: 22px; min-height: 270px; height: auto; overflow: visible; }
        .card h3, .mini-card h4, .persona-card h3, .test-card h4, .insight-card h4, .ci-card h3, .traffic-card h4, .pipe-card h4, .flow-node h4, .merge-node h4, .budget-card h4 { margin: 0 0 8px 0; letter-spacing: -0.02em; color: var(--ink); }
        .card p, .card li, .mini-card p, .persona-card p, .persona-card li, .test-card p, .insight-card p, .ci-card p, .ci-card li, .traffic-card p, .traffic-card li, .pipe-card p, .pipe-card li, .flow-node p, .merge-node p, .flow-node li, .merge-node li, .budget-card p, .budget-card li { color: var(--muted); line-height: 1.62; font-size: 14px; }
        .pill { display: inline-block; padding: 7px 11px; border-radius: 999px; font-size: 12px; font-weight: 750; margin-bottom: 12px; }
        .top { background: var(--blue); color: var(--blue-text); }
        .mid { background: var(--lavender); color: var(--lavender-text); }
        .bot { background: var(--mint); color: var(--mint-text); }
        .pink { background: var(--pink); color: var(--pink-text); }
        .amber { background: var(--amber); color: var(--amber-text); }
        .budget-card { border-radius: 20px; padding: 18px; min-height: 190px; }
        .budget-number { font-size: 30px; font-weight: 900; letter-spacing: -0.04em; color: var(--ink); margin: 2px 0 10px; }
        .arrow-row { display: flex; align-items: center; justify-content: center; min-height: 270px; margin: 0; color: #c4c9d4; font-size: 30px; font-weight: 800; }
        .mini-card, .persona-card, .test-card, .insight-card, .ci-card, .traffic-card, .pipe-card, .flow-node, .merge-node { border-radius: 20px; padding: 18px; }
        .persona-card, .unknown-card { min-height: 405px; height: auto; overflow: visible; }
        .placeholder { border: 1.5px dashed #cbd5e1; background: rgba(248,250,252,0.65); border-radius: 20px; padding: 18px; min-height: 190px; height: auto; overflow: visible; }
        .mini-card { min-height: 175px; height: auto; overflow: visible; }
        .insight-card { min-height: 160px; margin-top: 18px; overflow: visible; }
        .mid-target-card { min-height: 260px; }
        .ci-card { min-height: 390px; margin-top: 18px; }
        .traffic-card { min-height: 210px; }
        .pipe-card { min-height: 210px; background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(248,250,252,0.88)); }
        .ci-meta { display:grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 12px 0; }
        .ci-meta div { background:#f8fafc; border:1px solid var(--line); border-radius:14px; padding:10px; color:var(--muted); font-size:13px; line-height:1.45; }
        .visual-flow { margin-top: 18px; padding: 22px; border-radius: 26px; background: rgba(255,255,255,0.66); border: 1px solid var(--line); }
        .flow-node { min-height: 170px; }
        .merge-node { min-height: 190px; background: linear-gradient(180deg, #ffffff, #f8fafc); }
        .pipe-down { height: 34px; display:flex; align-items:center; justify-content:center; color:#94a3b8; font-size:30px; font-weight:900; }
        .pipe-h { height: 4px; border-radius: 999px; background: linear-gradient(90deg, #fbcfe8, #bfdbfe); margin: 15px 0; }
        .pipe-v { width: 4px; height: 34px; border-radius: 999px; background:#cbd5e1; margin: 0 auto; }
        .pipe-arrow { display:flex; align-items:center; justify-content:center; color:#c4c9d4; font-size:30px; font-weight:900; min-height:210px; }
        .person-icon { font-size: 42px; margin-bottom: 8px; }
        .unknown-card { border: 1.5px dashed #cbd5e1; background: rgba(248,250,252,0.72); border-radius: 20px; padding: 18px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; box-shadow: 0 12px 36px rgba(31,41,55,0.025); }
        .unknown-mark { font-size: 58px; font-weight: 900; color:#94a3b8; line-height:1; margin-bottom: 10px; }
        .footer-note { color: var(--muted); text-align: center; padding: 20px 0 6px; font-size: 13px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def open_module(title: str, desc: str):
    st.markdown(f"""<div class="module-wrap"><div class="module-head"><div><div class="module-title">{title}</div><p class="module-desc">{desc}</p></div></div>""", unsafe_allow_html=True)


def close_module():
    st.markdown("</div>", unsafe_allow_html=True)


def render_header():
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">🍬 Project Board · White Pastel Minimal · Modular-safe</div>
            <h1 class="title">ลูกอมบุหรี่ — TOP Funnel CI Workflow</h1>
            <div class="subtitle">
                TOP ใช้สร้าง Pain และ Persona ส่วน MID ใช้ต่อซีรีส์เดิมเพื่อ Retarget คนที่อินแล้ว<br>
                เป้าหมายคือพาเขาไปสู่บทสนทนา รีวิว และ Line OA ก่อนปิดการขาย
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_budget_plan():
    open_module("00_BUDGET_AND_AD_MANAGEMENT_PLAN", "งบเฉลี่ยสำหรับเริ่มยิงและแผนแบ่งงบตอน Manage Ads")
    b1, b2, b3, b4 = st.columns(4)
    with b1:
        st.markdown("""<div class="budget-card"><span class="pill top">TOTAL TEST BUDGET</span><h4>งบเฉลี่ยเริ่มต้น</h4><div class="budget-number">1,600–3,000฿</div><p>ใช้เป็นงบทดสอบ Funnel ชุดแรก เพื่อดูว่า CI ไหนสร้าง signal ดีพอจะ Retarget ต่อ</p></div>""", unsafe_allow_html=True)
    with b2:
        st.markdown("""<div class="budget-card"><span class="pill pink">TRAFFIC CI 01</span><h4>คู่รัก</h4><div class="budget-number">600–1,000฿</div><p>ยิงหา signal จากมุมแฟนไม่โอเคกับกลิ่น ดู Video View, Click, Engage, Comment/Share</p></div>""", unsafe_allow_html=True)
    with b3:
        st.markdown("""<div class="budget-card"><span class="pill mid">TRAFFIC CI 02</span><h4>ดูแลผู้สูงอายุ</h4><div class="budget-number">600–1,000฿</div><p>ยิงหา signal จากมุมคนในบ้านเป็นห่วง ดู Video View, Click, Engage, Comment เรื่องครอบครัว</p></div>""", unsafe_allow_html=True)
    with b4:
        st.markdown("""<div class="budget-card"><span class="pill amber">RETARGET / MID</span><h4>ดึงเข้า Line OA</h4><div class="budget-number">400–1,000฿</div><p>ยิง Warm audience ที่มี signal จาก Traffic CI ไปหา MID CI: สอบถามแฟน / รีวิว / Line OA</p></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="insight-card"><span class="pill bot">AD MANAGEMENT NOTE</span><h4>แผนตอน Manage Ads</h4><p>เริ่มจากแบ่งงบให้ Traffic CI 2 ตัวใกล้เคียงกันก่อน เพื่อวัดว่า Persona ไหนให้ signal ดีกว่า จากนั้นเอาคนดูวิดีโอ / Engage / Click / Comment / Share เข้า Retarget Pool แล้วค่อยโยกงบไป MID Retarget ถ้า CI ไหน CTR/Engagement/Comment intent ดีกว่า ให้เพิ่มงบฝั่งนั้นหรือแตก angle เพิ่ม</p></div>""", unsafe_allow_html=True)
    close_module()


def render_top_ci_workflow():
    open_module("01_TOP_FUNNEL_CI_FIRST_WORKFLOW_MODULE", "ลำดับการทำงานหลักของ TOP Funnel: เริ่มจาก Persona ก่อน แล้วค่อยแตก CI, Test และ Scale")
    st.markdown('<div class="flow-line"></div>', unsafe_allow_html=True)
    c1, a1, c2, a2, c3, a3, c4 = st.columns([1.05, .12, 1.05, .12, 1.05, .12, 1.05])
    with c1:
        st.markdown("""<div class="card"><span class="pill top">STEP 01</span><h3>Persona</h3><p>เลือกกลุ่มคนให้ชัดก่อนทำ CI</p><ul><li>คู่รัก</li><li>คนดูแลผู้สูงอายุ</li><li>??? กลุ่มใหม่ที่ค้นพบจากผลเทส</li></ul></div>""", unsafe_allow_html=True)
    with a1:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card"><span class="pill pink">STEP 02</span><h3>CI Angle</h3><p>แตกมุมครีเอทีฟตามบุคลิกกลุ่มคน</p><ul><li>Emotion / Care</li><li>Reaction / Concern</li><li>Interest signal</li></ul></div>""", unsafe_allow_html=True)
    with a2:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="card"><span class="pill amber">STEP 03</span><h3>Test Zone</h3><p>เว้นพื้นที่ไว้สำหรับเทส</p><ul><li>Hook</li><li>Visual</li><li>Message</li></ul></div>""", unsafe_allow_html=True)
    with a3:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="card"><span class="pill bot">STEP 04</span><h3>Scale Zone</h3><p>ขยายเฉพาะ CI ที่เริ่มชนะ</p><ul><li>Duplicate angle</li><li>แตก Persona</li><li>เพิ่ม Budget</li></ul></div>""", unsafe_allow_html=True)
    close_module()


def render_persona_creative():
    open_module("02_PERSONA_CREATIVE_MODULE", "แยกกลุ่มเป้าหมายตามบุคลิก/สถานการณ์ เพื่อใช้สร้าง CI และคัด Interest ที่ใช้ได้จริง")
    p1, p2, p3 = st.columns([1, 1, .72])
    with p1:
        st.markdown("""<div class="persona-card"><div class="person-icon">👩‍❤️‍👨</div><span class="pill pink">PERSONA 01 · คู่รัก</span><h3>คนรักเป็นตัวสะกิดให้เริ่มลด</h3><p><b>บทบาทคนรัก:</b> ไม่ด่า ไม่บังคับ แต่แสดง Reaction ว่ากลิ่นบุหรี่ทำให้ความใกล้ชิดหายไป</p><ul><li>แฟนกอดแล้วชะงัก</li><li>ดมเสื้อแล้วถอยออกเบาๆ</li><li>ยื่นลูกอมให้แบบห่วง ไม่ประชด</li></ul></div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class="persona-card"><div class="person-icon">🧑‍🦳👩‍🦱</div><span class="pill mid">PERSONA 02 · ดูแลผู้สูงอายุ</span><h3>คนในบ้านเป็นแรงห่วงใย</h3><p><b>บทบาทผู้ดูแล:</b> สื่อว่าควัน/กลิ่นบุหรี่กระทบคนแก่ในบ้าน จึงอยากให้เริ่มลดแบบค่อยเป็นค่อยไป</p><ul><li>ลูก/หลานเห็นผู้สูงอายุไอหรือปิดจมูก</li><li>หยิบลูกอมให้พ่อ/แม่/คนในบ้าน</li><li>พูดด้วยโทนเป็นห่วง ไม่ตำหนิ</li></ul></div>""", unsafe_allow_html=True)
    with p3:
        st.markdown("""<div class="unknown-card"><div class="unknown-mark">???</div><span class="pill amber">NEXT PERSONA</span><p>เว้นไว้เตรียมขยับเพิ่ม เมื่อผลเทสบอกว่ามีกลุ่มใหม่ที่ตอบสนองกับ CI</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="insight-card"><span class="pill top">INSIGHT</span><h4>ทำ Persona ไว้เพื่อคัด Interest สำหรับกลุ่ม CI</h4><p>จุดนี้ใช้หา “กลุ่มเป้าหมายที่ใช้ได้จริง” จากผลตอบสนองของ Creative เช่น คู่รักตอบสนองกับ Hook แบบแฟนถอยห่าง หรือกลุ่มดูแลผู้สูงอายุตอบสนองกับมุมเป็นห่วงคนในบ้าน จากนั้นค่อยเอา Insight ไปคัด Interest / Audience / Angle สำหรับรอบ Test และ Scale ต่อ</p></div>""", unsafe_allow_html=True)
    close_module()


def render_traffic_to_retarget_pipe():
    open_module("03_TRAFFIC_CI_TO_RETARGET_PIPE_MODULE", "ภาพท่อ: Traffic CI 2 ตัวไหลรวมเข้า Retarget Pool แล้วส่งเข้า MID Retarget")
    st.markdown('<div class="visual-flow">', unsafe_allow_html=True)
    top1, gap, top2 = st.columns([1, .16, 1])
    with top1:
        st.markdown("""<div class="flow-node"><span class="pill pink">TRAFFIC CI 01</span><h4>คู่รัก / แฟนไม่โอเคกับกลิ่น</h4><p>สร้างสัญญาณจากคนที่อินกับ Pain ความสัมพันธ์</p><ul><li>Video View</li><li>Click / Engage</li><li>Comment / Share / Save</li></ul></div>""", unsafe_allow_html=True)
        st.markdown('<div class="pipe-v"></div><div class="pipe-down">↓</div>', unsafe_allow_html=True)
    with gap:
        st.markdown("", unsafe_allow_html=True)
    with top2:
        st.markdown("""<div class="flow-node"><span class="pill mid">TRAFFIC CI 02</span><h4>ดูแลผู้สูงอายุ / คนในบ้านเป็นห่วง</h4><p>สร้างสัญญาณจากคนที่อินกับ Pain ครอบครัว</p><ul><li>Video View</li><li>Click / Engage</li><li>Comment เรื่องคนในบ้าน</li></ul></div>""", unsafe_allow_html=True)
        st.markdown('<div class="pipe-v"></div><div class="pipe-down">↓</div>', unsafe_allow_html=True)

    left, center, right = st.columns([1, .56, 1])
    with left:
        st.markdown('<div class="pipe-h"></div>', unsafe_allow_html=True)
    with center:
        st.markdown("""<div class="merge-node"><span class="pill amber">RETARGET POOL</span><h4>Warm Engagement + Traffic Intent</h4><p>รวมคนจาก CI ทั้งสองตัวที่มีสัญญาณสนใจ</p><ul><li>Video View / Engaged 7–14 วัน</li><li>Click / LPV / Profile Engage 7–14 วัน</li><li>Comment / Save / Share / Inbox 14–30 วัน</li></ul></div>""", unsafe_allow_html=True)
    with right:
        st.markdown('<div class="pipe-h"></div>', unsafe_allow_html=True)

    st.markdown('<div class="pipe-v"></div><div class="pipe-down">↓</div>', unsafe_allow_html=True)
    st.markdown("""<div class="merge-node"><span class="pill bot">MID RETARGET</span><h4>ส่งต่อเข้า CI กลางน้ำ</h4><p>ใช้ Retarget Pool ไปยิง MID CI: สอบถามแฟน / รีวิวจากแฟนหรือคนในบ้าน / ดึงเข้า Line OA</p></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    close_module()


def render_mid_target():
    open_module("04_MID_TARGET_MODULE", "ต่อซีรีส์จาก TOP และยิงแบบ Retarget ไปหาคนที่มีสัญญาณสนใจ เพื่อดึงเข้า Line OA")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""<div class="mini-card mid-target-card"><span class="pill mid">MID ROLE</span><h4>กลุ่มเป้าหมายกลางน้ำ</h4><p>คนที่เห็น TOP CI แล้วเริ่มอินกับ Pain เช่น แฟนไม่ชอบกลิ่น / คนในบ้านเป็นห่วง แต่ยังไม่พร้อมซื้อ ต้องพาเข้าสู่บทสนทนาและรีวิวต่อ</p></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="mini-card mid-target-card"><span class="pill mid">RETARGET SIGNAL</span><h4>สัญญาณที่ใช้ดึงเข้า MID</h4><p>Video View, Engagement, Click, Save, Share, Comment, Inbox เบื้องต้น หรือคนที่ตอบสนองกับมุม “อยากให้เขาลดเพื่อเรา”</p></div>""", unsafe_allow_html=True)
    with m3:
        st.markdown("""<div class="mini-card mid-target-card"><span class="pill mid">MID GOAL</span><h4>เป้าหมายของ MID</h4><p>ทำให้คนรู้สึกว่า “ควรลองคุย / ควรให้แฟนดู / ควรเก็บไว้ถามใน Line OA” ไม่ใช่แค่รับรู้สินค้าเฉย ๆ</p></div>""", unsafe_allow_html=True)

    ci1, ci2 = st.columns(2)
    with ci1:
        st.markdown("""<div class="ci-card"><span class="pill mid">MID CI 01 · RETARGET</span><h3>สอบถามแฟน: ถ้าเขาลดได้ คุณอยากให้เขาเริ่มไหม?</h3><p><b>Insight:</b> คนรักไม่ได้อยากบังคับให้เลิกทันที แต่อยากให้เขา “เริ่มลด” เพราะกลิ่นบุหรี่ทำให้ความใกล้ชิดและบรรยากาศในความสัมพันธ์แย่ลง</p><div class="ci-meta"><div><b>Creative Format</b><br>POV Couple / Question scene / Reaction clip</div><div><b>Hook</b><br>“ลองถามแฟนดู… กลิ่นบุหรี่ทำให้เขาอึดอัดแค่ไหน”</div><div><b>Retarget Audience</b><br>คนดู TOP video, Engaged, Click, Comment/Share มุมคู่รัก</div><div><b>CTA</b><br>ให้แฟนดู / ทัก Line OA เพื่อรับแนวทางเริ่มลด</div></div><ul><li>ต่อจาก TOP ที่แฟนถอยห่างหรือไม่ชอบกลิ่น</li><li>ใช้คำถามจากฝั่งแฟน ไม่ใช่แบรนด์พูดเอง</li><li>คัดคนที่มี Relationship Pain จริง</li></ul></div>""", unsafe_allow_html=True)
    with ci2:
        st.markdown("""<div class="ci-card"><span class="pill mid">MID CI 02 · RETARGET</span><h3>รีวิวจากแฟน/คนในบ้าน: เขาเริ่มพยายามลดแล้ว</h3><p><b>Insight:</b> คนรอบตัวไม่ได้ต้องการคำสัญญาใหญ่ ๆ แต่ต้องการเห็นสัญญาณว่าเขาเริ่มพยายาม เช่น มีลูกอมติดตัวแทนจังหวะที่อยากสูบ</p><div class="ci-meta"><div><b>Creative Format</b><br>Review scene / Couple testimonial / Family POV</div><div><b>Hook</b><br>“เขายังไม่ได้เลิกทันที… แต่เขาเริ่มพยายามลดแล้ว”</div><div><b>Retarget Audience</b><br>คน Engage TOP/MID, Inbox, Save, Comment เรื่องแฟนหรือคนในบ้าน</div><div><b>CTA</b><br>เข้า Line OA เพื่อดูวิธีเริ่มลด / รับโปร / รับของแถม</div></div><ul><li>ใช้รีวิวเชิงความรู้สึก ไม่ใช่รีวิวสินค้าแข็ง ๆ</li><li>ต่อได้ทั้งคู่รักและดูแลผู้สูงอายุ</li><li>เตรียมส่งคนสนใจเข้า Line OA ก่อนปิดการขาย</li></ul></div>""", unsafe_allow_html=True)
    close_module()


def render_test_and_scale_placeholder():
    open_module("05_TEST_AND_SCALE_PLACEHOLDER_MODULE", "พื้นที่ว่างสำหรับใส่ผล Test, Hook ที่ชนะ, Visual ที่เวิร์ก และ CI ที่ควร Scale")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("""<div class="placeholder"><span class="pill amber">TEST SLOT A</span><h4>Hook Test</h4><p>เว้นไว้ใส่ Hook ที่ต้องเทส เช่น คู่รัก / ผู้สูงอายุ / กลิ่นติดตัว</p></div>""", unsafe_allow_html=True)
    with t2:
        st.markdown("""<div class="placeholder"><span class="pill amber">TEST SLOT B</span><h4>Visual Test</h4><p>เว้นไว้ใส่มุมภาพ: กอดแล้วถอย, ปิดจมูก, ยื่นลูกอม, สีหน้าเป็นห่วง</p></div>""", unsafe_allow_html=True)
    with t3:
        st.markdown("""<div class="placeholder"><span class="pill bot">SCALE SLOT</span><h4>Scale Candidate</h4><p>เว้นไว้ใส่ CI ที่ชนะ แล้วแตก Angle / Duplicate / เพิ่มงบ</p></div>""", unsafe_allow_html=True)
    close_module()


def render_lower_funnel():
    open_module("06_BOT_FUNNEL_MODULE", "BOT จะใช้หลังจาก MID คัดคนสนใจจริงแล้ว เพื่อ Retarget และปิดการขาย")
    m1, m2 = st.columns(2)
    with m1:
        st.markdown("""<div class="mini-card"><span class="pill mid">MID SUMMARY</span><h4>Conversation / Line OA</h4><p>หลัง TOP CI มีคนอิน ให้ใช้ MID เพื่อพาไปสู่การคุย การรีวิว และการเพิ่มเพื่อน Line OA</p></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="mini-card"><span class="pill bot">BOT FUNNEL</span><h4>Close / Offer</h4><p>Retarget คนที่เข้า Line OA / ทัก / สนใจสูง ด้วย Offer, Bundle, Review Screenshot และ CTA ซื้อ</p></div>""", unsafe_allow_html=True)
    close_module()


def render_footer():
    st.markdown('<div class="footer-note">Visual Pipe: Traffic CI 01 + CI 02 → Retarget Pool → MID Retarget</div>', unsafe_allow_html=True)


def main():
    render_theme()
    render_header()
    render_budget_plan()
    render_top_ci_workflow()
    render_persona_creative()
    render_traffic_to_retarget_pipe()
    render_mid_target()
    render_test_and_scale_placeholder()
    render_lower_funnel()
    render_footer()


if __name__ == "__main__":
    main()
