from django.db import models


def upload_to(instance, filename):
    return f"{instance.type}/{filename}"


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_to)
    type = models.CharField(max_length=255, default='files')
    created_at = models.DateTimeField(auto_now_add=True)
