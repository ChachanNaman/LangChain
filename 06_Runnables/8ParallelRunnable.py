#same input passed to different sequentialRunnables

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'generate a twitter post about {topic}',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template = 'generate a linkedin post about {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({   #passed as dictoinary {}
    'tweet' : RunnableSequence(prompt1, model , parser),
    'linkedin' : RunnableSequence(prompt2,model, parser)
})

print( parallel_chain.invoke({'topic' : 'Joined intern in Oracle'}) )