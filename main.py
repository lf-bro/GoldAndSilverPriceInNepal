from flask import Flask, render_template, jsonify
import scrap
import json
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route("/")
def home():
    scrap.scrap()
    return render_template("index.html")


@app.route("/rate")
def rate():
    with open("rate.json", "r") as f:
        return jsonify(json.loads(f.read()))


app.run(debug=True)
