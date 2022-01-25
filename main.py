from flask import Flask, url_for


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return '<h1>suck</h1>'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
