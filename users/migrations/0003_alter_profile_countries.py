# Generated by Django 3.2.9 on 2021-12-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='countries',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]