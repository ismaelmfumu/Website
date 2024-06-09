# /project/app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/background')
def background():
    return render_template('background.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


@app.route('/photos')
def photos():
    # Assuming you have a photos.html template in your templates folder
    return render_template('photos.html')


if __name__ == '__main__':
    app.run(debug=True)
