from django.contrib import admin
from .models import Images,comments,likes,Profile

admin.site.register(Images)
admin.site.register(likes)
admin.site.register(comments)
admin.site.register(Profile)

