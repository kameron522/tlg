# Generated by Django 5.1.4 on 2024-12-29 22:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(blank=True, max_length=2056, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='messages_images/')),
                ('receiver_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('in_replay_to_msg_id', models.PositiveBigIntegerField(default=0)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
