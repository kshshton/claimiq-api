from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from ...models.dictionaries.registration_unit import RegistrationUnit
from ...serializers.dictionaries.registration_unit_serializers import \
    RegistrationUnit


class RegistrationUnitViewSet(viewsets.ModelViewSet):
    queryset = RegistrationUnit.objects.all()
    serializer_class = RegistrationUnit
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['label']
    ordering_fields = ['label']
