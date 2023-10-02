from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='team/images/')
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    join_date = models.DateField()

    def __str__(self):
        return self.name
