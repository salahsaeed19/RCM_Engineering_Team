# Generated by Django 4.2.6 on 2024-11-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineering_summaries', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineeringCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='engineeringsummary',
            name='category',
        ),
        migrations.AddField(
            model_name='engineeringsummary',
            name='categories',
            field=models.ManyToManyField(to='engineering_summaries.engineeringcategory'),
        ),
    ]