from rest_framework import serializers
from user_app.models import User


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Passwords must match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # remove confirm field
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=User.EMPLOYEE  # Default role
        )
        user.set_password(validated_data['password'])  # hash password
        user.save()
        return user
