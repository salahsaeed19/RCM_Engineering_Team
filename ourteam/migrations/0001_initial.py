# Generated by Django 4.2.5 on 2023-09-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=5000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='team/images/')),
                ('social_media_link', models.URLField(blank=True, null=True)),
                ('join_date', models.DateField()),
            ],
        ),
    ]
