from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)

link = 'https://www.flipkart.com/apple-macbook-neo-a18-pro-2026-pro-8-gb-256-gb-ssd-tahoe-mhfa4hn-a/p/itm9fce39e65bd7e?pid=COMHH8C57Y6W6NZU&lid=LSTCOMHH8C57Y6W6NZUASDOLA&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=c4017c23-7407-4507-8e41-5fbcc86c09d8.COMHH8C57Y6W6NZU.SEARCH&ppt=None&ppn=None&ssid=rxgowjggog0000001782149224282&ov_redirect=true'

loader = WebBaseLoader(link) #can pass multiple urls 

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question' : 'what is the product specs ?' , 'text' : docs[0].page_content})

print(result)

