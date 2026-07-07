MY RAG based system can answer live on youtube video i am watching 
Ex : is the video telling about ai ?
     give 5 important points about the lecture ?
System can be Chrome Plugin , StreamLit Website(New tab opens on device there have to paste link and get answers asked)

In this i am building in a jupyter noetbook 

Plan of Action -> 
YT video transcript load(YTloader[langchain component] or YTAPI[yt own apis])
Text Splitter(divide transcript into multiple chunks)
Generate Embedding for transcript and store in VectorStore
Now create a Retriever and send query to it then Retreiver perform Semantic Search in vector store and gives relevant chunks
Once got relevant chunks and have query merge them to make prompt and send to LLM 



