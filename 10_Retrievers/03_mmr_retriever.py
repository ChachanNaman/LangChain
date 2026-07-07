#MMR 
#how can we pick results that are not only relevant to search querry , but differs from each other 
#designed to reduce redundancy in retrieved results maintaing high relevance to the query
#in regular -> all similar to each others , repeat same info, no diversity 
#in MMR -> picks most relevant doc first, next pick most disimilar to first 

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS

# Initialize OpenAI embeddings
embedding_model = OpenAIEmbeddings()

# Step 2: Create the FAISS vector store from documents
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# Enable MMR in the retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",                   # <-- This enables MMR
    search_kwargs={"k": 3, "lambda_mult": 0.5}  # k = top results, lambda_mult = relevance-diversity balance
) #LESS THE lambda_mult MORE DIVERSE THE RESULT 

query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

# --- Result 1 ---
# LangChain is used to build LLM based applications.

# --- Result 2 ---
# Embeddings are vector representations of text.

# --- Result 3 ---
# LangChain supports Chroma, FAISS, Pinecone, and more.

