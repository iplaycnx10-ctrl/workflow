import streamlit as st


def render_theme():
    st.markdown("""
    <style>
    :root{--bg:#fbfbfe;--ink:#1f2937;--muted:#6b7280;--line:#e9edf5;--blue:#dbeafe;--blue-text:#1d4ed8;--lav:#ede9fe;--lav-text:#6d28d9;--mint:#dcfce7;--mint-text:#15803d;--pink:#fce7f3;--pink-text:#be185d;--amber:#fef3c7;--amber-text:#b45309;--sky:#e0f2fe;--sky-text:#0369a1;--black:#050608;--cyan:#38bdf8}
    .stApp{background:radial-gradient(circle at top left,#fdf2f8 0,transparent 28%),radial-gradient(circle at top right,#dbeafe 0,transparent 26%),radial-gradient(circle at bottom,#dcfce7 0,transparent 24%),var(--bg);color:var(--ink)}
    [data-testid="stSidebar"]{display:none}.main .block-container{padding-top:2.2rem;max-width:1280px}
    .module-wrap{background:rgba(255,255,255,.52);border:1px solid rgba(237,240,247,.95);border-radius:30px;padding:22px 22px 26px;margin:28px 0;box-shadow:0 18px 48px rgba(31,41,55,.035)}
    .module-title{font-size:14px;font-weight:850;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin:0}.module-desc{color:var(--muted);font-size:13px;line-height:1.55;margin:4px 0 16px}
    .hero,.card,.mini-card,.persona-card,.insight-card,.flow-node,.merge-node,.budget-card,.placeholder,.date-card{border:1px solid var(--line);box-shadow:0 12px 36px rgba(31,41,55,.045)}
    .hero{border-radius:28px;padding:28px 30px;margin-bottom:20px;background:linear-gradient(135deg,#fff,#fdf2f8 52%,#eff6ff)}.eyebrow{display:inline-flex;padding:7px 12px;border-radius:999px;background:#fff;border:1px solid var(--line);color:var(--muted);font-size:13px;margin-bottom:12px}.title{font-size:38px;font-weight:850;letter-spacing:-.04em;margin:0;color:var(--ink)}.subtitle{color:var(--muted);font-size:16px;margin-top:8px;line-height:1.7}
    .pill{display:inline-block;padding:7px 11px;border-radius:999px;font-size:12px;font-weight:750;margin-bottom:12px}.top{background:var(--blue);color:var(--blue-text)}.mid{background:var(--lav);color:var(--lav-text)}.bot{background:var(--mint);color:var(--mint-text)}.pink{background:var(--pink);color:var(--pink-text)}.amber{background:var(--amber);color:var(--amber-text)}.sky{background:var(--sky);color:var(--sky-text)}
    .card,.budget-card,.mini-card,.persona-card,.insight-card,.flow-node,.merge-node,.placeholder,.date-card{border-radius:20px;padding:18px;background:#fff}.card{min-height:270px;border-radius:24px}.budget-card{min-height:190px}.date-card{min-height:225px}.mini-card{min-height:175px}.persona-card{min-height:425px}.placeholder{min-height:190px;border:1.5px dashed #cbd5e1}
    .age-box{background:rgba(255,255,255,.72);border:1px solid var(--line);border-radius:14px;padding:10px 12px;margin:10px 0 12px;color:var(--ink);font-size:13.5px;line-height:1.5}.pastel-blue{background:linear-gradient(135deg,#fff,#dbeafe)}.pastel-pink{background:linear-gradient(135deg,#fff,#fce7f3)}.pastel-lav{background:linear-gradient(135deg,#fff,#ede9fe)}.pastel-mint{background:linear-gradient(135deg,#fff,#dcfce7)}.pastel-amber{background:linear-gradient(135deg,#fff,#fef3c7)}.pastel-sky{background:linear-gradient(135deg,#fff,#e0f2fe)}
    h3,h4{margin:0 0 8px;color:var(--ink);letter-spacing:-.02em}p,li{color:var(--muted);line-height:1.62;font-size:14px}.budget-number{font-size:30px;font-weight:900;letter-spacing:-.04em;color:var(--ink);margin:2px 0 10px}.arrow-row{display:flex;align-items:center;justify-content:center;min-height:170px;color:#c4c9d4;font-size:30px;font-weight:800}.flow-line{height:3px;border-radius:99px;background:linear-gradient(90deg,#bfdbfe,#fbcfe8,#ddd6fe,#bbf7d0);margin:12px 0 20px}.visual-flow{margin-top:18px;padding:22px;border-radius:26px;background:rgba(255,255,255,.66);border:1px solid var(--line)}.person-icon{font-size:42px;margin-bottom:8px}.unknown-card{min-height:425px;border:1.5px dashed #cbd5e1;background:linear-gradient(135deg,#fff,#f8fafc);border-radius:20px;padding:18px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}.unknown-mark{font-size:58px;font-weight:900;color:#94a3b8}
    .black-module{background:linear-gradient(135deg,rgba(13,17,23,.96),rgba(15,23,42,.86));border:1px solid #273142;border-radius:28px;padding:24px;margin:24px 0;box-shadow:0 20px 60px rgba(0,0,0,.22)}.black-kicker{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#94a3b8;font-weight:850}.black-title{font-size:30px;line-height:1.18;letter-spacing:-.04em;color:#f8fafc;font-weight:950;margin:6px 0 8px}.black-desc{font-size:14px;line-height:1.65;color:#94a3b8;margin:0 0 18px}
    .minimal-pipe-wrap{background:rgba(255,255,255,.92);border:1px solid rgba(226,232,240,.95);border-radius:26px;padding:22px;margin:16px 0;color:#111827;box-shadow:0 18px 44px rgba(15,23,42,.08)}.minimal-step{background:transparent;border-left:3px solid #cbd5e1;padding:2px 0 2px 16px;min-height:72px}.minimal-step h4{color:#0f172a;font-size:17px;margin:0 0 5px}.minimal-step p{color:#475569;font-size:13px;margin:0}.minimal-arrow{display:flex;align-items:center;justify-content:center;color:#94a3b8;font-size:26px;font-weight:900;min-height:72px}.minimal-note{color:#334155;font-size:13px;line-height:1.7;margin:0 0 16px}.minimal-fun-note{color:#0f172a;font-size:14px;line-height:1.8;margin:0 0 16px;padding:12px 14px;border-left:4px solid #38bdf8;background:linear-gradient(90deg,#eff6ff,#ffffff);border-radius:14px}.signal-path{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:10px 0 18px}.signal-chip{font-size:12px;font-weight:850;color:#0f172a;background:#f8fafc;border:1px solid #e2e8f0;border-radius:999px;padding:9px 12px}.signal-arrow{color:#94a3b8;font-weight:950}.minimal-compare{border-top:1px solid #e2e8f0;padding-top:16px;margin-top:18px}.minimal-compare h4{color:#0f172a;font-size:16px}.minimal-compare p{color:#475569;font-size:13px}.minimal-ref{background:linear-gradient(90deg,#eff6ff,#f0fdf4);border:1px solid #dbeafe;border-radius:18px;padding:14px;margin-top:16px}.footer-note{color:var(--muted);text-align:center;padding:20px 0 6px;font-size:13px}
    </style>""", unsafe_allow_html=True)


def open_module(title: str, desc: str):
    st.markdown(f'<div class="module-wrap"><div class="module-title">{title}</div><p class="module-desc">{desc}</p>', unsafe_allow_html=True)


def close_module():
    st.markdown('</div>', unsafe_allow_html=True)


def render_header():
    st.markdown('<div class="hero"><div class="eyebrow">🍬 Project Board · Modular</div><h1 class="title">ลูกอมบุหรี่ — Smoking Candy Workflow</h1><div class="subtitle">แยก Modular เป็นขั้นตอน: วางแผนงาน → รายงานผู้บริหาร</div></div>', unsafe_allow_html=True)


def render_footer():
    st.markdown('<div class="footer-note">Pastel Marketing Board · Smoking Candy · Modular Workflow</div>', unsafe_allow_html=True)
