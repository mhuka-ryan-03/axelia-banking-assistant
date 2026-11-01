from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
#loading all the pdf files


from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Step 1: Locate the data folder
data_path = Path(__file__).resolve().parent.parent / "data"

# Step 2: Load all PDF documents
dir_loader = DirectoryLoader(
    str(data_path),
    glob="*.pdf",
    loader_cls=PyPDFLoader,
    show_progress=True
)

# Step 3: Load the documents
pdf_documents = dir_loader.load()

# Step 4: Display the results
print("Documents loaded successfully!")

print("Total pages loaded:", len(pdf_documents))

# Step 5: Display the first document
if pdf_documents:
    print("\nFirst document content:")
    print(pdf_documents[0].page_content[:1000])

    print("\nDocument metadata:")
    print(pdf_documents[0].metadata)
