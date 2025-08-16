from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from ...models.dictionaries.complaint_decision import ComplaintDecision
from ...serializers.dictionaries.complaint_decision_serializers import \
    ComplaintDecisionSerializer


class ComplaintDecisionViewSet(viewsets.ModelViewSet):
    queryset = ComplaintDecision.objects.all()
    serializer_class = ComplaintDecisionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['label']
    ordering_fields = ['label']
