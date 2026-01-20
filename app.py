from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<body style="text-align:center; font-family:Arial;">
    <h1>RPS Docker Game</h1>
    <form method="POST">
        <button name="choice" value="rock">Rock</button>
        <button name="choice" value="paper">Paper</button>
        <button name="choice" value="scissors">Scissors</button>
    </form>
    {% if result %} <h2>{{ result }}</h2> {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def game():
    result = None
    if request.method == "POST":
        user = request.form.get("choice")
        comp = random.choice(["rock", "paper", "scissors"])
        if user == comp: result = f"Tie! Both chose {user}."
        elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock"):
            result = f"Win! {user} beats {comp}."
        else: result = f"Lose! {comp} beats {user}."
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
