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

metadata_list = [{"text": item["text"], "metadata": item["metadata"]} for item in embed_results]

print(f"shape: {embed_matrix.shape[1]}")
print(f"dimensions: {embed_matrix.ndim}")


faiss_handler_obj = FaissHandler(embed_matrix.shape[1])
faiss_handler_obj.embedding_insert(embed_matrix)

query = "“I am no child,” Elara said firmly"
test_retreive_query = embedding_generator.model.encode([query], convert_to_numpy=True).astype(np.float32)

k = 3
distance, indices = faiss_handler_obj.index.search(test_retreive_query, k)

print([metadata_list[i]["text"] for i in indices[0]])