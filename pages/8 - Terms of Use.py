import pandas as pd
import streamlit as st
from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer
import base64
import os

file0 = Path(__file__).parent / "pages' / "appdata" / "Terms-of-Use.pdf"#add_auth(required=True)

try:
  with open(file0, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    st.write(base64_pdf)
except FileNotFoundError:
  st.error(f"PDF file not found: {file0}")
st.write("  ---------------------------------------------------------------  ")
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")

