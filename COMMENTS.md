## Guia para Executar a Simulação de Jogo

Este documento fornece instruções detalhadas para configurar, executar e testar a aplicação de simulação de jogo.

### Rodar a aplicação

### 1) Instale o python:

#### Linux
```
sudo apt install python3.10
```
#### Windows
- Baixe o instalador do Python a partir do site oficial (https://www.python.org/downloads) e siga as instruções.
- Durante a instalação, certifique-se de selecionar a opção "Add Python to PATH".

### 2) Instale pip (package manager):
#### Linux
```
sudo apt install python3-pip
```
#### Windows
- O pip já vem instalado junto com o Python. Verifique executando no terminal:
```
pip --version
```

### 3) Instale virtualenv, crie o ambiente virtual e ative:
#### Linux
```
sudo pip install virtualenv 
virtualenv venv
source venv/bin/activate
```
#### Windows
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

__OBS:__ A linha de comando do terminal precisa começar com `(venv)`

### 4) Instale todos os pacotes necessários:

```
pip install --no-cache-dir --upgrade -r requirements.txt
``` 
### 5) Inicialize a API:
```
uvicorn main:app --host 127.0.0.1 --port 8000
```
or

```
python main.py
```
### 6) Teste acessando o endpoint através da documentação Swagger no link http://127.0.0.1:8000/docs
