import google.generativeai as genai
from config import GEMINI_API_KEY

class GeminiAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def gerar_conteudo(self, tipo_trabalho, tema, tamanho):
        prompt = f"""
        Escreva um {tipo_trabalho.lower()} acadêmico sobre o tema: {tema}.
        Use linguagem formal, original e acadêmica. Evite copiar materiais existentes.
        Siga a estrutura: Introdução, Desenvolvimento, Conclusão.
        O texto deve ter tamanho {tamanho} e conter referências genéricas.
        """

        resposta = self.model.generate_content(prompt)

        if not resposta.parts:
            raise ValueError("❌ A IA bloqueou a resposta. Tente mudar o tema ou tornar o pedido mais genérico.")

        return resposta.text
