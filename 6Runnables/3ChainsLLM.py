from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template = 'Suggest a catch blog title about {topic}',
    input_variables = ['topic']
)
chain = LLMChain(llm = model, prompt = prompt)


chain = prompt | model

# result = chain.invoke({
#     "topic": topic
# })

# print(result.content)
topic = input('Enter a topic : ')
output = chain.run(topic)

print("Generated blog title : ", output)