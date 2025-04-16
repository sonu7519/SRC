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

    # Use parameterized query to prevent injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    conn.close()

    return {"users": result}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

'''
Recommendation :-

    1.) Always use parameterized queries
    2.) Validate and sanitize user inputs
    3.) Use ORM like SQLAlchemy for abstraction and safety

'''