from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    tags = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True, null=True)
    sentiment_score = models.FloatField(blank=True, null=True)  # For sentiment analysis

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=500)

# outreach_app/models.py
from django.db import models

class Feedback(models.Model):
    text = models.TextField()  # Store the feedback text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when feedback was submitted

    def __str__(self):
        return self.text[:50]  # Display a truncated version of the feedback in admin

