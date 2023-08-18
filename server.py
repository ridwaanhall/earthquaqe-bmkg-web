from flask import Flask, render_template
from Controller.INATEWS import INA_TEWS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/inatews-news")
def inatews_news():
    inatews = INA_TEWS()
    json_data = inatews.news()
    return render_template("inatews-news.html", json_data=json_data)