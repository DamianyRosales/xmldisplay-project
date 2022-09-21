from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user_id)
    
