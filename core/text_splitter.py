from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List


def splitter(documents:List) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0) #might need adding additional parameters

    split_chunks = text_splitter.split_documents(documents)

    return split_chunks
