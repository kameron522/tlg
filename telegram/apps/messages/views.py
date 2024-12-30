from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from telegram.utils.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from .services import MessageService
from .models import Message


class Index(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        return MessageService.UserMessages(self, request)


class Store(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, username):
        return MessageService.SendMessage(self, request, username)


class Update(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def patch(self, request, message_id):
        message = Message.objects.get(id=message_id)
        self.check_object_permissions(request, message)
        return MessageService.EditMessage(self, request, message)


class Destroy(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self, request, message_id):
        message = Message.objects.get(id=message_id)
        self.check_object_permissions(request, message)
        return MessageService.DeleteMessage(self, request, message)


class DelMsgImg(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self, request, message_id):
        message = Message.objects.get(id=message_id)
        self.check_object_permissions(request, message)
        return MessageService.DeleteMessageImage(self, request, message)


class Replay(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, requset, message_id):
        message = Message.objects.get(id=message_id)
        return MessageService.ReplayMessage(self, requset, message)


class Search(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        return MessageService.SearchInMessages(self, request)


class Chat(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, username):
        return MessageService.ShowChats(self, request, username)
