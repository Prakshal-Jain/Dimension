from algorithms.analyseFiles import analyser
from flask import Flask, render_template, request, jsonify
import algorithms.analyseFiles

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route('/<name>', methods=['GET', 'POST'])
def hello(name=None):
    if(name == 'sitting'):
        return render_template('sitting.html', name=name)
    elif(name == 'virtual'):
        return render_template('virtual.html', name=name)


@app.route('/get-speaker', methods=['GET', 'POST'])
def getSpeaker():
    information = request.data.decode()
    print(information)
    return "1"

@app.route('/get-address', methods=['GET', 'POST'])
def getAddress():
    information = request.data.decode()
    algorithms.analyseFiles.analyser(information)
    return "1"