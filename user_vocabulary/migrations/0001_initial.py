# Generated by Django 5.0.4 on 2024-05-08 12:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('locale', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserVocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=50)),
                ('translation', models.CharField()),
                ('image', models.CharField()),
                ('examples', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_word_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'external_id', 'language')},
            },
        ),
    ]
