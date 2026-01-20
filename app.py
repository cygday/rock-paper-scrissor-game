from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML_TEMPLATE = """
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ROCK, PAPER, SCISSOR GAME</title>
    <link rel="stylesheet" href="https://pyscript.net">
    <script type="module" src="https://pyscript.net"></script>
    <style>
        body { font-family: 'Arial Black', sans-serif; text-align: center; background: #1a1a1a; color: white; padding: 20px; }
        
        /* Large Output Text */
        #output { 
            margin: 40px 0; 
            font-size: 3.5rem; /* Massive text */
            min-height: 150px;
            text-transform: uppercase;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        }

        /* Large Action Buttons */
        .btn-container { display: flex; flex-direction: column; gap: 15px; max-width: 500px; margin: 0 auto; }
        button {
            padding: 30px;
            font-size: 2rem;
            font-weight: bold;
            border: none;
            border-radius: 15px;
            cursor: pointer;
            transition: transform 0.1s;
            text-transform: uppercase;
        }
        button:active { transform: scale(0.95); }
        
        .rock { background-color: #ff4757; color: white; } /* Red */
        .paper { background-color: #2f3542; color: white; } /* Dark Blue/Grey */
        .scissors { background-color: #2ed573; color: white; } /* Green */
    </style>
</head>
<body>
    <h1>CHOOSE YOUR MOVE</h1>
    
    <div id="output">TAP A BUTTON TO START!</div>


    <div class="btn-container">
        <!-- Forms are used to send the user's choice to the Flask server -->
        <form method="post" action="/">
            <input type="hidden" name="user_choice" value="rock">
            <button type="submit" class="rock" py-click="play('rock')">🗿 ROCK</button>
        </form>
        <form method="post" action="/">
            <input type="hidden" name="user_choice" value="paper">
            <button type="submit" class="paper" py-click="play('paper')">📄 PAPER</button>
        </form>
        <form method="post" action="/">
            <input type="hidden" name="user_choice" value="scissors">
            <button type="submit" class="scissors" py-click="play('scissor')">✂️ SCISSORS</button>
        </form>
    </div>
<script type="py">
    import random
    # You must import 'document' to use getElementById
    from pyscript import document 

    def play(user_choice):
        options = ["rock", "paper", "scissors"]
        comp = random.choice(options)
        
        # Game Logic
        if user_choice == comp:
            msg = f"TIE!<br><small>Both chose {user_choice}</small>"
        elif (user_choice == "rock" and comp == "scissors") or \
             (user_choice == "paper" and comp == "rock") or \
             (user_choice == "scissors" and comp == "paper"):
            msg = f"WIN!<br><small>{user_choice} beats {comp}</small>"
        else:
            msg = f"LOSE!<br><small>{comp} beats {user_choice}</small>"
        
        # Accessing the DOM
        output_div = document.getElementById("output")
        output_div.innerHTML = msg
</script>
</body>
</html>
"""

def determine_winner(user, computer):
    """Logic to determine the winner of the game."""
    if user == computer:
        return "It's a draw!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return f"You Win! {user.capitalize()} beats {computer}."
    else:
        return f"You Lose! {computer.capitalize()} beats {user}."

@app.route('/', methods=['GET', 'POST'])
def game():
    result_message = "TAP A BUTTON TO START!"

    if request.method == 'POST':
        user_choice = request.form['user_choice']
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result_message = determine_winner(user_choice, computer_choice)
        # Add the choices to the message for clarity
        result_message = f"You chose {user_choice}, computer chose {computer_choice}. {result_message}"

    # Render the template with the current result message
    return render_template_string(HTML_TEMPLATE, result_message=result_message)

if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 so it is accessible over a network/container
    app.run(host='0.0.0.0', port=5000, debug=True)

