from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from ...models.dictionaries.complaint_type import ComplaintType
from ...serializers.dictionaries.complaint_type_serializers import \
    ComplaintTypeSerializer


class ComplaintTypeViewSet(viewsets.ModelViewSet):
    queryset = ComplaintType.objects.all()
    serializer_class = ComplaintTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['label']
    ordering_fields = ['label']
