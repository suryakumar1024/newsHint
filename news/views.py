from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import render
from news.models import News
from news.serializers import UserSerializer, NewsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
