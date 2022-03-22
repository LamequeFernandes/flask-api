from flask_restful import Resource, reqparse  #reqparse recebe os elementos da requisição
from models.despesa import DespesaModel

class Despesas(Resource):  # extende resource pq é um recurso da api, TODO recurso possui as funções get, post, put e delete pre-definidas
    def get(self):
        return {'despesas': [despesa.json() for despesa in DespesaModel.query.all()]}  # SELECT * 

class Despesa(Resource):
    argumentos = reqparse.RequestParser()
    # so pega os argumentos abaixo
    argumentos.add_argument('descricao')
    argumentos.add_argument('valor')
    argumentos.add_argument('data')

    def post(self, id):
        if DespesaModel.existe_despesa(id):
            return {"message": "Despesa id '{}' already exist".format(id)}, 400  # bad request
    
        dados = Despesa.argumentos.parse_args()  # chave a valor de todos os argumentos passados
        despesa = DespesaModel(id, **dados)
        despesa.salva_despesa()
        return despesa.json(), 200