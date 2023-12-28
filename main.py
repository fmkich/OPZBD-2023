from models import User, Review, Recipe
from database import engine, sessionmaker
from methods import UserMethod, ReviewMethod, RecipeMethod
from base import Base

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    session = SessionLocal()

    # Примеры использования методов
    user_method = UserMethod(session)
    review_method = ReviewMethod(session)
    recipe_method = RecipeMethod(session)

new_user = user_method.create_user(username="john", email="john@example.com", password="password123")
print("Created User:", new_user)

# Получение пользователя по ID
retrieved_user = user_method.get_user(user_id=new_user.id)
print("Retrieved User:", retrieved_user)

# Получение всех пользователей
all_users = user_method.get_all_users()
print("All Users:", all_users)

# Обновление пользователя
updated_user = user_method.update_user(user_id=new_user.id, email="new_email@example.com")
print("Updated User:", updated_user)

# Удаление пользователя
#user_method.delete_user(user_id=new_user.id)
#print("User deleted")

# Создание нового отзыва
new_review = review_method.create_review(text="Great product!", user_id=1)
print("Created Review:", new_review)

# Получение отзыва по ID
retrieved_review = review_method.get_review(review_id=new_review.id)
print("Retrieved Review:", retrieved_review)

# Получение всех отзывов
all_reviews = review_method.get_all_reviews()
print("All Reviews:", all_reviews)

# Обновление отзыва
updated_review = review_method.update_review(review_id=new_review.id, text="Updated review")
print("Updated Review:", updated_review)

# Удаление отзыва
#review_method.delete_review(review_id=new_review.id)
#print("Review deleted")

# Создание нового рецепта
new_recipe = recipe_method.create_recipe(title="Chocolate Cake", content="Best chocolate cake recipe!", author_id=1)
print("Created Recipe:", new_recipe)

# Получение рецепта по ID
retrieved_recipe = recipe_method.get_recipe(recipe_id=new_recipe.id)
print("Retrieved Recipe:", retrieved_recipe)

# Получение всех рецептов
all_recipes = recipe_method.get_all_recipes()
print("All Recipes:", all_recipes)

# Обновление рецепта
updated_recipe = recipe_method.update_recipe(recipe_id=new_recipe.id, title="Updated chocolate cake recipe")
print("Updated Recipe:", updated_recipe)

# Удаление рецепта
#recipe_method.delete_recipe(recipe_id=new_recipe.id)
#print("Recipe deleted")

# Закрытие сессии
session.close()
