from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="claude-3.8-sonnet-20241022", max_completion_tokens=20)

result = llm.invoke("What is the capital of India?")
print(result.content)  #fetch content to see the result only