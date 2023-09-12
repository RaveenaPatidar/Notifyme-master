from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/login/', views.user_login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),
]