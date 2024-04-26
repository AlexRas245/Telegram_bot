import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('game_results.db')
cursor = conn.cursor()

# Создание таблицы для хранения результатов игр
cursor.execute('''CREATE TABLE IF NOT EXISTS game_results (
                    id INTEGER PRIMARY KEY,
                    game_name TEXT,
                    winner TEXT,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                  )''')
conn.commit()


# Функция для записи результатов игры в базу данных
def record_game_result(game_name, winner):
    cursor.execute('''INSERT INTO game_results (game_name, winner) VALUES (?, ?)''', (game_name, winner))
    conn.commit()
