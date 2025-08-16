from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from ..models.dictionaries.producer import Producer
from ..serializers.dictionaries.producer_serializers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
