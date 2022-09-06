Isso é um chatbot que foi desenvolvido juntamente com drsantos20, onde eles nos direcionou durante um workshop ministrado por ele e organizado pela EBAC - Escola Britânica de artes criativas e tecnologia.
Esse workshop foi para nos ensinar o funcionamento basico de um chatbot simples e daí nos aprofundar mais posteriormente.
Exstem alguns requisitos para rodar esse chatbot:

*EM AMBIENTE WINDOWS*
- Instalar o git
- Instalar o python
- Instalar o vscode

Após instalar o python devemos criar um ambiente virtual 

# Abra o powershell e navegue até algum lugar, pode ser qualquer diretorio
- mkdir workshop_chatbot
- cd chatbot
- python3 -m venv env
- env\Scripts\activate.bat
- pip install Flask
- pip install chatterbot
- pip install SQLAlchemy
- pip install pytz
- pip install pytest

*NÃO FECHAR JANELA DO POWERSHELL*

# Abra o CLI do git e por comando vá até o diretorio que você está no powershell
- git clone https://github.com/feignbird/ChatterBot-spacy_fixed.git

# Volte para o powershell e digite conforme abaixo
- install ./ChatterBot-spacy_fixed
- install chatterbot-corpus
- pip uninstall pyYAML
- pip install pyYAML==5.3.1
- python -m spacy download en_core_web_sm

# Agora você pode ir pelo windows explorer até o diretorio atual e excluir a pasta ChatterBot-spacy_fixed
Isso apenas foi para corrigir um erro por causa da instalação do spacy durante a instalação do Flask.

# Agora abra o vscode e abra o diretorio que criou
Deixe a aba do github aberta:

![image](https://user-images.githubusercontent.com/11152265/188598100-d2028600-523e-4ec7-bc0b-e3968a588cdc.png)

# Após isso faça como abaixo:
- Crie o arquivo hello.py e insira as informações que contém no arquivo correspondente aqui nesse repositorio do github.
- Crie a pasta static, dentro dela crie as pastas css e img
- Dentro da pasta css crio o arquivo style.css e copiei o que está aqui no github
- Dentro da pasta img insira a imagem que está aqi no github, conforme estrutura
- Crie a pasta templates a nivel da pasta static
- Crie o arquivo index.html e coloque as informações que há nesse arquivo aqui no github
- Crie a pasta test e dentro dela crie os arquivos __init__.py e test_hello.py e coloque as informações dos arquivos correspondetes que tem aqui no github

No final ficará dessa forma sua estrutura do vscode, ( no caso eu coloquei o nome do meu arquivo de workshop_chatbot

![image](https://user-images.githubusercontent.com/11152265/188599429-84eae5bb-d664-4d14-bfa4-bc2df40f5d64.png)


# Após isso vá ate seu powershell e digite
- python hello.py

Sua saída será aparente com essa abaixo:

![image](https://user-images.githubusercontent.com/11152265/188599929-939185fd-b609-4e00-b52d-e09ddbfae7cf.png)


Pegue o endereço que está mostrando que no caso é: http://127.0.0.1:5000  e seu chatbot deverá abrir.

Ai é só digitar as mensagem como foram criadas no treinamento e está no arquivo hello.py 

![image](https://user-images.githubusercontent.com/11152265/188600317-2183690d-d674-4e6c-95c7-2553b3762b06.png)


E após conversar om seu chatbot ele ficará quase assim:

![image](https://user-images.githubusercontent.com/11152265/188600498-2721f51b-1bdd-4600-b33c-82d06ba9d9b8.png)

Eu digo isso, pois no meu caso eu já havia informado algumas coisas na mensagem para ele e ele guardou no banco.









