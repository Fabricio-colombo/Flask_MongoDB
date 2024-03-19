from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient

app = Flask(__name__)

URI_config = "mongodb://localhost:27017"
nome_config = "Site_Flask"
collection_name_config = "BD_LOGIN"

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

client = MongoClient(URI_config)
db = client[nome_config]
collection = db[collection_name_config]

@app.route('/')
def index():
    login = request.args.get('username', '')
    senha = request.args.get('password', '')
    user_data = collection.find_one({'username': login, 'password': senha})
    if user_data:
        print('Login bem sucedido')
        return redirect(url_for('login'))
    return render_template('index.html')

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_data = collection.find_one({'username': username, 'password': password})
        if user_data:
            session['username'] = username
            return redirect(url_for('index')) 
        else:
            return render_template('login.html', error='Credenciais inválidas. Tente novamente.')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if collection.find_one({'username': username}):
            return render_template('register.html', error='Nome de usuário já existe. Tente outro.')
        else:
            collection.insert_one({'username': username, 'password': password})
            return redirect(url_for('index')) 
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot.html')

if __name__ == '__main__':
    app.run(debug=True)
