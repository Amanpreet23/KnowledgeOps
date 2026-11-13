import openai
from dotenv import load_dotenv
import os
load_dotenv()

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

for m in client.models.list():
    print(m)