from django.db import models

class EngineeringCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class EngineeringSummary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField()
    categories = models.ManyToManyField(EngineeringCategory)
    source_link = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='engineering_summaries/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
