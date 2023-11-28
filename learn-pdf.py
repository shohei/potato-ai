import os
from llama_index import download_loader

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()
documents = loader.load_data(file='data/hatake.pdf')
print(documents)


from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

persist_dir = "./storage/"

# save to disk
if not os.path.exists(persist_dir):
    os.mkdir(persist_dir)
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir)


