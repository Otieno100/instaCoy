from django.conf import settings
from django.urls import re_path,include
from . import views
from django.conf.urls.static import static

urlpatterns=[
    # re_path(r'^$',views.index,name = 'welcome'),
    re_path('^$',views.profile_today,name='profileToday'),
    re_path(r'^search/', views.search_results, name='search_results'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    