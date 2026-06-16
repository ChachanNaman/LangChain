from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on topic {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'Give 5 most important out of {text}',
    input_variables = ['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic' : 'cricket'})

print(result)