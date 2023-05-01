from rest_framework import serializers
from djoser.serializers import UserCreatePasswordRetypeSerializer
from .models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()


class UserCreateSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = User
        fields = ('user_id', 'email', 'password', 'first_name', 'last_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id', 'create_date', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser',
            'modified_date', 'last_login_date'
        )

        read_only_fields = (
            'user_id', 'create_date', 'is_active', 'is_staff', 'is_superuser', 'modified_date', 'last_login_date'
        )
