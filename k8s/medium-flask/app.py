# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a GKE!'

@app.route('/<name>')
def hello_name(name):
    return 'Hello, ' + name + '!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

