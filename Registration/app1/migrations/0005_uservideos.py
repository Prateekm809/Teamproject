# Generated by Django 4.2.4 on 2023-09-28 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0004_remove_completedexercise_user_delete_exercise_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_1', models.BooleanField(default=False)),
                ('video_2', models.BooleanField(default=False)),
                ('video_3', models.BooleanField(default=False)),
                ('video_4', models.BooleanField(default=False)),
                ('video_5', models.BooleanField(default=False)),
                ('video_6', models.BooleanField(default=False)),
                ('video_7', models.BooleanField(default=False)),
                ('video_8', models.BooleanField(default=False)),
                ('video_9', models.BooleanField(default=False)),
                ('video_10', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
