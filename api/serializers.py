from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = [
        #     "username",
        #     "is_superuser",
        #     "is_staff",
        #     "first_name",
        #     "last_name",
        #     "email",
        #     "date_joined",
        #     "groups",
        # ]
        fields = "__all__"
