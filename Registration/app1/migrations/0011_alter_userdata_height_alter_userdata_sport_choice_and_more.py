# Generated by Django 4.2.4 on 2023-10-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_userdata_delete_userdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='sport_choice',
            field=models.CharField(blank=True, choices=[('basketball', 'Basketball'), ('swimming', 'Swimming'), ('Taekwondo', 'Taekwondo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='weight',
            field=models.FloatField(),
        ),
    ]
