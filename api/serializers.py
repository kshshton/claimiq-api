from rest_framework import serializers

from .models import ActionHistory, Company, Complaint, Producer, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'surname', 'role', 'last_activity']
        read_only_fields = ['last_activity']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'surname', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ['submit_date']


class ActionHistorySerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='email.email', read_only=True)

    class Meta:
        model = ActionHistory
        fields = '__all__'
        read_only_fields = ['date']
