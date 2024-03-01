from flask import jsonify, request
from flask_restful import Resource
from config import api, db
from models import Transaction, TransactionSchema  

transaction_schema = TransactionSchema()

class TransactionsResource(Resource):
  def get(self):
    transactions = Transaction.query.all()
    result = transaction_schema.dump(transactions, many=True)
    return jsonify(result), 200

  def post(self):
    data = request.get_json()
    new_transaction = Transaction(**data)
    db.session.add(new_transaction)
    db.session.commit()
    return transaction_schema.jsonify(new_transaction), 201

class TransactionById(Resource):
  def get(self, id):
    transaction = Transaction.query.get(id)
    if transaction:
      return transaction_schema.jsonify(transaction), 200
    return jsonify({"message": f"Transaction with ID {id} not found"}), 404

  def patch(self, id):
    transaction = Transaction.query.get(id)
    if transaction:
      data = request.get_json()
      for key, value in data.items():
        setattr(transaction, key, value)
      db.session.commit()
      return transaction_schema.jsonify(transaction), 200
    return jsonify({"message": f"Transaction with ID {id} not found"}), 404

  def delete(self, id):
    transaction = Transaction.query.get(id)
    if transaction:
      db.session.delete(transaction)
      db.session.commit()
      return jsonify({"message": f"Transaction with ID {id} deleted successfully"}), 200
    return jsonify({"message": f"Transaction with ID {id} not found"}), 404

api.add_resource(TransactionsResource, '/api/transactions')
api.add_resource(TransactionById, '/api/transaction/<int:id>')
