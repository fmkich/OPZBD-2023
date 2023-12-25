from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
db_url = 'postgresql://postgres:1@localhost:5432/postgres'

engine = create_engine(db_url)

def create_tables():
    Base.metadata.create_all(bind=engine)

def create_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
