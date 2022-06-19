from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("site", views.SiteInfoView, basename="SiteInfo ViewSet")

urlpatterns = router.urls
