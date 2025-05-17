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


Pré-requisitos:

    Python Instalado: Se você ainda não tem o Python no seu computador, vai lá no site oficial (https://www.python.org/downloads/) e baixa a versão mais recente.

    Bibliotecas Instaladas: Você precisa ter instalado as seguintes bibliotecas Python. Se você já tentou rodar o código antes, pode ser que já tenha algumas delas. Abra o seu terminal (ou prompt de comando) e rode estes comandos um por um:
    Bash

    pip install google-generativeai
    pip install Pillow
    pip install requests
    pip install pyttsx3
    pip install google-search-python

    Chave da API do Gemini: Você precisa criar uma conta no Google AI Studio (https://makersuite.google.com/app/apikey) e pegar a sua chave de API. Essa chave você vai colocar no código, substituindo "SUA_CHAVE_DE_API" pela sua chave real.

Passo a Passo para Usar:

    Abra o Código: Abra o arquivo .py do "Descreva Aí!" (aquele que você salvou com o código) em um editor de texto (como o Bloco de Notas, VS Code, Sublime Text, etc.).

    Coloque sua Chave da API: Procure pela linha que diz:
    Python

genai.configure(api_key="SUA_CHAVE_DE_API")

E substitua "SUA_CHAVE_DE_API" pela sua chave que você pegou no Google AI Studio. Cuidado para não apagar as aspas! Deve ficar assim (com a sua chave no lugar):
Python

genai.configure(api_key="SUA_CHAVE_DE_API_REAL_AQUI")

Salve o Código: Depois de colocar a sua chave, salve as alterações no arquivo.

Abra o Terminal (ou Prompt de Comando):

    Windows: Aperte a tecla do Windows, digite cmd e pressione Enter.
    macOS: Aperte Command + Espaço, digite terminal e pressione Enter.
    Linux: Geralmente você tem um ícone para abrir o terminal ou pode usar um atalho como Ctrl + Alt + T.

Navegue até a Pasta do Código: Use o comando cd no terminal para ir até a pasta onde você salvou o arquivo .py do "Descreva Aí!". Por exemplo, se você salvou na sua "Área de Trabalho" dentro de uma pasta chamada "NavegAIA", o comando seria algo como:
Bash

cd Desktop/NavegAIA

(Lembre-se de ajustar o caminho para onde você realmente salvou o arquivo.)

Execute o Script: Depois de estar na pasta certa, rode o script com o comando:
Bash

python seu_arquivo.py

(Substitua seu_arquivo.py pelo nome real do arquivo, que no seu caso parece ser app.py)
Bash

    python app.py

    Siga as Instruções: O script vai começar a rodar e vai te fazer algumas perguntas no terminal:
        "Digite o caminho do arquivo da imagem ou a URL da imagem:" Aqui, você vai digitar:
            O caminho completo de uma imagem que está no seu computador (exemplo: C:\Imagens\sala.jpg ou /home/usuario/imagens/quarto.png).
            Ou o link de uma imagem que está na internet (exemplo: https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png). Depois de digitar o caminho ou a URL, pressione Enter.
        "Deseja pesquisar informações sobre os elementos identificados? (s/n):" Se o script encontrar alguma pessoa famosa, lugar conhecido ou marca na imagem, ele vai te perguntar se você quer pesquisar sobre isso no Google. Digite s para sim ou n para não e pressione Enter.
        "Deseja ouvir a descrição do ambiente em áudio? (s/n):" Se você quiser ouvir a descrição do ambiente falada, digite s. Se preferir só ler, digite n e pressione Enter.

    Veja a Mágica Acontecer: O script vai processar a imagem, mostrar a descrição do ambiente na tela, e se você escolheu, vai pesquisar os elementos e/ou falar a descrição em áudio.

Dicas Importantes:

    Caminhos de Arquivo: Se o arquivo da imagem estiver na mesma pasta do script, você pode digitar só o nome do arquivo (exemplo: minha_foto.jpg). Se estiver em outra pasta, precisa do caminho completo.
    URLs: Certifique-se de que a URL da imagem está correta e acessível pela internet.
    Áudio: Para ouvir o áudio, seu computador precisa ter um dispositivo de saída de som funcionando.
    Erros: Se aparecer algum erro no terminal, leia a mensagem com atenção. Ela pode te dar uma pista do que está acontecendo. Se precisar de ajuda para entender o erro, pode me mostrar a mensagem aqui!

Pronto! Seguindo esses passos, você vai conseguir usar o "navegaIA!" para descrever imagens e até descobrir quem ou o que mais está nelas! 😉 Qualquer dúvida, só chamar!
