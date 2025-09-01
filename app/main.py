import os
import streamlit as st
from dotenv import load_dotenv
import numpy as np

from core.document_loader import doc_loader
from core.text_splitter import splitter
from core.embedding import EmbeddingGenerator
from core.vector_store import FaissHandler


load_dotenv()

file_path = os.getenv("FILE_PATH")
save_path = os.getenv("SAVE_PATH")

# Load the document
documents = doc_loader(file_path)

# Split the document to meaningful chunks
split_docs = splitter(documents)

# Transform to embeddings
embedding_generator = EmbeddingGenerator("sentence-transformers/all-MiniLM-L6-v2")
embed_results = embedding_generator.embed_documents(split_docs)

embed_matrix = embedding_generator.embed_matrix_gen(embed_results)
# print(f"embed result: {embed_results}")

# Save metadata in a list
metadata_list = [{"text": item["text"], "metadata": item["metadata"]} for item in embed_results]


# Handle faiss insert and query
faiss_handler_obj = FaissHandler(embed_matrix.shape[1], metadata_list)
faiss_handler_obj.embedding_insert(embed_matrix)

query = "“I am no child,” Elara said firmly"
search_results = faiss_handler_obj.similarity_search(query, embedding_generator)
