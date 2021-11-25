import uuid as uuid
from django.db import models


class Restaurant(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=64)
