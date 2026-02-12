from flask import Flask, request, jsonify
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Read env variables
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# Connect to Postgres
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

# Create table on startup
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            name TEXT,
            feedback TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/feedback", methods=["POST"])
def add_feedback():
    data = request.json
    name = data["name"]
    feedback = data["feedback"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (name, feedback) VALUES (%s, %s)", (name, feedback))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Feedback added"}), 201

@app.route("/feedback", methods=["GET"])
def get_feedback():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, feedback FROM feedback")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([{"name": r[0], "feedback": r[1]} for r in rows])

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
