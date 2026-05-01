# 🇳🇵 Nepal Gold & Silver Price Web App

A simple Flask-based web application that displays the latest gold and silver prices in Nepal using web scraping.

The application scrapes updated price data, stores it locally, and serves it through a clean web interface and JSON API.

---

# ✨ Features

- Displays gold prices in Nepal
- Displays silver prices in Nepal
- Web scraping integration
- JSON API endpoint
- Fast cached data delivery
- Flask backend
- Responsive frontend
- Deployable on Render

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask

## Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

## Deployment

- Render

---

# 📁 Project Structure

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

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/your-repository-name.git
2. Move into the project directory
cd your-repository-name
3. Create virtual environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Run the project
python main.py
🌐 API Endpoints
📊 Get Gold & Silver Prices
/rate

Returns JSON formatted price data.

❤️ Health Check
/health

Used for deployment monitoring on Render.

🚀 Deployment

This project can be deployed using:

Render
Railway
Fly.io
▶️ Recommended Start Command
gunicorn main:app
⚡ Optimization
Scraping process is separated from user requests
Data is stored locally in rate.json
Users receive cached data instantly
Improves performance and reduces unnecessary scraping
🔮 Future Improvements
Historical price records
Charts and visualization
PostgreSQL integration
Admin dashboard
Search functionality
Mobile UI improvements
👨‍💻 Author

Made by: L.F. PEMI MAGAR

🔗 GitHub: https://github.com/lf-bro

🔗 LinkedIn: https://www.linkedin.com/in/lfpemimagar/
```