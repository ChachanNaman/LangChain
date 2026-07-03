Vector store : 
A vector store is a sys designed to store and retrieve data as numerical vectors

key features : 
1.storage : ensures vector and their associated metadata(movie_id,name, date) are 
            retained (in-memory for quick lookups and disk for long term)
2.Similarity search : for querying vector , helps retrieving 
3.Indexing : enables fast searching on high dimensional vectors 
        (10 lakh vector -> clusters[10 clusters-> each 1 lakh vectors] and see for centroid 
        which is similar query vector now ignore all cluster and focus on 1 cluster and 
        now calc query score with only 1 lakh comparission)
4.CRUD oper : create , read, update, delete operation on vector database

USE CASE -> 
semantic search , rag, reco sys, img searching


