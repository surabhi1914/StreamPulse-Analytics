# dashboard/streamlit_app.py
"""
Purpose: Provide the starter Streamlit entry point for StreamPulse Analytics.

This file will:
- Configure the dashboard page.
- Display a Phase 0 placeholder message.
- Receive dashboard logic after analytics outputs exist.
"""

import streamlit as st

st.set_page_config(
    page_title="StreamPulse Analytics",
    page_icon="SP",
    layout="wide",
)

st.title("StreamPulse Analytics")
st.caption("Product Analytics Platform for Music Streaming Behavior")

st.info(
    "Dashboard implementation will be added after KPI, retention, funnel, "
    "segmentation, and replay prediction outputs are available."
)
