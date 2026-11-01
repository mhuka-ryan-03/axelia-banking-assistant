from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from chunk_documents import chunks

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device":"cpu"}
)

#creating a vector database

vectorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vectorstore"
)

print("vector database created successfully")
print("Total chunks stored:",len(chunks))