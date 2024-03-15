from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return 'Página de registro ainda não implementada.'

@app.route('/forgot-password')
def forgot_password():
    return 'Página de esqueceu sua senha ainda não implementada.'

if __name__ == '__main__':
    app.run(debug=True)
