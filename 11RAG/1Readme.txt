RAG COMPONENTS -> Document Loader, Text Splitter, Vector Store, Retriever 

WHY RAG ?
LLMs are giant trnasformer based neural networks , We pre train llm on huge amount of data 
LLM store all its knowledge in parameters -> Parametric Knowledge(13 billion > 7 millions)
Query -> LLM -> Response 
Situation where LLM fails -> 
1.Private Database Access -> chatgpt dont have that dataset cant answer those quesions
2.Every LLM have some cutoff date -> dont have lated info or recent data 
3.Hallucination -> Models llm give confident full answer but its wrong , but llm gave full confidence answer 


Fine Tuning is the way to solve these problems 
Fine Tuning : 
Takes pre trained model and train again on small domain specific dataset 
Methods -> Supervised Fine tuning -> we provide labeled dataset to out model (Prompt and desiered output)
           Continued Pre Training -> we provide no labeled dataset (like providing transcript to a model of a video)
           RLHF -> reinforcement and human feedback 
Steps : Collect Data(labelled data (prompts and desired outputs))
        Choose a method (Full parameter FT , LORA/QLORA)
        Training start(for few epochs), retrain all weights or feeze some weights
        Evaluate and safety tet (hallucination rate, measure match)
1. When llm trained on provate data -> model will answer
2. Want answers on recent documents -> Can do fine tuning for the new data (repeadtedly fine tuning on data)
3. Hallucination -> can train model on tricky prompts(like dont answer it just say i dont know)
Some Major Problems : Computtionaly Expensive , Need strong knowldege, need updation again and again 


In-Context Learning solves all those 3 problem betterly -> 
Here model learns to solve the task purely by seeing examples in prompt- without updating the weights 
Send examples in prompt to train model better (like providing sentence and its sentiment)(Few shot prompting)
It is LLMs emergent property-> means in-context learning feature automatically got appeared while training llm (by providing examples in prompt)


When student is learning a chapter from youtube video and asks doubt of gradient descent 
soo instead of sending just doubt, send doubt + context (video part of grad desc) 
This is called RAG 
RAG -> is a way to make a lang model smarter by giving extra info at the time you ask question 

QUERY AND CONTEXT injected to prompt -> Prompt -> LLM -> Response 

RAG made up of 2 concepts -> Info retrieval + text generation 
1.Indexing -> creating external knowledge base (deriving context from external knowldege base)
            Preparing your knowldege base soo that it can be efficiently searched at query time 
            Steps of indexing : 
            1. Document Ingestion -> load your source knowledge into memory (using lanchain tools -> PyPDFLoader, YoutubeLoader, GitLoader,etc)
            2. Text Chunking -> break large doc into small meaninggful semantic docs chunks (SemanticChunker, RecurssiveCharacterTextSplitter)
            3. Embedding Generation -> convert each chunk into a dense vector that captures its meaning. (Semantic searching always done through vectors)
                                        (OpenAIEmbeddings, Sentence ) harr chunk ke lie ek dense vector
            4. Storing in vector store -> store these vector along with original chunk text + metadata
                                        (FAISS, CHROMA, PineCome, Qdrant)
            Now i can use this my vector store as external knowldege base

2.Retrieval -> Understanding query and finds chunks related to query in external knowldge base 
            Now have to understant which chunk is the best according to the query 
            Finding most relevant pieces of info from indexed data 
            Query - Retrieval -> semantic search on Vector Store (perform ranking on each)
            Top results given by retrieval
            (search in transcript of the topic that user is asking , not sending entire transcript)

3.Augmentation -> user query and retrieved context made up an prompt
                Now we got most relevant Chunk and query given by user 

4.Generation -> llm generates answer from user query and knowledge 
                Now prompt given to llm model and generates answer 
QUERY -> EMBEDDING VECTOR -> 