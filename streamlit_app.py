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
        .stApp {
            background: radial-gradient(circle at top left, #fdf2f8 0, transparent 28%),
                        radial-gradient(circle at top right, #dbeafe 0, transparent 26%),
                        var(--bg);
            color: var(--ink);
        }
        [data-testid="stSidebar"] { display: none; }
        .main .block-container { padding-top: 2.2rem; max-width: 1280px; }
        .hero {
            background: rgba(255,255,255,0.86);
            border: 1px solid var(--line);
            border-radius: 28px;
            padding: 28px 30px;
            box-shadow: 0 18px 50px rgba(31,41,55,0.06);
            margin-bottom: 20px;
        }
        .eyebrow {
            display: inline-flex; padding: 7px 12px; border-radius: 999px;
            background: #f8fafc; border: 1px solid var(--line); color: var(--muted);
            font-size: 13px; margin-bottom: 12px;
        }
        .title { font-size: 38px; font-weight: 850; letter-spacing: -0.04em; margin: 0; color: var(--ink); }
        .subtitle { color: var(--muted); font-size: 16px; margin-top: 8px; line-height: 1.7; }
        .module-title { font-size: 14px; font-weight: 800; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin: 24px 0 12px 0; }
        .flow-line { height: 3px; border-radius: 99px; background: linear-gradient(90deg, #bfdbfe, #ddd6fe, #bbf7d0); margin: 12px 0 20px 0; }
        .card { background: rgba(255,255,255,0.9); border: 1px solid var(--line); border-radius: 24px; padding: 22px; min-height: 235px; box-shadow: 0 12px 36px rgba(31,41,55,0.045); }
        .card h3 { margin: 0 0 8px 0; font-size: 23px; letter-spacing: -0.02em; }
        .card p, .card li { color: var(--muted); line-height: 1.62; font-size: 14px; }
        .pill { display: inline-block; padding: 7px 11px; border-radius: 999px; font-size: 12px; font-weight: 750; margin-bottom: 12px; }
        .top { background: var(--blue); color: var(--blue-text); }
        .mid { background: var(--lavender); color: var(--lavender-text); }
        .bot { background: var(--mint); color: var(--mint-text); }
        .pink { background: var(--pink); color: var(--pink-text); }
        .amber { background: var(--amber); color: var(--amber-text); }
        .arrow-row { display: flex; align-items: center; justify-content: center; margin: 14px 0 2px 0; color: #c4c9d4; font-size: 28px; font-weight: 800; }
        .mini-card { background: rgba(255,255,255,0.92); border: 1px solid var(--line); border-radius: 20px; padding: 18px; box-shadow: 0 10px 28px rgba(31,41,55,0.04); min-height: 138px; }
        .mini-card h4 { margin: 0 0 8px 0; font-size: 16px; }
        .mini-card p { margin: 0; color: var(--muted); font-size: 13.5px; line-height: 1.6; }
        .footer-note { color: var(--muted); text-align: center; padding: 20px 0 6px; font-size: 13px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 02_HEADER_MODULE
# =========================================================
def render_header():
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">🍬 Project Board · White Pastel Minimal · Modular</div>
            <h1 class="title">ลูกอมบุหรี่ — Ads Workflow Report</h1>
            <div class="subtitle">
                บอร์ดหน้าเดียวสำหรับวางระบบยิงแอดแบบ Funnel: TOP → MID → BOT<br>
                ใช้ดูภาพรวมว่าแต่ละชั้นของแคมเปญทำหน้าที่อะไร ต้องใช้ Creative แบบไหน และวัดผลด้วยอะไร
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# 03_FUNNEL_WORKFLOW_MODULE
# =========================================================
def render_funnel_workflow():
    st.markdown('<div class="module-title">01_FUNNEL_WORKFLOW_MODULE</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-line"></div>', unsafe_allow_html=True)

    col1, col_arrow1, col2, col_arrow2, col3 = st.columns([1.15, 0.14, 1.15, 0.14, 1.15])

    with col1:
        st.markdown("""<div class="card"><span class="pill top">TOP FUNNEL · Awareness</span><h3>เปิด Pain ให้คนหยุดดู</h3><p><b>หน้าที่:</b> ดึงคนที่มีปัญหากลิ่นบุหรี่ / อยากลดบุหรี่ / คนรอบตัวเริ่มไม่โอเค</p><ul><li>Hook แรงใน 1–3 วิ</li><li>POV สถานการณ์จริง</li><li>ปั้นกลุ่ม Video View / Engage / Click</li></ul></div>""", unsafe_allow_html=True)
    with col_arrow1:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="card"><span class="pill mid">MID FUNNEL · Trust</span><h3>ทำให้เข้าใจและเชื่อ</h3><p><b>หน้าที่:</b> อธิบายว่าสินค้าช่วยอะไร เหมาะกับใคร และลดความลังเลก่อนซื้อ</p><ul><li>Explainer / FAQ / Review</li><li>Pain → Solution → Reason</li><li>ส่งคนสนใจเข้า BOT</li></ul></div>""", unsafe_allow_html=True)
    with col_arrow2:
        st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="card"><span class="pill bot">BOT FUNNEL · Conversion</span><h3>ปิดการขายและดัน AOV</h3><p><b>หน้าที่:</b> Retarget คน Intent สูงด้วย Offer, Bundle, Review และ CTA ชัด</p><ul><li>Offer / Bundle / Social Proof</li><li>Retarget Click / Inbox / ATC</li><li>วัด Purchase, CPA, ROAS, AOV</li></ul></div>""", unsafe_allow_html=True)


# =========================================================
# 04_CREATIVE_DIRECTION_MODULE
# =========================================================
def render_creative_direction():
    st.markdown('<div class="module-title">02_CREATIVE_DIRECTION_MODULE</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""<div class="mini-card"><span class="pill top">TOP CI</span><h4>Problem / Emotion</h4><p>แฟนเบ้หน้าเพราะกลิ่นบุหรี่, คนสูบไม่รู้ตัวว่ากลิ่นติดตัว, อยากลดแต่ยังปากว่างไม่ได้</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="mini-card"><span class="pill mid">MID CI</span><h4>Reason / Proof</h4><p>อธิบายวิธีใช้, รีวิวคนลองลดจำนวนมวน, เปรียบเทียบก่อน-หลัง, FAQ ว่าลูกอมช่วยตรงไหน</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="mini-card"><span class="pill bot">BOT CI</span><h4>Offer / Close</h4><p>โปรแพ็กคู่, คุ้มกว่าเมื่อซื้อหลายชิ้น, รีวิว Screenshot, CTA ไป Shopee / Inbox / ช่องทางปิดการขาย</p></div>""", unsafe_allow_html=True)


# =========================================================
# 05_KPI_AND_RETARGET_MODULE
# =========================================================
def render_kpi_and_retarget():
    st.markdown('<div class="module-title">03_KPI_AND_RETARGET_MODULE</div>', unsafe_allow_html=True)
    k1, k2 = st.columns([1, 1])

    with k1:
        st.markdown("""<div class="mini-card"><span class="pill pink">KPI WATCH</span><h4>ตัวเลขที่ต้องดูตาม Funnel</h4><p><b>TOP:</b> CTR, CPM, 3-sec View, Engagement<br><b>MID:</b> LPV, VC, Inbox, ATC, Comment Intent<br><b>BOT:</b> Purchase, CPA, ROAS, AOV, Close Rate</p></div>""", unsafe_allow_html=True)
    with k2:
        st.markdown("""<div class="mini-card"><span class="pill amber">RETARGET FLOW</span><h4>Audience Movement</h4><p>Video View / Engage / Click → LPV / VC / Inbox → ATC / High Intent Inbox / Shopee Click → Purchase / Bundle / Repeat</p></div>""", unsafe_allow_html=True)


# =========================================================
# 06_FOOTER_MODULE
# =========================================================
def render_footer():
    st.markdown('<div class="footer-note">Modular Board v0.1 · Project: ลูกอมบุหรี่ · White Pastel Minimal</div>', unsafe_allow_html=True)


# =========================================================
# 99_MAIN_RENDER_MODULE
# =========================================================
def main():
    render_theme()
    render_header()
    render_funnel_workflow()
    render_creative_direction()
    render_kpi_and_retarget()
    render_footer()


if __name__ == "__main__":
    main()
