# Ling-Park
Trabalho final da disciplina Linguagens de Programação - UFRJ EEL670
### Pre-requisitos

Python3

virtualenv

### Instalação 

Crie um ambiente virtual e instale as dependências do Python
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
Inicialize o banco de dados 
```
$ python3 run.py db init
$ python3 run.py db migrate
```
Para iniciar o servidor Flask
```
$ python3 run.py runserver 
```

### Configuração

veja o arquivo config.py para as configurações minimas do ambiente de desenvolvimento tais como modo de Debug e a chave para a API do banco de dados.

### Autores

[Pedro Henrique Teles](https://github.com/pedrohfteles)

[Vitor Pavani](https://github.com/PavaniVitor)

[Yuri Reis](https://github.com/yrs03)
