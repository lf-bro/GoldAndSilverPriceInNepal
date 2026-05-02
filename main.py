from flask import Flask, render_template, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import scrape
import json
import logging
import atexit

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Run scraper once on startup with error handling
try:
    scrape.scrape()
    logger.info("Initial scrape completed successfully")
except Exception as e:
    logger.error(f"Initial scrape failed: {e}", exc_info=True)

# Schedule scraper to run daily at 11 AM (Nepal Time)
scheduler = BackgroundScheduler(timezone="Asia/Kathmandu")
scheduler.add_job(
    func=scrape.scrape,
    trigger="cron",
    hour=11,
    minute=0,
    id="gold_silver_scraper",
    name="Gold and Silver Price Scraper",
    replace_existing=True,
    max_instances=1,
)
scheduler.start()
logger.info("Scheduler started")


# Graceful shutdown
def shutdown_scheduler():
    if scheduler.running:
        scheduler.shutdown()
        logger.info("Scheduler shut down gracefully")


atexit.register(shutdown_scheduler)


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
    app.run(debug=False)
