from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template = 'Suggest a catch blog title about {topic}',
    input_variables = ['topic']
)

topic = input('Enter the topic : ')

formatted__input = prompt.format(topic = topic)

result = model.invoke(formatted__input)

print("GENERATED BLOG TITLE : ", result)

