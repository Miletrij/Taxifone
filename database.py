import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('taxi_bot.db')
    cursor = conn.cursor()

    # Таблица для водителей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        name TEXT,
        phone TEXT,
        car_model TEXT,
        car_color TEXT,
        car_number TEXT,
        status TEXT DEFAULT 'free',
        current_order_id INTEGER DEFAULT NULL
    )
    ''')

    # Таблица для клиентов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        name TEXT,
        phone TEXT,
        pickup_address TEXT,
        destination_address TEXT,
        driver_id INTEGER DEFAULT NULL,
        status TEXT DEFAULT 'pending'
    )
    ''')

    # Таблица для заказов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        driver_id INTEGER,
        pickup_address TEXT,
        destination_address TEXT,
        status TEXT DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES clients(id),
        FOREIGN KEY (driver_id) REFERENCES drivers(id)
    )
    ''')

    conn.commit()
    conn.close()

init_db()  # Инициализация при запуске
