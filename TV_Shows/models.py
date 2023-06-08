from django.db import models
from django.utils import timezone
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        title = postData.get('title')
        if Show.objects.filter(title=title).exists():
            errors["title"] = "A TV show with this title already exists"
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if postData['description'] and len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters if it's added"
        release_date_str = postData.get('release_date')
        if release_date_str:
            release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
            current_date = timezone.now().date()
            if release_date > current_date:
                errors["release_date"] = "Release date must be in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()