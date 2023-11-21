from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('passwordchange/', views.passwordreset, name='passwordchange'),
    path('passwordchange2/', views.passwordreset2, name='passwordchange2'),
    path('logout/', views.userlogout, name='logout'),
]
