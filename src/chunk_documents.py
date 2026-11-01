from langchain_text_splitters import RecursiveCharacterTextSplitter

from load_documents import pdf_documents

text_spliter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=text_spliter.split_documents(pdf_documents)

print("chunking successfully completed")

print("Total documents: ",len(pdf_documents))

print("Total chunks",len(chunks))

print("\n First Chunk:")
print(chunks[0].page_content)

print("\n First chunk metadata:")

print(chunks[0].metadata)
