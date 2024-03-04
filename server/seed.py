from config import app, db
from models.models import User, Dog, Review, Sitter, Transaction

if __name__ == "__main__":
  with app.app_context():
    db.session.query(User).delete()
    db.session.query(Dog).delete()
    db.session.query(Review).delete()
    db.session.query(Sitter).delete()
    db.session.query(Transaction).delete()

    user1 = User(name="John", email="john@example.com")
    user1.password_hash = "password123"
    user2 = User(name="Jane",  email="jane@example.com")
    user2.password_hash = "password456"

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Create dogs
    dog1 = Dog(owner_id=user1.id, name="Buddy", breed="Labrador", age=3)
    dog2 = Dog(owner_id=user2.id, name="Max", breed="Golden Retriever", age=2)

    db.session.add(dog1)
    db.session.add(dog2)
    db.session.commit()

    # Create reviews
    review1 = Review(sitter_id=1, user_id=user1.id, rating=5, comment="Great service!")
    review2 = Review(sitter_id=2, user_id=user2.id, rating=4, comment="Very satisfied")

    db.session.add(review1)
    db.session.add(review2)
    db.session.commit()

    # Create sitters
    sitter1 = Sitter(user_id=user1.id, bio="Experienced dog sitter", availability="Weekdays")
    sitter2 = Sitter(user_id=user2.id, bio="Certified pet trainer", availability="Weekends")

    db.session.add(sitter1)
    db.session.add(sitter2)
    db.session.commit()

    # Create transactions
    transaction1 = Transaction(user_id=user1.id, sitter_id=1, amount=50.00, status="Completed")
    transaction2 = Transaction(user_id=user2.id, sitter_id=2, amount=60.00, status="Completed")

    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.commit()

    print("Database seeded successfully!")
