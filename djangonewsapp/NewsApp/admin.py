from django.contrib import admin
from .models import News,SportsNews,Place,Restaurant
# Register your models here.
admin.site.register(News)
admin.site.register(SportsNews)
admin.site.register(Place)
admin.site.register(Restaurant)