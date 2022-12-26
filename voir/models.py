from django.db import models
from datetime import datetime, timedelta, date

from django.utils.html import format_html

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task", null=True)
    due_date = models.DateField(null=True)

    scheldule_date = models.DateField(default=datetime.now()+timedelta(days=7)) 
    def __str__(self):
        return self.name
    
    """def colered_due_date(self):
        due_date = django_date(self.due_date, "d F Y")
        if self.due_date is None or self.due_date - timedelta(days=7) > date.today():

            color = "green"

        elif self.due_date < date.today():

            color = "red"

        else:

            color = "orange"
        return format_html("<span style=color:%s>%s</span>" % (color, due_date))
    
    colered_due_date.allow_tags = True
"""

    