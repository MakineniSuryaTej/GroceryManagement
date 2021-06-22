from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('grocery-home.html')

@app.route('/grocery-login')
def login():
    return render_template('grocery-login.html')

if __name__=='__main__':
    app.run(debug=True)