from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.schema import Document
import os


def doc_loader(filepath: str) -> list[Document]:
    ext = os.path.splitext(filepath)[-1].lower()

    if ext ==  ".pdf":
        loader = PyPDFLoader(filepath)
        docs = loader.load()
    elif ext == ".txt":
        loader = TextLoader(filepath, encoding="utf-8")
        docs = loader.load()
    else:
        raise ValueError(f"Unsupported file type {ext}")
    
    return docs