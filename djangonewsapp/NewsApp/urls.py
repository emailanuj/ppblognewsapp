from django.urls import path,include
from .views import News
urlpatterns = [
    path('',News,name='News')
]