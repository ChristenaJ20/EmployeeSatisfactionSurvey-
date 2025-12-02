from django.db import models
from django.contrib.auth.models import User

# Christena Jenkins

# Create your models here.

class SurveySubmission(models.Model):
    """Model to store employee survey submissions."""
    department = models.CharField(max_length=200)
    rating = models.IntegerField()
    comment = models.TextField()
    anonymous = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    # Meta information for the model
    class Meta:
        ordering = ['department', '-submitted_at']
        verbose_name = 'Survey Submission'
        verbose_name_plural = 'Survey Submissions'
    
    def __str__(self):
        if self.anonymous:
            return f"Anonymous - {self.department} - Rating: {self.rating}"
        return f"{self.username} - {self.department} - Rating: {self.rating}"
