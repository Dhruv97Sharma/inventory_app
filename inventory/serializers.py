from rest_framework import serializers
from .models import Item, Category

class CategoryOutputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=100)

class ItemOutputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    number_in_stock = serializers.IntegerField(default=0)
    description = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=100)
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    extra_fields = serializers.JSONField()