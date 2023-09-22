from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField(max_length=5000, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='team/images/')
    social_media_link = models.URLField(blank=True, null=True)
    join_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
