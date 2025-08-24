import os
import streamlit as st

from core.document_loader import doc_loader
from core.text_splitter import splitter
from core.embedding import EmbeddingGenerator 


st.title("📚 LEKHAM")

uploaded_file = st.file_uploader("upload doc", type=["pdf", "txt"])

if uploaded_file is not None:
    save_path = os.path.join("data/raw", uploaded_file.name)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"saved file: {save_path}")

    documents = doc_loader(save_path)

    split_docs = splitter(documents)

    embedding_generator = EmbeddingGenerator("sentence-transformers/all-MiniLM-L6-v2")
    embed_results = embedding_generator.embed_documents(split_docs)

    print(f"embed result: {embed_results}")
