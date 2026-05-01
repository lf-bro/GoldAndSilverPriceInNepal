# Gold & Silver Price in Nepal Web App

<p align="center">
  <img src="https://goldandsilverpriceinnepal.onrender.com/static/screenshots/banner.png" alt="Banner">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-Python-blue?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/Backend-API-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Deployment-Render-purple?style=for-the-badge" />
</p>

---

## 📌 Overview

A simple **Flask-based web application** that displays the latest **gold and silver prices in Nepal** using web scraping.

The application scrapes updated price data, stores it locally, and serves it through a **clean UI and JSON API**.

---

## ✨ Features

- 📈 Displays gold prices in Nepal
- 📉 Displays silver prices in Nepal
- 🕸️ Web scraping integration
- ⚡ Fast cached responses
- 🔗 JSON API support
- 📱 Responsive UI
- 🚀 Deployable on Render

---

## 🖼️ Screenshots

### 🏠 Homepage

<p align="center">
  <img src="https://goldandsilverpriceinnepal.onrender.com/static/screenshots/home.png" />
</p>

### 📊 Price Display

<p align="center">
  <img src="https://goldandsilverpriceinnepal.onrender.com/static/screenshots/display.png" />
</p>

---

## 🛠️ Tech Stack

### Backend

- Python
- Flask
- bs4
- requests
- apscheduler
- gunicorn

### Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates
- TailwindCSS

### Deployment

- Render

---

## 📁 Project Structure

```bash
project/
│
├── main.py
├── scrap.py
├── rate.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│
└── README.md

```

---

## ⚙️ Installation

### 1. Clone Repository

git clone https://github.com/lf-bro/GoldAndSilverPriceInNepal.git

### 2. Move into Project

cd your-repository-name

### 3. Create Virtual Environment

***Windows***
python -m venv venv
venv\Scripts\activate

***Linux / Mac***
python3 -m venv venv
source venv/bin/activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Run Project

python main.py
🌐 API Endpoints

📊 Get Prices
/rate
Returns JSON formatted gold & silver prices.

❤️ Health Check
/health

Used for deployment monitoring.

## 🚀 Deployment

You can deploy this project using:

Render
Railway
Fly.io
▶️ Production Start Command
gunicorn main:app

## ⚡ Optimization

Scraping runs separately from user requests
Data stored in rate.json
Instant API response using cached data
Reduces server load and improves speed

### 🔮 Future Improvements

📊 Historical price tracking
📈 Graph visualization
🗄️ PostgreSQL integration
🧑‍💻 Admin dashboard
🔍 Search functionality
📱 Mobile UI improvements
👨‍💻 Author

#### Made by: L.F. PEMI MAGAR

🔗 GitHub: https://github.com/lf-bro

🔗 LinkedIn: https://www.linkedin.com/in/lfpemimagar/

<p align="center"> ⭐ If you like this project, don't forget to star the repository! </p>
