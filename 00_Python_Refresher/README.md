# 00 — Python Refresher

A quick refresher on the core Python features used throughout this repo, before jumping into LangChain. Each file is a small, runnable script — just run it with `python <file>.py` and read the inline comments alongside the output.

## Files

| File | Covers |
|---|---|
| [`01_functions.py`](./01_functions.py) | Positional vs. keyword arguments, default values, `*args`/`**kwargs`, and functions that return multiple values |
| [`02_lambda_functions.py`](./02_lambda_functions.py) | Anonymous (`lambda`) functions vs. regular `def` functions |
| [`03_map_function.py`](./03_map_function.py) | `map()` — applying a function to every item in an iterable |
| [`04_filter_function.py`](./04_filter_function.py) | `filter()` — keeping only the items that satisfy a condition, with and without `lambda` |
| [`05_list_comprehension.py`](./05_list_comprehension.py) | List comprehensions as a concise replacement for manual `for`-loop list building, including conditional comprehensions |
| [`06_strings.py`](./06_strings.py) | String formatting with `.format()`, including named placeholders |
| [`07_iterables.py`](./07_iterables.py) | Iterables vs. iterators — `iter()`, `next()`, and how a `for` loop hides `StopIteration` handling for you |
| [`08_oop.py`](./08_oop.py) | Basic object-oriented programming: classes, `__init__`, `self`, and instance methods |
| [`09_exception_handling.py`](./09_exception_handling.py) | `try`/`except`/`else`/`finally`, catching specific exception types before generic ones, and the `Exception` base class |

## Why this matters for LangChain

LangChain code leans heavily on a few of these patterns — `lambda`s and comprehensions show up in chain composition (`RunnableLambda`), and clean exception handling matters once you're calling external LLM APIs that can fail or rate-limit. This folder is just muscle memory for that.
