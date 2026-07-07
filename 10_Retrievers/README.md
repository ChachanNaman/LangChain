# Retrievers

A retriever is a LangChain component that fetches relevant documents from a
data source in response to a user query.

## Types Covered

- **Wikipedia Retriever** — queries Wikipedia directly
- **VectorStore Retriever** — similarity search on a vector store
- **MMR (Maximum Marginal Relevance)** — balances relevance and diversity
- **Multi-Query Retriever** — reformulates the query multiple ways for better recall
- **Contextual Compression Retriever** — trims irrelevant content from retrieved chunks

## Files

| File | What it covers |
|---|---|
| `01_wikipedia_retriever.py` | Basic Wikipedia retrieval |
| `02_vectorstore_retriever.py` | Retrieval from a Chroma vector store |
| `03_mmr_retriever.py` | MMR strategy |
| `04_multi_query_retriever.py` | Multi-query strategy |
| `05_contextual_compression_retriever.py` | Contextual compression |