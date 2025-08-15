from rest_framework import serializers

from ..models import Complaint, ComplaintDecision, ComplaintStatus


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ['submit_date']


class ComplaintStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintStatus
        fields = ["label"]


class ComplaintDecisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintDecision
        fields = ["label"]
