import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', ('User', 'example@gmail.com', '10', '1000'))
for i in range(1, 11):
    cursor.execute('INSERT INTO  Users (username, email, age, balance) VALUES (?, ?, ?, ?) ',
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))
for j in range(1, 11):
    cursor.execute('UPDATE Users SET balance = ? WHERE id%2 = ?', (500, 1))
for k in range(1, 11):
    cursor.execute('DELETE FROM Users WHERE id%3 = ?', (1,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ? ', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users ')
total = cursor.fetchone()[0]
print(total)
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(total_balance)
cursor.execute('SELECT AVG(balance) FROM Users')
l_balance = cursor.fetchone()[0]
print(l_balance)
connection.commit()
connection.close()
