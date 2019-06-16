from django.contrib.auth.models import User as UserDjango
from rest_framework import serializers
from .models import User, Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True,
    )
    password = serializers.CharField(
        write_only=True,
    )
    permission = PermissionSerializer()

    class Meta:
        model = User
        fields = ('name', 'last_names', 'username', 'password', 'permission')

    def create(self, validated_data):
        permission_data = validated_data.pop('permission')

        django_user = UserDjango.objects.create(
            username=validated_data['username'],
            first_name=validated_data['name'],
            last_name=validated_data['last_names'],
        )

        django_user.set_password(validated_data['password'])
        django_user.save()

        permission = Permission.objects.get(
            name=permission_data['name'])

        instance = User.objects.create(
            name=validated_data['name'],
            last_names=validated_data['last_names'],
            permission=permission,
            django_user=django_user,
        )

        return instance
