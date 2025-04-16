from flask import Flask, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/user')
def get_user():
    username = request.args.get('username')  # Input from user
    conn = get_db_connection()
    cursor = conn.cursor()

    # Directly embedding user input into the SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    return {"users": result}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5080)

# http://192.168.1.166:5080/user?username=admin' or '1'='1