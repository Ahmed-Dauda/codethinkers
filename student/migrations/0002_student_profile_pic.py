# Generated by Django 3.2.9 on 2021-12-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/Student/'),
        ),
    ]
