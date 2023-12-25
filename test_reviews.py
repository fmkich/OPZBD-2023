import unittest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from base import Base
from models import Review, User

class TestReview(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

    def test_review_creation(self):
        # Test review creation and save to the database
        review_data = {'text': 'Test review text', 'user_id': 1}
        review = Review(**review_data)

        # Add review to the session and commit to the database
        self.session.add(review)
        self.session.commit()

        # Retrieve the review from the database and assert values
        retrieved_review = self.session.query(Review).filter_by(text='Test review text').first()
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.text, 'Test review text')
        self.assertEqual(retrieved_review.user_id, 1)

    def test_review_relationship_with_user(self):
        # Test the relationship between Review and User
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()

        review_data = {'text': 'Test review text', 'user_id': user.id}
        review = Review(**review_data)

        self.session.add(review)
        self.session.commit()

        # Retrieve the user with reviews and assert the relationship
        retrieved_user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(len(retrieved_user.reviews), 1)
        self.assertEqual(retrieved_user.reviews[0].text, 'Test review text')

    if __name__ == '__main__':
        unittest.main()
