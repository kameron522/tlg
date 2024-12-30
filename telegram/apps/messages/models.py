from django.db import models
from apps.users.models import User


class Message(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name='messages')
    txt = models.CharField(max_length=2056, null=True, blank=True)
    img = models.ImageField(
        upload_to='messages_images/', null=True, blank=True)
    receiver_id = models.PositiveBigIntegerField(null=True, blank=True)
    in_replay_to_msg_id = models.PositiveBigIntegerField(default=0)
    modified_at = models.DateTimeField(auto_now_add=True)
