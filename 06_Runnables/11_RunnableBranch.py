from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = ' generate a detailed 720 words report on {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = 'summarize the text of {text}',
    input_variables=['text']
)

report_gen = RunnableSequence(prompt1, model , parser)

def word_count(text):
    return len(text.split())

branch_chain = RunnableBranch(
    #(if condn, then pass thr runable)
    (lambda x : len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()  #default branch
)

final_chain = RunnableSequence(report_gen, branch_chain)

print(final_chain.invoke({'topic' : 'russia vs usa'}))