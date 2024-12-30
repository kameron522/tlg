from apps.users.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        if 'img' in validated_data and validated_data['img']:
            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
                img=validated_data['img'],
            )
        else:
            user = User(
                email=validated_data['email'],
                username=validated_data['username'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
