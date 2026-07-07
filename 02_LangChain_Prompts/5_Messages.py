from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

messages = [
    SystemMessage(content = 'You are a doctor'),
    HumanMessage(content = 'Tell me about Heart Diseases')
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)