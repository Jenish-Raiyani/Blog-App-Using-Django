from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path('register/', views.registerPage, name='register'),
     path('login/', views.loginPage, name='login'),
      path('logout/', views.logoutUser, name='logout'),

      path('blogs/', views.blogs,name="blogs"),
      path('blogpost/<int:id>', views.blogpost,name="blogpost"),
      path('contact/', views.contact,name="contact"),
 
]
