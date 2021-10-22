from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class Transaction(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        money = json_data['money']

        return jsonify(money)

api.add_resource(Transaction, '/transaction')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444 ,debug=True)