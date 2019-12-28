from django.db import models

# Create your models here.
class News(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.author
    

class SportsNews(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.author
        
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
