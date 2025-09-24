from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

accounts = {
    '1234-0': {'saldo': 1000.0}
}

class Conta(Resource):
    def get(self, account_id):
        if account_id in accounts:
            return accounts[account_id]
        else:
            return {'error': 'Conta não encontrada!'}, 404

class Deposito(Resource):
    def patch(self, account_id):
        if account_id not in accounts:
            return {'error': 'Conta não encontrada!'}, 404
        
        data = request.get_json()
        amount = data.get('quantidade', 0)
        accounts[account_id]['saldo'] += amount
        return accounts[account_id]

class Saque(Resource):
    def patch(self, account_id):
        if account_id not in accounts:
            return {'error': 'Conta não encontrada!'}, 404
        
        data = request.get_json()
        amount = data.get('amount', 0)
        if accounts[account_id]['saldo'] >= amount:
            accounts[account_id]['saldo'] -= amount
            return accounts[account_id]
        else:
            return {'error': 'Fundos insuficientes'}, 400

api.add_resource(Conta, '/conta/<string:account_id>')
api.add_resource(Deposito, '/conta/<string:account_id>/deposito')
api.add_resource(Saque, '/conta/<string:account_id>/saque')

if __name__ == '__main__':
    app.run(debug=True)

