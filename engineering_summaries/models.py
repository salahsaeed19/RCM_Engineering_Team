from django.db import models
from django.contrib.auth.models import User

class EngineeringSummary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    category = models.CharField(max_length=100, choices=(
        ('Mechanical', 'Mechanical Engineering'),
        ('Electrical', 'Electrical Engineering'),
        ('Civil', 'Civil Engineering'),
        ('Computer', 'Computer Engineering'),
        ('Other', 'Other'),
    ))
    source_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='engineering_summaries/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)  # New field for tracking views
    
    def __str__(self):
        return self.title
