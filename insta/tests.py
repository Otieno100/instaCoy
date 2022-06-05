# from django.test import TestCase
from unicodedata import name
from django.test import TestCase
from .models import Profile, Image, comments, likes


class ProfileTestClass(TestCase):
     """
    defining testcase for User class
    """
     def setUp(self):
         self.brian = Profile(name)

     def test_instance(self) :
         self.assertTrue(isinstance(self.brian,Profile)) 

     
     def test_save_method(self):
        self.brian.save_profile()
        Profiles = Profile.objects.all()
        self.assertTrue(len(Profiles) > 0)   
