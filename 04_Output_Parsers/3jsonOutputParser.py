from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

#whenever i use json outpur parsrr, i have to send additional insttuction (format_instructions) to the model which type of output you want , and parser.get_format_instructions() will return the instruction to the model in the prompt about how to format the output in json format so that parser can parse it correctly.
parser = JsonOutputParser()
#first wrote prompt then call model 
template = PromptTemplate(
    template = 'give me name , age and city of a fictinonal person. \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions' : parser.get_format_instructions()}  
)
#get_format_instructions() -> it will return a json object 
# prompt = template.format()
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser 
result = chain.invoke({})
print(result)