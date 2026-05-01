from flask import Flask, render_template, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import scrap
import json

app = Flask(__name__)

# Run scraper once on startup
scrap.scrap()

# Schedule scraper every 24 hours
scheduler = BackgroundScheduler()
scheduler.add_job(func=scrap.scrap, trigger="interval", hours=24)
scheduler.start()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return "ok", 200


@app.route("/rate")
def rate():
    with open("rate.json", "r") as f:
        return jsonify(json.load(f))


if __name__ == "__main__":
    app.run(debug=True)
