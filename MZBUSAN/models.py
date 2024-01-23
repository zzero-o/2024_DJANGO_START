from django.db import models

# Create your models here.

class Food (models.Model) :
    img_path = models.CharField(max_length = 255)
    type = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    score = models.FloatField()
    price = models.IntegerField()

    def __str__(self) :
        return self.name

class Local (models.Model) :
    name = models.CharField(max_length = 50)
    img_path = models.CharField(max_length = 255)

    def __str__(self) :
        return self.name
    

