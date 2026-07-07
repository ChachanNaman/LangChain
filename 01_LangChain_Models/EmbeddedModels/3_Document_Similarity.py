from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embed = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat kholi is a great player",
    "MS Dhoni is a great player",
    "Naman is a great player",
    "Rohit is a great player",
    "Dhruv is a great player",
]

query = 'Tell me about Naman'

doc_embedding = embed.embed_documents(documents)
query_embedding = embed.embed_query(query)

print(cosine_similarity([query_embedding], doc_embedding))

