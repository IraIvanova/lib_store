# Generated by Django 5.0.4 on 2024-04-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0006_remove_customuser_language_preference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.CharField(blank=True, null=True),
        ),
    ]
