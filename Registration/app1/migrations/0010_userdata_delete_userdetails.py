# Generated by Django 4.2.4 on 2023-10-01 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0009_userdetails_delete_userprofile1'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('sport_choice', models.CharField(blank=True, choices=[('basketball', 'Basketball'), ('swimming', 'Swimming'), ('chess', 'Chess')], max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
