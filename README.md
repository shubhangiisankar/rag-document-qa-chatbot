# QnA Generation Chatbot (RAG + LangChain)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload documents (PDFs) and ask questions about them. The system retrieves relevant information from the uploaded documents and generates answers using a local language model.

---

## Features

- Upload documents (PDF)
- Ask questions about the uploaded documents
- Retrieval-Augmented Generation (RAG)
- Uses vector embeddings for semantic search
- Runs LLM locally using Ollama
- Maintains conversation history
- Simple Streamlit interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Ollama (Local LLM)
- HuggingFace Embeddings
- Sentence Transformers
- Vector Database (Chroma / FAISS)

---

## Workflow

1. User uploads a PDF document
2. The document is split into smaller chunks
3. Each chunk is converted into embeddings
4. Embeddings are stored in a vector database
5. When a user asks a question:
   - The question is converted into an embedding
   - The retriever finds the most relevant chunks
6. Retrieved chunks + user question are sent to the LLM
7. The LLM generates the final answer

---

## Embedding Model Used

This project uses the HuggingFace embedding model:
sentence-transformers/all-MiniLM-L6-v2

This model converts text into numerical vectors (embeddings) that capture the semantic meaning of the text. 
These embeddings allow the vector database to perform semantic search and retrieve the most relevant document chunks for a given query.

This model was chosen because it is lightweight, fast, and widely used for semantic search and Retrieval-Augmented Generation (RAG) systems.

---

## LLM Used

This project uses a local Large Language Model served through Ollama.

Model used:
phi3

When a user asks a question, the system retrieves the most relevant document chunks and sends them along with the user query to the LLM. 
The LLM then generates an answer strictly based on the retrieved context.

---

## How to Run the Project

1. Clone the repository

git clone https://github.com/shubhangiisankar/rag-document-qa-chatbot.git

2. Navigate to the project folder

cd rag-document-qa-chatbot

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run app.py

5. Upload PDF documents and start asking questions.
