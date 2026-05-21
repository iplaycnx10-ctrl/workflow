import streamlit as st
from ui.heatmap import render_heatmap_path

st.set_page_config(page_title="ลูกอมบุหรี่ | Work Flow Board", page_icon="🍬", layout="wide", initial_sidebar_state="collapsed")

def render_theme():
    st.markdown("""
    <style>
    :root{--bg:#fbfbfe;--ink:#1f2937;--muted:#6b7280;--line:#e9edf5;--blue:#dbeafe;--blue-text:#1d4ed8;--lav:#ede9fe;--lav-text:#6d28d9;--mint:#dcfce7;--mint-text:#15803d;--pink:#fce7f3;--pink-text:#be185d;--amber:#fef3c7;--amber-text:#b45309;--sky:#e0f2fe;--sky-text:#0369a1;--black:#050608;--cyan:#38bdf8}
    .stApp{background:radial-gradient(circle at top left,#fdf2f8 0,transparent 28%),radial-gradient(circle at top right,#dbeafe 0,transparent 26%),radial-gradient(circle at bottom,#dcfce7 0,transparent 24%),var(--bg);color:var(--ink)}[data-testid="stSidebar"]{display:none}.main .block-container{padding-top:2.2rem;max-width:1280px}.module-wrap{background:rgba(255,255,255,.52);border:1px solid rgba(237,240,247,.95);border-radius:30px;padding:22px 22px 26px;margin:28px 0;box-shadow:0 18px 48px rgba(31,41,55,.035)}.module-title{font-size:14px;font-weight:850;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin:0}.module-desc{color:var(--muted);font-size:13px;line-height:1.55;margin:4px 0 16px}.hero,.card,.mini-card,.persona-card,.insight-card,.flow-node,.merge-node,.budget-card,.placeholder,.date-card{border:1px solid var(--line);box-shadow:0 12px 36px rgba(31,41,55,.045)}.hero{border-radius:28px;padding:28px 30px;margin-bottom:20px;background:linear-gradient(135deg,#fff,#fdf2f8 52%,#eff6ff)}.eyebrow{display:inline-flex;padding:7px 12px;border-radius:999px;background:#fff;border:1px solid var(--line);color:var(--muted);font-size:13px;margin-bottom:12px}.title{font-size:38px;font-weight:850;letter-spacing:-.04em;margin:0;color:var(--ink)}.subtitle{color:var(--muted);font-size:16px;margin-top:8px;line-height:1.7}.pill{display:inline-block;padding:7px 11px;border-radius:999px;font-size:12px;font-weight:750;margin-bottom:12px}.top{background:var(--blue);color:var(--blue-text)}.mid{background:var(--lav);color:var(--lav-text)}.bot{background:var(--mint);color:var(--mint-text)}.pink{background:var(--pink);color:var(--pink-text)}.amber{background:var(--amber);color:var(--amber-text)}.sky{background:var(--sky);color:var(--sky-text)}.card,.budget-card,.mini-card,.persona-card,.insight-card,.flow-node,.merge-node,.placeholder,.date-card{border-radius:20px;padding:18px;background:#fff}.card{min-height:270px;border-radius:24px}.budget-card{min-height:190px}.date-card{min-height:225px}.mini-card{min-height:175px}.persona-card{min-height:425px}.placeholder{min-height:190px;border:1.5px dashed #cbd5e1}.age-box{background:rgba(255,255,255,.72);border:1px solid var(--line);border-radius:14px;padding:10px 12px;margin:10px 0 12px;color:var(--ink);font-size:13.5px;line-height:1.5}.pastel-blue{background:linear-gradient(135deg,#fff,#dbeafe)}.pastel-pink{background:linear-gradient(135deg,#fff,#fce7f3)}.pastel-lav{background:linear-gradient(135deg,#fff,#ede9fe)}.pastel-mint{background:linear-gradient(135deg,#fff,#dcfce7)}.pastel-amber{background:linear-gradient(135deg,#fff,#fef3c7)}.pastel-sky{background:linear-gradient(135deg,#fff,#e0f2fe)}h3,h4{margin:0 0 8px;color:var(--ink);letter-spacing:-.02em}p,li{color:var(--muted);line-height:1.62;font-size:14px}.budget-number{font-size:30px;font-weight:900;letter-spacing:-.04em;color:var(--ink);margin:2px 0 10px}.arrow-row{display:flex;align-items:center;justify-content:center;min-height:170px;color:#c4c9d4;font-size:30px;font-weight:800}.flow-line{height:3px;border-radius:99px;background:linear-gradient(90deg,#bfdbfe,#fbcfe8,#ddd6fe,#bbf7d0);margin:12px 0 20px}.visual-flow{margin-top:18px;padding:22px;border-radius:26px;background:rgba(255,255,255,.66);border:1px solid var(--line)}.person-icon{font-size:42px;margin-bottom:8px}.unknown-card{min-height:425px;border:1.5px dashed #cbd5e1;background:linear-gradient(135deg,#fff,#f8fafc);border-radius:20px;padding:18px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}.unknown-mark{font-size:58px;font-weight:900;color:#94a3b8}.black-module{background:linear-gradient(135deg,rgba(13,17,23,.96),rgba(15,23,42,.86));border:1px solid #273142;border-radius:28px;padding:24px;margin:24px 0;box-shadow:0 20px 60px rgba(0,0,0,.22)}.black-kicker{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#94a3b8;font-weight:850}.black-title{font-size:30px;line-height:1.18;letter-spacing:-.04em;color:#f8fafc;font-weight:950;margin:6px 0 8px}.black-desc{font-size:14px;line-height:1.65;color:#94a3b8;margin:0 0 18px}.minimal-pipe-wrap{background:rgba(255,255,255,.92);border:1px solid rgba(226,232,240,.95);border-radius:26px;padding:22px;margin:16px 0;color:#111827;box-shadow:0 18px 44px rgba(15,23,42,.08)}.minimal-step{background:transparent;border-left:3px solid #cbd5e1;padding:2px 0 2px 16px;min-height:72px}.minimal-step h4{color:#0f172a;font-size:17px;margin:0 0 5px}.minimal-step p{color:#475569;font-size:13px;margin:0}.minimal-arrow{display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:26px;font-weight:900;min-height:72px}.minimal-note{color:#334155;font-size:13px;line-height:1.7;margin:0 0 16px}.minimal-fun-note{color:#0f172a;font-size:14px;line-height:1.8;margin:0 0 16px;padding:12px 14px;border-left:4px solid #38bdf8;background:linear-gradient(90deg,#eff6ff,#ffffff);border-radius:14px}.minimal-compare{border-top:1px solid #e2e8f0;padding-top:16px;margin-top:18px}.minimal-compare h4{color:#0f172a;font-size:16px}.minimal-compare p{color:#475569;font-size:13px}.minimal-ref{background:linear-gradient(90deg,#eff6ff,#f0fdf4);border:1px solid #dbeafe;border-radius:18px;padding:14px;margin-top:16px}.heatmap-path{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:10px 0 18px}.heatmap-chip{font-size:12px;font-weight:850;border:1px solid;border-radius:999px;padding:9px 12px;box-shadow:0 8px 20px rgba(15,23,42,.06)}.heatmap-arrow{color:#94a3b8;font-weight:950}.footer-note{color:var(--muted);text-align:center;padding:20px 0 6px;font-size:13px}
    </style>""", unsafe_allow_html=True)

def open_module(t,d): st.markdown(f'<div class="module-wrap"><div class="module-title">{t}</div><p class="module-desc">{d}</p>', unsafe_allow_html=True)
def close_module(): st.markdown('</div>', unsafe_allow_html=True)
def render_header(): st.markdown('<div class="hero"><div class="eyebrow">🍬 Project Board · Pastel Minimal</div><h1 class="title">ลูกอมบุหรี่ — Smoking Candy Workflow</h1><div class="subtitle">แยก Modular เป็นขั้นตอน: วางแผนงาน → รายงานผู้บริหาร</div></div>', unsafe_allow_html=True)

def render_budget_plan():
    open_module('00_BUDGET_AND_AD_MANAGEMENT_PLAN','งบเฉลี่ยสำหรับเริ่มยิงและแผนแบ่งงบตอน Manage Ads')
    cols=st.columns(4); data=[('TOTAL TEST BUDGET','งบเฉลี่ยเริ่มต้น','1,600–3,000฿','ใช้เป็นงบทดสอบ Funnel ชุดแรก เพื่อดูว่า CI ไหนสร้าง signal ดีพอจะ Retarget ต่อ','top','pastel-blue'),('TRAFFIC CI 01','คู่รัก','600–1,000฿','เริ่มยิงตั้งแต่วันที่ 1 เพื่อหา signal จากมุมแฟนไม่โอเคกับกลิ่น','pink','pastel-pink'),('TRAFFIC CI 02','ดูแลผู้สูงอายุ','600–1,000฿','เริ่มยิงตั้งแต่วันที่ 1 เพื่อหา signal จากมุมคนในบ้านเป็นห่วง','mid','pastel-lav'),('RETARGET / MID','ดึงเข้า Line OA','400–1,000฿','เปิดตั้งแต่วันแรกเพื่อรีกลุ่มเก่าก่อน แล้วค่อยเพิ่ม CI รับ Traffic ใหม่เมื่อ Traffic หลักเริ่มแน่น','amber','pastel-amber')]
    for c,x in zip(cols,data):
        with c: st.markdown(f'<div class="budget-card {x[5]}"><span class="pill {x[4]}">{x[0]}</span><h4>{x[1]}</h4><div class="budget-number">{x[2]}</div><p>{x[3]}</p></div>', unsafe_allow_html=True)
    close_module()

def render_date_project():
    open_module('00_DATE_PROJECT_MODULE','วันที่ 1–3 ไม่ใช่วันเริ่มยิงคนละตัว แต่คือช่วง monitor หลังจากยิงทุก CI ตั้งแต่วันแรก')
    d1,d2,d3=st.columns(3)
    with d1: st.markdown('<div class="date-card pastel-pink"><span class="pill pink">DAY 1</span><h4>Launch พร้อมกัน</h4><p>เปิด Traffic CI 01 คู่รัก + Traffic CI 02 ผู้สูงอายุ + Retarget กลุ่มเก่าพร้อมกันตั้งแต่วันแรก เพื่อเริ่มเก็บ signal</p></div>', unsafe_allow_html=True)
    with d2: st.markdown('<div class="date-card pastel-lav"><span class="pill mid">DAY 2</span><h4>Monitor Signal</h4><p>ดูว่า CI ไหนเริ่มมีสัญญาณดีกว่า เช่น View, Click, Engage, Comment intent และคุณภาพกลุ่มที่เข้ามา</p></div>', unsafe_allow_html=True)
    with d3: st.markdown('<div class="date-card pastel-mint"><span class="pill bot">DAY 3</span><h4>Optimize / เพิ่ม Retarget Layer</h4><p>ถ้า Traffic หลักเริ่มแน่น ค่อยเพิ่ม CI Retarget ที่รับคนจาก Traffic CI 01–02 เข้า Line OA หรือโยกงบไปฝั่งที่ชนะ</p></div>', unsafe_allow_html=True)
    close_module()

def render_top_ci_workflow():
    open_module('01_TOP_FUNNEL_CI_FIRST_WORKFLOW_MODULE','เริ่มจาก Persona → CI Angle → Test → Scale')
    st.markdown('<div class="flow-line"></div>', unsafe_allow_html=True); c1,a1,c2,a2,c3,a3,c4=st.columns([1.05,.12,1.05,.12,1.05,.12,1.05])
    cards=[('STEP 01','Persona','เลือกกลุ่มคนให้ชัดก่อนทำ CI<ul><li>คู่รัก</li><li>คนดูแลผู้สูงอายุ</li><li>??? กลุ่มใหม่จากผลเทส</li></ul>','top','pastel-blue'),('STEP 02','CI Angle','แตกมุมครีเอทีฟตามบุคลิกกลุ่มคน<ul><li>Emotion / Care</li><li>Reaction / Concern</li><li>Interest signal</li></ul>','pink','pastel-pink'),('STEP 03','Test Zone','เว้นพื้นที่ไว้สำหรับเทส<ul><li>Hook</li><li>Visual</li><li>Message</li></ul>','amber','pastel-amber'),('STEP 04','Scale Zone','ขยายเฉพาะ CI ที่เริ่มชนะ<ul><li>Duplicate angle</li><li>แตก Persona</li><li>เพิ่ม Budget</li></ul>','bot','pastel-mint')]
    for col,card in zip([c1,c2,c3,c4],cards):
        with col: st.markdown(f'<div class="card {card[4]}"><span class="pill {card[3]}">{card[0]}</span><h3>{card[1]}</h3><p>{card[2]}</p></div>', unsafe_allow_html=True)
    close_module()

def render_persona_creative():
    open_module('02_PERSONA_CREATIVE_MODULE','ใช้ Persona เพื่อสร้าง CI และคัด Interest ที่ใช้ได้จริง')
    p1,p2,p3=st.columns([1,1,.72])
    with p1: st.markdown('<div class="persona-card pastel-pink"><div class="person-icon">👩‍❤️‍👨</div><span class="pill pink">PERSONA 01 · คู่รัก</span><h3>คนรักเป็นตัวสะกิดให้เริ่มลด</h3><div class="age-box"><b>ช่วงอายุที่โฟกัส:</b><br>หญิง/ชาย 22–38 ปี · คู่รัก/แต่งงาน/อยู่ด้วยกัน</div><p><b>บทบาทคนรัก:</b> ไม่ด่า ไม่บังคับ แต่แสดง Reaction ว่ากลิ่นบุหรี่ทำให้ความใกล้ชิดหายไป</p></div>', unsafe_allow_html=True)
    with p2: st.markdown('<div class="persona-card pastel-lav"><div class="person-icon">🧑‍🦳👩‍🦱</div><span class="pill mid">PERSONA 02 · ดูแลผู้สูงอายุ</span><h3>คนในบ้านเป็นแรงห่วงใย</h3><div class="age-box"><b>ช่วงอายุที่โฟกัส:</b><br>ผู้ดูแล 28–50 ปี · ผู้สูงอายุในบ้าน 55+ ปี</div><p><b>บทบาทผู้ดูแล:</b> สื่อว่าควัน/กลิ่นบุหรี่กระทบคนแก่ในบ้าน จึงอยากให้เริ่มลดแบบค่อยเป็นค่อยไป</p></div>', unsafe_allow_html=True)
    with p3: st.markdown('<div class="unknown-card"><div class="unknown-mark">???</div><span class="pill amber">NEXT PERSONA</span><p>เว้นไว้เตรียมขยับเพิ่ม เมื่อผลเทสบอกว่ามีกลุ่มใหม่ที่ตอบสนองกับ CI</p></div>', unsafe_allow_html=True)
    close_module()

def render_traffic_to_retarget_pipe():
    open_module('03_TRAFFIC_CI_TO_RETARGET_PIPE_MODULE','Traffic CI 2 ตัวไหลรวมเข้า Retarget Pool แล้วส่งเข้า MID Retarget')
    st.markdown('<div class="visual-flow"><div class="merge-node pastel-amber"><span class="pill amber">RETARGET POOL</span><h4>Warm Engagement + Traffic Intent</h4><p>รวมคนจาก CI ทั้งสองตัว + กลุ่มเก่าที่มีอยู่</p></div></div>', unsafe_allow_html=True)
    close_module()

def render_mid_target():
    open_module('04_MID_TARGET_MODULE','Retarget คนที่มีสัญญาณสนใจ เพื่อดึงเข้า Line OA')
    m1,m2,m3=st.columns(3)
    with m1: st.markdown('<div class="mini-card pastel-lav"><span class="pill mid">MID ROLE</span><h4>กลุ่มเป้าหมายกลางน้ำ</h4><p>คนที่เห็น TOP CI แล้วเริ่มอินกับ Pain แต่ยังไม่พร้อมซื้อ ต้องพาเข้าสู่บทสนทนาและรีวิวต่อ</p></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="mini-card pastel-sky"><span class="pill top">RETARGET SIGNAL</span><h4>สัญญาณที่ใช้ดึงเข้า MID</h4><p>กลุ่มเก่า: Engaged / Inbox / Click เดิม<br>กลุ่มใหม่: Video View / Engage / Comment จาก Traffic CI</p></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="mini-card pastel-mint"><span class="pill bot">LINE OA GOAL</span><h4>เป้าหมายของ MID</h4><p>ทำให้คนรู้สึกว่า “ควรลองคุย / ควรรับโปร / ควรให้คนในบ้านดู” แล้วดึงเข้า Line OA</p></div>', unsafe_allow_html=True)
    close_module()

def render_test_and_scale_placeholder():
    open_module('05_TEST_AND_SCALE_PLACEHOLDER_MODULE','ช่องสำหรับใส่ Hook / Visual / Message ที่ชนะจากการเทส')
    t1,t2,t3=st.columns(3)
    with t1: st.markdown('<div class="placeholder"><span class="pill amber">TEST SLOT A</span><h4>Hook Test</h4><p>เว้นไว้ใส่ Hook ที่ต้องเทส เช่น คู่รัก / ผู้สูงอายุ / กลิ่นติดตัว</p></div>', unsafe_allow_html=True)
    with t2: st.markdown('<div class="placeholder"><span class="pill amber">TEST SLOT B</span><h4>Visual Test</h4><p>เว้นไว้ใส่มุมภาพ: กอดแล้วถอย, ปิดจมูก, ยื่นลูกอม, สีหน้าเป็นห่วง</p></div>', unsafe_allow_html=True)
    with t3: st.markdown('<div class="placeholder"><span class="pill bot">SCALE SLOT</span><h4>Scale Candidate</h4><p>เว้นไว้ใส่ CI ที่ชนะ แล้วแตก Angle / Duplicate / เพิ่มงบ</p></div>', unsafe_allow_html=True)
    close_module()

def black_open(kicker,title,desc):
    st.markdown(f'<div class="black-module"><div class="black-kicker">{kicker}</div><div class="black-title">{title}</div><p class="black-desc">{desc}</p>', unsafe_allow_html=True)
def black_close(): st.markdown('</div>', unsafe_allow_html=True)

def render_report_andromeda_module():
    black_open('00_AI_OPTIMIZATION_GAP','ช่องว่างของระบบหลังใช้ Andromeda / Advantage+','ปัญหาไม่ได้อยู่ที่ Andromeda ใช้ไม่ได้ แต่อยู่ที่ระบบของเรายังไม่มี Creative + Offer + Data Signal ที่พร้อมพอให้ AI วิ่งหาลูกค้าที่มีคุณภาพได้เต็มศักยภาพ')
    st.markdown('<div class="minimal-pipe-wrap"><p class="minimal-note"><b>Andromeda เป็นตัวเร่ง</b> แต่เชื้อเพลิงคือ Creative + Offer และเข็มทิศคือ Data Signal ถ้าสองส่วนนี้ยังไม่ชัด ระบบอาจเรียนรู้จาก Click / Message มากกว่า Buyer Signal</p><p class="minimal-fun-note"><b>ตอนนี้ Andromeda เหมือนเด็กขยันที่วิ่งเร็วมาก แต่เข็มทิศยังไม่แม่น</b><br>เพราะคนดูคลิปเราเยอะมาก ระบบเลยอาจจำว่า Video Viewer / Click / Message คือสัญญาณของลูกค้าคุณภาพ แล้วขยันส่งแอดไปหาคนลักษณะเดียวกันซ้ำ ๆ ผลคือทักเข้ามาได้จริง แต่หลายคนยังไม่มีกำลังซื้อหรือยังไม่พร้อมจ่าย</p>', unsafe_allow_html=True)
    render_heatmap_path()
    c1,a1,c2,a2,c3,a3,c4=st.columns([1,.07,1,.07,1,.07,1])
    steps=[('ยอดลดหลังใช้ Advantage+','ระบบเริ่มพึ่ง AI Optimization มากขึ้น แต่ Signal หลังบ้านยังไม่พร้อม'),('Creative + Offer ต้องตอบโจทย์','Hook, Pain, ราคา และเหตุผลซื้อ ต้องดึงคนที่มี Intent จริงเข้ามา'),('Pixel / Event ต้องส่งสัญญาณ','ระบบต้องรู้ว่าใครเห็นราคา กด LINE รับราคา และซื้อจริง'),('AI หา Buyer Pattern','เมื่อ Signal ดีขึ้น Retarget / Lookalike / Scale จะเริ่มแม่นขึ้น')]
    for col,x in zip([c1,c2,c3,c4],steps):
        with col: st.markdown(f'<div class="minimal-step"><h4>{x[0]}</h4><p>{x[1]}</p></div>', unsafe_allow_html=True)
    for a in [a1,a2,a3]:
        with a: st.markdown('<div class="minimal-arrow">→</div>', unsafe_allow_html=True)
    l,r=st.columns(2)
    with l: st.markdown('<div class="minimal-compare"><h4>ถ้าระบบยังไม่พร้อม</h4><p>Creative + Offer ไม่คม หรือ Data Signal ไม่พอ → AI เรียนรู้จาก Click / Message → Lead ดูถูก แต่ Close ต่ำ → CAC จริงแพง / Scale ไม่เต็มที่</p></div>', unsafe_allow_html=True)
    with r: st.markdown('<div class="minimal-compare"><h4>ถ้าระบบพร้อม</h4><p>Creative + Offer ตอบโจทย์ + Pixel/Event ส่งสัญญาณ → AI เข้าใจ Buyer Pattern → Lead คุณภาพดีขึ้น → Retarget / Scale ทำงานดีขึ้น</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="minimal-ref"><h4>Reference Example: ยันฮี</h4><p>บางสินค้าอย่างยันฮีอาจมี Pixel / Event บางส่วนส่งกลับเข้า Meta แม้ข้อมูลอาจไม่ตรง 100% แต่ยังทำให้ระบบมี Signal มากกว่าการพึ่ง Creative + Message เพียงอย่างเดียว</p></div></div>', unsafe_allow_html=True)
    black_close()

def render_report_tab():
    tab_andromeda = st.tabs(['อันโดเมด้า'])[0]
    with tab_andromeda:
        render_report_andromeda_module()

def render_planning_tab():
    render_budget_plan(); render_date_project(); render_top_ci_workflow(); render_persona_creative(); render_traffic_to_retarget_pipe(); render_mid_target(); render_test_and_scale_placeholder()

def render_footer(): st.markdown('<div class="footer-note">Pastel Marketing Board · Smoking Candy · Modular Workflow</div>', unsafe_allow_html=True)

def main():
    render_theme(); render_header()
    tab_plan, tab_report = st.tabs(['📌 วางแผนงาน', '📊 รายงานผู้บริหาร'])
    with tab_plan: render_planning_tab()
    with tab_report: render_report_tab()
    render_footer()

if __name__=='__main__': main()