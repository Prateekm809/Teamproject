# Generated by Django 4.2.4 on 2023-09-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_uservideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservideos',
            name='total_calories_burned',
            field=models.IntegerField(default=0),
        ),
    ]