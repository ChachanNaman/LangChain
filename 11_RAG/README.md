# 11 — RAG (Retrieval-Augmented Generation)

This folder is notes only — it's the conceptual glue that ties [`07_Document_Loaders`](../07_Document_Loaders), [`08_Text_Splitters`](../08_Text_Splitters), [`09_Vector_Stores`](../09_Vector_Stores), and [`10_Retrievers`](../10_Retrievers) together into one pipeline. The hands-on implementation lives in [`12_Project_YouTube_Chatbot`](../12_Project_YouTube_Chatbot).

## Why RAG?

LLMs are giant transformer-based neural networks, pretrained on huge amounts of data. All of that knowledge lives baked into the model's parameters — its **parametric knowledge**. A plain query → LLM → response setup fails in three specific ways:

1. **No access to private data** — a general-purpose model was never trained on your company's internal documents and simply can't answer questions about them.
2. **Knowledge cutoff** — every model has a training cutoff date and has no idea about anything more recent.
3. **Hallucination** — the model can give a fully confident, fluent answer that is simply wrong, with no signal to the user that it's guessing.

## Two ways to fix this — and why RAG usually wins

### Option 1: Fine-tuning

Take a pretrained model and continue training it on a smaller, domain-specific dataset.

- **Supervised fine-tuning** — train on labeled (prompt, desired output) pairs
- **Continued pretraining** — train on unlabeled domain data (e.g. feed it a video transcript)
- **RLHF** — reinforcement learning from human feedback

**Process:** collect labeled data → choose a method (full-parameter fine-tuning vs. LoRA/QLoRA) → train for a few epochs (retraining all weights, or freezing most and updating a few) → evaluate (hallucination rate, answer match).

Fine-tuning *can* address all three problems above — train on private data, retrain periodically on new data, train on "say I don't know" examples to curb hallucination — but at a real cost: **computationally expensive, requires ML expertise, and has to be repeated every time the underlying data changes.**

### Option 2: In-context learning (what RAG is built on)

Instead of updating the model's weights at all, you give it examples or information directly **in the prompt**, and it uses them to answer better — no training involved. This is called **few-shot prompting** when done with examples, and it's actually an *emergent property* of LLMs — the ability appeared on its own as a side effect of scale/training, nobody explicitly trained models to do it.

**RAG is this idea applied to knowledge injection.** Analogy: a student watching a lecture on YouTube has a doubt about gradient descent. Instead of just asking "what is gradient descent?" in isolation, they paste in the relevant part of the video transcript along with their question. The LLM now answers *using that context*, not just its parametric memory.

```
query + retrieved context → prompt → LLM → response
```

RAG solves all three of the original problems, without touching the model's weights at all — which is why it's usually the first thing reached for, with fine-tuning reserved for cases where RAG genuinely isn't enough (e.g. teaching a model an entirely new *behavior*, not just new *knowledge*).

## The RAG pipeline: two phases

RAG combines two ideas — **information retrieval** and **text generation**:

### 1. Indexing — build the external knowledge base (do this once, upfront)

Prepare your knowledge so it can be searched efficiently at query time:

1. **Document ingestion** — load source data into memory (`PyPDFLoader`, `YoutubeLoader`, `GitLoader`, etc. — see [`07_Document_Loaders`](../07_Document_Loaders))
2. **Text chunking** — break large documents into small, semantically meaningful chunks (`RecursiveCharacterTextSplitter`, `SemanticChunker` — see [`08_Text_Splitters`](../08_Text_Splitters))
3. **Embedding generation** — convert each chunk into a dense vector capturing its meaning (`OpenAIEmbeddings`, sentence-transformers — see [`01_LangChain_Models`](../01_LangChain_Models))
4. **Storage** — store each vector alongside its original chunk text and metadata in a vector store (FAISS, Chroma, Pinecone, Qdrant — see [`09_Vector_Stores`](../09_Vector_Stores))

The result is a searchable external knowledge base.

### 2. Retrieval + generation — run this per query

3. **Retrieval** — embed the user's query, semantically search the vector store, rank chunks by relevance, and return only the top results (see [`10_Retrievers`](../10_Retrievers)) — e.g. search just the relevant part of a video transcript, not the entire thing.
4. **Augmentation** — combine the retrieved chunks with the original user query into a single prompt.
5. **Generation** — send that augmented prompt to the LLM, which generates its answer grounded in the retrieved context instead of purely from parametric memory.

```
query → embedding → vector search → top-k relevant chunks
                                            │
query + retrieved chunks → prompt → LLM → response
```

## See it built end-to-end

[`12_Project_YouTube_Chatbot`](../12_Project_YouTube_Chatbot) implements this exact pipeline against a real YouTube video's transcript.
