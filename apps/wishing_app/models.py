from __future__ import unicode_literals
from django.db import models
from apps.logreg.models import User


class JobManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["title"] = "Job title must be greater than 3 characters"
        if len(postData['desc']) < 3:
            errors["desc"] = "Job description must be greater than 3 characters"
        if len(postData['location']) < 3:
            errors["location"] = "Job location must be greater than 3 characters"
        return errors



class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    location = models.CharField(max_length=255)
    user_jobs = models.ForeignKey(User, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
