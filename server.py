from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/inatews-news")
def inatews_news():
  return render_template("inatews-news.html")