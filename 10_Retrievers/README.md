# 10 — Retrievers

A **retriever** is a LangChain component that fetches relevant documents from a data source in response to a query — the piece that sits between "stuff is stored somewhere" ([`09_Vector_Stores`](../09_Vector_Stores)) and "the LLM answers using that stuff" ([`11_RAG`](../11_RAG)). Every retriever below shares the same interface (`.invoke(query)`), so they're interchangeable — what differs is *how* each one decides what's relevant.

## Files

| File | Strategy | What it shows |
|---|---|---|
| [`01_wikipedia_retriever.py`](./01_wikipedia_retriever.py) | `WikipediaRetriever` | Queries the Wikipedia API directly for keyword-based results — no vector store involved at all |
| [`02_vectorstore_retriever.py`](./02_vectorstore_retriever.py) | Similarity search | The standard case: `vectorstore.as_retriever(search_kwargs={"k": 2})`. Documents are embedded once, the query is embedded at search time, and the top-`k` closest vectors are returned |
| [`03_mmr_retriever.py`](./03_mmr_retriever.py) | Maximum Marginal Relevance | Reduces redundancy: plain similarity search can return several near-duplicate results; MMR picks the most relevant document first, then the next *most different from what's already picked* — trading a bit of relevance for diversity. `lambda_mult` controls the balance (lower = more diverse) |
| [`04_multi_query_retriever.py`](./04_multi_query_retriever.py) | `MultiQueryRetriever` | For ambiguous queries ("how can I improve my energy levels?" could mean diet, sleep, or exercise) — an LLM reformulates the query into several more specific variants, each is searched independently, and results are merged. Compares plain similarity search vs. multi-query side by side on the same query |
| [`05_contextual_compression_retriever.py`](./05_contextual_compression_retriever.py) | `ContextualCompressionRetriever` | A base retriever returns whole documents, even if only one sentence is relevant. This wraps it with an LLM-based compressor (`LLMChainExtractor`) that strips each retrieved document down to just the part relevant to the query |

## Choosing a retriever

| Situation | Reach for |
|---|---|
| General-purpose semantic search | Vector store retriever (`02`) |
| Results are too repetitive / lack diversity | MMR (`03`) |
| Query is vague or could mean several things | Multi-query (`04`) |
| Retrieved documents are long but only partially relevant | Contextual compression (`05`) |
| No vector store at all, just need external knowledge | Wikipedia retriever (`01`) — or swap in any other source-specific retriever |

> **Note:** `04` and `05` use `gpt-3.5-turbo` for their internal LLM calls (query reformulation / compression) — swap in whichever OpenAI model you have access to.
