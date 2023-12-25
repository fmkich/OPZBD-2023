import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from base import Base
from models import Recipe,User

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

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
        self.assertEqual(retrieved_recipe.title, 'Test Recipe')
        self.assertEqual(retrieved_recipe.content, 'Recipe content')
        self.assertEqual(retrieved_recipe.author_id, 1)

    def test_recipe_relationship_with_author(self):
        # Test the relationship between Recipe and User
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()

        recipe_data = {'title': 'Test Recipe', 'content': 'Recipe content', 'author_id': user.id}
        recipe = Recipe(**recipe_data)

        self.session.add(recipe)
        self.session.commit()

        # Retrieve the user with recipes and assert the relationship
        retrieved_user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(len(retrieved_user.recipes), 1)
        self.assertEqual(retrieved_user.recipes[0].title, 'Test Recipe')

    if __name__ == '__main__':
        unittest.main()


