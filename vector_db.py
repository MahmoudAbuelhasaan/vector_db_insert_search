from qdrant_client import QdrantClient
from qdrant_client.models import Distance , VectorParams

class VectorDB:

    def __init__(self):
        self.clint = QdrantClient(host="localhost",port="6333")   #url = http://localhost:6333
        self.collection_name = 'myCollection'
        self.vector_size = 384  #configrable based on llm

        self._setup_collection()

    
    def _setup_collection(self):
        pass

    def insert_vectors(self,vectors,payload,ids):
        pass

    def search(self,query_vector,limit=3):
        pass