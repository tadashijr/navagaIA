navagaIA 🧭

NavegaIA - Um projeto inovador de análise de Imagens com Gemini focado em ♿ Acessibilidade ♿

🎯 Objetivo 

Este projeto ambiciona analisar o conteúdo de uma imagem 🖼️, identificando elementos cruciais como:

    👤 Pessoas (e seus sentimentos 😊/😐/🙁)
    🏢 Estabelecimentos
    📍 Pontos Turísticos
    🏷️ Marcas

Além disso, o sistema descreve o ambiente com uma atenção especial à acessibilidade para pessoas com deficiência visual 🧑‍🦯.

Para enriquecer ainda mais a experiência, o projeto realiza pesquisas online 🌐 sobre os elementos identificados e gera áudio descrições 🗣️ tanto do ambiente para auxiliar na locomoção quanto dos resultados das pesquisas.

Em resumo, o projeto visa:

    🧠 Identificar automaticamente elementos relevantes em uma imagem utilizando o poderoso modelo gemini-1.5-flash-001.
    ✍️ Descrever o ambiente da imagem de forma detalhada, com ênfase em informações vitais para a locomoção de pessoas com deficiência visual, como:
        🚧 Obstáculos
        🚶‍♂️ Caminhos livres
        texture Texturas do piso
    🔍 Pesquisar informações adicionais sobre os estabelecimentos, pontos turísticos e marcas detectadas na imagem através do Google Search.
    🎧 Gerar áudio das descrições do ambiente e dos resultados das pesquisas, facilitando o acesso à informação para usuários com deficiência visual.

✨ Funcionalidades ✨

O script Python (app.py) implementa as seguintes funcionalidades incríveis:

    📂 Carregamento de Imagem: Permite o upload de imagens tanto de arquivos locais no seu dispositivo quanto de URLs da web 🌐.
    👁️ Identificação de Elementos: Utiliza a inteligência do Gemini Pro Vision para identificar:
        👤 Pessoas (e seus sentimentos 😊/😐/🙁)
        🏢 Estabelecimentos
        📍 Pontos Turísticos
        🏷️ Marcas
        🗺️ O tipo geral de local presente na imagem.
    🔎 Pesquisa de Elementos: Realiza buscas inteligentes no Google sobre os estabelecimentos, pontos turísticos e marcas identificadas, fornecendo informações contextuais valiosas.
    🚶‍♀️ Descrição do Ambiente para Locomoção: Gera uma descrição textual rica em detalhes do ambiente da imagem, com foco em aspectos cruciais para a locomoção de pessoas com deficiência visual, como:
        📐 Disposição do espaço
        🚧 Obstáculos
        🚶‍♂️ Caminhos livres
    🔊 Geração de Áudio: Converte as descrições do ambiente e os resultados das pesquisas em áudio nítido, utilizando a biblioteca pyttsx3.

⚙️ Como Utilizar ⚙️

Pré-requisitos:

    🐍 Python Instalado: Certifique-se de ter o Python 3.6 ou superior instalado no seu computador. Você pode baixá-lo no site oficial do Python.

    📚 Bibliotecas Instaladas: As seguintes bibliotecas Python são essenciais. Se você já tentou rodar o código antes, algumas podem já estar instaladas. Abra o seu terminal (ou prompt de comando) e execute estes comandos um por um:
    Bash

    pip install google-generativeai
    pip install Pillow
    pip install requests
    pip install pyttsx3
    pip install google-search-python

    🔑 Chave da API do Gemini: Você precisará obter uma chave de API válida para o Gemini. Crie uma conta no Google AI Studio e copie sua chave. Você irá substituir "SUA_CHAVE_DE_API" pela sua chave real no código.

🚀 Execução 🚀:

    💾 Salve o Código: Salve o código Python como um arquivo (por exemplo, analise_imagem.py).
    💻 Abra o Terminal: Abra o terminal (ou prompt de comando) no seu sistema operacional:
        Windows: Pressione a tecla Windows, digite cmd e pressione Enter.
        macOS: Pressione Command + Espaço, digite terminal e pressione Enter.
        Linux: Geralmente há um ícone ou atalho (Ctrl + Alt + T).
    📂 Navegue até a Pasta: Use o comando cd para navegar até a pasta onde você salvou o arquivo .py do NavegaIA. Exemplo:
    Bash

cd Desktop/NavegaIA

(Ajuste o caminho conforme a sua localização.)
🏃 Execute o Script: Execute o script com o comando:
Bash

python app.py

    python app.py

    🗣️ Siga as Instruções: O script será executado e fará algumas perguntas no terminal:
        Digite o caminho do arquivo da imagem ou a URL da imagem: Digite o caminho completo de uma imagem no seu computador (exemplo: C:\Imagens\sala.jpg ou /home/usuario/imagens/quarto.png) ou o link de uma imagem na internet (exemplo: https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png). Pressione Enter.
        Deseja pesquisar informações sobre os elementos identificados? (s/n): Se o script identificar pessoas famosas, lugares conhecidos ou marcas, ele perguntará se você deseja pesquisar sobre eles no Google. Digite s para sim ou n para não e pressione Enter.
        Deseja ouvir a descrição do ambiente em áudio? (s/n): Se quiser ouvir a descrição do ambiente falada, digite s. Se preferir apenas ler, digite n e pressione Enter.
    ✨ Veja a Mágica Acontecer ✨: O script processará a imagem, mostrará a descrição do ambiente na tela e, se você escolheu, pesquisará os elementos e/ou reproduzirá a descrição em áudio.

Exemplo de Uso

Ao executar o script e fornecer o caminho para uma imagem de uma praça movimentada, a saída no terminal pode ser semelhante a:

Digite o caminho do arquivo da imagem ou a URL da imagem: caminho/para/sua/imagem.jpg

Elementos Identificados:

- Pessoas: ['feliz 😊', 'neutro 😐', 'sorrindo 😄']
- Estabelecimentos: ['Café Central ☕']
- Pontos Turísticos: ['Monumento Histórico 🏛️']
- Marcas: ['Coca-Cola 🥤']
- Tipo De Local: praça pública 🌳

Descrição do Ambiente para Locomoção e Obstáculos:

O ambiente parece ser uma praça aberta de tamanho considerável. Há caminhos pavimentados 🚶 que parecem ser os principais espaços de circulação. À sua frente, você pode notar alguns bancos de praça fixos 🛋️. À direita, parece haver um pequeno degrau 🪜 de acesso a uma área com grama 🌿. Mais adiante, à esquerda, identifica-se o que parece ser a fachada de um estabelecimento chamado Café Central ☕, com uma porta de entrada visível 🚪. Não há corrimãos aparentes nos caminhos. O piso parece ser feito de pedras irregulares em algumas áreas e liso em outras. Ao fundo, avista-se um monumento histórico 🏛️ com uma base elevada, possivelmente com alguns degraus de acesso. É possível ouvir o murmúrio de vozes 🗣️ e o som distante de carros 🚗.

Gerando áudio da descrição para locomoção...
Áudio da descrição para locomoção gerado! 🔊

Buscando informações sobre: Café Central... 🔎
Buscando informações sobre: Monumento Histórico... 🔎
Buscando informações sobre: Coca-Cola... 🔎

Resultados da Pesquisa:

- Estabelecimentos:
  - Café Central ☕:
    1. O Café Central é uma cafeteria tradicional localizada no coração da cidade, conhecida por seus cafés especiais e bolos caseiros...
    Gerando áudio dos resultados para Café Central... 🔊
    Áudio dos resultados para Café Central gerado!
- Pontos Turísticos:
  - Monumento Histórico 🏛️:
    1. O Monumento Histórico foi erguido em homenagem aos heróis da revolução e é um importante símbolo da cidade...
    Gerando áudio dos resultados para Monumento Histórico... 🔊
    Áudio dos resultados para Monumento Histórico gerado!
- Marcas:
  - Coca-Cola 🥤:
    1. Coca-Cola é uma marca global de bebidas carbonatadas, conhecida por seu sabor único e campanhas publicitárias icônicas...
    Gerando áudio dos resultados para Coca-Cola... 🔊
    Áudio dos resultados para Coca-Cola gerado!

Processamento da imagem concluído. ✅

Dicas Importantes:

    📂 Caminhos de Arquivo: Se o arquivo da imagem estiver na mesma pasta do script, você pode digitar apenas o nome do arquivo (exemplo: minha_foto.jpg). Caso contrário, use o caminho completo.
    🌐 URLs: Certifique-se de que a URL da imagem esteja correta e acessível pela internet.
    🎧 Áudio: Para ouvir o áudio, seu computador precisa ter um dispositivo de saída de som funcionando.
    ⚠️ Erros: Se ocorrer algum erro no terminal, leia a mensagem com atenção. Ela pode indicar o problema. Se precisar de ajuda para entender o erro, pode me mostrar a mensagem aqui!

Pronto! Com esses passos e os emojis para facilitar a leitura, você está pronto para usar o NavegaIA e explorar o mundo através da análise de imagens com foco em acessibilidade! 😉 Se tiver mais alguma dúvida, é só perguntar! 😊


O Gemini pode cometer erros. Por isso, é bom checar as respostas
