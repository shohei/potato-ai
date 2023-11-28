import os
from llama_index import download_loader
import os

from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

persist_dir = "./storage-txt/"

# save to disk
if not os.path.exists(persist_dir):
    os.mkdir(persist_dir)
documents = SimpleDirectoryReader("data-txt").load_data()
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir)
