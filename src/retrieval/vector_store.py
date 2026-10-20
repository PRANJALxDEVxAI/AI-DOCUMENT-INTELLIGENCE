
import numpy as np
from src.embeddings.embedder import create_embedding, cosine_similarity


def retrieve_chunks(query, chunks, top_k=3):
    query_embedding = create_embedding(query)

    results = []

    for chunk in chunks:
        chunk_embedding = create_embedding(chunk)

        similarity = cosine_similarity(
            query_embedding,
            chunk_embedding
        )

        results.append((similarity, chunk))

    results.sort(key=lambda item: item[0], reverse=True)

    return results[:top_k]
