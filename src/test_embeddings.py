from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device":"cpu"}
)

text="The Reserve bank of Zimbabwe regulates financial institutions"

vector=embeddings.embed_query(text)

print("embeddings created successful")
print("vector length:",len(vector))
print("first 10 values",vector[:10])