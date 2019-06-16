# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Permission
from .serializers import UserSerializer, PermissionSerializer

# Create your views here.


class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({"user": serializer.data,
                             "detail": "Usuario creado con éxito"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": serializer.errors},
                            status=status.HTTP_409_CONFLICT)


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
