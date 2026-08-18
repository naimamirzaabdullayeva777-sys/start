from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.phone


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    level = models.CharField(max_length=10)
    pages = models.IntegerField()
    image = models.ImageField(upload_to="books/")
    pdf = models.FileField(upload_to="books/pdf/", blank=True, null=True)

    def __str__(self):
        return self.name


class Shadow(models.Model):
    video = models.FileField(upload_to="shadow/videos/", blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    minute = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="shadow/images/", blank=True, null=True)

    def __str__(self):
        return f"{self.level} - {self.minute}"


class Listening(models.Model):
    img = models.ImageField(upload_to="Listening/img/", blank=True, null=True)
    audio = models.FileField(upload_to="Listening/audio/", blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to="movies/", blank=True, null=True)
    video = models.FileField(upload_to="movies/videos/", blank=True, null=True)

    def __str__(self):
        return self.name


class QuizQuestion(models.Model):
    question = models.CharField(max_length=255)

    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)

    correct_answer = models.CharField(max_length=100)

    level = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    topic = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.question