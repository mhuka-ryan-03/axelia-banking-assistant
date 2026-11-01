# AXELIA – AI-Powered Banking Knowledge Assistant

AXELIA is an AI-powered banking knowledge assistant built using Retrieval-Augmented Generation (RAG). It allows users to ask questions in natural language and retrieve relevant information from banking and regulatory documents.

The project explores how Generative AI can make banking knowledge more accessible, searchable and easier to understand.

## The Problem

Banking institutions work with extensive regulatory documents, guidelines, circulars and policies. Finding specific information across lengthy PDF documents can be time-consuming.

AXELIA explores how AI can simplify access to this information by allowing users to ask questions and receive answers grounded in relevant document content.

## The Solution

AXELIA uses a RAG architecture to retrieve relevant sections from a collection of banking and regulatory documents before generating an answer using a Large Language Model (LLM).

Instead of relying solely on the language model's existing knowledge, the system uses retrieved document content as context when answering questions.

## Key Features

- PDF Document Processing: Extracts text from banking and regulatory PDF documents.
- Document Chunking: Splits lengthy documents into smaller, searchable sections.
- Semantic Search:Retrieves relevant information using vector embeddings.
- Retrieval-Augmented Generation: Generates contextual answers based on retrieved documents.
- Source References: Displays source document names and page references where available.
- Conversational Interface: Provides an interactive interface built with Streamlit.
- Context-Grounded Responses:Instructs the language model to avoid inventing information when the answer is not available in the supplied context.

## How It Works

1. Banking and regulatory PDF documents are loaded into the system.
2. Text is extracted and divided into smaller chunks.
3. The chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. A user submits a question through the Streamlit interface.
6. AXELIA retrieves relevant document sections using semantic similarity search.
7. The retrieved content is passed to the language model.
8. The model generates an answer using the retrieved context.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG application framework |
| ChromaDB | Vector database |
| Hugging Face Sentence Transformers | Text embeddings |
| Groq API | LLM inference |
| Streamlit | User interface |
| PyPDF / PyMuPDF | PDF text extraction |

Embedding Model: `sentence-transformers/all-MiniLM-L6-v2`

Language Model:`openai/gpt-oss-20b` via Groq.

## Project Structure

```text
zim-banking-rag/
│
├── data/                 # Source PDF documents
├── src/                  # RAG pipeline and processing scripts
├── vectorstore/          # Persisted ChromaDB vector database
├── app.py                # Streamlit application
├── test_rag.py           # RAG pipeline testing
├── requirements.txt      # Project dependencies
├── .env                  # Environment variables (not committed)
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/axelia-banking-assistant.git
```

```bash
cd axelia-banking-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your actual API key to GitHub.

### 6. Run the application

```bash
streamlit run app.py
```

## Potential Applications in Banking

AXELIA demonstrates how RAG-based systems could support:

- Access to banking regulations and compliance guidelines.
- Retrieval of internal policies and operational procedures.
- Employee knowledge management and onboarding.
- Regulatory information discovery.
- Banking compliance and technology-risk research.

## Current Status

AXELIA is a working proof of concept developed using a collection of Reserve Bank of Zimbabwe and banking-related documents.

The project is still under development. Further work will focus on improving retrieval accuracy, answer evaluation, source traceability, security and document management.

## Future Improvements

- Improved retrieval and ranking mechanisms.
- More detailed source citations within generated answers.
- Document version management.
- User authentication and role-based access control.
- Evaluation of answer accuracy and hallucination rates.
- Support for additional banking and regulatory documents.
- Exploration of secure deployment options for financial institutions.

## Disclaimer

AXELIA is an independent educational and technical project. It is not affiliated with or endorsed by the Reserve Bank of Zimbabwe or any financial institution.

It is a proof of concept and should not be used as a substitute for official regulatory guidance, professional compliance advice or institutional policies.

## Author

Developed as an independent AI/ML project exploring the application of Generative AI and Retrieval-Augmented Generation in banking and financial services.

Areas of interest:Artificial Intelligence, Banking Technology, FinTech, IT Audit, Technology Risk and AI Governance.