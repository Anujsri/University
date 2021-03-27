import uuid

from django.db import models


class Instructor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=256)
    address = models.TextField(null=True,blank=True)
    pf_number = models.TextField(unique=True,default='')
    email = models.TextField(null=True,blank=True)
    mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
