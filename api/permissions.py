from rest_framework import serializers
from .models import Meal, Rating



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'



class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'







