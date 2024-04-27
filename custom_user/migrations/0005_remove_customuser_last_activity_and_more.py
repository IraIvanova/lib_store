# Generated by Django 5.0.4 on 2024-04-19 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_customuser_language_preference_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='last_activity',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last name'),
        ),
    ]
