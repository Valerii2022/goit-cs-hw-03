import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
def connect_to_db():
    try:
        # client = MongoClient("mongodb+srv://vmpometun:91mifmx9qkClQKvC@cs.3g2qf.mongodb.net/?retryWrites=true&w=majority&appName=CS") # MongoDB Atlas
        client = MongoClient("mongodb://localhost:27017/") # Docker
        db = client['cat_database']  # Назва бази даних
        return db['cats']  # Назва колекції
    except Exception as e:
        print(f"Не вдалося підключитися до бази даних: {e}")
        return None

# CRUD Операції

# Додати котика
def create_cat(collection, name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"Котик доданий з ID: {result.inserted_id}")
    except Exception as e:
        print(f"Помилка створення запису: {e}")

# Отримати всіх котиків
def read_all_cats(collection):
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Помилка читання даних: {e}")

# Знайти котика за ім'ям
def read_cat_by_name(collection, name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Котик із таким ім'ям не знайдений.")
    except Exception as e:
        print(f"Помилка читання даних: {e}")

# Оновити вік котика
def update_cat_age(collection, name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count:
            print(f"Вік котика {name} оновлено до {new_age}.")
        else:
            print("Котик із таким ім'ям не знайдений.")
    except Exception as e:
        print(f"Помилка оновлення даних: {e}")

# Додати характеристику котику
def add_feature_to_cat(collection, name, feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": feature}})
        if result.matched_count:
            print(f"Додано нову характеристику до котика {name}: {feature}.")
        else:
            print("Котик із таким ім'ям не знайдений.")
    except Exception as e:
        print(f"Помилка оновлення даних: {e}")

# Видалити котика за ім'ям
def delete_cat_by_name(collection, name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"Котик {name} видалений.")
        else:
            print("Котик із таким ім'ям не знайдений.")
    except Exception as e:
        print(f"Помилка видалення даних: {e}")

# Видалити всіх котиків
def delete_all_cats(collection):
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
    except Exception as e:
        print(f"Помилка видалення даних: {e}")

# Головна функція
if __name__ == "__main__":
    collection = connect_to_db()
    if collection is not None:
        while True:
            print("\nВиберіть операцію:")
            print("1. Додати котика")
            print("2. Вивести всіх котиків")
            print("3. Знайти котика за ім'ям")
            print("4. Оновити вік котика")
            print("5. Додати характеристику котику")
            print("6. Видалити котика за ім'ям")
            print("7. Видалити всіх котиків")
            print("8. Вийти")
            
            choice = input("Ваш вибір: ")
            if choice == '1':
                name = input("Введіть ім'я котика: ")
                age = int(input("Введіть вік котика: "))
                features = input("Введіть характеристики (через кому): ").split(", ")
                create_cat(collection, name, age, features)
            elif choice == '2':
                read_all_cats(collection)
            elif choice == '3':
                name = input("Введіть ім'я котика: ")
                read_cat_by_name(collection, name)
            elif choice == '4':
                name = input("Введіть ім'я котика: ")
                new_age = int(input("Введіть новий вік котика: "))
                update_cat_age(collection, name, new_age)
            elif choice == '5':
                name = input("Введіть ім'я котика: ")
                feature = input("Введіть нову характеристику: ")
                add_feature_to_cat(collection, name, feature)
            elif choice == '6':
                name = input("Введіть ім'я котика: ")
                delete_cat_by_name(collection, name)
            elif choice == '7':
                delete_all_cats(collection)
            elif choice == '8':
                print("До побачення!")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")
