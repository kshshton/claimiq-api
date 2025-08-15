from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from ..models import Company
from ..serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['town', 'nip']
    search_fields = ['company_name', 'email']
    ordering_fields = ['company_name', 'town']

    @action(detail=True, methods=['post'])
    def upload_logo(self, request, pk=None):
        company = self.get_object()
        logo_file = request.FILES.get('logo')
        if logo_file:
            company.logo = logo_file.read()
            company.save()
            return Response({'message': 'Logo uploaded successfully'})
        return Response(
            {'error': 'Logo file is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
