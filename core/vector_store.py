import faiss
import numpy as np
from typing import List,Dict


class FaissHandler:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata: List[Dict] = []


    def embedding_insert(self, embeddings):
        if embeddings.dtype != np.float32:
            embeddings = embeddings.astype(np.float32)

        self.index.add(embeddings)

