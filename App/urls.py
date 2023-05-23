from  django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('extract/', views.extract_text, name='extract_text'),
]