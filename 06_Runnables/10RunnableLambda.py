from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

def word_counter(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template = 'Write a joke about a {topic}',
    input_variables=['topic']
)

joke_word_counter = RunnableLambda(word_counter)

joke_gen = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'words' : joke_word_counter
})

final_chain = RunnableSequence(joke_gen, parallel_chain)

result = final_chain.invoke({'topic' : 'football'})

final_result = """{} \n word count - {}""".format(result['joke'], result['words'])

print(final_result)

