from sentence_transformers import SentenceTransformer
from langchain.schema import Document
from typing import List
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


class EmbeddingGenerator:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, docs: List[Document]):
        texts = [doc.page_content for doc in docs]
        embeddings = self.model.encode(texts, batch_size=32, show_progress_bar=True)

        results = []

        for i, doc in enumerate(docs):
            results.append({
                "embedding": embeddings[i],
                "text": doc.page_content,
                "metadata": doc.metadata
            })
        
        return results
    
    def embed_matrix_gen(self, embed_results):
        embeddings = [item["embedding"] for item in embed_results]

        embedding_matrix = np.array(embeddings, dtype=np.float32)

        return embedding_matrix