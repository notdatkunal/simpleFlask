from flask import Flask, render_template, url_for, redirect, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "welcome to audit application"


@app.route("/details")
def details():
    return "this is details response"


@app.route("/page/<name>")
def page(name):
    return render_template("home.html", name=name)


@app.route("/page")
def normal_page():
    return render_template("home.html")


@app.route("/double")
def double():
    return jsonify({'output': [1, 2, "output element", "and", 5, "output again and ", "regular"]})
