from rest_framework import generics
from . import models, serializers, permissions

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render

class PlaceList(generics.ListCreateAPIView):
    serializer_class = serializers.PlaceSerializer

    def get_queryset(self):
        return models.Places.objects #return models.Places.objects.filter(owner_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryList(generics.ListCreateAPIView):#CreateAPIView):
  permission_classes = [permissions.IsOwnerOrReadOnly]
  serializer_class = serializers.CategorySerializer

  def get_queryset(self):
      return models.Category.objects  # return models.Places.objects.filter(owner_id=self.request.user.id)

  def perform_create(self, serializer):
      serializer.save(owner=self.request.user)

class CategoryDetail(generics.UpdateAPIView, generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsOwnerOrReadOnly]
  serializer_class = serializers.CategorySerializer
  queryset = models.Category.objects.all()

class MenuItemList(generics.CreateAPIView):
  permission_classes = [permissions.CategoryOwnerOrReadOnly]
  serializer_class = serializers.MenuItemSerializer

class MenuItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
  permission_classes = [permissions.CategoryOwnerOrReadOnly]
  serializer_class = serializers.MenuItemSerializer
  queryset = models.MenuItem.objects.all()

def home(request):
  return render(request, 'index.html')





















