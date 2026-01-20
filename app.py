from flask import Flask, request
import sqlite3
import random
import string
from datetime import datetime

app = Flask(__name__)

# Підключення до бази
def get_db_connection():
    conn = sqlite3.connect('licenses.db')
    conn.row_factory = sqlite3.Row
    return conn

# Логування всіх спроб у key.txt
def log_attempt(email, license_code, result):
    with open("key.txt", "a") as f:
        f.write(f"{datetime.now()} | Email: {email} | License: {license_code} | Result: {result}\n")

# Реєстрація нового користувача
@app.route("/register")
def register():
    email = request.args.get("email", "")
    if not email:
        return "Email required"

    conn = get_db_connection()
    cursor = conn.cursor()

    # Перевіряємо, чи вже є ліцензія для цього e-mail
    cursor.execute("SELECT license_code FROM licenses WHERE email=?", (email,))
    row = cursor.fetchone()
    if row:
        conn.close()
        return f"Your license code: {row['license_code']}"

    # Генеруємо новий ліцензійний код
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    cursor.execute("INSERT INTO licenses (license_code, email, active) VALUES (?,?,0)", (code, email))
    conn.commit()
    conn.close()

    return f"Your license code: {code}"

# Перевірка ліцензії при запуску гри
@app.route("/mottak")
def receive_license():
    license_code = request.args.get("license", "")
    email = request.args.get("email", "")
    
    if not license_code or not email:
        return "License code and email required"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT active FROM licenses WHERE license_code=? AND email=?", (license_code, email))
    row = cursor.fetchone()

    if row:
        # Ліцензія тепер може використовуватися багато разів, не змінюємо active
        conn.close()
        result = "License approved"
        log_attempt(email, license_code, result)
        return result
    else:
        conn.close()
        result = "Invalid license"
        log_attempt(email, license_code, result)
        return result

# Запуск сервера
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
