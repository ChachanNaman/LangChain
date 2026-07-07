# 07 — Document Loaders

Document Loaders are the entry point of a RAG pipeline: they pull external data — text files, PDFs, whole directories, web pages — into LangChain's `Document` object (`.page_content` + `.metadata`), so everything downstream (splitters, embeddings, vector stores) works against one consistent type regardless of source.

## Files

| File | Loader | What it shows |
|---|---|---|
| [`1_TextLoader.py`](./1_TextLoader.py) | `TextLoader` | Loads [`poem.txt`](./poem.txt), then pipes the loaded content straight into a `prompt \| model \| parser` chain to summarize it — shows a loader feeding directly into a chain from earlier folders |
| [`2_PyPDFLoader.py`](./2_PyPDFLoader.py) | `PyPDFLoader` | Loads a single PDF ([`file-sample.pdf`](./file-sample.pdf)) and inspects `docs[0].metadata` |
| [`3_DirectoryLoader.py`](./3_DirectoryLoader.py) | `DirectoryLoader` + `PyPDFLoader` | Loads every `*.pdf` in the [`pdfs/`](./pdfs) folder at once — `DirectoryLoader` is a wrapper that applies another loader (here `PyPDFLoader`) across a whole directory, glob-matched |
| [`4_WebBasedLoader.py`](./4_WebBasedLoader.py) | `WebBaseLoader` | Loads a live product page URL and answers a question about it via `prompt \| model \| parser`. ⚠️ Points at a real e-commerce URL that may go stale — swap in any URL to try it yourself |

## `Document` object

Every loader above returns a `list[Document]`, where each `Document` has:
- **`page_content`** — the actual extracted text
- **`metadata`** — a dict of source info (e.g. `{'source': 'poem.txt'}`, or page number for PDFs)

`TextLoader` and `WebBaseLoader` return one `Document` per file/page; `PyPDFLoader` returns one `Document` **per PDF page**, which is why `DirectoryLoader` over multiple PDFs can return dozens of `Document`s from just a couple of files.

## Sample data

[`pdfs/`](./pdfs) contains generic placeholder PDFs (`sample-1.pdf`, `sample-2.pdf`) so the `DirectoryLoader` example runs out of the box — swap in your own PDFs to try it on real documents.
