from llama_index.core import VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.readers.file import PDFReader
import os

# Load PDF documents from the ./manuals folder
pdf_reader = PDFReader()
documents = []
for fname in os.listdir("./manuals"):
    if fname.endswith(".pdf"):
        path = os.path.join("./manuals", fname)
        documents.extend(pdf_reader.load_data(file=path))

# Local language and embedding models
llm = Ollama(model="tinyllama")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# Build the document index
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Set up the chat engine
chat_engine = index.as_chat_engine(llm=llm, chat_mode="context")

# Chat loop
print("\n\n CHATBOT READY, type 'exit' to quit.")
while True:
    query = input("> ")
    if query.lower() in {"exit", "quit"}:
        break
    response = chat_engine.chat(query)
    print(f"\n\n -- {response}\n\n")

