from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route('/<name>', methods=['GET', 'POST'])
def hello(name=None):
    return render_template('sitting.html', name=name)


@app.route('/get-speaker', methods=['GET', 'POST'])
def getSpeaker():
    information = request.data.decode()
    print(information)
    return "1"