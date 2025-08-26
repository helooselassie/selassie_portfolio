from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200, default="SelData Solutions")
    description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.CharField(max_length=20, default="Present")

    def __str__(self):
        return f"{self.role} at {self.company}"
