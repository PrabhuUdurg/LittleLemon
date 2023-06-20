from django.shortcuts import render
from rest_framework import views, generics


# Create your views here.
class MenuItemView(views.APIView):
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    