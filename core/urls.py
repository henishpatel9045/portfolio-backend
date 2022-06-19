from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("site", views.SiteInfoView, basename="SiteInfo ViewSet")
router.register("message", views.ContactViewSet, basename="Contact Me Viewset")

urlpatterns = router.urls
