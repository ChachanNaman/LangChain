from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
#its used in chains mainly to parse the output of the model into string format

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

#1st prompt -> detailed report 
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on following text. \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()
#template1 -> sent to model to generate detailed report -> output of model sent to parser to convert it into string format -> that string is sent to template2 to generate summary -> that summary is sent to model again to generate final output
chain = template1 | model | parser | template2 | model | parser 
#this is the pipeline , entire flow 
result = chain.invoke({'topic': 'Black Hole'})

print(result)