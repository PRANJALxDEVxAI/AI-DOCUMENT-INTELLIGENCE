
from src.ingestion.pdf_loader import extract_text_from_pdf
from src.chunking.chunker import create_chunks
from src.retrieval.vector_store import retrieve_chunks


def main():
    pdf_path = "data/documents/1st Year CSIT Booklet.pdf"

    text = extract_text_from_pdf(pdf_path)
    chunks = create_chunks(text)

    query = "Course structure and list of subjects for B.Tech first year CSIT"

    results = retrieve_chunks(query, chunks, top_k=10)

    print("\nQuestion:", query)

    for i, (score, chunk) in enumerate(results, start=1):
        print(f"\n--- Result {i} | Similarity: {score:.4f} ---")
        print(chunk)


if __name__ == "__main__":
    main()
