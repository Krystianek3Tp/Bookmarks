from django.urls import path
from Account import views

urlpatterns = {
    path('login/', views.user_login, name = "login"),
}