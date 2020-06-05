# from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('fish', views.FishViewSet, basename='get-fishes')

urlpatterns = router.urls
