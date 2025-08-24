from sentence_transformers import SentenceTransformer
from langchain.schema import Document
from typing import List

model = SentenceTransformer("all-MiniLM-L6-v2")


class EmbeddingGenerator:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, docs: List[Document]):
        texts = [doc.page_content for doc in docs]
        embeddings = self.model.encode(texts, batch_size=32, show_progres_bar=T)

        results = []

        for i, doc in enumerate(docs):
            results.append({
                "embedding": embeddings[i],
                "text": doc.page_content,
                "metadata": doc.metadata
            })
        
        return results