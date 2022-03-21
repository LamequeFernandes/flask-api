from flask_restful import Resource, reqparse  #reqparse recebe os elementos da requisição
from models.receita import ReceitaModel

class Receitas(Resource):  # extende resource pq é um recurso da api, TODO recurso possui as funções get, post, put e delete pre-definidas
    def get(self):
        return {'receitas': [receita.json() for receita in ReceitaModel.query.all()]}  # SELECT * 

class Receita(Resource):
    argumentos = reqparse.RequestParser()
    # so pega os argumentos abaixo
    argumentos.add_argument('descricao')
    argumentos.add_argument('valor')
    argumentos.add_argument('data')

    def post(self, id):
        if ReceitaModel.existe_receita(id):
            return {"message": "Receita id '{}' already exist".format(id)}, 400  # bad request
    
        dados = Receita.argumentos.parse_args()  # chave a valor de todos os argumentos passados
        receita = ReceitaModel(id, **dados)
        receita.salva_receita()
        return receita.json(), 200