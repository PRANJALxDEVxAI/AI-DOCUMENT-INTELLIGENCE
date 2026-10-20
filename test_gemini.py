
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Explain what RAG is in two simple sentences."
)

print(response.text)
