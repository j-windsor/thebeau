from __future__ import unicode_literals

from django.db import models

# Create your models here.

class QuestionAndAnswer(models.Model):
    question = models.CharField(max_length=50)
    answer = models.TextField(max_length=300)
    def __str__(self):
        return self.question

class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    email = models.EmailField()
    image = models.ImageField(upload_to="team_member_pics")
    def __str__(self):
        return self.name
