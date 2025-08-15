from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from ..models import ActionHistory
from ..serializers import ActionHistorySerializer


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
