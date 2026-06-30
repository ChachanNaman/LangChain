# It queries the wikipedia api to fetch the relevant conetne for the given querry

# Querry -> wiki api -> retieves(keyword based) -> langchain docs

from langchain_community.retrievers import WikipediaRetriever

#initialise with lang of result 
retriever = WikipediaRetriever(top_k_results = 2, lang = "en")

query = "The geopolitics of india and pakistan perspective to china"

docs = retriever.invoke(query)  #can use invoke as its runnable
##
##
for i, doc in enumerate(docs):
    print(f"---Result {i+1} ---")
    print(f"Content : \n {doc.page_content}...")

