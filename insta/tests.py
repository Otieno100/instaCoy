# from django.test import TestCase
from unicodedata import name
from django.test import TestCase
from .models import Profile, Images, comments, likes


class ProfileTestClass(TestCase):
     """
    defining testcase for User class
    """
     def setUp(self):
         self.Brian = Profile(name = "Brian",bio = "kenyan born")

     def test_instance(self) :
         self.assertTrue(isinstance(self.Brian,Profile)) 

     
     def test_save_method(self):
        self.Brian.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)   

class likesTestClass(TestCase):
    """
     defining test for Likes class
    """
    def setUp(self):
        """
        Creating a new instance of the Likes class
        """
        self.likes =likes(True)
        self.likes.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.likes, likes))

    def test_save_method(self):
        like = likes.objects.all()
        self.assertTrue(len(like) > 0)


class commentsTestClass(TestCase):
    """
     defining test for comments class
    """
    def setUp(self):
        """
        Creating a new instance of the comments class
        """
        self.comments =comments(name = 'comments')
        self.comments.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.comments, comments))

    def test_save_method(self):
        comment = comments.objects.all()
        self.assertTrue(len(comment) > 0)        