from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseClass(models.Model):
    uid = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    # users = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user-user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    