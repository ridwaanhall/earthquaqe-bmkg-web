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


@app.route("/inatews-maps")
def inatews_maps():
    ina_tews = INA_TEWS()
    longitude, latitude, headline = ina_tews.maps()
    json_data = ina_tews.news()
    return render_template("inatews-maps.html", longitude=longitude, latitude=latitude, headline=headline, json_data=json_data)


@app.route("/test")
def test():
    return render_template("testing.html")