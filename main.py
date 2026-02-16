import os
import sys

# import library 
try:
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_chroma import Chroma
    from openai import OpenAI
except ImportError:
    print("❌ Libraries not found. Please run: pip install -r requirements.txt")
    sys.exit(1)

# --- Configuration ---
# input API Key in Environment Variable or .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("⚠️  Warning: GROQ_API_KEY not found in environment variables.")
    pass

# --- 1. System Setup ---
def setup_rag_system():
    print("🔄 Initializing Embedding Model (BAAI/bge-m3)...")
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    return embedding_model

# --- 2. Data Ingestion ---
def ingest_document(pdf_path, embedding_model):
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File not found at {pdf_path}")
        return None

    print(f"📄 Loading PDF: {pdf_path}...")
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    print("✂️  Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)
    print(f"✅ Split into {len(splits)} chunks.")

    print("💾 Creating Vector Database...")
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embedding_model,
        # persist_directory="./chroma_db" # Uncomment to save to disk
    )
    return vectorstore

# --- 3. Query Logic ---
def query_llm(vectorstore, question, api_key):
    if not api_key:
        return "❌ Error: No API Key provided."

    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key
    )

    # Retrieval
    results = vectorstore.similarity_search(question, k=3)
    context_text = "\n\n".join([doc.page_content for doc in results])

    # Prompt
    system_prompt = "You are a helpful assistant. Use the provided context to answer the user's question."
    user_prompt = f"Context:\n{context_text}\n\nQuestion:\n{question}"

    # Generation
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.2,
    )
    return response.choices[0].message.content

# --- Main Execution Block ---
if __name__ == "__main__":  
    # 1. Setup
    embed_model = setup_rag_system()
    
    # 2. Check for PDF 
    pdf_file = "document.pdf" # <---- your flie
    
    if not os.path.exists(pdf_file):
        print(f"⚠️  Please place a PDF file named '{pdf_file}' in this folder to run the demo.")
    else:
        # 3. Process & Run
        vector_db = ingest_document(pdf_file, embed_model)
        
        if vector_db:
            user_question = input("\n❓ Enter your question: ")
            if not GROQ_API_KEY:
                GROQ_API_KEY = input("🔑 Enter Groq API Key: ")
            
            print("\n🤖 Thinking...")
            answer = query_llm(vector_db, user_question, GROQ_API_KEY)
            print(f"\n💡 Answer:\n{answer}")
