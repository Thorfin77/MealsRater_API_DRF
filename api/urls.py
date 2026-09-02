from rest_framework import routers
from .views import MealViewSets, RatingViewSets
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'meals', MealViewSets, 'meal')
router.register(r'rating', RatingViewSets, 'rating')

urlpatterns = [
    path('', include(router.urls)),
]



