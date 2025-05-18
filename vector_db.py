from qdrant_client import QdrantClient
from qdrant_client.models import Distance , VectorParams

class VectorDB:

    def __init__(self):
        self.client = QdrantClient(host="localhost",port="6333")   #url = http://localhost:6333/
        self.collection_name = 'myCollection'
        self.vector_size = 384  #configrable based on llm

        self.__setup_collection()

    
    def __setup_collection(self):
        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_size,
                    distance=Distance.COSINE
                )
            )

    def insert_vectors(self,vectors,payloads,ids):
        self.client.upsert(
            collection_name=self.collection_name,
            points= [{
                "id":id,
                "vector":vector,
                "payload":payload

            } for id,vector,payload in zip(ids,vectors,payloads)
            ]
        )
        

    def search(self,query_vector,limit=3):
        return self.client.search(
            collection_name= self.collection_name,
            query_vector = query_vector,
            limit=limit
        )