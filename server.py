from flask import Flask, render_template
from Controller.EarthquakeController import INA_TEWS, BMKG_Data
from Controller.DashboardController import Dashboard, DashboardStatistics

app = Flask(__name__)


@app.route("/")
def home():
  return "ridwan dimari"


# ============= DASHBOARD ========
@app.route("/dashboard")
def dashboard():
  dashboard = Dashboard()
  list_mag = DashboardStatistics()
  #dashboard_chart = DashboardController()
  longitude, latitude, headline = dashboard.maps_dashboard()
  info_dashboard = dashboard.news_dashboard()
  mag30feltEvent = list_mag.McountList()
  magHistoryEvent = list_mag.magHistory()
  return render_template("dashboard.html",
                         info_dashboard=info_dashboard,
                         longitude=longitude,
                         latitude=latitude,
                         headline=headline,
                         mag30feltEvent=mag30feltEvent,
                         magHistoryEvent=magHistoryEvent
                        )


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
  return render_template("inatews-maps.html",
                         longitude=longitude,
                         latitude=latitude,
                         headline=headline,
                         json_data=json_data)


@app.route("/inatews-live30event")
def inatews_live30event():
  inatews = INA_TEWS()
  json_data, average_dalam, average_mag, total_data = inatews.live30event()
  #average_dalam_formatted = "{:.2f}".format(average_dalam)
  #average_mag_formatted = "{:.2f}".format(average_mag)
  return render_template("inatews-live30event.html",
                         json_data=json_data,
                         average_dalam=average_dalam,
                         average_mag=average_mag,
                         total_data=total_data)


@app.route("/inatews-last30event")
def inatews_last30event():
  inatews = INA_TEWS()
  json_data, average_magnitude, average_depth, total_data = inatews.last30event(
  )
  return render_template("inatews-last30event.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


@app.route("/inatews-last30feltevent")
def inatews_last30feltevent():
  inatews = INA_TEWS()
  json_data, average_magnitude, average_depth, total_data = inatews.last30feltevent(
  )
  return render_template("inatews-last30feltevent.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


@app.route("/inatews-last30tsunamievent")
def inatews_last30tsunamievent():
  inatews = INA_TEWS()
  json_data, average_magnitude, average_depth, total_data = inatews.last30tsunamievent(
  )
  return render_template("inatews-last30tsunamievent.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


@app.route("/inatews-EmgempaQL")
def inatews_EmgempaQL():
  inatews = INA_TEWS()
  json_data, average_magnitude, average_depth, total_data = inatews.EmgempaQL()
  return render_template("inatews-EmgempaQL.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


@app.route("/inatews-EQcatalog")
def inatews_EQcatalog():
  inatews = INA_TEWS()
  json_data, average_magnitude, average_depth, total_data = inatews.katalog_gempa(
  )
  return render_template("inatews-katalog_gempa.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


@app.route("/inatews-history")
def inatews_history():
  inatews = INA_TEWS()
  json_data, average_magnitude, average_depth, total_data = inatews.histori()
  return render_template("inatews-histori.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


# =========== BMKG DATA ==========
@app.route("/bmkgdata-news")
def bmkgdata_news():
  bmkgdata = BMKG_Data()
  json_data = bmkgdata.news()
  return render_template("bmkgdata-news.html", json_data=json_data)


@app.route("/bmkgdata-maps")
def bmkgdata_maps():
  bmkgdata = BMKG_Data()
  latitude, longitude, gempa_data = bmkgdata.maps()
  return render_template("bmkgdata-maps.html",
                         latitude=latitude,
                         longitude=longitude,
                         json_data=gempa_data)


@app.route("/bmkgdata-recentEQ")
def bmkgdata_recentEQ():
  bmkgdata = BMKG_Data()
  json_data, average_magnitude, average_depth, total_data = bmkgdata.recentEQ()
  return render_template("bmkgdata-recentEQ.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)


@app.route("/bmkgdata-EQfelt")
def bmkgdata_EQfelt():
  bmkgdata = BMKG_Data()
  json_data, average_magnitude, average_depth, total_data = bmkgdata.EQfelt()
  return render_template("bmkgdata-EQfelt.html",
                         json_data=json_data,
                         average_magnitude=average_magnitude,
                         average_depth=average_depth,
                         total_data=total_data)
