from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("taskapp.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return jsonify({"success": bool(user)})

if __name__ == "__main__":
    app.run(debug=True)