from rest_framework import serializers

from ...models.dictionaries.action_type import ActionType


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = ["code", "label"]
