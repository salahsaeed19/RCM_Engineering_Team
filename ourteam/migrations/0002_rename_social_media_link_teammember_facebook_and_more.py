# Generated by Django 4.2.5 on 2023-10-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='social_media_link',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='teammember',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='phone',
        ),
        migrations.AddField(
            model_name='teammember',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='bio',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
