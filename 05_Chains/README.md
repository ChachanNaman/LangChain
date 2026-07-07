# 05 — Chains

A **chain** in LangChain Expression Language (LCEL) is just a pipeline built with the `|` (pipe) operator: `prompt | model | parser`. Output of one step becomes input of the next, the same way Unix pipes work. This folder covers the four chain shapes you'll actually use.

## Files

| File | Chain shape | What it shows |
|---|---|---|
| [`1_Simple_chain.py`](./1_Simple_chain.py) | Single pipeline | The base case: `prompt \| model \| parser`. Also calls `chain.get_graph().print_ascii()` to visualize the pipeline in the terminal. |
| [`2_Sequential_chain.py`](./2_Sequential_chain.py) | Sequential | One prompt's output feeds the next prompt's input: generate a detailed report on a topic, then summarize that report into 5 key points — `prompt1 \| model \| parser \| prompt2 \| model \| parser`. |
| [`3_Parallel_chain.py`](./3_Parallel_chain.py) | Parallel | `RunnableParallel` runs two independent branches on the *same* input at once (generate notes + generate a quiz from the same text), then a third chain merges both results into one document. |
| [`4_Conditional_chain.py`](./4_Conditional_chain.py) | Conditional | `RunnableBranch` picks which chain to run based on a condition: classify feedback sentiment first, then branch to a "respond to positive feedback" chain or a "respond to negative feedback" chain depending on the result, with a fallback for anything unrecognized. |

## How to read a chain

- **Sequential** — straight line, `A → B → C`. Use when each step genuinely depends on the previous step's output.
- **Parallel** (`RunnableParallel`) — fan-out, same input to multiple independent branches at once, then usually fan back in. Use when two pieces of work don't depend on each other — running them in parallel is both simpler and faster than doing them one after another.
- **Conditional** (`RunnableBranch`) — a chain that picks its own next step at runtime based on the previous output, similar to an `if`/`elif`/`else`. `4_Conditional_chain.py` pairs this with `PydanticOutputParser` so the branch condition (`x.sentiment == 'positive'`) is checking a validated field, not raw text.

All four examples reuse the same three primitives from earlier folders — `PromptTemplate` ([`02_LangChain_Prompts`](../02_LangChain_Prompts)), a chat model ([`01_LangChain_Models`](../01_LangChain_Models)), and an output parser ([`04_Output_Parsers`](../04_Output_Parsers)) — chains are just different ways of wiring those three together.
