import pypdf 
from src.chunking.chunker import create_chunks

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path , 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            text = text + (page_text or "")

    return text



def main():
    pdf_path = "data/documents/1st Year CSIT Booklet.pdf"
    text = extract_text_from_pdf(pdf_path)
    chunks = create_chunks(text)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:3]):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk)  

if __name__ == "__main__":
    main()