A retriever is a component in a langchain that fetches relevant document from a data source 
in response to a user query 

Data source(vector store, api) <- RETREIVER <- Query 
Its a a function taking user query and outputing document by search in data source

All retrievers are Runnables (can use retiever to form chain or can use in chain)

Types : 
Data Source Basis -> Wikipedia retiever(query to wikipedia)
                  -> Vector store base (query to vector store)
                  -> Archive Retrievers(query to archive website)
Search Strategy -> MMR(maximum marginal relevance)
                -> Multi querry retrievers
                -> contextual compression retrievers
