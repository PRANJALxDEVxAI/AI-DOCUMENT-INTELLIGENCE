from sentence_transformers import SentenceTransformer

3
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    similarity = dot_product / (magnitude_a * magnitude_b)

    return float(similarity)



def create_embedding(text):
    return model.encode(text)



def main():
    sentences = [
        "Documents required for scholarship verification",
        "What papers are needed for scholarship verification?",
        "The weather is very hot today."
    ]


    embeddings = []

    for sentence in sentences:
        embedding = create_embedding(sentence)
        embeddings.append(embedding)

    for i, sentence in enumerate(sentences):
        print(f"\nSentence {i + 1}: {sentence}")
        print("Embedding dimensions:", len(embeddings[i]))

    print("\n--- Cosine Similarity ---")

    similarity_1 = cosine_similarity(embeddings[0], embeddings[1])
    similarity_2 = cosine_similarity(embeddings[0], embeddings[2])

    print("Sentence 1 vs Sentence 2:", similarity_1)
    print("Sentence 1 vs Sentence 3:", similarity_2)


if __name__ == "__main__":
    main()
    