import streamlit as st

from ui.action_plan_styles import render_action_plan_styles
from ui.action_plan_ldp import render_ldp_plan_tab
from ui.action_plan_pixel import render_pixel_plan_tab
from ui.action_plan_ga4 import render_ga4_plan_tab
from ui.action_plan_dropoff import render_dropoff_plan_tab
from ui.action_plan_case import render_case_plan_tab
from ui.action_plan_stability import render_stability_plan_tab


def render_action_plan_module():
    render_action_plan_styles()

    tabs = st.tabs([
        "01 ปรับ LDP",
        "02 Pixel",
        "03 GA4",
        "04 Drop-off",
        "05 Case 1 วัน",
        "06 ระบบเสถียร",
    ])

    with tabs[0]:
        render_ldp_plan_tab()

    with tabs[1]:
        render_pixel_plan_tab()

    with tabs[2]:
        render_ga4_plan_tab()

    with tabs[3]:
        render_dropoff_plan_tab()

    with tabs[4]:
        render_case_plan_tab()

    with tabs[5]:
        render_stability_plan_tab()
