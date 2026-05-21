import streamlit as st

from modules.theme import render_theme
from modules.header import render_header
from modules.budget import render_budget_plan
from modules.date_project import render_date_project
from modules.top_funnel import render_top_ci_workflow
from modules.persona import render_persona_creative
from modules.traffic_pipe import render_traffic_to_retarget_pipe
from modules.mid_target import render_mid_target
from modules.test_scale import render_test_and_scale_placeholder
from modules.bot_funnel import render_lower_funnel
from modules.footer import render_footer


st.set_page_config(
    page_title="ลูกอมบุหรี่ | Work Flow Board",
    page_icon="🍬",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def main():
    render_theme()
    render_header()
    render_budget_plan()
    render_date_project()
    render_top_ci_workflow()
    render_persona_creative()
    render_traffic_to_retarget_pipe()
    render_mid_target()
    render_test_and_scale_placeholder()
    render_lower_funnel()
    render_footer()


if __name__ == "__main__":
    main()
