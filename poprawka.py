from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return 'Użytkownik o tej nazwie już istnieje! Wybierz inną nazwę.'
    else:
        users[username] = password
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
