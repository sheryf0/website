# this is a custom url file to handle anything related to registration, login and landing page

from django.urls import path
from welcome import views
from django.contrib.auth import views as auth_views
# im just trying to import the follow comme authentication system to run my forgotten password

urlpatterns = [
    path('', views.landing_page, name="home"),
  
]