# 09 — Vector Stores

Notes and a hands-on demo on what a vector store is, how it differs from a vector *database*, and a full Chroma walkthrough.

## Why vector stores exist ([`01_why_vector_stores.md`](./01_why_vector_stores.md))

Take a movie recommendation system: naive **keyword matching** (compare actor, director, genre) fails in both directions — two movies can share every keyword and still not feel similar, or share none and still be near-identical in tone and plot. What you actually want is to compare the *meaning* of each movie's plot, not its tags.

**Embeddings** solve this: a neural network turns a piece of text into a vector of numbers (e.g. 512 dimensions) such that semantically similar text ends up as nearby vectors. Comparing "similarity" then becomes a distance calculation between two vectors (cosine similarity) instead of fuzzy tag matching.

This introduces three new problems, which is exactly what a vector store is built to solve:
1. **Generating** the embedding vectors in the first place
2. **Storing** them — a regular relational database (MySQL, Oracle) isn't built for this
3. **Searching** them efficiently — comparing a query vector against every stored vector one-by-one doesn't scale to millions of records; you need smarter (indexed) semantic search

## What a vector store is ([`02_what_is_a_vector_store.md`](./02_what_is_a_vector_store.md))

A system designed specifically to store and retrieve data as numerical vectors. Core capabilities:

- **Storage** — vectors plus their associated metadata (e.g. `movie_id`, `name`, `date`), in-memory for fast lookups and/or on disk for persistence
- **Similarity search** — the core retrieval operation: given a query vector, find the closest stored vectors
- **Indexing** — makes similarity search fast at scale. Instead of comparing a query against every one of, say, a million vectors, they're pre-clustered (e.g. 10 clusters of 100k each); the query is compared against cluster centroids first, then only searched within the closest cluster
- **CRUD** — create, read, update, delete operations on stored vectors, same as any database

**Use cases:** semantic search, RAG, recommendation systems, image search.

## Vector Store vs. Vector Database ([`03_vectorstore_vs_vectordb.md`](./03_vectorstore_vs_vectordb.md))

| | Vector Store | Vector DB |
|---|---|---|
| Scope | Storage + retrieval (similarity search) only | Everything a vector store does, *plus* full database features |
| Extra features | — | Distributed architecture (scaling), backup/restore, ACID transactions, concurrency (multiple users), authentication, rich metadata handling |
| Best for | Lightweight services, prototyping, smaller scale | Production environments |
| Examples | FAISS (Meta's library) | Milvus, Qdrant, Pinecone |

**Every vector DB is a vector store, but not every vector store is a vector DB** — a vector DB is a superset built for production; a vector store can be as lightweight as a local FAISS index.

## Chroma ([`05_chroma_notes.md`](./05_chroma_notes.md))

[Chroma](https://www.trychroma.com/) sits between a plain vector store and a full vector DB — lighter than Pinecone, open-source, and friendly for local dev through small/medium production workloads.

**Hierarchy:** Tenant (user) → Database (can have multiple) → Collection (of documents — embeddings + metadata)

**Typical flow:**
```python
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="my_chroma_db",   # Chroma persists to a local SQLite file here
    collection_name="sample"
)

vector_store.add_documents(docs)                                   # add — auto-generates a unique id per doc
vector_store.get(include=["embeddings", "metadatas", "documents"]) # read
vector_store.similarity_search(query="who is the fastest bowler?", k=2)             # search
vector_store.similarity_search_with_score(query="...", k=2)                          # search + relevance score
vector_store.similarity_search_with_score(query="", filter={"team": "RCB"})          # metadata filtering
vector_store.update_document(document_id="...", document=updated_doc)                # update
vector_store.delete(ids=["..."])                                                     # delete
```

## Hands-on demo: [`06_langchain_chroma_demo.ipynb`](./06_langchain_chroma_demo.ipynb)

Runs the full CRUD + search cycle above end-to-end against a small set of IPL cricketer documents: create documents → embed and store them in Chroma → similarity search ("who among these are a bowler?") → search with relevance scores → filter by metadata (`team`) → update a document → delete a document. Requires an `OPENAI_API_KEY` in a `.env` file in this folder (loaded via `python-dotenv`, same pattern as every other folder in this repo).
