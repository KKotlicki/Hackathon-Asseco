from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

class Transaction(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        money = json_data['money']
        print('hey')
        return jsonify(money)

api.add_resource(Transaction, '/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444 ,debug=True)
