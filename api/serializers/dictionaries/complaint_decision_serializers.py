from rest_framework import serializers

from ...models.dictionaries.complaint_decision import ComplaintDecision


class ComplaintDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintDecision
        fields = ["code", "label"]
