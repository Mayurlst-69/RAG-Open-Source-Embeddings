<div align="center">

# 📚 Serverless RAG & Open Source Embeddings

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Integration-1C3C3C?style=for-the-badge&logo=langchain)
![API](https://img.shields.io/badge/LLM-Llama3_(Groq)-orange?style=for-the-badge)

<br>

**A high-performance RAG system running entirely on Free Tier resources.**
<br>
*Fast Inference • Open Source Embeddings • Zero Cost*

</div>

---

## 🌟 Overview
This project demonstrates how to build a Retrieval-Augmented Generation (RAG) pipeline using **Groq API** for ultra-fast inference and **HuggingFace Embeddings** for high-quality retrieval, all within Google Colab.

### Key Features
* 🚀 **Blazing Fast:** Powered by Groq LPU (Linear Processing Unit) for sub-second responses.
* 🧠 **Smart Retrieval:** Uses `BAAI/bge-m3` 
* 💸 **100% Free:** Built using entirely open-source tools and free-tier APIs.
* 🔒 **Local Vector Store:** Implements ChromaDB for efficient, private vector storage.

---
## 🛠 Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **LLM** | llama-3.3-70b-versatile | Via Groq API (Free Beta) |
| **Embeddings** | BAAI/bge-m3 | High MTEB Score Model |
| **Vector DB** | ChromaDB | Lightweight & Local |
| **Framework** | LangChain | Orchestration |

🧠 How It Works
The system follows the standard RAG architecture:

1.  **Ingestion:** The PDF document is loaded and split into smaller chunks.
2.  **Embedding:** Each chunk is converted into a vector using the HuggingFace model.
3.  **Storage:** Vectors are stored in a local ChromaDB database.
4.  **Retrieval:** When you ask a question, the system finds the most relevant chunks using Cosine Similarity.
5.  **Generation:** The relevant chunks + your question are sent to Llama 3 (via Groq) to generate the final answer.

## 📂 Project Structure

```bash
RAG-Open-Source-Embeddings/
├── 📄 Code.ipynb          # Jupyter Notebook for interactive demo & experiments
├── 📄 main.py             # Production-ready Python script
├── 📄 requirements.txt    # List of dependencies
├── 📄 README.md           # Documentation
└── 📂 data/               # Folder to store your PDF documents
```
## 🚀 Quick Start

### Prerequisites
1.  **Groq API Key:** Get a free key from [Groq Cloud Console](https://console.groq.com/).
2.  **Python 3.10+** installed on your machine.

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Mayurlst-69/RAG-Open-Source-Embeddings.git](https://github.com/Mayurlst-69/RAG-Open-Source-Embeddings.git)
    cd RAG-Open-Source-Embeddings
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Key**
    * **Mac/Linux:** `export GROQ_API_KEY="your_api_key_here"`
    * **Windows:** `set GROQ_API_KEY=your_api_key_here`
    * *(Or simply paste it when prompted in the script)*

### Usage

**Option 1: Run Python Script (Recommended)**
Place your PDF file in the folder (e.g., named `document.pdf`) and run:
```bash
python main.py
```
**Option 2: Interactive Notebook
Open Code.ipynb in Jupyter Notebook or Google Colab for a step-by-step walkthrough.

##⚙️ Configuration
You can modify main.py to customize the pipeline:
<img width="686" height="195" alt="image" src="https://github.com/user-attachments/assets/277b0665-5ee7-42b0-81a5-213633b7c4a5" />

<div align="center">
Create by [Mayurlst-69]
</div>
