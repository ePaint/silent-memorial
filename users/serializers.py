from rest_framework import serializers
from .models import User


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
