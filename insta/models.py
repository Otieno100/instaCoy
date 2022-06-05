from django.db import models
from cProfile import Profile
import datetime as dt


class Profile(models.Model) :
    name = models.CharField(blank=True, max_length=120)
    bio = models.CharField(max_length = 30)
    profile_image = models.ImageField(upload_to = 'image/',default = 'brian')

    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    def update_profile(self):
        self.update()
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']    

    def __str__(self):
      return self.name

class likes(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self) :
        return self.name 


class comments(models.Model):
    comment = models.CharField(max_length = 30)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) :
        return self.comment                 



class Images(models.Model):
    instagram_image = models.ImageField(upload_to = 'instagram/',default = 'brian')
    image_name = models.CharField(max_length = 60)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE )
    likes = models.ManyToManyField(likes)
    comments = models.ManyToManyField(comments)
  
    
  

    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        self.update()
    
    def get_image_by_id(self, id):
        pass
    

    @classmethod
    def todays_profile(cls):
        profile = dt.date.today()
        return profile
 

    @classmethod
    def search_by_image_name(cls,search_term):
            insta = cls.objects.filter(image_name__icontains=search_term)
            return insta    
            