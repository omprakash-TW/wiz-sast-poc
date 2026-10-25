import sqlite3, os, subprocess, pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def user():
    uid = request.args.get("id")
    conn = sqlite3.connect("test.db")
    # SQL injection
    return str(conn.execute("SELECT * FROM users WHERE id = " + uid).fetchall())

@app.route("/ping")
def ping():
    host = request.args.get("host")
    # Command injection
    return subprocess.check_output("ping -c 1 " + host, shell=True)

@app.route("/load")
def load():
    # Insecure deserialization
    return str(pickle.loads(request.data))
