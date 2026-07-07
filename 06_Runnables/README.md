# 06 — Runnables

`Runnable` is the interface underneath every LCEL chain — it's *why* `prompt | model | parser` works at all. Every LangChain component (`PromptTemplate`, a chat model, a parser) implements the same `Runnable` interface (`.invoke()`, and the `|` operator to compose), so they can all be piped together interchangeably. This folder builds that idea up from a plain LLM call, through a from-scratch reimplementation of `Runnable` (to show what's actually going on), to the real `Runnable` primitives LangChain ships.

## Files

| File | What it shows |
|---|---|
| [`01_Simple_llm.py`](./01_Simple_llm.py) | The manual way: `prompt.format(...)` then `model.invoke(...)` — no piping, no chain, just two separate calls |
| [`02_PDF_Reader.py`](./02_PDF_Reader.py) | ⚠️ Empty stub — not yet written |
| [`03_ChainsLLM.py`](./03_ChainsLLM.py) | Shows the legacy `LLMChain` + `.run()` API alongside the modern LCEL `prompt \| model` chain, for contrast. `LLMChain` is deprecated in current LangChain — included here as a "what it used to look like" reference, not a recommended pattern |
| [`04_Runnable_FromScratch_Mock_LLM.ipynb`](./04_Runnable_FromScratch_Mock_LLM.ipynb) | **Build a mini-LangChain by hand, part 1.** Implements a fake LLM (`naklillm` — "nakli" = fake/mock in Hindi), a fake `PromptTemplate`, and a fake `LLMChain` from scratch in plain Python, with no LangChain imports at all, to show what these classes are actually doing internally |
| [`05_Runnable_FromScratch_Abstract_Base.ipynb`](./05_Runnable_FromScratch_Abstract_Base.ipynb) | **Part 2.** Introduces an abstract `Runnable` base class (`ABC` + `@abstractmethod`) that the mock LLM and a mock output parser both inherit from — this is the actual insight: everything in LangChain being swappable/composable only works because they all share one interface |
| [`06_Runnable_FromScratch_Multiple_Chains.ipynb`](./06_Runnable_FromScratch_Multiple_Chains.ipynb) | **Part 3.** Chains two of the from-scratch `Runnable`s together (prompt → joke → explanation), completing the mini-LangChain-from-scratch exercise |
| [`07_RunnableSequence.py`](./07_RunnableSequence.py) | Now the real thing: `RunnableSequence(prompt1, model, parser, prompt2, model, parser)` — same idea as `05_Chains`'s sequential chain, built explicitly instead of via `\|` |
| [`08_RunnableParallel.py`](./08_RunnableParallel.py) | `RunnableParallel` — same input (a topic) fanned out to two independent branches (tweet + LinkedIn post) |
| [`09_RunnablePassthrough.py`](./09_RunnablePassthrough.py) | `RunnablePassthrough` — forwards its input unchanged. Used here so a `RunnableParallel` branch can keep the *original* joke text available alongside a second branch that transforms it (explains it) |
| [`10_RunnableLambda.py`](./10_RunnableLambda.py) | `RunnableLambda` — wraps a plain Python function (a word counter) so it can sit inside a chain like any other `Runnable` |
| [`11_RunnableBranch.py`](./11_RunnableBranch.py) | `RunnableBranch` — conditional routing: if a generated report is over 500 words, summarize it; otherwise pass it through unchanged |

`Different_Chains.png` is a reference diagram of the different chain shapes covered across this folder and [`05_Chains`](../05_Chains).

## Why the "from scratch" notebooks matter

Notebooks 04–06 don't import LangChain at all — they reimplement `Runnable`, a mock LLM, and chaining using nothing but a Python `ABC`. The payoff: once you've built the abstraction yourself, `RunnableSequence`/`RunnableParallel`/`RunnableLambda`/`RunnableBranch` (07–11) stop looking like magic — they're just polished, production versions of the same three ideas: a shared `.invoke()` interface, and two ways to compose it (sequential and parallel), plus a conditional branch on top.
