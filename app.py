import google.generativeai as genai
from PIL import Image
import requests
from io import BytesIO
import pyttsx3

# Substitua 'SUA_CHAVE_DE_API' pela sua chave do Gemini
genai.configure(api_key="AIzaSyCGGfJy7wg9cjuCeHlfnhby7RkLjk638A0")

# Seleciona o modelo Gemini Pro Vision
model = genai.GenerativeModel('gemini-1.5-flash')

# Inicializa o motor de fala
engine = pyttsx3.init()

def carregar_imagem(caminho):
    """
    Carrega uma imagem a partir de um arquivo local ou de uma URL da web.

    Args:
        caminho (str): O caminho do arquivo da imagem no PC ou a URL da imagem na web.

    Returns:
        Image: A imagem carregada, ou None em caso de erro.
    """
    try:
        if caminho.startswith('http://') or caminho.startswith('https://'):
            response = requests.get(caminho, stream=True)
            response.raise_for_status()  # Lança uma exceção para status de erro (4xx ou 5xx)
            imagem = Image.open(BytesIO(response.content))
            return imagem
        else:
            imagem = Image.open(caminho)
            return imagem
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {caminho}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {caminho}: {e}")
        return None
    except Exception as e:
        print(f"Erro ao carregar a imagem de {caminho}: {e}")
        return None

def identificar_elementos(imagem):
    """
    Identifica pessoas, estabelecimentos, pontos turísticos, marcas e o tipo de local na imagem.

    Args:
        imagem (Image): A imagem a ser analisada.

    Returns:
        dict: Um dicionário contendo os elementos identificados.
    """
    if imagem:
        prompt = """
        Analise esta imagem e identifique:
        - Quaisquer pessoas visíveis e seus sentimentos predominantes (feliz, triste, neutro, etc.).
        - Quaisquer estabelecimentos conhecidos (mencione o nome, se souber).
        - Quaisquer pontos turísticos notáveis (mencione o nome).
        - Quaisquer marcas visíveis.
        - O tipo de local geral (por exemplo, rua, parque, restaurante). Se souber o nome específico do local, mencione-o.

        Formate sua resposta como um dicionário Python com as chaves: 'pessoas' (lista de sentimentos), 'estabelecimentos' (lista de nomes), 'pontos_turisticos' (lista de nomes), 'marcas' (lista de nomes), 'tipo_de_local' (string com o tipo e nome, se disponível). Se nenhum elemento for detectado para uma categoria, a chave deve ter uma lista vazia ou valor None.
        """
        response = model.generate_content([prompt, imagem])
        try:
            elementos = eval(response.text)
            if isinstance(elementos, dict):
                return elementos
            else:
                print(f"Aviso: Resposta do modelo não está no formato de dicionário esperado: {response.text}")
                return {
                    'pessoas': [],
                    'estabelecimentos': [],
                    'pontos_turisticos': [],
                    'marcas': [],
                    'tipo_de_local': None
                }
        except (SyntaxError, NameError):
            print(f"Aviso: Erro ao avaliar a resposta do modelo como dicionário: {response.text}")
            return {
                'pessoas': [],
                'estabelecimentos': [],
                'pontos_turisticos': [],
                'marcas': [],
                'tipo_de_local': None
            }
    else:
        return {
            'pessoas': [],
            'estabelecimentos': [],
            'pontos_turisticos': [],
            'marcas': [],
            'tipo_de_local': None
        }

def pesquisar_elementos(elementos):
    """
    Realiza pesquisas no Google para obter informações sobre os elementos identificados.

    Args:
        elementos (dict): Um dicionário com os elementos a serem pesquisados.

    Returns:
        dict: Um dicionário onde as chaves são os tipos de elementos ('estabelecimentos', 'pontos_turisticos', 'marcas')
              e os valores são dicionários (nome do elemento -> lista de resultados da pesquisa).
    """
    resultados_pesquisa = {}
    for tipo, lista_elementos in elementos.items():
        if lista_elementos and tipo in ['estabelecimentos', 'pontos_turisticos', 'marcas']:
            resultados_pesquisa[tipo] = {}
            for elemento in lista_elementos:
                print(f"\nBuscando informações sobre: {elemento}...")
                response = model.generate_content([f"Pesquisar sobre: {elemento}", {"tools": [{"google_search": {}}]}] )
                if response.parts and hasattr(response.parts[0], 'text'):
                    resultados_pesquisa[tipo][elemento] = [response.parts[0].text]
                else:
                    resultados_pesquisa[tipo][elemento] = ["Nenhuma informação encontrada."]
    return resultados_pesquisa

def descrever_ambiente_locomocao(imagem):
    """
    Gera uma descrição textual do ambiente na imagem com foco em informações
    de locomoção e possíveis obstáculos para pessoas com deficiência visual.

    Args:
        imagem (Image): A imagem do ambiente.

    Returns:
        str: A descrição do ambiente com foco em locomoção e obstáculos,
             ou uma mensagem de erro se a imagem for inválida.
    """
    if imagem:
        prompt = """
        Descreva este ambiente de forma detalhada, com foco em auxiliar uma pessoa
        com deficiência visual a se locomover. Inclua informações sobre:

        - A disposição geral do espaço (tamanho, forma).
        - A localização de paredes, móveis grandes e outros objetos relevantes.
        - Identifique caminhos livres e espaços abertos para circulação.
        - Mencione possíveis obstáculos como degraus, desníveis, objetos salientes,
          portas (abertas ou fechadas), corrimãos e outros elementos que possam
          impactar a locomoção.
        - Forneça informações sobre a textura do piso, se discernível (por exemplo,
          liso, antiderrapante, com tapetes).
        - Indique a presença de sons relevantes que possam auxiliar na orientação
          (por exemplo, eco, barulho de água, vozes).
        - Use linguagem clara e direcional (por exemplo, "à sua frente", "à sua direita",
          "três passos à esquerda").
        """
        response = model.generate_content([prompt, imagem])
        if response.parts and hasattr(response.parts[0], 'text'):
            return response.parts[0].text
        else:
            return "Erro: Não foi possível gerar a descrição do ambiente para locomoção."
    else:
        return "Erro: Nenhuma imagem fornecida para descrição da locomoção."

def gerar_audio_descricao(texto):
    """
    Gera um áudio a partir do texto fornecido.

    Args:
        texto (str): O texto a ser convertido em áudio.
    """
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    caminho_imagem = input("Digite o caminho do arquivo da imagem ou a URL da imagem: ")
    imagem_carregada = carregar_imagem(caminho_imagem)

    if imagem_carregada:
        elementos_identificados = identificar_elementos(imagem_carregada)
        print("\nElementos Identificados:\n")
        for chave, valor in elementos_identificados.items():
            if valor:
                print(f"- {chave.replace('_', ' ').title()}: {valor}")
            else:
                print(f"- {chave.replace('_', ' ').title()}: Nenhum encontrado")

        # Geração automática da descrição do ambiente para locomoção e áudio
        descricao_locomocao = descrever_ambiente_locomocao(imagem_carregada)
        print("\nDescrição do Ambiente para Locomoção e Obstáculos:\n")
        print(descricao_locomocao)
        print("\nGerando áudio da descrição para locomoção...")
        gerar_audio_descricao(descricao_locomocao)
        print("Áudio da descrição para locomoção gerado!")

        # Geração automática da pesquisa e exibição dos resultados
        resultados_pesquisa = pesquisar_elementos(elementos_identificados)
        if resultados_pesquisa:
            print("\nResultados da Pesquisa:\n")
            for tipo, resultados_elemento in resultados_pesquisa.items():
                print(f"- {tipo.replace('_', ' ').title()}:")
                for elemento, resultados in resultados_elemento.items():
                    print(f"  - {elemento}:")
                    for i, resultado in enumerate(resultados):
                        print(f"    {i+1}. {resultado}")
                    print(f"  Gerando áudio dos resultados para {elemento}...")
                    gerar_audio_descricao(f"Informações sobre {elemento}. {'. '.join(resultados)}")
                    print(f"Áudio dos resultados para {elemento} gerado!")
        else:
            print("\nNenhum elemento conhecido para pesquisar.")

        print("\nProcessamento da imagem concluído.")

    else:
        print("Não foi possível carregar a imagem. Verifique o caminho ou a URL.")