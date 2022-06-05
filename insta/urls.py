from django.urls import re_path,include
from . import views

urlpatterns=[
    # re_path(r'^$',views.index,name = 'welcome'),
    re_path('^$',views.profile_today,name='profileToday'),
    re_path(r'^search/', views.search_results, name='search_results'),
    ]


    