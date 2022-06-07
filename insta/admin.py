from django.contrib import admin
from .models import Images,comments,likes,Profile

class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal = ('comments',)


admin.site.register(Images)
admin.site.register(likes)
admin.site.register(comments)
admin.site.register(Profile)

