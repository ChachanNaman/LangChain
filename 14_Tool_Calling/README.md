# 14 — Tool Calling

[`13_Tools`](../13_Tools) covered *building* a tool. This folder covers what happens next: how an LLM decides to use one, and how that decision actually turns into code running.

## The three steps

1. **Tool binding** — registering a tool with the LLM via `llm.bind_tools([tool1, tool2, ...])`. This tells the model what tools exist, what each one does, and what input schema (arguments) each expects. The model now knows *what's available* — it hasn't used anything yet.
2. **Tool calling** — during a conversation, the LLM decides it needs a specific tool and outputs *which* tool to call and *what arguments* to call it with. Crucially: **the LLM never runs the tool itself.** It only suggests the call — running an arbitrary function chosen by the model with no check would be dangerous. The model advises; LangChain (or your code) executes.
3. **Tool execution** — the actual Python function runs, using the arguments the LLM suggested, and the result is fed back to the model so it can produce a final answer grounded in that result.

```
LLM knows what tools exist  →  LLM decides to call one + picks arguments  →  code actually runs it  →  result fed back to LLM
        (binding)                          (tool calling)                      (tool execution)
```

## Files

| File | What it shows |
|---|---|
| [`01_tool_calling_intro.ipynb`](./01_tool_calling_intro.ipynb) | The full binding → calling → execution cycle end to end with one `multiply` tool: bind it to a Groq model, send a plain "hi how are you" (no tool call happens) vs. "can you multiply 7 by 9" (the model responds with a tool call instead of text), manually execute the suggested tool call, append the result back into the message list as a `ToolMessage`, and get the model's final answer |
| [`02_tool_calling_currency_example.ipynb`](./02_tool_calling_currency_example.ipynb) | A more realistic two-tool example: currency conversion. `get_conversion_factor` hits a live exchange-rate API; `convert` does the actual multiplication. Introduces `InjectedToolArg` — the LLM supplies `base_currency_value`, but `conversion_rate` is deliberately withheld from the LLM's control and injected by your code after running the first tool, so the model can't just make up a plausible-looking rate |

## Message flow in practice

```python
messages = [HumanMessage("Can you multiply 7 by 9")]

result = llm_with_tools.invoke(messages)   # result.tool_calls[0] -> {'name': 'multiply', 'args': {'a': 7, 'b': 9}, ...}

tool_result = multiply.invoke(result.tool_calls[0])   # actually runs multiply(a=7, b=9) -> wrapped as a ToolMessage
messages.append(tool_result)

llm_with_tools.invoke(messages).content   # "The product of 7 and 9 is 63"
```

## Why `InjectedToolArg` matters (`02_tool_calling_currency_example.ipynb`)

For "convert 10 USD to INR", you *want* the LLM to supply `base_currency_value=10`, but you do **not** want it inventing the conversion rate — that has to come from the real API call your code just made via `get_conversion_factor`. `Annotated[float, InjectedToolArg]` marks `conversion_rate` as an argument the LLM is never asked to fill in; your code injects the real value into `tool_call['args']` after running the first tool and before running the second. This is the pattern for chaining tool calls where one tool's *real* output must feed the next tool's input — never a value the model guesses.

## Setup

```bash
pip install langchain-groq
```

Add a `.env` file in this folder with:
```env
GROQ_API_KEY=your_key_here
EXCHANGE_RATE_API_KEY=your_key_here
```

Get a free `EXCHANGE_RATE_API_KEY` from [exchangerate-api.com](https://www.exchangerate-api.com/).
