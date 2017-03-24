# Rest-Crawler Auto Esporte

Um servidor Flask que disponibiliza uma API Rest para consumir as informações extraídas do feed de notícias da revista Auto Esporte.

## Ambiente

- Linux Mint Rebecca 32 bits.
- Python 2.7.6

## Instalação

- Tenha os seguintes pacotes instalados no sistema:
```
crontab python-dev libxml2-dev libxslt1-dev zlib1g-dev ssl
```

- Crie de um usuário Linux sem acesso root exclusivo para esta aplicação.

- Recomenda-se a criação de um virtualenv para preservar o python do sistema.

- Instale os seguintes pacotes python:
```
lxml flask flask-sqlalchemy sqlalchemy-migrate flask-wtf werkzeug 
```

- Clone este repositório e abra o terminal na pasta raiz do repositório.

- Para iniciar o server rode o comando:
```
python main.py
```

- Acesse a pasta 'page_crawler' e rode o seguinte comando, para dar autorização de execução para o crontab:
```
chmod 733 update_crawler.py
```

- Abra o agendador de rotinas com o comando ```crontab -e``` e insira a seguinte linha:
```
*/5 * * * * [user] source [caminho do venv]/bin/activate && python [caminho do repositorio]/page_crawler/update_crawler.py && deactivate
```

- Caso tenha dispensado vitualenv e a criação de um usuário específico a linha a ser inserida no crontab é a que segue:
```
*/5 * * * * python [caminho do repositorio]/page_crawler/update_crawler.py
```

## Utilização

- Acesse localhost:5000 no navegador.

- Cadastre-se.

- Faça a requisição com o método POST com {"nickname":"seu nickname", "password":"sua senha"}

As urls para requisição são:
```
localhost:5000/restapi/fromfile
localhost:5000/restapi/fromsite
```

A primeira consulta os dados locais, que contem a informação pronta. A informação local é atualizada a cada 5 minutos pela rotina inserida no crontab.
Já a segunda busca no site do feed, processa a informação e a retorna.

A requisição pela primeira acaba sendo mais rápida, por não precisar crawlear o site do Auto Esporte durante a execução de cada requisição.
