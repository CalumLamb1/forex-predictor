import streamlit as st

try:
    from core.indicators import add_indicators
    st.write("✅ Import worked!")
except Exception as e:
    st.error(f"Import failed: {e}")
