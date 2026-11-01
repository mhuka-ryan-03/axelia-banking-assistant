from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

#loading the embedded models

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device":"cpu"}
)

vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)

question="what are the main features of a loan agreement?"

results=vectorstore.similarity_search(
    question,
    k=3
)

print("Question:",question)

for i,document in enumerate(results):
    print(f"\nResult{i+1}:")
    print(document.page_content)
    print("Source:",document.metadata["source"])
    print("page:",document.metadata["page"])