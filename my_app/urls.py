from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [

    path('', views.Indexview.as_view()),
    path('add2/', views.Addview.as_view()),
    path('update2/<int:id>/', views.Updateview.as_view()),
    path('delete2/<int:id>/', views.Deleteview.as_view()),

]
