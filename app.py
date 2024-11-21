from flask import Flask

# Criando a instância da aplicação Flask
app = Flask(__name__)

# Definindo a rota para o endereço raiz "/"
@app.route('/')
def hello_world():
    return 'Olá Mundo!'

# Rodando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
