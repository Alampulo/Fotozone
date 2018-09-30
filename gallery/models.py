from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 30)  

    @classmethod
    def filter_by_location(cls,name):
        location= cls.objects.filter(name = name) 
        return location      
    

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length = 60)
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 90)
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')