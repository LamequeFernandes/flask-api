from flask import Flask  # importação do flask
from flask_restful import Api  # biblioteca que vai auxiliar na criacao da API
from resources.receita import Receitas, Receita
from resources.despesa import Despesa, Despesas
from flask_migrate import Migrate


app = Flask(__name__)  # instancia o Flask, basicamente é a aplicaçao
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  #define o caminho e o nome do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # evitar msg de erro
api = Api(app)  # instancia API
migrate = Migrate()

api.add_resource(Receitas, '/receitas')
api.add_resource(Receita, '/receitas/<string:id>')
api.add_resource(Despesas, '/despesas')
api.add_resource(Despesa, '/despesas/<string:id>')

@app.before_first_request
def cria_banco():
    banco.create_all()  # cria automaticamente o banco e todas as tabelas

if __name__ == '__main__':  # vai rodar se chamar esse arquivo direto no terminal
    from sql_alchemy import banco
    banco.init_app(app)
    migrate.init_app(app,banco)
    app.run(debug=True)
