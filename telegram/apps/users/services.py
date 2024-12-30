from .serializers import UserSerializer
from .models import User
from django.contrib.auth.hashers import make_password
from telegram.utils.service_wrapper import service_wrapper
from telegram.utils import img_delete
from django.db.models import Q


class UserService:

    def UserContacts(self, request):

        def action():
            return True
        return True

    def RegisterUser(self, request):

        def action():
            srz_data = UserSerializer(data=request.data)
            if srz_data.is_valid():
                if 'password_confirmation' not in request.data:
                    return ["password confirmation is required", 422]
                if (request.data['password'] != request.data['password_confirmation']):
                    return ["passwords must match", 422]
                srz_data.save()
                return [srz_data.data, 200]
            return [srz_data.errors, 422]

        return service_wrapper(action)

    def UserDeatils(self, request, username):

        def action():
            user = User.objects.get(username=username)
            srz_data = UserSerializer(instance=user)
            return [srz_data.data, 200]

        return service_wrapper(action)

    def UpdateUser(self, request, user):

        def action():
            srz_data = UserSerializer(
                instance=user, data=request.data, partial=True)
            if srz_data.is_valid():
                srz_data.save()
                return [srz_data.data, 200]
            return [srz_data.errors, 422]

        return service_wrapper(action)

    def DeleteUser(self, request, user):

        def action():
            img_delete.perform(user)
            return [user.delete(), 200]

        return service_wrapper(action)

    def DeleteUserImage(self, request, user):

        def action():
            return [img_delete.perform(user), 200]

        return service_wrapper(action)

    def SearchInUsers(self, request):

        def action():
            search_phrase = (request.GET.get('q')).lower()
            results = User.objects.filter(username__contains=search_phrase) | User.objects.filter(
                name__contains=search_phrase)
            srz_data = UserSerializer(instance=results, many=True)
            return [srz_data.data, 200]

        return service_wrapper(action)
