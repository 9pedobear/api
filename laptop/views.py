from django.db.models import query
from rest_framework import generics, permissions
from .serializers import *
from .models import Laptop
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class LaptopCreateView(generics.CreateAPIView):
    serializer_class = LaptopAllSerializers
    permission_classes = (IsAuthenticated, IsAdminUser)

class LaptopListView(generics.ListAPIView):
    serializer_class = LaptopAllSerializers
    queryset = Laptop.objects.all()
    permission_classes = (IsAuthenticated,)

class LaptopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LaptopAllSerializers
    queryset = Laptop.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
