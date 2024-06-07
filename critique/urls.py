from django.urls import path, include
from .views import ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]