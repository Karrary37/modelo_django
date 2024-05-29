# Django Modelo 
Repositório padrão para criação de projetos Django.

### Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
<br>
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
<br>
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
# Contém os seguintes módulos
* Auth
* Core

# Docker de desenvolvimento
Para manter o Docker do projeto original inalterado, foi criado o arquivo docker-compose-dev.yml, ele utiliza variaveis de ambiente descritas no arquivo .env


#### Como usar o docker de desenvolvimento

- execute o comando para iniciar o sistema
<br/>```docker compose -f docker-compose-dev.yml up -d```