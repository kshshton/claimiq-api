from rest_framework import serializers

from ...models.dictionaries.registration_unit import RegistrationUnit


class RegistrationUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationUnit
        fields = ["code", "label"]
