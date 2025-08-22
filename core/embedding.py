from sentence_transformers import SentenceTransformer
from langchain.schema import Document
from typing import List

model = SentenceTransformer("all-MiniLM-L6-v2")


class EmbeddingGenerator:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, docs: List[Document]):
        pass
