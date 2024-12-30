from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from telegram.utils.permissions import IsOwnerOrReadOnly
from .services import UserService
from rest_framework.views import APIView
from apps.users.models import User
from rest_framework.response import Response


class Index(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        return UserService.UserContacts(self, request)


class Store(APIView):
    def post(self, request):
        return UserService.RegisterUser(self, request)


class Show(APIView):
    def get(self, request, username):
        return UserService.UserDeatils(self, request, username)


class Update(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def patch(self, request, username):
        user = User.objects.get(username=username)
        self.check_object_permissions(request, user)
        return UserService.UpdateUser(self, request, user)


class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self, request, username):
        user = User.objects.get(username=username)
        self.check_object_permissions(request, user)
        return UserService.DeleteUser(self, request, user)


class DelUserImg(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self, request, username):
        user = User.objects.get(username=username)
        self.check_object_permissions(request, user)
        return UserService.DeleteUserImage(self, request, user)


class Search(APIView):
    def get(self, request):
        return UserService.SearchInUsers(self, request)
