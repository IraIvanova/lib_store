# Generated by Django 5.0.4 on 2024-05-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0007_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='interface_language',
            field=models.CharField(default='Ukrainian', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='learned_language',
            field=models.CharField(default='English', max_length=10),
        ),
    ]
