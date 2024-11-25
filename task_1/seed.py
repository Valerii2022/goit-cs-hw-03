import psycopg2
from faker import Faker

# Налаштування підключення
connection = psycopg2.connect(
    dbname="task_management",
    user="postgres",
    password="qwe123QWE",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

# Ініціалізація Faker
fake = Faker()

# Додавання статусів
statuses = ['new', 'in progress', 'completed']
cursor.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING", [(status,) for status in statuses])

# Додавання користувачів
users = [(fake.name(), fake.unique.email()) for _ in range(100)]
cursor.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s)", users)

# Отримання ID статусів та користувачів
cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

# Додавання завдань
tasks = [
    (
        fake.sentence(nb_words=4),
        fake.paragraph(nb_sentences=2),
        fake.random.choice(status_ids),
        fake.random.choice(user_ids),
    )
    for _ in range(300)
]
cursor.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

# Завершення транзакції
connection.commit()
cursor.close()
connection.close()



