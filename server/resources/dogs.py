from flask import jsonify, request
from flask_restful import Resource
from config import db 
from models.models import Dog, DogSchema  

dog_schema = DogSchema()

class DogsResource(Resource):
    def get(self):
        dogs = Dog.query.all()
        result = dog_schema.dump(dogs, many=True)
        return jsonify(result), 200

    def post(self):
        data = request.get_json()
        new_dog = Dog(**data)
        db.session.add(new_dog)
        db.session.commit()
        return dog_schema.jsonify(new_dog), 201

class DogById(Resource):
    def get(self, id):
        dog = Dog.query.get(id)
        if dog:
            return dog_schema.jsonify(dog), 200
        return jsonify({"message": f"Dog with ID {id} not found"}), 404

    def patch(self, id):
        dog = Dog.query.get(id)
        if dog:
            data = request.get_json()
            for key, value in data.items():
                setattr(dog, key, value)
            db.session.commit()
            return dog_schema.jsonify(dog), 200
        return jsonify({"message": f"Dog with ID {id} not found"}), 404

    def delete(self, id):
        dog = Dog.query.get(id)
        if dog:
            db.session.delete(dog)
            db.session.commit()
            return jsonify({"message": f"Dog with ID {id} deleted successfully"}), 200
        return jsonify({"message": f"Dog with ID {id} not found"}), 404

