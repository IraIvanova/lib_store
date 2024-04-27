# Generated by Django 5.0.4 on 2024-04-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0005_remove_customuser_last_activity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='language_preference',
        ),
        migrations.AddField(
            model_name='customuser',
            name='interface_language',
            field=models.CharField(default='uk', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='learned_language',
            field=models.CharField(default='en', max_length=10),
        ),
    ]