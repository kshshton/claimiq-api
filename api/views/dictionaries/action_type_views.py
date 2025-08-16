from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from ...models.dictionaries.action_type import ActionType
from ...serializers.dictionaries.action_type_serializers import \
    ActionTypeSerializer


class ActionTypeViewSet(viewsets.ModelViewSet):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['label']
    ordering_fields = ['label']
