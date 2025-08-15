from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from ..models import Complaint
from ..models.dictionaries.complaint_status import ComplaintStatus
from ..serializers import ComplaintSerializer


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['type', 'status', 'submit_date']
    search_fields = ['number']
    ordering_fields = ['submit_date', 'exit_date', 'number']

    @action(detail=True, methods=['post'])
    def close_complaint(self, request, pk=None):
        complaint = self.get_object()
        complete_status = ComplaintStatus.objects.get(code="complete")
        complaint.status = complete_status
        complaint.save()
        return Response({'message': 'Complaint closed successfully'})

    @action(detail=True, methods=['post'])
    def reopen_complaint(self, request, pk=None):
        complaint = self.get_object()
        not_started_status = ComplaintStatus.objects.get(code="not_started")
        complaint.status = not_started_status
        complaint.save()
        return Response({'message': 'Complaint reopened successfully'})
