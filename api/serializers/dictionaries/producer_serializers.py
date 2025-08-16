from rest_framework import serializers

from ...models.dictionaries.producer import Producer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
