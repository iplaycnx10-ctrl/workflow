import streamlit as st


ANDROMEDA_SIGNAL_HEATMAP = [
    {
        "label": "คนดูคลิปเยอะ",
        "bg": "#dcfce7",
        "border": "#86efac",
        "text": "#166534",
        "level": "low-risk",
    },
    {
        "label": "AI จำว่าเป็น Signal ดี",
        "bg": "#fef9c3",
        "border": "#fde047",
        "text": "#854d0e",
        "level": "watch",
    },
    {
        "label": "หาคนชอบดู/ชอบถามเพิ่ม",
        "bg": "#ffedd5",
        "border": "#fdba74",
        "text": "#9a3412",
        "level": "warning",
    },
    {
        "label": "Lead เยอะ แต่ Close ต่ำ",
        "bg": "#fee2e2",
        "border": "#fca5a5",
        "text": "#991b1b",
        "level": "high-risk",
    },
    {
        "label": "CAC จริงแพง",
        "bg": "#fecaca",
        "border": "#f87171",
        "text": "#7f1d1d",
        "level": "critical",
    },
]


def render_heatmap_path(items=ANDROMEDA_SIGNAL_HEATMAP):
    chips = []
    for index, item in enumerate(items):
        chips.append(
            f"""
            <span class=\"heatmap-chip\" style=\"background:{item['bg']};border-color:{item['border']};color:{item['text']};\">
                {item['label']}
            </span>
            """
        )
        if index < len(items) - 1:
            chips.append('<span class="heatmap-arrow">→</span>')

    st.markdown(
        f"""
        <div class="heatmap-path">
            {''.join(chips)}
        </div>
        """,
        unsafe_allow_html=True,
    )
