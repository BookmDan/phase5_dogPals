from config import app
from http.client import NOT_FOUND
from flask import jsonify, request, make_response, render_template
from resources.routes import *
from models.models import *

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
  return render_template('index.html')

api.add_resource(CheckSession, '/api/check-session')
api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')
api.add_resource(Signup, '/api/signup')



if __name__ == "__main__":
  app.run(port=5555, debug=True)
