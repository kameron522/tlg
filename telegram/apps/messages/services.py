from .serializers import MessageSerializer
from .models import Message
from apps.users.models import User
from telegram.utils.service_wrapper import service_wrapper
from telegram.utils import img_delete
from django.db.models import Q


class MessageService:

    def UserMessages(self, request):

        def action():
            messages = Message.objects.filter(
                user=request.user) | Message.objects.filter(receiver_id=request.user.id)
            srz_data = MessageSerializer(instance=messages, many=True)
            return [srz_data.data, 200]

        return service_wrapper(action)

    def SendMessage(self, request, username):

        def action():
            if not (('txt' in request.data and request.data['txt']) or ('img' in request.data and request.data['img'])):
                return ["you cant send an empty message", 422]
            if ('txt' in request.data and not request.data['txt']):
                request.data['txt'] = None

            srz_data = MessageSerializer(data=request.data)
            if srz_data.is_valid():
                receiver = User.objects.get(username=username)
                srz_data.save(user=request.user, receiver_id=receiver.id)
                return [srz_data.data, 200]
            return [srz_data.errors, 422]

        return service_wrapper(action)

    def EditMessage(self, request, message):

        def action():
            if not (('txt' in request.data and request.data['txt']) or ('img' in request.data and request.data['img'])):
                return ["you cant send an empty message", 422]
            if ('txt' in request.data and not request.data['txt']):
                request.data['txt'] = None

            srz_data = MessageSerializer(
                instance=message, data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return [srz_data.data, 200]
            return [srz_data.errors, 422]

        return service_wrapper(action)

    def DeleteMessage(self, request, message):

        def action():
            img_delete.perform(message)
            return [message.delete(), 200]

        return service_wrapper(action)

    def DeleteMessageImage(self, request, message):

        def action():
            return [img_delete.perform(message), 200]

        return service_wrapper(action)

    def ReplayMessage(self, request, message):

        def action():
            if (request.user != message.user) and (request.user.id != message.receiver_id):
                return ["access denied!", 403]
            srz_data = MessageSerializer(data=request.data, insctance=message)
            if srz_data.is_valid():
                srz_data.save(user=request.user,
                              in_replay_to_msg_id=message.id)
                return [srz_data.data, 200]
            return [srz_data.errors, 422]

        return service_wrapper(action)

    def SearchInMessages(self, request):

        def action():
            search_phrase = request.GET.get('q')
            result = Message.objects.filter(
                (Q(user=request.user) | Q(receiver_id=request.user)),
                txt__contains=search_phrase.lower()
            )
            srz_data = MessageSerializer(instance=result, many=True)
            return [srz_data.data, 200]

        return service_wrapper(action)

    def ShowChats(self, request, username):

        def action():
            destination_user = User.objects.get(username=username)
            messages = Message.objects.filter(receiver_id=destination_user.id, user=request.user) | Message.objects.filter(
                receiver_id=request.user.id, user=destination_user)
            messages = messages.order_by('modified_at')
            srz_data = MessageSerializer(instance=messages, many=True)
            return [srz_data.data, 200]
        return service_wrapper(action)
