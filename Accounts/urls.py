from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('login', views.login),
    path('registration', views.registration),
    path('register', views.register),
    path('logout', views.logout),
    path('my_account', views.my_account),
    # Dashboard might need to be moved to the treasure app
    path('dashboard', views.dashboard),
]