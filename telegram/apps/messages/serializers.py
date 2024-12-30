from rest_framework.serializers import ModelSerializer
from .models import Message
from apps.users.models import User
from .models import Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
