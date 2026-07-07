# LangChain 🦜🔗

My notes, code, and hands-on experiments while learning **Generative AI using LangChain**, following the [CampusX YouTube playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0).

Each folder corresponds to a topic in the playlist and contains small, self-contained Python scripts / notebooks I wrote while following along, along with my own notes (`README.md`) summarizing the key concepts.

## 📂 Repository Structure

| Folder | Topic | What's inside |
|---|---|---|
| [`00_Python_Refresher`](./00_Python_Refresher) | Python fundamentals | Functions, lambda, map/filter, list comprehension, strings, iterables, OOP, exception handling — refresher before diving into LangChain |
| [`01_LangChain_Models`](./01_LangChain_Models) | Models | Chat models (OpenAI, Anthropic, HuggingFace — API & local), embedding models, and document similarity |
| [`02_LangChain_Prompts`](./02_LangChain_Prompts) | Prompts | Static vs. dynamic prompts, `PromptTemplate`, System/Human/AI messages, multi-turn chat history, `ChatPromptTemplate`, `MessagePlaceholder` |
| [`03_Structured_Output`](./03_Structured_Output) | Structured Output | `TypedDict`, `Annotated`, `Pydantic`, JSON Schema, and `with_structured_output()` |
| [`04_Output_Parsers`](./04_Output_Parsers) | Output Parsers | `StrOutputParser`, `JsonOutputParser`, `StructuredOutputParser`, `PydanticOutputParser` |
| [`05_Chains`](./05_Chains) | Chains | Simple, sequential, parallel, and conditional chains using LangChain Expression Language (LCEL) |
| [`06_Runnables`](./06_Runnables) | Runnables | `RunnableSequence`, `RunnableParallel`, `RunnableBranch`, `RunnableLambda`, and a PDF-reading example |
| [`07_Document_Loaders`](./07_Document_Loaders) | Document Loaders | `TextLoader`, `PyPDFLoader`, `DirectoryLoader`, `WebBaseLoader` — loading text, PDFs, whole directories, and web pages into LangChain `Document` objects (includes a `pdfs/` sample folder) |
| [`08_Text_Splitters`](./08_Text_Splitters) | Text Splitters | Length-based splitting, text/character-based splitting, document-based splitting (code & Markdown aware), and semantic-based splitting for chunking documents before embedding/retrieval |
| [`09_Vector_Stores`](./09_Vector_Stores) | Vector Stores | What vector stores are, VectorStore vs VectorDB, and a hands-on Chroma vector store walkthrough (`langchain_chroma`) |
| [`10_Retrievers`](./10_Retrievers) | Retrievers | Wikipedia retriever, vector store retriever, Maximum Marginal Relevance (MMR), Multi-Query retriever, and Contextual Compression retriever |
| [`11_RAG`](./11_RAG) | RAG | Putting it together — Retrieval-Augmented Generation pipeline notes |
| [`12_Project_YouTube_Chatbot`](./12_Project_YouTube_Chatbot) | YouTube Chatbot (RAG project) | End-to-end RAG chatbot (`youtube_chatbot_rag.ipynb`) that answers questions about a YouTube video's transcript |
| [`13_Tools`](./13_Tools) | Tools | Built-in tools, custom tools, and toolkits — packaging Python functions so an LLM can call them |
| [`14_Tool_Calling`](./14_Tool_Calling) | Tool Calling | Tool binding, tool calling, and a worked currency-conversion example |

## 🧠 Key Concepts Covered

- **Models** — connecting to LLMs (OpenAI, Anthropic, Groq, HuggingFace) and embedding models for semantic search/similarity
- **Prompts** — why `PromptTemplate` is preferred over Python f-strings (validation + reusability), and managing multi-turn conversation history
- **Structured Output** — forcing LLMs to return data in a well-defined format (JSON) instead of free-form text, using `TypedDict`, `Pydantic`, or JSON Schema
- **Output Parsers** — parsing raw LLM text output into structured data for models that don't support `with_structured_output()` natively
- **Chains (LCEL)** — composing `prompt | model | parser` pipelines: simple, sequential, parallel, and conditional (`RunnableBranch`) chains
- **Runnables** — the building blocks behind LCEL that make chains composable and interoperable
- **Document Loaders** — bringing external data (text files, PDFs, directories, web pages) into LangChain as `Document` objects, the first step of a RAG pipeline
- **Text Splitters** — breaking large documents into smaller chunks (by length, character, document structure, or semantic meaning) so they fit context windows and embed well for retrieval
- **Vector Stores** — storing document embeddings for similarity search; the difference between a VectorStore (abstraction) and a VectorDB (storage engine), with a hands-on Chroma example
- **Retrievers** — pulling relevant chunks back out of a vector store via similarity search, MMR (for diversity), Multi-Query (multiple reformulated queries), and Contextual Compression (trimming irrelevant content from retrieved chunks)
- **RAG (Retrieval-Augmented Generation)** — combining retrieval with generation so the LLM answers grounded in retrieved context instead of relying purely on parametric knowledge
- **Tools & Tool Calling** — packaging Python functions/APIs so an LLM can decide when and how to call them, and binding tool schemas to a model
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
   ```
4. Run any script
   ```bash
   python 05_Chains/1Simple_chain.py
   ```

## 📺 Reference

Course: **Generative AI using LangChain** by [CampusX](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0)

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

## ✍️ Author

**Naman Chachan** ([@ChachanNaman](https://github.com/ChachanNaman))
