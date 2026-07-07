# 13 — Tools

```
Tools → Tool Calling (tool + LLM) → Agents
```

## Why tools?

LLMs are strong at reasoning and language generation, but on their own they can't access live data, perform real-world actions, call APIs, or run code. A **tool** closes that gap: it's just a Python function packaged in a way the LLM can understand and decide to call. Example: a train-booking function — the LLM can't book a train itself, but it can recognize when to call an `book_irctc_ticket` tool and hand off the actual booking to that function.

**Tools can be built-in** (LangChain ships them, ready to use) **or custom** (you write them for your own APIs/business logic).

## What's an Agent?

An **agent** is an LLM-powered system that can think, decide, and take actions using external tools or APIs:

```
Agent = reasoning & decision-making (LLM) + action (tools)
```

Tools on their own don't do anything — an agent is what decides *when* and *which* tool to call. See [`14_Tool_Calling`](../14_Tool_Calling) for how that binding actually works.

## Files

| File | Covers |
|---|---|
| [`01_builtin_tools.ipynb`](./01_builtin_tools.ipynb) | Ready-made LangChain tools — `DuckDuckGoSearchRun` (web search) and `ShellTool` (run shell commands) invoked directly. Also lists other built-ins: `WikipediaQueryRun`, `PythonREPLTool`, Gmail/Slack message tools |
| [`02_custom_tools.ipynb`](./02_custom_tools.ipynb) | Three ways to build your own tool, from simplest to most explicit (see below) |
| [`03_toolkit.ipynb`](./03_toolkit.ipynb) | A **toolkit** — a collection of related tools packaged together for convenience (e.g. LangChain's `GoogleDriveToolKit` bundles several Drive-related tools). Builds a minimal `MathToolkit` wrapping `add` and `multiply` |

## Three ways to build a custom tool (`02_custom_tools.ipynb`)

Each wraps the same `multiply(a, b)` function, with increasing control:

1. **`@tool` decorator** — the simplest path. Write a plain function with type hints and a docstring, decorate it with `@tool`, and it becomes a `Runnable` (`.invoke()`, `.name`, `.description`, `.args` all just work). The docstring matters — it's what the LLM reads to know what the function does.
   ```python
   @tool
   def multiply(a: int, b: int) -> int:
       """Multiply two numbers"""
       return a * b
   ```
2. **`StructuredTool` + Pydantic** — for stricter input validation, define the arguments as a Pydantic model instead of relying on type hints, then build the tool with `StructuredTool.from_function(func=..., args_schema=...)`.
3. **`BaseTool` subclass** — the abstract base class every tool in LangChain (including `@tool` and `StructuredTool` under the hood) is built on. Subclass it directly, define `args_schema` and a `_run()` method, when you need full control over a tool's behavior.

**Key idea:** you never send the tool's actual code to the LLM — you send its **schema** (`tool.args_schema.model_json_schema()`): name, description, and expected arguments. The LLM decides *when* to call a tool and *what arguments to pass*; your code executes it.

## Setup

```bash
pip install langchain langchain-core langchain-community pydantic duckduckgo-search ddgs langchain_experimental
```
