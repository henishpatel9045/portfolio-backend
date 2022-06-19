from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from . import models, serializers

# Create your views here.

class SiteInfoView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = models.SiteInfo.objects.all()
    serializer_class = serializers.SiteInfoSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    
