from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    user = request.json.get("choice")
    comp = random.choice(["rock", "paper", "scissors"])

    if user == comp:
        result = "TIE"
        message = f"Both chose {user}"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        result = "WIN"
        message = f"{user} beats {comp}"
    else:
        result = "LOSE"
        message = f"{comp} beats {user}"

    return jsonify({
        "result": result,
        "message": message,
        "computer": comp
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
