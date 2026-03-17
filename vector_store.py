from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, QueryRequest
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="housing_resources",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

def embed_text(text: str):
    return model.encode(text).tolist()

def load_resources(all_resources):
    for i, resource in enumerate(all_resources):
        text = (
            f"{resource['name']} {resource['resource_type']} "
            f"{resource['services']} {resource['zip_code']}"
        )
        embedding = embed_text(text)
        client.upsert(
            collection_name="housing_resources",
            points=[PointStruct(id=i, vector=embedding, payload=resource)]
        )
    print(f"✅ Loaded {len(all_resources)} resources into vector store")

def search_resources(query: str, top_k: int = 10):
    query_embedding = embed_text(query)
    results = client.query_points(
        collection_name="housing_resources",
        query=query_embedding,
        limit=top_k
    ).points
    return [r.payload for r in results]
