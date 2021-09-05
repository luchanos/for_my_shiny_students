import psycopg2

DB_URL = 'postgresql://newuser:qwerty@127.0.0.1:5432/postgres'

conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

with cursor:
    cursor.execute("INSERT INTO notification_tasks (chat_id, message) "
                   "VALUES (362857450, 'не забудь сходить сегодня на тренировку!');")
    conn.commit()
