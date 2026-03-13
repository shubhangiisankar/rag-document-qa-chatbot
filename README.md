# Company Knowledge Base Chatbot (RAG + LangChain)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that allows users to upload company documents (PDFs) and ask questions about them. The system retrieves relevant information from the uploaded documents and generates answers using a local language model.

---

## Features

- Upload company documents (PDF)
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
