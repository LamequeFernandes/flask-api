from flask import Flask  # importação do flask
from flask_restful import Api  # biblioteca que vai auxiliar na criacao da API
from resources.receita import Receitas
app = Flask(__name__)  # instancia o Flask, basicamente é a aplicaçao
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  #define o caminho e o nome do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # evitar msg de erro
api = Api(app)  # instancia API

api.add_resource(Receitas, '/receitas')

@app.before_first_request
def cria_banco():
    banco.create_all()  # cria automaticamente o banco e todas as tabelas

if __name__ == '__main__':  # vai rodar se chamar esse arquivo direto no terminal
    from sql_alchemy import banco  # adicionado aqui pra não chama varias vezes
    banco.init_app(app)
    app.run(debug=True)