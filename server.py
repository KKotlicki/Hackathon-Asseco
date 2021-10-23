from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

class Person:
  def __init__(self, sex, maritalStatus,education,category,debitAmount,monthOfOperation, age, accountAge, correctenss ):
    self.sex = sex
    self.maritalStatus = maritalStatus
    self.education = education
    self.category = category
    self.debitAmount = debitAmount
    self.monthOfOperation = monthOfOperation
    self.age = age
    self.accountAge = accountAge
    self.correctenss = correctenss
  def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Transaction(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        money = json_data['money']
        print('hey')
        return jsonify(money)

    def get(self):
        print('hey')
        p1 = Person("woman", "wife", "math", "TV", "1000", "October", 23, 2, 0.3)

        return p1.toJSON()

api.add_resource(Transaction, '/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444 ,debug=True)

