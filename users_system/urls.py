from django.urls import path

from users_system import views

urlpatterns = [
    path('register/', views.register_page, name='register')
]