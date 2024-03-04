from config import app, api
from resources.routes import *
from models.models import *

api.add_resource(CheckSession, '/api/check-session')
api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')
api.add_resource(Signup, '/api/signup')
api.add_resource(DogsResource, '/api/dogs')
api.add_resource(DogById, '/api/dog/<int:id>')
api.add_resource(MessagesResource, '/api/messages')
api.add_resource(MessageById, '/api/message/<int:id>')
api.add_resource(ReviewsResource, '/api/reviews')
api.add_resource(ReviewById, '/api/review/<int:id>')
api.add_resource(SittersResource, '/api/sitters')
api.add_resource(SitterById, '/api/sitter/<int:id>')
api.add_resource(TransactionsResource, '/api/transactions')
api.add_resource(TransactionById, '/api/transaction/<int:id>')
api.add_resource(UsersResource, '/api/users')
api.add_resource(UserById, '/api/user/<int:id>')

if __name__ == "__main__":
  app.run(port=5555, debug=True)
