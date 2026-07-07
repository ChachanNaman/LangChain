# 01 — LangChain Models

LangChain's `Models` layer is how you talk to an LLM or an embedding model without hard-wiring your code to one vendor. This folder has two kinds of examples: **LLMs** (chat completion) and **Embedded Models** (turning text into vectors).

## `LLMs/` — Chat Models

| File | Provider | Notes |
|---|---|---|
| [`1_ChatModel_OpenAI.py`](./LLMs/1_ChatModel_OpenAI.py) | via `ChatGroq` | Calls a Groq-hosted `llama-3.1-8b-instant` model and prints `result.content` |
| [`2_ChatModel_Anthropic.py`](./LLMs/2_ChatModel_Anthropic.py) | Anthropic | Imports `ChatAnthropic` to call a Claude model |
| [`3_ChatModel_HuggingFace.py`](./LLMs/3_ChatModel_HuggingFace.py) | HuggingFace (API) | `HuggingFaceEndpoint` + `ChatHuggingFace` calling a hosted model (`zephyr-7b-beta`) over the HF Inference API |
| [`4_ChatModel_HuggingFace_Local.py`](./LLMs/4_ChatModel_HuggingFace_Local.py) | HuggingFace (local) | `HuggingFacePipeline.from_model_id()` — downloads and runs a small model (`facebook/opt-350m`) locally, no API key needed |

> **Note:** `1_ChatModel_OpenAI.py` and `2_ChatModel_Anthropic.py` currently both instantiate `ChatGroq` under the hood rather than their filename's provider — looks like a copy/paste carried over from an earlier version. Worth a quick fix if you want the file content to match its name.

All chat model classes share the same interface: build the model, call `.invoke("your prompt")`, read `.content` off the response. That consistency is the whole point of LangChain's Models abstraction — swap the class, keep the rest of your code unchanged.

## `EmbeddedModels/` — Embedding Models

| File | What it shows |
|---|---|
| [`1_Embedding_Query_API.py`](./EmbeddedModels/1_Embedding_Query_API.py) | `embed_query()` — embed a single string into a vector |
| [`2_Embedding_Docs_API.py`](./EmbeddedModels/2_Embedding_Docs_API.py) | `embed_documents()` — embed a list of strings at once |
| [`3_Document_Similarity.py`](./EmbeddedModels/3_Document_Similarity.py) | Embeds a query and a set of documents, then uses `sklearn`'s `cosine_similarity` to rank documents by relevance to the query |

All three use `HuggingFaceEndpointEmbeddings` with the `sentence-transformers/all-MiniLM-L6-v2` model.

## Setup

```bash
pip install -r requirements.txt
```

Then add a `.env` file in this folder with whichever provider keys the script you're running needs (`GROQ_API_KEY`, `ANTHROPIC_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`, etc).
