import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM

from rag_pipeline import split_documents, create_embeddings, create_retriever
from vector_store import create_vector_store


st.title("QnA Generation Chatbot")


# SESSION STATE
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "ask_mode" not in st.session_state:
    st.session_state.ask_mode = True


# FILE UPLOAD
uploaded_files = st.file_uploader(
    "Upload company documents (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)


@st.cache_resource
def build_vector_db(_documents):

    chunks = split_documents(_documents)

    embeddings = create_embeddings()

    vector_db = create_vector_store(chunks, embeddings)

    return vector_db


documents = []

if uploaded_files:

    for uploaded_file in uploaded_files:

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        loader = PyPDFLoader(file_path)
        docs = loader.load()

        documents.extend(docs)


# RAG PIPELINE
if documents:

    vector_db = build_vector_db(documents)

    retriever = create_retriever(vector_db)

    llm = OllamaLLM(model="phi3")


    # SHOW CONVERSATION
    if st.session_state.chat_history:

        st.subheader("Conversation")

        for chat in st.session_state.chat_history:

            # QUESTION (BIGGER + BOLD)
            st.markdown(
                f"<span style='font-size:20px; font-weight:bold;'>Question: {chat['question']}</span>",
                unsafe_allow_html=True
            )

            # ANSWER (NORMAL TEXT)
            st.write(chat["answer"])

            st.divider()


    # NEXT QUESTION BUTTON
    if not st.session_state.ask_mode:

        if st.button("Next Question"):
            st.session_state.ask_mode = True
            st.rerun()


    # QUESTION FORM
    if st.session_state.ask_mode:

        with st.form("question_form", clear_on_submit=True):

            query = st.text_input(
                "Ask a question",
                placeholder="Ask a question about the uploaded document..."
            )

            submit = st.form_submit_button("Submit Question")


        if submit and query:

            docs = retriever.invoke(query)

            if docs:

                context = " ".join([doc.page_content for doc in docs])

                prompt = f"""
You are an AI assistant answering questions using the provided context.

Only use the information in the context to answer.

If the answer exists in the context, explain it clearly.
If the answer is not in the context, say "The answer is not found in the document."

Context:
{context}

Question:
{query}

Answer:
"""

                response = llm.invoke(prompt)

            else:

                response = "No relevant information found."

            st.session_state.chat_history.append({
                "question": query,
                "answer": response
            })

            st.session_state.ask_mode = False

            st.rerun()


else:

    st.info("Please upload company documents to start asking questions.")