from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#i have 3 things = prompt -> model -> parser 
load_dotenv()

prompt = PromptTemplate(
    template = 'Generate 5 line summary of {topic}',
    input_variables = ['topic']
)

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

# | -> pipe operator  (langchain expression language)
chain = prompt | model | parser    #Pipeline

result = chain.invoke({'topic' : 'cricket'})

print(result)

chain.get_graph().print_ascii()
