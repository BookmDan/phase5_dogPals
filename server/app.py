from config import app
from http.client import NOT_FOUND
from flask import jsonify, request, make_response, render_template
from resources.routes import *
from models.models import *

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
  return render_template('index.html')

if __name__ == "__main__":
  app.run(port=5555, debug=True)
