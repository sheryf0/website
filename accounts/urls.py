from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register ,name="register"),
    path('login/', views.login_view, name= "login"),
    path('logout/', views.logout_view, name="logout"),
    path('display_profile', views.display_info, name="display_profile"),
    path('edit_account/<int:id>', views.edit_profile, name="edit_profile")
]
