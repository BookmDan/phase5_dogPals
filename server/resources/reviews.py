from flask import jsonify, request
from flask_restful import Resource
from config import db
from models.models import Review, ReviewSchema  

review_schema = ReviewSchema()

class ReviewsResource(Resource):
  def get(self):
    reviews = Review.query.all()
    result = review_schema.dump(reviews, many=True)
    return jsonify(result), 200

  def post(self):
    data = request.get_json()
    new_review = Review(**data)
    db.session.add(new_review)
    db.session.commit()
    return review_schema.jsonify(new_review), 201

class ReviewById(Resource):
  def get(self, id):
    review = Review.query.get(id)
    if review:
      return review_schema.jsonify(review), 200
    return jsonify({"message": f"Review with ID {id} not found"}), 404

  def patch(self, id):
    review = Review.query.get(id)
    if review:
      data = request.get_json()
      for key, value in data.items():
        setattr(review, key, value)
      db.session.commit()
      return review_schema.jsonify(review), 200
    return jsonify({"message": f"Review with ID {id} not found"}), 404

  def delete(self, id):
    review = Review.query.get(id)
    if review:
      db.session.delete(review)
      db.session.commit()
      return jsonify({"message": f"Review with ID {id} deleted successfully"}), 200
    return jsonify({"message": f"Review with ID {id} not found"}), 404

