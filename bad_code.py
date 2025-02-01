# Bad code
import sqlite3

def find_user(username):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()

    connection.close()
    return result

# Simulate user input
user_input = "'; DROP TABLE users; --"
print("User query result:", find_user(user_input))
