# Generated by Django 5.0.4 on 2024-05-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_vocabulary', '0003_alter_uservocabulary_external_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservocabulary',
            name='transcription',
            field=models.CharField(blank=True, null=True),
        ),
    ]