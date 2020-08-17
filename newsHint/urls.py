"""newsHint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
# Data sourcing module
from news.views import UsersViewSet, NewsViewSet
from datasource.views import NewsCrawler

router_obj = routers.DefaultRouter()
router_obj.register(r'', UsersViewSet, basename='users')
router_obj.register(r'api/news', NewsViewSet, basename='news')
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router_obj.urls)),
    url(r'api/v1/scrap$', NewsCrawler.as_view(), name="scraper")
]
