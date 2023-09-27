# Hospital ABC 

# API Completa

Este pequeno projeto faz parte do material extra da Disciplina **Desenvolvimento Back End Avançado e Arquitetura de Software** 

---
## Como executar em modo de desenvolvimento

Basta fazer o download do projeto todo e executar docker-compose.yaml.

## Como executar através do Docker-compose

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o docker-compose, no terminal Execute **como administrador** o seguinte comando para construir a imagem:

```
$ docker-compose -f docker-compose.yaml up -d --build

```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ python3 backend/main.py
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:8000/#/](http://localhost:8000/#/) no navegador.
