from django.db import models
from cProfile import Profile

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

        return self.text                  



class Images(models.Model):
    instagram_image = models.ImageField(upload_to = 'image/',default = 'brian')
    image_name = models.CharField(max_length = 60)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE )
    likes = models.ManyToManyField(likes)

            