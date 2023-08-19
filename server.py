from flask import Flask, render_template
from Controller.EarthquakeController import INA_TEWS, BMKG_Data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


# =========== INATEWS ==========
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


@app.route("/inatews-live30event")
def inatews_live30event():
    inatews = INA_TEWS()
    json_data, average_dalam, average_mag, total_data = inatews.live30event()
    average_dalam_formatted = "{:.2f}".format(average_dalam)
    average_mag_formatted = "{:.2f}".format(average_mag)
    return render_template("inatews-live30event.html", json_data=json_data, average_dalam=average_dalam, average_mag=average_mag, total_data=total_data)


# =========== BMKG DATA ==========
@app.route("/bmkgdata-news")
def bmkgdata_news():
    bmkgdata = BMKG_Data()
    json_data = bmkgdata.news()
    return render_template("bmkgdata-news.html", json_data=json_data)


@app.route("/bmkgdata-maps")
def bmkgdata_maps():
    bmkgdata = BMKG_Data()
    latitude, longitude = bmkgdata.maps()
    json_data = bmkgdata.news()
    return render_template("bmkgdata-maps.html", longitude=longitude, latitude=latitude, json_data=json_data)




@app.route("/test")
def test():
    return render_template("testing.html")