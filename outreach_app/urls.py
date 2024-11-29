# outreach_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'), 
    path('admindashboard', views.admindashboard, name='dashboard'), 
    path('a', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('community_feedback/', views.community_feedback, name='community_feedback'),
    # Other paths...
]
