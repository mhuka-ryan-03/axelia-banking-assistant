
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get the Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Step 3: Initialize the LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=api_key,
    temperature=0.3
)

# Step 4: Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# Step 5: Load existing ChromaDB
vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)

# Step 6: Ask a question
question = "What are the requirements for opening a bank account?"

# Step 7: Retrieve relevant chunks
results = vectorstore.similarity_search(
    question,
    k=3
)

# Step 8: Combine retrieved chunks and their sources
context = ""

for i, document in enumerate(results):
    source = document.metadata["source"]
    page = document.metadata["page"]

    context += f"""
Source: {source}
Page: {page}

Content:
{document.page_content}

"""

# Step 9: Create the prompt
prompt = f"""
You are a Zimbabwean banking information assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not available in the context,
say that the provided documents do not contain the information.

When answering, cite the source filename and page number
for the information used.

Context:
{context}

Question:
{question}

Answer:
"""

# Step 10: Generate the answer
response = llm.invoke(prompt)

# Step 11: Display the answer
print("\nQuestion:", question)
print("\nAnswer:")
print(response.content)

# Step 12: Display verified sources
print("\nSources:")

for i, document in enumerate(results):
    source = os.path.basename(document.metadata["source"])
    page = document.metadata["page"]

    print(f"{i + 1}. {source} - Page {page}")
