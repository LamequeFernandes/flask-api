from email.policy import default
from sql_alchemy import banco
from datetime import date

class DespesaModel(banco.Model):
    __tablename__ = 'despesas'

    id = banco.Column(banco.Integer, primary_key=True)
    descricao = banco.Column(banco.String(2000))
    valor = banco.Column(banco.Float(precision=2))
    data = banco.Column(banco.Date)
    print(data)

    def __init__(self, id, descricao, valor, data):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.data = data

    def json(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'valor': self.valor,
            'data': self.data
        }

    @classmethod
    def existe_despesa(cls, id):
        despesa = cls.query.filter_by(id=id).first()
        if despesa:
            return despesa
        return None

    def salva_despesa(self):
        banco.session.add(self)
        #print('cade vc caraio', date.today())
        banco.session.commit()
