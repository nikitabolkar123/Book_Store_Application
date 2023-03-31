from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
