from django.contrib import admin
from django.urls import include, re_path
from django.contrib.auth import views

urlpatterns = [
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'',include('insta.urls')),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^logout/$', views.LogoutView.as_view(), {"next_page": '/'}),
]
