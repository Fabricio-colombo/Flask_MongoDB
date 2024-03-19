# Projeto Flask de Teste de Penetração com Força Bruta

## Descrição
Este projeto é uma aplicação web simples construída com o microframework Flask e destina-se a ser utilizada como um alvo de teste de penetração usando ataques de força bruta. O site inclui funcionalidades de login, registro de usuários e uma página de esquecimento de senha satírica.

## Tecnologias Utilizadas
- Flask (microframework para aplicações web em Python)
- MongoDB (para armazenamento de dados de usuários)
- Selenium (para automação de navegador e realização de ataques de força bruta)
- HTML/CSS (para estruturação e estilização de páginas da web)

## Pré-requisitos
- Python 3.6+
- MongoDB
- MongoDB Compass (para visualizar os dados no banco de dados)
- Navegador com driver correspondente para o Selenium

## Instalação
Para instalar as dependências do projeto, execute:

```shell
pip install -r requirements.txt
git clone <URL_DO_REPOSITORIO>

Navegue até a pasta do projeto e inicie o servidor Flask com:
python app.py

# Uso
Para usar a aplicação web:

Abra o navegador e visite http://127.0.0.1:5000.
Utilize as funções de registro e login como desejar.
Para realizar um teste de penetração com força bruta:

Execute o script main.py na pasta atkforce_selenium.
Acompanhe as tentativas de login sendo realizadas pelo script.
```
## Lembrete Final

Antes de começar a utilizar ou contribuir para este projeto, certifique-se de instalar todas as bibliotecas necessárias listadas no arquivo `requirements.txt`. Além disso, não esqueça de realizar as alterações necessárias no código para que ele funcione adequadamente em sua máquina local, como ajustar as configurações do banco de dados e os parâmetros do Selenium.

~~ Fabricio Colombo
