from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask App"
        })

@app.route("/info")
def info():
    return "I am from India"

@app.route("/phone")
def phone():
    return "1111222233"

app.run(host="0.0.0.0")




