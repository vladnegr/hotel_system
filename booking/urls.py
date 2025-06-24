from django.urls import path

from booking import views

urlpatterns = [
    path('', views.main_page, name='main'),

]