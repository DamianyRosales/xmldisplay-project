from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user_id)

class Tab(models.Model):
    month = models.CharField(max_length=255)
    year = models.IntegerField()
    food = models.IntegerField()
    brewery = models.IntegerField()
    chemical_products  = models.IntegerField()
    other_manufactures = models.IntegerField()
    textiles_leather = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        name = str(self.year) + '-' + str(self.month)
        return name
