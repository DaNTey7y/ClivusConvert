from flask import Flask, render_template
from functions.generate_random_string import generate_random_string


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='База')


def main():
    app.config['SECRET_KEY'] = generate_random_string(12)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
