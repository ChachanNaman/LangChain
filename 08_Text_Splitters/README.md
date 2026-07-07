# 08 — Text Splitters

Before text can be embedded and stored in a vector store, large documents need to be broken into smaller chunks — small enough to fit an embedding model's context window and to keep retrieval precise (a whole book embedded as one vector is useless for similarity search; a well-sized paragraph isn't). This folder covers four splitting strategies, from crudest to most sophisticated.

## Files

| File | Strategy | What it shows |
|---|---|---|
| [`1_LengthBased.py`](./1_LengthBased.py) | Length-based | `CharacterTextSplitter` with a fixed `chunk_size`, splitting purely by character count with no regard for word/sentence boundaries — the crudest approach, but a useful baseline |
| [`2_TextStructureBased.py`](./2_TextStructureBased.py) | Recursive / structure-based | `CharacterTextSplitter` used with text-structure awareness — the *recursive* idea (see below) splits on paragraph breaks first, falls back to line breaks, then words, then characters, only as needed |
| [`3_DocumentBased.py`](./3_DocumentBased.py) | Language-aware | `RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, ...)` — splits code (or Markdown) on syntax-aware boundaries like `\nclass`, `\ndef` instead of generic whitespace, so a function body doesn't get chopped mid-block. See [`3_markdown_and_code_separators.png`](./3_markdown_and_code_separators.png) for the full separator list LangChain uses per language. |
| [`4_SemanticBased.py`](./4_SemanticBased.py) | Semantic | `SemanticChunker` — embeds each sentence, compares cosine similarity between consecutive sentences, and splits wherever similarity drops sharply (a topic change), using a standard-deviation threshold rather than a fixed size |

## The recursive idea (behind `2_TextStructureBased.py`)

Recursive splitting tries the "natural" boundaries first and only breaks things down further if a chunk is still too big:

```
paragraph break (\n\n) → line break (\n) → word (space) → character ("")
```

At each level, if a chunk still exceeds `chunk_size`, the splitter recurses to the next, finer-grained separator — and where possible, it re-merges small adjacent pieces back up toward `chunk_size` rather than leaving tiny fragments.

## Choosing a strategy

| Strategy | Use when |
|---|---|
| Length-based | You just need a quick, predictable chunk size and don't care about breaking mid-sentence |
| Structure-based (recursive) | General prose — you want chunks that roughly respect paragraph/sentence boundaries |
| Language-aware | Splitting source code or Markdown, where breaking inside a function or code block would lose meaning |
| Semantic | You care most about topic coherence per chunk — worth the extra embedding calls when retrieval quality matters most |

## Sample data

[`sample.pdf`](./sample.pdf) is a generic placeholder PDF used by `1_LengthBased.py` — swap in any PDF to try it on real content.
