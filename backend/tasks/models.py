from django.db import models
from django.contrib.auth.models import User

# project class (overall large task to be done)
class Project(models.Model):
    name = models.CharField(max_length=200)
    # can be blank
    description = models.TextField(blank=True)
    # auto add when made
    created_at = models.DateTimeField(auto_now_add=True)
    # when owner is deleted, delete the projects they own as well
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name


# task class, many tasks make up a project
class Task(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=200)
    # can be blank
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# comment designed to be added to tasks with an author as a user
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"