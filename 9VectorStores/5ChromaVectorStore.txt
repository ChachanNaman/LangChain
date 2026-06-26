Chroma : 
is a lightweight , open source , friendly for local dev and small-medium scale production need
lightweight than pinecone and all
can come bw vector store and vector db 

Tenant(user) -> database(can be multiple) -> collection -> of docs (embedding, metadata)

Install libraries -> import openaiEmbeddings, Chroma 
-> Now create document objects  -> create vector store(embedding func, persist directory[where storing], collection_name) 
->chroma mein joh data store horaha in sqlite file -> now crud oper in vector store
ADD : vector_store.add_document(docs) -> generate unique id for each doc 
GET : vector_store.get(include = ['embedding', 'metadata' , 'documents'])-> can see whatever we want to see
SEARCH : vector_store.similarity_search(
    query = ' who is the fastest bowler?', 
    k = 2   -> return the 2 values nearest to the query , if k = 1 then return 1 ans
)
SEARCH score : vector_store.similarity_search_with_score(
    query = ' who is the fastest bowler?', 
    k = 2   -> return the 2 values nearest to the query , if k = 1 then return 1 ans
)  -> return the score of each 
METADATA FILTERING : 
vector_store.similarity_search_with_score(
    query = ""
    filter = {"team" : "RCB"} 
) -> return the data from RCB docs 

UPDATE : 
updated_docs1 = Document(
    page_content = "new updated lines",
    metadata = {"team" : "RCB"}
)

vector_store.update_document(document_id = 'unique id got from add' , document = updated_docs1)