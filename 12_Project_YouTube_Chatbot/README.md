# 12 — Project: YouTube Video Chatbot (RAG)

An end-to-end RAG system that answers questions about a YouTube video using its transcript — e.g. "does this video talk about AI?" or "give me 5 key points from this lecture." Everything from [`11_RAG`](../11_RAG) implemented against a real data source, in one notebook: [`youtube_chatbot_rag.ipynb`](./youtube_chatbot_rag.ipynb).

**Possible product shapes** (not built here, just the underlying idea): a Chrome extension that answers questions about the video you're currently watching, or a Streamlit site where you paste a video link and ask questions in a new tab.

## Plan of action

```
YouTube video → transcript → chunks → embeddings → vector store
                                                          │
                     query → retriever → relevant chunks ┘
                                                          │
                     query + relevant chunks → prompt → LLM → answer
```

## Pipeline (as built in the notebook)

| Step | What happens | Tools used |
|---|---|---|
| **1a. Document ingestion** | Fetch the transcript for a given YouTube `video_id` via `youtube-transcript-api`, join it into one string | `YouTubeTranscriptApi` |
| **1b. Text splitting** | Split the transcript into overlapping chunks (`chunk_size=500`, `chunk_overlap=100`) | `RecursiveCharacterTextSplitter` |
| **1c. Embedding + storage** | Embed each chunk and store it in an in-memory FAISS index | `HuggingFaceEmbeddings` (`sentence-transformers/all-MiniLM-L6-v2`) + `FAISS` |
| **2. Retrieval** | Convert the vector store into a retriever, fetch the top-3 chunks most relevant to a query | `vector_store.as_retriever(search_kwargs={"k": 3})` |
| **3. Augmentation** | Combine retrieved chunks into a single context string, inject `{context}` + `{question}` into a prompt that instructs the LLM to answer *only* from the given context | `PromptTemplate` |
| **4. Generation** | Send the final prompt to the LLM | `ChatGroq` (`llama-3.3-70b-versatile`, `temperature=0` for deterministic answers) |
| **5. Wire it into one chain** | Replace the manual step-by-step calls above with a single LCEL chain that does retrieval → formatting → prompting → generation → parsing automatically on every `.invoke(question)` | `RunnableParallel`, `RunnableLambda`, `RunnablePassthrough`, `StrOutputParser` |

### The final chain

```python
parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),  # retrieve chunks, then join into one string
    "question": RunnablePassthrough()                    # pass the question through unchanged
})

main_chain = parallel_chain | prompt | llm | parser

main_chain.invoke("What is GPT?")
main_chain.invoke("Who is Demis Hassabis?")
main_chain.invoke("Did they discuss nuclear fusion?")
```

```
User Question
     │
     ▼
Retriever (FAISS) ──► Top-3 relevant chunks ──► Format into context string
     │                                                    │
     └──────────────────── + question ───────────────────┘
                              │
                              ▼
                       Prompt Template
                              │
                              ▼
                    Groq (Llama 3.3 70B)
                              │
                              ▼
                        Parsed answer
```

This is the same pattern as `04_Conditional_chain.py` in [`05_Chains`](../05_Chains) and the parallel/passthrough examples in [`06_Runnables`](../06_Runnables) — a `RunnableParallel` fans out to fetch context while passing the original question through unchanged, then everything downstream composes with `|` like any other LCEL chain.

## Setup

```bash
pip install langchain langchain-community langchain-groq sentence-transformers faiss-cpu youtube-transcript-api langchain-text-splitters
```

Add a `.env` file in this folder with:
```env
GROQ_API_KEY=your_key_here
```

Then open the notebook, set `video_id` to any YouTube video ID, and run through the cells.
