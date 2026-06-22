from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template = 'Write a joke about a {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain the joke - {text}',
    input_variables=['text']
)
parser = StrOutputParser()

joke_gen = RunnableSequence(prompt1 , model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explain' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen, parallel_chain)
print(final_chain.invoke({'topic' : 'America'}))

print(final_chain['joke'])
print(final_chain['explain'])
