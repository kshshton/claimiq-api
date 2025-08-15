from rest_framework import serializers

from ..models import ActionHistory


class ActionHistorySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='email.email', read_only=True)

    class Meta:
        model = ActionHistory
        fields = '__all__'
        read_only_fields = ['date']
