from django.contrib import admin
from django.urls import path
from Academy import views

urlpatterns = [

    path('', views.Index.as_view()),
    path('add/', views.Add.as_view()),
    path('update/<int:id>/', views.Update.as_view()),
    path('delete/<int:id>/', views.Delete.as_view()),

]
