# from django.shortcuts import render

from rest_framework import generics

from .models import Made254
from .serializers import Made254Serializer

# Create your views here.
class ListMade254(generics.ListAPIView):
    queryset = Made254.objects.all()
    serializer_class = Made254Serializer

class DetailMade254(generics.RetrieveAPIView):
    queryset = Made254.objects.all()
    serializer_class = Made254Serializer
