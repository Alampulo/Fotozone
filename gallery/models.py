from django.db import models
from __future__ import unicode_literals

Default_desc = '''nothing that is good in life will ever come easy life is not an easy road,
fally lover,
n if u dunno now u know.
hustle .'''

class Category(models.Model):
    Name = models.CharField(max_length=30)
    @property
    def preview(self):
        first=self.images.last()
        return first.image.url
    def __str__(self):
        return self.Name

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place

class Image(models.Model):
    Name = models.CharField(max_length =60)
    description = models.TextField(default=Deafult_desc)
    category = models.ForeignKey(Category, related_name="images")
    location = models.ForeignKey(Location)
    submited = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

    @property
    def allinfo(self):
        info={
            'name':self.Name,
            'desc':self.description,
            'image':self.image.url,
            'id':self.id
        }
        return str(info)
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,Name=None,category=None):
        self.Name=Name if Name else self.Name
        self.category=category if category else self.category
        self.save()

    @classmethod
    def get_image_by_id(cls,id):
        return cls.objects.get(pk = id)

    @classmethod
    def search_image(cls,key):
        images = cls.objects.filter(cls(description__contains = key)|cls(Name__icontains = key)|cls(location__place__icontains = key))
        print(images)
        return images

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    class Meta:
        ordering = ['submited']
