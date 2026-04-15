import os
from dotenv import load_dotenv
from emails import  emails_multilinhas
import google.genai as genai
load_dotenv()
MINHA_CHAVE_API = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=MINHA_CHAVE_API)
chat = client.chats.create(model='gemini-flash-latest')

emails_organizados = []

def organizar_emails(emails):
    for email in emails:
        resposta = chat.send_message(f"Resuma esse email para mim, me diga qual o assunto e quem me mandou e me retorne um item de dicionário em python:\n\n{email}, sem mais nada além do item de dicionário, apenas o codigo em python, sem explicações, sem texto, apenas o item de dicionário em python")
        emails_organizados.append(resposta.text)
        print(emails_organizados)
    return emails_organizados

organizar_emails(emails_multilinhas)

print(emails_organizados)