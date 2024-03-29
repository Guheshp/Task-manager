from django.db import models
from django.urls import path 
from . import views

urlpatterns = [
    
    # ----------------------- Home page -------------------------- #
    # --------------------------------------------------------------- #
    path('', views.home, name=""),
    
    # -----------------------Signup a user -------------------------- #
    # --------------------------------------------------------------- #
    
    path('signup',views.Signup,name='my-signup'),
    
    # -----------------------Signin a user -------------------------- #
    # --------------------------------------------------------------- #
   
    path('signin', views.Signin, name='my-signin'),

    #-----------------------Dashboard ------------------------------- #
    # --------------------------------------------------------------- #

    path('dashboard', views.Dashboard, name='my-dashboard'),

    #-----------------------Create a Task ------------------------------- #
    # --------------------------------------------------------------- #

    path('create-task', views.CreateTask, name='my-task'),

    #-----------------------Read a Task ------------------------------- #
    # --------------------------------------------------------------- #

    path('view-task', views.ViewTask, name='my-Viewtask'),

    #-----------------------Update a Task ------------------------------- #
    #-
    # --------------------------------------------------------------- #

    path('update-task/<str:pk>/', views.UpdateTask, name='my-updatetask'),

    #-----------------------Delete a Task ------------------------------- #
    #---------------------------------------------------------------- #

    path('delete-task/<str:pk>/', views.DeleteTask, name='my-deletetask'),

    #-----------------------Profile-management -------------------------- #
    #---------------------------------------------------------------- #

    path('profile-management', views.Profile_Management, name='my-profilemanagement'),

    #----------------------- Delete-Profile -------------------------- #
    #---------------------------------------------------------------- #

    path('delete-account', views.DeleteAccount, name='my-deleteaccount'),
    

    # -----------------------Signout a user ------------------------ #
    # --------------------------------------------------------------- #
  
    path('signout', views.Signout, name='my-signout'),


]