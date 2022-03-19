from flask_restful import Resource, reqparse  #reqparse recebe os elementos da requisição
from models.receita import ReceitaModel

class Receitas(Resource):  # extende resource pq é um recurso da api, TODO recurso possui as funções get, post, put e delete pre-definidas
    def get(self):
        return {'receitas': [receita.json() for receita in ReceitaModel.query.all()]}  # SELECT * 

