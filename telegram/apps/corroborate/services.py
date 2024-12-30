from rest_framework.authtoken.models import Token
from telegram.utils.service_wrapper import service_wrapper


class AuthService:

    def LogoutUser(self, request):

        def action():
            token = Token.objects.get(user=request.user)
            return [token.delete(), 200]

        return service_wrapper(action)
