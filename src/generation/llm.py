
from google import genai

client = genai.Client()


def generate_answer(query, retrieved_chunks):
    context = ""

    for i, (score, chunk) in enumerate(retrieved_chunks, start=1):
        context += f"\n--- Context {i} ---\n{chunk}\n"

    prompt = f"""
You are an assistant answering questions about a document.

Answer the question using only the context provided below.
If the context does not contain the answer, say that you could
not find the answer in the provided document context.
Do not invent facts.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text
