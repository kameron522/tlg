from django.shortcuts import render
from .services import AuthService
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class Destroy(APIView):
    permission_classes = [IsAuthenticated,]

    def delete(self, request):
        return AuthService.LogoutUser(self, request)
