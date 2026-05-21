import streamlit as st

st.set_page_config(page_title="ลูกอมบุหรี่ | Work Flow Board", page_icon="🍬", layout="wide", initial_sidebar_state="collapsed")

def render_theme():
    st.markdown("""
    <style>
    :root{--bg:#fbfbfe;--ink:#1f2937;--muted:#6b7280;--line:#e9edf5;--blue:#dbeafe;--blue-text:#1d4ed8;--lav:#ede9fe;--lav-text:#6d28d9;--mint:#dcfce7;--mint-text:#15803d;--pink:#fce7f3;--pink-text:#be185d;--amber:#fef3c7;--amber-text:#b45309;--sky:#e0f2fe;--sky-text:#0369a1;--rose:#ffe4e6;--rose-text:#be123c}
    .stApp{background:radial-gradient(circle at top left,#fdf2f8 0,transparent 28%),radial-gradient(circle at top right,#dbeafe 0,transparent 26%),radial-gradient(circle at bottom,#dcfce7 0,transparent 24%),var(--bg);color:var(--ink)}[data-testid="stSidebar"]{display:none}.main .block-container{padding-top:2.2rem;max-width:1280px}.module-wrap{background:rgba(255,255,255,.52);border:1px solid rgba(237,240,247,.95);border-radius:30px;padding:22px 22px 26px;margin:28px 0;box-shadow:0 18px 48px rgba(31,41,55,.035)}.module-title{font-size:14px;font-weight:850;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin:0}.module-desc{color:var(--muted);font-size:13px;line-height:1.55;margin:4px 0 16px}.hero,.card,.mini-card,.persona-card,.insight-card,.ci-card,.flow-node,.merge-node,.budget-card,.placeholder,.date-card{border:1px solid var(--line);box-shadow:0 12px 36px rgba(31,41,55,.045)}.hero{border-radius:28px;padding:28px 30px;margin-bottom:20px;background:linear-gradient(135deg,#fff,#fdf2f8 52%,#eff6ff)}.eyebrow{display:inline-flex;padding:7px 12px;border-radius:999px;background:#fff;border:1px solid var(--line);color:var(--muted);font-size:13px;margin-bottom:12px}.title{font-size:38px;font-weight:850;letter-spacing:-.04em;margin:0;color:var(--ink)}.subtitle{color:var(--muted);font-size:16px;margin-top:8px;line-height:1.7}.pill{display:inline-block;padding:7px 11px;border-radius:999px;font-size:12px;font-weight:750;margin-bottom:12px}.top{background:var(--blue);color:var(--blue-text)}.mid{background:var(--lav);color:var(--lav-text)}.bot{background:var(--mint);color:var(--mint-text)}.pink{background:var(--pink);color:var(--pink-text)}.amber{background:var(--amber);color:var(--amber-text)}.sky{background:var(--sky);color:var(--sky-text)}.rose{background:var(--rose);color:var(--rose-text)}.card,.budget-card,.mini-card,.persona-card,.insight-card,.ci-card,.flow-node,.merge-node,.placeholder,.date-card{border-radius:20px;padding:18px;background:#fff}.card{min-height:270px;border-radius:24px}.budget-card{min-height:190px}.date-card{min-height:225px}.mini-card{min-height:175px}.persona-card{min-height:425px}.insight-card{min-height:160px;margin-top:18px}.ci-card{min-height:390px;margin-top:18px}.flow-node{min-height:170px}.merge-node{min-height:190px}.placeholder{min-height:190px;border:1.5px dashed #cbd5e1}.date-number{font-size:32px;font-weight:950;letter-spacing:-.05em;color:var(--ink);margin:0 0 8px}.age-box{background:rgba(255,255,255,.72);border:1px solid var(--line);border-radius:14px;padding:10px 12px;margin:10px 0 12px;color:var(--ink);font-size:13.5px;line-height:1.5}.pastel-blue{background:linear-gradient(135deg,#fff,#dbeafe)}.pastel-pink{background:linear-gradient(135deg,#fff,#fce7f3)}.pastel-lav{background:linear-gradient(135deg,#fff,#ede9fe)}.pastel-mint{background:linear-gradient(135deg,#fff,#dcfce7)}.pastel-amber{background:linear-gradient(135deg,#fff,#fef3c7)}.pastel-sky{background:linear-gradient(135deg,#fff,#e0f2fe)}.pastel-rose{background:linear-gradient(135deg,#fff,#ffe4e6)}h3,h4{margin:0 0 8px;color:var(--ink);letter-spacing:-.02em}p,li{color:var(--muted);line-height:1.62;font-size:14px}.budget-number{font-size:30px;font-weight:900;letter-spacing:-.04em;color:var(--ink);margin:2px 0 10px}.arrow-row{display:flex;align-items:center;justify-content:center;min-height:270px;color:#c4c9d4;font-size:30px;font-weight:800}.flow-line{height:3px;border-radius:99px;background:linear-gradient(90deg,#bfdbfe,#fbcfe8,#ddd6fe,#bbf7d0);margin:12px 0 20px}.ci-meta{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}.ci-meta div{background:rgba(255,255,255,.7);border:1px solid var(--line);border-radius:14px;padding:10px;color:var(--muted);font-size:13px;line-height:1.45}.visual-flow{margin-top:18px;padding:22px;border-radius:26px;background:rgba(255,255,255,.66);border:1px solid var(--line)}.pipe-down{height:34px;display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:30px;font-weight:900}.pipe-h{height:4px;border-radius:999px;background:linear-gradient(90deg,#fbcfe8,#bfdbfe);margin:15px 0}.pipe-v{width:4px;height:34px;border-radius:999px;background:#cbd5e1;margin:0 auto}.person-icon{font-size:42px;margin-bottom:8px}.unknown-card{min-height:425px;border:1.5px dashed #cbd5e1;background:linear-gradient(135deg,#fff,#f8fafc);border-radius:20px;padding:18px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}.unknown-mark{font-size:58px;font-weight:900;color:#94a3b8}.footer-note{color:var(--muted);text-align:center;padding:20px 0 6px;font-size:13px}
    </style>""", unsafe_allow_html=True)

def open_module(t,d): st.markdown(f'<div class="module-wrap"><div class="module-title">{t}</div><p class="module-desc">{d}</p>', unsafe_allow_html=True)
def close_module(): st.markdown('</div>', unsafe_allow_html=True)
def render_header(): st.markdown('<div class="hero"><div class="eyebrow">🍬 Project Board · Pastel Minimal</div><h1 class="title">ลูกอมบุหรี่ — Smoking Candy Workflow</h1><div class="subtitle">แยก Modular เป็นขั้นตอน: วางแผนงาน → ปัญหาที่เจอ → แนวทางแก้ไข</div></div>', unsafe_allow_html=True)

def render_budget_plan():
    open_module('00_BUDGET_AND_AD_MANAGEMENT_PLAN','งบเฉลี่ยสำหรับเริ่มยิงและแผนแบ่งงบตอน Manage Ads')
    cols=st.columns(4); data=[('TOTAL TEST BUDGET','งบเฉลี่ยเริ่มต้น','1,600–3,000฿','ใช้เป็นงบทดสอบ Funnel ชุดแรก เพื่อดูว่า CI ไหนสร้าง signal ดีพอจะ Retarget ต่อ','top','pastel-blue'),('TRAFFIC CI 01','คู่รัก','600–1,000฿','เริ่มยิงตั้งแต่วันที่ 1 เพื่อหา signal จากมุมแฟนไม่โอเคกับกลิ่น','pink','pastel-pink'),('TRAFFIC CI 02','ดูแลผู้สูงอายุ','600–1,000฿','เริ่มยิงตั้งแต่วันที่ 1 เพื่อหา signal จากมุมคนในบ้านเป็นห่วง','mid','pastel-lav'),('RETARGET / MID','ดึงเข้า Line OA','400–1,000฿','เปิดตั้งแต่วันแรกเพื่อรีกลุ่มเก่าก่อน แล้วค่อยเพิ่ม CI รับ Traffic ใหม่เมื่อ Traffic หลักเริ่มแน่น','amber','pastel-amber')]
    for c,x in zip(cols,data):
        with c: st.markdown(f'<div class="budget-card {x[5]}"><span class="pill {x[4]}">{x[0]}</span><h4>{x[1]}</h4><div class="budget-number">{x[2]}</div><p>{x[3]}</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="insight-card pastel-mint"><span class="pill bot">AD MANAGEMENT NOTE</span><h4>ยิงพร้อมกันตั้งแต่วันแรก</h4><p>Phase แรกให้เปิด Traffic CI 01, Traffic CI 02 และ Retarget กลุ่มเก่าพร้อมกันตั้งแต่วันแรก เพื่อเก็บ signal และไม่ปล่อย Warm audience หลุด วันที่ 1–3 คือช่วงดูผล ปรับงบ และค่อยเพิ่ม CI Retarget ที่รับ Traffic ใหม่เมื่อ Traffic หลักเริ่มแน่น</p></div>', unsafe_allow_html=True); close_module()

def render_date_project():
    open_module('00_DATE_PROJECT_MODULE','วันที่ 1–3 ไม่ใช่วันเริ่มยิงคนละตัว แต่คือช่วง monitor หลังจากยิงทุก CI ตั้งแต่วันแรก')
    d1,d2,d3=st.columns(3)
    with d1: st.markdown('<div class="date-card pastel-pink"><span class="pill pink">DAY 1</span><div class="date-number">วันที่ 1</div><h4>Launch พร้อมกัน</h4><p>เปิด Traffic CI 01 คู่รัก + Traffic CI 02 ผู้สูงอายุ + Retarget กลุ่มเก่าพร้อมกันตั้งแต่วันแรก เพื่อเริ่มเก็บ signal</p></div>', unsafe_allow_html=True)
    with d2: st.markdown('<div class="date-card pastel-lav"><span class="pill mid">DAY 2</span><div class="date-number">วันที่ 2</div><h4>Monitor Signal</h4><p>ดูว่า CI ไหนเริ่มมีสัญญาณดีกว่า เช่น View, Click, Engage, Comment intent และคุณภาพกลุ่มที่เข้ามา</p></div>', unsafe_allow_html=True)
    with d3: st.markdown('<div class="date-card pastel-mint"><span class="pill bot">DAY 3</span><div class="date-number">วันที่ 3</div><h4>Optimize / เพิ่ม Retarget Layer</h4><p>ถ้า Traffic หลักเริ่มแน่น ค่อยเพิ่ม CI Retarget ที่รับคนจาก Traffic CI 01–02 เข้า Line OA หรือโยกงบไปฝั่งที่ชนะ</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="insight-card pastel-sky"><span class="pill top">PROJECT NOTE</span><h4>Logic วันที่ 1–3</h4><p>ทุก CI เริ่มยิงตั้งแต่วันที่ 1 อยู่แล้ว ส่วนวันที่ 2–3 คือช่วงอ่านผลและตัดสินใจว่าจะเพิ่ม Retarget CI ตัวที่รับ Traffic ใหม่หรือยัง ไม่ใช่รอเปิดยิงทีละวัน</p></div>', unsafe_allow_html=True); close_module()

def render_top_ci_workflow():
    open_module('01_TOP_FUNNEL_CI_FIRST_WORKFLOW_MODULE','เริ่มจาก Persona → CI Angle → Test → Scale')
    st.markdown('<div class="flow-line"></div>', unsafe_allow_html=True); c1,a1,c2,a2,c3,a3,c4=st.columns([1.05,.12,1.05,.12,1.05,.12,1.05])
    cards=[('STEP 01','Persona','เลือกกลุ่มคนให้ชัดก่อนทำ CI<ul><li>คู่รัก</li><li>คนดูแลผู้สูงอายุ</li><li>??? กลุ่มใหม่จากผลเทส</li></ul>','top','pastel-blue'),('STEP 02','CI Angle','แตกมุมครีเอทีฟตามบุคลิกกลุ่มคน<ul><li>Emotion / Care</li><li>Reaction / Concern</li><li>Interest signal</li></ul>','pink','pastel-pink'),('STEP 03','Test Zone','เว้นพื้นที่ไว้สำหรับเทส<ul><li>Hook</li><li>Visual</li><li>Message</li></ul>','amber','pastel-amber'),('STEP 04','Scale Zone','ขยายเฉพาะ CI ที่เริ่มชนะ<ul><li>Duplicate angle</li><li>แตก Persona</li><li>เพิ่ม Budget</li></ul>','bot','pastel-mint')]
    for col,card in zip([c1,c2,c3,c4],cards):
        with col: st.markdown(f'<div class="card {card[4]}"><span class="pill {card[3]}">{card[0]}</span><h3>{card[1]}</h3><p>{card[2]}</p></div>', unsafe_allow_html=True)
    for a in [a1,a2,a3]:
        with a: st.markdown('<div class="arrow-row">→</div>', unsafe_allow_html=True)
    close_module()

def render_persona_creative():
    open_module('02_PERSONA_CREATIVE_MODULE','ใช้ Persona เพื่อสร้าง CI และคัด Interest ที่ใช้ได้จริง')
    p1,p2,p3=st.columns([1,1,.72])
    with p1: st.markdown('<div class="persona-card pastel-pink"><div class="person-icon">👩‍❤️‍👨</div><span class="pill pink">PERSONA 01 · คู่รัก</span><h3>คนรักเป็นตัวสะกิดให้เริ่มลด</h3><div class="age-box"><b>ช่วงอายุที่โฟกัส:</b><br>หญิง/ชาย 22–38 ปี · คู่รัก/แต่งงาน/อยู่ด้วยกัน</div><p><b>บทบาทคนรัก:</b> ไม่ด่า ไม่บังคับ แต่แสดง Reaction ว่ากลิ่นบุหรี่ทำให้ความใกล้ชิดหายไป</p><ul><li>แฟนกอดแล้วชะงัก</li><li>ดมเสื้อแล้วถอยออกเบาๆ</li><li>ยื่นลูกอมให้แบบห่วง ไม่ประชด</li></ul></div>', unsafe_allow_html=True)
    with p2: st.markdown('<div class="persona-card pastel-lav"><div class="person-icon">🧑‍🦳👩‍🦱</div><span class="pill mid">PERSONA 02 · ดูแลผู้สูงอายุ</span><h3>คนในบ้านเป็นแรงห่วงใย</h3><div class="age-box"><b>ช่วงอายุที่โฟกัส:</b><br>ผู้ดูแล 28–50 ปี · ผู้สูงอายุในบ้าน 55+ ปี</div><p><b>บทบาทผู้ดูแล:</b> สื่อว่าควัน/กลิ่นบุหรี่กระทบคนแก่ในบ้าน จึงอยากให้เริ่มลดแบบค่อยเป็นค่อยไป</p><ul><li>ลูก/หลานเห็นผู้สูงอายุไอหรือปิดจมูก</li><li>หยิบลูกอมให้พ่อ/แม่/คนในบ้าน</li><li>พูดด้วยโทนเป็นห่วง ไม่ตำหนิ</li></ul></div>', unsafe_allow_html=True)
    with p3: st.markdown('<div class="unknown-card"><div class="unknown-mark">???</div><span class="pill amber">NEXT PERSONA</span><p>เว้นไว้เตรียมขยับเพิ่ม เมื่อผลเทสบอกว่ามีกลุ่มใหม่ที่ตอบสนองกับ CI</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="insight-card pastel-sky"><span class="pill top">INSIGHT</span><h4>ทำ Persona ไว้เพื่อคัด Interest สำหรับกลุ่ม CI</h4><p>ใช้หา “กลุ่มเป้าหมายที่ใช้ได้จริง” จากผลตอบสนองของ Creative แล้วเอา Insight ไปคัด Interest / Audience / Angle สำหรับรอบ Test และ Scale ต่อ</p></div>', unsafe_allow_html=True); close_module()

def render_traffic_to_retarget_pipe():
    open_module('03_TRAFFIC_CI_TO_RETARGET_PIPE_MODULE','Traffic CI 2 ตัวไหลรวมเข้า Retarget Pool แล้วส่งเข้า MID Retarget')
    st.markdown('<div class="visual-flow">', unsafe_allow_html=True); top1,gap,top2=st.columns([1,.16,1])
    with top1: st.markdown('<div class="flow-node pastel-pink"><span class="pill pink">TRAFFIC CI 01</span><h4>คู่รัก / แฟนไม่โอเคกับกลิ่น</h4><p>สร้างสัญญาณจาก Pain ความสัมพันธ์</p><ul><li>Video View</li><li>Click / Engage</li><li>Comment / Share / Save</li></ul></div><div class="pipe-v"></div><div class="pipe-down">↓</div>', unsafe_allow_html=True)
    with top2: st.markdown('<div class="flow-node pastel-lav"><span class="pill mid">TRAFFIC CI 02</span><h4>ดูแลผู้สูงอายุ / คนในบ้านเป็นห่วง</h4><p>สร้างสัญญาณจาก Pain ครอบครัว</p><ul><li>Video View</li><li>Click / Engage</li><li>Comment เรื่องคนในบ้าน</li></ul></div><div class="pipe-v"></div><div class="pipe-down">↓</div>', unsafe_allow_html=True)
    l,cen,r=st.columns([1,.56,1])
    with l: st.markdown('<div class="pipe-h"></div>', unsafe_allow_html=True)
    with cen: st.markdown('<div class="merge-node pastel-amber"><span class="pill amber">RETARGET POOL</span><h4>Warm Engagement + Traffic Intent</h4><p>รวมคนจาก CI ทั้งสองตัว + กลุ่มเก่าที่มีอยู่</p><ul><li>Old Warm: Engaged / Inbox / Click / Video View เดิม</li><li>New Warm: Video View / Engaged 7–14 วัน</li><li>Comment / Save / Share / Inbox 14–30 วัน</li></ul></div>', unsafe_allow_html=True)
    with r: st.markdown('<div class="pipe-h"></div>', unsafe_allow_html=True)
    st.markdown('<div class="pipe-v"></div><div class="pipe-down">↓</div><div class="merge-node pastel-mint"><span class="pill bot">MID RETARGET</span><h4>ส่งต่อเข้า CI กลางน้ำ</h4><p>Phase แรกรีกลุ่มเก่าก่อน แล้วค่อยเพิ่ม CI Retarget ที่รับ Traffic ใหม่เมื่อ Traffic หลักเริ่มแน่น</p></div></div>', unsafe_allow_html=True); close_module()

def render_mid_target():
    open_module('04_MID_TARGET_MODULE','Retarget คนที่มีสัญญาณสนใจ เพื่อดึงเข้า Line OA')
    m1,m2,m3=st.columns(3)
    with m1: st.markdown('<div class="mini-card pastel-lav"><span class="pill mid">MID ROLE</span><h4>กลุ่มเป้าหมายกลางน้ำ</h4><p>คนที่เห็น TOP CI แล้วเริ่มอินกับ Pain แต่ยังไม่พร้อมซื้อ ต้องพาเข้าสู่บทสนทนาและรีวิวต่อ</p></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="mini-card pastel-sky"><span class="pill top">RETARGET SIGNAL</span><h4>สัญญาณที่ใช้ดึงเข้า MID</h4><p>กลุ่มเก่า: Engaged / Inbox / Click เดิม และกลุ่มใหม่: Video View, Engagement, Save, Share, Comment จาก Traffic CI</p></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="mini-card pastel-mint"><span class="pill bot">MID GOAL</span><h4>เป้าหมายของ MID</h4><p>ทำให้คนรู้สึกว่า “ควรลองคุย / ควรให้แฟนดู / ควรเก็บไว้ถามใน Line OA”</p></div>', unsafe_allow_html=True)
    ci1,ci2=st.columns(2)
    with ci1: st.markdown('<div class="ci-card pastel-pink"><span class="pill mid">MID CI 01 · RETARGET</span><h3>สอบถามแฟน: ถ้าเขาลดได้ คุณอยากให้เขาเริ่มไหม?</h3><p><b>Insight:</b> คนรักไม่ได้อยากบังคับให้เลิกทันที แต่อยากให้เขา “เริ่มลด” เพราะกลิ่นบุหรี่ทำให้ความใกล้ชิดแย่ลง</p><div class="ci-meta"><div><b>Creative Format</b><br>POV Couple / Question scene</div><div><b>Hook</b><br>ลองถามแฟนดู…</div><div><b>Retarget Audience</b><br>Old Warm + คนดู TOP video / Engaged / Click</div><div><b>CTA</b><br>ให้แฟนดู / ทัก Line OA</div></div></div>', unsafe_allow_html=True)
    with ci2: st.markdown('<div class="ci-card pastel-mint"><span class="pill mid">MID CI 02 · RETARGET</span><h3>รีวิวจากแฟน/คนในบ้าน: เขาเริ่มพยายามลดแล้ว</h3><p><b>Insight:</b> คนรอบตัวอยากเห็นสัญญาณว่าเขาเริ่มพยายาม เช่น มีลูกอมติดตัวแทนจังหวะที่อยากสูบ</p><div class="ci-meta"><div><b>Creative Format</b><br>Review scene / Family POV</div><div><b>Hook</b><br>เขายังไม่ได้เลิกทันที…</div><div><b>Retarget Audience</b><br>Engage TOP/MID / Inbox / Save</div><div><b>CTA</b><br>เข้า Line OA / รับโปร / ของแถม</div></div></div>', unsafe_allow_html=True)
    close_module()

def render_test_and_scale_placeholder():
    open_module('05_TEST_AND_SCALE_PLACEHOLDER_MODULE','พื้นที่ใส่ผล Test และ CI ที่ควร Scale')
    t1,t2,t3=st.columns(3)
    with t1: st.markdown('<div class="placeholder pastel-amber"><span class="pill amber">TEST SLOT A</span><h4>Hook Test</h4><p>เว้นไว้ใส่ Hook ที่ต้องเทส เช่น คู่รัก / ผู้สูงอายุ / กลิ่นติดตัว</p></div>', unsafe_allow_html=True)
    with t2: st.markdown('<div class="placeholder pastel-rose"><span class="pill rose">TEST SLOT B</span><h4>Visual Test</h4><p>กอดแล้วถอย, ปิดจมูก, ยื่นลูกอม, สีหน้าเป็นห่วง</p></div>', unsafe_allow_html=True)
    with t3: st.markdown('<div class="placeholder pastel-mint"><span class="pill bot">SCALE SLOT</span><h4>Scale Candidate</h4><p>ใส่ CI ที่ชนะ แล้วแตก Angle / Duplicate / เพิ่มงบ</p></div>', unsafe_allow_html=True)
    close_module()

def render_lower_funnel():
    open_module('06_BOT_FUNNEL_MODULE','BOT ใช้หลัง MID คัดคนสนใจจริงแล้ว')
    c1,c2=st.columns(2)
    with c1: st.markdown('<div class="mini-card pastel-lav"><span class="pill mid">MID SUMMARY</span><h4>Conversation / Line OA</h4><p>ใช้ MID เพื่อพาไปสู่การคุย การรีวิว และการเพิ่มเพื่อน Line OA</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="mini-card pastel-mint"><span class="pill bot">BOT FUNNEL</span><h4>Close / Offer</h4><p>Retarget คนที่เข้า Line OA / ทัก / สนใจสูง ด้วย Offer, Bundle, Review Screenshot และ CTA ซื้อ</p></div>', unsafe_allow_html=True)
    close_module()

def render_problem_summary():
    open_module('01_CURRENT_PROBLEM_SECTION','สรุปปัญหาที่เจอตอนนี้จากเคส Smoking Candy')
    c1,c2,c3=st.columns(3)
    with c1: st.markdown('<div class="mini-card pastel-rose"><span class="pill rose">ปัญหา 01</span><h4>ยอดตกหลังใช้ระบบเดิม</h4><p>มีสัญญาณว่ายอดขายเริ่มตกหลังเปลี่ยนมาใช้ระบบ/โครงแคมเปญเดิมที่ปล่อยให้ระบบหา Conversion เองมากเกินไป</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="mini-card pastel-amber"><span class="pill amber">ปัญหา 02</span><h4>งบ 12,000 ขายได้ 9,000</h4><p>ตัวเลขสะท้อนว่าแคมเปญไม่คุ้มทุนในรอบนี้ และต้องหยุดมองแค่ยอดขายปลายทาง แต่ต้องไล่กลับมาดูคุณภาพ Traffic และ Intent</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="mini-card pastel-lav"><span class="pill mid">ปัญหา 03</span><h4>สินค้าไม่ได้ปิดง่ายเหมือนเดิม</h4><p>ตลาดเห็นสินค้ามานานหลายปี ลูกค้าเริ่มชิน โฆษณาเดิมจึงดึง Demand ได้ยากขึ้น ต้องใช้มุม Creative ที่ใหม่และคัดคนมากกว่าเดิม</p></div>', unsafe_allow_html=True)
    d1,d2,d3=st.columns(3)
    with d1: st.markdown('<div class="mini-card pastel-sky"><span class="pill top">ปัญหา 04</span><h4>Pixel / Event ไม่พร้อม</h4><p>ระบบ Tracking ยังไม่น่าไว้ใจ หรือไม่มี Event สำคัญมากพอ ทำให้การ Optimize แบบอัตโนมัติอาจเรียนรู้จากสัญญาณที่ผิด</p></div>', unsafe_allow_html=True)
    with d2: st.markdown('<div class="mini-card pastel-pink"><span class="pill pink">ปัญหา 05</span><h4>Advantage+ อาจกว้างเกิน</h4><p>สินค้านี้ต้องอาศัย Pain, Trust และการคุยต่อ ถ้าปล่อยกว้างเกินอาจได้คนสนใจผิวเผิน แต่ไม่ใช่คนที่พร้อมจ่ายจริง</p></div>', unsafe_allow_html=True)
    with d3: st.markdown('<div class="mini-card pastel-mint"><span class="pill bot">ปัญหา 06</span><h4>ราคาต้องคัดกรองลูกค้า</h4><p>แพ็ก 3 ซอง 1,000 ไม่ใช่สินค้าราคาถูก จึงต้องสื่อราคาและคุณค่าให้ชัด เพื่อกันคนไม่มีงบออกก่อนและดึงคนที่จริงจังเข้ามา</p></div>', unsafe_allow_html=True)
    close_module()

def render_root_cause_summary():
    open_module('02_ROOT_CAUSE_SECTION','สาเหตุหลักที่เราประเมินจากปัญหา')
    c1,c2,c3,c4=st.columns(4)
    causes=[('CAUSE 01','ระบบกว้างก่อนกลุ่มพร้อม','ปล่อยให้ระบบหาคนเองทั้งที่ข้อมูลเรียนรู้ยังไม่พร้อม ทำให้คุณภาพ Traffic แกว่ง','rose','pastel-rose'),('CAUSE 02','Creative ไม่ได้คัด Intent พอ','Hook/ภาพอาจทำให้คนหยุดดูได้ แต่ยังไม่พอให้รู้ว่าใครมีปัญหาจริงและพร้อมซื้อ','amber','pastel-amber'),('CAUSE 03','Funnel ยังไม่แยก Cold/Warm ชัด','คนใหม่ คนเคยเห็น คนเคยทัก และคนพร้อมซื้อไม่ควรถูกสื่อสารด้วยข้อความเดียวกัน','top','pastel-blue'),('CAUSE 04','Offer ยังไม่ช่วยกรองมากพอ','ถ้าไม่บอกราคา แพ็ก และเหตุผลความคุ้มตั้งแต่ต้น จะได้ Lead ที่คุยเยอะแต่ปิดยาก','bot','pastel-mint')]
    for col,x in zip([c1,c2,c3,c4],causes):
        with col: st.markdown(f'<div class="card {x[4]}"><span class="pill {x[3]}">{x[0]}</span><h3>{x[1]}</h3><p>{x[2]}</p></div>', unsafe_allow_html=True)
    close_module()

def render_fix_direction_summary():
    open_module('01_FIX_DIRECTION_SECTION','แนวทางของเราในการแก้ไขเบื้องต้น')
    a,b,c=st.columns(3)
    with a: st.markdown('<div class="ci-card pastel-blue"><span class="pill top">แนวทาง 01</span><h3>กลับมายิงมือก่อน</h3><p>ลดการพึ่ง Advantage+ ในช่วงที่ Pixel/Event ยังไม่พร้อม แล้วกลับมาคุมโครงสร้าง Campaign ด้วยมือ</p><div class="ci-meta"><div><b>Cold</b><br>ใช้ Traffic CI หา Persona และ Interest</div><div><b>Warm</b><br>ใช้ Retarget คนดู/คลิก/Engage/Inbox</div><div><b>Budget</b><br>แบ่งงบเทสเล็กก่อนโยกงบ</div><div><b>Goal</b><br>หา Signal คุณภาพก่อน Scale</div></div></div>', unsafe_allow_html=True)
    with b: st.markdown('<div class="ci-card pastel-pink"><span class="pill pink">แนวทาง 02</span><h3>ใช้ Creative คัดคน</h3><p>Creative ต้องไม่ใช่แค่สวย แต่ต้องบอกปัญหา กลุ่มเป้าหมาย ราคา และเหตุผลให้คนที่ไม่ใช่ออกไปตั้งแต่ต้น</p><div class="ci-meta"><div><b>Persona</b><br>คู่รัก / คนในบ้าน / ผู้ดูแลผู้สูงอายุ</div><div><b>Hook</b><br>กลิ่นบุหรี่กระทบคนรอบตัว</div><div><b>Message</b><br>เริ่มลด ไม่ขายว่าเลิกทันที</div><div><b>CTA</b><br>ทัก Line OA / รับโปร</div></div></div>', unsafe_allow_html=True)
    with c: st.markdown('<div class="ci-card pastel-mint"><span class="pill bot">แนวทาง 03</span><h3>ทำ Retarget เป็นระบบ</h3><p>ใช้ Traffic CI ปั้น Warm Pool แล้วค่อยส่ง MID/BOT เพื่อปิดการขาย ไม่หวังให้ Cold ปิดทันทีทุกคน</p><div class="ci-meta"><div><b>Pool</b><br>Video View / Engage / Click</div><div><b>MID</b><br>FAQ / Review / คนรอบตัว</div><div><b>BOT</b><br>Offer / Bundle / Screenshot Review</div><div><b>Filter</b><br>3 ซอง 1,000 ส่งฟรี</div></div></div>', unsafe_allow_html=True)
    close_module()

def render_action_plan_summary():
    open_module('02_ACTION_PLAN_SECTION','สิ่งที่ต้องทำต่อทันที')
    s1,s2,s3,s4=st.columns(4)
    actions=[('ACTION 01','พักตัวที่เผางบ','หยุด/ลดงบชุดที่ Spend สูงแต่ไม่มี Inbox, Line OA Add, Comment Intent หรือยอดขายจริง','rose','pastel-rose'),('ACTION 02','เปิด Manual Test','เปิด Traffic CI 2 Persona พร้อม Retarget กลุ่มเก่า ตั้งแต่วันแรก แล้ว monitor 1–3 วัน','top','pastel-blue'),('ACTION 03','ทำ CI แบบคัดลูกค้า','ใส่ Pain + ราคา + ส่งฟรี + CTA ชัด เช่น แพ็ก 3 ซอง 1,000 เพื่อกรองลูกค้าที่ไม่พร้อมซื้อ','pink','pastel-pink'),('ACTION 04','อ่านผลจาก Intent','ตัดสินใจจาก CTR, CPC, Engage, Comment, Inbox, Line OA Add และคุณภาพบทสนทนา ไม่ดู ROAS อย่างเดียว','bot','pastel-mint')]
    for col,x in zip([s1,s2,s3,s4],actions):
        with col: st.markdown(f'<div class="card {x[4]}"><span class="pill {x[3]}">{x[0]}</span><h3>{x[1]}</h3><p>{x[2]}</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="insight-card pastel-amber"><span class="pill amber">สรุปแนวคิดหลัก</span><h4>ตอนนี้ไม่ใช่แค่เปลี่ยนแอด แต่ต้องเปลี่ยนวิธีคัดคน</h4><p>ปัญหาหลักคือระบบเดิมอาจหา Traffic ได้ แต่ไม่ได้การันตีว่าคนเหล่านั้นมี Intent และกำลังซื้อจริง แนวทางแก้คือกลับมาคุม Persona, Creative, Offer, Retarget และการอ่านผลด้วยมือก่อน เมื่อเจอตัวที่ชนะค่อย Scale</p></div>', unsafe_allow_html=True)
    close_module()

def render_planning_tab():
    render_budget_plan(); render_date_project(); render_top_ci_workflow(); render_persona_creative(); render_traffic_to_retarget_pipe(); render_mid_target(); render_test_and_scale_placeholder(); render_lower_funnel()

def render_problem_tab():
    render_problem_summary(); render_root_cause_summary()

def render_solution_tab():
    render_fix_direction_summary(); render_action_plan_summary()

def render_footer(): st.markdown('<div class="footer-note">Pastel Marketing Board · Smoking Candy · Modular Workflow</div>', unsafe_allow_html=True)
def main():
    render_theme(); render_header()
    tab_plan, tab_problem, tab_solution = st.tabs(['📌 วางแผนงาน', '⚠️ ปัญหาที่เจอ', '🛠️ แนวทางแก้ไข'])
    with tab_plan: render_planning_tab()
    with tab_problem: render_problem_tab()
    with tab_solution: render_solution_tab()
    render_footer()
if __name__=='__main__': main()
