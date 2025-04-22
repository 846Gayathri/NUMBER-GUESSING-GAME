from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ''
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1
            if guess < session['number']:
                message = '📉Too low!'
            elif guess > session['number']:
              message = '📈Too high!'
            else:
                message = f'🎉 Congratulations! You guessed it in {session["attempts"]} tries!'
                session.pop('number')
                session.pop('attempts')
        except ValueError:
            message = '❌Please enter a valid number.'

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
