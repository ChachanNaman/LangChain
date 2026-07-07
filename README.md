# LangChain 🦜🔗

My notes, code, and hands-on experiments while learning **Generative AI using LangChain**, following the [CampusX YouTube playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0).

Every folder is numbered in the order the playlist builds on itself — start at `00` and work forward, or jump straight to whatever topic you need. Each one contains small, self-contained Python scripts / notebooks, plus its own `README.md` with the concept notes and a full file-by-file breakdown — the table below is the map, each folder's own README is the territory.

## 📂 Learning Path

| # | Folder | Topic | What's inside |
|---|---|---|---|
| 00 | [`Python_Refresher`](./00_Python_Refresher) | Python fundamentals | Functions, lambda, map/filter, list comprehension, strings, iterables, OOP, exception handling |
| 01 | [`LangChain_Models`](./01_LangChain_Models) | Models | Chat models (OpenAI, Anthropic, HuggingFace — API & local) and embedding models |
| 02 | [`LangChain_Prompts`](./02_LangChain_Prompts) | Prompts | `PromptTemplate`, System/Human/AI messages, multi-turn chat history, `ChatPromptTemplate`, `MessagesPlaceholder` |
| 03 | [`Structured_Output`](./03_Structured_Output) | Structured Output | `TypedDict`, `Pydantic`, JSON Schema, and `with_structured_output()` |
| 04 | [`Output_Parsers`](./04_Output_Parsers) | Output Parsers | `StrOutputParser`, `JsonOutputParser`, `StructuredOutputParser`, `PydanticOutputParser` |
| 05 | [`Chains`](./05_Chains) | Chains | Simple, sequential, parallel, and conditional chains using LCEL |
| 06 | [`Runnables`](./06_Runnables) | Runnables | The interface behind LCEL — built from scratch, then the real `RunnableSequence`/`Parallel`/`Lambda`/`Branch` |
| 07 | [`Document_Loaders`](./07_Document_Loaders) | Document Loaders | Loading text, PDFs, whole directories, and web pages into LangChain `Document` objects |
| 08 | [`Text_Splitters`](./08_Text_Splitters) | Text Splitters | Length, structure, language-aware, and semantic chunking strategies |
| 09 | [`Vector_Stores`](./09_Vector_Stores) | Vector Stores | What a vector store is, vs. a vector DB, and a hands-on Chroma walkthrough |
| 10 | [`Retrievers`](./10_Retrievers) | Retrievers | Similarity search, MMR, Multi-Query, Contextual Compression, Wikipedia |
| 11 | [`RAG`](./11_RAG) | RAG concepts | Why RAG beats fine-tuning for knowledge injection, and the full indexing → retrieval → generation pipeline |
| 12 | [`Project_YouTube_Chatbot`](./12_Project_YouTube_Chatbot) | RAG project | End-to-end: a chatbot that answers questions about any YouTube video's transcript |
| 13 | [`Tools`](./13_Tools) | Tools | Built-in tools, three ways to write a custom tool, and toolkits |
| 14 | [`Tool_Calling`](./14_Tool_Calling) | Tool Calling | Binding → calling → execution, plus a multi-tool currency-conversion example |

## 🧭 How the pieces fit together

```
Models (01) + Prompts (02) ──► Chains (05) / Runnables (06) ──► Structured Output (03) / Output Parsers (04)
                                                                            │
Document Loaders (07) ─► Text Splitters (08) ─► Vector Stores (09) ─► Retrievers (10)
                                                                            │
                                                                            ▼
                                                            RAG (11) ─► YouTube Chatbot project (12)

Tools (13) ─► Tool Calling (14)  — a separate track: giving an LLM the ability to act, not just retrieve
```

## 🧠 Key Concepts Covered

- **Models** — connecting to LLMs (OpenAI, Anthropic, Groq, HuggingFace) and embedding models for semantic search/similarity
- **Prompts** — why `PromptTemplate` is preferred over Python f-strings (validation + reusability), and managing multi-turn conversation history
- **Structured Output** — forcing LLMs to return data in a well-defined format (JSON) instead of free-form text, using `TypedDict`, `Pydantic`, or JSON Schema
- **Output Parsers** — parsing raw LLM text output into structured data for models that don't support `with_structured_output()` natively
- **Chains (LCEL)** — composing `prompt | model | parser` pipelines: simple, sequential, parallel, and conditional (`RunnableBranch`) chains
- **Runnables** — the shared interface behind every LCEL component, built from scratch once to demystify it
- **Document Loaders** — bringing external data (text files, PDFs, directories, web pages) into LangChain as `Document` objects, the first step of a RAG pipeline
- **Text Splitters** — breaking large documents into smaller chunks (by length, character, document structure, or semantic meaning) so they fit context windows and embed well for retrieval
- **Vector Stores** — storing document embeddings for similarity search; the difference between a VectorStore (abstraction) and a VectorDB (storage engine), with a hands-on Chroma example
- **Retrievers** — pulling relevant chunks back out of a vector store via similarity search, MMR (for diversity), Multi-Query (multiple reformulated queries), and Contextual Compression (trimming irrelevant content from retrieved chunks)
- **RAG (Retrieval-Augmented Generation)** — combining retrieval with generation so the LLM answers grounded in retrieved context instead of relying purely on parametric knowledge, and why it usually beats fine-tuning for knowledge injection
- **Tools & Tool Calling** — packaging Python functions/APIs so an LLM can decide when and how to call them, binding tool schemas to a model, and the binding → calling → execution split
- **End-to-End RAG Project** — a YouTube-video chatbot that loads transcripts, chunks and embeds them, retrieves relevant context, and answers questions

## 🛠️ Tech Stack

- Python 3.12
- [LangChain](https://www.langchain.com/) (`langchain`, `langchain-core`, `langchain-community`, `langchain-experimental`, `langchain-text-splitters`)
- LLM providers: OpenAI, Anthropic, Groq, Google Gemini, HuggingFace
- Vector store & retrieval: `langchain-chroma`, `chromadb`, `faiss-cpu`, `sentence-transformers`
- `python-dotenv` for environment variable management
- `pydantic` for data validation

## ⚙️ Setup

1. Clone the repo
   ```bash
   git clone https://github.com/ChachanNaman/LangChain.git
   cd LangChain
   ```
2. Create a virtual environment and install dependencies (covers every folder in this repo)
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the folder you want to run, with whichever keys that folder's scripts need
   ```env
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   GROQ_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   HUGGINGFACEHUB_API_TOKEN=your_key_here
   EXCHANGE_RATE_API_KEY=your_key_here
   ```
4. Run any script
   ```bash
   python 05_Chains/1_Simple_chain.py
   ```
   ...or open any `.ipynb` notebook in Jupyter / VS Code.

Each folder's own `README.md` lists exactly which keys and packages *that* folder needs — you don't need every key above unless you're running everything.

## 📺 Reference

Course: **Generative AI using LangChain** by [CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

## ✍️ Author

**Naman Chachan** ([@ChachanNaman](https://github.com/ChachanNaman))
