import os
from dotenv import load_dotenv
from emails import  emails_multilinhas
import google.genai as genai
load_dotenv()
MINHA_CHAVE_API = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=MINHA_CHAVE_API)
chat = client.chats.create(model='gemini-2.5-flash')

emails_organizados = []

def organizar_emails(emails):
    for email in emails:
        resposta = chat.send_message(f"Retorne uma linha resumindo o email nesse formato (assunto: remetente - resumo):{email}")
        
        print(resposta.text,'\n')
    return emails_organizados

organizar_emails(emails_multilinhas)

print(emails_organizados)