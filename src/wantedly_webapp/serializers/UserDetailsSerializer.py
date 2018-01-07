from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class DetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', )