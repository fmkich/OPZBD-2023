import unittest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from database import Base
from models import User, Review, Recipe

class TestModels(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)

    def tearDown(self):
        # Drop all tables and close the session
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

    def test_user_creation(self):
        # Test user creation and save to the database
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = User(**user_data)

        # Add user to the session and commit to the database
        self.session.add(user)
        self.session.commit()

        # Retrieve the user from the database and assert values
        retrieved_user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'test@example.com')
        self.assertEqual(retrieved_user.password, 'test_password')

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
        self.assertEqual(retrieved_review.user_id, 1)

    def test_recipe_creation(self):
        # Test recipe creation and save to the database
        recipe_data = {'title': 'Test Recipe', 'content': 'Recipe content', 'author_id': 1}
        recipe = Recipe(**recipe_data)

        # Add recipe to the session and commit to the database
        self.session.add(recipe)
        self.session.commit()

        # Retrieve the recipe from the database and assert values
        retrieved_recipe = self.session.query(Recipe).filter_by(title='Test Recipe').first()
        self.assertIsNotNone(retrieved_recipe)
        self.assertEqual(retrieved_recipe.content, 'Recipe content')
        self.assertEqual(retrieved_recipe.author_id, 1)

    if __name__ == '__main__':
        unittest.main()

