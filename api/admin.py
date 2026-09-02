from django.contrib import admin
from .models import Meal, Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ['meal', 'stars']
    list_filter = ['meal', 'stars']

class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    search_fields = ['title', 'description']
    
    

admin.site.register(Rating, RatingAdmin)
admin.site.register(Meal, MealAdmin)


