from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = 'pdfs',
    glob = '*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# print(len(docs)) #return the total number of pages of combining all pdfs in a folder ->82 total pages

# print(docs[1].page_content)  #will return page-wise not pdf wise means docs[0 to 82]

# print(docs[1].metadata) #return metadata of pdf of that page 

# docs = loader.lazy_load()
# for document in docs :  
#     print(document.metadata)  return fastly as scanning data , not waiting 