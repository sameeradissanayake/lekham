import os
import streamlit as st


st.title("📚 LEKHAM")

uploaded_file = st.file_uploader("upload doc", type=["pdf", "txt"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
