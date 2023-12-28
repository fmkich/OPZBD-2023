import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from base import Base
from models import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        self.session = Session(bind=self.engine)

    def tearDown(self):
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
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.email, 'test@example.com')
        self.assertEqual(retrieved_user.password, 'test_password')

    if __name__ == '__main__':
        unittest.main()

