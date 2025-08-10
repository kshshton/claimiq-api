from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from .models import ActionHistory, Company, Complaint, Producer, User
from .serializers import (ActionHistorySerializer, CompanySerializer,
                          ComplaintSerializer, ProducerSerializer,
                          UserCreateSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['role']
    search_fields = ['email', 'first_name', 'surname']
    ordering_fields = ['email', 'last_activity']

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    @action(detail=True, methods=['post'])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset successfully'})
        return Response(
            {'error': 'New password is required'},
            status=status.HTTP_400_BAD_REQUEST
        )


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


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


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
        complaint.status = 'closed'
        complaint.save()
        return Response({'message': 'Complaint closed successfully'})

    @action(detail=True, methods=['post'])
    def reopen_complaint(self, request, pk=None):
        complaint = self.get_object()
        complaint.status = 'open'
        complaint.save()
        return Response({'message': 'Complaint reopened successfully'})


class ActionHistoryViewSet(viewsets.ModelViewSet):
    queryset = ActionHistory.objects.all()
    serializer_class = ActionHistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['action', 'date', 'email']
    search_fields = ['details']
    ordering_fields = ['date', 'action']

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'])
    def user_actions(self, request):
        user_email = request.query_params.get('email')
        if user_email:
            actions = ActionHistory.objects.filter(email__email=user_email)
            serializer = self.get_serializer(actions, many=True)
            return Response(serializer.data)
        return Response(
            {'error': 'Email parameter is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
