import unittest
from sqlalchemy import create_engine, inspect
from database import create_tables, create_session
from sqlalchemy.orm import sessionmaker

class TestDatabase(unittest.TestCase):
    def test_db_connection(self):
        db_url = 'postgresql://postgres:1@localhost:5432/postgres'
        engine = create_engine(db_url)
        connection = engine.connect()
        self.assertIsNotNone(connection)
        connection.close()

    def test_create_session(self):
        db_url = 'postgresql://postgres:1@localhost:5432/postgres'

        engine = create_engine(db_url)

        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()

        self.assertIsNotNone(session)
        session.close()

    if __name__ == '__main__':
        unittest.main()
