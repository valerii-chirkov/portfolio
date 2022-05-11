from django.db import router
from rest_framework.routers import DefaultRouter
from offers.views import OfferViewSet


router = DefaultRouter()
router.register('offers', OfferViewSet, basename='offers')

urlpatterns = router.urls