import os
from dotenv import load_dotenv
import google.genai as genai
load_dotenv()
MINHA_CHAVE_API = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=MINHA_CHAVE_API)
chat = client.chats.create(model='gemini-flash-latest')

print("Chatbot iniciado! Digite 'sair' para encerrar.")
print("-*-"*15)
prompt = input("Você: ")
while prompt.lower() != "sair":
    # Envia a mensagem
    resposta = chat.send_message(prompt)
    
    # Imprime a resposta
    print(f"Gemini: {resposta.text}")
    print("-*-"*15)
    
    # Pede a próxima entrada
    prompt = input("Você: ")