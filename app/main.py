import os
import streamlit as st


st.title("📚 LEKHAM")

uploaded_file = st.file_uploader("upload doc", type=["pdf", "txt"])

if uploaded_file is not None:
    save_path = os.path.join("data/raw", uploaded_file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"saved file: {save_path}")
