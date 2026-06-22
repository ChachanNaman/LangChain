from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Write a summary of the following poem - \n {poem}',
    input_variables=['poem']
)

loader = TextLoader('poem.txt', encoding='utf-8') #encoding to treat symbols also

docs = loader.load() #load document in memory

print(type(docs)) #will return a list

print(len(docs)) #will give output as 1 as it treat whole poem.txt as 1 list 

# print(docs[0])  #will return everything about poem.txt

# print(docs[0].page_content) #will give the poem whole

print(docs[0].metadata) #output -> {'source': 'poem.txt'}

chain = prompt | model | parser 

result = chain.invoke({'poem' : docs[0].page_content}) #will send the poem from docs list 

print(result)
