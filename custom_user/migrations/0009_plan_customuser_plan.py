# Generated by Django 5.0.4 on 2024-05-10 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0008_alter_customuser_interface_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('desc', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        )
    ]
