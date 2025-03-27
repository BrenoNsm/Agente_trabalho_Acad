from ia.gemini_agent import GeminiAgent
from documento.doc_creator import DocCreator
from documento.markdown_converter import MarkdownConverter

def main():
    print("=== GERADOR DE TRABALHOS ACADÊMICOS ===")
    
    logo_path = r'Agente_academico\media\image\logo uerr.png'

    nome_materia = input("Matéria: ")
    nome_autor = input("Seu nome: ")
    sobre_o_documento = input("Sobre o que é o documento (ex: trabalho de Filosofia): ")
    nome_curso = input("Curso: ")

    tipo_trabalho = input("Tipo do trabalho (Resumo, Artigo, Relatório...): ")
    tema = input("Tema do trabalho: ")
    tamanho = input("Tamanho do trabalho (curto, médio, longo): ")

    print("\nGerando conteúdo com IA...")
    agente = GeminiAgent()
    texto_gerado = agente.gerar_conteudo(tipo_trabalho, tema, tamanho)
    
    criador = DocCreator(
        nome_materia, nome_autor,
        sobre_o_documento, nome_curso,
        caminho_logo=logo_path
    )

    criador.adicionar_capa()

    # Apenas usando o conversor markdown para o conteúdo
    converter = MarkdownConverter(criador.doc, permitir_listas=True)
    converter.adicionar_texto_formatado(texto_gerado)

    criador.salvar()
    print("✅ Documento gerado com sucesso!")

if __name__ == "__main__":
    main()
