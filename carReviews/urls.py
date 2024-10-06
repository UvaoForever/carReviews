"""
URL configuration for carReviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.db import router
from django.urls import path, include, re_path
from carReviews import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from carReviews.views import CountryViewSet, AutoViewSet, ProducerViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet, basename="countries")
router.register(r'producers', ProducerViewSet, basename="producers")
router.register(r'autos', AutoViewSet, basename="autos")
router.register(r'comments', CommentViewSet, basename="comments")

exports = [
    path("countries", views.parsing_countries),
    path("producers", views.parsing_producers),
    path("autos", views.parsing_autos),
    path("comments", views.parsing_comments)
]

urlpatterns = [
    path('admin/', admin.site.urls), # Админы
    path('', views.index), # Начальная страница
    path('api/', include(router.urls)), # Взаимодействие с таблицами
    path('api/export/', include(exports)), # Экспорт таблиц

    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
