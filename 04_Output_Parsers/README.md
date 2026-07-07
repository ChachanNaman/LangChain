# 04 — Output Parsers

`with_structured_output()` (see [`03_Structured_Output`](../03_Structured_Output)) only works with models that support structured generation natively. **Output parsers** are the fallback: the model still returns plain text, but the parser knows how to turn that text into structured data — and, crucially, can inject formatting instructions into the prompt so the model's raw output is parseable in the first place.

## Files

| File | Parser | What it shows |
|---|---|---|
| [`1_ManualChaining.py`](./1_ManualChaining.py) | *(none)* | The "before" example: two prompts chained by hand — `model.invoke()` → take `.content` → feed into the next `PromptTemplate` manually. No parser, no `\|` chain. This is the baseline the rest of the folder improves on. |
| [`2_StrOutputParser.py`](./2_StrOutputParser.py) | `StrOutputParser` | The same two-step pipeline, now written as one LCEL chain: `template1 \| model \| parser \| template2 \| model \| parser`. `StrOutputParser` just extracts `.content` as a plain string so the chain can keep piping without manual unwrapping. |
| [`3_JsonOutputParser.py`](./3_JsonOutputParser.py) | `JsonOutputParser` | Asks the model for a fictional person's `name`/`age`/`city`. The parser's `get_format_instructions()` is injected into the prompt via `partial_variables` so the model knows to respond with parseable JSON. |
| [`4_JsonOutputParser_Example.py`](./4_JsonOutputParser_Example.py) | `JsonOutputParser` | Same idea, parameterized — asks for facts about any `{topic}` instead of a fixed person schema. |
| [`5_StructuredOutputParser.py`](./5_StructuredOutputParser.py) | `StructuredOutputParser` | Defines the expected fields with `ResponseSchema(name=..., description=...)` — a lighter-weight alternative to a full Pydantic/TypedDict schema when you just need named string fields with descriptions. |
| [`6_PydanticOutputParser.py`](./6_PydanticOutputParser.py) | `PydanticOutputParser` | ⚠️ Currently an empty stub — not yet written. The intended pattern: define a `pydantic.BaseModel` schema, wrap it in `PydanticOutputParser(pydantic_object=Schema)`, and use its `get_format_instructions()` the same way as the JSON/Structured parsers above, but get back a validated Pydantic object instead of a raw dict. |

## Key idea: `format_instructions`

Every parser except `StrOutputParser` needs the model to know *how* to format its answer. The pattern is always the same:

```python
parser = JsonOutputParser()  # or StructuredOutputParser, PydanticOutputParser...

template = PromptTemplate(
    template="...your instructions... \n {format_instructions}",
    input_variables=[...],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser
```

`parser.get_format_instructions()` generates a text block describing the exact output shape the model should produce; `partial_variables` bakes it into the prompt so you don't have to pass it in on every `.invoke()`. The parser then turns the model's (hopefully compliant) text response back into a Python object.

## `StrOutputParser` vs. `with_structured_output()`

`StrOutputParser` doesn't parse anything meaningful — it just standardizes on `.content` so chains can pipe cleanly. For real structured data, use `JsonOutputParser` / `StructuredOutputParser` / `PydanticOutputParser` here, or prefer `with_structured_output()` (see [`03_Structured_Output`](../03_Structured_Output)) whenever the model supports it — it's more reliable since the provider enforces the schema instead of hoping the model followed the format instructions.
