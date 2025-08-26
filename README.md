# Selassie Portfolio 🚀

A modern, responsive portfolio website built with **Django**, **Bootstrap 5**, and **Bootstrap Icons**.  
This project showcases my work as a **Systems Engineer & Cybersecurity Advocate**, including featured projects, skills, and a contact form.

---

## 🌟 Features
- 🔥 **Dynamic Portfolio** – Projects are fetched from Django models  
- 🎨 **Modern UI/UX** – Bootstrap 5, animations, hover effects, and sticky navbar  
- 📬 **Contact Form** – Secure form with CSRF protection  
- 📂 **Projects Section** – Display featured projects with links to GitHub repos  
- 💡 **About Me** – Highlight experience, fun facts, and career philosophy  
- 📊 **Stats Section** – Years of experience, projects delivered, and clients served  
- ⚡ **Tech Stack Icons** – Python, JavaScript, Bootstrap, Git, Cloud, Cybersecurity  

---

## 🛠 Tech Stack
- **Backend:** Django 4+
- **Frontend:** Bootstrap 5, Bootstrap Icons, Animate.css
- **Database:** SQLite (default, easy for development)
- **Hosting Ready:** Can be deployed to **Heroku, Railway, Render, or DigitalOcean**

---

## 📂 Project Structure

selassie_portfolio/
│── core/ # Main Django app (templates, views, models, urls)
│ ├── templates/core/ # HTML templates
│ ├── static/ # Static files (CSS, JS, Images)
│ ├── views.py # Page logic
│ ├── models.py # Projects & content models
│ └── urls.py # URL routing
│
│── selassie_portfolio/ # Project config (settings, urls, wsgi/asgi)
│── db.sqlite3 # Default SQLite DB
│── manage.py # Django management tool
│── requirements.txt # Dependencies
│── README.md # Project documentation


1. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

2. Install Dependencies
pip install -r requirements.txt

3. Run Migrations
python manage.py migrate

4. Create Superuser (optional)
python manage.py createsuperuser

5. Run Development Server
python manage.py runserver


Visit 👉 http://127.0.0.1:8000/

## 📦 Deployment
Collect Static Files
Before deploying:
python manage.py collectstatic


## 👨‍💻 Author
Selassie Kwabla Heloo
🌍 Systems Engineer & Cybersecurity Advocate
📧 Contact Me
💼 LinkedIn
💻 GitHub