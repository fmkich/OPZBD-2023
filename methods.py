from models import User, Review, Recipe
from database import engine, sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
class BaseMethod:
    def __init__(self, session):
        self.session = session

    def create(self, model, **kwargs):
        instance = model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get(self, model, id):
        return self.session.query(model).filter_by(id=id).first()

    def get_all(self, model):
        return self.session.query(model).all()

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()

class UserMethod(BaseMethod):
    def create_user(self, username: str, email: str, password: str):
        user = User(username=username, email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def get_user(self, user_id: int):
        return self.get(User, user_id)

    def get_user_by_username(self, username: str):
        return self.session.query(User).filter_by(username=username).first()


    def get_all_users(self):
        return self.get_all(User)

    def update_user(self, user_id: int, **kwargs):
        user = self.get_user(user_id)
        return self.update(user, **kwargs)

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        self.delete(user)

class ReviewMethod(BaseMethod):
    def create_review(self, text: str, user_id: int):
        return self.create(Review, text=text, user_id=user_id)

    def get_review(self, review_id):
        return self.get(Review, review_id)

    def get_all_reviews(self):
        return self.get_all(Review)

    def update_review(self, review_id, **kwargs):
        review = self.get_review(review_id)
        return self.update(review, **kwargs)

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        self.delete(review)

class RecipeMethod(BaseMethod):
    def create_recipe(self, title: str, content: str, author_id: int):
        return self.create(Recipe, title=title, content=content, author_id=author_id)

    def get_recipe(self, recipe_id):
        return self.get(Recipe, recipe_id)

    def get_all_recipes(self):
        return self.get_all(Recipe)

    def update_recipe(self, recipe_id, **kwargs):
        recipe = self.get_recipe(recipe_id)
        return self.update(recipe, **kwargs)

    def delete_recipe(self, recipe_id):
        recipe = self.get_recipe(recipe_id)
        self.delete(recipe)
