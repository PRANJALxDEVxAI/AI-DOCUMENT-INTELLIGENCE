
from src.ingestion.pdf_loader import extract_text_from_pdf
from src.chunking.chunker import create_chunks
from src.retrieval.vector_store import retrieve_chunks
from src.generation.llm import generate_answer


def main():
    pdf_path = "data/documents/1st Year CSIT Booklet.pdf"

    # 1. Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)

    # 2. Split the text into chunks
    chunks = create_chunks(text)

    # 3. Ask the user for a question
    query = input("\nAsk a question about your PDF: ")

    # 4. Retrieve the most relevant chunks
    retrieved_chunks = retrieve_chunks(query, chunks, top_k=3)

    # 5. Generate an answer using Gemini
    answer = generate_answer(query, retrieved_chunks)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()
