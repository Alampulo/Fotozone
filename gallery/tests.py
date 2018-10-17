from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category= Category(category = 'war')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
#         self.location= Location(location = 'westcoast')
        self.location.save_location()

        self.new_category = Category(category = 'legend')
        self.new_category.save(
