from .models import Customer, Product, File
from rest_framework import serializers
from django.contrib.auth.models import User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'rut', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['product', 'image']


class ProductSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'product_id',
            'product_name',
            'description',
            'price',
            'available_quantity',
            'files',
            'status',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
