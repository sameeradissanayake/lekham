import os
import streamlit as st
from dotenv import load_dotenv

from core.document_loader import doc_loader
from core.text_splitter import splitter
from core.embedding import EmbeddingGenerator 


load_dotenv()

file_path = os.getenv("FILE_PATH")

# Load the document
documents = doc_loader(file_path)

# Split the document to meaningful chunks
split_docs = splitter(documents)

# Transform to embeddings
embedding_generator = EmbeddingGenerator("sentence-transformers/all-MiniLM-L6-v2")
embed_results = embedding_generator.embed_documents(split_docs)

print(f"embed result: {embed_results}")
