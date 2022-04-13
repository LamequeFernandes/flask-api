from sql_alchemy import banco

class ReceitaModel(banco.Model):
    __tablename__ = 'receitas'

    id = banco.Column(banco.Integer, primary_key=True)
    descricao = banco.Column(banco.String(2000))
    valor = banco.Column(banco.Float(precision=2))
    data = banco.Column(banco.String(11))

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
    def existe_receita(cls, id):
        receita = cls.query.filter_by(id=id).first()
        if receita:
            return receita
        return None

    def salva_receita(self):
        banco.session.add(self)
        banco.session.commit()
        
    def update_receita(self, descricao, valor, data):
        self.descricao = descricao
        self.valor = valor
        self.data = data