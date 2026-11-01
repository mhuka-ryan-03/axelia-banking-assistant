import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get the Groq API key
api_key = os.getenv("GROQ_API_KEY")

# Step 3: Connect to the LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=api_key,
    temperature=0.3
)

# Step 4: Send a question
response = llm.invoke("What is a loan agreement? Explain simply.")

# Step 5: Display the answer
print(response.content)