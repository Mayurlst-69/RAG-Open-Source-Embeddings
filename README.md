📚 Serverless RAG with Groq & Open Source Embeddings

A lightweight, high-performance Retrieval-Augmented Generation (RAG) system running entirely on Google Colab or local environment using free-tier resources.

🌟 Key Features
- High-Performance Embeddings: Utilizes `BAAI/bge-m3`
- Blazing Fast Inference: Powered by Groq Cloud API (Llama 3 / Mixtral) for sub-second responses.
- Zero Cost: Built using 100% free open-source tools and API tiers.
- Vector Database: Implements ChromaDB for efficient vector storage and retrieval.

🛠 Tech Stack
- LLM: llama-3.3-70b-versatile (via Groq API)
- Embeddings: HuggingFace (`BAAI/bge-m3`)
- Vector Store: ChromaDB
- Orchestration: LangChain
- PDF Processing: PyPDF

🚀 Quick Start

Prerequisites
1.  Get a free API Key from [Groq Cloud](https://console.groq.com/).
2.  Python 3.10+

Installation
`bash
pip install -r requirements.txt
