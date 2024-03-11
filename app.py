from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)

    result, reason = determine_winner(user_choice, computer_choice)

    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result, reason=reason)

def determine_winner(user_choice, computer_choice):
    # Game rules
    rules = {
        'Rock': {'Scissors': 'Rock crushes Scissors', 'Lizard': 'Rock crushes Lizard'},
        'Paper': {'Rock': 'Paper covers Rock', 'Spock': 'Paper disproves Spock'},
        'Scissors': {'Paper': 'Scissors cuts Paper', 'Lizard': 'Scissors decapitates Lizard'},
        'Lizard': {'Spock': 'Lizard poisons Spock', 'Paper': 'Lizard eats Paper'},
        'Spock': {'Scissors': 'Spock smashes Scissors', 'Rock': 'Spock vaporizes Rock'}
    }

    if user_choice == computer_choice:
        return 'It\'s a tie!', None
    elif computer_choice in rules[user_choice]:
        reason = rules[user_choice][computer_choice]
        return 'You win!', reason
    else:
        reason = rules[computer_choice][user_choice]
        return 'Computer wins!', reason


if __name__ == '__main__':
    app.run(debug=True)
