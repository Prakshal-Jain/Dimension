from algorithms.analyseFiles import analyser
from algorithms.generateRec import record, getAngle_intensity, stop, re_start
from flask import Flask, render_template, request, jsonify
import algorithms.analyseFiles
import json
import os

app = Flask(__name__)
userInfo = {"email": "", "dest_path": "", "flag": "", "URL_dest": ""}
@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route('/<name>', methods=['GET', 'POST'])
def hello(name=None):
    # if(userInfo["email"] == "" or userInfo["dest_path"] == ""):
    #     userInfo["flag"] = "Please complete your profile before proceeding."
    #     userInfo["URL_dest"] = "/"+name
    #     return render_template('settings.html', name=name, input_from_python= userInfo)
    # else:
        if(name == 'sitting'):
            userInfo["flag"] = ""
            return render_template('sitting.html', name=name, input_from_python= userInfo)
        elif(name == 'virtual'):
            userInfo["flag"] = ""
            return render_template('virtual.html', name=name)
        elif(name == 'settings'):
            userInfo["flag"] = ""
            return render_template('settings.html', name=name, input_from_python= userInfo)


@app.route('/start-recording', methods=['GET', 'POST'])
def startRec():
    algorithms.generateRec.re_start()
    information = request.data.decode()
    angle = int(json.loads(information))
    print(angle)
    filename = "recording_"+userInfo["email"].split("@")[0]
    while(os.path.exists(filename+".wav")):
        filename += "_new"
    algorithms.generateRec.getAngle_intensity(angle)
    algorithms.generateRec.record(filename+".wav")
    return "1"

@app.route('/get-speaker', methods=['GET', 'POST'])
def getSpeaker():
    information = request.data.decode()
    angle = int(json.loads(information))
    print(angle)
    algorithms.generateRec.getAngle_intensity(angle)
    return "1"

@app.route('/stop-recording', methods=['GET', 'POST'])
def stopRec():
    algorithms.generateRec.stop()
    return "1"

@app.route('/get-address', methods=['GET', 'POST'])
def getAddress():
    information = request.data.decode()
    algorithms.analyseFiles.analyser(information, userInfo["dest_path"], userInfo["email"])
    return "1"

@app.route('/get-user_info', methods=['GET', 'POST'])
def getUserInfo():
    information = json.loads(request.data.decode())
    userInfo["email"] = information["email"]
    userInfo["dest_path"] = information["dest_path"]
    return "1"