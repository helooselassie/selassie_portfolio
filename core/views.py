from django.shortcuts import render
from .models import Project, Experience
from .forms import ContactForm   # ✅ import the form
import requests
from django.core.mail import send_mail
import json
from core.models import Experience


def home(request):
    projects = Project.objects.all().order_by('-id')[:3]
    return render(request, "core/home.html", {
        "projects": projects,
    })

def about(request):
    return render(request, "core/about.html")

def resume(request):
    return render(request, "core/resume.html")

def skills(request):
    skills = ["Python", "Django", "APIs", "Backend development", "Frontend development"]
    services = [
        "Web & Software Development",
        "IT Infrastructure",
        "E-Security Systems",
        "Branding & Creative Design",
        "Digital Marketing"
    ]
    return render(request, "core/skills.html", {"skills": skills, "services": services})


def projects(request):
    # Fetch projects from DB
    db_projects = Project.objects.all()

    # Fetch repos from GitHub API
    url = "https://api.github.com/users/helooselassie/repos"
    response = requests.get(url)
    github_projects = []
    if response.status_code == 200:
        data = response.json()
        for repo in data:
            github_projects.append({
                "name": repo["name"],
                "description": repo.get("description", "No description"),
                "url": repo["html_url"]
            })

    return render(request, "core/projects.html", {
        "db_projects": db_projects,
        "github_projects": github_projects
    })


def contact(request):
    sent = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # send email
            subject = f"Portfolio Contact from {name}"
            body = f"Message from {name} <{email}>:\n\n{message}"
            send_mail(subject, body, email, ["your_email@gmail.com"])  # recipient

            sent = True
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form, "sent": sent})


def experience(request):
    exp_list = Experience.objects.all().order_by("-start_year")
    return render(request, "core/experience.html", {"exp_list": exp_list})
