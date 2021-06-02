from django.contrib import admin
from django.urls import path
from .views import SignUpView
from . import views


urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('editprofile/<str:pk_test>/', views.EditProfile, name='editprofile'),
    path('login/', views.loginPage, name='login'),
    path('/', views.loginPage, name='home'),
    #path('createprofile/', views.CreateProfile, name='createprofile'),
    path('logout/', views.logoutUser, name="logout"),
    path('courselist/',views.CourseList,name="courselist"),
    path('<str:course_id>/',views.Rate ,name='rate'),

]
