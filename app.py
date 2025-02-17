from flask import Flask, render_template, request, jsonify
import sqlite3
from models.chatbot import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

def init_db():
    conn = sqlite3.connect("database/db.sqlite")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS queries (
                      id INTEGER PRIMARY KEY,
                      user_query TEXT,
                      bot_response TEXT)''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("message")

    bot_response = get_response(user_query)

    conn = sqlite3.connect("database/db.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO queries (user_query, bot_response) VALUES (?, ?)", (user_query, bot_response))
    conn.commit()
    conn.close()

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
