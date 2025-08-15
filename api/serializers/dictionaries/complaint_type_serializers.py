from rest_framework import serializers

from ...models.dictionaries.complaint_type import ComplaintType


class ComplaintTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintType
        fields = ["code", "label"]
