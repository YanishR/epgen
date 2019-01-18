from flask import Flask, render_template, request
from ShowObject import *

#setup Flask application
app = Flask(__name__)


@app.route("/")
def index():
     return "Running"

@app.route("/show", methods=['GET', 'POST'])
def searchShow():
    if request.method == 'GET':
        resDict = {"printShow" : False}
        return render_template('template.html', resDict=resDict)
    elif request.method =='POST':
        try:
            userShow = Show(request.form['show'])
        except tvApi.tvdb_shownotfound:
            return render_template('error.html', message="This show does not exist")

        resDict = {"printShow" : True,
            "showName" : userShow.show['seriesName'],
            "episode" : userShow.generateRandomEpisode()
        }
        return render_template('template.html', resDict=resDict)
