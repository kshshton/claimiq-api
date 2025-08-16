from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from ...models.dictionaries.complaint_status import ComplaintStatus
from ...serializers.dictionaries.complaint_status_serializers import \
    ComplaintStatusSerializer


class ComplaintStatusViewSet(viewsets.ModelViewSet):
    queryset = ComplaintStatus.objects.all()
    serializer_class = ComplaintStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['label']
    ordering_fields = ['label']
