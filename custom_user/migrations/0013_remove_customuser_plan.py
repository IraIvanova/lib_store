# Generated by Django 5.0.4 on 2024-05-11 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0012_alter_customuser_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='plan',
        ),
    ]