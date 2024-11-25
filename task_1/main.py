import psycopg2

# Налаштування підключення
connection = psycopg2.connect(
    dbname="task_management",
    user="postgres",
    password="qwe123QWE",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

# SQL для створення таблиць
table_creation_queries = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
    );
    """
]

# Виконання запитів для створення таблиць
for query in table_creation_queries:
    try:
        cursor.execute(query)
        print(f"Таблиця створена успішно:\n{query}")
    except Exception as e:
        print(f"Помилка при створенні таблиці:\n{e}")

# Завершення роботи
connection.commit()
cursor.close()
connection.close()
