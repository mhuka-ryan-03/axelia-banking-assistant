
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Load environment variables
load_dotenv()


# Load the AI and database components only once
def get_rag_components():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY was not found in the .env file")

    # Initialize Groq LLM
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=api_key,
        temperature=0.3
    )

    # Initialize embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    # Load existing ChromaDB
    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    return llm, vectorstore


# Answer a user's question
def ask_axelia(question, llm, vectorstore):

    # Retrieve relevant document chunks
    results = vectorstore.similarity_search(
        question,
        k=5
    )

    # Check whether relevant documents were retrieved
    if not results:
        return (
            "I could not find relevant information in the "
            "available banking documents."
        ), []

    # Build context from retrieved documents
    context = ""

    for document in results:

        source = os.path.basename(document.metadata.get("source", "Unknown"))
        page = document.metadata.get("page", "Unknown")

        context += f"""
Source: {source}
Page: {page}

Content:
{document.page_content}

"""

    # Create the prompt
    prompt = f"""
You are AXELIA, a Zimbabwean banking information assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not available in the context,
clearly say that the provided documents do not contain
the information.

Do not invent banking regulations, requirements or facts.

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate the answer
    response = llm.invoke(prompt)

    # Collect source references
    sources = []

    for document in results:

        source = os.path.basename(
            document.metadata.get("source", "Unknown")
        )

        page = document.metadata.get("page", "Unknown")

        reference = {
            "source": source,
            "page": page
        }

        if reference not in sources:
            sources.append(reference)

    return response.content, sources
