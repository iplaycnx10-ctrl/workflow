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


# =========================================================
# 01_THEME_MODULE
# =========================================================
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
        .hero, .card, .mini-card, .persona-card, .test-card, .insight-card, .ci-card { background: rgba(255,255,255,0.9); border: 1px solid var(--line); box-shadow: 0 12px 36px rgba(31,41,55,0.045); }
        .hero { border-radius: 28px; padding: 28px 30px; margin-bottom: 20px; }
        .eyebrow { display: inline-flex; padding: 7px 12px; border-radius: 999px; background: #f8fafc; border: 1px solid var(--line); color: var(--muted); font-size: 13px; margin-bottom: 12px; }
        .title { font-size: 38px; font-weight: 850; letter-spacing: -0.04em; margin: 0; color: var(--ink); }
        .subtitle { color: var(--muted); font-size: 16px; margin-top: 8px; line-height: 1.7; }
        .flow-line { height: 3px; border-radius: 99px; background: linear-gradient(90deg, #bfdbfe, #ddd6fe, #bbf7d0); margin: 12px 0 20px 0; }
        .card { border-radius: 24px; padding: 22px; min-height: 270px; height: auto; overflow: visible; }
        .card h3, .mini-card h4, .persona-card h3, .test-card h4, .insight-card h4, .ci-card h3 { margin: 0 0 8px 0; letter-spacing: -0.02em; color: var(--ink); }
        .card p, .card li, .mini-card p, .persona-card p, .persona-card li, .test-card p, .insight-card p, .ci-card p, .ci-card li { color: var(--muted); line-height: 1.62; font-size: 14px; }
        .pill { display: inline-block; padding: 7px 11px; border-radius: 999px; font-size: 12px; font-weight: 750; margin-bottom: 12px; }
        .top { background: var(--blue); color: var(--blue-text); }
        .mid { background: var(--lavender); color: var(--lavender-text); }
        .bot { background: var(--mint); color: var(--mint-text); }
        .pink { background: var(--pink); color: var(--pink-text); }
        .amber { background: var(--amber); color: var(--amber-text); }
        .arrow-row { display: flex; align-items: center; justify-content: center; min-height: 270px; margin: 0; color: #c4c9d4; font-size: 30px; font-weight: 800; }
        .mini-card, .persona-card, .test-card, .insight-card, .ci-card { border-radius: 20px; padding: 18px; }
        .persona-card, .unknown-card { min-height: 405px; height: auto; overflow: visible; }
        .placeholder { border: 1.5px dashed #cbd5e1; background: rgba(248,250,252,0.65); border-radius: 20px; padding: 18px; min-height: 190px; height: auto; overflow: visible; }
        .mini-card { min-height: 175px; height: auto; overflow: visible; }
        .insight-card { min-height: 160px; margin-top: 18px; overflow: visible; }
        .mid-target-card { min-height: 260px; }
        .ci-card { min-height: 360px; margin-top: 18px; }
        .ci-meta { display:grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 12px 0; }
        .ci-meta div { background:#f8fafc; border:1px solid var(--line); border-radius:14px; padding:10px; color:var(--muted); font-size:13px; line-height:1.45; }
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


# =========================================================
# 02_HEADER_MODULE
# =========================================================
def render_header():
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">🍬 Project Board · White Pastel Minimal · Modular</div>
            <h1 class="title">ลูกอมบุหรี่ — TOP Funnel CI Workflow</h1>
            <div class="subtitle">
                โฟกัสงานแรกคือ CI ของ TOP Funnel: แยก Persona → ทำ Creative → Test → Scale<br>
                MID Target จะใช้รับคนที่เริ่มสนใจจาก CI แล้วค่อยอธิบายเหตุผล สร้างความเชื่อ และคัด Intent ต่อ
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 03_TOP_CI_WORKFLOW_MODULE
# =========================================================
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


# =========================================================
# 04_PERSONA_CREATIVE_MODULE
# =========================================================
def render_persona_creative():
    open_module("02_PERSONA_CREATIVE_MODULE", "แยกกลุ่มเป้าหมายตามบุคลิก/สถานการณ์ เพื่อใช้สร้าง CI และคัด Interest ที่ใช้ได้จริง")
    p1, p2, p3 = st.columns([1, 1, .72])
    with p1:
        st.markdown("""<div class="persona-card"><div class="person-icon">👩‍❤️‍👨</div><span class="pill pink">PERSONA 01 · คู่รัก</span><h3>คนรักเป็นตัวสะกิดให้เริ่มลด</h3><p><b>บทบาทคนรัก:</b> ไม่ด่า ไม่บังคับ แต่แสดง Reaction ว่ากลิ่นบุหรี่ทำให้ความใกล้ชิดหายไป</p><ul><li>แฟนกอดแล้วชะงัก</li><li>ดมเสื้อแล้วถอยออกเบาๆ</li><li>ยื่นลูกอมให้แบบห่วง ไม่ประชด</li></ul></div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class="persona-card"><div class="person-icon">🧑‍🦳👩‍🦱</div><span class="pill mid">PERSONA 02 · ดูแลผู้สูงอายุ</span><h3>คนในบ้านเป็นแรงห่วงใย</h3><p><b>บทบาทผู้ดูแล:</b> สื่อว่าควัน/กลิ่นบุหรี่กระทบคนแก่ในบ้าน จึงอยากให้เริ่มลดแบบค่อยเป็นค่อยไป</p><ul><li>ลูก/หลานเห็นผู้สูงอายุไอหรือปิดจมูก</li><li>หยิบลูกอมให้พ่อ/แม่/คนในบ้าน</li><li>พูดด้วยโทนเป็นห่วง ไม่ตำหนิ</li></ul></div>""", unsafe_allow_html=True)
    with p3:
        st.markdown("""<div class="unknown-card"><div class="unknown-mark">???</div><span class="pill amber">NEXT PERSONA</span><p>เว้นไว้เตรียมขยับเพิ่ม เมื่อผลเทสบอกว่ามีกลุ่มใหม่ที่ตอบสนองกับ CI</p></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="insight-card"><span class="pill top">INSIGHT</span><h4>ทำ Persona ไว้เพื่อคัด Interest สำหรับกลุ่ม CI</h4><p>จุดนี้ไม่ได้ทำเพื่อสวยอย่างเดียว แต่ใช้เป็นระบบหา “กลุ่มเป้าหมายที่ใช้ได้จริง” จากผลตอบสนองของ Creative เช่น คู่รักตอบสนองกับ Hook แบบแฟนถอยห่าง หรือกลุ่มดูแลผู้สูงอายุตอบสนองกับมุมเป็นห่วงคนในบ้าน จากนั้นค่อยเอา Insight ไปคัด Interest / Audience / Angle สำหรับรอบ Test และ Scale ต่อ</p></div>""", unsafe_allow_html=True)
    close_module()


# =========================================================
# 05_MID_TARGET_MODULE
# =========================================================
def render_mid_target():
    open_module("03_MID_TARGET_MODULE", "รับคนที่เริ่มสนใจจาก TOP CI แล้วทำให้เข้าใจ เชื่อ และแยก Intent ก่อนส่งไป BOT")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""<div class="mini-card mid-target-card"><span class="pill mid">MID ROLE</span><h4>กลุ่มเป้าหมายกลางน้ำ</h4><p>คนที่เห็น/ดู/คลิก/มีปฏิสัมพันธ์กับ TOP CI แล้ว แต่ยังไม่พร้อมซื้อทันที ต้องให้เหตุผลก่อนว่า “ทำไมต้องลอง” และ “สินค้าช่วยตรงไหน”</p></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="mini-card mid-target-card"><span class="pill mid">TARGET SIGNAL</span><h4>สัญญาณที่ใช้ดึงเข้า MID</h4><p>Video View, Engagement, Click, Save, Comment, Inbox เบื้องต้น หรือคนที่ตอบสนองกับ Persona เช่น คู่รัก / ดูแลผู้สูงอายุ / กลิ่นติดคนในบ้าน</p></div>""", unsafe_allow_html=True)
    with m3:
        st.markdown("""<div class="mini-card mid-target-card"><span class="pill mid">MID CONTENT</span><h4>คอนเทนต์ที่ควรใช้</h4><p>Explainer, FAQ, รีวิว, Before/After Situation, วิธีใช้ลูกอมแทนจังหวะอยากสูบ และคอนเทนต์ที่เชื่อม Pain → Solution → Reason to Buy</p></div>""", unsafe_allow_html=True)

    ci1, ci2 = st.columns(2)
    with ci1:
        st.markdown("""<div class="ci-card"><span class="pill mid">MID CI 01</span><h3>Explainer / FAQ: ลูกอมช่วยตรงไหน?</h3><p><b>Goal:</b> ทำให้คนที่เริ่มสนใจเข้าใจว่าไม่ได้ขายเวทมนตร์ แต่เป็นตัวช่วยในจังหวะที่ปากอยากสูบ/อยากเคี้ยว</p><div class="ci-meta"><div><b>Hook</b><br>“อยากลดบุหรี่ แต่ปากยังอยากสูบอยู่ใช่ไหม?”</div><div><b>Format</b><br>Short explainer / Talking head / Motion text</div><div><b>Key Message</b><br>ใช้ลูกอมเป็นตัวช่วยคั่นจังหวะอยากสูบ</div><div><b>CTA</b><br>ลองเริ่มจากลดทีละมวน</div></div><ul><li>ตอบคำถาม: ใช้ตอนไหน / เหมาะกับใคร</li><li>โยง Pain จาก TOP → Solution</li><li>คัดคนที่อ่าน/ดูแล้วเริ่มมี Intent</li></ul></div>""", unsafe_allow_html=True)
    with ci2:
        st.markdown("""<div class="ci-card"><span class="pill mid">MID CI 02</span><h3>Review / Before-After Situation</h3><p><b>Goal:</b> ทำให้คนเชื่อขึ้นผ่านสถานการณ์จริง เช่น จากเดิมคนรัก/คนในบ้านไม่โอเคกับกลิ่น → เริ่มมีตัวช่วยติดตัว</p><div class="ci-meta"><div><b>Hook</b><br>“ไม่ได้เลิกได้ทันที แต่เริ่มลดได้จริงจังกว่าเดิม”</div><div><b>Format</b><br>POV review / Testimonial / Before-After scene</div><div><b>Key Message</b><br>มีตัวช่วยแทนจังหวะสูบ ทำให้เริ่มคุมพฤติกรรมได้</div><div><b>CTA</b><br>ดูโปร / ทักถาม / กดไป Shopee</div></div><ul><li>ใช้มุมคู่รักหรือดูแลผู้สูงอายุต่อจาก TOP</li><li>เน้นความรู้สึก “เริ่มลดเพื่อคนข้างๆ”</li><li>ดู Comment/Inbox เพื่อแยกคนพร้อมซื้อ</li></ul></div>""", unsafe_allow_html=True)

    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""<div class="insight-card"><span class="pill top">MID DETAIL</span><h4>หน้าที่ของ MID Target</h4><p>MID ไม่ได้ปิดการขายทันที แต่ทำหน้าที่กรองคนที่มีความสนใจจริงจาก TOP CI ว่าเขาสนใจเพราะอะไร เช่น สนใจเพราะแฟนบ่นเรื่องกลิ่น หรือสนใจเพราะเป็นห่วงผู้สูงอายุในบ้าน จากนั้นค่อยส่งต่อกลุ่ม Intent สูงไป BOT</p></div>""", unsafe_allow_html=True)
    with d2:
        st.markdown("""<div class="insight-card"><span class="pill amber">OPTIMIZE NOTE</span><h4>สิ่งที่ต้องดูตอนเทส MID</h4><p>ดู CTR คุณภาพ, Comment intent, Inbox คุณภาพ, LPV/VC/ATC และคำถามซ้ำจากลูกค้า ถ้าคำถามซ้ำเยอะ แปลว่า MID Content ยังต้องอธิบายเพิ่มก่อนเอาไปปิดการขาย</p></div>""", unsafe_allow_html=True)
    close_module()


# =========================================================
# 06_TEST_AND_SCALE_PLACEHOLDER_MODULE
# =========================================================
def render_test_and_scale_placeholder():
    open_module("04_TEST_AND_SCALE_PLACEHOLDER_MODULE", "พื้นที่ว่างสำหรับใส่ผล Test, Hook ที่ชนะ, Visual ที่เวิร์ก และ CI ที่ควร Scale")
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("""<div class="placeholder"><span class="pill amber">TEST SLOT A</span><h4>Hook Test</h4><p>เว้นไว้ใส่ Hook ที่ต้องเทส เช่น คู่รัก / ผู้สูงอายุ / กลิ่นติดตัว</p></div>""", unsafe_allow_html=True)
    with t2:
        st.markdown("""<div class="placeholder"><span class="pill amber">TEST SLOT B</span><h4>Visual Test</h4><p>เว้นไว้ใส่มุมภาพ: กอดแล้วถอย, ปิดจมูก, ยื่นลูกอม, สีหน้าเป็นห่วง</p></div>""", unsafe_allow_html=True)
    with t3:
        st.markdown("""<div class="placeholder"><span class="pill bot">SCALE SLOT</span><h4>Scale Candidate</h4><p>เว้นไว้ใส่ CI ที่ชนะ แล้วแตก Angle / Duplicate / เพิ่มงบ</p></div>""", unsafe_allow_html=True)
    close_module()


# =========================================================
# 07_LOWER_FUNNEL_MODULE
# =========================================================
def render_lower_funnel():
    open_module("05_BOT_FUNNEL_MODULE", "BOT จะใช้หลังจาก MID คัดคนสนใจจริงแล้ว เพื่อ Retarget และปิดการขาย")
    m1, m2 = st.columns(2)
    with m1:
        st.markdown("""<div class="mini-card"><span class="pill mid">MID SUMMARY</span><h4>Trust / Explain</h4><p>หลัง TOP CI มีคนสนใจ ค่อยใช้ Explainer, FAQ, Review เพื่อทำให้เชื่อและเข้าใจสินค้า</p></div>""", unsafe_allow_html=True)
    with m2:
        st.markdown("""<div class="mini-card"><span class="pill bot">BOT FUNNEL</span><h4>Close / Offer</h4><p>Retarget คน Intent สูงด้วย Offer, Bundle, Review Screenshot และ CTA ไป Shopee / Inbox</p></div>""", unsafe_allow_html=True)
    close_module()


# =========================================================
# 08_FOOTER_MODULE
# =========================================================
def render_footer():
    st.markdown('<div class="footer-note">Modular Board v0.7 · Added MID CI Cards · TOP → MID → BOT</div>', unsafe_allow_html=True)


# =========================================================
# 99_MAIN_RENDER_MODULE
# =========================================================
def main():
    render_theme()
    render_header()
    render_top_ci_workflow()
    render_persona_creative()
    render_mid_target()
    render_test_and_scale_placeholder()
    render_lower_funnel()
    render_footer()


if __name__ == "__main__":
    main()
