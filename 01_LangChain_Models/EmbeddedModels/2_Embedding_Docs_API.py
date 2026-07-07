#to generate for multiple
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embed = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
        "Delhi is the capital of india",
        "Naman is a good boy",
        "How are you ?"
]
result = embed.embed_documents(documents)
print(str(result))