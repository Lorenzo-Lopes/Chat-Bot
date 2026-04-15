from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
        {
            "role": "user",
            "content": input("Digite sua mensagem aqui: ")
        }
        ],
        temperature=1,
        max_completion_tokens=2000,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
        stop=None
    )
    

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")