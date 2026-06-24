#there are certain scenario where length and doc based based 
#if in para 2 diff topics then if textstr based then decent chunks size then it divides into diff chunks and cant be that accurate 
#here we need to divide using semantic meaning 
#firstly undsertand the meaning of sentences and if sees difference bw two then perform textSplitting 
#text -> sentence by sentence -> gen embedding of each sentences -> sen1 vector compared to sen2 vector and get the cosine similarity 
#then s2 and s3 then s3 and s4 
#and where i got similarity is low there have to splitting 
#to identify deviation we need std deviation to identify low part in bw 2 sentences 
#if greater then SD Thresold value there we have to split 

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)
