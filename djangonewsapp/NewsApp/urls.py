from django.urls import path,include
from .views import News,Home,Latest
urlpatterns = [
    path('news/',News,name='News'),
    path('home/',Home,name='Home'),
    path('latest/',Latest,name='Latest')
]