from flask import Flask, render_template, request
from functions.generate_random_string import generate_random_string
from random import choice


app = Flask(__name__)


playlist = ['static/audio/shit.mp3', 'static/audio/teplovizor.mp3',
            'static/audio/govno.mp3', 'static/audio/banger.mp3',
            'static/audio/shit2.mp3', 'static/audio/shit3.mp3',
            'static/audio/cock.mp3', 'static/audio/shedevr.mp3',
            'static/audio/slit.mp3']

background_image = 'static/pictures/background.jpg'


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    params = dict()
    params['title'] = 'База'
    params['music'] = choice(playlist)
    params['background'] = background_image
    return render_template('home.html', **params)


@app.route('/text-to-gradient', methods=['GET', 'POST'])
def text_to_gradient():
    if request.method == 'GET':
        params = dict()
        params['title'] = 'Сучий градиент'
        params['music'] = choice(playlist)
        params['background'] = background_image
        return render_template('text-to-gradient.html', **params)
    elif request.method == 'POST':
        return '123'


@app.route('/image-to-audio', methods=['GET', 'POST'])
def image_to_audio():
    if request.method == 'GET':
        params = dict()
        params['title'] = 'Тайлер Дёрден'
        params['music'] = choice(playlist)
        params['background'] = background_image
        return render_template('text-to-gradient.html', **params)
    elif request.method == 'POST':
        return 'Мы вообще будем это делать?'


def main():
    app.config['SECRET_KEY'] = generate_random_string(12)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
