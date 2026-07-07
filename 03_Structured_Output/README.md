# 03 — Structured Output

By default an LLM returns free-form text. **Structured output** means forcing it to return data in a well-defined, parseable format (usually JSON) instead — so you can plug the result straight into code without parsing prose.

See [`8_WhenToUseWhat.png`](./8_WhenToUseWhat.png) for a visual decision guide.

## Why it matters

- **Data extraction** — e.g. upload a resume → extract text → LLM → JSON (`name`, `location`, `experience`, ...) → store in a database. Or: an Amazon review → extract keywords, pros/cons, and sentiment.
- **Agents** — a tool-calling agent needs the LLM's output in a fixed shape (e.g. numbers for a calculator tool) to hand off to the next step reliably.

## Two ways to get structured output

- **Models that support structured generation** — use `model.with_structured_output(schema)`. Under the hood this works one of two ways depending on the provider: **JSON mode** (the model is constrained to emit valid JSON) or **function/tool calling** (the schema is passed as a "tool" and the model "calls" it with arguments) — e.g. OpenAI uses function calling here.
- **Models that don't** (e.g. some HuggingFace models) — you parse the raw text output yourself. See [`04_Output_Parsers`](../04_Output_Parsers) for that approach.

`with_structured_output()` accepts three kinds of schema, each demonstrated here:

## Files

| File | Schema type | What it shows |
|---|---|---|
| [`1_TypedDict.py`](./1_TypedDict.py) | — | Plain Python `TypedDict` basics (no LLM yet) — a dict with an enforced *shape*, but no runtime validation |
| [`2_StrOutput_TypedDict.py`](./2_StrOutput_TypedDict.py) | `TypedDict` | First real example: `model.with_structured_output(Review)` where `Review` is a `TypedDict` |
| [`3_StrOutput_Annotated_TypedDict.py`](./3_StrOutput_Annotated_TypedDict.py) | `TypedDict` + `Annotated` | Adds `Annotated[type, "description"]` so each field carries an instruction the LLM reads, plus `Optional` fields |
| [`4_Pydantic.py`](./4_Pydantic.py) | — | Plain `pydantic.BaseModel` basics (no LLM yet) — real validation, type coercion, `EmailStr`, `Field(gt=..., lt=..., default=...)` |
| [`5_StrOutput_Pydantic.py`](./5_StrOutput_Pydantic.py) | `pydantic.BaseModel` | Same review-extraction task as above, now with a validated Pydantic schema and `Literal["pos", "neg"]` for constrained values |
| [`6_Json_schema.json`](./6_Json_schema.json) | — | A hand-written JSON Schema example (framework-agnostic, no Python types involved) |
| [`7_StrOutput_Json.py`](./7_StrOutput_Json.py) | raw JSON Schema | Same task again, this time passing a plain `dict` JSON Schema straight to `with_structured_output()` — useful when you don't want a Python type dependency at all |

## TypedDict vs. Pydantic vs. JSON Schema

| | `TypedDict` | `Pydantic` | JSON Schema |
|---|---|---|---|
| Validation | ❌ none — just a type hint | ✅ real runtime validation + coercion | ✅ (enforced by the LLM provider, not Python) |
| Best for | Quick, low-stakes schemas | Anything you'll actually validate/coerce (also why FastAPI uses it) | Framework-agnostic schemas, or when you don't want a Python class at all |

**Rule of thumb:** reach for `TypedDict` for a quick prototype, `Pydantic` when you need real validation (the field values actually matter downstream), and raw JSON Schema when you want zero Python-type coupling.
