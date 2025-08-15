from rest_framework import serializers

from ...models.dictionaries.complaint_status import ComplaintStatus


class ComplaintStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintStatus
        fields = ["code", "label"]
