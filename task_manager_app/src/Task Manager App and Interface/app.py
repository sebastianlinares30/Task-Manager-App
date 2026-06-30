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
        "SELECT id FROM users WHERE email = ? AND password = ?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"success": True, "user_id": user[0]})
    return jsonify({"success": False})

@app.route("/add-task", methods=["POST"])
def add_task():
    data = request.get_json()
    user_id = data["user_id"]
    task_name = data["task_name"]
    due_date = data["due_date"]

    conn = sqlite3.connect("taskapp.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (user_id, task_name, due_date) VALUES (?, ?, ?)",
        (user_id, task_name, due_date)
    )
    conn.commit()
    conn.close()

    return jsonify({"success": True})

@app.route("/get-tasks", methods=["GET"])
def get_tasks():
    user_id = request.args.get("user_id")

    conn = sqlite3.connect("taskapp.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT task_name, due_date FROM tasks WHERE user_id = ?", 
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    tasks = [{"task_name": row[0], "due_date": row[1]} for row in rows]
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)