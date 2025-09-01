import faiss
import numpy as np
from typing import List, Dict, Any



class FaissHandler:
    def __init__(self, dim: int, metadata_list: List):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata_list = metadata_list


    def embedding_insert(self, embeddings: np.ndarray) -> None:
        if embeddings.dtype != np.float32:
            embeddings = embeddings.astype(np.float32)

        self.index.add(embeddings)


    def similarity_search(self, search_query: str, embed_gen: Any, top_k: int = 3) -> List:
        test_retreive_query = embed_gen.model.encode([search_query], convert_to_numpy=True).astype(np.float32)
        distance, indices = self.index.search(test_retreive_query, top_k)

        search_results = [{"text": self.metadata_list[index]["text"], "metadata": self.metadata_list[index]["metadata"]} for index in indices[0]]

        return search_results