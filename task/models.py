from django.db.models import Model, CharField, TextField, FileField, ForeignKey, CASCADE, ManyToManyField, DateTimeField, TextChoices
from django.contrib.auth.models import AbstractUser


class Project(Model):
    name = CharField(max_length=255)
    description = TextField()
    owner = CharField(max_length=255)
    created_At = DateTimeField(auto_now_add=True)
    # assignes =

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Task(Model):
    name = CharField(max_length=255)
    description = TextField()
    project = ForeignKey('task.Project', CASCADE)
    # status =
    # deadline = DateTimeField()
    craeted_at = DateTimeField(auto_now_add=True)
    # assignes =


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = "admin", 'Admin'
        USER = "user", 'User'

    role = CharField(max_length=50, choices=Role.choices, default=Role.USER)


class Notifications(Model):
    user = ForeignKey('task.User', CASCADE)
    message = TextField()
    created_at = DateTimeField(auto_now_add=True)
