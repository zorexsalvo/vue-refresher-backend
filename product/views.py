from django.shortcuts import render
from rest_framework import viewsets

from .models import Product, Manufacturer
from .serializers import ProductSerializer, ManufacturerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
