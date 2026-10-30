
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def gerar_resposta(mensagens):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "Chave da Groq não encontrada no arquivo .env."
        )

    cliente = Groq(api_key=api_key)

    resposta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente virtual amigável. "
                    "Responda em português de forma clara "
                    "e ajude o usuário com suas dúvidas."
                )
            },
            *mensagens
        ],
        temperature=0.7,
        max_tokens=1024
    )

    return resposta.choices[0].message.content
