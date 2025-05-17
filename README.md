# navagaIA
NavegaIA - É um projeto de análise de Imagens com Gemini com foco em  Acessibilidade

Projeto: Análise de Imagens com Gemini e Descrição para Acessibilidade
Objetivo

Este projeto tem como objetivo analisar o conteúdo de uma imagem, identificando elementos como pessoas, estabelecimentos, pontos turísticos e marcas, além de descrever o ambiente com foco na acessibilidade para pessoas com deficiência visual.
Adicionalmente, o projeto realiza pesquisas online sobre os elementos identificados e gera áudio descrições tanto do ambiente para locomoção quanto dos resultados das pesquisas.

Em resumo, o projeto visa:

    Identificar automaticamente elementos relevantes em uma imagem utilizando o modelo gemini-1.5-flash-001.
    Descrever o ambiente da imagem de forma detalhada, com ênfase em informações cruciais para a locomoção de pessoas com deficiência visual, como obstáculos, caminhos livres e texturas do piso.
    Pesquisar informações adicionais sobre os estabelecimentos, pontos turísticos e marcas detectadas na imagem através do Google Search.
    Gerar áudio das descrições do ambiente e dos resultados das pesquisas, facilitando o acesso à informação para usuários com deficiência visual.

Funcionalidades

O script Python (app.py) implementa as seguintes funcionalidades:

    Carregamento de Imagem: Permite carregar imagens tanto de arquivos locais quanto de URLs da web.
    Identificação de Elementos: Utiliza o modelo Gemini Pro Vision para identificar pessoas (e seus sentimentos), estabelecimentos, pontos turísticos, marcas e o tipo geral de local presente na imagem.
    Pesquisa de Elementos: Realiza pesquisas no Google sobre os estabelecimentos, pontos turísticos e marcas identificadas, fornecendo informações contextuais adicionais.
    Descrição do Ambiente para Locomoção: Gera uma descrição textual detalhada do ambiente da imagem, focando em aspectos relevantes para a locomoção de pessoas com deficiência visual, como disposição do espaço, obstáculos e caminhos livres.
    Geração de Áudio: Converte as descrições do ambiente e os resultados das pesquisas em áudio, utilizando a biblioteca pyttsx3.

Como Utilizar

    Pré-requisitos:
        Python 3.6 ou superior instalado.
        As seguintes bibliotecas Python instaladas:
        Bash

    pip install google-generativeai Pillow requests pyttsx3

    Uma chave de API válida para o Gemini. Você precisará substituir "SUA_CHAVE_DE_API" pela sua chave no código.

Execução:

    Salve o código Python como um arquivo (por exemplo, analise_imagem.py).
    Execute o script a partir do terminal:
    Bash

        python analise_imagem.py

        O script solicitará que você digite o caminho do arquivo da imagem no seu computador ou a URL da imagem na web.
        Após fornecer o caminho ou a URL, o script processará a imagem, exibirá os elementos identificados, a descrição do ambiente para locomoção e os resultados das pesquisas (se houver), além de gerar áudios correspondentes.

Exemplo de Uso

Ao executar o script e fornecer o caminho para uma imagem de uma praça movimentada, a saída no terminal pode ser semelhante a:

Digite o caminho do arquivo da imagem ou a URL da imagem: caminho/para/sua/imagem.jpg

Elementos Identificados:

- Pessoas: ['feliz', 'neutro', 'sorrindo']
- Estabelecimentos: ['Café Central']
- Pontos Turísticos: ['Monumento Histórico']
- Marcas: ['Coca-Cola']
- Tipo De Local: praça pública

Descrição do Ambiente para Locomoção e Obstáculos:

O ambiente parece ser uma praça aberta de tamanho considerável. Há caminhos pavimentados que parecem ser os principais espaços de circulação. À sua frente, você pode notar alguns bancos de praça fixos. À direita, parece haver um pequeno degrau de acesso a uma área com grama. Mais adiante, à esquerda, identifica-se o que parece ser a fachada de um estabelecimento chamado Café Central, com uma porta de entrada visível. Não há corrimãos aparentes nos caminhos. O piso parece ser feito de pedras irregulares em algumas áreas e liso em outras. Ao fundo, avista-se um monumento histórico com uma base elevada, possivelmente com alguns degraus de acesso. É possível ouvir o murmúrio de vozes e o som distante de carros.

Gerando áudio da descrição para locomoção...
Áudio da descrição para locomoção gerado!

Buscando informações sobre: Café Central...
Buscando informações sobre: Monumento Histórico...
Buscando informações sobre: Coca-Cola...

Resultados da Pesquisa:

- Estabelecimentos:
  - Café Central:
    1. O Café Central é uma cafeteria tradicional localizada no coração da cidade, conhecida por seus cafés especiais e bolos caseiros...
  Gerando áudio dos resultados para Café Central...
  Áudio dos resultados para Café Central gerado!
- Pontos Turísticos:
  - Monumento Histórico:
    1. O Monumento Histórico foi erguido em homenagem aos heróis da revolução e é um importante símbolo da cidade...
  Gerando áudio dos resultados para Monumento Histórico...
  Áudio dos resultados para Monumento Histórico gerado!
- Marcas:
  - Coca-Cola:
    1. Coca-Cola é uma marca global de bebidas carbonatadas, conhecida por seu sabor único e campanhas publicitárias icônicas...
  Gerando áudio dos resultados para Coca-Cola...
  Áudio dos resultados para Coca-Cola gerado!

Processamento da imagem concluído.
