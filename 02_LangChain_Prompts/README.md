# 02 — LangChain Prompts

Notes and demos on why LangChain uses `PromptTemplate` / `ChatPromptTemplate` instead of raw Python f-strings, and how to manage conversation history.

## Why `PromptTemplate` over an f-string?

- **Validation** — `PromptTemplate(..., validate_template=True)` errors immediately if the variables you pass don't match the `{placeholders}` in the template, instead of silently producing a broken prompt.
- **Reusability / portability** — a template can be `.save()`d to JSON (see [`template.json`](./template.json)) and `load_prompt()`ed back in any other file or project, decoupled from the Python code that uses it.
- **Ecosystem fit** — templates are `Runnable`s, so they compose directly into LCEL chains (`template | model`) instead of needing a manual `.format()` step before every call.

## Files

| File | What it shows |
|---|---|
| [`1_Static_prompt.py`](./1_Static_prompt.py) | A minimal Streamlit app where the user types a free-form prompt directly — no template, the baseline this folder builds on |
| [`2_Prompt_generator.py`](./2_Prompt_generator.py) | Builds a `PromptTemplate` with input variables and saves it to [`template.json`](./template.json) via `.save()` — **run this first**, it's what `3_Dynamic_prompt.py` loads |
| [`3_Dynamic_prompt.py`](./3_Dynamic_prompt.py) | A Streamlit "research paper explainer" — loads `template.json` with `load_prompt()`, lets the user pick paper/style/length from dropdowns, and runs it through `template \| model` |
| [`4_Chatbot.py`](./4_Chatbot.py) | The simplest possible multi-turn chatbot loop: a plain list of raw strings passed straight to `model.invoke()`, no message roles |
| [`5_Messages.py`](./5_Messages.py) | Introduces LangChain's typed messages — `SystemMessage`, `HumanMessage`, `AIMessage` — a single exchange, not a loop |
| [`6_IntegratedChatbot.py`](./6_IntegratedChatbot.py) | Combines the two above: a real chat loop using typed messages, so the model gets proper role context on every turn |
| [`7_ChatPromptTemplate.py`](./7_ChatPromptTemplate.py) | `ChatPromptTemplate` — a template built from `(role, text)` tuples, so system/human turns can each have their own `{placeholders}` |
| [`8_MessagePlaceholders.py`](./8_MessagePlaceholders.py) | `MessagesPlaceholder` — reserves a slot inside a `ChatPromptTemplate` where a whole chat history gets injected at invoke time, loaded here from [`8_Chat_history.txt`](./8_Chat_history.txt) |

## Key Concepts

**Three message types** — every chat model conversation is built from:
1. `SystemMessage` — sets the model's role/behavior
2. `HumanMessage` — user input
3. `AIMessage` — the model's prior responses (needed so multi-turn context is preserved)

**Two ways to invoke a model:**
1. **Single message** — either static text or a `PromptTemplate`-rendered string
2. **List of messages** (multi-turn) — either a manually built list of typed messages, or a `ChatPromptTemplate` for the dynamic/reusable version

**`MessagesPlaceholder`** — a special slot inside a `ChatPromptTemplate` that injects an entire chat history (a list of messages) at runtime, instead of one fixed `{variable}`. Useful any time a prompt needs "everything said so far" rather than a single value — e.g. a support bot that needs to remember a customer already asked about their refund three messages ago.
