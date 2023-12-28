import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import User, Review, Recipe
from methods import BaseMethod, UserMethod, ReviewMethod, RecipeMethod
from base import Base

class TestBaseMethod(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)
        self.base_method = BaseMethod(session=self.session)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

    def test_create(self):
        # Test create method
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = self.base_method.create(User, **user_data)
        self.assertIsNotNone(user.id)

    def test_get(self):
        # Test get method
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = self.base_method.create(User, **user_data)
        retrieved_user = self.base_method.get(User, user.id)
        self.assertEqual(retrieved_user.username, 'test_user')

    def test_get_all(self):
        # Test get_all method
        user_data_1 = {'username': 'test_user1', 'email': 'test1@example.com', 'password': 'test_password1'}
        user_data_2 = {'username': 'test_user2', 'email': 'test2@example.com', 'password': 'test_password2'}
        self.base_method.create(User, **user_data_1)
        self.base_method.create(User, **user_data_2)

        all_users = self.base_method.get_all(User)
        self.assertEqual(len(all_users), 2)

    def test_update(self):
        # Test update method
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = self.base_method.create(User, **user_data)

        updated_user = self.base_method.update(user, username='updated_user')
        self.assertEqual(updated_user.username, 'updated_user')

    def test_delete(self):
        # Test delete method
        user_data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'test_password'}
        user = self.base_method.create(User, **user_data)

        self.base_method.delete(user)
        deleted_user = self.base_method.get(User, user.id)
        self.assertIsNone(deleted_user)

class TestUserMethod(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)
        self.user_method = UserMethod(session=self.session)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

    def test_create_user(self):
        # Test create_user method
        user = self.user_method.create_user(username='test_user', email='test@example.com', password='test_password')
        self.assertIsNotNone(user.id)

    def test_get_user(self):
        # Test get_user method
        user = self.user_method.create_user(username='test_user', email='test@example.com', password='test_password')
        retrieved_user = self.user_method.get_user(user.id)
        self.assertEqual(retrieved_user.username, 'test_user')

    def test_get_all_users(self):
        # Test get_all_users method
        user_data_1 = {'username': 'test_user1', 'email': 'test1@example.com', 'password': 'test_password1'}
        user_data_2 = {'username': 'test_user2', 'email': 'test2@example.com', 'password': 'test_password2'}
        self.user_method.create_user(**user_data_1)
        self.user_method.create_user(**user_data_2)

        all_users = self.user_method.get_all_users()
        self.assertEqual(len(all_users), 2)

    def test_update_user(self):
        # Test update_user method
        user = self.user_method.create_user(username='test_user', email='test@example.com', password='test_password')

        updated_user = self.user_method.update_user(user.id, username='updated_user')
        self.assertEqual(updated_user.username, 'updated_user')

    def test_delete_user(self):
        # Test delete_user method
        user = self.user_method.create_user(username='test_user', email='test@example.com', password='test_password')

        self.user_method.delete_user(user.id)
        deleted_user = self.user_method.get_user(user.id)
        self.assertIsNone(deleted_user)

class TestReviewMethod(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)
        self.review_method = ReviewMethod(session=self.session)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

    def test_create_review(self):
        # Test create_review method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        review = self.review_method.create_review(text='Test review text', user_id=user.id)
        self.assertIsNotNone(review.id)

    def test_get_review(self):
        # Test get_review method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        review = self.review_method.create_review(text='Test review text', user_id=user.id)
        retrieved_review = self.review_method.get_review(review.id)
        self.assertEqual(retrieved_review.text, 'Test review text')

    def test_get_all_reviews(self):
        # Test get_all_reviews method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        review_data_1 = {'text': 'Review 1', 'user_id': user.id}
        review_data_2 = {'text': 'Review 2', 'user_id': user.id}
        self.review_method.create_review(**review_data_1)
        self.review_method.create_review(**review_data_2)

        all_reviews = self.review_method.get_all_reviews()
        self.assertEqual(len(all_reviews), 2)

    def test_update_review(self):
        # Test update_review method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        review = self.review_method.create_review(text='Test review text', user_id=user.id)

        updated_review = self.review_method.update_review(review.id, text='Updated review text')
        self.assertEqual(updated_review.text, 'Updated review text')

    def test_delete_review(self):
        # Test delete_review method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        review = self.review_method.create_review(text='Test review text', user_id=user.id)

        self.review_method.delete_review(review.id)
        deleted_review = self.review_method.get_review(review.id)
        self.assertIsNone(deleted_review)

class TestRecipeMethod(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)
        self.recipe_method = RecipeMethod(session=self.session)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
        self.session.close()

    def test_create_recipe(self):
        # Test create_recipe method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        recipe = self.recipe_method.create_recipe(title='Test Recipe', content='Recipe content', author_id=user.id)
        self.assertIsNotNone(recipe.id)

    def test_get_recipe(self):
        # Test get_recipe method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        recipe = self.recipe_method.create_recipe(title='Test Recipe', content='Recipe content', author_id=user.id)
        retrieved_recipe = self.recipe_method.get_recipe(recipe.id)
        self.assertEqual(retrieved_recipe.title, 'Test Recipe')

    def test_get_all_recipes(self):
        # Test get_all_recipes method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        recipe_data_1 = {'title': 'Recipe 1', 'content': 'Content 1', 'author_id': user.id}
        recipe_data_2 = {'title': 'Recipe 2', 'content': 'Content 2', 'author_id': user.id}
        self.recipe_method.create_recipe(**recipe_data_1)
        self.recipe_method.create_recipe(**recipe_data_2)

        all_recipes = self.recipe_method.get_all_recipes()
        self.assertEqual(len(all_recipes), 2)

    def test_update_recipe(self):
        # Test update_recipe method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        recipe = self.recipe_method.create_recipe(title='Test Recipe', content='Recipe content', author_id=user.id)

        updated_recipe = self.recipe_method.update_recipe(recipe.id, title='Updated Recipe')
        self.assertEqual(updated_recipe.title, 'Updated Recipe')

    def test_delete_recipe(self):
        # Test delete_recipe method
        user = User(username='test_user', email='test@example.com', password='test_password')
        self.session.add(user)
        self.session.commit()

        recipe = self.recipe_method.create_recipe(title='Test Recipe', content='Recipe content', author_id=user.id)

        self.recipe_method.delete_recipe(recipe.id)
        deleted_recipe = self.recipe_method.get_recipe(recipe.id)
        self.assertIsNone(deleted_recipe)

    if __name__ == '__main__':
        unittest.main()
